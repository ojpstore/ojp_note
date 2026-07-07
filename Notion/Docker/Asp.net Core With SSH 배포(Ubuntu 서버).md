---
base: "[[Docker.base]]"
최종 편집 일시: 2024-09-26T19:58:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 순서 (Ubuntu 기준)
    - ssh key 생성
```plain text
ssh-keygen -t rsa -b 4096
```
    - 해당 계정 폴더
        - /계정/.ssh/authorized_keys 파일에 공개키 추가
![[Untitled.png]]
    - GitHub 리파토리의 ACTIONS - SECRET 에 비밀키 추가
        - /계정/.ssh/id_rsa
```plain text
-----BEGIN OPENSSH PRIVATE KEY-----
.....
-----END OPENSSH PRIVATE KEY-----
```
![[Untitled 1.png]]

    - /etc/systemd/system/core-api.service 생성 후 내용 작성
        - 배포 폴더 경로 : /home/api/core-api
```javascript
[Unit]
Description=Example .NET Web API App running on Linux

[Service]
WorkingDirectory=/home/api/core-api
ExecStart=/usr/bin/dotnet /home/api/core-api/app-backend-core.dll
Restart=always
# Restart service after 10 seconds if the dotnet service crashes:
RestartSec=10
KillSignal=SIGINT
SyslogIdentifier=dotnet-example
User=www-data
Environment=ASPNETCORE_ENVIRONMENT=Production
Environment=DOTNET_NOLOGO=true

[Install]
WantedBy=multi-user.target
```

    - 생성한 core-api.service  서비스 등록 (시작시 실행 추가)
```javascript
chmod 755 core-api.service

systemctl daemon-reload
systemctl enable core-api.service
systemctl start core-api.service
```

- Gitea Action - publish.yml
```yaml
name: scp files

on:
  push:
    branches: [main]

jobs:
  build:
    name: Build
    runs-on: ubuntu-latest
    steps:
      - name: 빌드
        uses: appleboy/ssh-action@v1.0.3
        with:
          host: ${{secrets.SSH_HOST}}
          username: ${{secrets.SSH_USERNAME}}
          # password: ${{secrets.SSH_PASSWORD}}
          port: ${{secrets.SSH_PORT}}
          # =========================================================
          # 1) 배포서버의 비밀키 (GITHUB ACTIONS - SECRET)에 추가
          # -----BEGIN OPENSSH PRIVATE KEY-----
          # .....
          # -----END OPENSSH PRIVATE KEY-----
          # =========================================================
          # 2) 배포서버의 공개키는 배포서버의 authorized_keys 에 추가
          # =========================================================
          key: ${{secrets.SSH_KEY}}
          script: |
            cd /home/git/core-api
            git pull origin main
            dotnet build
      - name: 배포
        uses: appleboy/ssh-action@v1.0.3
        with:
          host: ${{secrets.SSH_HOST}}
          username: ${{secrets.SSH_USERNAME}}
          # password: ${{secrets.SSH_PASSWORD}}
          port: ${{secrets.SSH_PORT}}
          # =========================================================
          # 1) 배포서버의 비밀키 (GITHUB ACTIONS - SECRET)에 추가
          # -----BEGIN OPENSSH PRIVATE KEY-----
          # .....
          # -----END OPENSSH PRIVATE KEY-----
          # =========================================================
          # 2) 배포서버의 공개키는 배포서버의 authorized_keys 에 추가
          # =========================================================
          key: ${{secrets.SSH_KEY}}
          script: |
            cd /home/git/core-api
            systemctl stop core-api.service
            rm -rf /home/api/core-api/*
            dotnet publish -c Release -o /home/api/core-api
            systemctl start core-api.service

      - name: 메일 발송
        if: always()
        # 관련주소 : https://github.com/dawidd6/action-send-mail
        uses: dawidd6/action-send-mail@v3
        with:
          server_address: smtp.gmail.com
          # Server port, default 25:
          server_port: 465
          # Optional whether this connection use TLS (default is true if server_port is 465)
          secure: true
          # Optional (recommended) mail server username:
          username: ${{secrets.MAIL_USERNAME}}
          # Optional (recommended) mail server password:
          password: ${{secrets.MAIL_PASSWORD}}
          from: ${{ secrets.MAIL_USERNAME }}
          to: ${{ secrets.MAIL_USERNAME }}
          subject: ${{ gitea.repository }} Action 작업 결과
          priority: high
          convert_markdown: true
          attachments: ./README.md
          body: |
            ==========
            🌟 정보
            ==========
            "The job was automatically triggered by a ${{ gitea.event_name }} event."
            "This job is now running on a ${{ runner.os }} server hosted by Gitea!"
            "The name of your branch is ${{ gitea.ref }} and your repository is ${{ gitea.repository }}."
            "The ${{ gitea.repository }} repository has been cloned to the runner."
            "The workflow is now ready to test your code on the runner."

            ==========
            🌟 메세지
            ==========
            [${{ gitea.repository }}] Repository
            의 Action 작업이 ${{ job.status }} 되었습니다.


```

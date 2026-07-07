---
notion-id: b9394506-0259-4d31-97bd-1a70fdfc93cb
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/Next.js With SSH 배포 (Ubuntu 서버)]]"
최종 편집 일시: 2024-09-26T19:59:00
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
![[Untitled 3.png]]
    - GitHub 리파토리의 ACTIONS - SECRET 에 비밀키 추가
        - /계정/.ssh/id_rsa
```plain text
-----BEGIN OPENSSH PRIVATE KEY-----
.....
-----END OPENSSH PRIVATE KEY-----
```
![[Untitled 4.png]]

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
      - name: SSH Remote Commands
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
            cd /home/app/next-app
            rm -rf .next
            git pull origin main
            yarn install
            yarn build:prod
            pm2 delete next-app
            pm2 start "yarn start" --name next-app

      - name: Send mail
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
            [${{ gitea.repository }}] Repository 의 Action 작업이 ${{ job.status }} 되었습니다.

```
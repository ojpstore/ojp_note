---
base: "[[Docker.base]]"
최종 편집 일시: 2024-03-21T16:01:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
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
      - name: execute remote ssh
        uses: appleboy/ssh-action@master
        with:
          host: 호스트
          username: 아이디
          password: 비밀번호
          port: 3322
          script: |
            whoami
            cd /home/app/next-app
            rm -rf .next
            git pull origin main
            yarn install
            yarn build:prod
            pm2 delete next-app
            pm2 start "yarn start" --name next-app            

      - name: Send mail
        # 관련주소 : https://github.com/dawidd6/action-send-mail
        uses: https://github.com/dawidd6/action-send-mail@v3
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
            👉 from gitea    
```
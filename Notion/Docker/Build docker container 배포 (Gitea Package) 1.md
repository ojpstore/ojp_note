---
notion-id: a051723b-2626-4caf-aac2-63a1ba1b3c32
base: "[[Docker.base]]"
최종 편집 일시: 2024-03-26T10:57:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
```docker
name: Build docker container (Gitea Package)
on:
  push:
    branches:
      - main

jobs:
  build:
    name: Build image
    runs-on: ubuntu-latest
    container:
      image: catthehacker/ubuntu:act-latest # The Docker image to use as the container
    # strategy: # Strategy for the job execution
    #   matrix: # Allows running jobs with different variations
    #     arch: [amd64, arm64] # Variations of architecture to run the job with
    steps:
      - name: Login to Docker Hub # Step to log in to Docker Hub
        uses: docker/login-action@v2.2.0 # Uses an action to perform the login
        with: # Inputs to the login-action
          registry: git.owork.co.kr
          username: ${{ secrets.GITEAHUB_USERNAME }} # Docker Hub username from secrets
          password: ${{ secrets.GITEAHUB_PASSWORD }} # Docker Hub token/password from secrets

      - name: Checkout repository # Step to check out the repository code
        uses: actions/checkout@v3.6.0 # Uses the checkout action

      - name: Set up Docker Buildx # Step to set up Docker Buildx
        uses: docker/setup-buildx-action@v2.10.0 # Uses an action to set up Buildx

      - name: Build and push
        run: |
          docker build -t git.owork.co.kr/visualstore/nextapp .
          docker push git.owork.co.kr/visualstore/nextapp
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
            [${{ gitea.repository }}] Repository 의 Action 작업이 ${{ job.status }} 되었습니다.

```
---
base: "[[Docker.base]]"
최종 편집 일시: 2024-04-09T08:37:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
```docker
name: Build docker container (Ubuntu)
on:
  push:
    branches:
      - master
# =======================================================================================
# 첫번째 : action runner 에서 모두 처리 (자체적으로 docker 빌드할 docker 세팅 포함)
# =======================================================================================
# jobs:
#   build:
#     name: Build image
#     runs-on: [ubuntu-latest]
#     container:
#       image: catthehacker/ubuntu:act-latest # The Docker image to use as the container
#     # strategy: # Strategy for the job execution
#     #   matrix: # Allows running jobs with different variations
#     #     arch: [amd64, arm64] # Variations of architecture to run the job with
#     steps:
#       - name: Login to Docker Hub # Step to log in to Docker Hub
#         uses: docker/login-action@v2.2.0 # Uses an action to perform the login
#         with: # Inputs to the login-action
#           # registry: { { registry_url } } # Specifies the registry to log in to. You can set a variable or just hardcode this value.
#           username: ${{ secrets.DOCKERHUB_USERNAME }} # Docker Hub username from secrets
#           password: ${{ secrets.DOCKERHUB_TOKEN }} # Docker Hub token/password from secrets

#       - name: Set up Docker Buildx # Step to set up Docker Buildx
#         uses: docker/setup-buildx-action@v2.10.0 # Uses an action to set up Buildx

#       - name: Checkout repository # Step to check out the repository code
#         uses: actions/checkout@v3.6.0 # Uses the checkout action

#       # ${{ gitea.workspace }} 는 작업폴더 경로를 의미
#       - name: Build and push
#         run: |
#           docker build -t ojpfight/ubuntu ${{ gitea.workspace }}/ubuntu
#           docker push ojpfight/ubuntu

# ==================================================================
# 두번째 : action runner 가 설치된 os 에 docker 가 설치되어 있는 경우
# ==================================================================
jobs:
  build:
    name: Build image
    runs-on: [git-action2]
    steps:
      - name: Login to Docker Hub # Step to log in to Docker Hub
        uses: docker/login-action@v2.2.0 # Uses an action to perform the login
        with: # Inputs to the login-action
          # registry: { { registry_url } } # Specifies the registry to log in to. You can set a variable or just hardcode this value.
          username: ${{ secrets.DOCKERHUB_USERNAME }} # Docker Hub username from secrets
          password: ${{ secrets.DOCKERHUB_TOKEN }} # Docker Hub token/password from secrets

      - uses: actions/checkout@v2
      - name: Build and push
        shell: cmd
        run: |
          docker build -t ojpfight/ubuntu ./ubuntu
          docker push ojpfight/ubuntu

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
            [${{ gitea.repository }}] Repository
            의 Action 작업이 ${{ job.status }} 되었습니다.


```
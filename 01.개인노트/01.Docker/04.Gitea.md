---
base: "[[Docker.base]]"
cover: "[[Notion/Docker/Gitea/attach/Gitea 1.jpeg]]"
최종 편집 일시: 2025-05-30T15:23:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- Docker Image 다운로드
```docker
docker pull gitea/gitea
```

- gitea/gitea 이미지 상세정보 확인
```docker
docker image inspect gitea/gitea
```

- 컨테이너 생성 및 실행
```docker
docker run -it --name gitea -p 3000:3000 -v d:\docker\gitea:/data gitea/gitea
```
    -  -it : -i 와 -t 를 동시에 사용한 것으로 터미널 입력을 위한 옵션
    -  --name 은 contrainer 이름 지정
    -  -p 3000:3000 : 3000번 포트로 접근하면 container의 3000 번 포트로 연결 지정
    - -v d:\docker\gitea:/data 는 gitea의 기본 폴더/data 를 d:\docker\gitea 로 매칭
    -  gitea/gitea 는 다운받은 Docker 이미지

- git actions
    - 관련주소 : [https://medium.com/@kisuk623/%EB%A1%9C%EC%BB%AC%EC%97%90%EC%84%9C-git%EC%84%9C%EB%B2%84%EC%99%80-ci-cd%EA%B5%AC%EC%B6%95-faab820b7bb3](https://medium.com/@kisuk623/%EB%A1%9C%EC%BB%AC%EC%97%90%EC%84%9C-git%EC%84%9C%EB%B2%84%EC%99%80-ci-cd%EA%B5%AC%EC%B6%95-faab820b7bb3)
        - synology 나스
```docker
docker run --name gitea-action --privileged  -e GITEA_INSTANCE_URL=https://git.owork.co.kr -e GITEA_RUNNER_REGISTRATION_TOKEN=토큰 -e GITEA_RUNNER_NAME=git-action -v /var/run/docker.sock:/var/run/docker.sock -v /volume1/docker/git-action:/data  gitea/act_runner:latest
```
        - window
```docker
docker run --name next-app-action --privileged -e GITEA_INSTANCE_URL=https://git.onsm.synology.me -e GITEA_RUNNER_REGISTRATION_TOKEN=토큰 -e GITEA_RUNNER_NAME=next-app-action -v /var/run/docker.sock:/var/run/docker.sock gitea/act_runner:latest
```
    - **Gitea Actions **
        [[Build docker container 배포 (Gitea Package)]]
    - Gitaa Actions 에러 발생시
        - 관련주소 : [https://nakkasoft.tistory.com/249](https://nakkasoft.tistory.com/249)
        - 에러 메세지 : Error response from daemon: could not find an available, non-overlapping IPv4 address pool among the defaults to assign to the network
오류: 네트워크에 할당할 기본값 중에서 사용 가능하고 겹치지 않는 IPv4 주소 풀을 찾을 수 없습니다.
![[Notion/Docker/Gitea/attach/Untitled.png]]
        - Gitea Actions Runner (Docker) 서버에서 남는 network 정리 (ex : synology 서버 )
```plain text
docker network prune -f
```

- gitea act runner (window)
    - runner 다운로드 : [https://dl.gitea.com/act_runner/](https://dl.gitea.com/act_runner/) (ex : [act_runner-0.2.9-windows-amd64.exe](https://dl.gitea.com/act_runner/0.2.9/act_runner-0.2.9-windows-amd64.exe))
    - 다운 받은 후 이름 변경 ([act_runner-0.2.9-windows-amd64.exe](https://dl.gitea.com/act_runner/0.2.9/act_runner-0.2.9-windows-amd64.exe) ⇒ act_runner.exe)
    - 실행
```javascript
act_runner register --no-interactive --instance https://git.onsm.synology.me --token 토큰 --name git-action2 --labels git-action2
```
![[Notion/Docker/Gitea/attach/Untitled 1.png]]
    - bat 파일  (git-act-runner.cmd)
```yaml
cd D:\git-act-runner
act_runner daemon
```

> [!note]+ yml (window 에서 실행되는 runner 를 이용한 next.js 배포)
> ```yaml
> name: window publish
> 
> on: [push]
> 
> jobs:
>   build:
>     runs-on: [git-action2] # 라벨명 (ex : git-action2) 
>     steps:
>       # - uses: actions/checkout@v2
>       - name: git pull
>         working-directory: D:\next-app
>         shell: cmd
>         run: |
>           git pull origin main && git reset --hard origin/main
>       - name: yarn install && build
>         working-directory: D:\next-app
>         shell: cmd
>         run: |
>           yarn install && yarn build:prod
>       # - name: yarn build
>       #   working-directory: D:\next-app
>       #   shell: cmd
>       #   run: |
>       #     yarn build:prod
>       - name: Send mail
>         if: always()
>         # 관련주소 : https://github.com/dawidd6/action-send-mail
>         uses: dawidd6/action-send-mail@v3
>         with:
>           server_address: smtp.gmail.com
>           # Server port, default 25:
>           server_port: 465
>           # Optional whether this connection use TLS (default is true if server_port is 465)
>           secure: true
>           # Optional (recommended) mail server username:
>           username: ${{secrets.MAIL_USERNAME}}
>           # Optional (recommended) mail server password:
>           password: ${{secrets.MAIL_PASSWORD}}
>           from: ${{ secrets.MAIL_USERNAME }}
>           to: ${{ secrets.MAIL_USERNAME }}
>           subject: ${{ gitea.repository }} Action 작업 결과
>           priority: high
>           convert_markdown: true
>           attachments: ./README.md
>           body: |
>             ==========
>             🌟 정보
>             ==========
>             "The job was automatically triggered by a ${{ gitea.event_name }} event."
>             "This job is now running on a ${{ runner.os }} server hosted by Gitea!"
>             "The name of your branch is ${{ gitea.ref }} and your repository is ${{ gitea.repository }}."
>             "The ${{ gitea.repository }} repository has been cloned to the runner."
>             "The workflow is now ready to test your code on the runner."
> 
>             ==========
>             🌟 메세지
>             ==========
>             [${{ gitea.repository }}] Repository
>             의 Action 작업이 ${{ job.status }} 되었습니다.
> 
> ```

> [!note]+ yml (window 에서 실행되는 runner 를 이용한 [asp.net](http://asp.net/) core && iis 배포)
> - IIS
> ![[Notion/Docker/Gitea/attach/Untitled 2.png]]
> 
> > [!note]+ ### 실행
> > ```yaml
> > name: window publish
> > 
> > on: [push]
> > 
> > jobs:
> >   build:
> >     runs-on: [git-action2] # 라벨명 (ex : git-action2)
> >     steps:
> >       - name: iis stop
> >         shell: cmd
> >         run: |
> >           %systemroot%\system32\inetsrv\appcmd stop site /site.name:Web && %systemroot%\system32\inetsrv\appcmd stop apppool /apppool.name:Web
> >       - uses: actions/checkout@v2
> >       - name: dotnet publish
> >         shell: cmd
> >         run: |
> >           dotnet publish -c Release -o D:\Web
> >       - name: iis start
> >         shell: cmd
> >         run: |
> >           %systemroot%\system32\inetsrv\appcmd start site /site.name:Web && %systemroot%\system32\inetsrv\appcmd start apppool /apppool.name:Web
> >       - name: Send mail
> >         if: always()
> >         # 관련주소 : https://github.com/dawidd6/action-send-mail
> >         uses: dawidd6/action-send-mail@v3
> >         with:
> >           server_address: smtp.gmail.com
> >           # Server port, default 25:
> >           server_port: 465
> >           # Optional whether this connection use TLS (default is true if server_port is 465)
> >           secure: true
> >           # Optional (recommended) mail server username:
> >           username: ${{secrets.MAIL_USERNAME}}
> >           # Optional (recommended) mail server password:
> >           password: ${{secrets.MAIL_PASSWORD}}
> >           from: ${{ secrets.MAIL_USERNAME }}
> >           to: ${{ secrets.MAIL_USERNAME }}
> >           subject: ${{ gitea.repository }} Action 작업 결과
> >           priority: high
> >           convert_markdown: true
> >           attachments: ./README.md
> >           body: |
> >             ==========
> >             🌟 정보
> >             ==========
> >             "The job was automatically triggered by a ${{ gitea.event_name }} event."
> >             "This job is now running on a ${{ runner.os }} server hosted by Gitea!"
> >             "The name of your branch is ${{ gitea.ref }} and your repository is ${{ gitea.repository }}."
> >             "The ${{ gitea.repository }} repository has been cloned to the runner."
> >             "The workflow is now ready to test your code on the runner."
> > 
> >             ==========
> >             🌟 메세지
> >             ==========
> >             [${{ gitea.repository }}] Repository
> >             의 Action 작업이 ${{ job.status }} 되었습니다.
> > 
> > ```
> 
> > [!note]+ ### 실행2
> > ```yaml
> > name: window publish
> > 
> > on: [push]
> > 
> > jobs:
> >   build:
> >     runs-on: [git-action2] # 라벨명 (ex : git-action2) 
> >     steps:
> >       - name: git pull
> >         working-directory: D:\WebApp # 소스코드 폴더 
> >         shell: cmd
> >         run: |
> >           git pull origin master && git reset --hard origin/master
> >       - name : iis stop
> >         shell: cmd
> >         run: |
> >             %systemroot%\system32\inetsrv\appcmd stop site /site.name:Web && %systemroot%\system32\inetsrv\appcmd stop apppool /apppool.name:Web
> >       - name: dotnet publish
> >         working-directory: D:\WebApp # 소스코드 폴더 
> >         shell: cmd
> >         run: |
> >            dotnet publish -c Release -o D:\Web
> >       - name : iis start
> >         shell: cmd
> >         run: |
> >             %systemroot%\system32\inetsrv\appcmd start site /site.name:Web && %systemroot%\system32\inetsrv\appcmd start apppool /apppool.name:Web
> >       - name: Send mail
> >         if: always()
> >         # 관련주소 : https://github.com/dawidd6/action-send-mail
> >         uses: dawidd6/action-send-mail@v3
> >         with:
> >           server_address: smtp.gmail.com
> >           # Server port, default 25:
> >           server_port: 465
> >           # Optional whether this connection use TLS (default is true if server_port is 465)
> >           secure: true
> >           # Optional (recommended) mail server username:
> >           username: ${{secrets.MAIL_USERNAME}}
> >           # Optional (recommended) mail server password:
> >           password: ${{secrets.MAIL_PASSWORD}}
> >           from: ${{ secrets.MAIL_USERNAME }}
> >           to: ${{ secrets.MAIL_USERNAME }}
> >           subject: ${{ gitea.repository }} Action 작업 결과
> >           priority: high
> >           convert_markdown: true
> >           attachments: ./README.md
> >           body: |
> >             ==========
> >             🌟 정보
> >             ==========
> >             "The job was automatically triggered by a ${{ gitea.event_name }} event."
> >             "This job is now running on a ${{ runner.os }} server hosted by Gitea!"
> >             "The name of your branch is ${{ gitea.ref }} and your repository is ${{ gitea.repository }}."
> >             "The ${{ gitea.repository }} repository has been cloned to the runner."
> >             "The workflow is now ready to test your code on the runner."
> > 
> >             ==========
> >             🌟 메세지
> >             ==========
> >             [${{ gitea.repository }}] Repository
> >             의 Action 작업이 ${{ job.status }} 되었습니다.
> > ```
> > 
> > - docker registry 올리기
> > ```docker
> > docker build -t git.owork.co.kr/[계정]/[태그명]
> > docker build -t git.owork.co.kr/visualstore/testapp .
> > 
> > docker push git.owork.co.kr/visualstore/testapp
> > docker pull git.owork.co.kr/visualstore/testapp
> > ```
> > 

- app.ini 전체내용
```plain text
APP_NAME = Git Server
RUN_MODE = prod
RUN_USER = git
WORK_PATH = /data/gitea

[ui]
DEFAULT_THEME = gitea-dark

[repository]
ROOT = /data/git/repositories

[repository.local]
LOCAL_COPY_PATH = /data/gitea/tmp/local-repo

[repository.upload]
TEMP_PATH = /data/gitea/uploads
; 관련 링크 : https://garve32.tistory.com/77
; default로 설정되어 있는 파일 업로드 최대 사이즈는 3메가바이트, 한번에 올릴 수 있는 파일의 개수는 5개입니다.
; 이를 각각 100메가, 10개로 조정합니다.
FILE_MAX_SIZE = 100
MAX_FILES = 10

[server]
APP_DATA_PATH = /data/gitea
DOMAIN = git.onsm.synology.me
SSH_DOMAIN = git.onsm.synology.me
HTTP_PORT = 3000
ROOT_URL = https://git.onsm.synology.me/
DISABLE_SSH = false
SSH_PORT = 5322
SSH_LISTEN_PORT = 22
LFS_START_SERVER = true
LFS_CONTENT_PATH = /var/lib/gitea/data/lfs
LFS_JWT_SECRET = X726k1t9Mv0HuueU1Ll1nr1txcWxOUvQLcbsHIBS00E

[lfs]
; Where your lfs files reside, default is data/lfs.
PATH = /data/gitea/data/lfs

[database]
PATH = /data/gitea/gitea.db
DB_TYPE = mysql
HOST = onsm.synology.me:3307
NAME = gitea
USER = gitea
PASSWD = `win#1234`
LOG_SQL = false
SCHEMA = 
SSL_MODE = disable
CHARSET = utf8

[indexer]
ISSUE_INDEXER_PATH = /data/gitea/indexers/issues.bleve

[session]
PROVIDER_CONFIG = /data/gitea/sessions
PROVIDER = file

[picture]
AVATAR_UPLOAD_PATH = /data/gitea/avatars
REPOSITORY_AVATAR_UPLOAD_PATH = /data/gitea/repo-avatars
DISABLE_GRAVATAR = false
ENABLE_FEDERATED_AVATAR = true

[attachment]
PATH = /data/gitea/attachments

[log]
MODE = console
LEVEL = info
ROUTER = console
ROOT_PATH = /data/gitea/log

[security]
INSTALL_LOCK = true
SECRET_KEY = Du6HSEuFeTs1WOQheDWziSOj82N6lF3rYCwnW0PTMPiOaTpEBrEYnDa9hBCXKrdo
INTERNAL_TOKEN = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2MTU1NTczMDR9.uxDuaoRXM8Wxpdq1Qktj6yHvpVH2qcHUBQ1WT3j7Z-s
PASSWORD_HASH_ALGO = pbkdf2

[service]
DISABLE_REGISTRATION = true
REQUIRE_SIGNIN_VIEW = true
REGISTER_EMAIL_CONFIRM = false
ENABLE_NOTIFY_MAIL = true
ALLOW_ONLY_EXTERNAL_REGISTRATION = false
ENABLE_CAPTCHA = false
DEFAULT_KEEP_EMAIL_PRIVATE = false
DEFAULT_ALLOW_CREATE_ORGANIZATION = false
DEFAULT_ENABLE_TIMETRACKING = false
NO_REPLY_ADDRESS = 

[oauth2]
JWT_SECRET = eFToJ4MLinQBsMKsJylVrLNhvA9VPcP0sXXwp737iwo

[mailer]
ENABLED = true
HOST = smtp.gmail.com:465
FROM = ojpfight@gmail.com
USER = ojpfight@gmail.com
PASSWD = sipjaqtksaqlothg
MAILER_TYPE = smtp
IS_TLS_ENABLED = true

[openid]
ENABLE_OPENID_SIGNIN = false
ENABLE_OPENID_SIGNUP = false

[packages]
ENABLED = true

[actions]
ENABLED = true
```

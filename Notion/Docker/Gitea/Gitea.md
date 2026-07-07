---
base: "[[Docker.base]]"
cover: "[[Notion/Docker/Gitea/attach/Gitea.jpeg]]"
최종 편집 일시: 2024-11-15T15:19:00
태그: []
인증: unverified
소유자:
  - 준표 오
---

![[gitea____1.png]]

![[gitea____2.png]]

![[gitea____.png]]

- app.ini
```plain text
APP_NAME = Git Server
RUN_MODE = prod
RUN_USER = git
WORK_PATH = /data/gitea

[ui]
DEFAULT_THEME = arc-green

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
DOMAIN = git.owork.co.kr
SSH_DOMAIN = git.owork.co.kr
HTTP_PORT = 3000
ROOT_URL = https://git.owork.co.kr/
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

- git actions
    - 관련주소 :  [https://medium.com/@kisuk623/%EB%A1%9C%EC%BB%AC%EC%97%90%EC%84%9C-git%EC%84%9C%EB%B2%84%EC%99%80-ci-cd%EA%B5%AC%EC%B6%95-faab820b7bb3](https://medium.com/@kisuk623/%EB%A1%9C%EC%BB%AC%EC%97%90%EC%84%9C-git%EC%84%9C%EB%B2%84%EC%99%80-ci-cd%EA%B5%AC%EC%B6%95-faab820b7bb3)
```docker
docker run --name gitea-action -e GITEA_INSTANCE_URL=https://git.owork.co.kr -e GITEA_RUNNER_REGISTRATION_TOKEN=f3Q7C56hFNt77E5mTNWt0iCHWu1tRmSBZ8PyspiR -e GITEA_RUNNER_NAME=git-action -v /var/run/docker.sock:/var/run/docker.sock -v /volume1/docker/git-action:/data  gitea/act_runner:latest
```

    - **실행 목록**
        [[next.js 를 원격 ubuntu 서버에 ssh 로 배포]]
        [[Build docker container 배포 (Gitea Package)]]
        [[Build docker container 배포 (Docker Hub)]]

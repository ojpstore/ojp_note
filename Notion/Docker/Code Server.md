---
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/Code Server.jpeg]]"
최종 편집 일시: 2024-08-24T21:33:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 관련주소 
    - [시놀로지 나스 도커에 Code-Server 설치 / JAVA 개발환경 구성하기](https://blog.f4ctor.com/nas/시놀로지-나스-도커에-code-server-설치-java-개발환경-구성하기/#사용자_지정_헤더)

# Code-Server는 무엇인가요?

Code-Server는 웹 버전 VS Code라고 생각하시면 됩니다.

인터넷만 된다면 데스크톱, 랩톱, 태블릿PC, 스마트폰 등 별도의 설치 과정 없이 내가 미리 설정해둔 IDE에서 작업을 이어나갈 수 있습니다.

글에서 사용된 환경은 다음과 같습니다.

- NAS: Synology DS920+
- DSM 버전: DSM 7.1.1-42962 Update 1
- Docker 20.10.3-1308 패키지

---

# 다운로드

시놀로지 Docker를 열고 ‘레지스트리’ 탭에서 “code-server”를 검색하여 ‘linuxserver/code-server’를 더블클릭합니다.

![](https://f4ctor.com/wp-content/uploads/2022/10/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA-2022-10-25-05.43.00.png)

버전은 ‘latest’로 해주시면 됩니다.

![](https://f4ctor.com/wp-content/uploads/2022/10/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA-2022-10-25-05.44.00.png)

---

# 사전 작업

# (필수) config 파일이 저장될 폴더를 생성

저는 docker -> code-server -> config 로 생성했습니다.

![](https://f4ctor.com/wp-content/uploads/2022/10/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA-2022-10-25-05.46.37.png)

![](https://f4ctor.com/wp-content/uploads/2022/10/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA-2022-10-25-05.46.58-1.png)

# (선택) 도메인 연결 준비

보유한 도메인의 하위 도메인을 만들어 줍니다.

예시) code.test.kr

시놀로지 제어판 -> 보안 -> 인증서 탭에서 새로운 인증서를 만들어줍니다.

![](https://f4ctor.com/wp-content/uploads/2022/10/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA-2022-10-25-06.09.25.png)

# 역방향 프록시

인증서 생성과 설정이 끝났다면,

시놀로지 제어판 -> 로그인 포털 -> 역방향 프록시로 들어갑니다.

![](https://f4ctor.com/wp-content/uploads/2022/10/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA-2022-10-25-06.08.42.png)

호스트 이름에 하위 도메인을 넣어줍니다.

![](https://f4ctor.com/wp-content/uploads/2022/10/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA-2022-10-25-06.08.47.png)

# 사용자 지정 헤더

역방향 프록시 규칙의 상단탭에서 사용자 지정 머리글을 클릭하고 아래와 같이 설정해 줍니다.

| 머리글 이름 | 값 |
| --- | --- |
| Upgrade | $http_upgrade |
| Connection | $connection_upgrade |
| Accept-Encoding | gzip |

![](https://f4ctor.com/wp-content/uploads/2022/10/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA-2022-10-25-06.08.52.png)

---

# 설치하기

‘**이미지**‘탭에서 ‘**linuxserver/code-server**‘를 더블클릭합니다.

![](https://f4ctor.com/wp-content/uploads/2022/10/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA-2022-10-25-05.45.11.png)

# 네트워크 선택

**네트워크**는 디폴트상태로 진행합니다. (선택한 네트워크 사용 – 컨테이너 이름 bridge)

![](https://f4ctor.com/wp-content/uploads/2022/10/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA-2022-10-25-05.45.23.png)

좌측 하단의 ‘**고급 설정**‘을 클릭합니다.

![](https://f4ctor.com/wp-content/uploads/2022/10/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA-2022-10-25-05.45.42.png)

# **파라미터 설정**

더 많은 파라미터를 확인하고 싶으시면 [https://hub.docker.com/r/linuxserver/code-server](https://hub.docker.com/r/linuxserver/code-server) 를 참고해 주세요.

| 변수 | 값 |
| --- | --- |
| TZ | Asia/Seoul |
| PUID | 1000 |
| PGID | 1000 |
| PASSWORD | 1q2w3e4r@! (접근 시 사용될 패스워드) |
| SUDO_PASSWORD | 1q2w3e4r@! (리눅스 root 패스워드) |
| PROXY_DOMAIN | code.test.kr (도메인 입력, 옵션으로 없으면 이 행은 삭제하세요.) |

![](https://f4ctor.com/wp-content/uploads/2022/10/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA-2022-10-25-05.54.44-1.png)

# **포트 설정**

로컬 포트가 기존 포트와 겹친다면 다른 포트로 해도 괜찮지만, 위쪽에서 설정한 ‘역방향 프록시’의 포트도 변경하셔야 합니다.

![](https://f4ctor.com/wp-content/uploads/2022/10/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA-2022-10-25-05.54.59.png)

# 볼륨 설정

‘폴더 추가’를 클릭하고 사전 작업에서 생성한 ‘config’ 폴더를 지정해 주세요.

![](https://f4ctor.com/wp-content/uploads/2022/10/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA-2022-10-25-05.55.33.png)

**마운트 경로**는 “*/config*“로 해주세요.

![](https://f4ctor.com/wp-content/uploads/2022/10/image-12.png)

마지막으로 전체 설정을 확인하는 화면이 나옵니다. 이상이 없는지 확인하시고 완료해 주세요.

---

# 사용하기

# 접속하기

브라우저 주소표시줄에 지정한 **도메인을 입력**하고 들어갑니다.

예) code.test.kr

**도메인이 없어 넘어갔다면** NAS의 ip주소와 포트를 입력하고 접속합니다.

예) 192.168.1.101:58443

**패스워드**는 파라미터 설정에서 지정한 ‘PASSWORD’를 입력하시면 됩니다.

예) 1q2w3e4r@!

![](https://f4ctor.com/wp-content/uploads/2022/10/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA-2022-10-26-15.23.24-1024x531.png)

성공했다면 VS Code와 같은 UI의 IDE가 뜹니다.

![](https://f4ctor.com/wp-content/uploads/2022/10/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA-2022-10-25-06.09.57-1-1024x703.png)

# 에러가 떠요

아래와 같은 에러가 뜬다면 ‘사전 작업’의 ‘사용자 지정 헤더’를 다시 확인해 주세요.

```plain text
An unexpected error occurred that requires a reload of this page.
The workbench failed to connect to the server (Error: WebSocket close with status code 1006)
```

---
base: "[[Docker.base]]"
최종 편집 일시: 2026-03-18T10:08:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- [개인PC] vscode extension 설치 
    - Remote - SSH

- [개인PC] ssh key 생성
```javascript
ssh-keygen 
or
ssh-keygen -t rsa -b 4096
```
    ## 1. `ssh-keygen` (기본 실행)
매개변수 없이 실행하면 시스템에 설정된 **기본값**으로 키 쌍을 생성합니다.
    - **암호화 알고리즘:** 최신 시스템(OpenSSH 8.0 이상)에서는 보통 `ed25519` 또는 `rsa`가 기본값입니다.
    - **키 길이:** `rsa`가 기본일 경우 보통 **3072비트** 또는 **2048비트**로 설정됩니다.
    - **특징:** 가장 빠르고 간편하게 키를 만들 수 있지만, 환경에 따라 보안 수준이 달라질 수 있습니다.
    ## 2. `ssh-keygen -t rsa -b 4096` (상세 지정)
사용자가 알고리즘과 복잡도를 직접 명시한 형태입니다.
    - `**t rsa**`: 암호화 방식을 **RSA** 알고리즘으로 고정합니다. RSA는 호환성이 가장 뛰어나 거의 모든 서버에서 지원합니다.
    - `**b 4096**`: 키의 길이를 **4096비트**로 설정합니다.
        - 일반적인 2048비트보다 해독하기 훨씬 어렵습니다.
        - 보안 표준(NIST 등)에서 권장하는 높은 수준의 보안 강도입니다.

`ssh-keygen` 명령어를 실행하면 기본적으로 **두 개의 파일**이 한 쌍(Key Pair)으로 생성됩니다. 이 파일들은 보통 사용자의 홈 디렉터리 내 `.ssh` 폴더에 저장됩니다.
---
    ## **1. 개인키 (Private Key)**
    - **파일명:** `id_rsa` (알고리즘에 따라 `id_ed25519` 등)
    - **역할:** 일종의 **'인감도장'** 또는 **'열람 열쇠'**입니다.
    - **특징:**
        - 내 컴퓨터에만 보관해야 하며, **절대로 타인에게 노출해서는 안 됩니다.**
        - 파일 권한이 엄격하게 관리되어야 합니다 (보통 `600` 권한).
        - 이 키를 가진 사람은 해당 공개키가 등록된 모든 서버에 당신의 이름으로 접속할 수 있습니다.
    ## **2. 공개키 (Public Key)**
    - **파일명:** `id_rsa.pub` (항상 `.pub` 확장자가 붙습니다)
    - **역할:** 일종의 **'자물쇠'**입니다.
    - **특징:**
        - 이름 그대로 **공개되어도 안전**합니다.
        - 접속하려는 원격 서버의 특정 파일(`~/.ssh/authorized_keys`)에 이 키의 내용을 복사해서 등록합니다.
        - 서버는 이 공개키(자물쇠)를 가지고 있다가, 접속 요청이 올 때 사용자가 올바른 개인키(열쇠)를 가지고 있는지 검증합니다.

- [개인PC]** **config 설정
    - 경로 : c:\Users\계정\.ssh\conf
```javascript
Host 서버주소 명칭 (ex : 127.0.0.1- [개발서버])
  User root
  Port 포트
  HostName 서버주소 (ex : 127.0.0.1)
  IdentityFile C:\Users\계정\.ssh\id_rsa
```
- 명령어로 ubuntu 서버에 ssh 등록 (powershell)
```javascript
type $env:USERPROFILE\.ssh\id_rsa.pub | ssh 계정@서버주소 "echo '' >> ~/.ssh/authorized_keys; cat >> .ssh/authorized_keys"
```
- 직접 ubuntu 서버 설정
    - /root/.ssh/authorized_keys 에 위에서 생성한 개인키 입력
```javascript
ssh-rsa AAAAB3.......
```

- [개인PC] 연결
![[Untitled 2.png]]
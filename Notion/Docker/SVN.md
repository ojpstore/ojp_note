---
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/SVN.jpeg]]"
최종 편집 일시: 2024-11-01T07:20:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 관련주소 : [https://enjoy-dev.tistory.com/16](https://enjoy-dev.tistory.com/16)
- 레지스트리에서  svn-server 이미지 다운로드
![[img1.daumcdn 1.png]]
![[img1.daumcdn 2.png]]

- 컨테이너 실행
![[img1.daumcdn 3.png]]
![[img1.daumcdn 4.png]]
![[img1.daumcdn 5.png]]
![[img1.daumcdn 6.png]]

- 접속
    - **http://{NAS-IP}:1180/svnadmin**
| **Subversion authorization file** | /etc/subversion/subversion-access-control |
| --- | --- |
| **User authentication file (SVNUserFile)** | /etc/subversion/passwd |
| **Parent directory of the repositories (SVNParentPath)** | /home/svn |
| **Subversion client executable** | /usr/bin/svn |
| **Subversion admin executable** | /usr/bin/svnadmin |

![[img1.daumcdn 7.png]]

- 비밀번호 변경

![[img1.daumcdn 8.png]]

![[img1.daumcdn 9.png]]

- 리파지토리 생성
![[img1.daumcdn 10.png]]

- 사용자를 해당 리파지토리에 권한 부여
![[img1.daumcdn 11.png]]

- svn 주소
    - http://{NAS-IP 혹은 도메인}:1180/svn/리파지토리명
![[img1.daumcdn 12.png]]

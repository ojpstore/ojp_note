---
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/Mattermost.jpeg]]"
최종 편집 일시: 2024-11-25T21:46:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
![[Notion/Docker/attach/Mattermost-Synology-NAS-Set-up-16-new-2024 1.png]]

> **매터모스트**(Mattermost)는 파일 공유, 검색, 통합 기능을 제공하는 [오픈 소스](https://ko.wikipedia.org/wiki/%EC%98%A4%ED%94%88_%EC%86%8C%EC%8A%A4_%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4) 셀프 호스팅 가능 온라인 [채팅](https://ko.wikipedia.org/wiki/%EC%B1%84%ED%8C%85) 서비스이다. 단체와 기업을 위한 내부 채팅으로 설계되어 있으며 대부분 그 자체를 [슬랙](https://ko.wikipedia.org/wiki/%EC%8A%AC%EB%9E%99_(%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4))과[[6]](https://ko.wikipedia.org/wiki/%EB%A7%A4%ED%84%B0%EB%AA%A8%EC%8A%A4%ED%8A%B8#cite_note-6)[[7]](https://ko.wikipedia.org/wiki/%EB%A7%A4%ED%84%B0%EB%AA%A8%EC%8A%A4%ED%8A%B8#cite_note-:0-7) [마이크로소프트 팀즈](https://ko.wikipedia.org/wiki/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%86%8C%ED%94%84%ED%8A%B8_%ED%8C%80%EC%A6%88)의 오픈 소스 대안으로 마케팅한다.

- 관련주소
- 문서 : [https://mattermost-docs.infograb.net/guides/administration.html](https://mattermost-docs.infograb.net/guides/administration.html) 
- 설치 
    - [https://mariushosting.com/how-to-install-mattermost-on-your-synology-nas/](https://mariushosting.com/how-to-install-mattermost-on-your-synology-nas/) 
    - [https://comling.tistory.com/11](https://comling.tistory.com/11)
- docker 테스트용
```docker
docker run --name mattermost -p 8401:8065 -e TZ=Asia/Seoul -e MM_SQLSETTINGS_DRIVERNAME=postgres -e MM_SQLSETTINGS_DATASOURCE=postgres://tgms:1234!@onsm.synology.me:54231/mattermost?sslmode=disable&connect_timeout=10 mattermost/mattermost-team-edition:latest
```
- docker 
```docker
docker run --name mattermost -p 8401:8065 \
- /volume1/docker/mattermost/config:/mattermost/config:rw \
- /volume1/docker/mattermost/data:/mattermost/data:rw \
- /volume1/docker/mattermost/logs:/mattermost/logs:rw \
- /volume1/docker/mattermost/plugins:/mattermost/plugins:rw \
- /volume1/docker/mattermost/client:/mattermost/client/plugins:rw \
- /volume1/docker/mattermost/indexes:/mattermost/bleve-indexes:rw \
-e TZ=Asia/Seoul \
-e MM_SQLSETTINGS_DRIVERNAME=postgres \
-e MM_SQLSETTINGS_DATASOURCE=postgres://tgms:1234!@onsm.synology.me:54231/mattermost \
-e MM_BLEVESETTINGS_INDEXDIR=/mattermost/bleve-indexes \
-e MM_SERVICESETTINGS_SITEURL=https://chat.onsm.synology.me \
mattermost/mattermost-team-edition:latest
```
```docker
docker run --name mattermost -p 8401:8065 \
- /volume1/docker/mattermost/config:/mattermost/config:rw \
- /volume1/docker/mattermost/data:/mattermost/data:rw \
- /volume1/docker/mattermost/logs:/mattermost/logs:rw \
- /volume1/docker/mattermost/plugins:/mattermost/plugins:rw \
- /volume1/docker/mattermost/client:/mattermost/client/plugins:rw \
- /volume1/docker/mattermost/indexes:/mattermost/bleve-indexes:rw \
-e TZ=Asia/Seoul \
-e MM_SQLSETTINGS_DRIVERNAME=postgres \
-e MM_SQLSETTINGS_DATASOURCE=postgres://tgms:1234!@onsm.synology.me:54231/mattermost?sslmode=disable&connect_timeout=10 \
-e MM_BLEVESETTINGS_INDEXDIR=/mattermost/bleve-indexes \
-e MM_SERVICESETTINGS_SITEURL=https://chat.onsm.synology.me \
mattermost/mattermost-team-edition:latest
```


- 관리자 설정
> [!note]+ SMTP 설정
> ![[Notion/Docker/attach/image 16.png]]

> [!note]+ 푸시 알림 서버 설정
> ![[Notion/Docker/attach/image 17.png]]

![[Mattermost synced block]]
> [!note]+ ai-framework and GPT4All
> - [Build your own local AI with mattermost-ai-framework and GPT4All](https://www.youtube.com/watch?v=h7vHwVabPQc&t=277s)
> -  https://github.com/mattermost/mattermost-ai-framework 

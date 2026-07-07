---
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/OpenProject.jpeg]]"
최종 편집 일시: 2025-04-18T14:30:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 컨테이너 실행
```docker
docker run -d --name openproject -p 8181:80 -e SERVER_HOSTNAME=op.onsn.synology.me -e SECRET_KEY_BASE=adsasddassad -e OPENPROJECT_EDITION="bim" -v /volume1/docker/openproject/pgdata:/var/openproject/pgdata -v /volume1/docker/openproject/assets:/var/openproject/assets -e OPENPROJECT_DEFAULT__LANGUAGE=ko openproject/openproject:14
```

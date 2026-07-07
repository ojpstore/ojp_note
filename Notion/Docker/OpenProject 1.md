---
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/OpenProject 1.jpeg]]"
최종 편집 일시: 2025-04-18T12:30:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 컨테이너 실행
```docker
docker run -it --name openproject -p 8080:80 -e OPENPROJECT_SECRET_KEY_BASE=secret -e OPENPROJECT_HOST__NAME=localhost:8080 -e OPENPROJECT_HTTPS=false -e OPENPROJECT_DEFAULT__LANGUAGE=ko -v d:/docker/openproject/pgdata:/var/openproject/pgdata -v d:/docker/openproject/assets:/var/openproject/assets openproject/openproject:15
```

---
notion-id: 4b5e24d0-0c31-4468-b124-4c0e2e63a819
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/Postgresql 1.jpeg]]"
최종 편집 일시: 2025-04-21T14:30:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 컨테이너 생성 및 실행
```docker
docker run -d -p 54320:5432 --name Postgresql -e POSTGRES_USER=puser -e POSTGRES_PASSWORD=win#1234 -v d:/docker/postgresql:/var/lib/postgresql/data postgres
```

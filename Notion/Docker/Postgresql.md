---
notion-id: 140ecbc3-9068-80cf-a3a2-ea8d9c10eecd
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/Postgresql.jpeg]]"
최종 편집 일시: 2024-11-19T09:07:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 컨테이너 생성 및 실행
```docker
docker run -d -p 54231:5432 --name Postgresql -e POSTGRES_USER=tgms -e POSTGRES_PASSWORD=1234! -v /volume1/docker/postgresql:/var/lib/postgresql/data postgres
```

- 설정
![[image 10.png]]
![[image 11.png]]
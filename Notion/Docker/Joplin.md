---
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/Joplin.jpeg]]"
최종 편집 일시: 2025-06-30T22:46:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 실행 

```java
docker run --name=joplin -p 8877:8877 -e APP_PORT=8877 -e APP_BASE_URL=도메인 -e DB_CLIENT=pg -e POSTGRES_PASSWORD=비밀번호 -e POSTGRES_DATABASE=joplin -e POSTGRES_USER=아이디 -e POSTGRES_PORT=포트번호 -e POSTGRES_HOST=호스트 docker.io/joplin/server:latest
```

- 관련 내용
[https://daten-kunst.tistory.com/6](https://daten-kunst.tistory.com/6)
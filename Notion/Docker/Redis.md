---
notion-id: e33b843d-6ff5-4bc7-b546-073f6137ba21
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/Redis.jpeg]]"
최종 편집 일시: 2024-03-21T13:23:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 컨테이너 생성 및 실행
```docker
docker run --name redis -d -v d:\docker\redis:/data -p 6379:6379 redis --appendonly yes
```
    - d옵션은 백그라운드에서 실행하겠다는 의미이며
    - p옵션은 외부에서 해당 포트로 접속할 수 있게 열어둔다는 의미입니다. (Docker를 실행하여 Redis서버를 올리면 기본 포트인 6379로 실행됩니다)
    - appendonly yes 옵션은 AOF방식으로 데이터를 저장 (참고:Redis Persistence Introduction)하겠다는 의미입니다.

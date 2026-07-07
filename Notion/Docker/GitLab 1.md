---
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/GitLab 1.jpeg]]"
최종 편집 일시: 2024-03-21T12:17:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 컨테이너 생성 및 실행
```docker
docker run --name gitlab --hostname localhost -p 35000:80 gitlab/gitlab-ce
```

---
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/Nexus.jpeg]]"
최종 편집 일시: 2025-05-29T15:36:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 실행

 

```docker
docker run --name nexus -p 8081:8081 -p 5000:5000 -v /volume1/docker/nexus:/nexus-data sonatype/nexus3
```

- 관련 링크
    - [https://velog.io/@haerong22/Nexus를-이용한-Docker-Registry](https://velog.io/@haerong22/Nexus%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-Docker-Registry)

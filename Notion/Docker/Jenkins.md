---
notion-id: 144ecbc3-9068-80e1-b12f-c95334cfb395
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/Jenkins.jpeg]]"
최종 편집 일시: 2024-11-21T08:59:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 컨테이너  생성 및 실행
```docker
docker run --name jenkins -p 8322:22 -p 8383:8080 -p 50000:50000 -v /volume1/docker/jenkins:/etc/docker-home/jenkins jenkins/jenkins
```
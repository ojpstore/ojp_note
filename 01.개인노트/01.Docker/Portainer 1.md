---
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/Portainer 1.jpeg]]"
최종 편집 일시: 2024-03-21T13:12:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- Docker Image 다운로드
```docker
docker pull portainer/portainer
```

- 컨테이너 생성 및 실행
```docker
docker run -d -p 9000:9000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v D:\docker\portainer:/data portainer/portainer
```

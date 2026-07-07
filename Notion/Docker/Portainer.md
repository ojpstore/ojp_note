---
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/Portainer.jpeg]]"
최종 편집 일시: 2024-03-21T19:55:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- putty 연결 후 실행
```plain text
sudo -i
docker run -d -p 9000:9000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v /volume1/docker/portainer:/data portainer/portainer-ce
```

- 세팅 이미지
![[portainer_docker____1.png]]
![[portainer_docker____2.png]]

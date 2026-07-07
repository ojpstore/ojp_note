---
notion-id: 20fecbc3-9068-8062-8c5c-ec0bec33d599
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/n8n.jpeg]]"
최종 편집 일시: 2025-06-11T16:04:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 컨테이너 실행
```docker
docker run --name n8n -p 5678:5678 -e WEBHOOK_URL=https://b8n.onsm.synology.me -v /volume1/docker/n8n:/home/node/.n8n n8nio/n8n
```
- 관련 강좌
    1. [https://mariushosting.com/how-to-install-n8n-on-your-synology-nas/](https://mariushosting.com/how-to-install-n8n-on-your-synology-nas/) (synology docker 에 설치)
    2. [https://youtu.be/DhuaKAW819s?si=xg2R4aNlxhETvMmg](https://youtu.be/DhuaKAW819s?si=xg2R4aNlxhETvMmg) (docker 설치 관련)
    3. 
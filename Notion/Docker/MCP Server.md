---
notion-id: 207ecbc3-9068-80de-80c4-ff36e1ad5bda
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/MCP Server.jpeg]]"
최종 편집 일시: 2025-06-03T16:19:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 컨테이너 실행

```docker
docker run --name mcp-server --restart=unless-stopped -p 25565:25565 -e EUL=TRUE  -v /volume1/docker/mcp:/data itzg/minecraft-server
```
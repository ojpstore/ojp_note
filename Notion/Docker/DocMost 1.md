---
notion-id: 1d8ecbc3-9068-802e-9489-fbbd135bf2b2
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/DocMost.jpeg]]"
최종 편집 일시: 2025-04-18T09:04:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 관련링크 : [https://mariushosting.com/how-to-install-docmost-on-your-synology-nas/](https://mariushosting.com/how-to-install-docmost-on-your-synology-nas/)
- docker-compose.yml
```yaml
services:
  db:
    image: postgres:17
    container_name: docmost-db
    hostname: docmost-db
    security_opt:
      - no-new-privileges:true
    healthcheck:
      test: ["CMD", "pg_isready", "-q", "-d", "docmost", "-U", "docmostuser"]
      timeout: 45s
      interval: 10s
      retries: 10
    volumes:
      - d:/docker/docmost/db:/var/lib/postgresql/data:rw
    environment:
      POSTGRES_DB: docmost
      POSTGRES_USER: docmostuser
      POSTGRES_PASSWORD: docmostpass
    restart: on-failure:5

  docmost:
    image: docmost/docmost:latest
    container_name: docmost
    user: 0:0
    healthcheck:
      test: timeout 10s bash -c ':> /dev/tcp/127.0.0.1/3000' || exit 1
      interval: 10s
      timeout: 5s
      retries: 3
      start_period: 90s
    depends_on:
      - db
      - redis
    environment:
      APP_URL: http://localhost
      APP_SECRET: dOxZYTTZgXKMHkqLBIQVImayQXAVWdzGBPuFJKggzcgvgPJPXpWzqzKaUOIOGGIr
      DATABASE_URL: "postgresql://docmostuser:docmostpass@db:5432/docmost?sslmode=disable"
      REDIS_URL: "redis://redis:6379"
      DISABLE_TELEMETRY: true
      MAIL_DRIVER: smtp
      SMTP_HOST: smtp.gmail.com
      SMTP_PORT: 587
      SMTP_USERNAME: gmail 계정
      SMTP_PASSWORD: gmail 앱 비밀번호
      MAIL_FROM_ADDRESS: gmail 계정
      MAIL_FROM_NAME: Docmost
    ports:
      - 3199:3000
    restart: on-failure:5
    volumes:
      - d:/docker/docmost/data:/app/data/storage:rw

  redis:
    image: redis:7.2-alpine
    container_name: docmost-redis
    security_opt:
      - no-new-privileges:true
    read_only: true
    user: 1026:100
    healthcheck:
      test: ["CMD-SHELL", "redis-cli ping || exit 1"]
    volumes:
      - d:/docker/docmost/redis:/data:rw
    environment:
      TZ: Europe/Bucharest
    restart: on-failure:5

```
- 실행전 변경할 사항
    - SMTP_USERNAME: gmail 계정
    - SMTP_PASSWORD: gmail 앱 비밀번호
    - MAIL_FROM_ADDRESS: gmail 계정

---
base: "[[Docker.base]]"
최종 편집 일시: 2024-08-24T21:28:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 실행
```javascript
docker run --name mongo -p 27017:27017  -e  MONGO_INITDB_ROOT_USERNAME=ojp -e MONGO_INITDB_ROOT_PASSWORD=win#1234 -e ME_CONFIG_BASICAUTH=false  mongo 

docker run --name mongodb -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=ojp -e MONGO_INITDB_ROOT_PASSWORD=Win#10245 mongodb/mongodb-community-server 
```

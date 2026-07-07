---
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/MongoDB.jpeg]]"
최종 편집 일시: 2024-11-01T07:20:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 도커 이미지 (둘중 하나를 사용함)
    - docker pull mongo:4.4.10
    - docker pull ojpfight/mongodb (mongo:4.4.10 기반으로 태그변경한 거)
- 환경변수 추가 항목
    - MONGO_INITDB_ROOT_USERNAME
    - MONGO_INITDB_ROOT_PASSWORD
- 실행명령 (실행하지 않으면 인증이 적용되지 않고 바로 연결이 됨)
```javascript
 mongod --auth
```


![[mongo_setting1.png]]

![[mongo_setting2.png]]

![[mongo_setting3.png]]

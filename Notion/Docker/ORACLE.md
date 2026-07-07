---
base: "[[Docker.base]]"
최종 편집 일시: 2025-10-20T09:31:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 실행
```docker
docker run -d -p 1521:1521 --name OraFree --restart=always -e ORACLE_PASSWORD=비밀번호 gvenzl/oracle-free
```

- DBeaver 연결
![[image.png]]
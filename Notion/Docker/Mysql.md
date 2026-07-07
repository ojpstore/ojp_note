---
notion-id: aee9016d-97ff-49d5-9298-502475f0fadb
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/Mysql.jpeg]]"
최종 편집 일시: 2025-04-17T16:31:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 컨테이너 생성 및 실행
```docker
docker run --name mysql -e MYSQL_ROOT_PASSWORD=pass#1234 -p 3306:3306 -v d:\docker\mysql:/var/lib/mysql -d mysql --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```

- dbeaver 연결시 에러 발생시
![[mysql_dbeaver_error.png]]

- 계정생성
```sql
CREATE USER '계정'@'%' IDENTIFIED BY '비밀번호';

## 전체 권한
#GRANT ALL PRIVILEGES ON *.* TO '계정'@'%';

## mysql 디비만 권한
#GRANT ALL PRIVILEGES ON mysql.* TO '계정'@'%';

######################################################################

CREATE USER 'user'@'%' IDENTIFIED BY 'Win#20200402';
## 전체 권한
GRANT ALL PRIVILEGES ON *.* TO 'user'@'%';

## mysql 디비만 권한
#GRANT ALL PRIVILEGES ON mysql.* TO 'user'@'%';

flush privileges;
```

- 계정삭제
```sql
delete from mysql.user where User ='삭제할 아이디';

delete from mysql.db where User ='삭제할 아이디';

flush privileges;

######################################################################

delete from mysql.user where User ='user';

delete from mysql.db where User ='user';

flush privileges;
```

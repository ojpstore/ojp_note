---
notion-id: 143ecbc3-9068-8051-a8fb-e5319a7a51f0
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/Redmine.jpeg]]"
최종 편집 일시: 2025-12-18T12:02:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 컨테이너 생성 및 실행
    - REDMINE_DB_MYSQL : [localhost](http://localhost/) 를 입력하면 연결이 안됨, 실제 dns 및 ip 주소를 입력해야 함.
```docker
docker run --name redmine -p 8888:3000   -e REDMINE_DB_MYSQL=서버주소 -e REDMINE_DB_PORT=포트 -e REDMINE_DB_USERNAME=계정 -e REDMINE_DB_PASSWORD=비밀번호 -e REDMINE_DB_DATABASE=데이터베이스 -e REDMINE_SECRET_KEY_BASE=보안비밀번호(개인지정) -e REDMINE_PLUGINS_MIGRATE=true -v /volume1/docker/redmine/files:/usr/src/redmine/files -v /volume1/docker/redmine/themes:/usr/src/redmine/public/themes -v /volume1/docker/redmine/plugins:/usr/src/redmine/plugins -v /volume1/docker/redmine/config/configuration.yml:/usr/src/redmine/config/configuration.yml:ro  ojpfight/redmine

docker run --name redmine -p 8888:3000   -e REDMINE_DB_MYSQL=서버주소 -e REDMINE_DB_PORT=포트 -e REDMINE_DB_USERNAME=계정 -e REDMINE_DB_PASSWORD=비밀번호 -e REDMINE_DB_DATABASE=데이터베이스 -e REDMINE_SECRET_KEY_BASE=보안비밀번호(개인지정) -e REDMINE_PLUGINS_MIGRATE=true -v /volume1/docker/redmine/files:/usr/src/redmine/files -v /volume1/docker/redmine/themes:/usr/src/redmine/public/themes -v /volume1/docker/redmine/plugins:/usr/src/redmine/plugins -v /volume1/docker/redmine/config/configuration.yml:/usr/src/redmine/config/configuration.yml:ro redmine:5.0

```

- 설정
> [!note]+ 메일알람
> - 관련주소 
>     -  [https://jsmun.com/104](https://jsmun.com/104)
>     - [https://www.redmine.org/boards/1/topics/46305](https://www.redmine.org/boards/1/topics/46305)
>     - 파일 경로 
> ![[image 6.png]]
>     - /config/configuration.yaml
> ```yaml
> default:
>   # Outgoing emails configuration (see examples above)
>   email_delivery:
>     delivery_method: :smtp
>   smtp_settings:
>     address: smtp.gmail.com
>     port: 465
>     ssl: true
>     enable_starttls_auto: true
>     domain: gmail.com
>     authentication: :login
>     user_name: 이메일 주소
>     password: 비밀번호
> ```

    - 도커 볼륨 정보
![[image 7.png]]
    - 디비 접속을 위한 환경변수 관련
![[image 8.png]]

- 관리 설정 
    - 일감유형
![[image 9.png]]
    - 일감상태
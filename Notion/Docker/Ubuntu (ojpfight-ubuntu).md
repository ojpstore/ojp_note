---
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/Ubuntu (ojpfight-ubuntu).jpeg]]"
최종 편집 일시: 2024-07-09T20:53:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 실행
```javascript
docker run --privileged --name ubuntu-server -p 3322:22 -p 8800:80 -p 8830-8840:8830-8840 git.onsm.synology.me/ojp/ubuntu:latest /usr/sbin/init
docker run --privileged --name ubuntu-server -p 3322:22 -p 8800:80 -p 8830-8840:8830-8840 ojpfight/ubuntu /usr/sbin/init
```

- ssh key 생성
```javascript
ssh-keygen 
or
ssh-keygen -t rsa -b 4096
```

- ubuntu git 사용자 정보 추가
```javascript
git config --global user.name "ojpfight"
git config --global user.email ojpfight@gmail.com
```

- ubuntu git 초기 및 remote 추가
```javascript
git init
git remote add origin [추가할 원격 git 저장소 주소]
git pull origin main
```

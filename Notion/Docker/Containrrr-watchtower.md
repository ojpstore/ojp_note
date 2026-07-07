---
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/Containrrr-watchtower.jpeg]]"
최종 편집 일시: 2024-05-27T19:48:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 실행
```javascript
docker run --name watchtower -d --restart=always -e TZ=Asia/Seoul -e WATCHTOWER_CLEANUP=true -e WATCHTOWER_POLL_INTERVAL=10 -v /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower
```

- 옵션 설명
    - TZ=Asia/Seoul : 컨테이너의 시간대를 서울 (KST) 로 설정합니다. 나중에 업데이트 이력을 로그에서 확인할 수 있는데, 시간대가 적용되지 않으면 헷갈릴 수 있으니까요.
    - WATCHTOWER_CLEANUP=true : 이미지 업데이트 후 과거 버전을 삭제합니다.
    - WATCHTOWER_POLL_INTERVAL=43200 : 업데이트를 확인할 주기입니다. 초 단위고요, 43,200은 12시간이에요. 기본값은 86,400 (24시간) 인데 옵션 설명을 위해 12시간으로 적용해봤어요. 사실 업데이트가 그렇게 즉각적으로 필요한 때는 없으니, 기본값을 사용해도 좋습니다.
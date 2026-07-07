---
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/Watchtower.png]]"
최종 편집 일시: 2024-11-19T21:04:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 컨테이너 생성 및 실행
```docker
docker run --name watchtower -e TZ=Asia/Seoul -e WATCHTOWER_CLEANUP=true -e WATCHTOWER_POLL_INTERVAL=10 containrrr/watchtower
```

- 컨테이너 예외 처리
    - 자동 업데이트 하지 않을 컨테이너의 labels 의 값을 com.centurylinklabs.watchtower.enable=false 로 설정
        - 관련링크
            - [https://www.clien.net/service/board/cm_nas/16427222](https://www.clien.net/service/board/cm_nas/16427222)
            - [https://containrrr.dev/watchtower/container-selection/](https://containrrr.dev/watchtower/container-selection/)
        - ex) redmine 컨테이너를 대상으로 예외처리 (potainer 에서 처리한 결과 이미지)
![[image 4.png]]
![[image 5.png]]
---
base: "[[Docker.base]]"
최종 편집 일시: 2024-12-12T22:00:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- **오픈소스 Task 관리 프로젝트**
- Docker Image : [https://betwe.tistory.com/entry/Docker-mattermostfocalboard-오픈소스-Task-관리-프로젝트-구축하기](https://betwe.tistory.com/entry/Docker-mattermostfocalboard-%EC%98%A4%ED%94%88%EC%86%8C%EC%8A%A4-Task-%EA%B4%80%EB%A6%AC-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0)
- 실행 
```plain text
docker run --name focalboard -p 8087:8000 -v /volume1/docker/focalboard:/var/lib/focalboard mattermost/focalboard
```
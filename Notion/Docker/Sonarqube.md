---
notion-id: 64482c6e-92ac-4148-8dd0-32ac4b0ce1c0
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/Sonarqube.jpeg]]"
최종 편집 일시: 2024-03-27T14:33:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- Sonarqube 와 Jenkins 연동 : [https://beomseok95.tistory.com/m/201](https://beomseok95.tistory.com/m/201)
- Sonarqube 와 dotnet 프로젝트 : [https://medium.com/@thiagoloureiro/code-analysis-with-sonarqube-docker-net-core-aee521ee8931](https://medium.com/@thiagoloureiro/code-analysis-with-sonarqube-docker-net-core-aee521ee8931)
- Ubuntu 에 Sonarqube 설치 : [https://kys9261.github.io/2019/05/02/programming/devops/how-to-install-sonarqube-on-ubuntu/](https://kys9261.github.io/2019/05/02/programming/devops/how-to-install-sonarqube-on-ubuntu/)
- Window 에서 다운로드 및 실행 : [https://daddyprogrammer.org/post/817/sonarqube-analysis-intergrated-intellij/](https://daddyprogrammer.org/post/817/sonarqube-analysis-intergrated-intellij/)

- window
```plain text
docker run --name sonarqube  -p 9000:9000 --restart always -v d:/sonarqube/conf:/opt/sonarqube/conf  -v d:/sonarqube/data:/opt/sonarqube/data  -v d:/sonarqube/logs:/opt/sonarqube/logs  -v d:/sonarqube/extensions:/opt/sonarqube/extensions sonarqube
```

- 나스
```plain text
docker run --name sonarqube -p 9000:9000 -v /volume1/docker/sonarqube/conf:/opt/sonarqube/conf  -v /volume1/docker/sonarqube/data:/opt/sonarqube/data  -v /volume1/docker/sonarqube/logs:/opt/sonarqube/logs  -v /volume1/docker/sonarqube/extensions:/opt/sonarqube/extensions sonarqube
```

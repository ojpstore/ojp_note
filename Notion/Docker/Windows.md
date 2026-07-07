---
base: "[[Docker.base]]"
최종 편집 일시: 2024-12-13T12:56:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
![[img1.daumcdn.png]]

- 관련주소 
    - [https://betwe.tistory.com/entry/Docker-도커로-Windows-구축하기-Windows-in-Docker](https://betwe.tistory.com/entry/Docker-%EB%8F%84%EC%BB%A4%EB%A1%9C-Windows-%EA%B5%AC%EC%B6%95%ED%95%98%EA%B8%B0-Windows-in-Docker)
    - [https://hub.docker.com/r/dockurr/windows](https://hub.docker.com/r/dockurr/windows)
- 실행 (docker-compose)
```yaml
version: "3"
services:
  windows:
    image: dockurr/windows
    container_name: windows
    devices:
      - /dev/kvm
    cap_add:
      - NET_ADMIN
    ports:
      # 브라우저에서 접속 포트
      - 8006:8006
      # RDP 접속 포트
      - 3389:3389/tcp
      - 3389:3389/udp
    stop_grace_period: 2m
    restart: on-failure
    environment:
      # 윈도우 버전 명시
      VERSION: "win10"
      # RAM 사이즈
      RAM_SIZE: "12G"
      # CPU Core 개수
      CPU_CORES: "6"
      # 디스크 사이즈 : 기본 64G
      DISK_SIZE: "150G"
      #VERSION: "https://example.com/win.iso"
    volumes:
      # local 볼륨 mount
      - ./win10:/storage
      # 공유폴더 mount
      #- ./example:/shared
    #networks:
    #  vlan:
    #    ipv4_address: 192.168.0.100
#networks:
#  vlan:
#    external: true
출처: https://betwe.tistory.com/entry/Docker-도커로-Windows-구축하기-Windows-in-Docker [개발과 육아사이:티스토리]
```

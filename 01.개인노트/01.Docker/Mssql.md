---
base: "[[Docker.base]]"
cover: "[[Notion/Docker/attach/Mssql.jpeg]]"
최종 편집 일시: 2025-04-17T17:01:00
태그: []
인증: unverified
소유자:
  - 준표 오
---
- 컨테이너 생성 및 실행
```docker
docker run --name mssql2019 -p 1533:1433 -v /volume1/docker/mssql:/var/opt/mssql -e ACCEPT_EULA=Y -e TZ='Asia/Seoul' -e "MSSQL_COLLATION=Korean_Wansung_CI_AS" -e SA_PASSWORD=비밀번호 ojpfight/mssql-2019
docker run --name mssql2022 -p 1533:1433 -v /volume1/docker/mssql2022/data:/var/opt/mssql/data -v /volume1/docker/mssql2022/log:/var/opt/mssql/log -e ACCEPT_EULA=Y -e TZ='Asia/Seoul' -e "MSSQL_COLLATION=Korean_Wansung_CI_AS" -e SA_PASSWORD=비밀번호 mcr.microsoft.com/mssql/server:2022-latest
```
    - 비밀번호는 8자이상

- SA 암호 변경
```docker
docker exec -it sql1 /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 12345 -Q 'ALTER LOGIN SA WITH PASSWORD=12345'
```

- **Environment Variables**
    - ACCEPT_EULA : 최종 사용자 사용권 계약에 동의 함을 나타냅니다.
    - SA_PASSWORD : 컨테이너가 실행되면 SQL Server에 연결하는 데 사용되는 데이터베이스 시스템 관리자 (userid = 'sa') 암호 중요 사항 :이 비밀번호에는 대문자, 소문자, 숫자 및 영숫자가 아닌 기호와 같은 4 가지 범주 중 3 개 이상에서 8 자 이상이 포함되어야합니다.
    - MSSQL_PID : 컨테이너가 실행될 제품 ID (PID) 또는 에디션. 허용 가능한 값
        -  [https://docs.microsoft.com/ko-kr/sql/sql-server/editions-and-components-of-sql-server-2017?view=sql-server-ver15](https://docs.microsoft.com/ko-kr/sql/sql-server/editions-and-components-of-sql-server-2017?view=sql-server-ver15)
        -  Developer : 이것은 Developer Edition을 사용하여 컨테이너를 실행합니다 (MSSQL_PID 환경 변수가 제공되지 않은 경우 기본값 임)
        - Express : Express Edition을 사용하여 컨테이너를 실행합니다.
        - Standard : Standard Edition을 사용하여 컨테이너를 실행합니다.
        - Enterprise : Enterprise Edition을 사용하여 컨테이너를 실행합니다.
        - EnterpriseCore : Enterprise Edition Core를 사용하여 컨테이너를 실행합니다. PID와 연관된 에디션으로 컨테이너를 실행합니다.

- SQL Sever 에이전트 활성화하기 on Docker - bash
    - 관련 링크 : [https://babocoding.tistory.com/125](https://babocoding.tistory.com/125)
        - docker exec -it --user root mssql2019 "bash”
```plain text
/opt/mssql/bin/mssql-conf set sqlagent.enabled true
```

![[Notion/Docker/attach/mssql2022_agent_menu.png]]

![[Notion/Docker/attach/mssql_agent_bash.png]]

- 메일 세팅 관련
    - 관련주소 : [https://saddev.tistory.com/23](https://saddev.tistory.com/23)

- 메일보내기
```sql
EXEC msdb.dbo.sp_send_dbmail @profile_name='MailSend',
@recipients='ojpfight@gmail.com',
@subject='메일 발송 테스트',
@body='이 메일은 테스트 메일 입니다. 받고 그냥 지워 버리세요'
```

- 메일 로그 확인
```sql
select * from msdb.dbo.sysmail_event_log
```

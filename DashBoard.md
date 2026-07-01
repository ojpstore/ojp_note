---
cssclasses:
  - dashboard
  - has-wide-page
---



## 노트 리스트
- 🗃 최근 수정한 노트
  `$=dv.list(dv.pages('').sort(f=>f.file.mtime.ts,"desc").limit(5).file.link)`
- 📝 최근 작성한 노트
  `$=dv.list(dv.pages('').sort(f=>f.file.ctime.ts,"desc").limit(5).file.link)`
- 📁 폴더: 폴더명
  `$=dv.list(dv.pages('"폴더명"').sort(f=>f.file.ctime.ts,"desc").limit(5).file.link)`
- 🔖 태그: 태그명
  `$=dv.list(dv.pages('#태그명').sort(f=>f.file.name,"desc").limit(5).file.link)`
- ✅ 완료: 프로젝트
  `$=dv.list(dv.pages('').where(p => p.source === "값").sort(f=>f.file.name, "asc").limit(5).file.link)`

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MyBatis XML 매퍼 parameterType 분석 및 일괄 적용 스크립트 v4
"""

import os
import re
from collections import defaultdict

# ----------------- 경로 설정 -----------------
# 사용자의 요청 및 실제 워크스페이스 경로에 맞춰 드라이브 정규화
XML_ROOT = r"c:\panocean-v2\src\main\resources\mappers\som"
JAVA_ROOTS = [
    r"c:\panocean-v2\src\main\java\com\pan\som\dao",
    r"c:\panocean-v2\src\main\java\com\pan\som\function",
    r"c:\panocean-v2\src\main\java\com\pan\som\service",
]
OUTPUT_FILE = r"d:\panocean-v2-parameterType-list.md"
# ---------------------------------------------

TAG_PATTERN = re.compile(r'<(insert|update|delete)\s+[^>]*\bid=["\']([^"\']+)["\']', re.IGNORECASE)
NAMESPACE_PATTERN = re.compile(r'<mapper\s+[^>]*\bnamespace=["\']([^"\']+)["\']', re.IGNORECASE)
IMPORT_PATTERN = re.compile(r'^\s*import\s+([\w.]+);\s*$', re.MULTILINE)
PACKAGE_PATTERN = re.compile(r'^\s*package\s+([\w.]+);\s*$', re.MULTILINE)

# uxbDAO.insert/update 호출 패턴 (다양한 공백/개행 허용)
UXBDAO_CALL_PATTERN = re.compile(
    r'uxbDAO\.(insert|update|delete)\s*\(\s*["\']([^"\']+)["\']\s*,\s*([\w\.]+)',
    re.MULTILINE
)



PRIMITIVES = {
    'long','int','double','float','boolean','byte','short','char',
    'Long','Integer','Double','Float','Boolean','String','Object',
    'Hashtable','Collection','List','ArrayList','HashMap','Map','void',
    'map', 'string', 'int', 'long', 'hashmap'
}

def build_class_index():
    """
    프로젝트의 모든 Java 소스를 스캔하여 클래스명 -> FQCN 매핑 사전을 빌드합니다.
    이를 통해 동일 패키지에 있거나 import되지 않은 VO/DTO 클래스의 FQCN을 정확히 찾아냅니다.
    """
    class_map = {}
    java_search_root = r"d:\panocean-v2-xml\src\main\java"
    if not os.path.isdir(java_search_root):
        print(f"[경고] 자바 소스 루트가 존재하지 않습니다: {java_search_root}")
        return class_map

    class_decl_pat = re.compile(r'\b(?:class|interface|enum)\s+([A-Z]\w*)')

    print("Java 클래스 FQCN 인덱싱 중...")
    for root, _, files in os.walk(java_search_root):
        for f in files:
            if f.endswith(".java"):
                fpath = os.path.join(root, f)
                try:
                    with open(fpath, encoding="utf-8", errors="ignore") as file:
                        content = file.read()
                    pkg_m = PACKAGE_PATTERN.search(content)
                    if not pkg_m:
                        continue
                    pkg = pkg_m.group(1)
                    for m in class_decl_pat.finditer(content):
                        cname = m.group(1)
                        class_map[cname] = f"{pkg}.{cname}"
                except Exception:
                    pass
    print(f"인덱싱 완료: 총 {len(class_map)}개 클래스 등록")
    return class_map

def load_java_files():
    jf = {}
    for root_dir in JAVA_ROOTS:
        if not os.path.isdir(root_dir):
            print(f"[알림] Java 경로가 존재하지 않아 건너뜁니다: {root_dir}")
            continue
        for dp, _, fnames in os.walk(root_dir):
            for fn in fnames:
                if fn.endswith(".java"):
                    fp = os.path.join(dp, fn)
                    try:
                        with open(fp, encoding="utf-8", errors="ignore") as f:
                            jf[fp] = f.read()
                    except Exception:
                        pass
    return jf

def extract_xml_ids(xp):
    try:
        with open(xp, encoding="utf-8", errors="ignore") as f:
            c = f.read()
    except Exception:
        return None, []
    ns = NAMESPACE_PATTERN.search(c)
    return (ns.group(1) if ns else None), [(m.group(1).lower(), m.group(2)) for m in TAG_PATTERN.finditer(c)]

def get_imports(c):
    imp = {}
    for m in IMPORT_PATTERN.finditer(c):
        fqcn = m.group(1)
        imp[fqcn.rsplit(".", 1)[-1]] = fqcn
    return imp

def find_method_params(content, pos):
    """
    pos 위치 이전의 텍스트를 줄 단위로 역순 스캔하여, 가장 가까이 있는 메서드 선언부를 안전하게 찾습니다.
    정규식 백트래킹 문제를 원천 차단하기 위해 텍스트 스캔 방식을 사용합니다.
    """
    lines = content[:pos].splitlines()
    for line in reversed(lines):
        line_strip = line.strip()
        # 주석이나 어노테이션은 제외
        if line_strip.startswith('//') or line_strip.startswith('*') or line_strip.startswith('/*') or line_strip.startswith('@'):
            continue
        # 메서드 선언 조건 검사
        if ('public' in line_strip or 'protected' in line_strip or 'private' in line_strip) and '(' in line_strip:
            # { 가 다음 줄에 있을 수 있으므로 시그니처 괄호 매칭
            m = re.search(r'(\w+)\s*\(([^)]*)\)', line_strip)
            if m:
                return m.group(1), m.group(2)
    return None, None

def is_class_type(t):
    t2 = re.sub(r'<[^>]*>', '', t).strip()
    return t2 not in PRIMITIVES and bool(re.match(r'^[A-Z]\w*$', t2)) and 'Map' not in t2 and 'List' not in t2

def resolve_fqcn(name, imports, class_index):
    if '.' in name:
        return name
    # 1. import 구문에서 매핑 확인
    if name in imports:
        return imports[name]
    # 2. 전체 프로젝트 클래스 인덱스에서 매핑 확인
    if name in class_index:
        return class_index[name]
    return name

def analyze_java_files(java_files, id_set, class_index):
    results = defaultdict(list)
    for fpath, content in java_files.items():
        imports = get_imports(content)
        fname = os.path.basename(fpath)
        
        # 패키지 정보 파악
        pkg_m = PACKAGE_PATTERN.search(content)
        current_pkg = pkg_m.group(1) if pkg_m else ""
        
        for m in UXBDAO_CALL_PATTERN.finditer(content):
            dao_op, full_id, param_var = m.group(1), m.group(2), m.group(3).strip()
            if full_id not in id_set:
                continue
            
            method_name, params_str = find_method_params(content, m.start())
            found_type = None
            
            # 1. 메서드 파라미터에서 찾기
            if params_str:
                for param in params_str.split(","):
                    parts = param.strip().split()
                    if len(parts) >= 2:
                        ptype = re.sub(r'<[^>]*>', '', parts[-2]).strip()
                        pvar = parts[-1].strip()
                        if pvar == param_var and is_class_type(ptype):
                            found_type = ptype
                            break
            
            # 2. 메서드 내부 지역 변수 선언에서 찾기 (param_var가 단순 변수명일 때만 정규식 검색 수행)
            if not found_type and re.match(r'^\w+$', param_var):
                pat = re.compile(rf'\b([A-Z]\w*)\s+{re.escape(param_var)}\b\s*[=;]')
                for lm in pat.finditer(content[:m.start()]):
                    cand = lm.group(1).strip()
                    if is_class_type(cand):
                        found_type = cand
            
            if not found_type:
                continue
            
            # FQCN 결정
            fqcn = resolve_fqcn(found_type, imports, class_index)
            # 만약 패키지명이 결정 안되었고 동일 패키지명일 가능성이 있으면 보완
            if '.' not in fqcn and current_pkg:
                fqcn = f"{current_pkg}.{fqcn}"
                
            sig = f"{method_name}({params_str.strip()})" if method_name else "unknown"
            results[full_id].append((fname, dao_op, sig, found_type, fqcn))
    return results

def pick_entries(entries):
    dto = [e for e in entries if e[3].endswith("DTO")]
    vo  = [e for e in entries if e[3].endswith("VO")]
    oth = [e for e in entries if not e[3].endswith("DTO") and not e[3].endswith("VO")]
    if dto and vo:
        return dto, "VO/DTO 혼재 → DTO 적용"
    if dto:
        return dto, "DTO 적용"
    if vo:
        return vo, "VO 적용"
    return oth, "클래스 적용"

def generate_md(xml_data, java_results):
    lines = ["# MyBatis XML ParameterType 분석 결과\n\n",
             f"- **분석 XML 폴더**: `{XML_ROOT}`\n\n---\n\n"]
             
    for xp in sorted(xml_data.keys(), key=lambda p: os.path.basename(p).lower()):
        data = xml_data[xp]
        ns = data["namespace"] or ""
        fname = os.path.basename(xp)
        rows = []
        
        for tt, qid in data["ids"]:
            if tt not in ("insert","update","delete"):
                continue
            full_id = f"{ns}.{qid}" if ns else qid
            entries = java_results.get(full_id, [])
            if not entries:
                continue
            
            apply, note = pick_entries(entries)
            fqcns = list(dict.fromkeys([e[4] for e in apply]))
            fqcn_str = "<br/>".join(fqcns)
            
            seen = set()
            funcs = []
            for e in entries:
                k = f"{e[0]}::{e[2]}"
                if k not in seen:
                    seen.add(k)
                    funcs.append(f"{e[0]} :: uxbDAO.{e[1]}({e[2]})")
            
            rows.append((qid, "<br/>".join(funcs), fqcn_str, note))
            
        if not rows:
            continue
            
        lines += [f"\n## {fname}\n\n", f"**Namespace**: `{ns}`\n\n",
                  '<table style="width:90%;border-collapse:collapse;margin:20px 0;font-size:13px;min-width:800px;">\n',
                  '  <thead><tr style="background-color:#2b3a4a;text-align:left;font-weight:bold;">\n',
                  '    <th style="padding:12px 15px;border:1px solid #dddddd;color:#ffffff;width:15%;">id</th>\n',
                  '    <th style="padding:12px 15px;border:1px solid #dddddd;color:#ffffff;width:42%;">함수</th>\n',
                  '    <th style="padding:12px 15px;border:1px solid #dddddd;color:#ffffff;width:30%;">권장 parameterType (FQCN)</th>\n',
                  '    <th style="padding:12px 15px;border:1px solid #dddddd;color:#ffffff;width:13%;">비고</th>\n',
                  '  </tr></thead>\n  <tbody>\n']
                  
        for qid, func_str, fqcn_str, note in rows:
            lines += [
                '    <tr>\n',
                f'      <td style="padding:12px 15px;border:1px solid #dddddd;color:#ffffff;font-weight:bold;word-break:break-all;">{qid}</td>\n',
                f'      <td style="padding:12px 15px;border:1px solid #dddddd;color:#ffffff;word-break:break-all;font-size:12px;">{func_str}</td>\n',
                f'      <td style="padding:12px 15px;border:1px solid #dddddd;color:#ffffff;font-weight:bold;word-break:break-all;">{fqcn_str}</td>\n',
                f'      <td style="padding:12px 15px;border:1px solid #dddddd;color:#ffffff;font-size:12px;">{note}</td>\n',
                '    </tr>\n'
            ]
        lines.append('  </tbody>\n</table>\n\n')
        
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("".join(lines))
    print(f"[MD 저장] {OUTPUT_FILE}")

def apply_xml(xml_data, java_results):
    total = 0
    for xp, data in xml_data.items():
        ns = data["namespace"] or ""
        fname = os.path.basename(xp)
        
        if not os.path.isfile(xp):
            continue
        try:
            with open(xp, encoding="utf-8", errors="ignore") as f:
                content = f.read()
        except Exception:
            continue
            
        modified = content
        changed = 0
        
        for tt, qid in data["ids"]:
            if tt not in ("insert","update","delete"):
                continue
            full_id = f"{ns}.{qid}" if ns else qid
            entries = java_results.get(full_id, [])
            if not entries:
                continue
                
            apply, _ = pick_entries(entries)
            fqcns = list(dict.fromkeys([e[4] for e in apply]))
            if not fqcns:
                continue
                
            target_fqcn = fqcns[0]
            
            # xml 태그의 parameterType="xxx" 부분을 교체하거나 추가하는 정규식
            # 1. 이미 parameterType 속성이 존재하는 경우 교체
            pat_exist = re.compile(
                rf'(<{tt}\s+[^>]*\bid=["\']' + re.escape(qid) + r'["\'][^>]*\bparameterType=)["\'][^"\']*["\']',
                re.IGNORECASE
            )
            
            # 2. parameterType 속성이 아예 없는 경우 추가 (id 속성 뒤에 바로 추가)
            pat_missing = re.compile(
                rf'(<{tt}\s+[^>]*\bid=["\']' + re.escape(qid) + r'["\'])(?![^>]*\bparameterType=)',
                re.IGNORECASE
            )
            
            new_content = pat_exist.sub(rf'\1"{target_fqcn}"', modified)
            if new_content == modified:
                new_content = pat_missing.sub(rf'\1 parameterType="{target_fqcn}"', modified)
                
            if new_content != modified:
                modified = new_content
                changed += 1
                print(f"  [적용 대기] {fname}::{qid} → {target_fqcn}")
                
        if changed > 0:
            try:
                with open(xp, "w", encoding="utf-8") as f:
                    f.write(modified)
                total += changed
                print(f"  [저장 완료] {xp} ({changed}건)")
            except Exception as e:
                print(f"  [에러] {xp}: {e}")
                
    print(f"\n총 {total}건 XML 변경 완료")

def main():
    print("=== MyBatis parameterType 일괄 마이그레이션 도구 ===")
    
    # 0. 클래스 FQCN 사전 인덱싱
    class_index = build_class_index()
    
    # 1. Java 파일 로딩
    print("1. Java 소스코드 스캔 중...", flush=True)
    jf = load_java_files()
    print(f"   로드된 Java 파일 수: {len(jf)}개")

    # 2. XML 파일 수집
    print("2. XML 매퍼 파일 검색 중...", flush=True)
    xml_files = []
    for dp, _, fns in os.walk(XML_ROOT):
        for fn in fns:
            if fn.lower().endswith(".xml"):
                xml_files.append(os.path.join(dp, fn))
    print(f"   검색된 XML 파일 수: {len(xml_files)}개")

    # 3. XML id 추출
    print("3. XML Tag ID 추출 중...", flush=True)
    xml_data = {}
    id_set = set()
    for xp in xml_files:
        ns, ids = extract_xml_ids(xp)
        if ids:
            xml_data[xp] = {"namespace": ns, "ids": ids}
            for tt, qid in ids:
                if tt in ("insert","update","delete"):
                    id_set.add(f"{ns}.{qid}" if ns else qid)
    print(f"   대상 ID 수: {len(id_set)}개")

    # 4. Java 소스 매핑 분석
    print("4. Java-MyBatis 매핑 분석 중...", flush=True)
    jr = analyze_java_files(jf, id_set, class_index)
    print(f"   매핑 성공한 ID 수: {len(jr)}개")

    # 5. 리포트 생성
    print("5. 마크다운 분석 리포트 생성 중...", flush=True)
    generate_md(xml_data, jr)

    # 6. XML 파일에 FQCN 자동 적용
    print("6. XML 매퍼 파일 업데이트 중...", flush=True)
    apply_xml(xml_data, jr)

    print("\n=== 마이그레이션 완료 ===")

if __name__ == "__main__":
    main()

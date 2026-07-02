import os
import re
import glob

def parse_xml_for_ids(file_path):
    ids = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Find all <insert id="..."> and <update id="...">
        matches = re.findall(r'<(?:insert|update)\s+id=["\']([^"\']+)["\']', content)
        ids = list(set(matches))
    return ids

def find_java_usages(java_roots, target_id):
    usages = []
    # Search for uxbDAO.insert("id", ...) or uxbDAO.update("id", ...)
    # Allowing for flexible spacing/formatting
    pattern = re.compile(rf'uxbDAO\.(?:insert|update)\s*\(\s*["\']{re.escape(target_id)}["\']\s*,\s*([^,\)]+)\s*\)')
    
    for root in java_roots:
        for java_file in glob.glob(os.path.join(root, "**", "*.java"), recursive=True):
            try:
                with open(java_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    matches = pattern.findall(content)
                    if matches:
                        for param in matches:
                            usages.append({
                                'file': os.path.basename(java_file),
                                'param_name': param.strip(),
                                'full_path': java_file,
                                'code_snippet': f'uxbDAO.insert("{target_id}", {param.strip()})' # Need adjustment if it's update
                            })
            except Exception:
                continue
    return usages

def get_param_type(java_file_path, param_name):
    # Rough parsing to find the type of 'param_name' in the method signature
    with open(java_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Look for method signature: Type param_name
        # Simple regex for method signature
        match = re.search(rf'(\w+)\s+{re.escape(param_name)}\s*[\),]', content)
        if match:
            type_name = match.group(1)
            # Find import for type_name
            import_match = re.search(rf'import\s+(.*\.\b{re.escape(type_name)}\b)', content)
            if import_match:
                return import_match.group(1)
            return type_name # Return simple name if FQCN not found
    return None

def main():
    xml_dir = "C:/hermes-work/panocean-v2/src/main/resources/mappers/som"
    java_dirs = [
        "C:/hermes-work/panocean-v2/src/main/java/com/pan/som/dao",
        "C:/hermes-work/panocean-v2/src/main/java/com/pan/som/function",
        "C:/hermes-work/panocean-v2/src/main/java/com/pan/som/dao/service"
    ]
    
    md_content = "# MyBatis ParameterType Analysis Report\n\n"
    
    xml_files = glob.glob(os.path.join(xml_dir, "**", "*.xml"), recursive=True)
    
    for xml_file in xml_files:
        ids = parse_xml_for_ids(xml_file)
        if not ids: continue
        
        md_content += f"## {os.path.basename(xml_file)}\n\n"
        md_content += "| id | 호출 함수 | 권장 parameterType (FQCN) |\n"
        md_content += "|---|---|---|\n"
        
        for tid in ids:
            usages = find_java_usages(java_dirs, tid)
            for use in usages:
                fqcn = get_param_type(use['full_path'], use['param_name'])
                if fqcn and not any(m in fqcn.lower() for m in ['map', 'long', 'string', 'object']):
                    md_content += f"| {tid} | {use['file']} | {fqcn} |\n"
        md_content += "\n"
        
    with open("D:/mybatis_parameterType.md", 'w', encoding='utf-8') as f:
        f.write(md_content)

main()

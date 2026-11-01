import pathlib, re
t=pathlib.Path(r'D:/Downloads/cv/_haf_sync/js/project-data.js').read_text(encoding='utf-8')
for m in re.finditer(r"slug:\s*'([^']+)'.*?liveUrl:\s*'([^']*)'", t, flags=re.S):
    print(m.group(1), "=>", m.group(2) or "(empty)")

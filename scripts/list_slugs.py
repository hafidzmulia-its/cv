import pathlib, re
txt = pathlib.Path(r'D:/Downloads/cv/_haf_sync/js/project-data.js').read_text(encoding='utf-8')
for m in re.finditer(r"slug:\s*'([^']+)'", txt):
    print(m.group(1))

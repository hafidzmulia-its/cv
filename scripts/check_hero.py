import pathlib
for path in [r'D:/Downloads/haf/index.html', r'D:/Downloads/cv/_haf_sync/index.html']:
    txt = pathlib.Path(path).read_text(encoding='utf-8')
    for line in txt.splitlines():
        if 'hero-title' in line or 'hero-subtitle' in line:
            print(path, line.strip())

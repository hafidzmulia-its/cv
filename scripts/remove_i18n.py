import pathlib, re
for name in ['index.html','portfolio.html','porto-show.html']:
    p = pathlib.Path(f'D:/Downloads/cv/_haf_sync/{name}')
    if not p.exists(): continue
    t = p.read_text(encoding='utf-8')
    # remove i18n script tag
    t = t.replace('    <script src="js/i18n.js"></script>\n', '')
    t = t.replace('<script src="js/i18n.js"></script>\n    ', '')
    # remove data-i18n attributes (keep text)
    t = re.sub(r'\s+data-i18n="[^"]+"', '', t)
    t = re.sub(r'\s+data-i18n-placeholder="[^"]+"', '', t)
    p.write_text(t, encoding='utf-8')
    print(f'cleaned {name}')

# Remove locales and i18n.js
import shutil, pathlib, os
for path in [r'D:/Downloads/cv/_haf_sync/js/i18n.js', r'D:/Downloads/cv/_haf_sync/locales']:
    p = pathlib.Path(path)
    if p.exists():
        if p.is_dir():
            shutil.rmtree(p)
        else:
            p.unlink()
        print(f'removed {path}')

# Also remove from haf
for path in [r'D:/Downloads/haf/js/i18n.js', r'D:/Downloads/haf/locales']:
    p = pathlib.Path(path)
    if p.exists():
        if p.is_dir():
            shutil.rmtree(p)
        else:
            p.unlink()
        print(f'removed haf {path}')

# Remove i18n script from haf html as well (they were synced)
for name in ['index.html','portfolio.html','porto-show.html']:
    for base in [r'D:/Downloads/haf', r'D:/Downloads/cv/_haf_sync']:
        p = pathlib.Path(f'{base}/{name}')
        if p.exists():
            t = p.read_text(encoding='utf-8')
            if 'js/i18n.js' in t:
                t = t.replace('    <script src="js/i18n.js"></script>\n', '')
                t = t.replace('<script src="js/i18n.js"></script>\n    ', '')
                t = re.sub(r'\s+data-i18n="[^"]+"', '', t)
                t = re.sub(r'\s+data-i18n-placeholder="[^"]+"', '', t)
                p.write_text(t, encoding='utf-8')
                print(f'cleaned haf {name}')

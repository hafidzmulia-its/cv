import pathlib
for path in [r'D:/Downloads/cv/_haf_sync/index.html', r'D:/Downloads/haf/index.html']:
    p = pathlib.Path(path)
    t = p.read_text(encoding='utf-8')
    # Ensure hero title is single, remove duplication if exists (e.g., Hafidz MuliaHafidz Mulia)
    t = t.replace('Hafidz MuliaHafidz Mulia', 'Hafidz Mulia')
    # Update subtitle to match image: Product-Minded Software Engineer | Data-Driven Problem Solver
    # The current subtitle is Product Builder | Technical Problem Solver | Student Leader
    # Replace with new subtitle as per image, but keep data-i18n
    t = t.replace('Product Builder | Technical Problem Solver | Student Leader', 'Product-Minded Software Engineer | Data-Driven Problem Solver')
    # Also update en.json subtitle to match?
    p.write_text(t, encoding='utf-8')
    print(f'fixed {path}')

# Update locales en.json subtitle to match new hero
import json, pathlib
en_p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/locales/en.json')
en = json.loads(en_p.read_text(encoding='utf-8'))
en['hero.subtitle'] = 'Product-Minded Software Engineer | Data-Driven Problem Solver'
en_p.write_text(json.dumps(en, indent=2), encoding='utf-8')
id_p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/locales/id.json')
id_data = json.loads(id_p.read_text(encoding='utf-8'))
# keep id as is, but ensure hero subtitle Indonesian maybe keep? No change
print('updated locales en hero.subtitle')

# Also ensure haf locales updated
import shutil, pathlib
shutil.copy(r'D:/Downloads/cv/_haf_sync/locales/en.json', r'D:/Downloads/haf/locales/en.json')
print('synced locales to haf')

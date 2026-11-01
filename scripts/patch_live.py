import pathlib, re
p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/js/project-data.js')
t = p.read_text(encoding='utf-8')
t = re.sub(r"(slug:\s*'sidedikk'.*?liveUrl:\s*)''", r"\1'https://sidedikk.my.id'", t, flags=re.S)
t = re.sub(r"(slug:\s*'portal-tpq'.*?liveUrl:\s*)''", r"\1'https://tpqnh.my.id'", t, flags=re.S)
t = re.sub(r"(slug:\s*'sadariyuk'.*?liveUrl:\s*)''", r"\1'https://sadariyul.vercel.app'", t, flags=re.S)
# also update detailMap liveUrl if present? add if not
# Ensure detailMap entries have liveUrl synced via project liveUrl, no need
p.write_text(t, encoding='utf-8')
print('patched')
txt = p.read_text(encoding='utf-8')
for m in re.finditer(r"slug:\s*'(sidedikk|portal-tpq|sadariyuk)'.*?liveUrl:\s*'([^']*)'", txt, flags=re.S):
    print(m.group(1), "=>", m.group(2))

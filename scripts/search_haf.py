import pathlib, re
base='C:/Users/kenji/.codex/sessions/2026'
import pathlib as pl
hits=[]
for fp in pl.Path(base).rglob('*.jsonl'):
    try:
        txt = fp.read_text(encoding='utf-8', errors='ignore')
        if '_haf_sync' in txt:
            m = re.search(r'"cwd"\s*:\s*"([^"]+)"', txt)
            cwd = m.group(1) if m else '?'
            cnt = txt.count('_haf_sync')
            hits.append((str(fp), cwd, cnt))
    except: pass
print(len(hits))
for p,cwd,cnt in sorted(hits, key=lambda x: x[2], reverse=True)[:30]:
    print(cnt, cwd, pl.Path(p).name)

import pathlib, re
fp = pathlib.Path(r'C:\Users\kenji\.codex\sessions\2026\05\29\rollout-2026-05-29T13-12-07-019e725c-760a-7621-8f1f-f09e43191edc.jsonl')
txt = fp.read_text(encoding='utf-8', errors='ignore')
for m in re.finditer(r'_haf_sync.{0,600}', txt):
    s=m.group(0).replace('\n',' ')[:700]
    print(s[:700])
    print('---')
    break

# also find sync instructions
for m in re.finditer(r'sync.{0,300}', txt, flags=re.I):
    s=m.group(0).replace('\n',' ')
    if 'haf' in s.lower():
        print('SYNC:', s[:500])

# try second file
fp2 = pathlib.Path(r'C:\Users\kenji\.codex\sessions\2026\04\01\rollout-2026-04-01T12-46-22-019d4794-1d19-70f1-abc3-3b30d71e2d97.jsonl')
txt2 = fp2.read_text(encoding='utf-8', errors='ignore')
print('=== FILE2 ===')
for m in re.finditer(r'_haf_sync.{0,600}', txt2):
    print(m.group(0).replace('\n',' ')[:700])
    print('---')
    break
for m in re.finditer(r'D:\\\\Downloads\\\\haf.{0,300}', txt2):
    print('HAF:', m.group(0).replace('\n',' ')[:500])

fp3 = pathlib.Path(r'C:\Users\kenji\.codex\sessions\2026\05\04\rollout-2026-05-04T17-58-14-019df2a3-80a2-7cc3-9336-c3907a884a4b.jsonl')
txt3 = fp3.read_text(encoding='utf-8', errors='ignore')
print('=== FILE3 ===')
for m in re.finditer(r'_haf_sync.{0,800}', txt3):
    print(m.group(0).replace('\n',' ')[:800])
    print('---')
    break

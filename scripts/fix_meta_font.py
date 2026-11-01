import pathlib
p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
t = p.read_text(encoding='utf-8')
# remove previous otherwise block
import re
t = re.sub(r'\n/\* otherwise font: Narrative.*?\}\n', '\n', t, flags=re.S)
# add new: essentials/build system same as narrative
extra = """
/* essentials & build system same font as narrative project overview */
.meta-v2 dt, .meta-v2 dd, .prose-v2 p, .highlights-v2 li{font-family:'Inter', sans-serif;}
.meta-v2 dt{font-size:1rem; font-weight:400; line-height:1.7; color:var(--muted-foreground); text-transform:none; letter-spacing:0;}
.meta-v2 dd{font-size:1rem; font-weight:400; line-height:1.7; color:var(--muted-foreground);}
.meta-v2 dt+dd{margin-top:.1rem}
"""
if 'essentials & build system same font' not in t:
    # remove old prose overrides if any? ensure clean
    t = t.replace(".prose-v2 p{font-family:'Inter', sans-serif; font-size:.95rem; font-weight:600;}", "")
    t += extra
    p.write_text(t, encoding='utf-8')
    print('updated meta to match narrative')
else:
    print('exists')

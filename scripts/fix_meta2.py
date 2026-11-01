import pathlib
p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
t = p.read_text(encoding='utf-8')
# remove any previous prose overrides from otherwise
import re
# remove old prose/highlights 0.95rem 600 lines
t = t.replace(".prose-v2 p{font-family:'Inter', sans-serif; font-size:.95rem; font-weight:600;}", "")
t = t.replace(".highlights-v2 li{font-family:'Inter', sans-serif; font-size:.95rem; font-weight:600;}", "")
t = t.replace(".highlights-v2 li span:last-child{font-weight:600;}", "")
# ensure final overrides for all to match narrative: 1rem 400 Inter muted
override = """
/* final: all detail text same as narrative */
.prose-v2 p, .highlights-v2 li, .highlights-v2 li span, .meta-v2 dt, .meta-v2 dd{font-family:'Inter', sans-serif; font-size:1rem; font-weight:400; line-height:1.7; color:var(--muted-foreground);}
.meta-v2 dt{letter-spacing:0; text-transform:none;}
.meta-v2 dd a{font-weight:400;}
"""
if 'final: all detail text same as narrative' not in t:
    t += override
    p.write_text(t, encoding='utf-8')
    print('applied final')
else:
    print('exists')

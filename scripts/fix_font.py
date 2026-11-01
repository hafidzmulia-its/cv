import pathlib
p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
t = p.read_text(encoding='utf-8')
extra = """
/* font standardization for detail essentials/build system */
.card-v2, .detail-hero-v2, .meta-v2, .prose-v2, .highlights-v2, .tags-v2, .gallery-caption-v2 {font-family:'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;}
.card-v2 h2, .card-v2 h3, .detail-title-v2, .detail-eyebrow-v2 {font-family:'Montserrat', sans-serif;}
.meta-v2 dt{font-family:'Inter', sans-serif; font-size:.75rem;}
.meta-v2 dd{font-family:'Inter', sans-serif; font-size:.95rem; font-weight:600;}
.card-v2 .kicker{font-family:'Inter', sans-serif;}
"""
if 'font standardization for detail' not in t:
    p.write_text(t+extra, encoding='utf-8')
    print('added font standardization')
else:
    print('exists')

import pathlib
p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
t = p.read_text(encoding='utf-8')
extra = """
/* center Project Catalog header (index) */
.projects-header{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:.6rem;margin-bottom:1.2rem}
.projects-header>div{max-width:720px;text-align:center}
.projects-header .section-title{margin-bottom:.4rem;text-align:center}
.projects-header .projects-intro{margin:0 auto;text-align:center;max-width:640px}
.projects-header .projects-count{margin:0;text-align:center;align-self:center}
"""
if 'center Project Catalog header' not in t:
    p.write_text(t+extra, encoding='utf-8')
    print('centered')
else:
    print('exists')

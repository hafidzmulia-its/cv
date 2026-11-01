import pathlib
p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
t = p.read_text(encoding='utf-8')
extra = """
.nav-email{font-weight:600}
.nav-email:hover{color:var(--primary) !important}
@media(max-width:767px){
  .nav-email{width:100%;text-align:left;padding:.75rem 1rem;border-radius:.5rem}
  .nav-email:hover{background:rgba(124,58,237,.05)}
}
.lang-switch button.active{background:var(--primary) !important;color:#fff !important;border-color:var(--primary) !important}
"""
if '.nav-email' not in t or 'lang-switch button.active' not in t:
    # ensure not duplicate
    if '.nav-email:hover' not in t:
        p.write_text(t+extra, encoding='utf-8')
        print('added nav email css')
    else:
        print('exists partial')
else:
    print('exists')

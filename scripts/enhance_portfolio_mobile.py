import pathlib
p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
t = p.read_text(encoding='utf-8')
extra = """
/* Enhanced mobile UI for portfolio.html toolbar + filter */
@media(max-width:767px){
  .portfolio-hero{padding:5.5rem 0 1.2rem}
  .portfolio-toolbar{gap:1rem !important; align-items:stretch !important}
  .portfolio-search{flex:1 1 auto !important; max-width:100% !important;}
  .portfolio-search input{height:2.9rem !important; font-size:.92rem !important; padding-left:2.4rem !important; border-radius:999px !important;}
  .portfolio-search svg{left:.85rem !important; width:16px !important; height:16px !important;}
  .portfolio-sort{flex-direction:row !important; align-items:center !important; justify-content:space-between !important; gap:.6rem !important; flex-wrap:nowrap !important;}
  .portfolio-sort label{font-size:.75rem !important; letter-spacing:.07em !important;}
  .portfolio-sort select{flex:1 1 auto !important; min-width:0 !important; height:2.7rem !important; font-size:.88rem !important; border-radius:999px !important; padding:.5rem .9rem !important;}
  .portfolio-meta{font-size:.82rem !important; text-align:right !important; white-space:nowrap !important; flex:0 0 auto !important;}
  .project-filter-bar{margin:0 -0.75rem !important; padding:0 0.75rem .2rem !important; gap:0 !important; border-bottom:1px solid var(--border) !important;}
  .project-filter-btn{padding:.8rem .9rem !important; font-size:.84rem !important;}
  .filter-divider{margin:0 .35rem !important}
  /* portfolio grid cards tighter */
  .projects-grid{gap:1rem !important}
  .project-content{padding:1.1rem !important}
}
/* Detail page mobile polish */
@media(max-width:767px){
  .detail-shell-v2{padding:1.2rem 0 2rem !important}
  .detail-hero-v2{padding:1.3rem !important; border-radius:1.2rem !important}
  .detail-title-v2{font-size:1.85rem !important; line-height:1.15 !important}
  .detail-summary-v2{font-size:.98rem !important}
  .detail-pills-v2{gap:.45rem !important}
  .detail-pill-v2{padding:.4rem .7rem !important; font-size:.8rem !important}
  .detail-actions-v2{gap:.5rem !important}
  .detail-actions-v2 .btn-v2{flex:1 1 calc(50% - .25rem); min-height:2.7rem !important; font-size:.88rem !important; padding:.6rem .9rem !important}
  .card-v2{padding:1.15rem !important; border-radius:1.2rem !important}
  .card-v2-head h2{font-size:1.25rem !important}
  .gallery-stage-v2{border-radius:1rem !important}
  .gallery-img-v2{max-height:52vh !important}
  .gallery-nav-v2{width:2.2rem !important; height:2.2rem !important; font-size:.9rem !important}
  .gallery-bar-v2{flex-wrap:wrap !important; gap:.5rem !important}
  .detail-layout-v2{gap:1rem !important}
}
"""
if 'Enhanced mobile UI for portfolio' not in t:
    p.write_text(t+extra, encoding='utf-8')
    print('enhanced mobile')
else:
    print('exists')

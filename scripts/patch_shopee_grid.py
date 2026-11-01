import pathlib
p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
t = p.read_text(encoding='utf-8')
extra = """
/* Shopee-like 2-col grid on mobile: hide description, show only kicker/title/role/tags */
@media(max-width:767px){
  .projects-grid{grid-template-columns:repeat(2, 1fr) !important; gap:.75rem !important;}
  .project-card{border-radius:.9rem !important; overflow:hidden !important;}
  .project-card .project-image-container{aspect-ratio:1/1 !important;}
  .project-card .project-content{padding:.75rem !important;}
  .project-card .project-kicker{font-size:.68rem !important; margin-bottom:.2rem !important; letter-spacing:.03em !important;}
  .project-card .project-title{font-size:.88rem !important; line-height:1.25 !important; margin-bottom:.2rem !important; display:-webkit-box; -webkit-line-clamp:2; -webkit-box-orient:vertical; overflow:hidden; min-height:2.2rem;}
  .project-card .project-roleline{font-size:.74rem !important; margin-bottom:.45rem !important; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;}
  .project-card .project-description{display:none !important;}
  .project-card .project-meta{display:none !important;}
  .project-card .project-links{display:none !important;}
  .project-card .project-tags{gap:.3rem !important; margin-bottom:0 !important; flex-wrap:wrap !important;}
  .project-card .project-tag{font-size:.62rem !important; padding:.18rem .38rem !important; border-radius:.3rem !important;}
  .project-card .project-tag:nth-child(n+4){display:none !important;}
  .project-card .project-status-badge{font-size:.65rem !important; padding:.25rem .5rem !important; top:.5rem !important; right:.5rem !important;}
}
@media(max-width:480px){
  .projects-grid{gap:.6rem !important;}
  .project-card .project-content{padding:.6rem !important;}
}
"""
if 'Shopee-like 2-col' not in t:
    p.write_text(t+extra, encoding='utf-8')
    print('added shopee grid')
else:
    print('exists')

# Also make cards clickable on mobile via JS
for js_path in [r'D:/Downloads/cv/_haf_sync/js/script.js', r'D:/Downloads/cv/_haf_sync/js/portfolio.js']:
    pp = pathlib.Path(js_path)
    tt = pp.read_text(encoding='utf-8')
    if 'shopee-card-click' not in tt:
        # Add after renderProjects or renderGrid
        # Find where grid.innerHTML is set and add click handler
        # Add a delegated click on projects-grid
        snippet = """
  // shopee mobile: tap card to go to detail (since links hidden)
  document.addEventListener('click', (e)=>{
    if(window.innerWidth>767) return;
    const card=e.target.closest('.project-card');
    if(!card) return;
    if(e.target.closest('a, button')) return;
    const slug = card.querySelector('[href*="porto-show.html?project="]')?.getAttribute('href')?.match(/project=([^&]+)/)?.[1];
    if(slug) location.href=`porto-show.html?project=${slug}`;
  });
"""
        # Insert before final }); of DOMContentLoaded
        # Find last occurrence of "});" at end
        if '});' in tt:
            # Insert before last });
            idx = tt.rfind('});')
            tt = tt[:idx] + snippet + tt[idx:]
            pp.write_text(tt, encoding='utf-8')
            print(f'added card click for {js_path}')
        else:
            print('no closing found')
    else:
        print(f'already has shopee click {js_path}')

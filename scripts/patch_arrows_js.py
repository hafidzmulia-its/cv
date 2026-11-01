import pathlib

# Patch script.js (index)
p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/js/script.js')
t = p.read_text(encoding='utf-8')
arrow_code = """
    function setupFilterArrows(){
      if(document.querySelector('.filter-wrap')) return;
      const fb=document.getElementById('project-filter-bar');
      if(!fb) return;
      const wrap=document.createElement('div'); wrap.className='filter-wrap';
      fb.parentNode.insertBefore(wrap, fb);
      wrap.appendChild(fb);
      const left=document.createElement('button'); left.className='filter-arrow left'; left.type='button'; left.innerHTML='‹'; left.setAttribute('aria-label','Scroll left');
      const right=document.createElement('button'); right.className='filter-arrow right'; right.type='button'; right.innerHTML='›'; right.setAttribute('aria-label','Scroll right');
      wrap.prepend(left); wrap.append(right);
      left.addEventListener('click',()=> fb.scrollBy({left:-220,behavior:'smooth'}));
      right.addEventListener('click',()=> fb.scrollBy({left:220,behavior:'smooth'}));
      const upd=()=>{ left.disabled=fb.scrollLeft<=2; right.disabled=fb.scrollLeft+fb.clientWidth>=fb.scrollWidth-2; };
      fb.addEventListener('scroll', upd); window.addEventListener('resize', upd); upd();
    }
    setupFilterArrows();
"""
# Find place after const getProjectsForFilter
if 'setupFilterArrows' not in t:
    # insert before filterBar.addEventListener
    t = t.replace("    filterBar.addEventListener('click',", arrow_code + "\n    filterBar.addEventListener('click',")
    p.write_text(t, encoding='utf-8')
    print('patched script.js arrows')
else:
    print('already patched script.js')

# Patch portfolio.js
pp = pathlib.Path(r'D:/Downloads/cv/_haf_sync/js/portfolio.js')
tt = pp.read_text(encoding='utf-8')
arrow_code2 = """
  function setupFilterArrows(){
    if(document.querySelector('.filter-wrap')) return;
    const fb=document.getElementById('portfolio-filter-bar')||document.getElementById('project-filter-bar');
    if(!fb) return;
    const wrap=document.createElement('div'); wrap.className='filter-wrap';
    fb.parentNode.insertBefore(wrap, fb);
    wrap.appendChild(fb);
    const left=document.createElement('button'); left.className='filter-arrow left'; left.type='button'; left.innerHTML='‹'; left.setAttribute('aria-label','Scroll left');
    const right=document.createElement('button'); right.className='filter-arrow right'; right.type='button'; right.innerHTML='›'; right.setAttribute('aria-label','Scroll right');
    wrap.prepend(left); wrap.append(right);
    left.addEventListener('click',()=> fb.scrollBy({left:-220,behavior:'smooth'}));
    right.addEventListener('click',()=> fb.scrollBy({left:220,behavior:'smooth'}));
    const upd=()=>{ left.disabled=fb.scrollLeft<=2; right.disabled=fb.scrollLeft+fb.clientWidth>=fb.scrollWidth-2; };
    fb.addEventListener('scroll', upd); window.addEventListener('resize', upd); upd();
  }
  setupFilterArrows();
"""
if 'setupFilterArrows' not in tt:
    # insert before bar.addEventListener
    tt = tt.replace("  bar.addEventListener('click',", arrow_code2 + "\n  bar.addEventListener('click',")
    # also handle case where bar variable is named differently: in portfolio.js it's bar
    pp.write_text(tt, encoding='utf-8')
    print('patched portfolio.js arrows')
else:
    print('already patched portfolio.js')

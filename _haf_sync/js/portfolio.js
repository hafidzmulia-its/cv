document.addEventListener('DOMContentLoaded', function(){
  const grid=document.getElementById('portfolio-grid');
  const bar=document.getElementById('portfolio-filter-bar');
  const count=document.getElementById('portfolio-count');
  const search=document.getElementById('portfolio-search');
  const sortSel=document.getElementById('portfolio-sort');
  const clearBtn=document.getElementById('clear-filter-btn');
  let projects=Array.isArray(window.portfolioProjects)?[...window.portfolioProjects]:[];
  const paramsRaw=new URLSearchParams(location.search);
  const isProperindo=paramsRaw.has('properindo') || paramsRaw.get('filter')==='properindo' || paramsRaw.get('view')==='properindo';
  if(isProperindo){
    const allow=['real-keke','hisurabaya','erapor','soulmom','sidedikk','literasik'];
    projects=projects.filter(p=>allow.includes(p.slug));
  }
  if(!grid||!bar) return;

  const filters=[
    {id:'all',label:'All'},
    {id:'featured',label:'Featured'},
    {id:'nextjs',label:'Next.js / React'},
    {id:'laravel',label:'Laravel / PHP'},
    {id:'gis',label:'GIS / Maps'},
    {id:'health',label:'Health-Tech'},
    {id:'education',label:'Education'},
    {id:'systems',label:'Internal Systems'},
    {id:'frontend',label:'Frontend'},
    {id:'experiments',label:'Experiments'}
  ];

  const params=new URLSearchParams(location.search);
  let active=isProperindo?'all':(params.get('filter')||'all');
  if(!filters.some(f=>f.id===active)) active='all';
  let q=isProperindo?'':(params.get('q')||'').trim();
  let sort=params.get('sort')||'newest';
  search.value=q;
  sortSel.value=['newest','oldest','az','za'].includes(sort)?sort:'newest';

  const isMobileShowcase=(p)=>{const c=(p.category||'').toLowerCase();const tg=(p.tags||[]).join(' ').toLowerCase();return p.slug==='smartbalita-app'||c.includes('mobile')||tg.includes('react native')||tg.includes('expo');};
  function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;')}

  function filtered(){
    let list=projects.filter(p=>{
      const catOk=active==='all'?true:active==='featured'?p.featured:Array.isArray(p.categories)&&p.categories.includes(active);
      if(!catOk) return false;
      if(!q) return true;
      const hay=[p.title,p.category,p.role,p.summary,p.domain,(p.tags||[]).join(' '),p.status].join(' ').toLowerCase();
      return q.toLowerCase().split(/\s+/).every(tok=>hay.includes(tok));
    });
    if(sortSel.value==='newest') list.sort((a,b)=>(b.sortKey||0)-(a.sortKey||0));
    else if(sortSel.value==='oldest') list.sort((a,b)=>(a.sortKey||0)-(b.sortKey||0));
    else if(sortSel.value==='az') list.sort((a,b)=>a.title.localeCompare(b.title));
    else if(sortSel.value==='za') list.sort((a,b)=>b.title.localeCompare(a.title));
    return list;
  }

  function card(p){
    const mobile=isMobileShowcase(p);
    const img=p.coverImage?`<img src="${p.coverImage}" alt="${esc(p.title)}" class="${mobile?'project-image project-image-mobile':'project-image'}">`:`<div class="project-image project-image-placeholder"><span>${esc(p.coverLabel||p.title)}</span></div>`;
    const pills=[p.period,p.role,p.status,`${p.repoVisibility} Repo`].filter(Boolean).map(v=>`<span class="project-meta-pill">${esc(v)}</span>`).join('');
    const detail=`<a href="porto-show.html?project=${p.slug}" class="project-link project-link-show">Show</a>`;
    const primary=p.liveUrl?`<a href="${p.liveUrl}" target="_blank" rel="noopener noreferrer" class="project-link project-link-primary">Live Site</a>`:p.repoUrl?`<a href="${p.repoUrl}" target="_blank" rel="noopener noreferrer" class="project-link project-link-primary">GitHub</a>`:`<span class="project-link project-link-disabled">Private Repo</span>`;
    const secondary=p.liveUrl&&p.repoUrl?`<a href="${p.repoUrl}" target="_blank" rel="noopener noreferrer" class="project-link project-link-secondary">GitHub</a>`:'';
    return `<article class="project-card project-card-catalog${mobile?' is-mobile-showcase':''}"><div class="project-image-container ${mobile?'is-mobile-container':''}">${img}<div class="project-overlay"></div><span class="project-status-badge">${esc(p.status)}</span></div><div class="project-content"><p class="project-kicker">${esc(p.category)}</p><h3 class="project-title font-montserrat">${esc(p.title)}</h3><p class="project-roleline">${esc(p.role)}</p><div class="project-meta">${pills}</div><p class="project-description">${esc(p.summary)}</p><div class="project-tags">${(p.tags||[]).map(t=>`<span class="project-tag">${esc(t)}</span>`).join('')}</div><div class="project-links">${detail}${primary}${secondary}</div></div></article>`;
  }

  function syncUrl(){
    const sp=new URLSearchParams();
    if(active!=='all') sp.set('filter',active);
    if(q) sp.set('q',q);
    if(sortSel.value!=='newest') sp.set('sort',sortSel.value);
    const qs=sp.toString();
    history.replaceState(null,'',qs?`?${qs}`:'');
  }

  function renderBar(){
    bar.innerHTML=filters.map((f, idx)=>{ const btn=`<button class="project-filter-btn${f.id===active?' active':''}" data-filter="${f.id}" type="button">${f.label}</button>`; const div= idx===1 ? `<span class="filter-divider" aria-hidden="true"></span>` : ``; return btn+div; }).join('');
  }

  function renderGrid(){
    const list=filtered();
    if(list.length===0){
      grid.innerHTML=`<div class="portfolio-empty"><strong>No projects found</strong><p style="margin:.5rem 0 0;">Try another keyword or category. <button onclick="document.getElementById('portfolio-search').value='';document.getElementById('portfolio-search').dispatchEvent(new Event('input'))" style="color:var(--primary);background:none;border:none;cursor:pointer;font-weight:700;">Clear search</button></p></div>`;
    } else {
      grid.innerHTML=list.map(card).join('');
    }
    count.textContent=list.length+' project'+(list.length!==1?'s':'')+' • '+projects.length+' total';
    syncUrl();
  }


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

  bar.addEventListener('click',e=>{
    const b=e.target.closest('[data-filter]');
    if(!b) return;
    active=b.getAttribute('data-filter');
    renderBar(); renderGrid();
  });
  search.addEventListener('input',e=>{
    q=e.target.value.trim();
    renderGrid();
  });
  sortSel.addEventListener('change',renderGrid);
  clearBtn&&clearBtn.addEventListener('click',()=>{
    active='all';q='';search.value='';sortSel.value='newest';renderBar();renderGrid();
  });

  renderBar(); renderGrid();

  // shopee mobile: tap card to go to detail (since links hidden)
  document.addEventListener('click', (e)=>{
    if(window.innerWidth>767) return;
    const card=e.target.closest('.project-card');
    if(!card) return;
    if(e.target.closest('a, button')) return;
    const slug = card.querySelector('[href*="porto-show.html?project="]')?.getAttribute('href')?.match(/project=([^&]+)/)?.[1];
    if(slug) location.href=`porto-show.html?project=${slug}`;
  });
});

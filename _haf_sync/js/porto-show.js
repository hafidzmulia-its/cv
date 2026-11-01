document.addEventListener('DOMContentLoaded', function () {
    const root = document.getElementById('project-detail-root');
    const projects = Array.isArray(window.portfolioProjects) ? window.portfolioProjects : [];
    const params = new URLSearchParams(window.location.search);
    const slug = params.get('project');
    const project = projects.find((item) => item.slug === slug);

    if (!root) return;

    if (!project) {
        root.innerHTML = `
            <div class="container detail-shell">
                <div class="detail-card detail-empty" style="text-align:center;padding:3rem;">
                    <h1 class="font-montserrat">Project not found</h1>
                    <p class="detail-summary" style="margin:1rem auto;">The requested portfolio entry is missing or the URL slug is invalid.</p>
                    <a href="portfolio.html" class="detail-action detail-action-primary">Browse portfolio</a>
                </div>
            </div>
        `;
        return;
    }

    const domain = project.domain || project.category;
    const overview = Array.isArray(project.overview) && project.overview.length > 0 ? project.overview : [project.summary];
    const highlights = Array.isArray(project.highlights) && project.highlights.length > 0 ? project.highlights : [`Delivered as a ${project.status.toLowerCase()} project.`, `Stack: ${(project.tags||[]).slice(0,4).join(', ')}`];
    const stack = project.stack && Object.keys(project.stack).length ? project.stack : {'Primary Stack':(project.tags||[]).join(', ')};

    document.title = `${project.title} — Hafidz Mulia`;

    const screenshots = Array.isArray(project.screenshots) && project.screenshots.length ? project.screenshots : [
        {title:`${project.title} — Overview`, description:`Add a main interface capture for ${project.title} later.`},
        {title:`${project.title} — Workflow`, description:'Add internal workflow screenshot.'},
        {title:`${project.title} — Detail`, description:'Add supporting screen.'}
    ];

    const hasLive = !!project.liveUrl;
    const hasRepo = !!project.repoUrl;

    root.innerHTML = `
        <div class="container detail-shell-v2">
            <div class="detail-hero-v2">
                <p class="detail-eyebrow-v2">${esc(project.category)}</p>
                <h1 class="detail-title-v2 font-montserrat">${esc(project.title)}</h1>
                <p class="detail-summary-v2">${esc(project.summary)}</p>
                <div class="detail-pills-v2">
                    <span class="detail-pill-v2"><span class="dot"></span>${esc(project.period)}</span>
                    <span class="detail-pill-v2">${esc(project.role)}</span>
                    <span class="detail-pill-v2 tone">${esc(domain)}</span>
                    <span class="detail-pill-v2 ${project.status==='Live'?'live':''}">${esc(project.status)}</span>
                </div>
                <div class="detail-actions-v2">
                    <a href="portfolio.html" class="btn-v2 btn-ghost-v2">&larr; Back to portfolio</a>
                    ${hasLive ? `<a href="${project.liveUrl}" target="_blank" rel="noopener noreferrer" class="btn-v2 btn-primary-v2">Open live site &nearr;</a>` : ''}
                    ${hasRepo ? `<a href="${project.repoUrl}" target="_blank" rel="noopener noreferrer" class="btn-v2 btn-secondary-v2">View repository</a>` : `<span class="btn-v2 btn-disabled-v2">${esc(project.repoVisibility)} repo</span>`}
                </div>
            </div>

            <div class="detail-layout-v2">
                <div class="detail-main-v2">
                    <section class="card-v2 card-gallery-v2">
                        <div class="card-v2-head">
                            <span class="kicker">Visual walkthrough</span>
                            <h2 class="font-montserrat">Screens and product surfaces</h2>
                            <p class="muted">${screenshots.length} screens • images scale to their own ratio</p>
                        </div>
                        <div class="gallery-v2">
                            <div class="gallery-stage-v2">
                                <div class="gallery-track-v2">
                                    ${screenshots.map(s=> s.image ? `<div class="gallery-slide-v2"><img class="gallery-img-v2" src="${s.image}" alt="${esc(s.title)}" loading="lazy"><div class="gallery-caption-v2"><strong>${esc(s.title)}</strong><span>${esc(s.description)}</span></div></div>` : `<div class="gallery-slide-v2"><div class="gallery-placeholder-v2"><strong>${esc(s.title)}</strong><p>${esc(s.description)}</p><em>Put files in <code>img/${esc(project.mediaFolder||project.slug)}/1-${screenshots.length}.png</code></em></div></div>`).join('')}
                                </div>
                                <button class="gallery-nav-v2 prev" type="button" data-g-prev aria-label="Previous">&larr;</button>
                                <button class="gallery-nav-v2 next" type="button" data-g-next aria-label="Next">&rarr;</button>
                            </div>
                            <div class="gallery-bar-v2">
                                <span class="gallery-count-v2" data-g-count>1 / ${screenshots.length}</span>
                                <div class="gallery-dots-v2">
                                    ${screenshots.map((_,i)=>`<button class="g-dot ${i===0?'on':''}" data-g-dot="${i}" aria-label="Go to ${i+1}"></button>`).join('')}
                                </div>
                                <span class="gallery-hint-v2" data-g-title>${esc(screenshots[0].title)}</span>
                            </div>
                        </div>
                    </section>

                    <section class="card-v2">
                        <div class="card-v2-head">
                            <span class="kicker">Narrative</span>
                            <h2 class="font-montserrat">Project overview</h2>
                        </div>
                        <div class="prose-v2">
                            ${overview.map(p=>`<p>${esc(p)}</p>`).join('')}
                        </div>
                    </section>

                    <section class="card-v2">
                        <div class="card-v2-head">
                            <span class="kicker">Delivery notes</span>
                            <h2 class="font-montserrat">What stands out</h2>
                            <p class="muted">${highlights.length} focus points</p>
                        </div>
                        <ol class="highlights-v2">
                            ${highlights.map((h,i)=>`<li><span class="num">${String(i+1).padStart(2,'0')}</span><span>${esc(h)}</span></li>`).join('')}
                        </ol>
                    </section>
                </div>

                <aside class="detail-side-v2">
                    <section class="card-v2">
                        <div class="card-v2-head">
                            <span class="kicker">Essentials</span>
                            <h2 class="font-montserrat">Metadata</h2>
                        </div>
                        <dl class="meta-v2">
                            <div><dt>Role</dt><dd>${esc(project.role)}</dd></div>
                            <div><dt>Period</dt><dd>${esc(project.period)}</dd></div>
                            <div><dt>Domain</dt><dd>${esc(domain)}</dd></div>
                            <div><dt>Repository</dt><dd>${hasRepo?'<a href="'+project.repoUrl+'" target="_blank" rel="noopener">'+esc(project.repoVisibility)+'</a>':esc(project.repoVisibility)}</dd></div>
                            <div><dt>Live access</dt><dd>${hasLive?'<a href="'+project.liveUrl+'" target="_blank" rel="noopener">'+esc(project.liveUrl.replace(/^https?:\/\//,''))+'</a>':'Private / unpublished'}</dd></div>
                        </dl>
                    </section>

                    <section class="card-v2">
                        <div class="card-v2-head">
                            <span class="kicker">Build system</span>
                            <h2 class="font-montserrat">Tech stack</h2>
                        </div>
                        <dl class="meta-v2">
                            ${Object.entries(stack).map(([k,v])=>`<div><dt>${esc(k)}</dt><dd>${esc(v)}</dd></div>`).join('')}
                        </dl>
                        <div class="tags-v2" style="margin-top:1rem;">${(project.tags||[]).map(t=>`<span class="tag-v2">${esc(t)}</span>`).join('')}</div>
                    </section>

                    <section class="card-v2 card-cta-v2">
                        <h3 class="font-montserrat" style="font-size:1rem;">Need the full catalog?</h3>
                        <p class="muted" style="font-size:.9rem;margin:.4rem 0 1rem;">Browse all projects with search and filters.</p>
                        <a href="portfolio.html" class="btn-v2 btn-primary-v2" style="width:100%;justify-content:center;">Open portfolio</a>
                    </section>
                </aside>
            </div>
        </div>
    `;

    initGallery(root);
});

function initGallery(root){
    const track=root.querySelector('.gallery-track-v2');
    const dots=[...root.querySelectorAll('[data-g-dot]')];
    const prev=root.querySelector('[data-g-prev]');
    const next=root.querySelector('[data-g-next]');
    const count=root.querySelector('[data-g-count]');
    const titleEl=root.querySelector('[data-g-title]');
    if(!track||!dots.length) return;
    let idx=0;
    const slides=[...root.querySelectorAll('.gallery-slide-v2')];
    const titles=slides.map(s=> s.querySelector('strong')?.textContent || '');
    function go(i){
        idx=(i+dots.length)%dots.length;
        track.style.transform=`translateX(-${idx*100}%)`;
        dots.forEach((d,j)=>d.classList.toggle('on',j===idx));
        if(count) count.textContent=`${idx+1} / ${dots.length}`;
        if(titleEl) titleEl.textContent=titles[idx]||'';
    }
    prev?.addEventListener('click',()=>go(idx-1));
    next?.addEventListener('click',()=>go(idx+1));
    dots.forEach((d,i)=>d.addEventListener('click',()=>go(i)));
    let sx=0;
    track.addEventListener('touchstart',e=>sx=e.touches[0].clientX,{passive:true});
    track.addEventListener('touchend',e=>{
        const dx=e.changedTouches[0].clientX - sx;
        if(Math.abs(dx)>40) go(idx + (dx<0?1:-1));
    });
}

function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;')}

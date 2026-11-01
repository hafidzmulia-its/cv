const siteHeaderHTML = `
<nav class="nav-fixed transition-smooth bg-background/95 backdrop-blur-md shadow-md">
  <div class="container">
    <div class="nav-container">
      <button class="nav-brand font-montserrat" onclick="window.location.href='index.html#home'">haf<span class="text-gradient">.</span></button>
      <div class="nav-menu" id="site-nav-menu">
        <a class="nav-link" href="index.html#about" data-nav="about">About</a>
        <a class="nav-link" href="index.html#experience" data-nav="experience">Experience</a>
        <a class="nav-link" href="portfolio.html" data-nav="portfolio">Portfolio</a>
        <a class="nav-link" href="index.html#contact" data-nav="contact">Contact</a>
      </div>
      <button class="mobile-menu-btn" id="site-mobile-btn" aria-label="menu" aria-expanded="false">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"></line><line x1="4" x2="20" y1="6" y2="6"></line><line x1="4" x2="20" y1="18" y2="18"></line></svg>
      </button>
    </div>
  </div>
</nav>`;

const siteFooterHTML = `
<footer class="gradient-primary">
  <div class="container">
    <div class="footer-content">
      <div class="footer-info">
        <h3 class="footer-title font-montserrat">Hafidz Mulia</h3>
        <p class="footer-subtitle">Software Developer | Empathetic Problem Solver</p>
        <p style="margin:.4rem 0 0;font-size:.9rem;opacity:.9;"><a href="mailto:hafidzmuliia@gmail.com" style="color:#fff;text-decoration:underline;">hafidzmuliia@gmail.com</a></p>
      </div>
      <div class="footer-social">
        <a href="https://github.com/hafidzmulia-its" target="_blank" rel="noopener noreferrer" aria-label="GitHub">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"></path><path d="M9 18c-4.51 2-5-2-7-2"></path></svg>
        </a>
        <a href="https://www.linkedin.com/in/hafidz-mulia/" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect width="4" height="12" x="2" y="9"></rect><circle cx="4" cy="4" r="2"></circle></svg>
        </a>
        <a href="https://www.instagram.com/haf.mul/" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"></line></svg>
        </a>
        <a href="mailto:hafidzmuliia@gmail.com" aria-label="Email">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path></svg>
        </a>
      </div>
    </div>
    <div class="footer-bottom">
      <p class="footer-copyright">Serving people through software, systems thinking, and practical teaching.<br>&copy; 2026 Hafidz Mulia. All rights reserved.</p>
      
    </div>
  </div>
</footer>`;

(function(){
  function inject(){
    const h = document.getElementById('site-header');
    const f = document.getElementById('site-footer');
    if(h && !h.innerHTML.trim()) h.innerHTML = siteHeaderHTML;
    else if(h && h.innerHTML.trim() && !h.querySelector('#site-nav-menu')) h.innerHTML = siteHeaderHTML;
    if(f && !f.innerHTML.trim()) f.innerHTML = siteFooterHTML;
    else if(f && f.innerHTML.trim() && !f.querySelector('.footer-content')) f.innerHTML = siteFooterHTML;
    const path = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
    const isPortfolio = path === 'portfolio.html' || path.includes('portfolio');
    const isDetail = path === 'porto-show.html';
    document.querySelectorAll('#site-nav-menu .nav-link').forEach(a=>{
      const href = (a.getAttribute('href')||'').toLowerCase();
      if((isPortfolio || isDetail) && href.includes('portfolio.html')) a.classList.add('active');
      if((isPortfolio || isDetail) && href.includes('portfolio.html')){ a.style.color='var(--primary)'; a.style.background='rgba(124,58,237,.08)'; }
    });
    // hamburger helpers (also used by inline fallback)
    window.hafToggleMenu = function(){
      const m=document.getElementById('site-nav-menu'), b=document.getElementById('site-mobile-btn');
      if(!m||!b) return;
      const open=m.classList.toggle('nav-menu-open');
      b.classList.toggle('active', open);
      b.setAttribute('aria-expanded', open?'true':'false');
      document.body.style.overflow=open?'hidden':'';
      if(open){ m.style.display='flex'; m.style.visibility='visible'; m.style.opacity='1'; m.style.transform='translateY(0)'; }
      else { m.style.display=''; m.style.visibility=''; m.style.opacity=''; m.style.transform=''; }
    };
    window.hafCloseMenu = function(){
      const m=document.getElementById('site-nav-menu'), b=document.getElementById('site-mobile-btn');
      if(!m||!b) return;
      m.classList.remove('nav-menu-open'); b.classList.remove('active'); b.setAttribute('aria-expanded','false'); document.body.style.overflow=''; m.style.display=''; m.style.visibility=''; m.style.opacity=''; m.style.transform='';
    };
  }
  // immediate inject if placeholder already in DOM (script at bottom), plus DOMContentLoaded fallback
  inject();
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', inject);
  else setTimeout(inject, 0);
  // global delegation for hamburger (works even if header injected late, no double-toggle)
  document.addEventListener('click', (e)=>{
    const b=e.target.closest('#site-mobile-btn');
    if(b){
      e.preventDefault(); e.stopPropagation();
      const m=document.getElementById('site-nav-menu');
      const isOpen=m&&m.classList.contains('nav-menu-open');
      if(isOpen) window.hafCloseMenu(); else window.hafToggleMenu();
      return;
    }
    const m=document.getElementById('site-nav-menu');
    if(m && m.classList.contains('nav-menu-open')){
      const btn=document.getElementById('site-mobile-btn');
      if(m.contains(e.target) || (btn && btn.contains(e.target))) return;
      window.hafCloseMenu();
    }
  });
  document.addEventListener('keydown', (e)=>{ if(e.key==='Escape') window.hafCloseMenu(); });
  window.addEventListener('resize', ()=>{ if(window.innerWidth>=768) window.hafCloseMenu(); });
  document.addEventListener('click', (e)=>{
    const a=e.target.closest('#site-nav-menu .nav-link');
    if(a) window.hafCloseMenu();
  });
})();

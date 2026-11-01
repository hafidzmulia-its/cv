import pathlib

# Patch script.js
p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/js/script.js')
t = p.read_text(encoding='utf-8')
old = """    const createProjectCard = (project) => {
        const imageMarkup = project.coverImage
            ? `<img src="${project.coverImage}" alt="${escapeProjectText(project.title)}" class="project-image">`
            : `<div class="project-image project-image-placeholder"><span>${escapeProjectText(project.coverLabel || project.title)}</span></div>`;"""
new = """    const isMobileShowcase = (project) => {
            const cat = (project.category||'').toLowerCase();
            const tags = (project.tags||[]).join(' ').toLowerCase();
            return project.slug==='smartbalita-app' || cat.includes('mobile') || tags.includes('react native') || tags.includes('expo');
        };
    const createProjectCard = (project) => {
        const mobile = isMobileShowcase(project);
        const imageMarkup = project.coverImage
            ? `<img src="${project.coverImage}" alt="${escapeProjectText(project.title)}" class="${mobile?'project-image project-image-mobile':'project-image'}">`
            : `<div class="project-image project-image-placeholder"><span>${escapeProjectText(project.coverLabel || project.title)}</span></div>`;"""
t = t.replace(old, new)
t = t.replace('<article class="project-card project-card-catalog">', '<article class="project-card project-card-catalog${mobile?\' is-mobile-showcase\':\'\'}">')
# Actually need to inject mobile variable inside template: the return uses mobile, so move isMobile inside createProjectCard already, but article needs mobile too
# The previous replace for article uses mobile var but mobile is inside function, so okay
t = t.replace('return `\n            <article class="project-card project-card-catalog">', 'return `\n            <article class="project-card project-card-catalog${mobile?\' is-mobile-showcase\':\'\'}">')
p.write_text(t, encoding='utf-8')
print('patched script.js')

# Patch portfolio.js
pp = pathlib.Path(r'D:/Downloads/cv/_haf_sync/js/portfolio.js')
tt = pp.read_text(encoding='utf-8')
# add helper
tt = tt.replace(
    "  function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/\"/g,'&quot;').replace(/'/g,'&#39;')}",
    "  const isMobileShowcase=(p)=>{const c=(p.category||'').toLowerCase();const tg=(p.tags||[]).join(' ').toLowerCase();return p.slug==='smartbalita-app'||c.includes('mobile')||tg.includes('react native')||tg.includes('expo');};\n  function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/\"/g,'&quot;').replace(/'/g,'&#39;')}"
)
tt = tt.replace(
    "  function card(p){\n    const img=p.coverImage?`<img src=\"${p.coverImage}\" alt=\"${esc(p.title)}\" class=\"project-image\">`:`<div class=\"project-image project-image-placeholder\"><span>${esc(p.coverLabel||p.title)}</span></div>`;",
    "  function card(p){\n    const mobile=isMobileShowcase(p);\n    const img=p.coverImage?`<img src=\"${p.coverImage}\" alt=\"${esc(p.title)}\" class=\"${mobile?'project-image project-image-mobile':'project-image'}\">`:`<div class=\"project-image project-image-placeholder\"><span>${esc(p.coverLabel||p.title)}</span></div>`;"
)
tt = tt.replace(
    'return `<article class="project-card project-card-catalog"><div class="project-image-container">${img}',
    'return `<article class="project-card project-card-catalog${mobile?\' is-mobile-showcase\':\'\'}"><div class="project-image-container ${mobile?\'is-mobile-container\':\'\'}">${img}'
)
pp.write_text(tt, encoding='utf-8')
print('patched portfolio.js')

# Patch css
cssp = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
css = cssp.read_text(encoding='utf-8')
extra = """
/* mobile showcase: height follows image, white pillarbox */
.is-mobile-showcase .project-image-container.is-mobile-container,
.is-mobile-showcase .project-image-container{background:#fff;display:flex;align-items:center;justify-content:center;aspect-ratio:auto !important;}
.is-mobile-showcase .project-image-mobile{width:100%;height:auto !important;object-fit:contain !important;aspect-ratio:auto !important;display:block;max-height:none;}
.project-image-mobile{background:#fff}
"""
if 'is-mobile-showcase' not in css:
    cssp.write_text(css + extra, encoding='utf-8')
    print('patched css')
else:
    print('css already')

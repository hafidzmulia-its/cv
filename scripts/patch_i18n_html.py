import pathlib

# Add lang switch css and i18n script plus data-i18n attributes
css_p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
css = css_p.read_text(encoding='utf-8')
if '.lang-switch' not in css:
    css += """
.lang-switch button.active{background:var(--primary) !important;color:#fff !important;border-color:var(--primary) !important}
.lang-switch{display:flex;gap:.3rem}
@media(max-width:767px){.lang-switch{margin-left:auto}}
"""
    css_p.write_text(css, encoding='utf-8')
    print('added lang css')

# Add i18n script to html files
for name in ['index.html','portfolio.html','porto-show.html']:
    p = pathlib.Path(f'D:/Downloads/cv/_haf_sync/{name}')
    html = p.read_text(encoding='utf-8')
    if 'js/i18n.js' not in html:
        html = html.replace('<script src="js/layout.js"></script>', '<script src="js/layout.js"></script>\n    <script src="js/i18n.js"></script>')
        # fallback if layout.js not found (porto-show originally had layout.js now)
        if 'js/i18n.js' not in html:
            html = html.replace('<script src="js/project-data.js">', '<script src="js/i18n.js"></script>\n    <script src="js/project-data.js">')
        p.write_text(html, encoding='utf-8')
        print(f'added i18n script to {name}')
    else:
        print(f'{name} already has i18n')

# Add data-i18n to index.html key sections
idx = pathlib.Path(r'D:/Downloads/cv/_haf_sync/index.html')
html = idx.read_text(encoding='utf-8')
replacements = [
    ('<h1 class="hero-title font-montserrat">Hafidz Mulia</h1>', '<h1 class="hero-title font-montserrat" data-i18n="hero.title">Hafidz Mulia</h1>'),
    ('<p class="hero-subtitle">Product Builder | Technical Problem Solver | Student Leader</p>', '<p class="hero-subtitle" data-i18n="hero.subtitle">Product Builder | Technical Problem Solver | Student Leader</p>'),
    ('<p class="hero-description">', '<p class="hero-description" data-i18n="hero.description">'),
    ('>Get in Touch</button>', ' data-i18n="hero.btn_contact">Get in Touch</button>'),
    ('>Download CV</a>', ' data-i18n="hero.btn_cv">Download CV</a>'),
    # About
    ('Professional <span class="text-gradient">Summary</span>', '<span data-i18n="about.title">Professional Summary</span>'),
    # Projects
    ('Project <span class="text-gradient">Catalog</span>', '<span data-i18n="projects.title">Project Catalog</span>'),
    ('The front view shows my latest featured work. Switch categories to browse the wider repo-backed project catalog.', '<span data-i18n="projects.intro">The front view shows my latest featured work. Switch categories to browse the wider repo-backed project catalog.</span>'),
    # Skills
    ('Skills & <span class="text-gradient">Technologies</span>', '<span data-i18n="skills.title">Skills & Technologies</span>'),
    # Contact
    ("Let&apos;s <span class=\"text-gradient\">Connect</span>", '<span data-i18n="contact.title">Let\'s Connect</span>'),
]
for old, new in replacements:
    if old in html:
        html = html.replace(old, new)
        print(f'replaced {old[:30]}')
idx.write_text(html, encoding='utf-8')
print('patched index data-i18n')

# Patch portfolio.html
port = pathlib.Path(r'D:/Downloads/cv/_haf_sync/portfolio.html')
html = port.read_text(encoding='utf-8')
# add data-i18n to portfolio hero title and intro and search placeholder and sort
html = html.replace('Complete <span class="text-gradient">Portfolio</span>', '<span data-i18n="portfolio.title">Complete Portfolio</span>')
html = html.replace('Searchable catalog of all shipped projects — education, GIS, health-tech, internal systems. Filter by stack or search by keyword.', '<span data-i18n="portfolio.intro">Searchable catalog of all shipped projects — education, GIS, health-tech, internal systems. Filter by stack or search by keyword.</span>')
if 'data-i18n-placeholder' not in html:
    html = html.replace('placeholder="Search by title', 'data-i18n-placeholder="portfolio.search_placeholder" placeholder="Search by title')
# sort options
html = html.replace('<option value="newest">Newest first</option>', '<option value="newest" data-i18n="portfolio.sort_newest">Newest first</option>')
html = html.replace('<option value="oldest">Oldest first</option>', '<option value="oldest" data-i18n="portfolio.sort_oldest">Oldest first</option>')
html = html.replace('<option value="az">A → Z</option>', '<option value="az">A → Z</option>')
html = html.replace('<option value="za">Z → A</option>', '<option value="za">Z → A</option>')
port.write_text(html, encoding='utf-8')
print('patched portfolio')

# Patch porto-show detail strings via i18n? The detail is dynamic JS, but we can add data-i18n for static back link? It's generated via JS, handled via i18n.js t() later if we update porto-show.js. For now leave.

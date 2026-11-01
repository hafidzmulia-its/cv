import pathlib, re

# 1. Fix sidedikk data
p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/js/project-data.js')
t = p.read_text(encoding='utf-8')

# Replace sidedikk project entry
old_proj = """    {
        slug: 'sidedikk',
        title: 'Sidedikk',
        period: '2026',
        sortKey: 20260821,
        category: 'Education / School System',
        categories: ['laravel', 'education', 'systems'],
        featured: true,
        role: 'Fullstack Developer',
        status: 'Live',
        repoVisibility: 'Public',
        liveUrl: 'https://sidedikk.my.id',
        repoUrl: 'https://github.com/hafidzmulia-its/sidedikk',
        coverImage: '',
        coverLabel: 'Sidedikk',
        tags: ['Laravel', 'PHP', 'MySQL', 'Tailwind CSS'],
        summary: 'School information system with admin workflows, data management, and operational dashboards.'
    },"""
new_proj = """    {
        slug: 'sidedikk',
        title: 'Sidedikk',
        period: '2026',
        sortKey: 20260821,
        category: 'Health-Tech / PWA Screening',
        categories: ['laravel', 'health', 'systems'],
        featured: true,
        role: 'Fullstack Developer',
        status: 'Live',
        repoVisibility: 'Public',
        liveUrl: 'https://sidedikk.my.id',
        repoUrl: 'https://github.com/hafidzmulia-its/sidedikk-pwa',
        coverImage: '',
        coverLabel: 'Sidedikk',
        tags: ['Laravel 13', 'PHP 8.3', 'MySQL', 'Tailwind CSS 4', 'Alpine.js', 'PWA', 'Chart.js'],
        summary: 'Progressive Web App for early pregnancy-complication screening — HPHT registration, 20 Yes/No questions, 4-level risk classification (KRR/KRS/KRT/KRST) with ANC/delivery/attendant advice, immutable versioned snapshots, and production-hardened PWA on shared hosting.'
    },"""
if old_proj in t:
    t = t.replace(old_proj, new_proj)
    print('replaced sidedikk project')
else:
    print('sidedikk project not found exact, trying regex')
    t = re.sub(r"\{\s+slug:\s*'sidedikk'.*?\},", new_proj, t, flags=re.S)

# Replace sidedikk detail map
old_detail = """    sidedikk: {
        categories: ['featured', 'laravel', 'education', 'systems'],
        domain: 'Education / School Information System',
        mediaFolder: 'sidedikk',
        overview: [
            'Sidedikk is a school information system built for day-to-day administrative operations.',
            'The platform focuses on structured data workflows and dashboard visibility for internal users.'
        ],
        highlights: [
            'Built admin workflows for school operational data.',
            'Implemented Laravel-based CRUD and role-aware dashboards.',
            'Latest portfolio update as of August 2026.'
        ],
        stack: {
            Frontend: 'Blade, Tailwind CSS',
            Backend: 'Laravel 12, PHP 8.2',
            Data: 'MySQL',
            Auth: 'Laravel Breeze / session',
            Extras: 'Admin workflows, operational dashboards'
        },
        scenes: [
            { title: 'Dashboard', description: 'Main school dashboard and operational overview.' },
            { title: 'Data Workflow', description: 'Core admin or data-management interface inside the system.' },
            { title: 'Detail View', description: 'Supporting screen showing detailed records or management flow.' }
        ]
    },"""
new_detail = """    sidedikk: {
        categories: ['featured', 'laravel', 'health', 'systems'],
        domain: 'Health-Tech / PWA Screening Platform',
        mediaFolder: 'sidedikk',
        liveUrl: 'https://sidedikk.my.id',
        overview: [
            'SIDEDIKK is a mobile-first Laravel 13 PWA for early pregnancy-complication screening, built to run on low-resource shared hosting (1.5 vCPU / 2GB) while handling sensitive health data.',
            'The screening engine is versioned and snapshot-based: every completed screening locks questionnaire + risk-rule versions and stores score, risk label, recommendation, ANC/delivery/attendant as immutable data — new publications never rewrite history.'
        ],
        highlights: [
            'Implemented HPHT registration (15–60y) → gestational age derived server-side and 20-question Yes/No flow with progress, review, and idempotent transactional submit.',
            'Built 4-level risk classification (KRR 0–4, KRS 5–8, KRT 9–14, KRST ≥15) with color/icon, plus ANC place, delivery place, and birth attendant advice snapshotted per screening.',
            'Delivered custom admin panel (no Filament) with Chart.js risk distribution & 14-day trend, versioned questionnaire/risk-rule draft/publish, education CRUD, streamed CSV export, and audit log — 58 PHPUnit tests, PWA installable with offline support.'
        ],
        stack: {
            Frontend: 'Blade, Tailwind CSS 4.3, Alpine.js 3.15, Vite 8, Chart.js 4.5',
            Backend: 'Laravel 13.8, PHP 8.3, Laravel Breeze 2.4',
            Data: 'MySQL 8 / MariaDB, Eloquent, database cache/session/queue (no Redis)',
            Auth: 'Role middleware (user/admin), Policies + scoped queries, rate limiting, security headers',
            Extras: 'PWA (manifest + sw.js + offline.html), cPanel split-domain deploy (sidedikk.my.id + app.sidedikk.my.id), Laravel Pint, PHPUnit 12'
        },
        scenes: [
            { title: 'Landing & PWA Install', description: 'Public landing at sidedikk.my.id and installable app at app.sidedikk.my.id with brand icons.' },
            { title: 'HPHT Registration & Dashboard', description: 'Register with HPHT → gestational age card and screening entry point.' },
            { title: '20-Question Screening Flow', description: 'Progress 3/20, Yes/No, back/forward, review, and idempotent submit with server-side scoring.' },
            { title: 'Result with 4 Advice Cards', description: 'Score 8/20 + risk badge (KRR/KRS/KRT/KRST) and cards for ANC place, delivery place, birth attendant.' },
            { title: 'Admin Dashboard & Charts', description: 'Admin cards + Chart.js risk distribution & trend, plus versioned questionnaire and education management.' }
        ]
    },"""
if old_detail in t:
    t = t.replace(old_detail, new_detail)
    print('replaced sidedikk detail')
else:
    print('detail not found')

# Also improve resource description for other projects? Keep but enhance summaries slightly? For now just sidedikk
p.write_text(t, encoding='utf-8')

# 2. Add arrows to filter bar - patch CSS
css_p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
css = css_p.read_text(encoding='utf-8')
arrow_css = """
/* filter arrows left/right */
.filter-wrap{position:relative;display:flex;align-items:center;gap:.5rem}
.filter-arrow{flex:0 0 2.2rem;width:2.2rem;height:2.2rem;border-radius:999px;border:1px solid var(--border);background:#fff;display:grid;place-items:center;cursor:pointer;box-shadow:0 4px 12px rgba(15,23,42,.08);font-weight:700}
.filter-arrow:hover{border-color:rgba(124,58,237,.3);color:var(--primary)}
.filter-arrow:disabled{opacity:.35;cursor:default}
.project-filter-bar{scroll-behavior:smooth}
@media(min-width:768px){.filter-arrow{display:none}}
"""
if 'filter-arrow' not in css:
    css_p.write_text(css + arrow_css, encoding='utf-8')
    print('added arrow css')
else:
    print('arrow css exists')


import pathlib, re
p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/js/project-data.js')
t = p.read_text(encoding='utf-8')
# Find sidedikk detail block via regex and replace whole block
pattern = r"sidedikk:\s*\{.*?scenes:\s*\[.*?\]\s*\},"
# new detail with better resource description
new = """    sidedikk: {
        categories: ['featured', 'laravel', 'health', 'systems'],
        domain: 'Health-Tech / PWA Screening Platform',
        mediaFolder: 'sidedikk',
        liveUrl: 'https://sidedikk.my.id',
        overview: [
            'SIDEDIKK is a mobile-first Laravel 13 PWA for early pregnancy-complication screening, optimized for low-resource shared hosting (1.5 vCPU / 2GB) while remaining production-hardened for sensitive health data.',
            'The core engine is versioned and snapshot-based: every completed screening locks the questionnaire and risk-rule versions and stores score, risk label, recommendation, ANC place, delivery place, and birth attendant as immutable snapshots — new publications never rewrite history.'
        ],
        highlights: [
            'Built HPHT registration (age 15–60, privacy & medical disclaimer) → gestational age derived server-side and 20-question Yes/No screening with progress 3/20, back/forward, review, and idempotent transactional submit.',
            'Implemented 4-level risk classification (KRR 0–4, KRS 5–8, KRT 9–14, KRST ≥15) with color/icon, plus per-level advice for ANC place, delivery place, and birth attendant, snapshotted per screening.',
            'Shipped custom admin panel (no Filament) with Chart.js risk distribution & 14-day trend, users/screenings (scoped, paginated, read-only completed), questionnaire & risk-rule draft/publish versioning, education CRUD with cover images, streamed CSV export, audit log, and 58 PHPUnit tests — PWA installable via manifest + sw.js (cache-first for hashed assets, network-only for auth) and split-domain cPanel deploy.'
        ],
        stack: {
            Frontend: 'Blade, Tailwind CSS 4.3, Alpine.js 3.15, Vite 8, Chart.js 4.5',
            Backend: 'Laravel 13.8, PHP 8.3, Laravel Breeze 2.4',
            Data: 'MySQL 8 / MariaDB, Eloquent, database cache/session/queue (no Redis)',
            Auth: 'Role middleware (user/admin), Policies + scoped queries, rate limiting, CSRF, security headers, SESSION_ENCRYPT',
            Extras: 'PWA (manifest.webmanifest + sw.js + offline.html + brand icons), deployment/scripts/deploy-cpanel.sh (public/build committed for cPanel), Laravel Pint, PHPUnit 12'
        },
        scenes: [
            { title: 'Landing & PWA Install', description: 'Public landing at sidedikk.my.id and installable app at app.sidedikk.my.id with brand icons and offline.html.' },
            { title: 'HPHT Registration & Dashboard', description: 'Register with HPHT date, privacy & medical disclaimer → dashboard shows gestational age and screening CTA.' },
            { title: '20-Question Screening Flow', description: 'Progress 3/20, Ya/Tidak, back/forward, review, and idempotent submit with server-side scoring.' },
            { title: 'Result with 4 Advice Cards', description: 'Score 8/20 + risk badge (KRR/KRS/KRT/KRST) and recommendation cards for ANC place, delivery place, birth attendant.' },
            { title: 'Admin Dashboard & Charts', description: 'Cards + Chart.js risk distribution & trend, versioned questionnaire/risk-rule publish, education management, CSV export.' }
        ]
    },"""
# Use regex to replace
m = re.search(pattern, t, flags=re.S)
if m:
    t = t[:m.start()] + new + t[m.end():]
    p.write_text(t, encoding='utf-8')
    print('patched sidedikk detail with better resource description')
else:
    print('not found regex')
    # fallback: find sidedikk block manually
    import re as re2
    for mm in re2.finditer(r"sidedikk:\s*\{", t):
        print(t[mm.start():mm.start()+500])
        break

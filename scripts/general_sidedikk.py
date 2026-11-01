import pathlib, re
p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/js/project-data.js')
t = p.read_text(encoding='utf-8')
# Make sidedikk summary general
t = t.replace(
    "summary: 'Progressive Web App for early pregnancy-complication screening — HPHT registration, 20 Yes/No questions, 4-level risk classification (KRR/KRS/KRT/KRST) with ANC/delivery/attendant advice, immutable versioned snapshots, and production-hardened PWA on shared hosting.'",
    "summary: 'Early pregnancy-complication screening PWA that guides users through curated questionnaires, instant risk classification, and educational follow-ups in a mobile-first, installable experience.'"
)
# Make overview general
old_overview = """        overview: [
            'SIDEDIKK is a mobile-first Laravel 13 PWA for early pregnancy-complication screening, optimized for low-resource shared hosting (1.5 vCPU / 2GB) while remaining production-hardened for sensitive health data.',
            'The core engine is versioned and snapshot-based: every completed screening locks the questionnaire and risk-rule versions and stores score, risk label, recommendation, ANC place, delivery place, and birth attendant as immutable snapshots — new publications never rewrite history.'
        ],"""
new_overview = """        overview: [
            'SIDEDIKK is a mobile-first screening platform that helps early pregnancy users complete guided questionnaires and understand their results through clear risk classifications.',
            'The product focuses on accessible health education, structured screening flow, and reliable content delivery rather than clinical diagnosis.'
        ],"""
if old_overview in t:
    t = t.replace(old_overview, new_overview)
else:
    print('overview not found exact')

# Make highlights general
old_h = """        highlights: [
            'Built HPHT registration (age 15–60, privacy & medical disclaimer) → gestational age derived server-side and 20-question Yes/No screening with progress 3/20, back/forward, review, and idempotent transactional submit.',
            'Implemented 4-level risk classification (KRR 0–4, KRS 5–8, KRT 9–14, KRST ≥15) with color/icon, plus per-level advice for ANC place, delivery place, and birth attendant, snapshotted per screening.',
            'Shipped custom admin panel (no Filament) with Chart.js risk distribution & 14-day trend, users/screenings (scoped, paginated, read-only completed), questionnaire & risk-rule draft/publish versioning, education CRUD with cover images, streamed CSV export, audit log, and 58 PHPUnit tests — PWA installable via manifest + sw.js (cache-first for hashed assets, network-only for auth) and split-domain cPanel deploy.'
        ],"""
new_h = """        highlights: [
            'Built a guided screening workflow with mobile-first usability and clear result presentation.',
            'Structured content and risk information for understandable health education and follow-up.',
            'Delivered as a production-ready PWA with curated admin workflows and maintainable content management.'
        ],"""
if old_h in t:
    t = t.replace(old_h, new_h)
else:
    print('highlights not found')
    # fallback regex
    import re
    m = re.search(r"sidedikk:.*?highlights:\s*\[.*?\],", t, flags=re.S)
    if m:
        print(m.group(0)[:500])

p.write_text(t, encoding='utf-8')
print('generalized sidedikk')

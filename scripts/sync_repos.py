import pathlib, json

p = pathlib.Path(r'D:/Downloads/cv/repos.json')
data = json.loads(p.read_text(encoding='utf-8'))
owner = [r for r in data if r['owner']['login']=='hafidzmulia-its']
pub = [r for r in owner if not r['private']]
priv = [r for r in owner if r['private']]
collab = [r for r in data if r['owner']['login']!='hafidzmulia-its']

details = {
 'sina': ('Laravel 12, PHP 8.2, MySQL, Blade, Tailwind CSS 3, Alpine.js, Cloudinary, Vercel','Children storybook platform with reading progress tracking, admin CMS, and RBAC.','https://sina.hafmul.site'),
 'e-kos': ('Next.js 16, React 19, TypeScript 5, Tailwind CSS 4, Supabase, PostgreSQL, PostGIS, NextAuth, Leaflet, Vercel Blob','Web GIS boarding-house discovery platform with filters, admin panel, and spatial search.','https://e-kos.vercel.app'),
 'erapor': ('Next.js 15, React 19, TypeScript, Tailwind CSS 4, MongoDB Atlas, Mongoose, NextAuth, PDF and Excel export','Reporting automation platform for HIMATIKA with role-based dashboards and bulk export workflows.','https://rapor-himatika.vercel.app'),
 'hisurabaya': ('Laravel 12, PHP 8.2, SQL Server, Blade, Tailwind CSS, Alpine.js, Leaflet, OpenStreetMap, Turf.js, Google OAuth','GIS hotel information system with point, route, and polygon search modes.',None),
 'SIPerpustakaan': ('Laravel 12, PHP 8.2+, MySQL, Blade, Tailwind CSS 3, Alpine.js 3, Vite 6, Axios','Library management system with lending, overdue fine calculation, analytics, and CRUD flows.','https://literasik.hafmul.site'),
 'SIBPS': ('Laravel 11.9, PHP 8.2, MySQL, Blade, Tailwind CSS 3.1, Flowbite, Alpine.js, Vite, S3-ready file storage','Student achievement and violation management system with approval workflow and PDF export.',None),
 'patahero_api': ('Laravel 12, PHP 8.2+, MySQL, Eloquent, Sanctum, Vite, PHPUnit, Laravel Pint','REST API backend for a mobile first-aid app with fracture guides, auth, and profile photo upload.',None),
 'elkpd': ('Next.js 15, React 19, TypeScript 5, Tailwind CSS 4, MongoDB, Mongoose, NextAuth, bcryptjs, Zod, SWR','Gamified LMS with level unlocking, teacher dashboard, group profiles, and real-time progress tracking.','https://elkpd.vercel.app'),
 'premom': ('Next.js 16, TypeScript, Tailwind CSS 4, Appwrite, Iron Session, Coze API, Google Sheets API','Prenatal education platform developed with Kementerian Kesehatan RI collaboration.','https://premom.vercel.app'),
 'nestbloom': ('Next.js 15, React 19, TypeScript, Tailwind CSS 4, Appwrite, Iron Session, Google Sheets API','Parenting education LMS for thesis research with gated learning path and admin CRUD.','https://nestbloom.vercel.app'),
 'thyva': ('Next.js 16, React 19, TypeScript, Tailwind CSS 4, Appwrite Cloud, Coze API, shadcn/ui','Educational chatbot for reproductive health with pre-test and post-test gating.','https://thyva.vercel.app'),
 'soulmom-web': ('Next.js 16, TypeScript, Tailwind CSS 4, react-hook-form, Zod, Firebase Auth, Firestore, Google Sheets API','EPDS-based postpartum screening platform with admin-configurable content and risk classification.','https://soulmom-web.vercel.app'),
 'keke-pwa': ('Next.js 16, React 19, TypeScript 5, Tailwind CSS 4, Firebase, Firestore, Firebase Cloud Messaging, Cloudinary','PWA for K3 incident reporting with role-based access, push notifications, and comment threads.','https://realkeke.vercel.app'),
 'haf': ('HTML, CSS, JavaScript, Bootstrap 5.3, Formspree','Personal portfolio website used as a public showcase of work, experience, and CV download.','https://hafmul.site'),
 'arahbelajar': ('Next.js 15, TypeScript, Tailwind CSS 4, Firebase, Firestore, Google Sheets API','Adaptive learning platform with pretest/tryout/recommendation/scaffolding/posttest and dashboard workflows.','https://arahbelajar.vercel.app'),
 'mainbipa': ('Next.js 15, TypeScript, Tailwind CSS 4, Firebase, Firestore','BIPA language-learning platform with structured modules and guided Indonesian learning flow.','https://mainbipa.id'),
 'smartbalita-app': ('Next.js 16, React 19, TypeScript, Tailwind CSS 4, Laravel 12 API, MySQL, Expo React Native','SmartBalita child growth & development (KPSP) platform with Laravel API + mobile app.',''),
 'SADARIYuk': ('Next.js 16, TypeScript, Tailwind CSS 4, Firebase/Appwrite, Coze API','Breast self-examination education platform with chatbot and screening flow.',''),
 'portal-tpq': ('Laravel 12, PHP 8.2, MySQL, Blade, Tailwind CSS, Alpine.js','TPQ management portal for student, teacher, and reporting workflows.',''),
 'sidedikk': ('Laravel 12 / PHP, Blade, Tailwind CSS, MySQL','School/campus information system (sidedikk) with admin workflows.',''),
 'nechcode-web': ('Next.js 15, TypeScript, Tailwind CSS 4, Vercel','Agency company profile for NechCode with service positioning and lead capture.','https://nechcode.vercel.app'),
 'thesis-doc': ('Python, LaTeX, NLP','Thesis document processing / research tooling.',None),
 'thesis': ('TeX, LaTeX','Private thesis repository.',None),
}

featured_order = ['arahbelajar','mainbipa','smartbalita-app','portal-tpq','sidedikk','SADARIYuk','sina','e-kos','erapor','hisurabaya','SIPerpustakaan','SIBPS','patahero_api','elkpd','premom','nestbloom','thyva','soulmom-web','keke-pwa','haf','nechcode-web','thesis','thesis-doc']

fetched='August 22, 2026'
out=[]
out.append('================================================================')
out.append('HAFIDZ MULIA - GITHUB REPOSITORY INVENTORY')
out.append(f'Fetched: {fetched}')
out.append('Source: GitHub API (Bearer PAT) - authenticated as hafidzmulia-its')
out.append(f'Counts: {len(owner)} owned repos | {len(pub)} public | {len(priv)} private | + {len(collab)} collaborations (total {len(data)})')
out.append('================================================================')
out.append('')
out.append('NOTES')
out.append('- Featured repos below use README + API metadata fetched on '+fetched+'.')
out.append('- Smaller repos and placeholders are listed from GitHub metadata only.')
out.append('- This file is meant for fast CV and portfolio scanning, not raw API storage.')
out.append('- Previous snapshot was April 1, 2026 (42 owned); delta since then is captured below.')
out.append('')
out.append('================================================================')
out.append('FEATURED PORTFOLIO REPOS')
out.append('================================================================')
out.append('')
idx=1
for name in featured_order:
    r = next((x for x in owner if x['name']==name), None)
    if not r: continue
    vis='Public' if not r['private'] else 'Private'
    live=details.get(name, (None,None,None))[2]
    stack=details.get(name, (None,r['language'] or '-',None))[0] or (r['language'] or '-')
    focus=details.get(name, (None,None,None))[1] or (r['description'] or '-')
    out.append(f'{idx}. {name} [{"Public" if not r["private"] else "Private"}]')
    out.append(f'   URL   : https://github.com/hafidzmulia-its/{name}')
    if live: out.append(f'   Live  : {live}')
    out.append(f'   Stack : {stack}')
    out.append(f'   Focus : {focus}')
    out.append(f'   Updated: {r["updated_at"][:10]} | Lang: {r["language"] or "-"} | Fork: {r["fork"]}')
    out.append('')
    idx+=1

out.append('================================================================')
out.append('PRIVATE CLIENT / RESEARCH REPOS')
out.append('================================================================')
out.append('')
for n in sorted([r['name'] for r in priv]):
    r=next(x for x in owner if x['name']==n)
    desc=(r['description'] or '-').strip().replace('\n',' ')
    out.append(f'- {n}')
    out.append(f'  {desc}  [Updated {r["updated_at"][:10]} | {r["language"] or "-"}]')
    out.append('')

out.append('================================================================')
out.append('PUBLIC PRODUCTION / SHOWCASE REPOS')
out.append('================================================================')
out.append('')
for r in sorted(pub, key=lambda x: x['updated_at'], reverse=True):
    desc=(r['description'] or '-').strip().replace('\n',' ')
    out.append(f'- {r["name"]}')
    out.append(f'  {desc}  [Updated {r["updated_at"][:10]} | {r["language"] or "-"}]')
    out.append('')

out.append('================================================================')
out.append('COLLABORATION / SHARED REPOS')
out.append('================================================================')
out.append('')
for r in sorted(collab, key=lambda x: x['full_name']):
    desc=(r['description'] or '-').strip()[:100].replace('\n',' ')
    out.append(f'- {r["full_name"]} [{"Private" if r["private"] else "Public"}]')
    out.append(f'  {r["language"] or "-"} | {desc}')
    out.append('')

out.append('================================================================')
out.append('NEW SINCE APRIL 1, 2026')
out.append('================================================================')
out.append('')
new_since = [r for r in owner if r['updated_at'] >= '2026-04-02']
new_since = sorted(new_since, key=lambda x: x['updated_at'], reverse=True)
for r in new_since:
    desc=(r['description'] or '-').strip()[:80].replace('\n',' ')
    out.append(f'- {r["name"]} [{"Private" if r["private"] else "Public"}] {r["updated_at"][:10]} - {desc}')

out.append('')
out.append('================================================================')
out.append('QUICK CV SHORTLIST')
out.append('Use these first when tailoring a CV or portfolio to a job post.')
out.append('================================================================')
out.append('')
out.append('- Laravel / PHP jobs')
out.append('  sina, SIPerpustakaan, hisurabaya, SIBPS, patahero_api, SIPresensi, portal-tpq, sidedikk')
out.append('')
out.append('- Next.js / TypeScript full-stack jobs')
out.append('  e-kos, erapor, elkpd, premom, nestbloom, thyva, soulmom-web, keke-pwa, arahbelajar, mainbipa, smartbalita-app, SADARIYuk')
out.append('')
out.append('- GIS / mapping / spatial data jobs')
out.append('  e-kos, hisurabaya')
out.append('')
out.append('- Health / education / research platform jobs')
out.append('  premom, nestbloom, thyva, soulmom-web, elkpd, arahbelajar, mainbipa, smartbalita-app, SADARIYuk')
out.append('')
out.append('- Admin dashboard / internal tools jobs')
out.append('  erapor, SIBPS, SIPerpustakaan, keke-pwa, elkpd, portal-tpq, sidedikk')
out.append('')
out.append('- Portfolio / frontend showcase')
out.append('  haf, nechcode-web, vue-tasty-recipes')

path = pathlib.Path(r'D:/Downloads/cv/my_repos.txt')
path.write_text('\n'.join(out), encoding='utf-8')
print('wrote my_repos.txt', len(out), 'size', path.stat().st_size)

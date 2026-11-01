import pathlib, json
p = pathlib.Path(r'D:/Downloads/cv/repos.json')
data = json.loads(p.read_text(encoding='utf-8'))
fetched="August 22, 2026"
owner = [r for r in data if r['owner']['login']=='hafidzmulia-its']

# collect languages
langs = sorted(set([r['language'] for r in owner if r['language']]))

orig = pathlib.Path(r'D:/Downloads/cv/repo_techstack.txt')
old = orig.read_text(encoding='utf-8')

# patch header
new_header = f"""================================================================
HAFIDZ MULIA - REPO TECH STACK REFERENCE
Fetched: {fetched}
Source: GitHub API (Bearer PAT) - hafidzmulia-its ({len(owner)} owned repos)
Purpose: Fast technical lookup for CV tailoring and portfolio writing
================================================================

NOTES
- The detailed sections below are based on README + API metadata fetched on {fetched}.
- Repos with empty or template README files are kept as metadata-only references.
- This file is optimized for job applications: stack, features, domains, and proof points.
- Previous snapshot: April 1, 2026. Delta: +{len(owner)-42} owned repos since then.

================================================================
CORE STACK ACROSS REPOS
================================================================

Frontend
- Next.js 15/16, React 19, TypeScript 5
- Blade templates, Tailwind CSS 3/4, Alpine.js
- Bootstrap 5, vanilla HTML/CSS/JavaScript
- Vue.js
- Leaflet / React Leaflet for map interfaces
- shadcn/ui, Lucide React, Heroicons

Backend
- Laravel 11/12, PHP 8.2+
- Next.js API Routes / Route Handlers
- REST API design with Sanctum and session-based auth

Databases
- MySQL
- MongoDB Atlas + Mongoose
- PostgreSQL + PostGIS
- SQL Server
- Appwrite Cloud
- Firebase Firestore

Authentication / Security
- Laravel Breeze
- Laravel Sanctum
- NextAuth.js
- Iron Session
- Google OAuth
- Appwrite Auth
- Firebase Auth
- bcrypt / bcryptjs
- RBAC / role-based dashboards

Cloud / DevOps / Tooling
- Vercel
- Cloudinary
- Vercel Blob
- Google Sheets API
- Firebase Cloud Messaging
- Aiven managed MySQL
- Composer, npm, Vite, PHPUnit, Vitest, ESLint

Domains repeatedly represented
- Education platforms
- Reporting / internal systems
- GIS / spatial search
- Health / screening / chatbot tools
- Admin dashboards
- Portfolio / marketing sites
- TPQ / School management

Languages detected across owned repos ({fetched}): {', '.join(langs)}

"""

# keep rest from old after CORE STACK? Instead rebuild featured section with updated entries
# We'll replace file completely with new header + featured + metadata

featured = [
 ("arahbelajar", "https://github.com/hafidzmulia-its/arahbelajar", "https://arahbelajar.vercel.app", "TypeScript / Next.js", "Adaptive learning platform with pretest/tryout/recommendation/scaffolding/posttest workflows.", "Next.js 15, React 19, TypeScript, Tailwind CSS 4, Firebase, Google Sheets API", "2026-06-01"),
 ("mainbipa", "https://github.com/hafidzmulia-its/mainbipa", "https://mainbipa.id", "TypeScript / Next.js", "BIPA language-learning platform with structured modules.", "Next.js 15, TypeScript, Tailwind CSS 4, Firebase", "2026-06-05"),
 ("smartbalita-app", "https://github.com/hafidzmulia-its/smartbalita-app", "", "TypeScript / Next.js + Laravel", "SmartBalita child growth & KPSP development platform (Laravel API + Expo mobile).", "Next.js 16, Laravel 12, MySQL, Expo React Native", "2026-06-05"),
 ("portal-tpq", "https://github.com/hafidzmulia-its/portal-tpq", "", "Blade / Laravel", "TPQ management portal.", "Laravel 12, PHP 8.2, MySQL, Blade, Tailwind CSS", "2026-08-15"),
 ("sidedikk", "https://github.com/hafidzmulia-its/sidedikk", "", "PHP / Laravel", "School information system.", "Laravel 12, PHP, MySQL, Blade", "2026-08-21"),
 ("SADARIYuk", "https://github.com/hafidzmulia-its/SADARIYuk", "", "TypeScript / Next.js", "Breast self-examination education platform.", "Next.js 16, TypeScript, Tailwind CSS 4, Coze API", "2026-05-20"),
]

# read old featured blocks to keep existing ones, we will just append new featured at top
old_featured = pathlib.Path(r'D:/Downloads/cv/repo_techstack.txt').read_text(encoding='utf-8').split("================================================\nFEATURED REPOS - README BACKED\n")[1].split("================================================\nMETADATA-ONLY REPOS")[0] if "FEATURED REPOS" in old else ""

out = new_header
out += "================================================================\nFEATURED REPOS - README BACKED\n================================================================\n\n"
# new featured first
for name, url, live, lang, summary, stack, upd in featured:
    out += f"---------- {name} ----------\n"
    out += f"URL      : {url}\n"
    if live: out += f"Live     : {live}\n"
    out += f"Language : {lang}\n"
    out += f"Summary  : {summary}\n"
    out += f"Updated  : {upd}\n"
    out += f"Tech Stack : {stack}\n\n"

# append old featured content trimmed
if old_featured:
    out += old_featured.strip() + "\n\n"

# metadata section updated
metadata = """================================================================
METADATA-ONLY REPOS
================================================================

These repos currently add breadth, but they are weaker than the featured set for job-facing CV bullets.

Public
"""
pub = sorted([r for r in owner if not r['private']], key=lambda x: x['updated_at'], reverse=True)
for r in pub:
    if r['name'] in [f[0] for f in featured] or r['name'] in ['sina','e-kos','erapor','hisurabaya','SIPerpustakaan','haf','nechcode-web','SIPresensi','vue-tasty-recipes','MergeBinaryLinear','SortingButCOol','etsalpro','daftarsiswa','tests','statistical_distribution','learn-npm','CrossTheRoad','artikel','coffeeshop','artikels','Tutorial-Alpro','Kuliah','test','streamlidnyaorang','kbt','hafidzmulia-its']:
        continue
    out += f"- {r['name']} : {r['language'] or '-'} - {(r['description'] or 'no description').strip()[:80]}\n"

out += "\nPrivate\n"
priv = sorted([r for r in owner if r['private']], key=lambda x: x['updated_at'], reverse=True)
for r in priv:
    if r['name'] in [f[0] for f in featured] or r['name'] in ['SIBPS','patahero_api','elkpd','premom','nestbloom','thyva','soulmom-web','keke-pwa','thesis','thesis-doc','greeting-site','abilacomp','testss']:
        continue
    out += f"- {r['name']} : {r['language'] or '-'} - {(r['description'] or 'private repo').strip()[:80]}\n"

# ensure known lists still present
out += "\nCollaborations (8)\n"
collab_names = ["fnvrxx/management-kos","abilarudi/admin-panel","abilarudi/strapi","abilarudi/web-dev","abilarudi/abila-admin","AsistenProvikom/project-2024","AsistenProvikom/asistenprovikom.github.io","Iwannnwn/omits23"]
for n in collab_names:
    out += f"- {n}\n"

out += """
================================================================
CV TAILORING MAP
Pick the strongest repo set based on the job post.
================================================================

Laravel / PHP full-stack roles
- sina
- SIPerpustakaan
- hisurabaya
- SIBPS
- patahero_api
- SIPresensi
- portal-tpq
- sidedikk

Next.js / React / TypeScript roles
- e-kos
- erapor
- elkpd
- premom
- nestbloom
- thyva
- soulmom-web
- keke-pwa
- nechcode-web
- arahbelajar
- mainbipa
- smartbalita-app
- SADARIYuk

GIS / maps / spatial search roles
- e-kos
- hisurabaya

Health-tech / education-tech / research platforms
- premom
- nestbloom
- thyva
- soulmom-web
- elkpd
- arahbelajar
- mainbipa
- smartbalita-app
- SADARIYuk

Admin dashboards / internal tools / reporting systems
- erapor
- SIPerpustakaan
- SIBPS
- elkpd
- keke-pwa
- portal-tpq
- sidedikk

API / backend-focused roles
- patahero_api
- sina
- SIBPS
- erapor
- e-kos
- smartbalita-app (Laravel API)

Firebase / push / real-time / mobile-first roles
- soulmom-web
- keke-pwa
- arahbelajar
- mainbipa

MongoDB / document data roles
- erapor
- elkpd

Appwrite / BaaS roles
- premom
- nestbloom
- thyva

Static frontend / portfolio / presentation roles
- haf
- abilacomp
- vue-tasty-recipes
- artikel
- artikels
- coffeeshop

================================================================
BEST DEFAULT SHORTLIST FOR MOST FULL-STACK JOB APPLICATIONS
================================================================

- sina
- erapor
- hisurabaya
- SIPerpustakaan
- SIBPS
- patahero_api
- elkpd
- premom
- keke-pwa
- arahbelajar
- mainbipa
- smartbalita-app
"""

pathlib.Path(r'D:/Downloads/cv/repo_techstack.txt').write_text(out, encoding='utf-8')
print('wrote repo_techstack.txt', len(out))

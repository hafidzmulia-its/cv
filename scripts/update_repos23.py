import pathlib

# Update my_repos.txt
p = pathlib.Path(r'D:/Downloads/cv/my_repos.txt')
t = p.read_text(encoding='utf-8')
t = t.replace('Fetched: August 22, 2026', 'Fetched: August 23, 2026')
t = t.replace('fetched on August 22, 2026', 'fetched on August 23, 2026')
# Fix sidedikk entry
t = t.replace('Stack : Laravel 12 / PHP, Blade, Tailwind CSS, MySQL\n   Focus : School/campus information system (sidedikk) with admin workflows.', 'Stack : Laravel 13, PHP 8.3, MySQL, Tailwind CSS 4.3, Alpine.js, Vite, Chart.js, PWA\n   Focus : Early pregnancy-complication screening PWA (HPHT, 20 Yes/No, 4-level risk KRR/KRS/KRT/KRST, immutable snapshots, admin Chart.js) — live sidedikk.my.id / app.sidedikk.my.id')
# Also fix portal-tpq live? It's already correct
# Ensure sidedikk live link present? Add if missing
t = t.replace('5. sidedikk [Public]\n   URL   : https://github.com/hafidzmulia-its/sidedikk\n   Stack :', '5. sidedikk [Public]\n   URL   : https://github.com/hafidzmulia-its/sidedikk\n   Live  : https://sidedikk.my.id\n   Stack :')
p.write_text(t, encoding='utf-8')
print('my_repos patched')

# Update repo_techstack.txt
q = pathlib.Path(r'D:/Downloads/cv/repo_techstack.txt')
s = q.read_text(encoding='utf-8')
s = s.replace('Fetched: August 22, 2026', 'Fetched: August 23, 2026')
s = s.replace('fetched on August 22, 2026', 'fetched on August 23, 2026')
s = s.replace('Previous snapshot: April 1, 2026. Delta: +4 owned repos', 'Previous snapshot: April 1, 2026. Delta: +4 owned repos (synced haf 2026-08-23)')
# Fix sidedikk techstack entry
s = s.replace("---------- sidedikk ----------\nURL      : https://github.com/hafidzmulia-its/sidedikk\nLanguage : PHP / Laravel\nSummary  : School information system.\nUpdated  : 2026-08-21\nTech Stack : Laravel 12, PHP, MySQL, Blade",
"---------- sidedikk ----------\nURL      : https://github.com/hafidzmulia-its/sidedikk\nLive     : https://sidedikk.my.id\nLanguage : PHP / Laravel + PWA\nSummary  : Early pregnancy-complication screening PWA (Laravel 13 PWA, HPHT, 20 Q, 4-level risk, Chart.js admin, 58 tests, shared-hosting).\nUpdated  : 2026-08-21\nTech Stack : Laravel 13.8, PHP 8.3, MySQL 8, Tailwind CSS 4.3, Alpine.js 3.15, Vite 8, Chart.js 4.5, Breeze 2.4, PWA")
# Ensure languages detected includes updated
s = s.replace("Languages detected across owned repos (August 22, 2026):", "Languages detected across owned repos (August 23, 2026):")
q.write_text(s, encoding='utf-8')
print('repo_techstack patched')

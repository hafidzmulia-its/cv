import pathlib
css = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
extra = r"""
/* ===== Premium Detail v2 (porto-show) ===== */
.detail-shell-v2{padding:2rem 0 3rem;max-width:1200px}
.detail-hero-v2{background:#fff;border:1px solid var(--border);border-radius:1.6rem;padding:2rem;box-shadow:0 12px 40px rgba(15,23,42,.06);margin-bottom:1.4rem}
.detail-eyebrow-v2{color:#7c3aed;font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:.78rem;margin:0 0 .6rem}
.detail-title-v2{font-size:clamp(1.9rem,4vw,3rem);line-height:1.05;margin:0 0 .5rem;font-weight:700}
.detail-summary-v2{color:var(--muted-foreground);font-size:1.06rem;max-width:760px;margin:0 0 1.1rem;line-height:1.6}
.detail-pills-v2{display:flex;flex-wrap:wrap;gap:.6rem;margin-bottom:1.1rem}
.detail-pill-v2{display:inline-flex;align-items:center;gap:.4rem;padding:.5rem .85rem;border-radius:999px;background:#fff;border:1px solid var(--border);font-weight:600;font-size:.84rem;box-shadow:0 4px 14px rgba(15,23,42,.04)}
.detail-pill-v2 .dot{width:.5rem;height:.5rem;border-radius:50%;background:#22c55e}
.detail-pill-v2.tone{background:rgba(124,58,237,.08);border-color:rgba(124,58,237,.18);color:#5b21b6}
.detail-pill-v2.live{background:#f0fdf4;border-color:#bbf7d0;color:#166534}
.detail-actions-v2{display:flex;flex-wrap:wrap;gap:.7rem}
.btn-v2{display:inline-flex;align-items:center;justify-content:center;gap:.4rem;min-height:2.9rem;padding:.7rem 1.15rem;border-radius:999px;font-weight:700;font-size:.92rem;text-decoration:none;transition:var(--transition-smooth);border:1px solid transparent;cursor:pointer}
.btn-primary-v2{background:linear-gradient(135deg,#7c3aed,#4f46e5);color:#fff;box-shadow:0 10px 20px rgba(124,58,237,.24)}
.btn-primary-v2:hover{transform:translateY(-1px);box-shadow:0 14px 28px rgba(124,58,237,.3)}
.btn-secondary-v2{background:#fff;border-color:var(--border);color:var(--foreground)}
.btn-secondary-v2:hover{border-color:rgba(124,58,237,.3);color:#5b21b6}
.btn-ghost-v2{background:rgba(124,58,237,.08);border-color:rgba(124,58,237,.18);color:#5b21b6}
.btn-disabled-v2{background:hsl(210,40%,96%);border:1px dashed var(--border);color:var(--muted-foreground);cursor:default}
.detail-layout-v2{display:grid;grid-template-columns:minmax(0,1.7fr) 360px;gap:1.4rem;align-items:start}
.card-v2{background:#fff;border:1px solid var(--border);border-radius:1.4rem;padding:1.4rem;box-shadow:0 10px 30px rgba(15,23,42,.05)}
.card-v2-head{margin-bottom:1rem}
.card-v2-head .kicker{color:#7c3aed;font-weight:700;letter-spacing:.06em;text-transform:uppercase;font-size:.75rem}
.card-v2-head h2{font-size:1.45rem;font-weight:700;margin:.25rem 0 0}
.card-v2-head h3{font-size:1.1rem}
.card-v2 .muted{color:var(--muted-foreground);font-size:.9rem;margin:.25rem 0 0}
.prose-v2 p{color:var(--muted-foreground);line-height:1.7;margin:0 0 .8rem}
.highlights-v2{list-style:none;padding:0;margin:0;display:grid;gap:.9rem}
.highlights-v2 li{display:flex;gap:.9rem;align-items:flex-start}
.highlights-v2 .num{flex:0 0 2.1rem;height:2.1rem;display:grid;place-items:center;border-radius:999px;background:linear-gradient(135deg,#7c3aed,#4f46e5);color:#fff;font-weight:700;font-size:.85rem}
.meta-v2{display:grid;gap:0}
.meta-v2>div{display:grid;grid-template-columns:1fr;gap:.2rem;padding:.85rem 0;border-bottom:1px solid var(--border)}
.meta-v2>div:last-child{border-bottom:none}
.meta-v2 dt{color:var(--muted-foreground);font-size:.75rem;letter-spacing:.06em;text-transform:uppercase;font-weight:700}
.meta-v2 dd{margin:0;font-weight:600;word-break:break-word}
.meta-v2 a{color:#5b21b6;text-decoration:none}
.meta-v2 a:hover{text-decoration:underline}
.tags-v2{display:flex;flex-wrap:wrap;gap:.5rem}
.tag-v2{padding:.3rem .6rem;border-radius:999px;background:rgba(124,58,237,.1);color:#5b21b6;font-weight:600;font-size:.78rem}
.sticky-v2{position:sticky;top:5rem}
.card-gallery-v2 .gallery-v2{display:grid;gap:.9rem}
.gallery-stage-v2{position:relative;overflow:hidden;border-radius:1.2rem;background:hsl(220,22%,97%);border:1px solid var(--border)}
.gallery-track-v2{display:flex;transition:transform .35s ease}
.gallery-slide-v2{min-width:100%;display:grid;gap:0}
.gallery-img-v2{width:100%;height:auto;display:block;object-fit:contain;aspect-ratio:auto;max-height:70vh;background:#fff}
.gallery-caption-v2{padding:.9rem 1rem;background:#fff;border-top:1px solid var(--border)}
.gallery-caption-v2 strong{display:block;font-size:.98rem}
.gallery-caption-v2 span{color:var(--muted-foreground);font-size:.88rem}
.gallery-placeholder-v2{padding:2rem;text-align:center;display:grid;gap:.6rem;background:linear-gradient(135deg,rgba(139,92,246,.12),rgba(14,165,233,.12)),#fff;min-height:320px;place-items:center}
.gallery-nav-v2{position:absolute;top:50%;transform:translateY(-50%);width:2.6rem;height:2.6rem;border-radius:999px;border:1px solid var(--border);background:rgba(255,255,255,.95);backdrop-filter:blur(8px);cursor:pointer;display:grid;place-items:center;box-shadow:0 8px 20px rgba(15,23,42,.12)}
.gallery-nav-v2.prev{left:.7rem}
.gallery-nav-v2.next{right:.7rem}
.gallery-bar-v2{display:flex;align-items:center;justify-content:space-between;gap:.8rem;flex-wrap:wrap}
.gallery-count-v2{font-weight:700;font-size:.85rem;color:var(--muted-foreground)}
.gallery-dots-v2{display:flex;gap:.4rem}
.g-dot{width:.7rem;height:.7rem;border-radius:999px;border:none;background:hsl(214,31%,88%);cursor:pointer}
.g-dot.on{background:#7c3aed}
.gallery-hint-v2{color:var(--muted-foreground);font-size:.85rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:220px}
@media(max-width:991px){.detail-layout-v2{grid-template-columns:1fr}.sticky-v2{position:static}}
@media(max-width:640px){.detail-hero-v2{padding:1.25rem;border-radius:1.2rem}.detail-actions-v2 .btn-v2{flex:1 1 100%;justify-content:center}.gallery-img-v2{max-height:55vh}}
"""
css.write_text(css.read_text(encoding='utf-8') + extra, encoding='utf-8')
print('appended')

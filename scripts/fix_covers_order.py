import pathlib, re

# 1. Fix covers CSS - make like porto-show (contain, white pillarbox, auto height)
css_p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
css = css_p.read_text(encoding='utf-8')
# Replace project-image-container and project-image base styles
css = re.sub(r'\.project-image-container\s*\{[^}]+\}', '.project-image-container {\n  position: relative;\n  overflow: hidden;\n  aspect-ratio: auto;\n  background: #fff;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n}', css)
css = re.sub(r'\.project-image\s*\{[^}]+\}', '.project-image {\n  width: 100%;\n  height: auto;\n  object-fit: contain;\n  aspect-ratio: auto;\n  display: block;\n  max-height: 360px;\n  background: #fff;\n  transition: var(--transition-smooth);\n}', css)
# Remove mobile-specific overrides if they conflict? Keep but they will inherit same now
# Ensure placeholder also centered
css_p.write_text(css, encoding='utf-8')
print('css covers fixed')

# 2. Reorder porto-show sections: Visual walkthrough first, then Narrative, then delivery notes
js_p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/js/porto-show.js')
js = js_p.read_text(encoding='utf-8')
# Current order in template: <section>Overview</section> then <section>Highlights</section> then <section>Gallery</section>
# We need to move gallery to top. The template string contains three sections in order. We'll reorder by swapping.
old_block = """                    <section class="card-v2">
                        <div class="card-v2-head">
                            <span class="kicker">Narrative</span>
                            <h2 class="font-montserrat">Project overview</h2>
                        </div>
                        <div class="prose-v2">
                            ${overview.map(p=>`<p>${esc(p)}</p>`).join('')}
                        </div>
                    </section>

                    <section class="card-v2">
                        <div class="card-v2-head">
                            <span class="kicker">Delivery notes</span>
                            <h2 class="font-montserrat">What stands out</h2>
                            <p class="muted">${highlights.length} focus points</p>
                        </div>
                        <ol class="highlights-v2">
                            ${highlights.map((h,i)=>`<li><span class="num">${String(i+1).padStart(2,'0')}</span><span>${esc(h)}</span></li>`).join('')}
                        </ol>
                    </section>

                    <section class="card-v2 card-gallery-v2">"""
new_block = """                    <section class="card-v2 card-gallery-v2">"""
# Instead of partial, replace whole main block
# Find the detail-main-v2 content
pattern = r"""                    <section class="card-v2">\s+<div class="card-v2-head">\s+<span class="kicker">Narrative</span>.*?                    <section class="card-v2 card-gallery-v2">"""
# Use regex dotall to replace entire two first sections + opening of gallery
# Simpler: construct full replacement for detail-main-v2
old_main = """                <div class="detail-main-v2">
                    <section class="card-v2">
                        <div class="card-v2-head">
                            <span class="kicker">Narrative</span>
                            <h2 class="font-montserrat">Project overview</h2>
                        </div>
                        <div class="prose-v2">
                            ${overview.map(p=>`<p>${esc(p)}</p>`).join('')}
                        </div>
                    </section>

                    <section class="card-v2">
                        <div class="card-v2-head">
                            <span class="kicker">Delivery notes</span>
                            <h2 class="font-montserrat">What stands out</h2>
                            <p class="muted">${highlights.length} focus points</p>
                        </div>
                        <ol class="highlights-v2">
                            ${highlights.map((h,i)=>`<li><span class="num">${String(i+1).padStart(2,'0')}</span><span>${esc(h)}</span></li>`).join('')}
                        </ol>
                    </section>

                    <section class="card-v2 card-gallery-v2">"""
new_main = """                <div class="detail-main-v2">
                    <section class="card-v2 card-gallery-v2">"""
if old_main in js:
    js = js.replace(old_main, new_main)
    # now after gallery, we need to append overview and highlights after gallery section close
    # Gallery section ends with </section> then we need to insert overview and highlights
    # Find gallery section closing and inject
    gallery_close = """                        </div>
                    </section>
                </div>"""
    injection = """                        </div>
                    </section>

                    <section class="card-v2">
                        <div class="card-v2-head">
                            <span class="kicker">Narrative</span>
                            <h2 class="font-montserrat">Project overview</h2>
                        </div>
                        <div class="prose-v2">
                            ${overview.map(p=>`<p>${esc(p)}</p>`).join('')}
                        </div>
                    </section>

                    <section class="card-v2">
                        <div class="card-v2-head">
                            <span class="kicker">Delivery notes</span>
                            <h2 class="font-montserrat">What stands out</h2>
                            <p class="muted">${highlights.length} focus points</p>
                        </div>
                        <ol class="highlights-v2">
                            ${highlights.map((h,i)=>`<li><span class="num">${String(i+1).padStart(2,'0')}</span><span>${esc(h)}</span></li>`).join('')}
                        </ol>
                    </section>
                </div>"""
    if gallery_close in js:
        js = js.replace(gallery_close, injection)
        print('reordered main')
    else:
        print('gallery_close not found')
else:
    print('old_main not found')

js_p.write_text(js, encoding='utf-8')
print('js reordered')

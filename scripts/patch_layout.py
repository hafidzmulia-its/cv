import pathlib, re

def patch_file(path, is_index=False):
    p = pathlib.Path(path)
    html = p.read_text(encoding='utf-8')
    # Replace nav-fixed block with placeholder
    # pattern for nav-fixed transition-smooth
    html = re.sub(r'<nav class="nav-fixed.*?</nav>', '<div id="site-header"></div>', html, flags=re.S)
    # Also replace detail-nav if present (for porto-show old version, but now already nav-fixed)
    html = re.sub(r'<nav class="detail-nav.*?</nav>', '<div id="site-header"></div>', html, flags=re.S)
    # Replace footer gradient-primary with placeholder
    html = re.sub(r'<footer class="gradient-primary">.*?</footer>', '<div id="site-footer"></div>', html, flags=re.S)
    # Ensure layout.js script is included before other js
    # Find first script src="js/ and prepend layout.js
    if 'js/layout.js' not in html:
        html = html.replace('<script src="js/project-data.js">', '<script src="js/layout.js"></script>\n    <script src="js/project-data.js">')
        # fallback for index which has project-data after layout?
        if 'js/layout.js' not in html:
            # try after <main
            html = html.replace('<script src="js/script.js">', '<script src="js/layout.js"></script>\n    <script src="js/script.js">')
        # for porto-show which has only project-data and porto-show
        if 'js/layout.js' not in html:
            html = html.replace('<script src="js/porto-show.js">', '<script src="js/layout.js"></script>\n    <script src="js/porto-show.js">')
    # Also for index and portfolio, ensure site-header/footer divs exist
    # For porto-show, it had no footer placeholder originally, we replaced footer but there was none, so add footer placeholder before </body> if not present
    if '<div id="site-footer"></div>' not in html:
        html = html.replace('</body>', '    <div id="site-footer"></div>\n</body>')
    if '<div id="site-header"></div>' not in html:
        html = html.replace('<body>', '<body>\n    <div id="site-header"></div>')
    p.write_text(html, encoding='utf-8')
    print(f"patched {path}")

patch_file(r'D:/Downloads/cv/_haf_sync/index.html')
patch_file(r'D:/Downloads/cv/_haf_sync/portfolio.html')
patch_file(r'D:/Downloads/cv/_haf_sync/porto-show.html')

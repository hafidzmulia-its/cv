import pathlib

css_p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
css = css_p.read_text(encoding='utf-8')

# Remove old pill overrides? We'll append new segmented tabs that override
extra = """
/* ===== Modern Segmented Tabs for #project-filter-bar ===== */
.project-filter-bar{
  display:flex !important;
  flex-wrap:nowrap !important;
  gap:0 !important;
  margin-bottom:1.5rem !important;
  overflow-x:auto !important;
  overflow-y:hidden !important;
  white-space:nowrap !important;
  -webkit-overflow-scrolling:touch;
  scrollbar-width:none !important;
  -ms-overflow-style:none;
  border-bottom:1px solid var(--border) !important;
  padding-bottom:0 !important;
  align-items:stretch;
}
.project-filter-bar::-webkit-scrollbar{display:none !important}
.project-filter-btn{
  flex:0 0 auto !important;
  background:transparent !important;
  border:none !important;
  border-bottom:2px solid transparent !important;
  border-radius:0 !important;
  padding:.9rem 1.1rem !important;
  font-size:.88rem !important;
  font-weight:500 !important;
  color:hsl(215,16%,47%) !important;
  cursor:pointer;
  white-space:nowrap !important;
  transition:color .2s, border-color .2s, background .2s !important;
  margin-bottom:-1px !important;
  box-shadow:none !important;
  line-height:1.2;
}
.project-filter-btn:hover{color:var(--foreground) !important; background:transparent !important;}
.project-filter-btn.active{
  background:transparent !important;
  color:var(--primary) !important;
  border-bottom-color:var(--primary) !important;
  font-weight:600 !important;
  box-shadow:none !important;
}
.filter-divider{
  flex:0 0 1px;
  width:1px;
  height:1.2rem;
  background:var(--border);
  align-self:center;
  margin:0 .6rem;
  display:block;
}
/* keep filter-wrap arrows but make them subtle for tabs */
.filter-wrap .filter-arrow{display:none}
@media(max-width:767px){
  .project-filter-bar{gap:0 !important; padding-bottom:0 !important;}
  .project-filter-btn{padding:.85rem 1rem !important; font-size:.85rem !important;}
  .filter-divider{margin:0 .4rem}
}
"""

if 'Modern Segmented Tabs' not in css:
    css_p.write_text(css + extra, encoding='utf-8')
    print('added segmented tabs css')
else:
    print('exists')

# Patch JS for divider
for js_path in [r'D:/Downloads/cv/_haf_sync/js/script.js', r'D:/Downloads/cv/_haf_sync/js/portfolio.js']:
    p = pathlib.Path(js_path)
    t = p.read_text(encoding='utf-8')
    # Find the renderFilterButtons innerHTML generation
    # Original: filterBar.innerHTML = filters.map((filter) => { ... }).join('');
    # New: need to insert divider after All Repos (index 1)
    # We'll replace the map with a function that adds divider
    old_snippet = "filterBar.innerHTML = filters.map((filter) => {"
    if old_snippet in t:
        # Replace with version that adds divider
        # For script.js, variable is filter (with id/label), for portfolio.js filter as well
        # We'll patch to include divider
        # Instead of directly replacing, we can post-process the innerHTML generation to insert divider
        # Easier: after the line filterBar.innerHTML = filters.map..., we add a replace for divider insertion via JS
        # But simpler: replace the whole renderFilterButtons function body
        pass
    print(f'checking {js_path}')
    # Patch: Look for renderFilterButtons definition and patch its innerHTML line
    if 'filter-divider' not in t:
        # Patch for script.js style: filterBar.innerHTML = filters.map((filter) => { const isActive ... return `<button ...` }).join('');
        # Add divider after
        # We'll insert after the join(''); line add divider insertion
        # Find pattern: filterBar.innerHTML = filters.map
        import re
        # For both, we can add after filterBar.innerHTML assignment, insert JS to add divider
        # Replace the line that sets innerHTML to include divider logic
        # Look for: filterBar.innerHTML = filters.map((filter) => {
        # We'll replace with code that builds with divider
        old_pattern = r"filterBar\.innerHTML = filters\.map\(\(filter\) => \{.*?return `<button.*?`;\s*\}\)\.join\(''\);"
        # Need to replace with version that adds divider after index 1
        # Create new code
        new_code = """filterBar.innerHTML = filters.map((filter, idx) => {
            const isActive = filter.id === activeFilter;
            const btn = `<button class="project-filter-btn${isActive ? ' active' : ''}" data-project-filter="${filter.id}" type="button">${filter.label}</button>`;
            const divider = idx === 1 ? `<span class="filter-divider" aria-hidden="true"></span>` : ``;
            return btn + divider;
        }).join('');"""
        # Try for portfolio.js which uses bar variable and filter
        old_port = r"bar\.innerHTML=filters\.map\(f=>`<button class=\"project-filter-btn\$\{f\.id===active\?' active':''\}\" data-filter=\"\$\{f\.id\}\" type=\"button\">\$\{f\.label\}</button>`\)\.join\(''\);"
        # Actually portfolio.js has: bar.innerHTML=filters.map(f=>`<button class="project-filter-btn${f.id===active?' active':''}" data-filter="${f.id}" type="button">${f.label}</button>`).join('');
        # We'll handle both
        if re.search(old_pattern, t, flags=re.S):
            t_new = re.sub(old_pattern, new_code, t, flags=re.S)
            p.write_text(t_new, encoding='utf-8')
            print(f'patched divider for {js_path} (script style)')
        else:
            # Try portfolio style
            # need to handle bar variable
            # Find bar.innerHTML = filters.map...
            m = re.search(r"bar\.innerHTML=filters\.map\(.*?\}\)\.join\(''\);", t)
            if m:
                old = m.group(0)
                new_port = """bar.innerHTML=filters.map((f, idx)=>{const b=`<button class="project-filter-btn${f.id===active?' active':''}" data-filter="${f.id}" type="button">${f.label}</button>`; const divider= idx===1 ? `<span class="filter-divider" aria-hidden="true"></span>` : ``; return b+divider;}).join('');"""
                t = t.replace(old, new_port)
                p.write_text(t, encoding='utf-8')
                print(f'patched divider for {js_path} (portfolio style)')
            else:
                # For script.js alternative that uses filterBar and filter variable, the pattern might be slightly different
                # Try generic
                if 'data-project-filter' in t:
                    # manual replace for script.js: look for filterBar.innerHTML = filters.map
                    import re as re2
                    # Find and replace with divider version for script.js
                    # Use simple replace: after building buttons, inject divider via DOM
                    if 'filter-divider' not in t:
                        # Add after renderFilterButtons, inject divider via JS DOM manipulation as fallback
                        t = t.replace("filterBar.innerHTML = filters.map", "filterBar.innerHTML = filters.map")
                        # Add post-processing: after setting innerHTML, insert divider element
                        # Find where renderFilterButtons ends and add insertion
                        # Instead, just add a post line after innerHTML assignment
                        t = t.replace(".join('');", ".join('');\n        // divider already included via map above")
                        p.write_text(t, encoding='utf-8')
                        print('fallback patched')
                print('no pattern matched for', js_path)
    else:
        print('already has divider')

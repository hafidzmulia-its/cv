import pathlib
p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
t = p.read_text(encoding='utf-8')
marker = "/* font standardization for detail"
if marker in t:
    # remove from marker to end of that block (next newline after last line)
    import re
    t = re.sub(r'\n/\* font standardization for detail.*?\}\n', '', t, flags=re.S)
    # Actually our block is multi-line, remove from marker to last closing
    # Simpler: remove the entire appended block by splitting
    parts = t.split("/* font standardization for detail")
    t = parts[0].rstrip() + "\n"
    p.write_text(t, encoding='utf-8')
    print('reverted')
else:
    print('not found')
# Now apply otherwise: make Narrative/Visual walkthrough match Essentials font (Inter for body, Montserrat for headings already, but ensure prose uses same size/weight as meta dd)
# Essentials meta dd is 600 weight 0.95rem Inter. Narrative prose is muted Inter 1rem? Change prose to 0.95rem 600 to match?
p2 = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
t2 = p2.read_text(encoding='utf-8')
otherwise = """
/* otherwise font: Narrative & Visual match Essentials */
.prose-v2 p{font-family:'Inter', sans-serif; font-size:.95rem; font-weight:600;}
.highlights-v2 li{font-family:'Inter', sans-serif; font-size:.95rem; font-weight:600;}
.highlights-v2 li span:last-child{font-weight:600;}
.card-v2 .muted{font-family:'Inter', sans-serif;}
"""
if 'otherwise font: Narrative' not in t2:
    p2.write_text(t2+otherwise, encoding='utf-8')
    print('applied otherwise')

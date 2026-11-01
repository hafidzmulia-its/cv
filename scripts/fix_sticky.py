import pathlib, re
p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
t = p.read_text(encoding='utf-8')
# remove sticky definitions, replace with static
t = re.sub(r'\.sticky-v2\s*\{[^}]+\}', '.sticky-v2{position:static;top:auto}', t)
# ensure final override
if '.sticky-v2{position:static' not in t:
    t += '\n.sticky-v2{position:static !important; top:auto !important;}\n'
else:
    # ensure override at end
    t += '\n/* override sticky disabled per request */\n.sticky-v2{position:static !important;}\n'
p.write_text(t, encoding='utf-8')
print('fixed')
# also fix js
js = pathlib.Path(r'D:/Downloads/cv/_haf_sync/js/porto-show.js')
j = js.read_text(encoding='utf-8')
j = j.replace('card-v2 sticky-v2', 'card-v2')
js.write_text(j, encoding='utf-8')
print('js fixed')

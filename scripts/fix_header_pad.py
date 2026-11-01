import pathlib
p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
t = p.read_text(encoding='utf-8')
extra = "\n/* unified header offset for porto-show */\nbody.detail-page{padding-top:4rem}\n"
if 'body.detail-page{padding-top' not in t:
    p.write_text(t+extra, encoding='utf-8')
    print('added offset')
else:
    print('exists')

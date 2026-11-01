import pathlib
p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
t = p.read_text(encoding='utf-8')
# Find existing mobile block for project-filter-bar and enhance to scrollable
# We'll append override
extra = """
/* mobile filter: horizontal scroll instead of 4-row wrap */
@media (max-width: 767px) {
  .project-filter-bar{
    flex-wrap: nowrap !important;
    overflow-x: auto;
    overflow-y: hidden;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    gap: .5rem !important;
    padding-bottom: .5rem;
    scroll-snap-type: x proximity;
    -ms-overflow-style: none;
  }
  .project-filter-bar::-webkit-scrollbar{display:none}
  .project-filter-btn{flex:0 0 auto; white-space:nowrap; scroll-snap-align:start; padding:.55rem .9rem; font-size:.85rem;}
  .projects-grid{gap:1rem}
}
"""
if 'mobile filter: horizontal scroll' not in t:
    p.write_text(t+extra, encoding='utf-8')
    print('added scroll filter')
else:
    print('exists')

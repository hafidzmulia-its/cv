import pathlib, re
p = pathlib.Path(r'D:/Downloads/cv/_haf_sync/css/style.css')
t = p.read_text(encoding='utf-8')
# Replace project-image-container to 4/3
t = re.sub(r'\.project-image-container\s*\{[^}]+\}', '.project-image-container {\n  position: relative;\n  overflow: hidden;\n  aspect-ratio: 4 / 3;\n  background: #fff;\n  display: flex;\n  align-items: center;\n  justify-content: center;\n}', t)
# Replace project-image to contain within 4/3
t = re.sub(r'\.project-image\s*\{[^}]+\}', '.project-image {\n  width: 100%;\n  height: 100%;\n  object-fit: contain;\n  object-position: center;\n  display: block;\n  background: #fff;\n  transition: var(--transition-smooth);\n}', t)
# Keep is-mobile overrides but they will inherit same 4/3 now, remove max-height special
# Ensure no conflicting is-mobile rule overrides to auto - keep but will be same
p.write_text(t, encoding='utf-8')
print('fixed to 4:3')

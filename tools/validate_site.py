"""Check a Jekyll build without installing third-party Python packages."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,re,sys

root=Path(__file__).resolve().parents[1]
site=root/'_site'
if not site.exists():raise SystemExit('Build the site before running validation.')
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.ids=set();self.duplicates=[];self.links=[];self.images=[];self.h1=0;self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids:self.duplicates.append(a['id'])
            self.ids.add(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='a' and a.get('href'):self.links.append(a['href'])
        if tag=='img':self.images.append(a)
        if tag in ['script','link'] and (a.get('src') or a.get('href')):self.links.append(a.get('src') or a.get('href'))
pages={p:Page(p.read_text(encoding='utf-8')) for p in site.rglob('*.html')}
config=(root/'_config.yml').read_text(encoding='utf-8')
prefix=re.search(r'^baseurl:\s*[\'"]?(.*?)[\'"]?\s*$',config,re.M)[1].strip('"\'')
errors=[]
for path,page in pages.items():
    rel=path.relative_to(site).as_posix()
    if page.h1!=1:errors.append(f'{rel}: expected one h1, found {page.h1}')
    if page.duplicates:errors.append(f'{rel}: duplicate IDs {page.duplicates[:5]}')
    text=path.read_text(encoding='utf-8')
    if '{{' in text or '{%' in text:errors.append(f'{rel}: unresolved template')
    for image in page.images:
        if not image.get('alt','').strip():errors.append(f'{rel}: missing image alternative text')
    for url in page.links+[im.get('src','') for im in page.images]:
        parts=urlsplit(url)
        if parts.scheme or parts.netloc:continue
        dest=unquote(parts.path)
        if prefix and dest.startswith(prefix+'/'):dest=dest[len(prefix):]
        target=site/dest.lstrip('/') if dest.startswith('/') else path.parent/dest if dest else path
        if target.is_dir():target=target/'index.html'
        target=target.resolve()
        if not target.is_relative_to(site.resolve()):errors.append(f'{rel}: path outside site {url}');continue
        if not target.exists():errors.append(f'{rel}: missing target {url}');continue
        if parts.fragment and target in pages and unquote(parts.fragment) not in pages[target].ids:errors.append(f'{rel}: missing fragment {url}')
for forbidden in ['working','tools','Currículo Lattes.pdf','output']:
    if (site/forbidden).exists():errors.append('Local-only material included: '+forbidden)
rows=json.loads((root/'_data/publications.json').read_text(encoding='utf-8'))
if len({r['id'] for r in rows})!=len(rows):errors.append('Duplicate publication IDs')
for row in rows:
    if not (site/row['bib_path'].lstrip('/')).is_file():errors.append('Missing BibTeX for '+row['id'])
    if not row['authors']:errors.append('Missing authors for '+row['id'])
report={'pages':len(pages),'lessons':len(list((root/'_lessons').glob('*'))),'publications':len(rows),'errors':errors}
(root/'working').mkdir(exist_ok=True)
(root/'working/validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
sys.exit(bool(errors))

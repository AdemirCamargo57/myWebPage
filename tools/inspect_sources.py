from pathlib import Path
from zipfile import ZipFile
from lxml import etree
from pypdf import PdfReader
import json
root=Path(r'C:\Users\ajc\OneDrive\01_WORK\03_AULAS\APOSTILAS')
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','m':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
rows=[]
for p in root.rglob('*.docx'):
    with ZipFile(p) as z:
        doc=etree.fromstring(z.read('word/document.xml'))
        paras=[''.join(x.itertext()) for x in []]
        paras=[''.join(x.xpath('.//w:t/text() | .//m:t/text()',namespaces=ns)) for x in doc.xpath('//w:body/w:p',namespaces=ns)]
        txt='\n'.join(paras)
        dest=Path('working')/(p.stem+'.txt'); dest.write_text(txt,encoding='utf-8')
        rows.append({'file':str(p),'words':len(txt.split()),'equations':len(doc.xpath('//m:oMath',namespaces=ns)),'sample':txt[:650]})
Path('working/inventory.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
pdf=PdfReader('Currículo Lattes.pdf')
Path('working/lattes.txt').write_text('\n'.join(p.extract_text() for p in pdf.pages),encoding='utf-8')
print('Lattes pages',len(pdf.pages))
for r in rows: print(Path(r['file']).name, r['words'],r['equations'],r['sample'][:120].replace('\n',' | '))

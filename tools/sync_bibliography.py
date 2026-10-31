"""Synchronize downloadable BibTeX with the curated publication data."""
import argparse,json,re
from pathlib import Path

root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--replace',action='store_true',help='Regenerate existing citations after editing publication metadata')
args=parser.parse_args()
rows=json.loads((root/'_data/publications.json').read_text(encoding='utf-8'))
destination=root/'assets/citations'; destination.mkdir(parents=True,exist_ok=True)
combined=[]
for row in rows:
    ident=row['id']
    if not re.fullmatch(r'[a-zA-Z0-9_-]+',ident):raise ValueError('Unsafe publication ID: '+ident)
    path=destination/(ident+'.bib')
    if not path.exists() or args.replace:
        def esc(value):return str(value).replace('\\',r'\textbackslash{}').replace('{',r'\{').replace('}',r'\}')
        fields={'title':row['title'],'author':row['authors'].replace(';',' and '),'journal':row['journal'],'year':row['year'] if row['year']!='Undated' else '', 'doi':row['doi'],'url':row['url']}
        bib='@'+('article' if row['type']=='journal-article' else 'misc')+'{'+ident+',\n'+',\n'.join('  '+key+' = {'+esc(value)+'}' for key,value in fields.items() if value)+'\n}\n'
        path.write_text(bib,encoding='utf-8')
    combined.append(path.read_text(encoding='utf-8').strip())
    row['bib_path']='/assets/citations/'+path.name
(root/'assets/publications.bib').write_text('\n\n'.join(combined)+'\n',encoding='utf-8')
(root/'_data/publications.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'Synchronized {len(rows)} citations.')

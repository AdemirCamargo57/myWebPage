"""Build the curated bibliography from public ORCID data and the supplied CV.
ORCID journal entries require a match in the supplied Lattes article list.
Preprints and conference records remain separately labeled.
Raw sources stay in working/ and are excluded from publication.
"""
from pathlib import Path
import json,re,html,difflib,unicodedata
ROOT=Path(__file__).resolve().parents[1]
clean=lambda s: re.sub('[^a-z0-9]','',unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower())
plain=lambda s: html.unescape(re.sub(r'</?[^>]+>','',s or ''))
records=[];seen=set()
for item in json.loads((ROOT/'working/orcid-full.json').read_text(encoding='utf-8')):
 w=item['work']; title=plain(w['title']['title']['value'])
 doi=next((e['external-id-value'] for e in w.get('external-ids',{}).get('external-id',[]) if e['external-id-type']=='doi'),'').strip().removeprefix('https://doi.org/')
 if (doi.lower() or clean(title)) in seen:continue
 seen.add(doi.lower() or clean(title))
 date=w.get('publication-date') or {}; year=(date.get('year') or {}).get('value','Undated'); month=(date.get('month') or {}).get('value','01'); day=(date.get('day') or {}).get('value','01')
 authors='; '.join(plain(c['credit-name']['value']) for c in (w.get('contributors') or {}).get('contributor',[]) if c.get('credit-name'))
 records.append(dict(id='camargo-'+str(w['put-code']),title=title,authors=authors,journal=plain((w.get('journal-title') or {}).get('value','')),year=year,date=f'{year if year!="Undated" else "0000"}-{month.zfill(2)}-{day.zfill(2)}',doi=doi,url='https://doi.org/'+doi if doi else (w.get('url') or {}).get('value',''),type=w['type'],source='ORCID',_bib=plain((w.get('citation') or {}).get('citation-value','')) if (w.get('citation') or {}).get('citation-type')=='bibtex' else ''))
text=(ROOT/'working/lattes.txt').read_text(encoding='utf-8')
text=re.sub(r'10/31/26, 10:59 AM Currículo Lattes\nhttps://wwws.cnpq.br/cvlattesweb/pkg_impcv.trata \d+/15\n','',text)
section=text.split('Articles Published in Scientific Journals',1)[1].split('Presentations in Events',1)[0]
markers=list(re.finditer(r'(?:^|\n)(\d{1,2})\.\s*',section))
assert [int(m[1]) for m in markers]==list(range(1,99)), 'Expected exactly the 98 numbered Lattes articles'
matched=set();added=[];review=[]
for i,m in enumerate(markers):
 b=section[m.end():markers[i+1].start() if i+1<len(markers) else len(section)]
 info=re.search(r'\.\s*(\d{4})\.\s*\.\s*(.*?)\s*In(?=\s|[A-Z])\s*(.*?)(?:Keywords:|Knowledge areas:|Additional references:|Citações:|$)',b,re.S)
 assert info, 'Could not parse Lattes entry '+m[1]
 year,title,journal=info.groups(); title=' '.join(title.split()); authors=' '.join(b[:info.start()].strip().split()).rstrip('.')
 doi_m=re.search(r'\[doi:([^\]]+)\]',b); doi=doi_m[1].strip() if doi_m else ''
 nearest=max(records,key=lambda r:difflib.SequenceMatcher(None,clean(title),clean(r['title'])).ratio())
 score=difflib.SequenceMatcher(None,clean(title),clean(nearest['title'])).ratio()
 exact=next((r for r in records if doi and r['doi'].lower()==doi.lower()),None)
 r=exact or (nearest if score>.88 else None)
 if r:
  matched.add(r['id']); r['source']='ORCID; Lattes'
  if not r['authors']:r['authors']=authors
  review.append({'lattes_number':int(m[1]),'id':r['id'],'match':'DOI' if exact else 'title','similarity':round(score,3)})
 else:
  ident='lattes-'+m[1]; link=re.search(r'Home page:\s*\[(https?://[^\]]+)\]',b)
  r=dict(id=ident,title=title,authors=authors,journal=journal.split(', v.')[0].replace('RevistaBrasileira','Revista Brasileira').replace('ofPharmaceutical','of Pharmaceutical'),year=year,date=year+'-01-01',doi=doi,url='https://doi.org/'+doi if doi else link[1] if link else 'https://lattes.cnpq.br/4703181040916099',type='journal-article',source='Lattes',_bib='')
  added.append(r)
quarantine=[r for r in records if r['type']=='journal-article' and r['id'] not in matched]
records=[r for r in records if r['type']!='journal-article' or r['id'] in matched]+added
# BibTeX uses author metadata from Lattes if the ORCID contributor field was empty.
all_bib=[];keep=set();(ROOT/'assets/citations').mkdir(parents=True,exist_ok=True)
for r in records:
 bib=r.pop('_bib')
 def safe(s):return s.replace('\\',r'\textbackslash{}').replace('{',r'\{').replace('}',r'\}')
 if not bib:
  fields={'title':r['title'],'author':r['authors'].replace(';',' and '),'year':r['year'] if r['year']!='Undated' else '', 'journal':r['journal'],'doi':r['doi'],'url':r['url']}
  bib='@'+('article' if r['type']=='journal-article' else 'misc')+'{'+r['id']+',\n'+',\n'.join('  '+k+' = {'+safe(v)+'}' for k,v in fields.items() if v)+'\n}'
 elif r['authors'] and not re.search(r'\bauthor\s*=',bib,re.I):
  bib=re.sub(r',',lambda m:',\n  author = {'+safe(r['authors'].replace(';',' and '))+'},',bib,count=1)
 path=ROOT/'assets/citations'/(r['id']+'.bib');path.write_text(bib+'\n',encoding='utf-8');keep.add(path.name);all_bib.append(bib)
 r['bib_path']='/assets/citations/'+path.name
for p in (ROOT/'assets/citations').glob('*.bib'):
 if p.name not in keep:p.unlink()
records.sort(key=lambda r:r['date'],reverse=True)
(ROOT/'_data/publications.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'assets/publications.bib').write_text('\n\n'.join(all_bib)+'\n',encoding='utf-8')
(ROOT/'working/bibliography-reconciliation.json').write_text(json.dumps({'lattes_count':len(markers),'matched':review,'added':added,'excluded_orcid':quarantine,'total':len(records)},ensure_ascii=False,indent=2),encoding='utf-8')
print(f'{len(records)} curated records; {sum(r["type"]=="journal-article" for r in records)} journal articles; {len(quarantine)} unmatched ORCID journal records excluded.')

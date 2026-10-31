import requests,json,re
from pathlib import Path
s=requests.Session(); s.headers['Accept']='application/json'
j=json.loads(Path('working/orcid-works.json').read_text(encoding='utf-8'))
codes=[str(g['work-summary'][0]['put-code']) for g in j['group']]
works=[]
for i in range(0,len(codes),40):
 r=s.get('https://pub.orcid.org/v3.0/0000-0001-9016-222X/works/'+','.join(codes[i:i+40]),timeout=60); r.raise_for_status(); works.extend(r.json()['bulk'])
Path('working/orcid-full.json').write_text(json.dumps(works,ensure_ascii=False,indent=2),encoding='utf-8')
r=s.get('https://api.github.com/users/AdemirCamargo57/repos?per_page=100',timeout=30); r.raise_for_status(); repos=r.json(); Path('working/github-repos.json').write_text(json.dumps(repos,indent=2),encoding='utf-8')
print('Work records:',len(works)); print('Repositories:', [(x['name'], x.get('homepage')) for x in repos])
r=s.get('https://www.ademircamargo.com/',headers={'Accept':'text/html'},timeout=30); r.raise_for_status(); Path('working/old-home.html').write_text(r.text,encoding='utf-8')
urls=re.findall(r'https://static.wixstatic.com/media/[^\s"<>]+',r.text)
print('Portrait candidates:',list(dict.fromkeys(u for u in urls if 'jpg' in u))[:12])

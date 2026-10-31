from pathlib import Path
from lxml import html,etree
import re,json
root=html.fromstring('<article>'+Path('working/properties.html').read_text(encoding='utf-8')+'</article>')
parts=[('reduced-density-gradient','Reduced Density Gradient and Noncovalent Interactions',5,247,'Electron density gradients, Hessian eigenvalues, NCI plots, and interpretation of interaction patterns.',40),('hole-electron-analysis','Hole–Electron Analysis and Transition Properties',247,496,'Hole and electron distributions, transition densities, charge transfer, and spectroscopic interpretation.',50),('natural-transition-orbitals','Natural Transition Orbitals',666,959,'Constructing the transition matrix and using singular value decomposition to interpret electronic excitations.',60)]
for slug,title,start,end,desc,order in parts:
 nodes=list(root)[start:end]
 # The title is supplied by the lesson layout.
 if nodes[0].tag=='h1': nodes=nodes[1:]
 for node in nodes:
  for h in [node,*node.iterdescendants()]:
   if re.fullmatch('h[1-5]',h.tag or ''): h.tag='h'+str(min(int(h.tag[1])+1,6))
   if h.tag=='span' and h.get('class')=='math inline' and (h.text or '').startswith(r'\(\sigma_{h,x}'):
    h.set('class','math display'); h.text=r'\['+h.text[2:-2]+r'\]'
   if h.tag=='img':
    src=h.get('src','').replace('\\','/')
    h.set('src',"{{ '/"+src+"' | relative_url }}")
    image_alts={'image1.png':'Occupied wavevector states inside a spherical Fermi surface with radius k_F.', 'image2.png':'Fermi sphere centered at the origin of wavevector space with axes k_x, k_y, and k_z.', 'image3.png':'Two RDG versus sign(lambda_2) rho scatter plots at 0.01 ps and 3.15 ps; the later configuration shows more features near zero.', 'image4.png':'NCI color scale: negative sign(lambda_2) rho indicates attraction in blue, values near zero indicate weak contacts in green, and positive values indicate repulsion in red.'}
    h.set('alt',image_alts.get(src.split('/')[-1],h.get('alt') or 'Molecular analysis diagram'))
    h.set('loading','lazy')
 content='\n'.join(etree.tostring(n,encoding='unicode',method='html') for n in nodes)
 content=content.replace('{{%20', '{{ ').replace('%20|%20', ' | ').replace('%20}}', ' }}').replace(".png'%20", ".png' ")
 front='---\ntitle: '+json.dumps(title,ensure_ascii=False)+'\nsubject: Quantum chemistry\norder: '+str(order)+'\ndescription: '+json.dumps(desc)+'\nsource: CAP-VI_v2.docx\n---\n'
 Path('_lessons/'+slug+'.html').write_text(front+content+'\n',encoding='utf-8')
 print(slug,len(html.fromstring('<div>'+content+'</div>').text_content().split()), 'words including math')

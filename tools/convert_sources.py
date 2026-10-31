from pathlib import Path
import json,subprocess
root=Path(r'C:\Users\ajc\OneDrive\01_WORK\03_AULAS\APOSTILAS')
selected=[*list((root/'Site').glob('*.docx'))]
selected += [root/'01_MDEE_Chapters'/n for n in ['CAP-I_v12.docx','CAP-II_v10.docx','CAP-III_v11.docx','CAP-IV_v12.docx','CAP-V_v13.docx','CAP-VI_v2.docx']]
selected += [root/'02_QQ_Chapters'/n for n in ['QQ_CAP-I_Rev1.docx','QQ_CAP-II_Rev1.docx','QQ_CAP-III_Rev1.docx','QQ_CAP-IV_Rev1.docx','QQ_CAP-V_Rev1.docx','QQ_CAP-VI_Rev1.docx','QQ_CAP-VII_Rev1.docx']]
Path('working/converted').mkdir(exist_ok=True)
for p in selected:
 out=Path('working/converted')/(p.stem+'.md')
 r=subprocess.run(['tools/pandoc.exe',str(p),'-t','markdown','--wrap=none','--extract-media=working/converted/'+p.stem,'-o',str(out)],capture_output=True,text=True,encoding='utf-8')
 print(p.name, 'OK' if not r.returncode else r.stderr[:200])
Path('working/selected-sources.json').write_text(json.dumps([str(p) for p in selected],ensure_ascii=False,indent=2),encoding='utf-8')

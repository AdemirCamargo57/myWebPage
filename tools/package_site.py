"""Package source and a built local preview without private source documents."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
root=Path(__file__).resolve().parents[1]
out=root/'output';out.mkdir(exist_ok=True)
source_names=['_config.yml','.gitignore','Gemfile','README.md','CONTENT_STATUS.md','index.html','404.html','about.md','contact.md','group.md','research.md','publications.html','teaching.html']
source_files=[root/n for n in source_names]
for folder in ['_data','_layouts','_lessons','.github','assets']:
    source_files.extend(p for p in (root/folder).rglob('*') if p.is_file())
source_files.extend(root/'tools'/n for n in ['sync_bibliography.py','validate_site.py','package_site.py','serve.py'])
with ZipFile(out/'academic-website-source.zip','w',ZIP_DEFLATED) as z:
    for path in source_files:z.write(path,path.relative_to(root).as_posix())
with ZipFile(out/'academic-website-preview.zip','w',ZIP_DEFLATED) as z:
    for path in (root/'_site').rglob('*'):
        if path.is_file():z.write(path,path.relative_to(root).as_posix())
    z.write(root/'tools/serve.py','tools/serve.py')
    z.writestr('START-HERE.txt','Extract this archive, open a terminal in the extracted folder, and run:\n\npython tools/serve.py\n\nThen open http://127.0.0.1:8765/myWebPage/ in your browser.\nPress Ctrl+C in the terminal to stop the preview. Python 3 is required.\nMath rendering requires internet access.\nThis preview is not a complete textbook translation; see the source package CONTENT_STATUS.md.\n')
for path in out.glob('*.zip'):
    with ZipFile(path) as z:
        assert not any('Lattes.pdf' in n or n.startswith(('working/','tools/ruby')) for n in z.namelist())
    print(path.name,path.stat().st_size,'bytes')

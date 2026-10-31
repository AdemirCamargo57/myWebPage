from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlsplit
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'_site'
class Handler(SimpleHTTPRequestHandler):
 def __init__(self,*a,**kw): super().__init__(*a,directory=str(ROOT),**kw)
 def do_GET(self):
  if self.path.startswith('/myWebPage/'):
   self.path=self.path[len('/myWebPage'):]
  super().do_GET()
print('Preview: http://127.0.0.1:8765/myWebPage/',flush=True)
ThreadingHTTPServer(('127.0.0.1',8765),Handler).serve_forever()

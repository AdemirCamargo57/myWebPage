from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlsplit
from pathlib import Path
import argparse
parser=argparse.ArgumentParser(description='Preview the built academic website locally.')
parser.add_argument('--port',type=int,default=8765)
args=parser.parse_args()
ROOT=Path(__file__).resolve().parents[1]/'_site'
class Handler(SimpleHTTPRequestHandler):
 def __init__(self,*a,**kw): super().__init__(*a,directory=str(ROOT),**kw)
 def do_GET(self):
  if self.path.startswith('/myWebPage/'):
   self.path=self.path[len('/myWebPage'):]
  super().do_GET()
print(f'Preview: http://127.0.0.1:{args.port}/myWebPage/',flush=True)
ThreadingHTTPServer(('127.0.0.1',args.port),Handler).serve_forever()

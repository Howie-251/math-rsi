"""One live streaming source request, with durable progress and no duplicate request."""
from datetime import datetime,timezone
from pathlib import Path
import json,os,time,urllib.request

P=Path(__file__).resolve().parent
url='https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD5/N15_D5_100132_FINAL.edges'
assert not(P/'source100132.edges').exists()and not(P/'source100132.edges.partial').exists()
start=time.monotonic();received=0;expected=None
def progress(status,**extra):
 r={'status':status,'requested_url':url,'pid':os.getpid(),'bytes_received':received,
    'expected_bytes':expected,'elapsed_wall_seconds':time.monotonic()-start,
    'checked_UTC':datetime.now(timezone.utc).isoformat(),**extra}
 (P/'DOWNLOAD_PROGRESS.json').write_text(json.dumps(r,indent=2)+'\n')
 return r
print(json.dumps(progress('DOWNLOAD_IN_PROGRESS')),flush=True)
try:
 with urllib.request.urlopen(url,timeout=90)as response,(P/'source100132.edges.partial').open('wb')as out:
  expected=int(response.headers['Content-Length'])if response.headers.get('Content-Length')else None
  last=0
  while True:
   chunk=response.read(16384)
   if not chunk:break
   out.write(chunk);received+=len(chunk)
   if received-last>=262144:
    out.flush();print(json.dumps(progress('DOWNLOAD_IN_PROGRESS')),flush=True);last=received
  out.flush()
  receipt=progress('DOWNLOAD_COMPLETE',returned_url=response.geturl(),http_status=response.status)
 (P/'source100132.edges.partial').rename(P/'source100132.edges')
 (P/'SOURCE.json').write_text(json.dumps(receipt,indent=2)+'\n')
 print(json.dumps(receipt),flush=True)
except Exception as e:
 progress('DOWNLOAD_NOT_COMPLETE',exception_type=type(e).__name__,detail=str(e))
 raise

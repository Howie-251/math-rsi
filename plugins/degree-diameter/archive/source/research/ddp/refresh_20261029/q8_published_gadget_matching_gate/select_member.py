from pathlib import Path
from datetime import datetime,timezone
import json,struct,urllib.request,time
D=Path(__file__).resolve().parent
files=json.loads((D/'FILE_LIST.json').read_text())
f=next(x for x in files if x['name']=='data-and-verification.zip')
size=f['size'];start=size-65536;url=f['url']
rec={'started_utc':datetime.now(timezone.utc).isoformat(),'operation':'Read only ZIP tail directory; do not download full archive','url':url,'archive_size':size,'range':[start,size-1],'contents_obtained':False}
t=time.monotonic()
try:
 req=urllib.request.Request(url,headers={'Range':f'bytes={start}-{size-1}'})
 with urllib.request.urlopen(req,timeout=25) as z:
  rec.update(http_status=z.status,content_range=z.headers.get('Content-Range'))
  if z.status!=206: raise RuntimeError('Exact partial response unavailable; full archive not read')
  b=z.read(65537)
 assert len(b)==65536
 k=b.rfind(b'PK\x05\x06');assert k>=0
 eo=struct.unpack_from('<4s4H2IH',b,k)
 cdsize,cdpos=eo[5],eo[6]
 assert cdpos>=start and cdpos+cdsize<=size
 off=cdpos-start;entries=[]
 for _ in range(eo[4]):
  x=struct.unpack_from('<4s6H3I5H2I',b,off);assert x[0]==b'PK\x01\x02'
  nl,el,cl=x[10:13];name=b[off+46:off+46+nl].decode()
  entries.append({'name':name,'compressed_size':x[8],'size':x[9],'compression_method':x[4],'local_header_offset':x[16]})
  off+=46+nl+el+cl
 (D/'ARCHIVE_MEMBER_LIST.json').write_text(json.dumps(entries,indent=2)+'\n')
 rec.update(contents_obtained=True,tail_bytes=len(b),member_count=len(entries))
 print(json.dumps([e for e in entries if '1088' in e['name'] or 'witness' in e['name'] or 'verify' in e['name']],indent=2))
except Exception as e:rec.update(error_type=type(e).__name__,error=str(e))
rec['wall_seconds']=time.monotonic()-t
(D/'ARCHIVE_DIRECTORY_RECEIPT.json').write_text(json.dumps(rec,indent=2)+'\n')
print(json.dumps(rec,indent=2))

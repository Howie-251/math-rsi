from pathlib import Path
from datetime import datetime,timezone
import json,struct,urllib.request,zlib,time
D=Path(__file__).resolve().parent
files=json.loads((D/'FILE_LIST.json').read_text())
f=next(x for x in files if x['name']=='data-and-verification.zip')
e=next(x for x in json.loads((D/'ARCHIVE_MEMBER_LIST.json').read_text()) if x['name']=='witnesses/fq_d14_k3_n1088.json')
start=e['local_header_offset'];end=start+30+len(e['name'].encode())+e['compressed_size']-1
rec={'started_utc':datetime.now(timezone.utc).isoformat(),'url':f['url'],'member':e['name'],'range':[start,end],'contents_obtained':False,'main1088_member_read':False}
t=time.monotonic()
try:
 req=urllib.request.Request(f['url'],headers={'Range':f'bytes={start}-{end}'})
 with urllib.request.urlopen(req,timeout=20) as z:
  rec.update(http_status=z.status,content_range=z.headers.get('Content-Range'))
  if z.status!=206:raise RuntimeError('Exact partial response unavailable; full archive not read')
  b=z.read(end-start+2)
 assert len(b)==end-start+1
 h=struct.unpack_from('<4s5H3I2H',b,0);assert h[0]==b'PK\x03\x04'
 nl,el=h[9:11];assert el==0
 assert b[30:30+nl].decode()==e['name']
 payload=b[30+nl+el:];assert len(payload)==e['compressed_size']
 raw=zlib.decompress(payload,-15);assert len(raw)==e['size']
 obj=json.loads(raw)
 omitted=[]
 def clean(v,path=''):
  if isinstance(v,dict):
   out={}
   for k,x in v.items():
    if any(s in k.lower() for s in ('hash','sha','checksum','fingerprint')):omitted.append(path+k)
    else:out[k]=clean(x,path+k+'.')
   return out
  if isinstance(v,list):return [clean(x,path) for x in v]
  return v
 obj=clean(obj)
 (D/'PUBLISHED_WITNESS_FILTERED.json').write_text(json.dumps(obj,indent=2)+'\n')
 rec.update(contents_obtained=True,member_bytes=e['size'],transfer_bytes=len(b),omitted_nonmathematical_field_names=omitted)
 print(json.dumps(obj,indent=2))
except Exception as x:rec.update(error_type=type(x).__name__,error=str(x))
rec['wall_seconds']=time.monotonic()-t
(D/'WITNESS_EXTRACTION_RECEIPT.json').write_text(json.dumps(rec,indent=2)+'\n')
print(json.dumps(rec,indent=2))

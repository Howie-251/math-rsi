"""Exactly one newly authorized payload request for failed order110."""
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError
from datetime import datetime,timezone
import json
import os
import re
import time
import zlib

HERE=Path(__file__).resolve().parent/'selected_orders_20261028'
initial=json.loads((HERE/'INITIAL_BATCH_RECEIPT.json').read_text())
url=initial['official_archive_url']
begin,end=10181681577,10181729867
length=end-begin+1
assert length==48291 and initial['budget_charged_declared_body_bytes']+length<=8_000_000
start=time.perf_counter()
r={'status':'RUNNING_ONE_AUTHORIZED_PAYLOAD_REQUEST','url':url,'range_start':begin,
   'range_end':end,'compressed_bytes':48291,'expected_uncompressed_bytes':75000,
   'filename':'Cay4val_110.s6','request_count':1,'timeout_seconds':15,'parent_wall_seconds':25,
   'body_bytes_read_known':0,'local_header_reused':True,
   'local_header_binding':'Original successful order110 header request, validated name by original worker; no header redownload.',
   'original_receipt':'INITIAL_BATCH_RECEIPT.json','started_at_utc':datetime.now(timezone.utc).isoformat(),
   'graph_parsing':0,'BFS':0,'solver_calls':0,'CRC_or_hash_computations':0}


def save():
    (HERE/'RETRY_110_RECEIPT.json').write_text(json.dumps(r,indent=2)+'\n')


save()
try:
    req=Request(url,headers={'Range':f'bytes={begin}-{end}','Accept-Encoding':'identity',
                            'User-Agent':'Python urllib one bounded missing-member payload request'})
    try:
        response=urlopen(req,timeout=15)
    except HTTPError as exc:
        r.update(HTTP_status=exc.code,headers=dict(exc.headers.items()))
        exc.close()
        raise RuntimeError(f'HTTP {r["HTTP_status"]}; body not read')
    with response:
        r.update(HTTP_status=response.status,headers=dict(response.headers.items()),final_url=response.url)
        if response.status!=206:
            raise RuntimeError(f'HTTP {response.status}; immediately closed without reading body')
        match=re.fullmatch(r'bytes (\d+)-(\d+)/(\d+)',response.headers.get('Content-Range',''))
        assert match and tuple(map(int,match.groups()))==(begin,end,initial['archive_size_bytes'])
        compressed=response.read(length)
        r['body_bytes_read_known']=len(compressed)
        assert len(compressed)==length
    raw=zlib.decompress(compressed,-15)
    assert len(raw)==75000
    temp=HERE/'Cay4val_110.s6.part'
    temp.write_bytes(raw)
    os.replace(temp,HERE/'Cay4val_110.s6')
    r.update(status='COMPLETE_MEMBER_RETRY110',decompressed_bytes=len(raw),
             decompressed_size_matches=True,filename_order_matches_saved_header=True,
             local_path=str(HERE/'Cay4val_110.s6'))
except Exception as exc:
    r.update(status='FAILED_ONE_AUTHORIZED_RETRY_NO_MORE_REQUESTS',error=f'{type(exc).__name__}: {exc}')
finally:
    r.update(wall_seconds=time.perf_counter()-start,completed_at_utc=datetime.now(timezone.utc).isoformat())
    save()
    print(json.dumps(r,indent=2),flush=True)

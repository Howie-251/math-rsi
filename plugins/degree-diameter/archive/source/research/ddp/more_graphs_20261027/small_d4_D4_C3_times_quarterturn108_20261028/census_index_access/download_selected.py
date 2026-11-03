"""Single bounded batch: selected raw-deflate ZIP members, never the archive."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import json
import os
import re
import struct
import threading
import time
import zlib

HERE=Path(__file__).resolve().parent
OUT=HERE/'selected_orders_20261028'
OUT.mkdir(exist_ok=True)
index=json.loads((HERE/'CENTRAL_INDEX.json').read_text())
access=json.loads((HERE/'ACCESS_RESULT.json').read_text())
url=index['archive_url']
archive_bytes=access['archive_size_bytes']
selected=[row for row in index['entries'] if row['order_from_filename'] is not None
          and (42<=row['order_from_filename']<=53 or 105<=row['order_from_filename']<=161)]
selected.sort(key=lambda row:row['order_from_filename'])
assert len(selected)==69
assert sum(row['compressed_size'] for row in selected)==5743613
assert all(row['compression_method']==8 for row in selected)
start=time.perf_counter()
deadline=start+118.5
lock=threading.Lock()
charged_bytes=0
known_read_bytes=0
request_records=[]
budget=8_000_000


def write_json(name,value):
    temp=OUT/(name+'.tmp')
    temp.write_text(json.dumps(value,indent=2)+'\n')
    os.replace(temp,OUT/name)


def get_range(begin,end,order,kind):
    global charged_bytes,known_read_bytes
    length=end-begin+1
    remaining=deadline-time.perf_counter()
    if remaining<=0:
        raise TimeoutError('Batch deadline reached before request')
    record={'order':order,'kind':kind,'requested_start':begin,'requested_end':end,
            'requested_bytes':length,'body_bytes_read_known':0,'timeout_seconds':min(15,remaining)}
    with lock:
        if charged_bytes+length>budget:
            raise RuntimeError('8,000,000-byte declared-body budget would be exceeded')
        charged_bytes+=length
        request_records.append(record)
    req=Request(url,headers={'Range':f'bytes={begin}-{end}','Accept-Encoding':'identity',
                            'User-Agent':'Python urllib selected ZIP member reader'})
    try:
        response=urlopen(req,timeout=min(15,remaining))
    except HTTPError as exc:
        with lock:
            record.update(status=exc.code,headers=dict(exc.headers.items()),read_closed_without_body=True)
        exc.close()
        raise RuntimeError(f'HTTP {record["status"]}; no body read')
    with response:
        headers=dict(response.headers.items())
        with lock:
            record.update(status=response.status,final_url=response.url,headers=headers)
        if response.status!=206:
            with lock:
                record['read_closed_without_body']=True
            raise RuntimeError(f'Range ignored with HTTP {response.status}; response immediately closed')
        text=response.headers.get('Content-Range','')
        match=re.fullmatch(r'bytes (\d+)-(\d+)/(\d+)',text)
        if not match or tuple(map(int,match.groups()))!=(begin,end,archive_bytes):
            with lock:
                record['read_closed_without_body']=True
            raise RuntimeError(f'Content-Range mismatch: {text}')
        chunks=[]
        left=length
        while left:
            if time.perf_counter()>=deadline:
                raise TimeoutError('Batch deadline reached while reading body')
            chunk=response.read(min(65536,left))
            if not chunk:
                raise RuntimeError('Truncated range body')
            chunks.append(chunk)
            left-=len(chunk)
            with lock:
                known_read_bytes+=len(chunk)
                record['body_bytes_read_known']+=len(chunk)
        return b''.join(chunks)


def download(entry):
    order=entry['order_from_filename']
    offset=entry['local_header_offset']
    out=dict(entry,order=order,status='STARTED',expected_graph_count=None,
             graph_count_note='ZIP central metadata contains byte sizes, not graph counts; no graphs parsed here.')
    try:
        header=get_range(offset,offset+511,order,'local_header_first512')
        fields=struct.unpack_from('<4s5H3L2H',header)
        sig,version,flags,method,_,_,_,_,_,name_n,extra_n=fields
        assert sig==b'PK\x03\x04' and method==8 and not flags&1
        header_size=30+name_n+extra_n
        if header_size>512:
            header+=get_range(offset+512,offset+header_size-1,order,'local_header_extra')
        name=header[30:30+name_n].decode('utf-8' if flags&0x800 else 'cp437')
        assert name==entry['name']
        assert name==f'Cay4val_{order}.s6'
        payload_start=offset+header_size
        compressed=get_range(payload_start,payload_start+entry['compressed_size']-1,order,'compressed_member_payload')
        raw=zlib.decompress(compressed,-15)
        assert len(raw)==entry['uncompressed_size']
        path=OUT/name
        temp=path.with_suffix(path.suffix+'.part')
        temp.write_bytes(raw)
        os.replace(temp,path)
        out.update(status='COMPLETE_MEMBER',local_header_bytes=header_size,
                   payload_start=payload_start,payload_bytes=len(compressed),
                   decompressed_bytes=len(raw),local_filename_matches=True,
                   decompressed_size_matches=True,local_path=str(path),
                   checksums_computed=False,CRC_computed=False,graph_parsing=False)
    except Exception as exc:
        out.update(status='FAILED_MEMBER_NO_RETRY',error=f'{type(exc).__name__}: {exc}')
    return out


records={row['order_from_filename']:dict(row,order=row['order_from_filename'],status='NOT_STARTED',expected_graph_count=None)
         for row in selected}


def checkpoint(final=False):
    complete=[order for order,row in records.items() if row['status']=='COMPLETE_MEMBER']
    failed=[order for order,row in records.items() if row['status']=='FAILED_MEMBER_NO_RETRY']
    pending=[order for order,row in records.items() if row['status'] not in ('COMPLETE_MEMBER','FAILED_MEMBER_NO_RETRY')]
    with lock:
        reqs=json.loads(json.dumps(request_records))
        charged,known=charged_bytes,known_read_bytes
    status=('COMPLETE_DOWNLOAD' if len(complete)==69 else 'PARTIAL_DOWNLOAD_BATCH_CLOSED') if final else 'RUNNING_SELECTED_MEMBER_DOWNLOAD'
    value={'status':status,'official_archive_url':url,'archive_size_bytes':archive_bytes,
           'configured_total_body_budget_bytes':budget,'budget_charged_declared_body_bytes':charged,
           'network_body_bytes_read_known':known,'maximum_parallel_requests':4,
           'maximum_request_timeout_seconds':15,'overall_parent_wall_limit_seconds':120,
           'whole_archive_downloaded':False,'selected_orders_count':69,
           'completed_orders':sorted(complete),'failed_orders':sorted(failed),'pending_orders':sorted(pending),
           'member_records':[records[k] for k in sorted(records)],'requests':reqs,
           'CRC_or_hash_computations':0,'graph_parsing':0,'graph_BFS':0,'solver_calls':0,
           'expected_graph_counts':None,'graph_format':'sparse6; graph counts are not in ZIP index metadata',
           'wall_seconds':time.perf_counter()-start,'updated_at_utc':datetime.now(timezone.utc).isoformat()}
    write_json('DOWNLOAD_RECEIPT.json',value)
    write_json('terminal.json',{k:v for k,v in value.items() if k not in ('member_records','requests')})
    return value


write_json('PLAN.json',{'scope':'Exactly69 indexed members, no graph parsing/BFS/solver',
    'orders':sorted(records),'compressed_payload_bytes':5743613,'network_body_budget_bytes':budget,
    'parallel_requests':4,'request_timeout_seconds':15,'parent_wall_limit_seconds':120,
    'HTTP_rule':'206 and exact Content-Range required before any body read',
    'CRC_or_hash_computations':False,'retry_or_mirror_fallback':False})
checkpoint()
with ThreadPoolExecutor(max_workers=4) as pool:
    futures={pool.submit(download,entry):entry['order_from_filename'] for entry in selected}
    completed=0
    for future in as_completed(futures):
        order=futures[future]
        records[order]=future.result()
        completed+=1
        state=checkpoint()
        if len(state['completed_orders'])==1 or completed%10==0 or completed==69:
            print(json.dumps({'completed_members':len(state['completed_orders']),'failed_members':len(state['failed_orders']),
                              'returned_members':completed,'last_order':order,'last_status':records[order]['status'],
                              'first_complete_path':records[order].get('local_path') if len(state['completed_orders'])==1 else None,
                              'network_body_bytes_read_known':state['network_body_bytes_read_known'],
                              'wall_seconds':state['wall_seconds']}),flush=True)
final=checkpoint(final=True)
print(json.dumps({k:v for k,v in final.items() if k not in ('member_records','requests')},indent=2),flush=True)

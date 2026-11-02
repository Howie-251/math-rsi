"""Inspect only official ZIP metadata with bounded HTTP206 reads; no payload."""
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import json
import re
import struct
import time

HERE=Path(__file__).resolve().parent
receipt=json.loads((HERE/'URL_RECEIPT.json').read_text())
original_url=receipt['archive']['url']
url=original_url.replace('http://','https://',1)
budget=2_000_000
read_bytes=receipt['source_HTML_bytes_read']
requests=[]
started=time.perf_counter()


def save(name,obj):
    (HERE/name).write_text(json.dumps(obj,indent=2)+'\n')


def get_range(spec, maximum):
    global read_bytes
    record={'url':url,'Range':spec,'maximum_body_bytes':maximum,'timeout_seconds':15}
    requests.append(record)
    req=Request(url,headers={'Range':spec,'Accept-Encoding':'identity',
                            'User-Agent':'Python urllib bounded ZIP metadata reader'})
    try:
        response=urlopen(req,timeout=15)
    except HTTPError as exc:
        record.update(status=exc.code,headers=dict(exc.headers.items()),body_bytes_read=0)
        exc.close()
        raise RuntimeError(f'HTTP status {record["status"]}; stopped without reading body')
    with response:
        record.update(status=response.status,final_url=response.url,headers=dict(response.headers.items()))
        if response.status != 206:
            record['body_bytes_read']=0
            raise RuntimeError(f'Range not honored: HTTP {response.status}; closed without reading body')
        match=re.fullmatch(r'bytes (\d+)-(\d+)/(\d+)',response.headers.get('Content-Range',''))
        if not match:
            record['body_bytes_read']=0
            raise RuntimeError('206 has no usable Content-Range; closed without reading body')
        begin,end,total=map(int,match.groups())
        length=end-begin+1
        if length>maximum or read_bytes+length>budget:
            record['body_bytes_read']=0
            raise RuntimeError('Declared range exceeds this request or total byte budget')
        body=response.read(length)
        read_bytes+=len(body)
        record.update(body_bytes_read=len(body),range_start=begin,range_end=end,total_archive_bytes=total)
        if len(body)!=length:
            raise RuntimeError('Range body truncated')
        return body,begin,total


result={'status':'IN_PROGRESS','official_href':original_url,'transport_url':url,
        'transport_note':'HTTPS on the exact official hostname and path; no mirror/proxy fallback.',
        'maximum_archive_tail_bytes':131072,'maximum_central_directory_bytes':1048576,
        'total_network_read_budget_bytes':budget,'graph_payload_bytes_requested':0,
        'hashes_generated':0}
try:
    tail,tail_start,total=get_range('bytes=-131072',131072)
    pos=tail.rfind(b'PK\x05\x06')
    if pos<0 or pos+22>len(tail):
        raise RuntimeError('Ordinary ZIP EOCD not present in bounded tail')
    _,disk,cd_disk,n_disk,n_total,cd_size,cd_offset,comment_length=struct.unpack_from('<4s4H2LH',tail,pos)
    if pos+22+comment_length!=len(tail):
        raise RuntimeError('EOCD comment-length binding failed')
    zip64=any((n_total==65535,cd_size==4294967295,cd_offset==4294967295))
    if zip64:
        locator=pos-20
        if locator<0 or tail[locator:locator+4]!=b'PK\x06\x07':
            raise RuntimeError('ZIP64 locator missing in bounded tail')
        _,z_disk,z_offset,z_disks=struct.unpack_from('<4sLQL',tail,locator)
        if z_disk or z_disks!=1:
            raise RuntimeError('Multidisk ZIP64 unsupported; no further reads')
        if tail_start<=z_offset and z_offset+56<=tail_start+len(tail):
            header=tail[z_offset-tail_start:z_offset-tail_start+56]
        else:
            header,_,_=get_range(f'bytes={z_offset}-{z_offset+55}',56)
        fields=struct.unpack('<4sQ2H2L4Q',header)
        if fields[0]!=b'PK\x06\x06':
            raise RuntimeError('Invalid ZIP64 EOCD signature')
        _,z_length,_,_,disk,cd_disk,n_disk,n_total,cd_size,cd_offset=fields
        result['ZIP64_record_length']=z_length
    if disk or cd_disk or n_disk!=n_total:
        raise RuntimeError('Multidisk ZIP central directory unsupported')
    if cd_size>1048576:
        raise RuntimeError(f'Central directory {cd_size} exceeds1MiB; stopped')
    if tail_start<=cd_offset and cd_offset+cd_size<=tail_start+len(tail):
        central=tail[cd_offset-tail_start:cd_offset-tail_start+cd_size]
        reused=True
    else:
        central,_,_=get_range(f'bytes={cd_offset}-{cd_offset+cd_size-1}',1048576)
        reused=False
    entries=[]
    cur=0
    while cur<len(central):
        if cur+46>len(central):
            raise RuntimeError('Truncated central entry')
        fields=struct.unpack_from('<4s6H3L5H2L',central,cur)
        if fields[0]!=b'PK\x01\x02':
            raise RuntimeError('Unexpected central-directory signature')
        _,made,needed,flags,method,_,_,_,compressed,uncompressed,name_n,extra_n,comment_n,start_disk,_,_,offset=fields
        end=cur+46+name_n+extra_n+comment_n
        if end>len(central):
            raise RuntimeError('Central variable data truncated')
        name_data=central[cur+46:cur+46+name_n]
        name=name_data.decode('utf-8' if flags&0x800 else 'cp437')
        extra=central[cur+46+name_n:cur+46+name_n+extra_n]
        ep=0
        while ep+4<=len(extra):
            kind,n=struct.unpack_from('<HH',extra,ep)
            value=extra[ep+4:ep+4+n]
            ep+=4+n
            if kind==1:
                vp=0
                if uncompressed==4294967295:
                    uncompressed=struct.unpack_from('<Q',value,vp)[0];vp+=8
                if compressed==4294967295:
                    compressed=struct.unpack_from('<Q',value,vp)[0];vp+=8
                if offset==4294967295:
                    offset=struct.unpack_from('<Q',value,vp)[0];vp+=8
                if start_disk==65535:
                    start_disk=struct.unpack_from('<L',value,vp)[0]
        if start_disk:
            raise RuntimeError('Nonzero entry disk; stopped')
        stem=Path(name).stem
        numbers=re.findall(r'\d+',stem)
        order=int(numbers[-1]) if numbers and not name.endswith('/') else None
        entries.append({'name':name,'order_from_filename':order,'compressed_size':compressed,
                        'uncompressed_size':uncompressed,'local_header_offset':offset,
                        'compression_method':method,'general_purpose_flags':flags,
                        'directory_entry':name.endswith('/')})
        cur=end
    if len(entries)!=n_total:
        raise RuntimeError(f'Entry count mismatch {len(entries)} vs {n_total}')
    orders=[e['order_from_filename'] for e in entries if not e['directory_entry']]
    binding=len(orders)==1021 and sorted(orders)==list(range(5,1026))
    result.update(status='COMPLETE_CENTRAL_INDEX_NO_GRAPH_PAYLOAD',archive_size_bytes=total,
                  ZIP64=zip64,central_directory_offset=cd_offset,central_directory_bytes=cd_size,
                  central_directory_reused_from_tail=reused,entry_count=len(entries),
                  filename_order_binding='EXACT_ONE_FILE_PER_ORDER5_TO1025' if binding else 'NEEDS_MANUAL_FILENAME_REVIEW')
    save('CENTRAL_INDEX.json',{'archive_url':url,'entries':entries,'filename_order_binding':result['filename_order_binding']})
    if binding:
        totals={}
        for lo,hi in [(42,53),(105,161)]:
            selected=[e for e in entries if e['order_from_filename'] is not None and lo<=e['order_from_filename']<=hi]
            totals[f'{lo}..{hi}']={'file_count':len(selected),'compressed_bytes':sum(e['compressed_size'] for e in selected),
                                 'uncompressed_bytes':sum(e['uncompressed_size'] for e in selected),
                                 'all_compression_methods':sorted({e['compression_method'] for e in selected}),
                                 'entries':selected}
        result['relevant_order_totals']=totals
except Exception as exc:
    result.update(status='INDEX_ACCESS_GAP_STOPPED',error=f'{type(exc).__name__}: {exc}')
finally:
    result.update(total_network_body_bytes_read=read_bytes,archive_body_bytes_read=read_bytes-receipt['source_HTML_bytes_read'],
                  requests=requests,wall_seconds=time.perf_counter()-started,
                  completed_at_utc=datetime.now(timezone.utc).isoformat(),no_graph_payload_download=True,
                  graph_BFS=0,solver_calls=0,graph_searches=0)
    save('ACCESS_RESULT.json',result)
    print(json.dumps({k:v for k,v in result.items() if k not in ('requests','relevant_order_totals')},indent=2))
    if 'relevant_order_totals' in result:
        print(json.dumps({k:{x:y for x,y in v.items() if x!='entries'} for k,v in result['relevant_order_totals'].items()},indent=2))

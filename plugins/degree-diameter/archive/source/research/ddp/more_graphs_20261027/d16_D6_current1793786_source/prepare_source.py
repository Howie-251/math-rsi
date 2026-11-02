import json
import lzma
import pathlib
import shutil
import time
import urllib.request

D = pathlib.Path(__file__).resolve().parent
URL = 'https://zenodo.org/api/records/23691325/files/deg16_diam6_n1793786.txt.xz/content'
archive = D/'source1793786.author.adjlist.txt.xz'
literal = D/'source1793786.author.adjlist.txt'
start = time.monotonic()
cpu = time.process_time()
(D/'checkpoint.json').write_text(json.dumps({'status':'DOWNLOADING_EXACT_CURRENT1793786_SOURCE','URL':URL},indent=2)+'\n')
if archive.exists():
    receipt = dict(status='REUSED_EXISTING_EXACT_LOCAL_ARCHIVE',URL=URL,bytes=archive.stat().st_size)
else:
    request = urllib.request.Request(URL,headers={'User-Agent':'degree-diameter-source-research'})
    try:
        with urllib.request.urlopen(request,timeout=90) as response, (D/'source1793786.download').open('wb') as out:
            receipt = dict(status=response.status,URL=URL,returned_URL=response.geturl(),content_type=response.headers.get('Content-Type'))
            downloaded = 0
            while chunk := response.read(1024*1024):
                out.write(chunk)
                downloaded += len(chunk)
                (D/'checkpoint.json').write_text(json.dumps({'status':'DOWNLOADING_EXACT_CURRENT1793786_SOURCE','bytes_received':downloaded,'URL':URL},indent=2)+'\n')
        (D/'source1793786.download').rename(archive)
        receipt['bytes'] = archive.stat().st_size
    except Exception as error:
        receipt = dict(status='EXACT_PRIMARY_SOURCE_DOWNLOAD_FAILED',URL=URL,error=str(error))
        (D/'SOURCE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
        (D/'checkpoint.json').write_text(json.dumps({'status':receipt['status'],'running':False},indent=2)+'\n')
        raise
receipt['download_wall_seconds'] = time.monotonic()-start
receipt['download_CPU_seconds'] = time.process_time()-cpu
assert receipt['bytes']==52392708
decomp_start=time.process_time()
if not literal.exists():
    (D/'checkpoint.json').write_text(json.dumps({'status':'DECOMPRESSING_EXACT_ARCHIVE','archive_bytes':receipt['bytes']},indent=2)+'\n')
    with lzma.open(archive,'rb') as inp, literal.open('wb') as out:
        shutil.copyfileobj(inp,out)
receipt.update(decompressed_bytes=literal.stat().st_size,decompression_CPU_seconds=time.process_time()-decomp_start,literal_file=literal.name,source_claimed_n=1793786,source_reported_D=6,profile_not_yet_run=True)
(D/'SOURCE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
(D/'checkpoint.json').write_text(json.dumps({'status':'EXACT_CURRENT_LITERAL_READY_FOR_PROFILE','literal':literal.name,'running':False},indent=2)+'\n')
print(json.dumps(receipt))

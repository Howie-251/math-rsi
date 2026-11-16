"""Bind current42402, build all R4 providers, independently check three balls."""
from pathlib import Path
from collections import deque,Counter
import array,csv,json,resource,subprocess,sys,time

HERE=Path(__file__).resolve().parent
ROOT=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
BINDING=json.loads((HERE.parent/'SOURCE_BINDING.json').read_text())
SOURCE=ROOT/BINDING['source_file']
start=time.process_time();before=resource.getrusage(resource.RUSAGE_CHILDREN)
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'prepare.cpp'),'-o',str(HERE/'prepare')],check=True)
subprocess.run([str(HERE/'prepare'),str(SOURCE),str(HERE)],check=True)

# Independent Python controls use the original edge text, not the new CSR.
with SOURCE.open() as stream:
    n,m=map(int,next(stream).split());adj=[[] for _ in range(n)]
    for line in stream:
        a,b=map(int,line.split());adj[a].append(b);adj[b].append(a)
assert (n,m)==(42402,245937) and sum(map(len,adj))==2*m
free=[v for v,row in enumerate(adj) if len(row)<12]
stored=array.array('I');stored.frombytes((HERE/'FREE_IDS.u32le.bin').read_bytes())
if sys.byteorder!='little':stored.byteswap()
assert free==list(stored) and len(free)==13857
assert bytes(map(len,adj))==(HERE/'DEGREES.u8.bin').read_bytes()
stats={int(row['provider_id']):row for row in csv.DictReader((HERE/'PROVIDER_STATS.csv').open())}
meta=json.loads((HERE/'PROVIDERS_META.json').read_text());rowbytes=meta['provider_row_bytes']
controls=[]
with (HERE/'PERIPHERY_R4_FREE.u64le.bin').open('rb') as providers:
    for root in [41356,41879,42401]:
        distance={root:0};queue=deque([root])
        while queue:
            v=queue.popleft()
            if distance[v]==4:continue
            for w in adj[v]:
                if w not in distance:distance[w]=distance[v]+1;queue.append(w)
        providers.seek((root-41356)*rowbytes);row=providers.read(rowbytes)
        expected=bytearray(rowbytes)
        covered=0
        for index,v in enumerate(free):
            if v in distance:expected[index//8]|=1<<(index%8);covered+=1
        assert row==bytes(expected)
        spheres=Counter(distance.values());native=stats[root]
        assert int(native['ball4_size'])==len(distance) and int(native['covered_free'])==covered
        assert [int(native[f'sphere{i}']) for i in range(5)]==[spheres[i] for i in range(5)]
        controls.append({'root':root,'ball4_size':len(distance),'spheres':[spheres[i] for i in range(5)],'covered_free':covered,'all13857_provider_bits_match':True})
after=resource.getrusage(resource.RUSAGE_CHILDREN)
receipt={'status':'COMPLETE_WITH_THREE_INDEPENDENT_RAW_EDGE_BALL_CONTROLS','source_file':str(SOURCE),
         'source_n':n,'source_m':m,'free_count':len(free),'provider_rows_complete':1046,
         'source_CSR_current_n':42402,'stale42398_cache_used':False,'controls':controls,
         'compile_native_and_Python_control_CPU':after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime+time.process_time()-start,
         'solver_calls':0,'shared_STATE_modified':False}
(HERE/'PREP_RESULT.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt),flush=True)

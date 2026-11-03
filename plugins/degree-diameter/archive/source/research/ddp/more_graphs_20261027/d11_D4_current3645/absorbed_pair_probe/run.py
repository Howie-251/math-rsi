"""Execute only the scout-frozen absorbed-pair batch."""
from array import array
from pathlib import Path
import json,resource,subprocess,time

P=Path(__file__).resolve().parent
ROOT=P.parents[4]
START=time.process_time()
CHILD=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-START+c.ru_utime+c.ru_stime-CHILD.ru_utime-CHILD.ru_stime
def save(name,data):
    (P/name).write_text(json.dumps(data,indent=2)+'\n')

assert json.loads((P/'PREDICTION.json').read_text())['status']=='FROZEN_BEFORE_CANDIDATE_RADIUS_PREPARATION'
assert not(P/'RESULT.json').exists()
frozen=json.loads((P/'frozen.json').read_text())
assert frozen['candidate_count']==len(frozen['records'])<=3280
source=Path(frozen['source_file'])
cache=json.loads((P/'FREE_R3_CACHE.json').read_text())
assert cache['source_n']==3645 and cache['covered_count']==2902 and cache['new_BFS_runs']==0
words=array('Q',map(int,cache['covered_words_u64']))
assert len(words)==57
(P/'free_R3.u64le.bin').write_bytes(words.tobytes())
with(P/'candidates.txt').open('w')as out:
    out.write(str(len(frozen['records']))+'\n')
    out.write(' '.join(map(str,frozen['free_ports']))+'\n')
    for record in frozen['records']:
        types=[{'T':0,'L':1}[t]for t in record['host_types']]
        values=[record['ordinal'],record['point_p'],*types,
                *[v for edge in record['deleted_edges']for v in edge],
                *record['endpoint_set'],*record['new_neighbors'],
                len(record['affected_roots']),*record['affected_roots']]
        out.write(' '.join(map(str,values))+'\n')
subprocess.run(['g++','-O3','-march=native','-std=c++17',str(P/'probe.cpp'),'-o',str(P/'probe')],check=True)
compile_cpu=cpu()
remaining=29.5-compile_cpu
assert remaining>1
with(P/'native.log').open('w')as log:
    ret=subprocess.run([str(P/'probe'),str(source),str(P/'candidates.txt'),str(P),str(remaining)],stdout=log,stderr=subprocess.STDOUT,timeout=45)
r=json.loads((P/'NATIVE_RESULT.json').read_text())if(P/'NATIVE_RESULT.json').exists()else{'status':'NATIVE_INCOMPLETE_OUTPUT','candidates_screened':0,'candidates_closed':0}
hit=bool(r.get('hit'))
if hit:
    item=json.loads((P/'first_hit.json').read_text())
    original=frozen['records'][item['ordinal']]
    assert original['ordinal']==item['ordinal'] and original['new_neighbors']==item['full_neighbor_set']
    item.update(graph_file=str((P/'graph_d11_D4_n3646.edges').relative_to(ROOT)),
                source_file=str(source.relative_to(ROOT)),source_D4_inherited=True,
                host_types=original['host_types'],hosts=original['hosts'],
                used_in_author_chain=original['used_in_author_chain'],
                parent_independent_pending=True,producer_D_at_most=4,Moore_D3_bound=1222)
    save('first_hit.json',item)
r.update(compile_CPU_seconds=compile_cpu,total_process_and_children_CPU_seconds=cpu(),CPU_budget_seconds=30,
         returncode=ret.returncode,target_Delta=11,target_D=4,public_savedL=3645,hypothetical_n=3646,
         actual_success_n=3646 if hit else None,actual_success_m=20053 if hit else None,
         producer_D_at_most=4 if hit else None,ordinary_bad_unordered_pairs=None,
         graphs_exported=int(hit),source_allBFS_revalidation=0,
         candidates_unattempted=len(frozen['records'])-r.get('candidates_screened',0),
         candidates_unresolved=r.get('candidates_screened',0)-r.get('candidates_closed',0),
         prediction_verdict='SUPPORTED_PRODUCER_ROOT_PENDING'if hit else'REFUTED'if r['status']=='COMPLETE_FROZEN_FAMILY_NO_HIT'else'UNRESOLVED',
         parent_independent_pending=hit,pending=['Root independentfirstmechanism full3646-rootBFS']if hit else[])
save('RESULT.json',r)
save('terminal.json',{**r,'running':False})
print(json.dumps({k:v for k,v in r.items()if k!='rows'},indent=2))

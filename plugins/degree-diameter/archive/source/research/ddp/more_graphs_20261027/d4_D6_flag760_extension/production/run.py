"""Execute only the source-bound45568 flag/layer pairs."""
from pathlib import Path
import json,resource,subprocess,time
P=Path(__file__).resolve().parent
ROOT=P.parents[4]
START=time.process_time()
CHILD=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-START+r.ru_utime+r.ru_stime-CHILD.ru_utime-CHILD.ru_stime
def save(name,data):
    (P/name).write_text(json.dumps(data,indent=2)+'\n')

assert json.loads((P/'PREDICTION.json').read_text())['status']=='FROZEN_BEFORE_ENDPOINT_RADIUS_OR_CANDIDATE_QUERY'
assert not(P/'RESULT.json').exists()
frozen=json.loads((P.parent/'frozen.json').read_text())
assert (frozen['source_n'],frozen['source_m'],frozen['candidate_count'])==(760,1520,45568)
with(P/'candidates.txt').open('w')as out:
    out.write('45568\n')
    for row in frozen['records']:
        values=[row['ordinal'],row['base_edge_index'],row['layer_edge_index'],
                *[v for edge in row['deleted_edges']for v in edge],*row['new_neighbors']]
        out.write(' '.join(map(str,values))+'\n')
subprocess.run(['g++','-O3','-march=native','-std=c++17',str(P/'probe.cpp'),'-o',str(P/'probe')],check=True)
compiled=cpu()
remaining=19.5-compiled
assert remaining>0.5
with(P/'native.log').open('w')as log:
    answer=subprocess.run([str(P/'probe'),frozen['source_file'],str(P/'candidates.txt'),str(P),str(remaining)],stdout=log,stderr=subprocess.STDOUT,timeout=30)
r=json.loads((P/'NATIVE_RESULT.json').read_text())if(P/'NATIVE_RESULT.json').exists()else{'status':'NATIVE_INCOMPLETE_OUTPUT','candidates_total':45568,'candidates_screened':0,'candidates_closed':0}
hit=bool(r.get('hit'))
if hit:
    item=json.loads((P/'first_hit.json').read_text())
    original=next(v for v in frozen['records']if v['ordinal']==item['ordinal'])
    assert original['new_neighbors']==item['full_neighbor_set']and original['deleted_edges']==item['deleted_edges']
    item.update(graph_file=str((P/'graph_d4_D6_n761.edges').relative_to(ROOT)),
                source_file=str(Path(frozen['source_file']).resolve().relative_to(ROOT)),
                source_D6_inherited=True,source_actual_layer_cycles=[8,8,16],
                producer_D_at_most=6,Moore_D5_bound=485,parent_independent_pending=True)
    save('first_hit.json',item)
r.update(compile_and_input_CPU_seconds=compiled,total_process_and_children_CPU_seconds=cpu(),CPU_budget_seconds=20,
         returncode=answer.returncode,target_Delta=4,target_D=6,public_savedL=760,hypothetical_n=761,hypothetical_m=1522,
         actual_success_n=761 if hit else None,actual_success_m=1522 if hit else None,
         producer_D_at_most=6 if hit else None,ordinary_bad_unordered_pairs=None,graphs_exported=int(hit),
         oldsource_allBFS_revalidation=0,geometry_reconstruction_repeated=False,
         candidates_unattempted=r['candidates_total']-r['candidates_screened'],
         candidates_unresolved=r['candidates_screened']-r['candidates_closed'],
         prediction_verdict='SUPPORTED_PRODUCER_PENDING_ROOT'if hit else'REFUTED'if r['status']=='COMPLETE_FROZEN_FLAG_LAYER_FAMILY_NO_HIT'else'UNRESOLVED',
         parent_independent_pending=hit,pending=['Root independentcomplete761-rootBFS']if hit else[])
save('RESULT.json',r)
save('terminal.json',{**r,'running':False})
print(json.dumps({k:v for k,v in r.items()if k!='rows'},indent=2))

"""One original-witness paired-switch slice; no parent-family rerun."""
from pathlib import Path
import json,resource,subprocess,time

P=Path(__file__).resolve().parent
ROOT=P.parents[4]
OLD=P.parent/'absorbed_pair_probe'
START=time.process_time()
CHILD=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-START+c.ru_utime+c.ru_stime-CHILD.ru_utime-CHILD.ru_stime
def save(name,value):
    (P/name).write_text(json.dumps(value,indent=2)+'\n')

assert json.loads((P/'PREDICTION.json').read_text())['status']=='FROZEN_BEFORE_SWITCH_GROUP_OR_RADIUS_QUERY'
assert not(P/'RESULT.json').exists()
prior=json.loads((OLD/'RESULT.json').read_text())
frozen=json.loads((OLD/'frozen.json').read_text())
byordinal={r['ordinal']:r for r in frozen['records']}
records=sorted((r for r in prior['rows']if r['status']=='OLDPAIR_D4_FAIL'and r['source_R3_missing']==0),key=lambda r:r['ordinal'])
assert len(records)==47
cache=json.loads((OLD/'ENDPOINT_CACHE.json').read_text())
assert cache['complete']and cache['roots_prepared']==len(cache['roots'])==1964
(P/'old_roots.txt').write_text('\n'.join(map(str,cache['roots']))+'\n')
with(P/'original47.txt').open('w')as out:
    out.write('47\n'+' '.join(map(str,frozen['free_ports']))+'\n')
    for record in records:
        item=byordinal[record['ordinal']]
        values=[record['ordinal'],item['point_p'],record['first_bad_root'],record['first_bad_target'],
                *[v for edge in item['deleted_edges']for v in edge],*item['new_neighbors']]
        out.write(' '.join(map(str,values))+'\n')
subprocess.run(['g++','-O3','-march=native','-std=c++17',str(P/'probe.cpp'),'-o',str(P/'probe')],check=True)
compiled=cpu()
remaining=7.5-compiled
assert remaining>0.3
with(P/'native.log').open('w')as log:
    answer=subprocess.run([str(P/'probe'),frozen['source_file'],str(P/'original47.txt'),str(OLD),str(P),str(remaining)],stdout=log,stderr=subprocess.STDOUT,timeout=15)
r=json.loads((P/'NATIVE_RESULT.json').read_text())if(P/'NATIVE_RESULT.json').exists()else{'status':'NATIVE_INCOMPLETE_OUTPUT','candidates_total':0,'candidates_screened':0,'candidates_closed':0}
hit=bool(r.get('hit'))
if hit:
    item=json.loads((P/'first_hit.json').read_text())
    item.update(graph_file=str((P/'graph_d11_D4_n3646.edges').relative_to(ROOT)),
                source_file=str(Path(frozen['source_file']).relative_to(ROOT)),
                first_stage_original_frozen_record=byordinal[item['original_ordinal']],
                producer_D_at_most=4,Moore_D3_bound=1222,parent_independent_pending=True)
    save('first_hit.json',item)
r.update(compile_CPU_seconds=compiled,total_process_and_children_CPU_seconds=cpu(),CPU_budget_seconds=8,
         returncode=answer.returncode,source_n=3645,source_m=20044,target_Delta=11,target_D=4,public_savedL=3645,
         hypothetical_n=3646,hypothetical_m=20052,actual_success_n=3646 if hit else None,
         actual_success_m=20052 if hit else None,producer_D_at_most=4 if hit else None,
         ordinary_bad_unordered_pairs=None,graphs_exported=int(hit),oldsource_allBFS_revalidation=0,
         previous2673_candidates_retested=0,
         candidates_unattempted=r['candidates_total']-r['candidates_screened'],
         candidates_unresolved=r['candidates_screened']-r['candidates_closed'],
         prediction_verdict='SUPPORTED_PRODUCER_PENDING_ROOT'if hit else'REFUTED'if r['status']=='COMPLETE_SINGLE_SWITCH_CLASS_NO_HIT'else'UNRESOLVED',
         parent_independent_pending=hit,pending=['Root independentcomplete3646-rootBFS']if hit else[])
save('RESULT.json',r)
save('terminal.json',{**r,'running':False})
print(json.dumps({k:v for k,v in r.items()if k!='rows'},indent=2))

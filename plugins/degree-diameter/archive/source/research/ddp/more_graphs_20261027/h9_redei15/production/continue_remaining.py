"""One pass of original untested ordinals2..84 after accepted Redei42399."""
from pathlib import Path
from collections import Counter
import json
import resource
import subprocess
import time

PROD=Path(__file__).resolve().parent
OUT=PROD/'continuation'
GROUP=PROD.parent
ROOT=PROD.parents[4]
INITIAL_SELF=time.process_time()
INITIAL_CHILD=resource.getrusage(resource.RUSAGE_CHILDREN)
BUDGET=120.0
load=lambda p:json.loads(p.read_text())


def cpu():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-INITIAL_SELF+c.ru_utime+c.ru_stime-INITIAL_CHILD.ru_utime-INITIAL_CHILD.ru_stime


def save(name,d):
    (OUT/name).write_text(json.dumps(d,indent=2)+'\n')


def rel(p):return str(p.relative_to(ROOT))


def write_graph(path,n,m,edge_lines,new_vertex,neighbors):
    with path.open('w') as f:
        f.write(f'{n} {m}\n');f.write(edge_lines)
        if edge_lines and not edge_lines.endswith('\n'):f.write('\n')
        for v in neighbors:f.write(f'{v} {new_vertex}\n')


def main():
    prediction=load(OUT/'PREDICTION.json');assert prediction['frozen_before_continuation']
    assert not (OUT/'RESULT.json').exists(),'Continuation already terminal'
    source=ROOT/prediction['source'];current_file=source
    with source.open() as f:
        n,m=map(int,f.readline().split());edge_lines=f.read()
    assert (n,m)==(42399,245901)
    old_degrees=[0]*n
    for line in edge_lines.splitlines():
        u,v=map(int,line.split());old_degrees[u]+=1;old_degrees[v]+=1
    initial_n=n;initial_m=m
    original=load(PROD/'frozen_items.json');assert len(original)==85
    assert original[0]['pool_index']==7 and original[1]['pool_index']==8
    frozen=original[2:];assert len(frozen)==83 and [r['ordinal'] for r in frozen]==list(range(2,85))
    assert all(r['degree']==12 for r in frozen)
    save('frozen_items.json',frozen)
    pool=load(GROUP/'pool/pool12.json');assert (pool['source_n'],pool['source_m'])==(42398,245889)
    (OUT/'items').mkdir(exist_ok=True);(OUT/'graphs').mkdir(exist_ok=True)
    rows=[];accepted=[];native_calls=0;mandatory_calls=0;profile=None;status='ALL83_ORIGINAL_UNTESTED_ITEMS_TERMINAL'

    def persist_sequence():
        sequence=dict(initial_n=initial_n,initial_m=initial_m,final_n=n,final_m=m,records=accepted,
                      initial_source=rel(source),final_graph=rel(current_file),degree=12,
                      neighbor_type='Folded Redei15 projectiveblocking set plus permitted oldanchors')
        save('accepted_sequence.json',sequence)
        first=load(PROD/'first_hit.json')
        (PROD/'accepted_sequence.json').write_text(json.dumps(dict(initial_n=42398,initial_m=245889,final_n=n,final_m=m,
            records=[first]+accepted,source_graph=first['source_graph'],final_graph=rel(current_file),
            first_newmechanism_acceptance=prediction['source_acceptance']),indent=2)+'\n')

    print('FROZEN_REMAINING '+json.dumps(dict(items=len(frozen),ordinals=[2,84],source_n=n,source_m=m,CPU=cpu())),flush=True)
    for item in frozen:
        pins=item['mandatory_pins'];cap=item['anchor_cap'];assert cap==12-len(pins) and 0<=cap<=2
        row=dict(item,source_n=n,source_m=m,source_graph=rel(current_file),
                 prior_accepted_continuation_pool_indices=[r['pool_index'] for r in accepted])
        blocked=[v for v in pins if old_degrees[v]>=12]
        if blocked:
            row.update(status='CURRENT_DEGREE_BLOCKED',blocked_pins=blocked);rows.append(row);continue
        if BUDGET-cpu()<8.0:status='TOTAL_CPU_RESERVE_STOP';break
        prefix=OUT/'items'/f'ord{item["ordinal"]:03d}_pool{item["pool_index"]}_n{n}'
        pf=Path(str(prefix)+'.pins.txt');pf.write_text(' '.join(map(str,pins))+'\n')
        mode='prepare' if cap else 'verify'
        with Path(str(prefix)+'.log').open('w') as log:
            ret=subprocess.run([str(PROD/'cover'),mode,str(current_file),str(pf),str(prefix),'12'],stdout=log,stderr=log)
        native_calls+=1;mandatory_calls+=1
        if ret.returncode:
            row.update(status='UNKNOWN_NATIVE_PROCESS_LIMIT',returncode=ret.returncode);rows.append(row);continue
        check=load(Path(str(prefix)+'.json'))
        row.update(mandatory_R4_file=rel(Path(str(prefix)+'.json')),native_CPU_seconds=check['CPU_seconds'])
        if check['status']=='DEGREE_INFEASIBLE':
            row.update(status='CURRENT_DEGREE_BLOCKED_NATIVE',blocked_pins=check['blocked']);rows.append(row);continue
        assert (check['source_n'],check['source_m'])==(n,m) and check['pins']==pins
        missing=check['missing'];core_missing=[v for v in missing if v<41356]
        row.update(mandatory_R4_missing=len(missing),core_R4_missing_count=len(core_missing),extra_R4_missing_count=len(missing)-len(core_missing))
        if core_missing:
            row.update(status='PCORE_COUNTEREXAMPLE_STOP',missing_core_vertices=core_missing,
                       pool_witness=pool['records'][item['pool_record_index']])
            rows.append(row);save('Pcore_counterexample.json',row);status='PCORE_COUNTEREXAMPLE_STOP';break
        anchors=[] if not missing else None
        if missing:
            if cap==0:row['status']='EXACT_CAP0_EXTRAS_MISSING'
            elif check.get('exact_one_or_two_found'):
                found=check['exact_anchors']
                if len(found)<=cap:anchors=found
                else:row['status']='EXACT_NO_ONE_ANCHOR'
            elif cap==1:row['status']='EXACT_NO_ONE_ANCHOR'
            else:row['status']='EXACT_NO_AT_MOST_TWO_ANCHORS' if check.get('exact_two_complete') else 'UNKNOWN_NATIVE_EXACT_TWO_LIMIT'
        if profile is None and mandatory_calls>=5:
            profile=dict(mandatory_calls=mandatory_calls,rows_visited=len(rows)+1,accepted_so_far=len(accepted),CPU=cpu(),
                         estimated_all83_CPU=cpu()*len(frozen)/max(1,len(rows)+1))
            save('first5_profile.json',profile);print('PROFILE '+json.dumps(profile),flush=True)
        if anchors is None:rows.append(row);continue
        neighbors=sorted(pins+anchors)
        assert len(neighbors)==len(set(neighbors))<=12 and all(old_degrees[v]<12 for v in neighbors)
        selected_path=Path(str(prefix)+'.json');good=check
        if anchors:
            pf.write_text(' '.join(map(str,neighbors))+'\n');selected=Path(str(prefix)+'_selected')
            with Path(str(selected)+'.log').open('w') as log:
                ret=subprocess.run([str(PROD/'cover'),'verify',str(current_file),str(pf),str(selected),'12'],stdout=log,stderr=log)
            native_calls+=1;assert ret.returncode==0
            selected_path=Path(str(selected)+'.json');good=load(selected_path)
        assert good['missing_count']==0 and good['covered_count']==n and max(good['pin_current_degrees'])<12
        new_vertex=n;new_m=m+len(neighbors);new_n=n+1
        graph=OUT/'graphs'/f'graph_d12_D5_n{new_n}.edges'
        write_graph(graph,new_n,new_m,edge_lines,new_vertex,neighbors)
        row.update(status='ACCEPTED_COMPLETE_CURRENT_R4_EXTENSION',new_vertex=new_vertex,new_n=new_n,new_m=new_m,
            new_vertex_degree=len(neighbors),full_neighbor_set=neighbors,anchors=anchors,
            neighbors_old_degrees=good['pin_current_degrees'],actual_current_R4_missing=0,actual_current_R4_covered=n,
            actual_selected_R4_file=rel(selected_path),graph_file=rel(graph),source_edges_retained=True,
            pool_file=rel(GROUP/'pool/pool12.json'),pool_witness=pool['records'][item['pool_record_index']],
            new_neighbor_type='Folded Redei15 projectiveblocking set plus permitted oldanchors')
        for v in neighbors:old_degrees[v]+=1
        old_degrees.append(len(neighbors))
        edge_lines+=''.join(f'{v} {new_vertex}\n' for v in neighbors)
        n,m=new_n,new_m;current_file=graph;rows.append(row);accepted.append(row);persist_sequence()
        save(f'accepted_{len(accepted):02d}.json',row)
        print('HIT '+json.dumps(dict(continuation_count=len(accepted),pool_index=item['pool_index'],new_n=n,new_m=m,anchors=anchors,CPU=cpu())),flush=True)
    persist_sequence()
    result=dict(status=status,initial_n=initial_n,initial_m=initial_m,final_n=n,final_m=m,
        original_unattempted_scope=83,rows_visited=len(rows),items_unattempted=83-len(rows),rows=rows,
        accepted_extensions=len(accepted),records=accepted,final_graph=rel(current_file),
        native_calls=native_calls,mandatory_calls=mandatory_calls,CPU_parent_plus_all_children_seconds=cpu(),
        row_status_counts=dict(Counter(r['status'] for r in rows)),core_counterexample=status=='PCORE_COUNTEREXAMPLE_STOP',
        currentbase_changes_handled_by_fresh_degree_and_R4=True,prior_pool7_failure_not_retried=True,
        old_source_BFS=0,all_source_BFS=0,per_step_independent_review=0,external_review=0,Lean=0,MIP=0,
        shared_delivery_modified=False,pending=[])
    save('RESULT.json',result);save('terminal.json',{k:v for k,v in result.items() if k not in ['rows','records']})
    report=(f'# Redei15 original remaining83 continuation\n\n{status}. Source42399/245901; final{n}/{m}. '
        f'Visited{len(rows)}/83; unattempted{83-len(rows)}; complete accepted extensions{len(accepted)}. '
        f'Parent+allnative CPU{cpu():.6f}s. Each accepted step retained all old edges and passed actualdegree plus complete current-source selectedR4. '
        'Every executed mandatory set had zero missing core vertices. Failed items were not retried on later bases. '
        'No per-step root review, old-source/all-source BFS, MIP, external review, shared family or Wiki edit.\n\n'
        'Literal steps and complete geometry witnesses: accepted_sequence.json. The parent production/accepted_sequence.json also includes the initial root-accepted42399 step. '
        'Finite failures retain their evaluation source_n and do not exclude a later changed base.\n')
    (OUT/'REPORT.md').write_text(report)
    print('TERMINAL '+json.dumps({k:v for k,v in result.items() if k not in ['rows','records']}),flush=True)


if __name__=='__main__':main()

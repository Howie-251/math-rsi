"""First complete Redei15 extension only; fresh exact current-base coverage."""
from pathlib import Path
from collections import Counter
import json
import resource
import subprocess
import time

OUT=Path(__file__).resolve().parent
GROUP=OUT.parent
BASE=OUT.parents[1]
ROOT=OUT.parents[4]
BUDGET=120.0
INITIAL_CHILD=resource.getrusage(resource.RUSAGE_CHILDREN)
INITIAL_SELF=time.process_time()
load=lambda p:json.loads(p.read_text())


def cpu():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-INITIAL_SELF+c.ru_utime+c.ru_stime-INITIAL_CHILD.ru_utime-INITIAL_CHILD.ru_stime


def save(name,value):
    (OUT/name).write_text(json.dumps(value,indent=2)+'\n')


def relative(p):
    return str(p.relative_to(ROOT))


def compile_native():
    original=(BASE/'h9_d12_eightpin_extensions/cover.cpp').read_text()
    replacements={
        'assert(argc==5);':'assert(argc==6);int DEG=stoi(argv[5]);assert(DEG==11||DEG==12);',
        'pins.size()<=12':'pins.size()<=size_t(DEG)',
        'g[p].size()>=12':'g[p].size()>=size_t(DEG)',
        'g[u].size()<12':'g[u].size()<size_t(DEG)',
        'bool found=false,exacttwo=true;':'bool found=false,exacttwo=(DEG-int(pins.size())>=2);',
        'if(!found&&zeroTargets.empty()){':'if(!found&&zeroTargets.empty()&&DEG-int(pins.size())>=2){',
    }
    for old,new in replacements.items():
        assert original.count(old)==1,(old,original.count(old))
        original=original.replace(old,new)
    (OUT/'cover.cpp').write_text(original)
    started=cpu()
    subprocess.run(['g++','-O3','-std=c++17',str(OUT/'cover.cpp'),'-o',str(OUT/'cover')],check=True)
    return cpu()-started


def read_base(degree,spec):
    source=ROOT/spec['source']
    with source.open() as f:
        n,m=map(int,f.readline().split())
        assert (n,m)==(spec['n'],spec['m'])
        edge_lines=f.read()
    old_degrees=[0]*n
    for line in edge_lines.splitlines():
        u,v=map(int,line.split());old_degrees[u]+=1;old_degrees[v]+=1
    return dict(degree=degree,source=source,n=n,m=m,old_degrees=old_degrees,edge_lines=edge_lines,core_n=spec['core_n'])


def main():
    prediction=load(OUT/'PREDICTION.json');assert prediction['frozen_before_completion_checks']
    pool_paths={d:GROUP/'pool'/f'pool{d}.json' for d in [12,11]}
    if not all(p.exists() for p in pool_paths.values()):
        print('WAITING_POOL',json.dumps({str(d):p.exists() for d,p in pool_paths.items()}),flush=True)
        return
    assert not (OUT/'RESULT.json').exists(),'This finite producer has already terminated'
    bases={d:read_base(d,prediction['bases'][str(d)]) for d in [12,11]}
    frozen=[];pools={}
    for degree in [12,11]:
        pool=load(pool_paths[degree]);pools[degree]=pool
        b=bases[degree]
        assert (pool['source_n'],pool['source_m'])==(b['n'],b['m'])
        order=sorted(enumerate(pool['records']),key=lambda x:(len(x[1]['pins']),tuple(x[1]['pins']),x[0]))
        for original_index,item in order:
            pins=item['pins'];assert pins==sorted(set(pins))
            cap=degree-len(pins)
            assert cap==item['anchor_cap']
            frozen.append(dict(ordinal=len(frozen),degree=degree,pool_record_index=original_index,
                pool_index=item.get('pool_index',original_index),mandatory_pins=pins,anchor_cap=cap,
                source_n=b['n'],source_m=b['m'],source_graph=relative(b['source'])))
    save('frozen_items.json',frozen)
    freeze=dict(status='FROZEN_BEFORE_COVERAGE',items=len(frozen),order=prediction['order'],
        by_degree={str(d):dict(Counter(len(r['mandatory_pins']) for r in frozen if r['degree']==d)) for d in [12,11]},
        unsupported_anchor_capacity_items=[r['ordinal'] for r in frozen if r['anchor_cap']>2],
        CPU_parent_plus_all_children_seconds=cpu())
    save('freeze_summary.json',freeze)
    print('FROZEN '+json.dumps(freeze),flush=True)
    compile_cpu=compile_native();(OUT/'items').mkdir(exist_ok=True)
    rows=[];hit=None;status='ALL_FROZEN_ITEMS_TERMINAL';native_calls=0;first_profile=None
    for fitem in frozen:
        degree=fitem['degree'];b=bases[degree];pins=fitem['mandatory_pins'];cap=fitem['anchor_cap']
        row=dict(fitem)
        blocked=[v for v in pins if b['old_degrees'][v]>=degree]
        if blocked:
            row.update(status='CURRENT_DEGREE_BLOCKED',blocked_pins=blocked);rows.append(row);continue
        if cap<0 or cap>2:
            row.update(status='UNEXECUTED_ANCHOR_CAPACITY_OUTSIDE_ZERO_ONE_TWO',required_capacity=cap);rows.append(row);continue
        if BUDGET-cpu()<8.0:
            status='TOTAL_CPU_RESERVE_STOP';break
        prefix=OUT/'items'/f'ord{fitem["ordinal"]:05d}_d{degree}_pool{fitem["pool_index"]}'
        pinfile=Path(str(prefix)+'.pins.txt');pinfile.write_text(' '.join(map(str,pins))+'\n')
        mode='prepare' if cap else 'verify'
        with Path(str(prefix)+'.log').open('w') as log:
            ret=subprocess.run([str(OUT/'cover'),mode,str(b['source']),str(pinfile),str(prefix),str(degree)],stdout=log,stderr=log)
        native_calls+=1
        if ret.returncode:
            row.update(status='UNKNOWN_NATIVE_PROCESS_LIMIT',returncode=ret.returncode);rows.append(row);continue
        check=load(Path(str(prefix)+'.json'))
        row.update(mandatory_R4_file=relative(Path(str(prefix)+'.json')),native_CPU_seconds=check['CPU_seconds'])
        if check['status']=='DEGREE_INFEASIBLE':
            row.update(status='CURRENT_DEGREE_BLOCKED_NATIVE',blocked_pins=check['blocked']);rows.append(row);continue
        assert (check['source_n'],check['source_m'])==(b['n'],b['m']) and check['pins']==pins
        missing=check['missing'];core_missing=[v for v in missing if v<b['core_n']]
        row.update(mandatory_R4_missing=len(missing),core_R4_missing_count=len(core_missing),extra_R4_missing_count=len(missing)-len(core_missing))
        if core_missing:
            item=pools[degree]['records'][fitem['pool_record_index']]
            row.update(status='PCORE_COUNTEREXAMPLE_STOP',missing_core_vertices=core_missing,pool_witness=item)
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
        if first_profile is None and native_calls>=5:
            first_profile=dict(native_calls=native_calls,rows_visited=len(rows)+1,total_CPU_seconds=cpu(),compile_CPU_seconds=compile_cpu,
                estimated_allitems_CPU_seconds=cpu()*len(frozen)/max(1,len(rows)+1))
            save('first_profile.json',first_profile);print('PROFILE '+json.dumps(first_profile),flush=True)
        if anchors is None:rows.append(row);continue
        neighbors=sorted(pins+anchors)
        assert len(neighbors)==len(set(neighbors))<=degree
        assert all(b['old_degrees'][v]<degree for v in neighbors)
        selected_path=Path(str(prefix)+'.json');good=check
        if anchors:
            pinfile.write_text(' '.join(map(str,neighbors))+'\n');selected=Path(str(prefix)+'_selected')
            with Path(str(selected)+'.log').open('w') as log:
                ret=subprocess.run([str(OUT/'cover'),'verify',str(b['source']),str(pinfile),str(selected),str(degree)],stdout=log,stderr=log)
            native_calls+=1
            assert ret.returncode==0
            selected_path=Path(str(selected)+'.json');good=load(selected_path)
        assert good['missing_count']==0 and good['covered_count']==b['n']
        assert max(good['pin_current_degrees'])<degree
        graph=OUT/f'graph_d{degree}_D5_n{b["n"]+1}.edges'
        with graph.open('w') as f:
            f.write(f'{b["n"]+1} {b["m"]+len(neighbors)}\n');f.write(b['edge_lines'])
            if b['edge_lines'] and not b['edge_lines'].endswith('\n'):f.write('\n')
            for v in neighbors:f.write(f'{v} {b["n"]}\n')
        item=pools[degree]['records'][fitem['pool_record_index']]
        row.update(status='PRODUCER_COMPLETE_FIRST_HIT_ROOT_ACCEPTANCE_PENDING',new_vertex=b['n'],new_n=b['n']+1,
            new_m=b['m']+len(neighbors),new_vertex_degree=len(neighbors),full_neighbor_set=neighbors,anchors=anchors,
            neighbors_old_degrees=good['pin_current_degrees'],actual_current_R4_missing=0,actual_current_R4_covered=b['n'],
            actual_selected_R4_file=relative(selected_path),graph_file=relative(graph),source_edges_retained=True,
            new_neighbor_type='Folded Redei15 projectiveblocking set plus permitted oldanchors',pool_witness=item,
            pool_file=relative(pool_paths[degree]),actual_all_source_D=None)
        hit=row;rows.append(row);save('first_hit.json',hit);status='FIRST_COMPLETE_GRAPH_STOP'
        print('FIRST_HIT '+json.dumps({k:row[k] for k in ['degree','pool_index','new_n','new_m','full_neighbor_set','anchors','graph_file']}),flush=True)
        break
    result=dict(status=status,scope_items=len(frozen),rows_visited=len(rows),items_unattempted=len(frozen)-len(rows),
        rows=rows,accepted_extensions=int(hit is not None),first_hit_file='first_hit.json' if hit else None,
        compile_CPU_seconds=compile_cpu,CPU_parent_plus_all_children_seconds=cpu(),native_calls=native_calls,
        row_status_counts=dict(Counter(r['status'] for r in rows)),core_counterexample=status=='PCORE_COUNTEREXAMPLE_STOP',
        producer_complete_current_R4_acceptance=bool(hit),old_source_BFS=0,all_source_BFS=0,external_review=0,Lean=0,MIP=0,
        shared_delivery_modified=False,pending=['Root independent newmechanism acceptance'] if hit else [])
    save('RESULT.json',result);save('terminal.json',{k:v for k,v in result.items() if k!='rows'})
    report=(f"# Redei15 finite production\n\nStatus: {status}. Frozen {len(frozen)} items; visited {len(rows)}; unattempted {len(frozen)-len(rows)}. "
        f"Accepted complete graphs: {int(hit is not None)}. Total parent+all-child CPU: {cpu():.6f}s. "
        "Current source degrees and complete selected radius4 coverage determine acceptance. The inherited polar/blocking lemma was checked against actual core coverage for every executed mandatory set. "
        "No old-source BFS, all-source BFS, new anchors beyond2, MIP, shared delivery, Wiki or Lean operation was performed.\n")
    if hit:report+=f"\nFirst hit: [{hit['new_n']} vertices, degree{hit['degree']}]({Path(hit['graph_file']).name}), literal neighbors {hit['full_neighbor_set']}. Root newmechanism acceptance pending.\n"
    report+="\nFinite failures concern their literal pinset/current base and allowed anchors. UNKNOWN and unattempted items remain open.\n"
    (OUT/'REPORT.md').write_text(report)
    print('TERMINAL '+json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)


if __name__=='__main__':main()

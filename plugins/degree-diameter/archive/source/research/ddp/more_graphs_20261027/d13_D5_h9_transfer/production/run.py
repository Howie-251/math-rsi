"""Degree13 current-source Redei15 zero/one/two-anchor production only."""
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
INITIAL_SELF=time.process_time()
INITIAL_CHILD=resource.getrusage(resource.RUSAGE_CHILDREN)
load=lambda p:json.loads(p.read_text())


def cpu():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-INITIAL_SELF+c.ru_utime+c.ru_stime-INITIAL_CHILD.ru_utime-INITIAL_CHILD.ru_stime


def save(name,d):
    (OUT/name).write_text(json.dumps(d,indent=2)+'\n')


def rel(p):return str(p.relative_to(ROOT))


def convert_source(prediction):
    ready=load(GROUP/'READY_FOR_POOL.json')
    source=ROOT/ready['source_graph']
    if source.exists():
        with source.open() as f:
            assert tuple(map(int,f.readline().split()))==(51417,324451)
        degrees=list((ROOT/ready['degree_cache']).read_bytes())
        assert len(degrees)==51417 and max(degrees)==13 and sum(degrees)==2*324451
        save('source_binding.json',dict(status='REUSED_ONCE_CONVERTED_CURRENT_SOURCE',
            raw_source=prediction['source'],edge_source=rel(source),source_n=51417,source_m=324451,
            degree_cap=13,core_n=50554,extras=863,degree_histogram=dict(Counter(degrees)),
            degree_cache=ready['degree_cache'],source_conversion_repeated=False,old_pi12_reused=False,
            all_source_BFS=0,CPU_seconds=cpu()))
        return source,degrees
    raw=ROOT/prediction['source'];adj=[];comments=[]
    with raw.open() as f:
        for line in f:
            line=line.strip()
            if not line:continue
            if line.startswith('#'):comments.append(line);continue
            values=list(map(int,line.split()));assert values[0]==len(adj)
            adj.append(values[1:])
    n=len(adj);degrees=list(map(len,adj))
    assert n==51417 and max(degrees)==13
    edges=[(u,v) for u,ns in enumerate(adj) for v in ns if u<v]
    assert len(edges)==324451 and sum(degrees)==2*len(edges)
    source=OUT/'source51417.edges'
    with source.open('w') as f:
        f.write(f'{n} {len(edges)}\n')
        for u,v in edges:f.write(f'{u} {v}\n')
    binding=dict(status='ACTUAL_RAW_ADJACENCY_CONVERTED_ONCE',raw_source=rel(raw),edge_source=rel(source),
        source_n=n,source_m=len(edges),degree_cap=13,core_n=50554,extras=863,
        degree_histogram=dict(Counter(degrees)),source_comments=comments,all_source_BFS=0,
        old_pi12_reused=False,CPU_seconds=cpu())
    save('source_binding.json',binding)
    return source,degrees


def compile_native():
    original=(BASE/'h9_redei15/production/cover.cpp').read_text()
    assert original.count('assert(DEG==11||DEG==12);')==1
    assert 'MAXN' not in original
    original=original.replace('assert(DEG==11||DEG==12);','assert(DEG==13);')
    marker='if(mode=="verify"||missing.empty())'
    assert original.count(marker)==1
    # The raw string keeps C++ JSON escapes as source text.
    guard=r'''if(any_of(missing.begin(),missing.end(),[](int v){return v<50554;})){out<<",\"status\":\"CORE_MISSING_STOP\",\"CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";return 0;}
 '''
    original=original.replace(marker,guard+marker)
    (OUT/'cover.cpp').write_text(original)
    started=cpu()
    subprocess.run(['g++','-O3','-std=c++17',str(OUT/'cover.cpp'),'-o',str(OUT/'cover')],check=True)
    return cpu()-started


def main():
    prediction=load(OUT/'PREDICTION.json');assert prediction['frozen_before_completion']
    poolfile=GROUP/'redei_pool/pool13.json'
    if not poolfile.exists():
        print('WAITING_POOL13',flush=True);return
    assert not (OUT/'RESULT.json').exists(),'This finite batch is already terminal'
    pool=load(poolfile);assert (pool['source_n'],pool['source_m'])==(51417,324451)
    if not pool['records']:
        poolresult=load(GROUP/'redei_pool/RESULT.json')
        assert poolresult['complete1120plane_scope'] and poolresult['raw_shape_occurrences_covered']==786240
        assert poolresult['raw_degree_allowed_occurrences']==0
        save('frozen_items.json',[]);save('deferred_cap3_items.json',[])
        save('source_binding.json',load(GROUP/'READY_FOR_POOL.json'))
        result=dict(status='EMPTY_COMPLETE_DEGREE_POOL_NO_COMPLETION_EXECUTED',
            source_n=51417,source_m=324451,degree_cap=13,core_n=50554,extras=863,
            pool_file=rel(poolfile),pool_evidence=rel(GROUP/'redei_pool/RESULT.json'),
            finite_shape_occurrences=786240,degree_allowed_occurrences=0,
            phase1_scope_records=0,phase1_rows_visited=0,phase1_unattempted=0,
            deferred_cap3_records=0,deferred_cap3_executed=0,
            accepted_extensions=0,actual_n=None,actual_D=None,native_compiled=False,native_calls=0,
            source_conversion_repeated=False,old_source_BFS=0,all_source_BFS=0,
            R4_evaluations=0,anchor_tests=0,MIP=0,shared_delivery_modified=False,
            prediction_supported=False,CPU_parent_plus_all_children_seconds=cpu(),pending=[])
        save('RESULT.json',result);save('terminal.json',result)
        (OUT/'REPORT.md').write_text('# Degree13 Redei15 completion: empty degree pool\n\nThe complete702-shape by1120-plane pool contains no degree-legal occurrence on the actual51417/324451/max13 source. Therefore no11/12/13-pin or deferred10-pin candidate reaches completion. The prediction is refuted at the degree filter; no native compilation, source reconversion, R4, anchor search or graph generation was run. The existing bound source and current50554-core mapping were reused, with no oldpi12 or oldsource BFS. This closes only the frozen702 PGL3(F3) orbit in the1120 saved F3-defined singular planes on this fixed source, not arbitrary blocking sets or all degree13 graphs.\n')
        print('TERMINAL '+json.dumps(result),flush=True)
        return
    source,degrees=convert_source(prediction)
    order=sorted(enumerate(pool['records']),key=lambda x:({11:0,12:1,13:2,10:3}.get(len(x[1]['pins']),4),tuple(x[1]['pins']),x[0]))
    frozen=[];deferred=[]
    for original_index,item in order:
        pins=item['pins'];assert pins==sorted(set(pins))
        cap=13-len(pins);assert cap==item['anchor_cap']
        row=dict(ordinal=len(frozen),pool_record_index=original_index,pool_index=item.get('pool_index',original_index),
            mandatory_pins=pins,anchor_cap=cap,source_n=51417,source_m=324451)
        frozen.append(row)
        if cap>2:deferred.append(row)
    quick=[r for r in frozen if 0<=r['anchor_cap']<=2]
    save('frozen_items.json',frozen);save('deferred_cap3_items.json',deferred)
    freeze=dict(status='FROZEN_BEFORE_COVERAGE',all_pool_records=len(frozen),phase1_records=len(quick),
        deferred_cap3_records=len(deferred),pin_count_histogram=dict(Counter(len(r['mandatory_pins']) for r in frozen)),
        source_n=51417,source_m=324451,degree_cap=13,CPU=cpu())
    save('freeze_summary.json',freeze);print('FROZEN '+json.dumps(freeze),flush=True)
    compile_cpu=compile_native();(OUT/'items').mkdir(exist_ok=True)
    rows=[];hit=None;native_calls=0;mandatory_calls=0;profile=None;status='PHASE1_ALL_ZERO_ONE_TWO_ANCHOR_ITEMS_TERMINAL'
    for item in quick:
        pins=item['mandatory_pins'];cap=item['anchor_cap']
        row=dict(item,source_graph=rel(source))
        blocked=[p for p in pins if degrees[p]>=13]
        if blocked:
            row.update(status='CURRENT_DEGREE_BLOCKED',blocked_pins=blocked);rows.append(row);continue
        if BUDGET-cpu()<8.0:status='TOTAL_CPU_RESERVE_STOP';break
        prefix=OUT/'items'/f'ord{item["ordinal"]:05d}_pool{item["pool_index"]}'
        pf=Path(str(prefix)+'.pins.txt');pf.write_text(' '.join(map(str,pins))+'\n')
        with Path(str(prefix)+'.log').open('w') as log:
            ret=subprocess.run([str(OUT/'cover'),'prepare' if cap else 'verify',str(source),str(pf),str(prefix),'13'],stdout=log,stderr=log)
        native_calls+=1;mandatory_calls+=1
        if ret.returncode:
            row.update(status='UNKNOWN_NATIVE_PROCESS_LIMIT',returncode=ret.returncode);rows.append(row);continue
        check=load(Path(str(prefix)+'.json'))
        row.update(mandatory_R4_file=rel(Path(str(prefix)+'.json')),native_CPU_seconds=check['CPU_seconds'])
        if check['status']=='DEGREE_INFEASIBLE':
            row.update(status='CURRENT_DEGREE_BLOCKED_NATIVE',blocked_pins=check['blocked']);rows.append(row);continue
        assert (check['source_n'],check['source_m'])==(51417,324451) and check['pins']==pins
        missing=check['missing'];core=[v for v in missing if v<50554]
        row.update(mandatory_R4_missing=len(missing),core_R4_missing_count=len(core),extra_R4_missing_count=len(missing)-len(core))
        if core:
            row.update(status='PCORE_COUNTEREXAMPLE_STOP',missing_core_vertices=core,pool_witness=pool['records'][item['pool_record_index']])
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
            profile=dict(mandatory_calls=mandatory_calls,rows_visited=len(rows)+1,CPU=cpu(),compile_CPU_seconds=compile_cpu,
                estimated_all_phase1_CPU=cpu()*len(quick)/max(1,len(rows)+1))
            save('first5_profile.json',profile);print('PROFILE '+json.dumps(profile),flush=True)
        if anchors is None:rows.append(row);continue
        neighbors=sorted(pins+anchors)
        assert len(neighbors)==len(set(neighbors))<=13 and all(degrees[p]<13 for p in neighbors)
        good=check;selected_path=Path(str(prefix)+'.json')
        if anchors:
            pf.write_text(' '.join(map(str,neighbors))+'\n');selected=Path(str(prefix)+'_selected')
            with Path(str(selected)+'.log').open('w') as log:
                ret=subprocess.run([str(OUT/'cover'),'verify',str(source),str(pf),str(selected),'13'],stdout=log,stderr=log)
            native_calls+=1;assert ret.returncode==0
            selected_path=Path(str(selected)+'.json');good=load(selected_path)
        assert good['missing_count']==0 and good['covered_count']==51417
        assert max(good['pin_current_degrees'])<13
        graph=OUT/'graph_d13_D5_n51418.edges'
        with source.open() as old,graph.open('w') as new:
            old.readline();new.write(f'51418 {324451+len(neighbors)}\n')
            for line in old:new.write(line)
            for p in neighbors:new.write(f'{p} 51417\n')
        row.update(status='PRODUCER_COMPLETE_NEW_PARAMETER_ROOT_CHECK_PENDING',degree=13,target_D=5,savedL=51417,
            new_vertex=51417,new_n=51418,new_m=324451+len(neighbors),new_vertex_degree=len(neighbors),
            full_neighbor_set=neighbors,anchors=anchors,neighbors_old_degrees=good['pin_current_degrees'],
            actual_current_R4_missing=0,actual_current_R4_covered=51417,actual_selected_R4_file=rel(selected_path),
            graph_file=rel(graph),raw_source=prediction['source'],source_edges_retained=True,
            pool_file=rel(poolfile),pool_witness=pool['records'][item['pool_record_index']],
            neighbor_type='Currentwholeclassfolded Redei15blocking set plus permittedoldanchors',actual_all_source_D=None)
        hit=row;rows.append(row);save('first_hit.json',row);status='FIRST_COMPLETE_NEW_PARAMETER_GRAPH_STOP'
        print('FIRST_HIT '+json.dumps({k:row[k] for k in ['degree','pool_index','new_n','new_m','full_neighbor_set','anchors','graph_file']}),flush=True)
        break
    result=dict(status=status,source_n=51417,source_m=324451,degree_cap=13,core_n=50554,extras=863,
        all_pool_records=len(frozen),phase1_scope_records=len(quick),phase1_rows_visited=len(rows),phase1_unattempted=len(quick)-len(rows),
        deferred_cap3_records=len(deferred),deferred_cap3_executed=0,rows=rows,accepted_extensions=int(hit is not None),
        first_hit_file='first_hit.json' if hit else None,compile_CPU_seconds=compile_cpu,CPU_parent_plus_all_children_seconds=cpu(),
        native_calls=native_calls,row_status_counts=dict(Counter(r['status'] for r in rows)),
        core_counterexample=status=='PCORE_COUNTEREXAMPLE_STOP',old_source_BFS=0,all_source_BFS=0,MIP=0,
        anchors_over_two_executed=0,shared_delivery_modified=False,
        pending=['Root independent newparameter acceptance'] if hit else (['Root decision on frozen10pin/cap3 items'] if deferred else []))
    save('RESULT.json',result);save('terminal.json',{k:v for k,v in result.items() if k!='rows'})
    (OUT/'REPORT.md').write_text(f'# Degree13 Redei15 production\n\n{status}. Phase1 visited{len(rows)}/{len(quick)}; deferredcap3={len(deferred)} unexecuted. Completegraphs={int(hit is not None)}. Parent+allchild CPU{cpu():.6f}s. Actualsource51417/324451 convertedoncefromrawadjacency; no oldsource/allsourceBFS. Everyacceptedneighbor set passedactualdegree13 andcomplete selectedR4 over51417oldvertices. Root independentnewparameter acceptance pending onlyifhit. No sharedfamily/Wiki edit, MIP, thirdanchor, or oldpi12 reuse.\n')
    print('TERMINAL '+json.dumps({k:v for k,v in result.items() if k!='rows'}),flush=True)


if __name__=='__main__':main()

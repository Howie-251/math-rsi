import time
START=time.process_time();WALL=time.time()
import resource
resource.setrlimit(resource.RLIMIT_CPU,(20,21))
import csv,json,os
from pathlib import Path
from collections import Counter
D=Path(__file__).resolve().parent
PARENT=D.parent.parent
SOURCE=PARENT.parent
phase='read_accepted_center_recipe'
def read_edges(path,expected_n,expected_m):
    # Each file is opened exactly once. No graph-distance checks on accepted inputs.
    edges=[]
    with path.open() as f:
        header=tuple(map(int,f.readline().split()))
        assert header==(expected_n,expected_m),(str(path),'header',header)
        previous=(-1,-1)
        for lineno,line in enumerate(f,2):
            a,b=map(int,line.split())
            assert 0<=a<b<expected_n,(str(path),lineno,a,b)
            assert (a,b)>previous,(str(path),lineno,'not_strict_lex')
            edges.append((a,b));previous=(a,b)
    assert len(edges)==expected_m,(str(path),'body_count',len(edges))
    return edges
try:
    centers=json.loads((PARENT/'ORDERED_CENTERS.json').read_text())['centers']
    assert len(centers)==289
    diag={c['index']:c for c in centers if c['is_incident_flag']}
    assert len(diag)==17 and {c['spread_index'] for c in diag.values()}==set(range(17))
    assert all(c['index']==i and c['old_center_label']==85*c['point']+c['spread_line'] for i,c in enumerate(centers))
    expected_removed={(7225+c['spread_index'],7242+i) for i,c in diag.items()}
    expected_added={(f,7531) for f in range(7225,7242)}
    (D/'HANDLE.json').write_text(json.dumps(dict(pid=os.getpid(),phase='literal_parse_and_new_root_BFS',CPU_budget_seconds=20,single_worker=True),indent=2)+'\n')
    phase='parse_three_literal_files_once'
    h_edges=read_edges(SOURCE/'graph_d25_D3_n7242.edges',7242,90525)
    old_edges=read_edges(PARENT/'graph_d26_D3_n7531.edges',7531,97750)
    new_edges=read_edges(D.parent/'graph_d26_D3_n7532.edges',7532,97750)
    old_set,new_set=set(old_edges),set(new_edges)
    removed=old_set-new_set;added=new_set-old_set
    assert removed==expected_removed,('removed_delta',sorted(removed),sorted(expected_removed))
    assert added==expected_added,('added_delta',sorted(added),sorted(expected_added))
    actual_old_body=[(a,b) for a,b in new_edges if b<7242]
    assert actual_old_body==h_edges,('source_H_body_not_exact',len(actual_old_body))
    h_adj=[[] for _ in range(7242)]
    for a,b in h_edges:h_adj[a].append(b);h_adj[b].append(a)
    adj=[[] for _ in range(7532)]
    for a,b in new_edges:adj[a].append(b);adj[b].append(a)
    for row in adj:row.sort()
    degree_hist=Counter(map(len,adj))
    assert degree_hist==Counter({17:1,24:17,25:289,26:7225}),('degree_hist',degree_hist)
    assert adj[7531]==list(range(7225,7242))
    phase='bind_all_289_modified_clone_neighborhoods'
    pin_owner={};bindings=[]
    for i,c in enumerate(centers):
        center=c['old_center_label'];label=7242+i
        actual_U=sorted(v for v in h_adj[center] if v<7225)
        raw_without_self=sorted(v for v in c['raw_neighborhood_ordered'] if v!=center)
        assert actual_U==raw_without_self,('U_openN_binding',i)
        assert adj[label]==actual_U,('clone_literal_binding',i)
        assert len(actual_U)==(24 if i in diag else 25)
        for v in actual_U:
            assert v not in pin_owner,('pin_collision',i,v,pin_owner.get(v))
            pin_owner[v]=i
        bindings.append(dict(index=i,center=center,clone=label,point=c['point'],spread_index=c['spread_index'],
                             diagonal=i in diag,pins=actual_U,
                             deleted_filler=(7225+c['spread_index']) if i in diag else -1))
    assert len(pin_owner)==7208
    assert not any(a>=7242 and b>=7242 for a,b in new_edges)
    with (D/'ALL_289_CLONE_BINDINGS.tsv').open('w') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['index','center','clone','point','spread_index','diagonal','deleted_filler','pin_count','actual_U_pins'])
        for c in bindings:w.writerow([*[c[k] for k in ['index','center','clone','point','spread_index','diagonal','deleted_filler']],len(c['pins']),json.dumps(c['pins'])])
    (D/'EXACT_LITERAL_DELTA.json').write_text(json.dumps(dict(
        source_n=7242,source_m=90525,all_source_H_edges_exact=True,
        removed_edges=sorted(removed),added_edges=sorted(added),only_17_diagonal_F_edges_removed=True,
        clone_new_new_edges=0,source_H_to_clones=7208,hub_to_fillers=17,
        total_new_to_source_H=7225,clone_binding_rows=289,clone_pins_only_U=True,
        clone_pin_distinct_count=7208,source_pin_max_load=1,
        diagonal_indices=sorted(diag),actual_diagonal_owners=[diag[i]['spread_index'] for i in sorted(diag)]),indent=2)+'\n')
    phase='290_ordinary_new_root_BFS'
    bfstart=time.process_time()
    roots=[];witness=None;predicted_counts=Counter();actual_classes={}
    predictions={'diagonal':(1,24,418,7089),'offdiagonal':(1,25,441,7065),'hub':(1,17,425,7089)}
    for root in range(7242,7532):
        kind='hub' if root==7531 else ('diagonal' if root-7242 in diag else 'offdiagonal')
        dist=[-1]*7532;prev=[-1]*7532;dist[root]=0;q=[root]
        for v in q:
            if dist[v]==3:continue
            for v2 in adj[v]:
                if dist[v2]<0:
                    dist[v2]=dist[v]+1;prev[v2]=v;q.append(v2)
        hist=tuple(sum(d==r for d in dist) for r in range(4))
        missing=sum(d<0 for d in dist)
        record=dict(root=root,kind=kind,actual_hist=hist,predicted_hist=predictions[kind],
                    prediction_match=hist==predictions[kind],reached=len(q),missing=missing,
                    first_missing=next((i for i,d in enumerate(dist) if d<0),-1))
        roots.append(record);predicted_counts[kind]+=1
        actual_classes.setdefault(kind,Counter())[hist]+=1
        if witness is None:
            target=next((i for i,d in enumerate(dist) if d==3 and i<7225),None)
            if target is not None:
                walk=[];x=target
                while x!=-1:walk.append(x);x=prev[x]
                walk.reverse()
                witness=dict(root=root,target=target,distance=3,genuine_walk=walk,
                             derivation='ordinary BFS layers: target absent at0/1/2 and present at3; no old-root BFS')
    bfs_cpu=time.process_time()-bfstart
    assert len(roots)==290 and witness is not None
    with (D/'ALL_290_NEW_ROOT_BFS.tsv').open('w') as f:
        w=csv.writer(f,delimiter='\t');w.writerow(['root','kind','actual0','actual1','actual2','actual3','pred0','pred1','pred2','pred3','prediction_match','reached','missing','first_missing'])
        for r in roots:w.writerow([r['root'],r['kind'],*r['actual_hist'],*r['predicted_hist'],r['prediction_match'],r['reached'],r['missing'],r['first_missing']])
    (D/'NON_D2_ACTUAL_NEW_ROOT_WITNESS.json').write_text(json.dumps(witness,indent=2)+'\n')
    all_roots=all(r['missing']==0 for r in roots)
    all_hist=all(r['prediction_match'] for r in roots)
    status=('PASS' if all_hist else 'PASS_WITH_BFS_HIST_PREDICTION_MISMATCH') if all_roots else 'FAIL_NEW_ROOT_D3'
    result=dict(status=status,literal_delta_PASS=True,all289_clone_bindings_PASS=True,
        actual_order=7532,actual_edges=97750,simple=True,header_matches_body=True,degree_histogram=dict(sorted(degree_hist.items())),
        max_degree=26,old_old_H_edges_retained=90525,removed_diagonal_clone_F_edges=17,added_hub_F_edges=17,
        source_H_to_clones_edges=7208,hub_to_source_F_edges=17,new_new_edges=0,
        old_edgefiles_parse_counts={'source_H7242':1,'accepted7531_for_delta_only':1,'new7532':1},
        old_roots_BFS=0,new_roots_BFS=290,new_root_classes=dict(predicted_counts),
        all_new_roots_R3_cover=all_roots,all_hist_predictions_match=all_hist,
        histogram_mismatches=[r for r in roots if not r['prediction_match']],
        actual_hist_by_class={k:[dict(hist=list(h),count=n) for h,n in sorted(v.items())] for k,v in actual_classes.items()},
        inherited_old_H_diameter_at_most=3,
        all_pair_D3_proof='Every H-H pair inherits retained H D3; all290 new roots independently cover all7532 vertices.',
        prefix_claim='Build modified clones from H, hub last. Each prefix D3 uses old-only paths proved in NOTE, not deletion from7531/maxgraph.',
        nonD2=witness,exact_diameter=3 if all_roots else None,
        paper_Moore_nonD2='maxdegree26 permits at most1+26+26*25=677 vertices at radius2;7532>677',
        BFS_CPU_seconds=bfs_cpu,total_CPU_seconds=time.process_time()-START,
        field_or_old_geometry_retests=0,old_graph_BFS=0,Lean_runs=0,solver_calls=0,new_candidates_generated=0,
        root_counts_or_reports_modified=False,priority_or_global_record_claim=False)
    (D/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    terminal=dict(status=status,total_CPU_seconds=time.process_time()-START,BFS_CPU_seconds=bfs_cpu,
                  wall_seconds=time.time()-WALL,CPU_budget_seconds=20,single_worker=True,
                  source_H_parse=1,old7531_delta_parse=1,new7532_parse=1,
                  ordinary_new_root_BFS=290,old_root_BFS=0,
                  all_processes_terminal=True,no_automatic_continuation=True,
                  measurement_boundary='Imports, recipe preparation, one parse of each literal input, exactdelta/degree/pinbinding, all290 new-root ordinary BFS, aggregation; no compiler required.')
    assert terminal['total_CPU_seconds']<20
    (D/'TERMINAL.json').write_text(json.dumps(terminal,indent=2)+'\n')
    (D/'HANDLE.json').write_text(json.dumps(dict(status='TERMINAL',all_processes_terminal=True),indent=2)+'\n')
    print(json.dumps(dict(terminal=terminal,actual_hist_by_class=result['actual_hist_by_class'],nonD2=witness),indent=2))
except Exception as e:
    fail=dict(status='FAILED_OR_UNKNOWN_NO_CONTINUATION',phase=phase,error=str(e),
              total_CPU_seconds=time.process_time()-START,all_processes_terminal=True)
    (D/'RESULT.json').write_text(json.dumps(fail,indent=2)+'\n')
    (D/'TERMINAL.json').write_text(json.dumps(fail,indent=2)+'\n')
    raise

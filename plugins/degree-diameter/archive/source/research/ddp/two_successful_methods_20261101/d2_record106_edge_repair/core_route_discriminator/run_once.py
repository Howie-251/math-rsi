#!/usr/bin/env python3
import time
START=time.process_time()
import collections,json,os,resource
from pathlib import Path
D=Path(__file__).resolve().parent
C=D.parent
resource.setrlimit(resource.RLIMIT_CPU,(3,3))
PRIOR=json.loads((C/'structure_symmetry_sector/TERMINAL.json').read_text())['case_CPU_seconds']

def dump(name,x):
    (D/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')

def complement_cycles(vertices,adj):
    vertices=set(vertices)
    comp={u:vertices-{u}-adj[u] for u in vertices}
    if any(len(n)!=2 for n in comp.values()):return None
    unseen=set(vertices);cycles=[]
    while unseen:
        start=min(unseen);prev=None;u=start;row=[]
        while u not in row:
            row.append(u);unseen.discard(u)
            options=comp[u]-({prev}if prev is not None else set())
            v=min(options);prev,u=u,v
        if u!=start:return None
        cycles.append(row)
    return cycles

def main():
    dump('HANDLE.json',dict(pid=os.getpid(),actual_process_started=True,stage='CORE_SIGNATURE_READOUT',
        batch_CPU_budget_seconds=3,prior_case_CPU_seconds=PRIOR,case_CPU_budget_seconds=20))
    inherited=json.loads((C/'structure_probe/RESULT.json').read_text())
    small=set().union(*(set(v)for v in inherited['color_classes']if len(v)==7))
    core=set(next(v for v in inherited['color_classes']if len(v)==49))
    A=[set()for _ in range(106)]
    with (C/'source106.author.adjlist.txt').open()as f:
        for line in f:
            row=list(map(int,line.split()));A[row[0]]=set(row[1:])
    grouped=collections.defaultdict(list)
    for u in sorted(core):grouped[tuple(sorted(A[u]&small))].append(u)
    groups=[];groupof={}
    for i,(signature,vertices)in enumerate(sorted(grouped.items())):
        for u in vertices:groupof[u]=i
        groups.append(dict(group_index=i,small_neighbors=list(signature),vertices=vertices,
            size=len(vertices)))
    rowprofiles=[];matrix=[[0]*len(groups)for _ in groups]
    for u in sorted(core):
        neighbors=sorted(A[u]&core)
        counts=collections.Counter(groupof[v]for v in neighbors)
        for gi,count in counts.items():matrix[groupof[u]][gi]+=count
        rowprofiles.append(dict(vertex=u,signature_group=groupof[u],core_neighbors=neighbors,
            core_degree=len(neighbors),neighbor_group_counts=dict(sorted(counts.items()))))
    for group in groups:
        members=set(group['vertices'])
        degrees={u:len(A[u]&members)for u in group['vertices']}
        group['internal_degree_by_vertex']=degrees
        group['internal_degree_histogram']=dict(sorted(collections.Counter(degrees.values()).items()))
        group['four_regular_on_seven']=len(members)==7 and set(degrees.values())=={4}
        if group['four_regular_on_seven']:
            cyc=complement_cycles(members,A)
            group['complement_cycle_components']=cyc
            group['circulant_C7_complement_certified']=cyc is not None and len(cyc)==1 and len(cyc[0])==7
        else:group['circulant_C7_complement_certified']=False
    blocks=[]
    for i in range(len(groups)):
        for j in range(i+1,len(groups)):
            if not matrix[i][j]:continue
            left={u:sorted(A[u]&set(groups[j]['vertices']))for u in groups[i]['vertices']}
            right={u:sorted(A[u]&set(groups[i]['vertices']))for u in groups[j]['vertices']}
            matching=all(len(v)<=1 for v in left.values())and all(len(v)<=1 for v in right.values())
            perfect=matching and all(len(v)==1 for v in left.values())and all(len(v)==1 for v in right.values())
            blocks.append(dict(left_group=i,right_group=j,edges=[[u,v]for u,vs in left.items()for v in vs],
                edge_count=matrix[i][j],left_degree_histogram=dict(collections.Counter(map(len,left.values()))),
                right_degree_histogram=dict(collections.Counter(map(len,right.values()))),
                matching=matching,perfect_matching=perfect))
    profiles=json.loads((C/'CRITICAL_EDGE_PROFILES.json').read_text())['profiles']
    saved={(r['u'],r['v']):r for r in profiles}
    payload={}
    for root in [8,10]:
        rows=[]
        for middle in sorted(A[root]&core):
            r=saved[tuple(sorted([root,middle]))]
            unique=(r['u_unique_via_v_targets']if r['u']==root else r['v_unique_via_u_targets'])
            rows.append(dict(first_edge=[root,middle],inherited_unique_twohop_targets=unique,
                source='CRITICAL_EDGE_PROFILES.json; not recomputed'))
        payload[str(root)]=rows
    witness=None
    for row in payload['8']:
        middle=row['first_edge'][1]
        for target in row['inherited_unique_twohop_targets']:
            if target==10 or target in A[10]:continue
            via10=[w for w in sorted(A[10]&core)if target in A[w]]
            if via10:
                # Only a targeted four-neighbor route readout, never all-pair source validation.
                witness=dict(target=target,route_from8=[8,middle,target],
                    unique_from8_inherited_from_profile=True,
                    routes_from10=[[10,w,target]for w in via10],
                    small_common_route_absent_reason='8 and10 have identical small neighbors; the inherited unique8 route uses a core middle.',
                    changed_physical_middle_edges=True)
                break
        if witness:break
    dump('SIGNATURE_CLASSES.json',dict(classes=groups))
    dump('CORE_ROW_DEGREE_PROFILES.json',dict(rows=rowprofiles))
    dump('CORE_GROUP_EDGE_BLOCKS.json',dict(directed_group_edge_count_matrix=matrix,nonempty_intergroup_blocks=blocks,
        matrix_diagonal_counts_each_internal_edge_twice=True))
    dump('ROUTE_8_10_DISCRIMINATOR.json',dict(same_small_neighbors=sorted(A[8]&small),
        core_neighbors8=sorted(A[8]&core),core_neighbors10=sorted(A[10]&core),
        signature_group8=groupof[8],signature_group10=groupof[10],
        inherited_unique_route_payloads=payload,targeted_route_witness=witness))
    prediction_a=len(groups)==7 and all(g['size']==7 for g in groups)
    result=dict(status='CORE_SIGNATURE_AND_ROUTE_READOUT_COMPLETE',
        prediction_seven_size7_signature_classes='SUPPORTED'if prediction_a else'REFUTED',
        signature_class_count=len(groups),signature_class_size_histogram=dict(sorted(collections.Counter(g['size']for g in groups).items())),
        all49_core_row_degree_histogram=dict(sorted(collections.Counter(r['core_degree']for r in rowprofiles).items())),
        size7_four_regular_groups=[g['group_index']for g in groups if g['four_regular_on_seven']],
        certified_C7_complement_circulant_groups=[g['group_index']for g in groups if g['circulant_C7_complement_certified']],
        nonempty_intergroup_blocks=len(blocks),matching_intergroup_blocks=sum(b['matching']for b in blocks),
        perfect_matching_intergroup_blocks=sum(b['perfect_matching']for b in blocks),
        nonmatching_block_indices=[[b['left_group'],b['right_group']]for b in blocks if not b['matching']],
        core8_and10_same_signature=groupof[8]==groupof[10],core8_and10_different_physical_core_neighbors=A[8]&core!=A[10]&core,
        targeted_route_witness=witness,root8_root10_private_payloads_source='Existing saved critical profiles',
        new_graph_BFS=0,source_common_neighbor_or_D2_revalidation=0,color_refinement_runs=0,
        sector_permutation_enumeration=0,general_graph_isomorphism=0,solver_Lean_field_rank_web_runs=0,
        new_graph_parameter_Lean_count=0,rootdocs_Wiki_oldfiles_modified=False,
        prior_case_CPU_seconds=PRIOR,batch_CPU_seconds=time.process_time()-START,
        case_CPU_seconds=PRIOR+time.process_time()-START,batch_CPU_budget_seconds=3,case_CPU_budget_seconds=20)
    text='''# Core-route discriminator: actual partition and route obligations

This is one new structural readout of the inherited49core labels and unchanged source adjacency; no source validity, common-neighbor all-pair test, BFS, color refinement, solver or isomorphism search was rerun. The previous duplicate-signature interface remains a failed uniqueness prediction, not a no-C7 theorem.

Actual signature partition: '''+str(len(groups))+''' classes, size histogram '''+str(result['signature_class_size_histogram'])+'''. The prediction of seven size-seven classes is '''+result['prediction_seven_size7_signature_classes']+'''. All classes, actual internal degrees, intergroup edges and each physical core row's neighbor-group counts are saved in SIGNATURE_CLASSES.json / CORE_GROUP_EDGE_BLOCKS.json / CORE_ROW_DEGREE_PROFILES.json. These data are not silently treated as automorphism orbits. Any7vertex4regular class is checked only for the exact complement-C7 certificate; absence of that form is not a general noncirculant classification.

Core8 and10 share small neighbors '''+str(sorted(A[8]&small))+''', but have core neighbors '''+str(sorted(A[8]&core))+''' and '''+str(sorted(A[10]&core))+''' respectively. Their same small signature therefore leaves different physical edges and different source route payloads unresolved.

The targeted route witness, using the existing unique-route profile for8, is:

```json
'''+json.dumps(witness,indent=2)+'''
```

The unique-from8 statement is inherited from the saved profile, not recomputed by common-neighbor enumeration. The10 routes were read only along its four core neighbors for that one target. This is a route discriminator, not a second full-source D2 check.

## Concrete consequence for internal-pin changes

If an original nonadjacent pair(v,u) has unique common middlew, deletingv-w loses that source route. In the current rule onlyG[S] changes. Ifv,u both lie inS, newz repairs them; ifv∈S andu outside, any replacement must be a chosen internal neighbora∈S that is an ORIGINAL neighbor ofu, givingv-a-u. Merely selecting another vertex with the same small signature asv does not preserve that physical core edge or its inherited unique-target payload. When deleting the displayed8-middle edge, the target in the witness must be selected too or receive an explicit replacement2route; the10-middle route cannot simply be substituted without a genuine edge from8 to that middle.

This directly changes the next selection/edge rule: track the actual4core-neighbor choices and their directional private-target lists, not just small-signature class membership. A duplicate-signature class can still have an automorphism acting on it together with other core classes; differing labeled neighborhoods neither prove nor refute that. Consequently nox8=x10 orbit constraint, arbitrary replacement of one by the other, orC7-invariant pin-set reduction is justified by this partition alone.

The data stop at structural route obligations. No S is selected, no core/sector permutation is enumerated, no rewiring or graph is generated, and no further timer follows. Root may use the concrete intergroup blocks and route payloads to formulate a separately authorized prediction; this result does not resolve the previous internal-rewiring UNKNOWN model or claim any new107graph.
'''
    (D/'NOTE.md').write_text(text)
    result['batch_CPU_seconds']=time.process_time()-START;result['case_CPU_seconds']=PRIOR+result['batch_CPU_seconds']
    dump('RESULT.json',result)
    dump('TERMINAL.json',dict(status=result['status'],running=False,all_processes_terminal=True,
        prior_case_CPU_seconds=PRIOR,batch_CPU_seconds=time.process_time()-START,
        case_CPU_seconds=PRIOR+time.process_time()-START,batch_CPU_budget_seconds=3,
        case_CPU_budget_seconds=20,no_automatic_continuation=True))
    dump('HANDLE.json',dict(pid=os.getpid(),stage='TERMINAL',actual_process_started=True,
        batch_CPU_budget_seconds=3,case_CPU_budget_seconds=20))
    print(json.dumps(dict(status=result['status'],signature_groups=len(groups),size_hist=result['signature_class_size_histogram'],
        prediction_a=result['prediction_seven_size7_signature_classes'],route=witness,
        batch_CPU_seconds=time.process_time()-START,case_CPU_seconds=PRIOR+time.process_time()-START),ensure_ascii=False),flush=True)

try:
    main()
except Exception as error:
    result=dict(status='UNKNOWN_IMPLEMENTATION_ERROR_NO_RETRY',exception=repr(error),
        prior_case_CPU_seconds=PRIOR,batch_CPU_seconds=time.process_time()-START,
        case_CPU_seconds=PRIOR+time.process_time()-START,batch_CPU_budget_seconds=3,case_CPU_budget_seconds=20)
    dump('RESULT.json',result);dump('TERMINAL.json',dict(**result,running=False,no_automatic_continuation=True))
    (D/'NOTE.md').write_text('The one bounded implementation stopped with the saved exception. No negative mathematical result or retry is claimed.\n')
    print(json.dumps(result),flush=True)

import collections,itertools,json,math,os,resource,time
from pathlib import Path
started=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(20,20))
D=Path(__file__).resolve().parent
def save(name,v):(D/name).write_text(json.dumps(v,indent=2)+'\n')
save('MINIMAL4_HANDLE.json',dict(pid=os.getpid(),running=True,CPU_budget_seconds=20))
source=json.loads((D/'SOURCE_RESULT.json').read_text())
profiles=json.loads((D/'CRITICAL_EDGE_PROFILES.json').read_text())['profiles']
T=set(source['spare_vertices']);assert T=={34,54}
candidates=[p for p in profiles if p['u']not in T and p['v']not in T and len(set(p['required_if_both_endpoints_pin'])|T)<=10]
assert len(candidates)==21
U={v for p in candidates for v in[p['u'],p['v']]};K={7,23,46,59}
certificate=[dict(edge=[p['u'],p['v']],critical_required=p['required_if_both_endpoints_pin'],
                  forced_unavailable_K=sorted(K&set(p['required_if_both_endpoints_pin'])))for p in candidates]
forcing=not(K&(T|U))and all(p['forced_unavailable_K']for p in certificate)
save('MINIMAL4_FORCING_CERTIFICATE.json',dict(T=sorted(T),K=sorted(K),candidate_endpoint_union=sorted(U),
    K_disjoint_from_all_possible_pins=not bool(K&(T|U)),edge_certificates=certificate,
    every_candidate_edge_forces_unavailable_K=all(p['forced_unavailable_K']for p in certificate)))
tested=disjoint=closed=0;solution=None;hist=collections.Counter();best=None;adj=None
if not forcing:
    for comb in itertools.combinations(candidates,4):
        tested+=1;ends={v for p in comb for v in[p['u'],p['v']]}
        if len(ends)!=8:continue
        disjoint+=1;S=T|ends
        required=T|{v for p in comb for v in p['required_if_both_endpoints_pin']}
        missing=required-S;hist[len(missing)]+=1
        if best is None or len(missing)<best['missing_count']:
            best=dict(edges=[[p['u'],p['v']]for p in comb],S=sorted(S),missing=sorted(missing),missing_count=len(missing))
        if missing:continue
        closed+=1
        if adj is None:
            adj=[set()for _ in range(106)]
            with(D/'source106.header.edges').open()as f:
                assert list(map(int,next(f).split()))==[106,582]
                for line in f:
                    u,v=map(int,line.split());adj[u].add(v);adj[v].add(u)
        cover=set(S)
        for u in S:cover|=adj[u]
        if len(cover)==106:
            solution=dict(deleted_edges=[[p['u'],p['v']]for p in comb],pins=sorted(S));break
if solution is not None:
    final=[set(v)for v in adj]+[set()]
    for u,v in solution['deleted_edges']:final[u].remove(v);final[v].remove(u)
    for v in solution['pins']:final[106].add(v);final[v].add(106)
    bad=[(u,v)for u in range(107)for v in range(u+1,107)if v not in final[u]and not(final[u]&final[v])]
    degrees=collections.Counter(map(len,final));assert not bad and degrees=={10:1,11:106}
    edges=[(u,v)for u in range(107)for v in sorted(final[u])if u<v];assert len(edges)==588
    with(D/'graph_d11_D2_n107_minimal4.edges').open('w')as f:
        f.write('107 588\n');f.writelines(f'{u} {v}\n'for u,v in edges)
    save('MINIMAL4_PARAMETERS.json',dict(n=107,m=588,Delta=11,D=2,source='source106.header.edges',**solution))
status='EXACT_NO_MINIMAL4_MATCHING_BY_UNAVAILABLE_CRITICAL_PIN_CERTIFICATE'if forcing else'SAT_MINIMAL4_CANDIDATE_107_EXACT_D2'if solution else'EXACT_NO_MINIMAL4_MATCHING_COMPLETE_ENUMERATION'
result=dict(status=status,source_n=106,source_m=582,source_profile_inherited='SOURCE_RESULT.json',
    new_vertex_degree=10,target_n=107,target_m=588,candidate_edges=len(candidates),potential_four_edge_combinations=math.comb(21,4),
    forcing_prediction_SUPPORTED=forcing,forcing_certificate='MINIMAL4_FORCING_CERTIFICATE.json',
    combinations_enumerated=tested,disjoint_combinations=disjoint if not forcing else None,
    critical_closed_combinations=closed,critical_closed_count_is_proved_not_enumerated=forcing,
    critical_missing_count_histogram=dict(hist),best_if_enumerated=best,solution=solution,
    complete_exact_scope='Onlydelete4matchingoldedges awayfromT,addonevertex adjacentexactlyT+8endpoints,nootherold-oldrepair',
    source_body_reads=0 if adj is None else 1,source_profile_or_BFS_repeated=False,old_geometry_field_rank_solver_Lean_query_paidreview_runs=0,
    candidate_graph_exported=solution is not None,candidate_common_neighbor_check_count=5671 if solution else 0,
    graph_parameter_Lean_increment=0,CPU_seconds=time.process_time()-started,CPU_budget_seconds=20,running=False)
save('MINIMAL4_RESULT.json',result)
save('MINIMAL4_TERMINAL.json',dict(status=status,running=False,CPU_seconds=result['CPU_seconds'],CPU_budget_seconds=20,
     candidate_graph_exported=solution is not None,broader106_to107_excluded=False))
save('MINIMAL4_HANDLE.json',dict(status=status,running=False,CPU_seconds=result['CPU_seconds']))
print(json.dumps(result))

import resource
resource.setrlimit(resource.RLIMIT_CPU,(8,8))
from pathlib import Path
import json,time
from collections import Counter
import networkx as nx
OUT=Path(__file__).resolve().parent;START=time.process_time();source=OUT.parent/'d6_rajiv441_orbit_mechanism/COORDINATES.json'
def save(n,x):(OUT/n).write_text(json.dumps(x,indent=2)+'\n')
triads=json.loads(source.read_text())['triads'];assert len(triads)==63 and all(len(L)==len(set(L))==3 for L in triads)
local=nx.Graph();local.add_nodes_from(range(126));local.add_edges_from((p,63+i) for i,L in enumerate(triads) for p in L)
assert local.number_of_edges()==189 and set(dict(local.degree()).values())=={3} and not nx.number_of_selfloops(local)
J=[17,27,-13,-59,-35,35,-11,13,-53,53,-27,21,57,11,-21,-57,59,-17]
lcf=nx.Graph();lcf.add_nodes_from(range(126));lcf.add_edges_from((i,(i+1)%126) for i in range(126));lcf.add_edges_from((i,(i+J[i%18])%126) for i in range(126))
assert lcf.number_of_edges()==189 and set(dict(lcf.degree()).values())=={3} and not nx.number_of_selfloops(lcf)
localedges={tuple(sorted(e)) for e in local.edges()};lcfedges={tuple(sorted(e)) for e in lcf.edges()};assert all(u%2!=v%2 for u,v in lcfedges)
save('BINDING_INPUT.json',{'local_source':str(source),'local_vertex_definition':'point0..62,line63+i','triads':triads,'local_edges':sorted(localedges),'LCF_offsets':J,'LCF_repeat':7,'LCF_edges':sorted(lcfedges),'n':126,'m':189,'local_degree_histogram':dict(Counter(dict(local.degree()).values())),'LCF_degree_histogram':dict(Counter(dict(lcf.degree()).values())),'isomorphism_calls_planned':1,'matching_graphs':0,'BFS':0})
save('checkpoint.json',{'status':'ONE_GRAPHMATCHER_RUNNING','CPU_seconds':time.process_time()-START})
matcher=nx.algorithms.isomorphism.GraphMatcher(local,lcf)
isomorphic=matcher.is_isomorphic()
if not isomorphic:
 save('WORKER_RESULT.json',{'status':'COMPLETE_SINGLE_BINDING_NOT_ISOMORPHIC','isomorphic':False,'CPU_seconds':time.process_time()-START,'matching_graphs':0,'BFS':0});print('NOT_ISOMORPHIC');raise SystemExit(0)
mapping=dict(matcher.mapping);inverse={v:k for k,v in mapping.items()}
assert len(mapping)==len(inverse)==126 and {tuple(sorted((mapping[u],mapping[v]))) for u,v in localedges}==lcfedges
sigma=[(v+18)%126 for v in range(126)];assert {tuple(sorted((sigma[u],sigma[v]))) for u,v in lcfedges}==lcfedges
assert all(sigma[v]!=v for v in range(126))
cycles=[]
for r in range(18):
 C=[(r+18*s)%126 for s in range(7)];assert len(set(C))==7 and sigma[C[-1]]==r;cycles.append(C)
assert {v for C in cycles for v in C}==set(range(126))
parity=[C[0]%2 for C in cycles];assert all(len({v%2 for v in C})==1 for C in cycles) and Counter(parity)==Counter({0:9,1:9})
local_sigma=[inverse[sigma[mapping[v]]] for v in range(126)];assert {tuple(sorted((local_sigma[u],local_sigma[v]))) for u,v in localedges}==localedges
save('ISOMORPHISM.json',{'status':'EXPLICIT_ALL189_EDGES_MATCH','local_to_LCF':[mapping[v] for v in range(126)],'LCF_to_local':[inverse[v] for v in range(126)],'local_parts':'point0..62,line63..125','LCF_point_part_parities':sorted({mapping[v]%2 for v in range(63)}),'local_line_part_parities':sorted({mapping[v]%2 for v in range(63,126)})})
save('AUTOMORPHISM.json',{'status':'ALL189_EDGE_IMAGES_MATCH','LCF_permutation':sigma,'formula':'v->v+18 mod126','order':7,'cycles':cycles,'orbit_roots':list(range(18)),'cycle_parities':parity,'bipartite_orbit_counts':{'even':9,'odd':9},'conjugated_local_permutation':local_sigma,'automorphism_not_fullAut_group':'Only this one explicit C7 checked, not an Autgroup computation.'})
(OUT/'source126.edges').write_text('126 189\n'+''.join(f'{u} {v}\n' for u,v in sorted(lcfedges)))
r={'status':'COMPLETE_EXACT_SOURCE_LCF_ISOMORPHISM_AND_C7','isomorphic':True,'n':126,'m':189,'degree':3,'isomorphism_calls':1,'actual189_edge_map_match':True,'explicit_C7_edge_permutation_match':True,'C7_order':7,'C7_cycles':18,'cycle_length':7,'bipartite_orbit_counts':[9,9],'source_D6_girth12':'Inherited localGH2proof/primarydescription; no freshdistance orcyclecount check','CPU_seconds':time.process_time()-START,'source_BFS':0,'diameter_computations':0,'matching_graphs':0,'solver_calls':0,'SA_calls':0}
save('WORKER_RESULT.json',r);save('checkpoint.json',{'status':r['status'],'isomorphism_calls':1,'CPU_seconds':time.process_time()-START});print(json.dumps(r),flush=True)

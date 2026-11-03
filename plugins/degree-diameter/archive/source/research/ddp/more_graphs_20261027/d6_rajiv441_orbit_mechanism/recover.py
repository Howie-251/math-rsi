"""Recover Rajiv441 source flags directly from its three orbit edge sets.
No source diameter BFS, SAT or new graph optimization.
"""
import collections,json,pathlib,time,resource
resource.setrlimit(resource.RLIMIT_CPU,(179,180))
P=pathlib.Path(__file__).resolve().parent;ROOT=P.parents[3];start=time.process_time()
SRC=ROOT/'research/ddp/second_mechanism/rajiv441.edges'
def save(n,d):(P/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
save('PREDICTION.json',{'prediction_id':'P_RAJIV441_QUOTA_AND_FLAGS','frozen_before_source_adjacency_measurement':True,
 'supplied_hypothesis_to_test':'A63nonisotropicpoints;Ahas3B+3C;B/Cbothtriangles,3cross+1A.',
 'paper_based_prediction':'The supplieddegreeprofile isrefuted: AppendixA predicts A->B6,B->A2/C4,C->B4/C2; only C hasinternaldegree2.',
 'flag_prediction':'Project eachB toits2Aneighbors. The189Bshould form all edges ofa simple6regular63pointgraph decomposed into63triads,3triads/point. LabelB by(triad,omittedpoint). ForC,4Bneighbor marks should consist oftwo points eachtwice, determinea unique triad anditsomittedmark;Cinternaltriangles sharethat triad. CrossB(P,L)-C(Q,M) iffP inM\{Q},L!=M.',
 'scope':'One actual knownsource, geometric reconstruction and scalarq4arithmetic onlyif model matches. Noq4newgraph/BFS/solver/search implied.',
 'workers':1,'CPU_budget_seconds':180})
edges=[]
for line in SRC.read_text().splitlines():
 if line.strip() and not line.startswith('#'):edges.append(tuple(map(int,line.split())))
adj=[set()for _ in range(441)]
for u,v in edges:adj[u].add(v);adj[v].add(u)
A=set(range(63));B=set(range(63,252));C=set(range(252,441));parts=[A,B,C]
quota=[]
for group in parts:quota.append(collections.Counter(tuple(len(adj[v]&part)for part in parts)for v in group))
components=[];remain=set(C)
while remain:
 seed=min(remain);comp={seed};stack=[seed]
 while stack:
  v=stack.pop()
  for w in adj[v]&C:
   if w not in comp:comp.add(w);stack.append(w)
 remain-=comp;components.append(sorted(comp))
profile={'status':'SOURCE_ADJACENCY_PROFILE_COMPLETE','source_path':str(SRC.relative_to(ROOT)),'source_n':441,'source_m':len(edges),
 'parts':{'A':[0,62],'B':[63,251],'C':[252,440]},'per_orbit_neighbor_counts':[{','.join(map(str,k)):n for k,n in row.items()}for row in quota],
 'C_internal_component_sizes':dict(collections.Counter(map(len,components))),'C_components':components,
 'supplied_hypothesis_verdict':'REFUTED','paper_quota_matched':quota==[collections.Counter({(0,6,0):63}),collections.Counter({(2,0,4):189}),collections.Counter({(0,4,2):189})],
 'source_BFS':0,'CPU_seconds':time.process_time()-start}
save('SOURCE_PROFILE.json',profile);print('PROFILE',profile['per_orbit_neighbor_counts'],profile['C_internal_component_sizes'],flush=True)
# First geometric prediction: B is an edge of a point-triad geometry.
bpairs={b:tuple(sorted(adj[b]&A))for b in B};pair_to_B={pair:b for b,pair in bpairs.items()}
H=[set()for _ in range(63)]
for a,b in bpairs.values():H[a].add(b);H[b].add(a)
triads=sorted({tuple(sorted((a,b,c)))for a,b in pair_to_B for c in H[a]&H[b]})
triad_of_pair={pair:[T for T in triads if set(pair)<=set(T)]for pair in pair_to_B}
valid_B=len(pair_to_B)==189 and len(triads)==63 and all(len(Ts)==1 for Ts in triad_of_pair.values()) and all(len(x)==6 for x in H)
if not valid_B:
 save('RESULT.json',{'status':'FLAG_RECONSTRUCTION_REFUTED_AT_B','profile':profile,'B_pair_unique_count':len(pair_to_B),'triad_count':len(triads),'pending':[]});raise SystemExit('B hypothesis refuted')
Tindex={T:i for i,T in enumerate(triads)};incident={a:[T for T in triads if a in T]for a in A}
blabel={}
for b,pair in bpairs.items():
 T=triad_of_pair[pair][0];p=next(iter(set(T)-set(pair)));blabel[b]=(p,Tindex[T])
clabel={};fail=[]
for c in sorted(C):
 marks=collections.Counter(blabel[b][0]for b in adj[c]&B)
 if len(marks)!=2 or sorted(marks.values())!=[2,2]:fail.append({'C':c,'reason':'Bmarksnot2+2','marks':dict(marks)});continue
 pair=tuple(sorted(marks));Ts=triad_of_pair.get(pair,[])
 if len(Ts)!=1:fail.append({'C':c,'reason':'Bmarksnotatr i ad','marks':dict(marks)});continue
 T=Ts[0];q=next(iter(set(T)-set(pair)));clabel[c]=(q,Tindex[T])
if fail or len(set(clabel.values()))!=189:
 save('RESULT.json',{'status':'FLAG_RECONSTRUCTION_REFUTED_AT_C','profile':profile,'B_prediction':True,'C_failures':fail,'unique_C_labels':len(set(clabel.values())),'pending':[]});raise SystemExit('C hypothesis refuted')
cbylabel={lab:c for c,lab in clabel.items()}
pred=set()
for b,(p,t)in blabel.items():
 for M in incident[p]:
  if Tindex[M]==t:continue
  for q in M:
   if q!=p:pred.add((b,cbylabel[q,Tindex[M]]))
actual={(b,c)for b in B for c in adj[b]&C}
triangle_match=all(len({clabel[c][1]for c in comp})==1 and {clabel[c][0]for c in comp}==set(triads[clabel[comp[0]][1]]) for comp in components)
res={'status':'COMPLETE_SOURCE_FLAG_MECHANISM_RECOVERED'if pred==actual and triangle_match else'FLAG_CROSS_RULE_REFUTED',
 'source_path':str(SRC.relative_to(ROOT)),'source_n':441,'source_m':1323,'supplied_hypothesis':'REFUTED','paper_quota':'MATCH','flag_prediction':'SUPPORTED'if pred==actual and triangle_match else'REFUTED',
 'A_points':63,'triads':63,'triads_per_A':dict(collections.Counter(len(incident[a])for a in A)),'B_labels':189,'C_labels':189,'B_projection_degree':dict(collections.Counter(map(len,H))),
 'AB_edges':378,'BC_edges':len(actual),'CC_edges':189,'predicted_BC_equals_actual':pred==actual,'C_triangles_share_triad':triangle_match,
 'geometric_rule':'A=pointsa; B/C=two copies of flags(P,L),P inL. A-B adjacent iff a inL\{P}; B(P,L)-C(Q,M) iff P inM\{Q} andL!=M; CflagswithsameM formtriangle.',
 'q3_unitary_coordinate_identification':'Notyettested;pointtriad geometryrecoveredwithoutassuming Hermitian coordinates.',
 'source_BFS':0,'new_graphs':0,'CPU_seconds':time.process_time()-start,'pending':[]}
save('COORDINATES.json',{'A_adjacency':{str(a):sorted(H[a])for a in A},'triads':triads,'B_flags':{str(b):{'point':p,'triad':t,'A_neighbors':list(bpairs[b])}for b,(p,t)in blabel.items()},'C_flags':{str(c):{'point':p,'triad':t,'B_neighbors':sorted(adj[c]&B)}for c,(p,t)in clabel.items()},'C_triangles':components})
save('RESULT.json',res);print('FLAGS',res['status'],'triads',len(triads),'BCmatch',pred==actual,'triangle',triangle_match,'CPU',res['CPU_seconds'])

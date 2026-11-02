from pathlib import Path
from collections import Counter
import json,lzma,time

P=Path(__file__).resolve().parent;t=time.process_time();N=66430
with lzma.open(P/'duality_source/tau.txt.xz','rt') as f:tau=list(map(int,f.read().split()))
assert len(tau)==2*N
orb=[-1]*(2*N);reps=[];members=[]
for p in range(2*N):
 if orb[p]>=0:continue
 idx=len(reps);reps.append(p);row=[];u=p
 while orb[u]<0:orb[u]=idx;row.append(u);u=tau[u]
 assert u==p
 members.append(row)
assert len(reps)==33397
h3fold=[i for i,r in enumerate(reps) if tau[tau[r]]==r]
genericfold=[i for i,r in enumerate(reps) if tau[tau[r]]!=r]
assert len(h3fold)==364 and len(genericfold)==33033
hi={v:i for i,v in enumerate(h3fold)};qi={v:i for i,v in enumerate(genericfold)}
adj=[[] for _ in reps]
with lzma.open(P/'duality_source/graph_d10k5_n33397.edges.xz','rt') as f:
 n,m=map(int,next(f).split());assert(n,m)==(33397,166425)
 for line in f:
  u,v=map(int,line.split());adj[u].append(v);adj[v].append(u)
Q=[[qi[v] for v in adj[u] if v in qi] for u in genericfold]
h_of=[next((hi[v] for v in adj[u] if v in hi),-1) for u in genericfold]
HN=[[hi[v] for v in adj[u] if v in hi] for u in h3fold]
HQ=[[qi[v] for v in adj[u] if v in qi] for u in h3fold]
absolute=[len(row)==3 for row in HN]
assert Counter(map(len,Q))=={9:1092,10:31941}
assert all(len(row)==3 for row in HQ) and sum(absolute)==28
assert all(sum(v in hi for v in adj[u])<=1 for u in genericfold)
W=json.loads((P/'partial_fold_source/witnesses/pf_d12_k5_n41699.json').read_text())
def bits(s):return [(b>>j)&1 for b in bytes.fromhex(s) for j in range(7,-1,-1)][:33033]
sp=bits(W['split']);co=bits(W['colour']);ch=W['h3_twins'];state=[(1+co[i]) if sp[i] else 0 for i in range(33033)]
assert sum(sp)==7959 and sum(ch)==280 and len(W['pad'])==63
generic_degree=[]
for u in range(33033):
 load=sum(sp[v] if not sp[u] else (sp[v] and co[v]==co[u]) for v in Q[u])
 generic_degree.append(10+load+(ch[h_of[u]] if h_of[u]>=0 else 0))
hdegree=[7-int(absolute[h])+sum(sp[u] for u in HQ[h])+sum(ch[k] for k in HN[h]) for h in range(364)]
labels=[];kind_by_label={};degree_by_label={}
for i,fold in enumerate(genericfold):
 p=reps[fold];pts=[p,tau[tau[p]]] if sp[i] else [p]
 for pp in pts:labels.append(pp);kind_by_label[pp]='generic_split' if sp[i] else 'generic_merged';degree_by_label[pp]=generic_degree[i]
for h,fold in enumerate(h3fold):
 p=reps[fold];labels.append(p);kind_by_label[p]='H3';degree_by_label[p]=hdegree[h]
labels.sort();num={p:i for i,p in enumerate(labels)}
core_kind=[kind_by_label[p] for p in labels];core_degree=[degree_by_label[p] for p in labels]
for h,fold in enumerate(h3fold):
 core_kind.extend(['H3_copy']*ch[h]);core_degree.extend([hdegree[h]]*ch[h])
core_n=len(core_degree);assert core_n==41636 and max(core_degree)<=12
final_degree=[0]*41699;core_adj=[set() for _ in range(core_n)];pad_adj=[set() for _ in range(63)]
with lzma.open(P/'partial_fold_source/graph_d12k5_n41699.edges.xz','rt') as f:
 n,m=map(int,next(f).split());assert n==41699
 for line in f:
  u,v=map(int,line.split());final_degree[u]+=1;final_degree[v]+=1
  if u<core_n and v<core_n:core_adj[u].add(v);core_adj[v].add(u)
  elif u>=core_n:pad_adj[u-core_n].add(v)
  else:pad_adj[v-core_n].add(u)
assert [len(x) for x in core_adj]==core_degree
assert all(pad_adj[i]==core_adj[v] for i,v in enumerate(W['pad']))
assert max(final_degree)==12
def summary(deg):return dict(vertices=len(deg),degree_histogram=dict(sorted(Counter(deg).items())),free_degree_slots=sum(12-d for d in deg),vertices_with_free_slot=sum(d<12 for d in deg))
groups={}
for k in sorted(set(core_kind)):
 ids=[i for i,t in enumerate(core_kind) if t==k]
 groups[k]=dict(core=summary([core_degree[i] for i in ids]),after_padding=summary([final_degree[i] for i in ids]))
groups['padding_twins']=dict(after_padding=summary(final_degree[core_n:]))
boundary={u for u,h in enumerate(h_of) if h>=0};radius1=boundary|{v for u in boundary for v in Q[u]}
stats=dict(status='SOURCE_WITNESS_LOCAL_LOADS_REPRODUCED',Q_vertices=33033,Q_edges=sum(map(len,Q))//2,Q_degree_histogram=dict(Counter(map(len,Q))),H3_vertices=364,H3_edges=sum(map(len,HN))//2,H3_absolute_points=sum(absolute),H3_to_Q_edges=sum(map(len,HQ)),split_fibers=sum(sp),split_color_histogram=dict(Counter(co[i] for i in range(33033) if sp[i])),H3_extra_copies=sum(ch),H3_copy_count_histogram=dict(Counter(ch)),padding_twins=len(W['pad']),core_vertices=core_n,final_vertices=41699,core=summary(core_degree),final=summary(final_degree),groups=groups,padding_attach_edge_count=sum(map(len,pad_adj)),padding_twin_base_vertices=W['pad'],Q_boundary_vertices=len(boundary),Q_boundary_and_one_Q_neighborhood=len(radius1),target_order=42343,target_degree=12,current_saved_record=42342,need_gain_after_existing_padding=644,target_core_split_plus_H3_if_no_padding=8946,current_core_split_plus_H3=sum(sp)+sum(ch),need_core_gain_if_no_padding=707,PSL_2_8_orbit_partition='NOT_INCLUDED_IN_AUTHOR_DEPOSITS',PSL_2_8_orbit_number=None,PSL_2_8_smallest_orbit=None,full_BFS_performed=False,geometry_reconstruction_performed=False,CPU_seconds=time.process_time()-t)
(P/'Q_data.json').write_text(json.dumps(dict(Q=Q,H3_neighbors=h_of,H3_graph=HN,H3_generic_neighbors=HQ,H3_absolute=absolute,generic_fold_ids=genericfold,generic_point_representatives=[reps[v] for v in genericfold],H3_fold_ids=h3fold,H3_point_representatives=[reps[v] for v in h3fold]),separators=(',',':'))+'\n')
(P/'witness12_state.json').write_text(json.dumps(dict(states=state,state_meaning=['merged','split_color0','split_color1'],h3_extra_copies=ch,pad=W['pad'],source_record='23056128',source_witness='partial_fold_source/witnesses/pf_d12_k5_n41699.json',split_color_counts=stats['split_color_histogram']),separators=(',',':'))+'\n')
(P/'structure_check.json').write_text(json.dumps(stats,indent=2)+'\n')
print(json.dumps(stats,indent=2))

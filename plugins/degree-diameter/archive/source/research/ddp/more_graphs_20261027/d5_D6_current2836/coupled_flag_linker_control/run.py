"""One frozen coupled flag/linker subdivision; no parameter grid or old-source BFS."""
from pathlib import Path
from collections import deque,Counter
import json,time
OUT=Path(__file__).resolve().parent;SOURCE=OUT.parent/'source2836.author.edges.txt';start=time.process_time()
n=2836;E=set()
for line in SOURCE.read_text().splitlines():
 if not line or line.startswith('#'):continue
 E.add(tuple(sorted(map(int,line.split()))))
adj=[set() for _ in range(n)]
for u,v in E:adj[u].add(v);adj[v].add(u)
F=sorted(e for e in E if e[0]>=2730)
f1=F[0];f2=next(e for e in F if not set(e)&set(f1))
flags=[]
for e in [f1,f2]:
 endpoint=e[0];p=next(v for v in adj[endpoint] if v<1365)
 eligible=sorted(v for v in adj[p] if 1365<=v<2730 and (p,v) not in flags)
 assert eligible,'Frozen control has no eligible unselected flag; no alternate scope.'
 flags.append((p,eligible[0]))
z,w=n,n+1;deleted=[flags[0],flags[1],f1,f2]
A=[*flags[0],*f1];B=[*flags[1],*f2]
added=[tuple(sorted((z,x))) for x in A]+[tuple(sorted((w,x))) for x in B]+[(z,w)]
pred={'status':'FROZEN_BEFORE_RADIUS_COMPUTATION','target_Delta':5,'target_D':6,'savedL':2836,'source_n':n,'candidate_n':2838,'rule':'Pick first two lexicographic vertex-disjoint F edges. For each smaller endpoint, take its original H4 flag point and smallest still-unsubdivided incident line; use the same new vertex to subdivide that H4 incidence and that F edge, then join the two new vertices.','intuition':'Each new root is attached to both ends of a working linker edge and shares a point with one of those existing flags; the buddy supplies another linker pair. Test whether these complementary local access routes already suffice globally.','prediction':'Both new roots have eccentricity at most6. This is necessary, not sufficient, for final diameter6.','deleted_edges':deleted,'added_edges':added,'new_old_neighbor_sets':{'z':A,'w':B},'fixed_controls':1,'stop':'First failed new root stops; no alternate flags, F edges, pair orientation, or helper variants. Passing roots alone does not establish old-old coverage.','whole_source_BFS':0}
(OUT/'PREDICTION.json').write_text(json.dumps(pred,indent=2)+'\n')
newE=(E-set(deleted))|set(added)
g=[set() for _ in range(n+2)]
for u,v in newE:g[u].add(v);g[v].add(u)
assert len(newE)==7095 and all(len(row)==5 for row in g)
assert all(u not in row for u,row in enumerate(g))
assert all(len(set(row))==5 for row in g)
roots=[];failure=None
for r in [z,w]:
 d=[-1]*(n+2);parent=[-1]*(n+2);d[r]=0;q=deque([r])
 while q:
  u=q.popleft()
  for v in g[u]:
   if d[v]<0:d[v]=d[u]+1;parent[v]=u;q.append(v)
 missing=[v for v in range(n) if d[v]<0 or d[v]>6]
 row={'root':r,'visited':sum(x>=0 for x in d),'eccentricity':max(d),'old_targets_outside_R6':len(missing),'missing_by_type':dict(Counter('point' if v<1365 else 'line' if v<2730 else 'old_flag' for v in missing)),'missing_sample':missing[:20]}
 roots.append(row)
 if missing:
  t=missing[0];path=[];v=t
  while v>=0:path.append(v);v=parent[v]
  path.reverse()
  # One exact diagnostic in the source-minus-four-edges graph, not its diameter.
  g0=[set(row) for row in adj]
  for a,b in deleted:g0[a].remove(b);g0[b].remove(a)
  ds=[-1]*n;ds[t]=0;queue=deque([t])
  while queue:
   u=queue.popleft()
   for v in g0[u]:
    if ds[v]<0:ds[v]=ds[u]+1;queue.append(v)
  distA=min(ds[v] for v in A);distB=min(ds[v] for v in B)
  expected=min(1+(distA if r==z else distB),2+(distB if r==z else distA))
  assert expected==d[t]
  failure={'root':r,'target':t,'actual_distance':d[t],'path':path,'source_minus_cuts_distance_to_A':distA,'source_minus_cuts_distance_to_B':distB,'exact_new_root_distance_formula':expected}
  break
result={'status':'ONE_FROZEN_CONTROL_NEW_ROOT_REFUTED_STOP' if failure else 'NEW_ROOT_CONDITION_PASSED_OLD_OLD_UNCHECKED','target_Delta':5,'target_D':6,'savedL':2836,'source_n':2836,'candidate_n':2838,'candidate_m':7095,'simple':True,'degree_histogram':dict(Counter(map(len,g))),'connected':all(x['visited']==n+2 for x in roots),'candidate_global_D':None,'ordinary_bad_unordered_pairs':None,'deleted_edges':deleted,'added_edges':added,'roots':roots,'failure':failure,'old_old_coverage_checked':False,'prediction':'REFUTED' if failure else 'SUPPORTED_NECESSARY_CONDITION_ONLY','source_D6_BFS_repeated':0,'candidate_new_root_BFS':len(roots),'diagnostic_source_minus_cuts_single_target_BFS':int(failure is not None),'controls_evaluated':1,'remaining_control_grid':0,'CPU_seconds':time.process_time()-start,'scope':'Exactly this frozen choice of two incidences and two linker edges; no claim excluding other H4 flag/linker surgeries.'}
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'terminal.json').write_text(json.dumps({'status':result['status'],'running':False,'pending':[],'scope':result['scope'],'prediction':result['prediction']},indent=2)+'\n')
print(json.dumps(result))

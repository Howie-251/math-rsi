"""One fixed controlled lift, source recipe already recovered without source BFS."""
from pathlib import Path
from collections import Counter,deque
import json,time
OUT=Path(__file__).resolve().parent
assert not (OUT/'CONTROL_RESULT.json').exists()
START=time.process_time()
pred=json.loads((OUT/'PREDICTION_PROPOSAL.json').read_text())
pred.update(status='FROZEN_ACTUAL_CONTROL_BEFORE_NEW_ADJACENCY',prediction='The one specified p139/r6 centered-literal lift has global diameter at most9; all three deck identity-root R9 balls cover all9591 vertices.',state='AUTHORIZED_SINGLE_FIXED_CONTROL',budget_CPU_seconds=3,stop='Only this one candidate; stop on first failing root. No free translations/other r/prime.',source_BFS=0)
(OUT/'PREDICTION.json').write_text(json.dumps(pred,indent=2)+'\n')
p=139;m=23;r=6;GN=p*m;N=3*GN
assert pow(r,m,p)==1 and r!=1
rp=[pow(r,x,p) for x in range(m)]
def inv(g):
 a,c=g
 return (-a)%m,(-pow(r,(-a)%m,p)*c)%p
A=(3,8);B=(11,2);C=(6,-12);D=(4,-2)
darts=[(0,0,A),(0,0,inv(A)),(1,1,B),(1,1,inv(B)),(2,2,C),(2,2,inv(C)),
 (0,1,(0,0)),(1,0,(0,0)),(0,2,(0,0)),(2,0,(0,0)),(1,2,D),(2,1,inv(D))]
reverse=[1,0,3,2,5,4,7,6,9,8,11,10]
for i,(_,_,g) in enumerate(darts):
 assert tuple(x%mod for x,mod in zip(inv(g),[m,p]))==tuple(x%mod for x,mod in zip(darts[reverse[i]][2],[m,p]))
ports=[[i for i,d in enumerate(darts) if d[0]==b] for b in range(3)]
comm=((pow(r,3,p)-1)*2-(pow(r,11,p)-1)*8)%p
assert comm==7
adj=[]
for base in range(3):
 for y in range(p):
  for x in range(m):
   row=[]
   for i in ports[base]:
    _,to,(a,c)=darts[i]
    row.append(to*GN+(x+a)%m+m*((y+rp[x]*c)%p))
   u=base*GN+x+m*y
   assert len(set(row))==4 and u not in row
   adj.append(row)
assert len(adj)==N and all(u in adj[v] for u,row in enumerate(adj) for v in row)
roots=[]
for base in range(3):
 root=base*GN;dist=[-1]*N;par=[-1]*N;dist[root]=0;queue=deque([root])
 while queue:
  u=queue.popleft()
  for v in adj[u]:
   if dist[v]<0:dist[v]=dist[u]+1;par[v]=u;queue.append(v)
 visited=sum(x>=0 for x in dist);ecc=max(dist)
 missing=[i for i,d in enumerate(dist) if d<0 or d>9]
 rr={'base':base,'root':root,'visited':visited,'eccentricity':ecc,'R9_missing':len(missing),'distance_histogram':dict(sorted(Counter(dist).items()))}
 slots=Counter()
 for v in missing:
  b,g=divmod(v,GN);slots[b,g%m]+=1
 rr['R9_missing_by_base_phase']=[{'target_base':b,'phase':x,'missing':slots[b,x]} for b in range(3) for x in range(m)]
 if missing and visited==N:
  v=missing[0];path=[];w=v
  while w>=0:path.append(w);w=par[w]
  path.reverse()
  rr['first_missing_witness']={'vertex':v,'base':v//GN,'phase':v%GN%m,'field':v%GN//m,'distance':dist[v],'exact_shortest_path':path}
 roots.append(rr)
 print(json.dumps({'base':base,'visited':visited,'eccentricity':ecc,'R9_missing':len(missing)}),flush=True)
 if missing:break
assert roots[0]['visited']==N
hit=len(roots)==3 and all(x['R9_missing']==0 for x in roots)
recipe={'source_literal':'source3243.raw_adj.txt','source_recipe_all12972arcs_MATCH':True,'source_BFS':0,'n':N,'m':2*N,'degree':4,'base_vertices':3,'group_order':GN,
 'group':'F139 semidirect C23','rightlaw':'(x,y)*(a,c)=(x+a mod23,y+6^x*c mod139)',
 'vertex_encoding':'base*3197+x+23*y','primitive_action_r':r,'action_order':23,
 'darts':[{'id':i,'from':d[0],'to':d[1],'phase':d[2][0]%m,'translation':d[2][1]%p,'reverse':reverse[i]} for i,d in enumerate(darts)],
 'positive_centered_integer_voltages':{'loop0':[3,8],'loop1':[11,2],'loop2':[6,-12],'cross12':[4,-2]},
 'connectedness_argument':'Identity links connect base copies. Loop0/1 commutator has nonzero field translation7; prime normal139 generated, and phase3 generatesC23.',
 'deck_argument':'Every dart acts by right multiplication; left deck translations preserve edges and are transitive separately in each of three base fibres.'}
(OUT/'CONTROL_RECIPE.json').write_text(json.dumps(recipe,indent=2)+'\n')
result={'status':'FIRST_HIT_REQUIRES_PARENT_ACCEPTANCE' if hit else 'SINGLE_FIXED_CONTROL_REFUTED','hit':hit,'n':N,'m':2*N,'degree':4,'simple':True,'undirected':True,'connected':True,
 'target_Delta':4,'target_D':9,'savedL':7884,'actual_global_D':max(x['eccentricity'] for x in roots) if len(roots)==3 else None,
 'actual_global_D_lower_bound':max(x['eccentricity'] for x in roots),'ordinary_bad_unordered_pairs':None,'roots_checked':len(roots),'roots':roots,
 'all_three_root_BFS_complete':len(roots)==3,'source_BFS':0,'actual_graphs_built':1,'edgefiles_exported':0,'unattempted_candidates':0,
 'prediction':'SUPPORTED' if hit else 'REFUTED','CPU_seconds':time.process_time()-START,'compile_CPU_seconds':0,
 'pending':['Parent independent verification'] if hit else []}
if hit:
 edge=OUT/'graph_d4_D9_n9591.edges'
 with edge.open('w') as f:
  f.write(f'{N} {2*N}\n');count=0
  for u,row in enumerate(adj):
   for v in sorted(row):
    if u<v:f.write(f'{u} {v}\n');count+=1
 assert count==2*N
 result['edgefiles_exported']=1;result['graph_file']=str(edge)
result['CPU_seconds']=time.process_time()-START
(OUT/'CONTROL_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','roots_checked','actual_global_D','actual_global_D_lower_bound','CPU_seconds','pending']}),flush=True)

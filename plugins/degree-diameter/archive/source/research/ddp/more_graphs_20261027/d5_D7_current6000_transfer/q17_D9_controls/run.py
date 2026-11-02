"""Four frozen prime-field embeddings. Never rebuild/revalidate source6000."""
from collections import Counter, deque
from pathlib import Path
import json, time

OUT=Path(__file__).resolve().parent
assert not (OUT/'RESULT.json').exists()
START=time.process_time()
pred=json.loads((OUT/'PREDICTION.json').read_text())
assert pred['lambdas']==[2,8,9,15]
P=17; VN=P*P; GN=120*VN; N=2*GN
I=(1,0,0,1); K=(1,16,0,16); beta=(0,16,1,16)
def mm(A,B):
 return tuple((A[2*i]*B[j]+A[2*i+1]*B[2+j])%P for i in range(2) for j in range(2))
def mv(A,v):
 x,y=v%P,v//P
 return (A[0]*x+A[1]*y)%P+P*((A[2]*x+A[3]*y)%P)
def vn(v):return (-v%P)+P*((- (v//P))%P)
def hm(h,k):
 u,v=h%3,h//3;a,b=k%3,k//3
 return (u+(-a if v%2 else a))%3+3*((v+b)%8)
def hi(h):
 u,v=h%3,h//3
 return ((u if v%2 else -u)%3)+3*((-v)%8)
chi=[pow(2,j,5) for j in range(8)]
def qm(q,r):
 z,h=q%5,q//5;w,k=r%5,r//5
 return (z+chi[h//3]*w)%5+5*hm(h,k)
def qi(q):
 z,h=q%5,q//5;k=hi(h)
 return (-chi[k//3]*z)%5+5*k
vadd=[[(a%P+b%P)%P+P*((a//P+b//P)%P) for b in range(VN)] for a in range(VN)]
assert all((x*x+x+1)%P for x in range(P))
qvol=[0,66,74,114,22,15,105,69,71]
ports=[[(1,0),(1,1),(1,3),(0,5),(0,6)],[(0,0),(0,2),(0,4),(1,7),(1,8)]]
models=[];reports=[]
(OUT/'RUN_HANDLE.json').write_text(json.dumps({'status':'FOUR_Q17_CONTROLS_RUNNING','budget_CPU_seconds':10},indent=2)+'\n')
for lam in [2,8,9,15]:
 cs=time.process_time()
 alpha=tuple(lam*x%P for x in K)
 ap=[I];bp=[I]
 for _ in range(8):ap.append(mm(ap[-1],alpha))
 for _ in range(3):bp.append(mm(bp[-1],beta))
 assert ap[8]==bp[3]==I and ap[4]!=I and bp[1]!=I
 assert mm(alpha,beta)==mm(bp[2],alpha)
 rho=[mm(bp[u],ap[v]) for v in range(8) for u in range(3)]
 assert all(mm(rho[h],rho[k])==rho[hm(h,k)] for h in range(24) for k in range(24))
 def gm(g,k):
  nv,q=g%VN,g//VN;nw,r=k%VN,k//VN
  return vadd[nv][mv(rho[q//5],nw)]+VN*qm(q,r)
 def gi(g):
  nv,q=g%VN,g//VN
  return vn(mv(rho[hi(q//5)],nv))+VN*qi(q)
 vv=[0,P,0,1+P*16,0,0,0,2*P,0]
 for pos in [1,3,5,7]:
  g=VN*qvol[pos]+vv[pos];ng=gi(g)
  assert ng//VN==qvol[pos+1]
  vv[pos+1]=ng%VN
  assert gm(g,ng)==gm(ng,g)==0
 volts=[VN*qvol[j]+vv[j] for j in range(9)]
 orders=[]
 for g in volts:
  cur=0;k=0
  while True:
   cur=gm(cur,g);k+=1
   if cur==0:break
   assert k<=1000
  orders.append(k)
 assert orders==[1,30,30,8,8,8,8,30,30]
 qnext=[[qm(q,r) for r in qvol] for q in range(120)]
 shifts=[[mv(rho[h],v) for v in vv] for h in range(24)]
 graph=[]
 for node in range(N):
  base,g=divmod(node,GN);nv,q=g%VN,g//VN;h=q//5
  row=[target*GN+vadd[nv][shifts[h][j]]+VN*qnext[q][j] for target,j in ports[base]]
  assert len(set(row))==5 and node not in row
  graph.append(row)
 assert all(u in graph[v] for u,row in enumerate(graph) for v in row)
 roots=[]
 for root in [0,GN]:
  dist=[-1]*N;dist[root]=0;queue=deque([root])
  while queue:
   u=queue.popleft()
   for v in graph[u]:
    if dist[v]<0:
     dist[v]=dist[u]+1;queue.append(v)
  visited=sum(d>=0 for d in dist)
  roots.append({'root':root,'visited':visited,'eccentricity':max(dist),'R9_missing':sum(d<0 or d>9 for d in dist),'distance_histogram':dict(sorted(Counter(dist).items()))})
 connected=all(r['visited']==N for r in roots)
 D=max(r['eccentricity'] for r in roots) if connected else None
 hit=connected and D<=9
 report={'status':'POSITIVE_REQUIRES_PARENT_ACCEPTANCE' if hit else 'FIXED_CONTROL_FAILED','lambda':lam,
  'n':N,'m':N*5//2,'degree':5,'simple':True,'undirected':True,'connected':connected,'actual_global_D':D,
  'accepted_D9':hit,'ordinary_bad_unordered_pairs':None,'alpha':list(alpha),'beta':list(beta),
  'voltage_ids':volts,'voltage_orders':orders,'roots':roots,'complete_new_orbit_root_BFS':2,'old_source_BFS':0}
 model={'lambda':lam,'alpha':list(alpha),'alpha_order':8,'beta_order':3,'inversion_relation':True,
  'rho_Hlaw_all576':True,'beta_eigenvalues_in_F17':0,'positive_orders_Y_A_B_D':[8,30,8,30],'true_new_inverses':True}
 if hit:
  edge=OUT/f'graph_d5_D9_n69360_lambda{lam}.edges'
  with edge.open('w') as f:
   f.write(f'{N} {N*5//2}\n');m=0
   for u,row in enumerate(graph):
    for v in sorted(row):
     if u<v:f.write(f'{u} {v}\n');m+=1
  assert m==N*5//2
  report['graph_file']=str(edge)
 report['CPU_seconds']=time.process_time()-cs
 (OUT/f'lambda{lam}.RESULT.json').write_text(json.dumps(report,indent=2)+'\n')
 reports.append(report);models.append(model)
 print(json.dumps({'lambda':lam,'connected':connected,'actual_global_D':D,'R9_missing':[r['R9_missing'] for r in roots],'CPU_seconds':report['CPU_seconds']}),flush=True)
 if hit:break
 assert time.process_time()-START<9.5
model={'group':'(F17^2 x C5) semidirect (C3 semidirect C8)','rightlaw':'(V,z,h)(W,d,k)=(V+rho(h)W,z+2^v*d,hk)',
 'Hlaw':'(u,v)(a,b)=(u+(-1)^v*a mod3,v+b mod8)','vertex_encoding':'base*34680+289*(z+5*(u+3v))+(x+17y)',
 'qvol_ids':qvol,'ports':ports,'n':N,'m':N*5//2,'degree':5,'deck_orbits':2,'beta':list(beta),
 'normal_VA':[0,1],'normal_VB':[1,16],'normal_VD':[0,2],'source_positive_orders_Y_A_B_D':[8,30,8,30],
 'models':models,'leftdeck_argument':'Adjacency uses right group multiplication; left group translations preserve every edge and are transitive on each of the two base fibres.'}
(OUT/'MODEL.json').write_text(json.dumps(model,indent=2)+'\n')
hit=any(r['accepted_D9'] for r in reports)
Ds=[r['actual_global_D'] for r in reports]
r={'status':'FIRST_HIT_REQUIRES_PARENT_ACCEPTANCE' if hit else 'ALL_FOUR_Q17_CONTROLS_COMPLETE_NO_HIT',
 'hit':hit,'controls_processed':len(reports),'unattempted':4-len(reports),
 'actual_graphs_built':len(reports),'complete_new_orbit_root_BFS':2*len(reports),'source_BFS':0,
 'target_Delta':5,'target_D':9,'savedL':60686,'actual_n':N,'actual_D':Ds[0] if len(set(Ds))==1 else None,
 'ordinary_bad_unordered_pairs':None,'controls':reports,'compile_CPU_seconds':0,
 'total_batch_CPU_seconds':time.process_time()-START,'prediction':'SUPPORTED' if hit else 'REFUTED',
 'pending':['Parent independent acceptance'] if hit else []}
for fn in ['RESULT.json','terminal.json']:(OUT/fn).write_text(json.dumps(r,indent=2)+'\n')
(OUT/'RUN_HANDLE.json').write_text(json.dumps({k:r[k] for k in ['status','controls_processed','total_batch_CPU_seconds','pending']},indent=2)+'\n')
print(json.dumps({k:r[k] for k in ['status','controls_processed','total_batch_CPU_seconds','pending']}),flush=True)

from pathlib import Path
from collections import Counter,deque
import json,time,resource
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
P=Path(__file__).resolve().parent;BASE=P.parent
assert not(P/'RESULT.json').exists()
START=time.process_time()
I=json.loads((BASE/'INTERFACE.json').read_text())
W=json.loads((BASE/'route_capacity/WORD_IMAGES.json').read_text())['records']
B=json.loads((P/'BINDING.json').read_text())
assert B['selected_word']==[0,1,3,2]and B['cached_word_rank']==4
a=I['global_type_permutations'][0]+[-1];b=I['global_type_permutations'][1]+[-1]
u,v,c,t,w=[B[k]for k in['u','v','c','t','w']]
assert(a[u],b[c])==(v,t)and len({u,v,c,t})==4
a[u]=w;a[w]=v;b[c]=w;b[w]=t
def inverse(p):
 assert sorted(p)==list(range(65));q=[-1]*65
 for i,j in enumerate(p):q[j]=i
 return q
A=inverse(a);BB=inverse(b);perms=[a,b,BB,A]
adj=[[p[i]for p in perms]for i in range(65)]
assert all(len(set(row))==4 and i not in row for i,row in enumerate(adj))
assert all(i in adj[j]for i,row in enumerate(adj)for j in row)
trace=[w];now=w
for k in B['selected_word']:now=perms[k][now];trace.append(now)
assert now==w
controller={'n':65,'m':130,'degree':4,'simple':True,'inverse_types':[3,2,1,0],
 'permutations':perms,'selected_word_loop_trace':trace}
(P/'CONTROLLER65.json').write_text(json.dumps(controller,indent=2)+'\n')
with(P/'controller65.edges').open('w')as f:
 f.write('65 130\n')
 for i,row in enumerate(adj):
  for j in row:
   if i<j:f.write(f'{i} {j}\n')
bad=[];hist=Counter()
for root in range(65):
 d=[-1]*65;d[root]=0;q=deque([root])
 while q:
  x=q.popleft()
  if d[x]==4:continue
  for y in adj[x]:
   if d[y]<0:d[y]=d[x]+1;q.append(y)
 missing=[j for j,z in enumerate(d)if z<0]
 hist[len(missing)]+=1
 bad.extend([root,j]for j in missing)
coarse={'roots_checked':65,'coarse_R4_bad_ordered_pairs':len(bad),'coarse_R4_bad_unordered_pairs':len(bad)//2,
 'root_missing_count_histogram':dict(hist),'bad_ordered_pairs':bad,
 'first_witness':bad[0]if bad else None,'all_radius4':not bad,'CPU_seconds':time.process_time()-START}
assert len(bad)%2==0
(P/'COARSE_R4.json').write_text(json.dumps(coarse,indent=2)+'\n')
r={'status':'CONTROLLER65_COARSE_R4_REFUTED'if bad else'COARSE_PASS_CERT_PENDING',
 'prediction':'REFUTED'if bad else'UNRESOLVED','new_controller_n':65,'hypothetical_final_n':16640,
 'actual_final_n':None,'actual_final_D':None,'ordinary_final_bad_unordered_pairs':None,
 'controller_bad_ordered_pairs':len(bad),'controller_bad_unordered_pairs':len(bad)//2,
 'controller_R4_roots':65,'controller_first_witness':bad[0]if bad else None,
 'large_graph_generated':False,'old_source_BFS':0,'certificate_evaluated':False,'actual_newfiber_R4_gate':False,
 'hard_worker_CPU_seconds':5,'compile_CPU_seconds':0,'pending':[]}
if not bad:
 rankwords=[rec['word_types']for rec in W if rec['rank']==4]
 certmiss=[]
 for root in range(65):
  reached=set()
  for word in rankwords:
   z=root
   for k in word:z=perms[k][z]
   reached.add(z)
  certmiss.extend([root,z]for z in range(65)if z not in reached)
 cert={'rank4_words':len(rankwords),'ordered_pairs':4225,'certified_pairs':4225-len(certmiss),
  'uncertified_pairs':certmiss,'sufficient_certificate_complete':not certmiss}
 (P/'UNIVERSAL_RANK4_CERT.json').write_text(json.dumps(cert,indent=2)+'\n')
 r.update(certificate_evaluated=True,rank4_certified_pairs=4225-len(certmiss),rank4_uncertified_pairs=len(certmiss))
 def fm(a,b):
  s=0
  while b:
   if b&1:s^=a
   b>>=1;a<<=1
   if a&4:a^=7
  return s
 def sv(s,x):
  out=0
  for j in range(4):out|=fm(s,(x>>(2*j))&3)<<(2*j)
  return out
 def linear(cols,x):
  out=0
  for j in range(4):out^=sv((x>>(2*j))&3,cols[j])
  return out
 types=I['relation_types'];maps=[[[linear(T['canonical_columns'],x)^T['constant']^dd for dd in T['D']]for x in range(256)]for T in types]
 N=65*256
 graph=[]
 for g in range(65):
  for x in range(256):
   row=[256*perms[k][g]+y for k in range(4)for y in maps[k][x]]
   assert len(set(row))==16 and 256*g+x not in row
   graph.append(row)
 assert all(i in graph[j]for i,row in enumerate(graph)for j in row)
 r.update(large_graph_generated=True,large_n=N,large_m=N*8,large_degree=16)
 if certmiss:
  root=256*w;d=[-1]*N;d[root]=0;q=deque([root])
  while q:
   x=q.popleft()
   if d[x]==4:continue
   for y in graph[x]:
    if d[y]<0:d[y]=d[x]+1;q.append(y)
  missing=[j for j,z in enumerate(d)if z<0]
  gate={'root':root,'controller_root':w,'fiber_root':0,'R4_covered':N-len(missing),'R4_missing':len(missing),
   'first_missing_target':missing[0]if missing else None,'same_newfiber_missing':[x for x in range(256)if d[256*w+x]<0],
   'ordinary_global_bad_unordered_pairs':None,'global_D':None}
  (P/'ACTUAL_NEWFIBER_R4_GATE.json').write_text(json.dumps(gate,indent=2)+'\n')
  r.update(actual_newfiber_R4_gate=True,newfiber_R4_missing=len(missing),
   status='ACTUAL_NEWFIBER_R4_REFUTED'if missing else'CERT_INCOMPLETE_NEWFIBER_GATE_PASS_UNKNOWN',
   prediction='REFUTED'if missing else'UNRESOLVED')
 else:
  edge=P/'graph_d16_D4_n16640.edges'
  with edge.open('w')as f:
   f.write(f'{N} {N*8}\n');ct=0
   for x,row in enumerate(graph):
    for y in row:
     if x<y:f.write(f'{x} {y}\n');ct+=1
  assert ct==N*8
  recipe={'controller':'CONTROLLER65.json','charts':types,'field':'F4=F2[t]/(t²+t+1),labels0..3',
   'vertex_encoding':'256*controller+fiber withfour2bitF4coords',
   'rank4_word_cache':'../route_capacity/WORD_IMAGES.json','certificate':'UNIVERSAL_RANK4_CERT.json',
   'source_edge_rule':'Globalrelationtypes0/1/2/3,controllernewperms, reverse0<->3/1<->2',
   'all_source_old_BFS_repeated':False}
  (P/'FIRST_HIT_RECIPE.json').write_text(json.dumps(recipe,indent=2)+'\n')
  r.update(status='FULL_RANK4_CERT_FIRST_HIT_PARENT_PENDING',prediction='SUPPORTED',actual_final_n=N,
   actual_final_D=4,graph_file=str(edge),pending=['Parent independent verification'])
r['worker_CPU_seconds']=time.process_time()-START
assert r['worker_CPU_seconds']<5
for fn in['RESULT.json','terminal.json']:(P/fn).write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))

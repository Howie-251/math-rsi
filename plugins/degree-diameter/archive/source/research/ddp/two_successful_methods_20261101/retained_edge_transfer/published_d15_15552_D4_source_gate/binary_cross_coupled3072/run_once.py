import time
START=time.process_time()
from pathlib import Path
from itertools import product
import json,resource,subprocess
resource.setrlimit(resource.RLIMIT_CPU,(9,9))
HERE=Path(__file__).resolve().parent;PRIOR=.965472064
BAR=[0,3,4,1,2];M=[[4,7,1,13],[2,1,4,8],[1,2,8,4],[2,1,4,8],[1,2,8,4]];V=[15,1,4,2,8]
FULL=(1<<256)-1

def save(n,o):(HERE/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
if(HERE/'ATTEMPT.json').exists():raise RuntimeError('one shot singlecrosscoupledchart')
save('ATTEMPT.json',{'status':'STARTED','prior_read_prep':PRIOR,'casecap':10})
old=json.loads((HERE.parent/'NEW_ROUTE4_TYPES_AND_TRANSITIONS.json').read_text());C=old['transition']
assert len(C)==192 and all(len(r)==5 for r in C)
assert all(C[C[u][p]][BAR[p]]==u for u in range(192)for p in range(5))
def app(cols,x):return(cols[0]if x&1 else 0)^(cols[1]if x&2 else 0)^(cols[2]if x&4 else 0)^(cols[3]if x&8 else 0)
for p in range(5):
 assert app(M[BAR[p]],V[p])==V[BAR[p]]
 assert all(app(M[BAR[p]],app(M[p],x))==x for x in range(16))
words=[]
for n in range(5):
 for w in product(range(5),repeat=n):
  pack=0
  for x in range(16):
   out={x}
   for p in w:out={app(M[p],y)^(V[p]if lam else 0)for y in out for lam in [0,1]}
   pack|=sum(1<<y for y in out)<<(16*x)
  words.append((w,pack))
assert len(words)==781
selfpass=0;badroots=0;firstbad=None;rows=[]
for u in range(192):
 if time.process_time()-START>7:break
 cover=[0]*192
 for w,pack in words:
  v=u
  for p in w:v=C[v][p]
  cover[v]|=pack
 same=cover[u]==FULL;selfpass+=same
 bad=next((v for v,pack in enumerate(cover)if pack!=FULL),None)
 rows.append({'controllerroot':u,'self_fibre_all16':same,'full_target_fibres':sum(x==FULL for x in cover),'first_bad_controller':bad})
 if bad is not None:
  badroots+=1
  if firstbad is None:
   pack=cover[bad];x=next(x for x in range(16)if(pack>>(16*x))&65535!=65535);mask=(pack>>(16*x))&65535
   packet=[]
   for w,img in words:
    v=u
    for p in w:v=C[v][p]
    if v==bad:packet.append({'word':list(w),'noise_rank':((img&65535).bit_count()).bit_length()-1,'zero_source_image_mask':img&65535})
   firstbad={'controllerroot':u,'controllertarget':bad,'source_x':x,'first_missing_y':next(y for y in range(16)if not(mask>>y&1)),'actual_fibre_covered_for_x':mask.bit_count(),'whole_fibre_source_counts':[((pack>>(16*x))&65535).bit_count()for x in range(16)],'actual_controller_word_packet':packet}
complete=len(rows)==192
save('CONTROLLER_ROOT_RESULTS.json',rows)
if firstbad:save('FIRST_BAD_PACKET.json',firstbad)
hit=complete and badroots==0
producer=False;roots=0
if hit:
 edges=set()
 for u in range(192):
  for x in range(16):
   a=16*u+x
   for p in range(5):
    for lam in [0,1]:
     v=16*C[u][p]+(app(M[p],x)^(V[p]if lam else 0))
     if a!=v:edges.add(tuple(sorted((a,v))))
 degrees=[0]*3072
 for a,b in edges:degrees[a]+=1;degrees[b]+=1
 assert max(degrees)<=10
 with(HERE/'candidate_d10_D4_n3072.edges').open('w')as f:
  f.write(f'3072 {len(edges)}\n')
  for u,v in sorted(edges):f.write(f'{u} {v}\n')
 save('PARAMETERS.json',{'n':3072,'m':len(edges),'maxdegree':max(degrees),'controller':C,'M_columns':M,'v':V,'bar':BAR,'point_packet_D4':True,'degree_histogram':{d:degrees.count(d)for d in set(degrees)},'producer_allroots':'PENDING_NATIVE','fresh_Lean_ARIS':'PENDING'})
status='POINT_COVER3072_HIT_PENDING_ORDINARY_PRODUCER'if hit else('COMPLETE_NO_SINGLE_BINARY_CROSS_COUPLED_CHART'if complete else'UNKNOWN_POINTGATE_CPU_CAP')
r={'status':status,'same_controller_allpass':selfpass==len(rows),'self_fibre_roots_checked':len(rows),'all_crosscontroller_roots_complete':complete,'bad_controller_roots':badroots,'fullgraph_hit':hit,'first_bad_path':'FIRST_BAD_PACKET.json'if firstbad else None,'ordinary_fullgraph_BFS':roots,'source_F3_graph_R3_BFS_Lean_ARIS_solver':0,'native_CPU':time.process_time()-START,'case_CPU':PRIOR+time.process_time()-START,'case_cap':10,'graph_generated':hit,'new_accepted_graph_parameter_Lean':[0,0,0],'scope':'oneactualC192/fixedcrosscoupledbinaryF2^4chart,one-dimensionalnoiseper5actualports; notgeneral10D4/binarycharts','next':'STOP_SINGLECHART_NOMATRIX_ORFIELD_LADDER'if not hit else'ORDINARY_PRODUCER_THEN_FRESH_LATESTPUBLIC_FORMAL_REVIEWS','terminal':True}
save('RESULT.json',r);save('TERMINAL.json',r)
print(json.dumps(r,ensure_ascii=False),flush=True)

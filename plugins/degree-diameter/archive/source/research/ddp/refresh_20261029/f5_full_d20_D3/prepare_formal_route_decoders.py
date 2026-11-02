from pathlib import Path
import json,itertools,time,resource,os
ROOT=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
D=Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_CPU,(120,121));start=time.process_time()
(D/'FORMAL_DECODER_PREP_HANDLE.json').write_text(json.dumps(dict(status='RUNNING',pid=os.getpid()))+'\n')
P=json.loads((D/'PARAMETERS.json').read_text());C=P['controller'];I=P['inverse_ports'];T=P['matrices'];L=P['directions']
def digits(x):return (x%5,x//5%5,x//25)
def enc(x):return x[0]+5*x[1]+25*x[2]
def step(p,t,x):
 v=digits(x);return enc([(sum(T[p][i][j]*v[j] for j in range(3))+t*L[I[p]][i])%5 for i in range(3)])
def route(p,q,r,n):
 a,b,c=digits(n);return step(r,c,step(q,b,step(p,a,0)))
def word(w):return w%4,w//4%4,w//16
nb=[];valid=0
for w in range(64):
 p,q,r=word(w)
 if q==I[p] or r==I[q]:nb.append([0]*125);continue
 inverse=[None]*125
 for n in range(125):
  y=route(p,q,r,n);assert inverse[y] is None;inverse[y]=n
 assert all(n is not None for n in inverse)
 nb.append(inverse);valid+=1
controller_words=[];required=0
for a in range(30):
 row=[]
 for b in range(30):
  if b in C[a]:row.append(0);continue
  required+=1
  found=next(w for w in range(64) if (lambda v:v[1]!=I[v[0]] and v[2]!=I[v[1]] and C[C[C[a][v[0]]][v[1]]][v[2]]==b)(word(w)))
  row.append(found)
 controller_words.append(row)
adj=[]
for p in range(4):
 inverse=[None]*125
 for side in range(2):
  for q in range(4):
   if (side==0 and q==p) or (side==1 and q==I[p]):continue
   a,b,c=(q,I[q],p) if side==0 else (p,q,I[q])
   for n in range(125):
    y=route(a,b,c,n)
    if inverse[y] is None:inverse[y]=side*500+q*125+n
 assert all(n is not None for n in inverse)
 adj.append(inverse)
def vec(x):return '!['+', '.join(vec(t) for t in x)+']' if isinstance(x,list) else str(x)
s='import DegreeDiameter.Portfolio.F5Graph3750Routes\n\nnamespace DegreeDiameter.Portfolio.F5Graph3750\nset_option maxRecDepth 20000\nset_option maxHeartbeats 40000000\n\n'
s+='def controllerWord : Fin 30 → Fin 30 → Fin 64 := '+vec(controller_words)+'\n\n'
s+='def nbNoiseDecoder : Fin 64 → Fin 125 → Fin 125 := '+vec(nb)+'\n\n'
s+='def adjacentDecoder : Fin 4 → Fin 125 → Fin 1000 := '+vec(adj)+'\n\n'
s+='end DegreeDiameter.Portfolio.F5Graph3750\n'
(ROOT/'formal/DegreeDiameter/Portfolio/F5Graph3750RouteData.lean').write_text(s)
result=dict(status='COMPLETE_FINITE_DECODERS',valid_nonbacktracking_words=valid,NB_displacement_checks=valid*125,adjacent_displacement_checks=500,controller_ordered_cells=900,required_NB_controller_cells=required,CPU_seconds=time.process_time()-start,graph_generated=False,BFS=0,Lean_proved=False)
(D/'FORMAL_DECODER_PREP_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(D/'FORMAL_DECODER_PREP_HANDLE.json').write_text(json.dumps(dict(status='TERMINAL',pid=os.getpid()))+'\n');print(json.dumps(result))

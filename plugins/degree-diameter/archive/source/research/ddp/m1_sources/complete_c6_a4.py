"""Bounded complete 1+5 bi-Cayley test on C6 x A4 after necessary quotient filters."""
from pathlib import Path
from itertools import product
import json,time
P=Path(__file__).resolve().parent
profiles=json.loads((P/'central_halfturn_profile.json').read_text())
start=time.monotonic()
rot=[[0,1,2,3],[0,2,3,1],[0,3,1,2]]
def encode(r,t,v):return (r%6)*12+(t%3)*4+v
def decode(g):return g//12,(g%12)//4,g%4
mul=[]
for g in range(72):
 r,t,v=decode(g);row=[]
 for h in range(72):
  s,u,w=decode(h);row.append(encode(r+s,t+u,v^rot[t][w]))
 mul.append(row)
inv=[next(j for j in range(72) if mul[i][j]==0) for i in range(72)]
results={}
for ab in ['0,3','3,3']:
 alpha,beta=map(int,ab.split(','));a=encode(alpha,0,1)
 tested=0;best=0;best_record=None;full=[]
 for qs in profiles[ab]['projected_survivors']:
  for vs in product(range(4),repeat=4):
   T=[0]+[encode(r,t,v) for (r,t),v in zip(qs[1:],vs)]
   if len(set(T))<5:continue
   Ti=[inv[t] for t in T]
   C={mul[x][y] for x in T for y in Ti}
   C1={mul[x][y] for x in Ti for y in T}
   for vb in (1,2,3):
    b=encode(beta,0,vb);tested+=1
    W00=C|{mul[a][x] for x in C}|{mul[x][a] for x in C}|{mul[mul[x][b]][y] for x in T for y in Ti}
    W11=C1|{mul[b][x] for x in C1}|{mul[x][b] for x in C1}|{mul[mul[x][a]][y] for x in Ti for y in T}
    covered=len(W00)+len(W11)
    if covered>best:best=covered;best_record={'a':decode(a),'b':decode(b),'T':[decode(t) for t in T],'same_layer_coverage':[len(W00),len(W11)]}
    if len(W00)==len(W11)==72:
     W01=set(T)|{mul[a][t] for t in T}|{mul[t][b] for t in T}|{mul[mul[a][t]][b] for t in T}|{mul[x][t] for x in C for t in T}
     if len(W01)==72:full.append({'a':decode(a),'b':decode(b),'T':[decode(t) for t in T]})
 results[ab]={'tested_lift_assignments':tested,'best_same_layer_sum':best,'best_same_layer_example':best_record,'full_successes':full}
 print(ab,results[ab],flush=True)
results['elapsed_seconds']=time.monotonic()-start
results['scope']='All simple degree 1+5 bi-Cayley lifts over C6 x A4, after analytic exclusions of central involutions and pure-A4 pair, normalization of a by conjugation and one cross voltage to identity, and necessary quotient filtering. Finite exploration, not certified formal exclusion.'
(P/'c6_a4_complete_result.json').write_text(json.dumps(results,indent=2)+'\n')
print('seconds',results['elapsed_seconds'])

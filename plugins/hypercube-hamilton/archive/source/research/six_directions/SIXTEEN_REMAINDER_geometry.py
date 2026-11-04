"""Producer-only structure of the148 frozen conditional residual, no exclusion theorem."""
from pathlib import Path
from collections import Counter,defaultdict
import json,itertools,hashlib
R=Path(__file__).resolve().parent
def swap(x,i,j):return x^((1<<i)|(1<<j)) if ((x>>i)^(x>>j))&1 else x
def orbit(seed,gens):
 todo=[seed];seen={seed}
 while todo:
  z,w=todo.pop()
  for i,j in gens:
   r=(tuple(sorted(swap(x,i,j) for x in z)),tuple(sorted(swap(x,i,j) for x in w)))
   if r not in seen:seen.add(r);todo.append(r)
 return seen
groups=Counter();cache={};stats=Counter();rows=[];N0={1<<d for d in range(6)}
for v in (1,7,31):
 raw=(R/f'SIXTEEN_LOCAL_remaining_v{v}_covered.bin').read_bytes();assert len(raw)%15==0
 for index in range(len(raw)//15):
  rec=raw[15*index:15*(index+1)];Z,W=tuple(rec[:7]),tuple(rec[7:]);H={0,*rec};stats[(v,'N0_in_W')]+=N0<=set(W)
  ns=sorted({v^(1<<d) for d in range(6)}-H);stats[(v,'target_degree',len(ns))]+=1
  cuts=[]
  for d in range(6):
   if v>>d&1:continue
   if all(z>>d&1 for z in Z):cuts.append({'d':d,'T':sorted(z^(1<<d) for z in Z),'odd_A_holes':sorted(w for w in W if not w>>d&1),'extra_odd_A':sum(not(w>>d&1) and w not in N0 for w in W)})
  stats[(v,'has_all_Z_B_cut')]+=bool(cuts)
  key=(v,(Z,W))
  if key not in cache:
   gens=[]
   for bit in (0,1):
    pos=[d for d in range(6) if v>>d&1==bit];gens.extend(zip(pos,pos[1:]))
   images=orbit((Z,W),gens);canonical=min(images)
   for image in images:cache[(v,image)]=(v,*canonical)
  groups[cache[key]]+=1;rows.append({'v':v,'index':index,'Z':Z,'W':W,'target_available_original_neighbors':ns,'all_Z_B_cuts':cuts,'canonical':cache[key]})
out={'status':'PRODUCER_GEOMETRY_ONLY_NOT_A_REALIZABILITY_OR_EXTENSION_PROOF','count':len(rows),'orbits':len(groups),'statistics':{str(k):v for k,v in stats.items()},'representatives':[{'v':v,'Z':z,'W':w,'records':n} for (v,z,w),n in sorted(groups.items())],'rows':rows,'full_sixteen_hole_proved':False,'full_P6_proved':False}
(R/'SIXTEEN_REMAINDER_geometry.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))

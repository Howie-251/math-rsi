from pathlib import Path
from itertools import permutations
from collections import Counter,defaultdict
import json,hashlib
P=Path(__file__).resolve().parent
par=lambda x:x.bit_count()%2
nb=lambda x:[x^(1<<d) for d in range(6)]
records={v:[tuple(b[i:i+13]) for i in range(0,len(b),13)] for v in (1,7,31) for b in [(P/f'FOURTEEN_HALL_remaining_v{v}_covered.bin').read_bytes()]}

def maps(v):
 groups=[[i for i in range(6) if bool(v>>i&1)==z] for z in (False,True)]
 out=[]
 for a in permutations(groups[0]):
  for b in permutations(groups[1]):
   perm=dict(zip(groups[0]+groups[1],a+b))
   out.append([sum(((x>>d)&1)<<perm[d] for d in range(6)) for x in range(64)])
 return out

def matching_info(rec):
 H={0,*rec};E=[x for x in range(64) if not par(x) and x not in H];O={x for x in range(64) if par(x) and x not in H};mate={}
 def aug(e,seen):
  for o in nb(e):
   if o not in O or o in seen:continue
   seen.add(o)
   if o not in mate or aug(mate[o],seen):mate[o]=e;return True
  return False
 assert all(aug(e,set()) for e in E)
 M={e:o for o,e in mate.items()}
 # Reachability on alternating orientation: unmatched E->O, matched O->E.
 reach={x:{x} for x in E+sorted(O)}
 for e in E:
  for o in nb(e):
   if o in O:reach[o if M[e]==o else e].add(e if M[e]==o else o)
 for k in reach:
  for i in reach:
   if k in reach[i]:reach[i]|=reach[k]
 allowed=[(e,o) for e in E for o in nb(e) if o in O and (M[e]==o or (o in reach[e] and e in reach[o]))]
 forced=[(e,o) for e,o in M.items() if not(o in reach[e] and e in reach[o])]
 return {'perfect_matching':sorted(M.items()),'allowed_edges':sorted(allowed),'forced_edges':sorted(forced),'covered_degrees':dict(Counter(sum(o in O for o in nb(e)) for e in E))}

out=[];table=[];hist=Counter();rootstars=[]
for v,recs in records.items():
 remaining=set(recs);trans=maps(v);count=0
 while remaining:
  rep=min(remaining);orbit={tuple(sorted(t[x] for x in rep[:6]))+tuple(sorted(t[x] for x in rep[6:])) for t in trans}
  assert orbit<=set(recs),(v,rep,len(orbit-set(recs)))
  remaining-=orbit;count+=1
  Z=rep[:6];W=rep[6:];H={0,*rep};info=matching_info(rep)
  row={'index':len(out),'v':v,'representative':list(rep),'Z':list(Z),'W':list(W),'orbit_size':len(orbit),'stabilizer_size':len(trans)//len(orbit),'root_odd_hole_neighbors':sorted(set(nb(0))&set(W)),'root_covered_neighbors':sorted(set(nb(0))-set(W)),'target_allowed_mates':sorted(e if o==v else o for e,o in info['allowed_edges'] if v in (e,o)),**info}
  cuts=[]
  for d in range(6):
   A={x for x in range(64) if (x^v)&(1<<d)==0};a=len(set(Z)&A);b=len(set(W)&A);delta=int(0 in A)
   cut={'d':d,'a':a,'b':b,'delta':delta}
   if a==0 and delta and b>=3:
    JA=sorted(set(W)&A);T=sorted(z^(1<<d) for z in Z);block=sorted(w^(1<<d) for w in W if w not in A and w!=(1<<d))
    cut.update(maximal_A_candidate=True,J=JA,T=T,blocked_even=block,w_options=sorted(set(JA)&set(nb(0))),s=b-2,B_shape=[7-b,b+3,b-2])
    rootstars.append([row['index'],d])
   cuts.append(cut)
  row['cuts']=cuts;out.append(row)
  hist[(v,len(row['root_odd_hole_neighbors']),len(info['forced_edges']))]+=len(orbit)
  table.append([row['index'],v,len(orbit),len(row['root_odd_hole_neighbors']),len(info['forced_edges']),','.join(map(str,Z)),','.join(map(str,W))])
 print(v,'records',len(recs),'orbits',count,'group',len(trans))
summary={'status':'PRODUCER_STRUCTURE_ONLY_PENDING_INDEPENDENT_REVIEW','inputs':{f'FOURTEEN_HALL_remaining_v{v}_covered.bin':hashlib.sha256((P/f'FOURTEEN_HALL_remaining_v{v}_covered.bin').read_bytes()).hexdigest() for v in records},'records':sum(map(len,records.values())),'orbits':len(out),'orbit_rows':out,'root_hole_neighbor_forced_edge_histogram':[{'v':v,'root_hole_neighbors':r,'forced_edges':f,'records':n} for (v,r,f),n in sorted(hist.items())],'maximal_A_candidate_cuts':rootstars,'full_fourteen_hole_proved':False,'full_P6_proved':False}
(P/'FOURTEEN_RESIDUAL_STRUCTURE.json').write_text(json.dumps(summary,indent=2)+'\n')
(P/'FOURTEEN_RESIDUAL_STRUCTURE.tsv').write_text('index\tv\torbit_size\troot_hole_neighbors\tforced_edges\tZ\tW\n'+''.join('\t'.join(map(str,r))+'\n' for r in table))
print('maxA cuts',len(rootstars));print('hist',hist)

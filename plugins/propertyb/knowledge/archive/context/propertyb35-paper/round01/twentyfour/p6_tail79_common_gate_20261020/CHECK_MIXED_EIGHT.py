"""Bounded old-domain transfer pilot, not a new generic-gate claim.
All existing7 E3 /86 E4..8 templates with a marked capacity3 label,
plus old59's E2 templates. Actual distinctpair extensions and C3/C4 bounds.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
from fractions import Fraction as F
from math import comb
import json,time
HERE=Path(__file__).resolve().parent;BASE=HERE.parent/'positive_occ_three';start=time.process_time()
def restore(g,caps):
 A=[set() for _ in caps];ds=[0]*5;v=0
 for (i,j),m in zip(combinations(range(5),2),g):
  ds[i]+=m;ds[j]+=m
  for _ in range(m):A[i].add(v);A[j].add(v);v+=1
 for i in range(5):
  for _ in range(caps[i]-ds[i]):A[i].add(v);v+=1
 return A
params=[(r,t,v) for t in range(3) for r in range(t+1) for v in range(5-r)]
rows=[]
def check(name,A,extra):
 U=set.union(*A);N=len(U);assert U==set(range(N))
 R={k:[q for q in combinations(range(N),k) if all(set(q)&a for a in A)] for k in (3,4)}
 count={k:len(R[k]) for k in R}
 for k in (3,4):
  ie=sum((-1)**s.bit_count()*comb(N-len(set.union(set(),*[A[i] for i in range(5) if s>>i&1])),k) for s in range(32) if N-len(set.union(set(),*[A[i] for i in range(5) if s>>i&1]))>=k)
  assert ie==count[k]
 P={k:Counter(p for q in R[k] for p in combinations(q,2)) for k in R}
 pref={k:[sum(sorted(P[k].values(),reverse=True)[:r]) for r in range(3)] for k in R}
 tri=Counter(t for q in R[4] for t in combinations(q,3));h=max(tri.values(),default=0)
 bad=[]
 for r,t,v in params:
  b3=pref[3][r]+t-r+v;b4=pref[4][r]+(t-r+v)*h+19-v
  if count[3]<=b3 and count[4]<=b4:bad.append({'r':r,'t':t,'v':v,'b':19,'block3':b3,'block4':b4,'margin3':count[3]-b3,'margin4':count[4]-b4})
 rows.append({'name':name,'sets':[sorted(a) for a in A],'U':N,'C3':count[3],'C4':count[4],
 'C3_pair_prefix':pref[3],'C4_pair_prefix':pref[4],'h3':h,'nongated_parameters':bad,**extra})
old7=json.loads((BASE/'eighteen_one_triple/THREE_EDGE_CHECK.json').read_text())['results']
for i,s in enumerate(old7):
 g=s['vector'];ds=[sum(m for (a,b),m in zip(combinations(range(5),2),g) if q in (a,b)) for q in range(5)]
 for mark in range(5):
  if ds[mark]<=3:check('old7_%d_mark%d'%(i,mark),restore(g,[3 if q==mark else 4 for q in range(5)]),{'source':'old7','old_index':i,'graph':g,'marked_three_label':mark})
old86=json.loads((BASE/'five_graph_catalogue.json').read_text())['graphs']
for i,s in enumerate(old86):
 g=s['edge_vector'];ds=[sum(m for (a,b),m in zip(combinations(range(5),2),g) if q in (a,b)) for q in range(5)]
 for mark in range(5):
  if ds[mark]<=3:check('old86_%d_mark%d'%(i,mark),restore(g,[3 if q==mark else 4 for q in range(5)]),{'source':'old86','old_index':i,'graph':g,'marked_three_label':mark})
old59=json.loads((BASE/'eight_mixed_eighteen/SMALL_GRAPH_CHECK.json').read_text())['rows']
for i,s in enumerate(old59):
 if s['E']==2:check('old59_%d_E2'%i,list(map(set,s['sets'])),{'source':'old59','old_index':i,'E':2})
# Lowocc exact upper: replace every negativeincidence by quadcharge first,
# then assign <=6 tripleincidences to largest marginal p^3/3-p^4/4.
low=[]
for d in range(4):
 for e in range((28-d)//2+1):
  types=[(3-d,6,F(1,3)),(28-d-2*e,6,F(1,4)),(d,5,F(1,2)),(e,5,F(7,16))]
  base=sum(n*c*p**4/4 for n,c,p in types);left=6;cost=base
  for n,c,p in sorted(types,key=lambda z:z[2]**3/3-z[2]**4/4,reverse=True):
   take=min(left,n*c);cost+=take*(p**3/3-p**4/4);left-=take
  low.append({'double_mixed_points':d,'double_four_points':e,'bound':str(cost)})
assert max(F(r['bound']) for r in low)==F(61999,65536)<1
out={'status':'COMPLETE_OLD_TEMPLATE_TRANSFER_PILOT','negative_T_budget':2,'negative_B_budget':19,
 'old_templates_only':True,'rows':rows,'rows_checked':len(rows),'raw_sum_nongated':sum(bool(r['nongated_parameters']) for r in rows),
 'nongated_rows':[r for r in rows if r['nongated_parameters']], 'lowocc_bound':str(max(F(r['bound']) for r in low)),'lowocc_parameter_rows':low,
 'scope':'Counts only; no generic mixedeight repair claim. Markedold7/86 transports cover all E3 and E>=4,M2<=6 mixed34444 families; E2 fromold59. LargerM2 and M2=0 require analytic cases.',
 'cpu_seconds':time.process_time()-start}
(HERE/'CHECK_MIXED_EIGHT.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k not in ('rows','nongated_rows','lowocc_parameter_rows')})
for r in out['nongated_rows'][:8]:print(r['name'],r['C3'],r['C4'],r['C3_pair_prefix'],r['C4_pair_prefix'],r['h3'],r['nongated_parameters'])

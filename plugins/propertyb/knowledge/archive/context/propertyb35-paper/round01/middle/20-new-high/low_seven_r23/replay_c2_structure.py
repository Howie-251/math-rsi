"""Exact 38-residual type extraction and bounded six-type count consequences.
This is a necessary typed-count relaxation, not an actual hypergraph search.
"""
from pathlib import Path
from itertools import combinations_with_replacement,product
from collections import Counter
import json,time
HERE=Path(__file__).parent;start=time.time();audit=json.loads((HERE/'R2_C2_REPLAY.json').read_text());assert audit['status']=='PASS'
raw=json.loads((HERE/'R2_C23_DP.json').read_text())['cases'];byid={r['id']:r for r in raw};names={(0,8,0):'A',(0,8,1):'B',(0,9,0):'C',(0,9,1):'D',(1,8,0):'E',(1,9,0):'F',(2,8,0):'Z8',(2,9,0):'Z9'};allT=set();withZ=set();unitrows=[]
for r in audit['residual_structures']:
 types=[tuple(x[:3]) for x in r['types']];signature=tuple(sorted(names[t] for t in types));w=[t[0] for t in types]
 if max(w)<=1:allT.add(signature)
 else:assert w.count(2)==1;withZ.add(signature)
 if types==[(0,8,0)]*3:
  ns={int(t):v for t,v in byid[r['source_id']]['counts'].items()};coincidences=[]
  for low in (1,2):
   pairs=[sum(v for t,v in ns.items() if t&low and t&m==m) for m in (12,20,24)]
   assert all(v in (0,1) for v in pairs);coincidences.extend(pairs)
  assert sum(coincidences)<=1;unitrows.append(r['source_id'])
expectedT={tuple(sorted(x)) for x in [('A','A','B'),('A','B','C'),('A','A','D'),('C','D','F'),('D','E','E'),('D','E','F'),('A','A','A'),('A','A','C')]};expectedZ={tuple(sorted(x)) for x in [('A','B','Z9'),('A','D','Z9'),('D','E','Z9'),('A','A','Z8'),('A','A','Z9'),('A','C','Z9'),('B','B','Z9')]}
assert allT==expectedT and withZ==expectedZ and len(unitrows)==4
assert all(2*n-n//2>10 for n in range(7,19))
letters='ABCDEF';classes=[]
for a in range(7):
 for rest in product(range(3),repeat=5):
  counts=(a,*rest);t=sum(counts)
  if t<2:continue
  valid=True
  for tri in combinations_with_replacement(range(6),3):
   need=Counter(tri)
   if all(counts[i]>=v for i,v in need.items()) and tuple(letters[i] for i in tri) not in allT:valid=False;break
  if valid:classes.append(counts)
feasible=[]
for counts in classes:
 t=sum(counts);bT=counts[2]+counts[3]+counts[5];wT=counts[4]+counts[5]
 for z8 in range(19-t):
  for z9 in range(19-t-z8):
   q=t+z8+z9
   if not 10<=q<=18 or wT+2*(z8+z9)>16 or bT+z9>2*q-19:continue
   valid=True
   for Z,num in (('Z8',z8),('Z9',z9)):
    if not num:continue
    for i,j in combinations_with_replacement(range(6),2):
     if counts[i]<(2 if i==j else 1) or counts[j]<1:continue
     if tuple(sorted((letters[i],letters[j],Z))) not in withZ:valid=False;break
    if not valid:break
   if valid:feasible.append(dict(T_counts=dict(zip(letters,counts)),Z8=z8,Z9=z9,q=q))
assert feasible and all(r['T_counts']['E']==r['T_counts']['F']==0 for r in feasible)
assert all(sum(r['T_counts'].values())<=7 for r in feasible)
assert any(r['T_counts']==dict(A=6,B=0,C=0,D=0,E=0,F=0) and r['Z8']==4 and r['Z9']==0 for r in feasible)
degreecap=[]
for r in feasible:
 x=r['T_counts'];t=sum(x.values());q=r['q'];b=x['C']+x['D']+r['Z9'];h=18-q;e=2*q-19-b;rh=16-2*(r['Z8']+r['Z9'])
 if rh==0 and e>h:continue
 lower=x['A']+x['C']+max(0,q-2*t-4+x['B']+x['D']);assert lower>=3
 degreecap.append(dict(r,high_count=h,high_degree_excess=e,high_w_budget=rh,unpaired_unit_total_lower=lower))
assert len(degreecap)==76
result=dict(status='PASS',scope=__doc__,all_T_allowed=sorted(allT),two_T_plus_Z_allowed=sorted(withZ),unit8_unpaired_triple_sources=unitrows,unit8_unpaired_bound=6,all_T_type_count_profiles=len(classes),max_T_before_Q_budget=max(map(sum,classes)),full_scalar_feasible_profiles=len(feasible),all_Q_w1_excluded=True,max_T_with_Q_budget=max(sum(r['T_counts'].values()) for r in feasible),feasible_type_profiles=feasible,high_unit_degree_cap_profiles=degreecap,after_high_unit_degree_cap_count=len(degreecap),elapsed_seconds=time.time()-start)
(HERE/'R2_C2_STRUCTURE_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items() if k!='feasible_type_profiles'})

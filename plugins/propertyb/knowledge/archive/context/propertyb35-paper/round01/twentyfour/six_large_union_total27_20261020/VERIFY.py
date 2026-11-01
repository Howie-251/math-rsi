"""Independent stdlib replay of old-core transfer and twelve exact certificates.
Reconstruct positives from graph, C3 from perfect matchings, C4 from64-term IE;
minimal-C4 target counts use missing-label intersections minus forced extensions.
No SciPy, discovery code, or enumeration of all four-point candidates imported.
"""
from itertools import combinations
from fractions import Fraction as F
from pathlib import Path
from collections import Counter
from math import comb
import json,time
P=Path(__file__).resolve().parent;start=time.process_time()
old=P.parent/'positive_occ_three/nine_positive_joint_negative_budget_20261020/six_label_pilot/CENSUS_PROFILE.json'
source=json.load(open(old)); certs=json.load(open(P/'TWELVE_CERTIFICATES.json'))['rows']
bygraph={tuple(r['old_vector']):r for r in certs};pairs=list(combinations(range(6),2));rows=[]; columns=0

def choose(n,k):return comb(n,k) if 0<=k<=n else 0
for original in source['rows']:
 if not 7<=original['E']<=9:continue
 g=original['vector'];A=[set() for _ in range(6)];nextpoint=0
 for m,(a,b) in zip(g,pairs):
  for _ in range(m):A[a].add(nextpoint);A[b].add(nextpoint);nextpoint+=1
 for i in range(6):
  for _ in range(4-len(A[i])):A[i].add(nextpoint);nextpoint+=1
 assert [sorted(B) for B in A]==original['sets'];U=set(range(nextpoint));N=len(U)
 incidence={p:frozenset(i for i,B in enumerate(A) if p in B) for p in U}
 double=[p for p in U if len(incidence[p])==2]
 C3={frozenset(R) for R in combinations(double,3) if len(set.union(*(set(incidence[p]) for p in R)))==6}
 assert len(C3)==original['M3']==original['C3']
 nonminimal4={R|{p} for R in C3 for p in U-R}
 total4=sum((-1)**len(S)*choose(len(U-set.union(*(A[i] for i in S))) if S else N,4) for k in range(7) for S in combinations(range(6),k))
 assert total4==original['C4'];C4=total4-len(nonminimal4);assert C4>0
 def targets_count(T):
  T=frozenset(T);missing=[B for B in A if not(B&T)]
  if len(T)==3:
   possible=(set.intersection(*missing) if missing else U)-T
   return len(possible)-sum(T<=R for R in nonminimal4)
  assert len(T)==4
  return int(not missing and T not in nonminimal4)
 allT=[(frozenset(T),targets_count(T)) for T in combinations(sorted(U),3)]
 assert min(n for T,n in allT)>=0
 prefix=sorted((n for T,n in allT),reverse=True)
 maxima=max((sum(prefix[:t-len(C3)])+27-t,t) for t in range(len(C3),16))
 margin=C4-maxima[0]
 record={'vector':g,'E':sum(g),'C3':len(C3),'minimal_C4':C4,'raw_total27_worst_blocked':maxima[0],'raw_worst_t':maxima[1],'raw_margin':margin}
 if margin>0:record['accepted']='forced_C3_then_distinct_T_prefix'
 elif tuple(g) in bygraph:
  cert=bygraph[tuple(g)];assert cert['C3']==len(C3) and cert['minimal_C4']==C4
  assert not cert['upper_weights']
  beta=list(map(F,cert['beta']));budgets=[15-len(C3),27-len(C3)]+[7-len(incidence[p])-sum(p in S for S in C3) for p in sorted(U)]
  assert budgets==cert['budgets'] and min(budgets)>=0 and all(b>=0 for b in beta)
  assert len(beta)==2+N
  for k in (3,4):
   for T in combinations(sorted(U),k):
    q=F(targets_count(T),C4)
    rhs=beta[0]*int(k==3)+beta[1]+sum(beta[2+p] for p in T)
    assert q<=rhs,(g,k,T,q,rhs)
    columns+=1
  cost=sum(x*y for x,y in zip(beta,budgets));assert cost==F(cert['exact_cost'])<1
  record.update({'accepted':'exact_uniform_joint_budget','cost':str(cost)})
 else:
  # The only three special raw boundary graphs, recognized by actual structure.
  iso=[i for i,B in enumerate(A) if all(len(incidence[p])==1 for p in B)]
  if len(iso)==2:
   assert len(C3)==0 and C4==64
   corelabels=set(range(6))-set(iso)
   core=[p for p in double if incidence[p]<=corelabels]
   Q=[frozenset(S) for S in combinations(core,2) if set.union(*(set(incidence[p]) for p in S))==corelabels]
   active=set.union(*(set(S) for S in Q));dq=Counter(p for S in Q for p in S)
   assert len(Q)==4 and len(active)<=7 and max(dq.values())<=2
   assert F(3*15)+F(5*len(active),2)<64
   record.update({'accepted':'two_isolate_core_budget','core_points':len(active),'bound':str(F(45)+F(5*len(active),2))})
  else:
   # Do not enumerate C4: conditionalIE at fixed p gives all-candidate commonness.
   allcommon=[]
   for p in U:
    missing=[B for B in A if p not in B];Hp=0
    for k in range(len(missing)+1):
     for J in combinations(range(len(missing)),k):
      excluded=set.union(*(missing[j] for j in J)) if J else set()
      Hp+=(-1)**k*choose(len((U-excluded)-{p}),3)
    Hp-=sum(p in R for R in nonminimal4)
    if Hp==C4:allcommon.append(p)
   assert C4==48 and len(C3)==0 and len(allcommon)==1
   z=allcommon[0];assert len(incidence[z])==2
   assert max(n for T,n in allT if z in T)<=4
   assert max(n for T,n in allT if z not in T)<=1
   bound=max(4*r+(15-r)+v for r in range(6) for v in range(6-r));assert bound==30<48
   record.update({'accepted':'common_positive_double_point','z':z,'bound':bound})
 rows.append(record)
assert len(rows)==698
hist=Counter(r['accepted'] for r in rows)
assert hist=={'forced_C3_then_distinct_T_prefix':683,'exact_uniform_joint_budget':12,'two_isolate_core_budget':2,'common_positive_double_point':1},hist
out={'status':'PASS','scope':__doc__,'old_core_rows':len(rows),'acceptance_counts':dict(hist),'all_exact_certificate_target_columns':columns,'max_certificate_cost':str(max(F(r['cost']) for r in rows if 'cost' in r)),'rows':rows,'cpu_seconds':time.process_time()-start}
(P/'VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))

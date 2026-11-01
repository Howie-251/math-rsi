"""Read-only use of the old complete 981 six-label cores, no new domain.
Force every three-transversal as a negative triple before counting minimal fours.
This is a sufficient count test only, not an infeasibility or counterexample claim.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time
P=Path(__file__).resolve().parent;start=time.process_time()
old=P.parent/'positive_occ_three/nine_positive_joint_negative_budget_20261020/six_label_pilot/CENSUS_PROFILE.json'
rows=[]
for r in json.load(open(old))['rows']:
 if not 7<=r['E']<=9:continue
 A=[set(B) for B in r['sets']];U=sorted(set.union(*A))
 C3=[frozenset(R) for R in combinations(U,3) if all(set(R)&B for B in A)]
 C4=[frozenset(R) for R in combinations(U,4) if all(set(R)&B for B in A) and not any(S<=set(R) for S in C3)]
 assert len(C3)==r['C3']
 assert len(C4)+sum(any(S<=set(R) for S in C3) for R in combinations(U,4) if all(set(R)&B for B in A))==r['C4']
 counts=Counter(T for R in C4 for T in combinations(sorted(R),3))
 top=sorted(counts.values(),reverse=True);left=15-len(C3)
 assert left>=0
 blocked=sum(top[:left])+12
 rows.append({'old_vector':r['vector'],'E':r['E'],'union':len(U),'C3':len(C3),'minimal_C4':len(C4),'h3':max(top,default=0),'remaining_T':left,'distinct_T_prefix':sum(top[:left]),'B':12,'margin':len(C4)-blocked,'sets':r['sets']})
out={'scope':__doc__,'rows_checked':len(rows),'strict':sum(r['margin']>0 for r in rows),'not_strict':sum(r['margin']<=0 for r in rows),'minimum_margin':min(r['margin'] for r in rows),'residual':[r for r in rows if r['margin']<=0],'cpu_seconds':time.process_time()-start}
(P/'OLD_CORE_SCALAR_PROFILE.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='residual'},indent=2));print('residual count',len(out['residual']));print(json.dumps(out['residual'][:3],indent=2))

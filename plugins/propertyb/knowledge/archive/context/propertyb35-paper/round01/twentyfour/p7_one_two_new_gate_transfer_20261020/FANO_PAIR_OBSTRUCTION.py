"""One necessary P-source, not an H construction or a signed counterexample."""
from itertools import combinations
from pathlib import Path
import json
P=set(range(7))
missing=[{5,6},{0,1}]
internal=[P-f for f in missing]
higher=list(map(set,[(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5),(0,1,2,3)]))
c=[sum(i in T for T in internal) for i in range(7)]
h=[sum(i in T for T in higher) for i in range(7)]
w=[sum(len(T)-1 for T in higher if i in T) for i in range(7)]
u=[8-c[i]-h[i] for i in range(7)]
assert min(u)>=0 and sum(u)==27
assert all(w[i]<=15-4*c[i] for i in range(7))
pairs=list(map(set,combinations(P,2)))
assert all(any(q<=T for T in internal+higher) for q in pairs)
def good(Q):return all(Q&T and not T<=Q for T in internal+higher)
two=[sorted(q) for q in pairs if good(q)]
three=[dict(blue=sorted(Q),P4=sum(u[i] for i in Q),T3=0,B4=27-sum(u[i] for i in Q))
       for Q in map(set,combinations(P,3)) if good(Q)]
assert not two and len(three)==9 and min(x['P4'] for x in three)==11
witness=next(x for x in three if x['blue']==[1,2,5])
assert witness==dict(blue=[1,2,5],P4=11,T3=0,B4=16)
result=dict(scope=__doc__,inventory=[0,5,1],missing=[sorted(x) for x in missing],
            higher=[sorted(x) for x in higher],c=c,h=h,w=w,u=u,
            nonnegative_private=True,Ppaircover=True,PL_capacity=True,
            proper_blue_pairs=two,proper_three_blue_choices=three,old_eleven_gate_witness=witness)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS necessary source, zero proper blue pairs; three-blue old11 witness',witness)

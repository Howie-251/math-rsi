from itertools import combinations
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent;d=json.loads((HERE/'FALLBACK_FAILURE.json').read_text())
internal=d['internal_masks'];high=d['quad_masks']+d['triple_masks']
c=[sum(T>>v&1 for T in internal) for v in range(7)]
a=[sum(T>>v&1 for T in d['triple_masks']) for v in range(7)]
b=[sum(T>>v&1 for T in d['quad_masks']) for v in range(7)]
u=[8-c[v]-a[v]-b[v] for v in range(7)];assert u==[4]*7==d['u']
assert all(4*u[v]+2*a[v]+b[v]>=17 for v in range(7))
def masks(k):return [sum(1<<v for v in Q) for Q in combinations(range(7),k)]
pairs=masks(2);trios=masks(3)
assert all(any(pair&T==pair for T in internal+high) for pair in pairs)
proper=lambda Q:all(Q&T and Q&T!=T for T in internal+high)
assert not [Q for Q in pairs if proper(Q)]
good=[Q for Q in trios if proper(Q)];assert len(good)==22
assert all(sum(u[v] for v in range(7) if Q>>v&1)==12 for Q in good)
assert d['W']==d['M']==d['D']==0
badsets=[]
for T in internal+high:
    badsets.append({Q for Q in pairs if not Q&T})
assert set.union(*badsets)==set(pairs)
Q=d['best_blue_three'];assert Q in good
source=internal+high+[1<<v for v in range(7) for _ in range(u[v])];assert len(source)==35
pos=[];neg=[];propercount=0
for T in source:
    if Q&T and T&(127^Q):propercount+=1
    elif Q&T==T:pos.append(5-T.bit_count())
    else:neg.append(5-T.bit_count())
assert propercount==7 and pos==[4]*12 and neg==[4]*16
result=dict(PASS=True,necessary_P_source_verified=True,uniform_private_counts=u,
            PL_outside_incidence=[4*u[v]+2*a[v]+b[v] for v in range(7)],Ppaircover=True,
            bad_pair_union_size=21,proper_pair_count=0,proper_three_count=22,
            all_proper_three_costs_equal=12,weighted_D=0,
            actual_signed_interface=dict(Q=Q,P4=12,T3=0,B4=16,L=17,D=7),
            original_trace_classifications=35,not_an_H_or_signed_counterexample=True)
(HERE/'FALLBACK_FAILURE_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS exact fallback obstruction: no pair;22 proper cost12 triples;12P4/0T16B interface')

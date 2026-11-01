from pathlib import Path
from itertools import combinations
import json
HERE=Path(__file__).resolve().parent
d=json.loads((HERE/'FAILURE.json').read_text());internal=d['internal_masks'];quads=d['quad_masks'];triples=d['triple_masks'];high=quads+triples
c=[sum(T>>i&1 for T in internal) for i in range(7)]
a=[sum(T>>i&1 for T in triples) for i in range(7)]
b=[sum(T>>i&1 for T in quads) for i in range(7)]
u=[8-c[i]-a[i]-b[i] for i in range(7)]
assert u==d['u']==[4]*7 and sum(u)==28
assert all(4*u[i]+2*a[i]+b[i]>=17 for i in range(7))
pairs=[sum(1<<i for i in q) for q in combinations(range(7),2)]
trios=[sum(1<<i for i in q) for q in combinations(range(7),3)]
assert all(any(pair&T==pair for T in internal+high) for pair in pairs)
proper=lambda Q:all(Q&T and Q&T!=T for T in internal+high)
good3=[Q for Q in trios if proper(Q)]
assert len(good3)==25 and all(sum(u[i] for i in range(7) if Q>>i&1)==12 for Q in good3)
W=M=0
for Q in trios:
    if Q in triples:continue
    weight=max(0,12-sum(u[i] for i in range(7) if Q>>i&1));W+=weight;M+=weight*sum(not Q&T for T in set(high))
assert W==M==d['W']==d['M']==0
good2=[Q for Q in pairs if proper(Q)];Q=(1<<1)|(1<<4);assert Q in good2
source=internal+high+[1<<i for i in range(7) for _ in range(u[i])];assert len(source)==35
positive=[];negative=[];nproper=0
for T in source:
    if Q&T and T&(127^Q):nproper+=1
    elif Q&T==T:positive.append(5-T.bit_count())
    else:negative.append(5-T.bit_count())
assert nproper==7 and positive==[4]*8 and negative==[4]*20
result=dict(PASS=True,necessary_P_source_verified=True,not_an_H_or_signed_counterexample=True,
            uniform_singletons=u,proper_three_blue_count=25,minimum_three_blue_private_cost=12,
            weighted_D=0,proper_two_blue_masks=good2,old_gate_witness=dict(Q=Q,P4=8,T3=0,B4=20,L=17),
            original_source_traces_classified=35)
(HERE/'FAILURE_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS uniform u4 selector obstruction; 25 cost12 proper triples; old8 bluepair14 witness')

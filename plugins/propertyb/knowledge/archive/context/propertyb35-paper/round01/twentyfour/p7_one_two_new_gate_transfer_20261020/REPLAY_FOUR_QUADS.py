"""Rebuild all 35 indexed traces from every saved source; not a second domain generator."""
from pathlib import Path
from collections import Counter
from itertools import combinations
import json,time
HERE=Path(__file__).resolve().parent;START=time.process_time();P=127
shapes=[(3,6),(3,12)];seen=set();byshape=Counter();gates=Counter();sigcount=Counter()
for line in (HERE/'FOUR_QUAD_WITNESSES.jsonl').open():
    shape,higher,pair,u,blue,gate,signature=json.loads(line)
    key=(shape,tuple(higher),pair);assert key not in seen;seen.add(key)
    assert shape in (0,1) and len(higher)==4 and all(q.bit_count()==4 for q in higher)
    assert pair.bit_count()==2 and blue.bit_count()==2 and len(u)==7 and min(u)>=0
    traces=[P^f for f in shapes[shape]]+higher+[pair]
    for i,count in enumerate(u):traces.extend([1<<i]*count)
    assert len(traces)==35 and sum(5-t.bit_count() for t in traces)==119
    assert all(sum(bool(t&(1<<i)) for t in traces)==8 for i in range(7))
    assert all(any(t&(1<<i) and t&(1<<j) for t in traces) for i,j in combinations(range(7),2))
    assert all(sum(5-t.bit_count() for t in traces if t&(1<<i))>=17 for i in range(7))
    pos=Counter();neg=Counter()
    for t in traces:
        if not t&blue:neg[5-t.bit_count()]+=1
        elif not t&~blue:pos[5-t.bit_count()]+=1
    assert not any(pos[k] for k in (1,2,3,5)) and not any(neg[k] for k in (1,2,5))
    m,t,b=signature;assert pos[4]==m and neg[3]==t and neg[4]==b
    if gate==0:assert m<=7 and t<=4 and b<=35
    elif gate==1:assert m==8 and t<=3 and b<=20
    elif gate==2:assert m==9 and t<=3 and t+b<=20
    else:raise AssertionError(gate)
    byshape[shape]+=1;gates[gate]+=1;sigcount[tuple(signature)]+=1
assert len(seen)==77840 and dict(byshape)=={0:26189,1:51651}
result=dict(PASS=True,saved_unique_sources=len(seen),indexed_source_traces_rebuilt=35*len(seen),
            by_missing_shape=dict(byshape),by_gate=dict(gates),
            signature_counts=[dict(P4=k[0],N3=k[1],N4=k[2],sources=v) for k,v in sorted(sigcount.items())],
            cpu_seconds=time.process_time()-START,scope=__doc__,independent_full_domain_generation='PENDING_SECOND_IMPLEMENTATION')
(HERE/'REPLAY_FOUR_QUADS.json').write_text(json.dumps(result,indent=2)+'\n')
print(result)

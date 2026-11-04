"""Producer-side direct witness checks, not independent proof acceptance."""
from pathlib import Path
from itertools import permutations
from collections import Counter
import hashlib,json
R=Path(__file__).resolve().parent
H={0,1,2,4,8,15,23,27,29,30};K=set(range(32))-H
raw=(R/'A10_ORBIT3_SPECTRUM_pairs.bin').read_bytes();forests=(R/'A10_ORBIT3_SPECTRUM_forests.bin').read_bytes()
assert len(raw)==17496*22 and len(forests)==17496*40
records=[]
for i in range(17496):
    p=raw[22*i:22*i+22];s=forests[40*i:40*i+40]
    edges=[tuple(s[j:j+2]) for j in range(0,40,2)]
    assert edges==sorted(set(edges)) and all(a<b and (a^b) in (1,2,4,8,16) for a,b in edges)
    adj={x:[] for x in range(1,32)}
    for a,b in edges:adj[a].append(b);adj[b].append(a)
    assert all(len(adj[x])==(1 if x in K else 2) for x in adj)
    seen=set();pairs=[]
    for start in sorted(K):
        if start in seen:continue
        path=[start];previous=None;now=start
        while True:
            seen.add(now)
            nxt=[x for x in adj[now] if x!=previous]
            if not nxt:break
            assert len(nxt)==1;previous,now=now,nxt[0];assert now not in seen;path.append(now)
        assert now in K and now!=start and len(path) in (2,3)
        pairs.append(tuple(sorted((start,now))))
    assert seen==set(range(1,32)) and len(pairs)==11
    assert bytes(x for e in sorted(pairs) for x in e)==p
    records.append(p)
assert records==sorted(set(records))
trs=[]
for pi in permutations(range(4)):
    trs.append([sum(((x>>j)&1)<<pi[j] for j in range(4))+(x&16) for x in range(32)])
left=set(records);all_records=set(records);hist=Counter()
while left:
    a=min(left);orbit=set()
    for tr in trs:
        edges=sorted(tuple(sorted((tr[a[j]],tr[a[j+1]]))) for j in range(0,22,2))
        b=bytes(x for e in edges for x in e);assert b in all_records;orbit.add(b)
    left-=orbit;hist[len(orbit)]+=1
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
out={'status':'ALL_POSITIVE_FOREST_WITNESSES_PASS_PRODUCER_CHECK','pairing_records':17496,
     'short_forest_witnesses':17496,'spectrum_orbit_size_histogram':dict(hist),
     'universal_F_coverage_rank_checked':False,'full_A10_orbit3_accepted':False,
     'hashes':{n:sha(n) for n in ['A10_ORBIT3_SPECTRUM_enumerate.py','A10_ORBIT3_SPECTRUM_pairs.bin','A10_ORBIT3_SPECTRUM_forests.bin','A10_ORBIT3_SPECTRUM_verify.py']}}
(R/'A10_ORBIT3_SPECTRUM_verified.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))

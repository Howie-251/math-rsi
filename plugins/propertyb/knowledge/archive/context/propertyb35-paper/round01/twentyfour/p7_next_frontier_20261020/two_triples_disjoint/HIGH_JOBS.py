from itertools import permutations, combinations_with_replacement
from collections import Counter
from pathlib import Path
import json,time
start=time.process_time();p=Path(__file__).parent
triples=[m for m in range(128) if m.bit_count()==3]
F={3,12};groups=[]
for perm in permutations(range(7)):
    def image(m):return sum(1<<perm[v] for v in range(7) if m>>v&1)
    if {image(m) for m in F}==F:groups.append([image(m) for m in range(128)])
assert len(groups)==48
allhigher=list(combinations_with_replacement(triples,2));assert len(allhigher)==630
valid={h for h in allhigher if all(sum(bool(t>>v&1) for t in h)<=1 for v in (4,5,6))}
seen=set();jobs=[]
for h in sorted(valid):
    if h in seen:continue
    orbit={tuple(sorted(g[t] for t in h)) for g in groups}
    assert orbit<=valid
    assert not orbit&seen
    seen|=orbit
    jobs.append({'id':len(jobs),'triple_masks':list(h),'orbit_size':len(orbit)})
assert seen==valid
(p/'JOBS.tsv').write_text(''.join(f"{j['id']} {' '.join(map(str,j['triple_masks']))} {j['orbit_size']}\n" for j in jobs))
(p/'JOBS.json').write_text(json.dumps({'all_labeled_high_multisets':len(allhigher),'conditional_labeled_high_multisets':len(valid),'group_order':48,'job_count':len(jobs),'jobs':jobs,'cpu_seconds':time.process_time()-start},indent=2)+'\n')
print(len(allhigher),len(valid),len(jobs),time.process_time()-start)

"""Construct Q7/Q8 cycles by the paper's fibre-splicing mechanism."""
import json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
source=ROOT/'pilot_results_retry.json'; data=json.loads(source.read_text(encoding='utf8'))
templates={}
for c in data['cases']:
    if c['n']!=6 or c['status']!='FOUND':continue
    key=tuple(sorted(tuple(sorted(e)) for e in c['matching']))
    t=templates.setdefault(key,{'matching':list(key),'paths':{}})
    t['paths'][c['v']]=c['path']
valid=[t for t in templates.values() if len(t['paths'])==32]
full=[t for t in valid if len({a^b for a,b in t['matching']})==6]
assert full
results=[]
for outer_dim in (1,2):
    k=1<<outer_dim;order=[i^(i>>1) for i in range(k)]
    assigned=[full[i%len(full)] for i in range(k)]
    local_paths=[None]*k;exit_vertex=0
    for i in range(1,k):
        template=assigned[i];cycle=template['paths'][1]
        entry=exit_vertex;index=cycle.index(entry)
        required={tuple(e) for e in template['matching']}
        next_vertex=cycle[(index+1)%64]
        if tuple(sorted((entry,next_vertex))) not in required:
            path=[cycle[(index-j)%64] for j in range(64)]
        else:
            previous=cycle[(index-1)%64]
            assert tuple(sorted((entry,previous))) not in required
            path=[cycle[(index+j)%64] for j in range(64)]
        local_paths[i]=path;exit_vertex=path[-1]
    assert exit_vertex.bit_count()%2==1
    local_paths[0]=assigned[0]['paths'][exit_vertex][::-1]
    cycle=[(order[i]<<6)|x for i in range(k) for x in local_paths[i]]
    matching=[[(order[i]<<6)|a,(order[i]<<6)|b] for i in range(k) for a,b in assigned[i]['matching']]
    results.append({'n':6+outer_dim,'matching':matching,'cycle':cycle})
out={'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'distinct_rooted_templates':len(valid),'templates_using_all_six_directions':len(full),'examples':results}
(ROOT/'lifted_cycles.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='examples'}))

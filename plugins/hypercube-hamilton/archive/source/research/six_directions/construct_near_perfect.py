"""Exercise the exact N3 artificial-edge deletion/splice construction on 16 cases."""
import json, random
from pathlib import Path
from single_bridge_probe import random_maximum, solve, verify
ROOT=Path(__file__).resolve().parent
rng=random.Random(11012026)
cases=[]
for w in (7,31):
    for j in range(8):
        matching=random_maximum(6,{0,w},rng)
        assert len(matching)==31 and len({a^b for a,b in matching})>=4
        v=rng.choice([z for z in range(64) if z.bit_count()%2 and z!=w])
        p=matching+[(0,w)]
        mate={a:b for edge in p for a,b in (edge,edge[::-1])}
        x=next(w^(1<<k) for k in range(6) if (w^(1<<k))!=mate[v])
        result=solve(6,p,x,v,5,seconds=10,allowed_long=[(0,w)])
        case={'n':6,'u':0,'v':v,'w':w,'x':x,'matching':matching,'status':result['status']}
        if result['status']=='FOUND':
            k=result['path']; split=k.index(0)
            assert split%2==0 and k[split+1]==w
            h=list(reversed(k[:split+1]))+k[split+1:]
            verify(6,matching,0,v,h)
            case.update({'path':h,'intermediate_path':k})
        cases.append(case)
        (ROOT/'near_perfect_constructions.json').write_text(json.dumps(cases,indent=2),encoding='utf8')
        print(w,v,x,case['status'],flush=True)
assert all(c['status']=='FOUND' for c in cases)
print('PASS: 16 artificial-edge deletions and splices; every final edge is a cube edge.')

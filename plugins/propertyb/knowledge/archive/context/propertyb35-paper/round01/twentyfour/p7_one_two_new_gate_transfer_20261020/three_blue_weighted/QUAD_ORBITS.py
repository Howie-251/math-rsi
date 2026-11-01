"""Exact missing-graph automorphisms, all 35 quad images, and their transports."""
from itertools import permutations
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
def move(mask,p):return sum(1<<p[i] for i in range(7) if mask>>i&1)
quads=[m for m in range(128) if m.bit_count()==4]
shapes=[];jobs=[]
for shape,missing in enumerate(((3,6),(3,12))):
    group=[p for p in permutations(range(7)) if sorted(move(f,p) for f in missing)==sorted(missing)]
    assert len(group)==48
    representatives=sorted({min(move(q,p) for p in group) for q in quads})
    assert len(representatives)==(6 if shape==0 else 5)
    sources=[];orbits=[]
    for rep in representatives:
        job=len(jobs);jobs.append([job,shape,rep])
        images=sorted({move(rep,p) for p in group})
        for q in images:
            p=next(p for p in group if move(rep,p)==q)
            sources.append(dict(quad=q,representative=rep,job=job,transport=list(p)))
        orbits.append(dict(job=job,representative=rep,images=images))
    assert sorted(x['quad'] for x in sources)==quads
    shapes.append(dict(shape=shape,missing=list(missing),automorphisms=[list(p) for p in group],
                       orbits=orbits,all_quad_images=sorted(sources,key=lambda x:x['quad'])))
assert len(jobs)==11
(HERE/'QUAD_ORBITS.json').write_text(json.dumps(dict(shapes=shapes,jobs=jobs),indent=2)+'\n')
(HERE/'JOBS.tsv').write_text(''.join(' '.join(map(str,j))+'\n' for j in jobs))
print('PASS: 48+48 automorphisms, 6+5 quad orbits, all 35+35 image keys and transports')

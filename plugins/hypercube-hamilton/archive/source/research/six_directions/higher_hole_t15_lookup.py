"""Build a conservative lookup from fixed accepted marked T15 theorems.

No unrestricted same-face shortcut is used. Table codes: accepted core ID,
100 = audited split lemma, 101 = short augmentation to audited T44_5.
"""
import itertools,json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
CORE_IDS=[0,1,2,4,5,7,8,10,13,14,15,18,19,21,23,24,25,27,31,32,35,37,38,44]
rows=json.loads((R/'t15_analytic_geometry.json').read_text())['T15']['residual_orbits']
odd=[v for v in range(32) if v.bit_count()%2]
oi={v:i for i,v in enumerate(odd)}
def key(a,b):return sum(1<<oi[x] for x in a)|(sum(1<<oi[x] for x in b)<<16)
coremap={}
for p in itertools.permutations(range(5)):
    tr=[sum(((x>>j)&1)<<p[j] for j in range(5)) for x in range(32)]
    for i,row in enumerate(rows):
        z=key([tr[x] for x in row['avoided']],[tr[x] for x in row['included']])
        assert z not in coremap or coremap[z]==i
        coremap[z]=i
out={}
for inc in itertools.combinations(odd,3):
    for av in itertools.combinations([x for x in odd if x not in inc],2):
        z=key(av,inc)
        if any(x.bit_count()==1 for x in inc):out[z]=101
        elif any(sum((x>>d)&1 for x in (*av,*inc))==2 and ((av[0]^av[1])>>d)&1 for d in range(5)):out[z]=100
        elif coremap.get(z) in CORE_IDS:out[z]=coremap[z]
(R/'higher_hole_t15_lookup.txt').write_text(''.join(f'{k} {v}\n' for k,v in sorted(out.items())))
(R/'higher_hole_t15_all_hard.txt').write_text(''.join(f'{k} {v}\n' for k,v in sorted(coremap.items())))
inputs=['t15_analytic_geometry.json','EIGHT_HOLE_FULL_REVIEW.json','Q4_RICH_GLUING_REVIEW.json','T44_Q5_CLOSURE_REVIEW.json']
meta={'scope':'Conservative geometric T15 sufficient lookup; not independently audited yet',
      'accepted_core_ids':CORE_IDS,'accepted_entries':len(out),'all_hard_entries':len(coremap),
      'input_hashes':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in inputs}}
(R/'higher_hole_t15_lookup.json').write_text(json.dumps(meta,indent=2)+'\n')
print(meta['accepted_entries'],meta['all_hard_entries'])

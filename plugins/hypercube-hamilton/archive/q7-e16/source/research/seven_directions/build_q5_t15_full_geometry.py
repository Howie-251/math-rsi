"""Complete preprocessed T15 geometry, minority fixed at 0; no theorem claim."""
from pathlib import Path
from itertools import combinations,permutations
import json
ROOT=Path(__file__).resolve().parent

def main():
    odd=[x for x in range(32) if x.bit_count()%2]
    inc=[x for x in odd if x.bit_count()!=1]
    maps=[[sum(((x>>j)&1)<<p[j] for j in range(5)) for x in range(32)] for p in permutations(range(5))]
    def canon(I,U):return min((tuple(sorted(t[x] for x in I)),tuple(sorted(t[x] for x in U))) for t in maps)
    groups={}
    for I in combinations(inc,3):
        for U in combinations([x for x in odd if x not in I],2):
            key=canon(I,U);groups[key]=groups.get(key,0)+1
    old=[]
    for i in range(15):
        pre=ROOT.parent/'six_directions'/f'Q5_T15_RANK_orbit_{i:02d}'
        vals=list(map(int,Path(str(pre)+'_config.txt').read_text().split()))
        H=vals[:6];U=vals[6:];assert H[0]==0
        old.append((canon([x for x in H[1:] if x not in U],U),str(pre)))
    old=dict(old);rows=[]
    for i,((I,U),size) in enumerate(sorted(groups.items())):
        pre=f'Q5_T15_FULL_{i:03d}'
        (ROOT/(pre+'_config.txt')).write_text(' '.join(map(str,[0,*sorted(I+U),*U]))+'\n')
        rows.append(dict(index=i,included=list(I),omitted=list(U),size=size,prefix=pre,
                         existing_rank_prefix=old.get((I,U))))
    out=dict(scope='all Q5 T15 inputs with no minority-to-included-majority short edge, modulo coordinate permutations',
             normalized_configurations=sum(groups.values()),orbits=len(rows),existing_rank_orbits=sum(bool(r['existing_rank_prefix']) for r in rows),
             full_theorem_proved=False,rows=rows)
    (ROOT/'Q5_T15_FULL_GEOMETRY.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'}))

if __name__=='__main__':main()

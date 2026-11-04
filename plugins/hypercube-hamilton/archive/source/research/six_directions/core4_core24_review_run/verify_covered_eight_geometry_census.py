"""Independent residual-record checks, analytic total count and stabilizer orbits.

No assertion of matching realizability. No import from existing research code.
"""
from collections import Counter
from itertools import combinations,permutations
from math import comb
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parent
GOOD={(0,1),(0,2),(1,1),(1,2),(1,3),(2,2),(2,3),(2,4),(3,3)}
SPLIT_BITS={(1,0):1,(1,4):2,(2,0):4,(2,1):8}
E=[x for x in range(1,64) if x.bit_count()%2==0]
O=[x for x in range(64) if x.bit_count()%2]

def rows(g,v):
    return tuple((sum((x^v)&(1<<i)==0 for x in g[:3]),
                  sum((x^v)&(1<<i)==0 for x in g[3:])) for i in range(6))

def main():
    supplied=json.loads((ROOT/'covered_eight_geometry_census.json').read_text())
    results=[]
    for item in supplied['targets']:
        v=item['v']
        # Count the full enumerated domain without iterating over W quadruples.
        total=0
        for zz in combinations(E,3):
            allowed=sum(w!=v and all((w^z).bit_count()!=1 for z in zz) for w in O)
            total+=comb(allowed,4)
        assert total==item['eligible_geometries']
        raw=(ROOT/item['record_file']).read_bytes()
        assert len(raw)%7==0
        records={tuple(raw[i:i+7]) for i in range(0,len(raw),7)}
        assert len(records)==len(raw)//7==item['no_good_cut']
        rowhist=Counter();signatures=Counter();patterns=Counter();splits=Counter();without=[]
        sig_by_g={}
        for g in records:
            zz,ww=g[:3],g[3:]
            assert tuple(sorted(set(zz)))==zz and tuple(sorted(set(ww)))==ww
            assert set(zz)<=set(E) and set(ww)<=set(O)-{v}
            assert all((z^w).bit_count()!=1 for z in zz for w in ww)
            rr=rows(g,v)
            assert not (set(rr)&GOOD)
            rowhist.update(rr);patterns[tuple(sorted(rr))]+=1
            sig=0
            for row in rr:
                if row[0] in (1,2):sig|=SPLIT_BITS[row]
            assert sig!=0 and sig&(4|8)
            sig_by_g[g]=sig;signatures[sig]+=1
            splits[sum(a in (1,2) for a,b in rr)]+=1
            if not sig&(2|8):
                assert sig==4
                without.append(g)
        assert rowhist==Counter({(r['a'],r['b']):r['count'] for r in item['bad_row_occurrences']})
        assert signatures==Counter({s['mask']:s['count'] for s in item['split_signatures']})
        assert patterns==Counter({tuple(tuple(r) for r in p['rows']):p['count'] for p in item['sorted_row_multisets']})
        assert [splits[i] for i in range(7)]==item['splitting_coordinate_count_histogram']
        assert len(without)==item['without_a1b4_or_a2b1']
        maps=[]
        for p in permutations(range(6)):
            t=tuple(sum(((x>>i)&1)<<p[i] for i in range(6)) for x in range(64))
            if t[v]==v:maps.append(t)
        pending=set(records);orbits=[]
        while pending:
            g=next(iter(pending))
            orbit={tuple(sorted(t[x] for x in g[:3]))+tuple(sorted(t[x] for x in g[3:])) for t in maps}
            assert orbit<=records and orbit<=pending
            rep=min(orbit)
            pending.difference_update(orbit)
            orbits.append(dict(Z=list(rep[:3]),W=list(rep[3:]),size=len(orbit),
                rows=rows(rep,v),split_mask=sig_by_g[rep],without_a1b4_or_a2b1=(sig_by_g[rep]==4)))
        orbits.sort(key=lambda o:(o['Z'],o['W']))
        result=dict(v=v,eligible_geometries=total,residual_geometries=len(records),
            stabilizer_order=len(maps),residual_orbits=len(orbits),
            without_near_geometries=len(without),without_near_orbits=sum(o['without_a1b4_or_a2b1'] for o in orbits),
            all_residual_have_a2b0_or_a2b1=True,orbits=orbits,
            record_sha256=hashlib.sha256(raw).hexdigest())
        results.append(result)
        print(json.dumps({k:val for k,val in result.items() if k not in ('orbits','record_sha256')}))
        print('EXCEPTION ORBITS:',json.dumps([o for o in orbits if o['without_a1b4_or_a2b1']]))
    output=dict(status='PASS',scope='all residual records independently checked; C++ exhaustive no-good-cut selection',
        review_independence='same-family',acceptance_status='provisional',p6_proved=False,
        targets=results,source_sha256={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in
            ['covered_eight_geometry_census.cpp','covered_eight_geometry_census.json',Path(__file__).name]})
    (ROOT/'covered_eight_geometry_census_independent_check.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')

if __name__=='__main__':main()

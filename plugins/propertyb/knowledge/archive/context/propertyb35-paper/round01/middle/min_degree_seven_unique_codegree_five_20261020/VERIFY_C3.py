"""Independent inclusive/Mobius missing C3 domain and415 expanded35 replays."""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction
import json,sys,time

P=Path(__file__).resolve().parent;ROOT=P.parents[4];START=time.process_time()
sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
dom=json.loads((P/'C3_DOMAIN.json').read_text());primary=json.loads((P/'C3_RESULT.json').read_text())
PP=(3,5,6,9,10,12);CROSS=(5,6,9,10);TRIPLES=(7,11,13,14)
keys={};familycounts=Counter()
for fid,fam in enumerate(dom['families']):
    mark=fam['marked_pair'];degrees=fam['degrees'];others=[p for p in PP if p!=mark]
    for values in product(range(1,5),repeat=5):
        inclusive={mark:5,**dict(zip(others,values))}
        total=sum(inclusive[p] for p in CROSS)
        if total<14:continue
        for full in range(min(inclusive.values())+1):
            maximum=(total-14-4*full)//2
            if maximum<0:continue
            assert maximum<=1
            tvs=[(0,0,0,0)]+([tuple(int(i==j) for i in range(4)) for j in range(4)] if maximum==1 else [])
            for tv in tvs:
                mu=[0]*16;mu[15]=full
                for m,n in zip(TRIPLES,tv):mu[m]=n
                for p in PP:mu[p]=inclusive[p]-full-sum(n for m,n in zip(TRIPLES,tv) if m&p==p)
                if min(mu)<0 or mu[3]<1 or mu[12]<1 or sum(mu[p] for p in CROSS)<14:continue
                for v,d in enumerate(degrees):mu[1<<v]=d-sum(n for m,n in enumerate(mu) if m.bit_count()>=2 and m>>v&1)
                mu[0]=35-sum(mu)
                if min(mu)<0:continue
                key=tuple(mu);keys.setdefault(key,[]).append(fid);familycounts[fid]+=1
expected={tuple(z['counts']):z['families'] for z in dom['keys']}
assert keys==expected and len(keys)==415
assert primary['strict_count']==415 and len(primary['cases'])==415
cases=[];maximum=Fraction()
for z in primary['cases']:
    mu=z['counts'];masks=[m for m,n in enumerate(mu) for _ in range(n)]
    assert len(masks)==35
    stubs=[frozenset(v+1 for v in range(4) if m>>v&1) for m in masks]
    rows=independent_rows(21,tuple(z['best']['positions']),stubs)
    value=sum((min(r['A'],r['B'],r['C']) for r in rows),Fraction())
    assert value==Fraction(z['best']['bound'])<1
    maximum=max(maximum,value)
    cases.append({'counts':mu,'families':z['families'],'expanded35_masks':masks,
                  'positions':z['best']['positions'],'bound':str(value),'quota':0,
                  'rows':[{k:str(v) if isinstance(v,Fraction) else v for k,v in r.items()} for r in rows]})
    assert time.process_time()-START<8,'eight CPU independent C3 cutoff'
out={'status':'PASS_COMPLETE_INDEPENDENT_MISSING_C3_GATE','families':20,'inventory_count':415,
     'inclusive_Mobius_domain_equal':True,'family_counts':dict(familycounts),
     'strict_certificates':415,'maximum':str(maximum),'expanded_indices_per_case':35,
     'ordered_distinct_pairs_per_case':1190,'replayed_position_rows':415*21,
     'cases':cases,'cpu_seconds':time.process_time()-START}
(P/'C3_VERIFY_RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k!='cases'})

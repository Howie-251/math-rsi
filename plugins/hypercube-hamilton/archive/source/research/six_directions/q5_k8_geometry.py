"""Complete positive geometry witnesses for balanced-eight-hole Q5 cycles.
No arbitrary matching enumeration is needed: A8 partial theorem handles each.
"""
import itertools as it,json,collections,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
E=[x for x in range(32) if not x.bit_count()%2]
O=[x for x in range(32) if x.bit_count()%2]
rows=[];hist=collections.Counter()
for e in it.combinations(E,4):
    available=[y for y in O if all((x^y).bit_count()!=1 for x in e)]
    for o in it.combinations(available,4):
        witnesses=[]
        for r in (*e,*o):
            own,opp=(e,o) if r in e else (o,e)
            for d in range(5):
                y=r^(1<<d)
                assert y not in e and y not in o
                majority=[*opp,y];minority=[x for x in own if x!=r]
                cuts=[]
                for j in range(5):
                    delta=sum(((x^y)>>j)&1==0 for x in majority)-sum(((x^y)>>j)&1==0 for x in minority)
                    if delta in (1,2,3):cuts.append([j,delta])
                if cuts:witnesses.append({'root':r,'neighbor':y,'avoid_cut':cuts[0][0],'delta':cuts[0][1]})
        assert witnesses,(e,o)
        hist[len(witnesses)]+=1
        rows.append({'even_holes':e,'odd_holes':o,'witness':witnesses[0],'valid_root_neighbor_pairs':len(witnesses)})
assert len(rows)==980
out={'scope':'Complete independent 4+4 Q5 hole geometry coverage via delta123 A8 partial; matching quantifier comes from that theorem',
     'geometry_count':len(rows),'root_neighbor_pair_histogram':dict(sorted(hist.items())),
     'remaining':0,'rows':rows,'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'independent_review_pending':True,'full_p6_proved':False}
(R/'q5_k8_geometry.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'}))

"""All cost-four repeated-point supports on six link labels; no H or outside edges."""
from itertools import combinations, combinations_with_replacement, product
from fractions import Fraction
from math import comb
from pathlib import Path
from time import process_time
import json

start=process_time()
DIR=Path(__file__).parent
P=list(combinations(range(6),2))
supports={r:list(combinations(range(6),r)) for r in range(2,6)}
jobs=[
    ("1+1+1+1",combinations_with_replacement(supports[2],4),8294,3060),
    ("2+1+1",((a,b,c) for a in supports[3] for b,c in combinations_with_replacement(supports[2],2)),8734,2400),
    ("2+2",combinations_with_replacement(supports[3],2),7590,210),
    ("3+1",product(supports[4],supports[2]),6050,225),
    ("4",((a,) for a in supports[5]),6380,6)]
rows=[]
for name,iterator,bound,expected_raw in jobs:
    raw=valid=0
    maximum=-1
    witness=None
    for system in iterator:
        system=tuple(system)
        raw+=1
        assert sum(len(S)-1 for S in system)==4
        occ=[sum(i in S for S in system) for i in range(6)]
        assert max(occ)<=4
        m=[sum(i in S and j in S for S in system) for i,j in P]
        if max(m)==4:
            assert name=="1+1+1+1"
            continue # Coincident original link four-sets, forbidden by simplicity.
        assert max(m)<=3
        private=[4-d for d in occ]
        assert len(system)+sum(private)==20
        value=2*sum(comb(12+w,2+w) for w in m)
        assert value<=bound
        valid+=1
        if value>maximum:
            maximum=value
            witness=dict(repeated_point_supports=system,
                         private_link_sizes=private,pair_intersections=m)
    assert raw==expected_raw and maximum==bound
    rows.append(dict(cost_partition=name,raw=raw,simple_covering_links=valid,
                     maximum_bad_numerator=maximum,witness=witness))
assert sum(r["raw"] for r in rows)==5901
assert sum(r["simple_covering_links"] for r in rows)==5886
den=comb(20,10)
nonstar=29*2*comb(15,5)
worst=max(r["maximum_bad_numerator"] for r in rows)
assert worst==8734
assert Fraction(nonstar+worst,den)==Fraction(4157,4199)<1
assert den-nonstar-worst==1848
out=dict(status="PASS",scope="complete repeated-point supports of six covering four-links, excess4; no noncenter H",
         raw_count=5901,valid_simple_link_system_count=5886,rows=rows,
         total_joint_bound=str(Fraction(nonstar+worst,den)),
         guaranteed_balanced_good_colorings=den-nonstar-worst,
         cpu_seconds=process_time()-start)
(DIR/"CHECK_GENERAL.json").write_text(json.dumps(out,indent=2)+"\n")
print({k:out[k] for k in ["status","raw_count","valid_simple_link_system_count",
                         "total_joint_bound","guaranteed_balanced_good_colorings","cpu_seconds"]})

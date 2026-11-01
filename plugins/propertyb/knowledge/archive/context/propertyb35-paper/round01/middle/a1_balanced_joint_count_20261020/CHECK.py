"""Exact scalar count, plus one explicit link only; no H realization/search."""
from fractions import Fraction
from math import comb
from itertools import combinations
from pathlib import Path
from time import process_time
import json

start=process_time()
DIR=Path(__file__).parent
den=comb(20,10)

def partitions(n, upper):
    if n==0:
        yield ()
    for first in range(min(n,upper),0,-1):
        for rest in partitions(n-first,first):
            yield (first,)+rest

rows=[]
for shape in partitions(4,3):
    value=2*(sum(comb(12+j,2+j) for j in shape)
             +(15-len(shape))*comb(12,2))
    rows.append(dict(nonzero_link_intersections=shape,colored_pair_union_bound=value))
assert len(rows)==4
worst=max(row["colored_pair_union_bound"] for row in rows)
assert worst==8294
nonstar=29*2*comb(15,5)
assert nonstar==174174
total=nonstar+worst
assert Fraction(total,den)==Fraction(319,323)<1
assert den-total==2288

# Independently enumerate balanced colorings of the six actual center edges
# already displayed in A1_FINAL_ROLE_ENTRY. This implements only those six
# edges, not the 29 unspecified noncenter edges.
names=["p"]+[f"u{i}" for i in range(1,6)]+[f"B{i}" for i in range(1,5)]+[f"v{i}" for i in range(1,11)]
pos={v:i for i,v in enumerate(names)}
links=[["u1","u2","u3","B1"],["u4","u5","B2","v1"],
       ["p","B3","v2","v3"],["B1","B2","v4","v5"],
       ["B3","B4","v6","v7"],["B4","v8","v9","v10"]]
masks=[sum(1<<pos[v] for v in edge) for edge in links]
assert len(set(masks))==6
freq={v:sum(v in edge for edge in links) for v in names}
assert sorted(freq.values())==[1]*16+[2]*4
intersections=[(masks[i]&masks[j]).bit_count()
               for i,j in combinations(range(6),2)]
assert sum(intersections)==4 and max(intersections)==1
distribution={}
for red in combinations(range(20),10):
    mask=sum(1<<v for v in red)
    A=sum((mask&e)==e for e in masks)
    B=sum((mask&e)==0 for e in masks)
    distribution[A,B]=distribution.get((A,B),0)+1
assert sum(distribution.values())==den
bad=sum(count for (a,b),count in distribution.items() if max(a,b)>=2)
exact_pair_bound=2*sum(comb(12+j,2+j) for j in intersections)
assert exact_pair_bound==3740 and bad<=exact_pair_bound
out=dict(status="PASS",scope="four integer partitions and one already explicit center link; no noncenter H",
         denominator=den,intersection_partition_bounds=rows,
         worst_star_bound=worst,noncenter_edge_union_bound=nonstar,
         total_upper_bound=str(Fraction(total,den)),
         guaranteed_balanced_good_colorings=den-total,
         explicit_existing_link=dict(links=links,intersections=intersections,
                                     max_at_least_two_bad_count=bad,
                                     pair_union_bound=exact_pair_bound,
                                     AB_distribution={f"{a},{b}":n for (a,b),n in sorted(distribution.items())}),
         cpu_seconds=process_time()-start)
(DIR/"CHECK.json").write_text(json.dumps(out,indent=2)+"\n")
print({k:out[k] for k in ["status","total_upper_bound","guaranteed_balanced_good_colorings","cpu_seconds"]})
print(dict(explicit_star_bad=bad,explicit_star_pair_bound=exact_pair_bound))

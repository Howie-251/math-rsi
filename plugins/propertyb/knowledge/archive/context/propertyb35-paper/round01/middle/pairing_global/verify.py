"""Independent literal-edge and weighted vertex-dual verification; no geometry generation or search."""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as Q
from collections import Counter
import json,time
HERE=Path(__file__).parent
st=time.time();r=json.loads((HERE/'COUNTEREXAMPLE.json').read_text());v=r['vertices'];base=[frozenset(e) for e in r['base_edges']];extra=[frozenset(e) for e in r['extra_edges']];edges=base+extra
assert v==24 and len(base)==30 and len(extra)==5 and len(set(edges))==35 and all(len(e)==5 and min(e)>=0 and max(e)<v for e in edges)
degree=[sum(i in e for e in edges) for i in range(v)];assert degree==r['degrees'] and sorted(degree)==[7]*20+[8]*3+[11] and sum(degree)==175
pairs=list(combinations(range(v),2));lam={p:sum(set(p)<=e for e in base) for p in pairs};assert len(lam)==276 and min(lam.values())>=1
alpha=list(map(Q,r['weighted_matching_vertex_dual']));assert min(alpha)>=0 and sum(alpha)==2
assert all(Q(c-1)<=alpha[i]+alpha[j] for (i,j),c in lam.items());upper=v//2+sum(alpha)+len(extra);assert upper==19
colors=r['proper_coloring'];assert len(colors)==v and set(colors)<={0,1} and all({colors[i] for i in e}=={0,1} for e in edges)
result=dict(status='PASS',scope=__doc__,vertices=v,simple_five_edges=len(edges),covered_pairs=len(lam),minimum_degree=min(degree),degree_spectrum=dict(Counter(degree)),degree_sum=sum(degree),literal_base_edges=30,additional_edges=5,weighted_matching_dual_sum=str(sum(alpha)),all_pair_dual_inequalities=len(lam),universal_matching_hit_upper_bound=str(upper),explicit_coloring_valid=True,elapsed_seconds=time.time()-st)
(HERE/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))

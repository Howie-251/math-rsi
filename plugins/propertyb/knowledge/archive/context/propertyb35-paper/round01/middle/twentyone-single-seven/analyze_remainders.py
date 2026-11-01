"""Exact common unit8-pool consequences of the64 independently replayed residual four-views."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
HERE=Path(__file__).parent;rs=json.loads((HERE/'FOUR_REMAINDERS.json').read_text())['cases'];out=[]
for r in rs:
 ns={int(t):n for t,n in r['counts'].items()};cs=[sum(n for t,n in ns.items() if t>>(i+1)&1 and t>>(j+1)&1) for i,j in combinations(range(4),2)];blocks=[(t>>1).bit_count() for t,n in ns.items() if t&1 and t!=1 and n];assert all(n==1 for t,n in ns.items() if t&1 and t!=1);assert cs==r['neighbor_codegrees'];assert sorted(blocks)==sorted(map(len,r['partition']));assert max(cs)<=3 and cs.count(3)<=1 and max(blocks)<=3 and sum(cs)>=9
 if 3 in cs:assert cs.count(1) in (0,2,4)
 out.append(dict(id=r['id'],pair_codegrees=cs,unit_block_sizes=sorted(blocks),pair_sum=sum(cs),one_pairs=cs.count(1),three_pairs=cs.count(3)))
result=dict(status='PASS',source_residual_count=len(out),max_codegree_three_pairs_per_four=1,max_unit8_per_center_block=3,min_pair_sum_per_four=9,one_pair_counts_when_three_present=sorted({r['one_pairs'] for r in out if r['three_pairs']}),pair_multiset_counts={str(k):n for k,n in Counter(tuple(sorted(r['pair_codegrees'])) for r in out).items()},block_size_counts={str(k):n for k,n in Counter(tuple(r['unit_block_sizes']) for r in out).items()},all_pair2_residual_count=sum(all(c==2 for c in r['pair_codegrees']) for r in out),cases=out)
(HERE/'REMAINDER_STRUCTURE.json').write_text(json.dumps(result,indent=2)+'\n');print({k:v for k,v in result.items() if k!='cases'})

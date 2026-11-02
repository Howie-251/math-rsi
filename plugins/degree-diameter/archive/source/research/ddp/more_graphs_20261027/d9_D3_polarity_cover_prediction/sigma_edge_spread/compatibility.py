"""Explain the existing exact-cover failure using only its 32 saved masks."""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import time

start=time.process_time()
out=Path(__file__).resolve().parent
masks=[r['port_pair_mask'] for r in json.loads((out/'SIGMA_EDGES.json').read_text())]
hist=Counter((a&b).bit_count() for a,b in combinations(masks,2))
disjoint=[(i,j) for i,j in combinations(range(len(masks)),2) if not masks[i]&masks[j]]
triple=any(not (masks[i]|masks[j])&masks[k] for i,j in disjoint for k in range(j+1,len(masks)))
assert disjoint and not triple
result={'same_saved_mask_family':True,'sigma_edges':len(masks),
        'pair_intersection_size_histogram_in_port_pairs':dict(hist),
        'disjoint_edge_pair_count':len(disjoint),'disjoint_edge_triple_exists':triple,
        'maximum_pairwise_disjoint_blocks':2,
        'upper_bound_reason':'144 disjointpairs exist, but every possible thirdmask intersects at least one member. The compatibilitygraph has no triangle, so maximum pairwise-disjoint size is2.',
        'CPU_seconds':time.process_time()-start,'new_blocks':0,'coverage_optimization':False,'BFS':0}
(out/'COMPATIBILITY.json').write_text(json.dumps(result,indent=2)+'\n')

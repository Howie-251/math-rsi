"""Complete exact S5 agreement-one graph; no hypergraph enumeration."""
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path
from time import process_time
import json

start=process_time()
P=list(permutations(range(5)))
assert P[0]==tuple(range(5)) and len(P)==120
adj=[0]*120
for i,j in combinations(range(120),2):
    if sum(a==b for a,b in zip(P[i],P[j]))==1:
        adj[i]|=1<<j;adj[j]|=1<<i
assert set(x.bit_count() for x in adj)=={45}
# Left-composing by the inverse of a clique member preserves agreement.
# It suffices to enumerate ALL cliques in the 45 neighbours of identity.
counts=Counter(); witness={}
def all_cliques(C,R):
    counts[len(C)]+=1
    witness.setdefault(len(C),C)
    while R:
        bit=R&-R;R^=bit;v=bit.bit_length()-1
        all_cliques(C+[v],R&adj[v])
all_cliques([],adj[0])
assert dict(counts)=={0:1,1:45,2:420,3:1020,4:300}
idx=[0]+witness[max(counts)]
W=[list(P[i]) for i in idx]
agreements=[{'pair':[i,j],'positions':[k for k in range(5) if W[i][k]==W[j][k]]}
            for i,j in combinations(range(len(W)),2)]
assert all(len(x['positions'])==1 for x in agreements)
params=[]
for a in range(36):
    for b in range(36):
        ns=[42-3*a-b,-63+8*a+3*b,56-6*a-3*b,b,a]
        if min(ns)>=0 and sum(ns)==35:
            assert sum(j*x for j,x in enumerate(ns))==49
            assert sum(j*(j-1)//2*x for j,x in enumerate(ns))==56
            params.append({'a':a,'b':b,'n_0_through_4':ns,
                           'full_low_pairwise_intersect_forced':a>=6})
assert [(p['a'],p['b']) for p in params]==[(5,8),(6,5),(6,6),(7,3),(7,4),(8,0),(8,1),(8,2),(9,0)]
result={'status':'PASS','scope':'all 120 S5 permutations and all normalized cliques; 9 necessary scalar types, not actual H classification',
        'vertices':120,'edges':sum(x.bit_count() for x in adj)//2,
        'identity_neighbours':45,'normalized_cliques_by_size':dict(sorted(counts.items())),
        'normalized_cliques_enumerated':sum(counts.values()),'maximum_agreement_one_family':1+max(counts),
        'witness':W,'witness_pair_agreements':agreements,'necessary_parameters':params,
        'cpu_seconds':process_time()-start}
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['necessary_parameters','witness_pair_agreements']},indent=2))

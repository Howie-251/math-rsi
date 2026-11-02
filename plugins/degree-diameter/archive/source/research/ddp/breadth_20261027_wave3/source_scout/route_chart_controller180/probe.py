from pathlib import Path
from itertools import permutations,combinations,product
from collections import Counter,deque
import json,time

P=Path(__file__).resolve().parent
start=time.process_time()
perms=[p for p in permutations(range(5)) if sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2==0]
assert len(perms)==60 and perms[0]==tuple(range(5))
idx={p:i for i,p in enumerate(perms)}
small=[[idx[tuple(p[q[i]] for i in range(5))] for q in perms] for p in perms]
table=[[60*((g//60+h//60)%3)+small[g%60][h%60] for h in range(180)] for g in range(180)]
inverses=[next(h for h in range(180) if table[g][h]==table[h][g]==0) for g in range(180)]
pair_pool=[g for g in range(1,180) if g<inverses[g]]
assert len(pair_pool)==82
words=[w for w in product(range(4),repeat=5) if all(w[i+1]!=(w[i]^1) for i in range(4))]
assert len(words)==324
hist=Counter();best=None;hit=None;tested=0
for a,b in combinations(pair_pool,2):
    S=[a,inverses[a],b,inverses[b]]
    seen={}
    for w in words:
        g=0
        for c in w:g=table[g][S[c]]
        seen.setdefault(g,w)
    score=len(seen);hist[score]+=1;tested+=1
    if best is None or score>best['exact_NB5_reached']:
        best=dict(S=S,exact_NB5_reached=score,missing=[g for g in range(180) if g not in seen],candidate_index=tested)
    if score==180:
        hit=dict(S=S,route_words={str(g):list(seen[g]) for g in range(180)})
        break
    if time.process_time()-start>9.0:break

result=dict(status='FOUND_EXACT_NB5_CONTROLLER' if hit else ('COMPLETE_TWO_INVERSE_PAIR_CONTROLLER_SCOPE_NO_HIT' if tested==3321 else 'CPU_STOP_SAVED_CURSOR'),group='A5 direct_product C3',group_order=180,vertex_encoding='60*t+permutation_index',controller_degree=4,controller_target='Every ordered pair has a reduced walk of exactly5 edges',candidate_scope='All unordered pairs of distinct nonidentity noninvolution inverse-pairs in this fixed group',candidate_scope_count=3321,candidates_checked=tested,best=best,histogram=dict(sorted(hist.items())),CPU_seconds=time.process_time()-start,prospective_lift=dict(field=3,fiber_dimension=5,degree=12,diameter_bound=5,n=43740,saved_baseline=42342),full_lift_constructed=False,found_new_lower_bound=False,hit=hit)
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(P/'group.json').write_text(json.dumps(dict(permutations=perms,product_convention='p composed with q; t coordinates add mod3',inverse=inverses))+'\n')
if hit:
    S=hit['S'];edges=sorted({tuple(sorted((g,table[g][s]))) for g in range(180) for s in S})
    assert len(edges)==360 and all(u!=v for u,v in edges)
    (P/'controller.edges').write_text('180 360\n'+''.join(f'{u} {v}\n' for u,v in edges))
    adj=[[] for _ in range(180)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    d=[-1]*180;d[0]=0;queue=deque([0])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if d[v]<0:d[v]=d[u]+1;queue.append(v)
    assert -1 not in d and max(d)<=5
    (P/'controller_identity_BFS.json').write_text(json.dumps(dict(distances=d,eccentricity=max(d),regular_degree=4,root=0,proven_left_regular_action=True))+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['histogram','hit','best']},ensure_ascii=False))
print('best',best)

from pathlib import Path
from itertools import combinations,product
from collections import Counter,deque
import json,time
P=Path(__file__).resolve().parent;t=time.process_time()
p=31;k=6;r=26
assert pow(r,6,p)==1 and all(pow(r,j,p)!=1 for j in range(1,6))
rp=[pow(r,i,p) for i in range(k)]
table=[[p*((g//p+h//p)%k)+(g%p+rp[g//p]*(h%p))%p for h in range(p*k)] for g in range(p*k)]
inv=[next(h for h in range(186) if table[g][h]==table[h][g]==0) for g in range(186)]
pairs=[g for g in range(1,186) if g<inv[g]];assert len(pairs)==77
words=[w for w in product(range(4),repeat=5) if all(w[i+1]!=(w[i]^1) for i in range(4))];assert len(words)==324
hist=Counter();best=None;hit=None;tested=0
for a,b in combinations(pairs,2):
 S=[a,inv[a],b,inv[b]];seen={}
 for w in words:
  g=0
  for c in w:g=table[g][S[c]]
  seen.setdefault(g,w)
 z=len(seen);hist[z]+=1;tested+=1
 if best is None or z>best['exact_NB5_reached']:best=dict(S=S,exact_NB5_reached=z,missing=[g for g in range(186) if g not in seen],candidate_index=tested)
 if z==186:hit=dict(S=S,route_words={str(g):list(seen[g]) for g in range(186)});break
 if time.process_time()-t>8.0:break
result=dict(status='FOUND_EXACT_NB5_CONTROLLER' if hit else ('COMPLETE_TWO_INVERSE_PAIR_CONTROLLER_SCOPE_NO_HIT' if tested==2926 else 'CPU_STOP_SAVED_CURSOR'),group='F31 semidirect_26 C6',group_order=186,encoding='x+31*i',product='(x,i)(y,j)=(x+26^i*y mod31,i+j mod6)',controller_degree=4,candidate_scope='All two distinct noninvolution inverse-pairs, with fixedpointfree inverse labels',scope_size=2926,candidates_checked=tested,best=best,histogram=dict(sorted(hist.items())),CPU_seconds=time.process_time()-t,prospective_lift=dict(n=45198,degree=12,diameter_bound=5,saved_baseline=42342),full_lift_constructed=False,found_new_lower_bound=False,hit=hit)
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
if hit:
 S=hit['S'];edges=sorted({tuple(sorted((g,table[g][s]))) for g in range(186) for s in S});assert len(edges)==372
 (P/'controller.edges').write_text('186 372\n'+''.join(f'{u} {v}\n' for u,v in edges))
print(json.dumps({key:value for key,value in result.items() if key not in ['best','histogram','hit']}));print('best',best)

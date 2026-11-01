"""Integer weighted-matching kernel and the one frozen literal-H control.
No H search, LP, MILP, or external matching library.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import json
import time

started = time.process_time()
here = Path(__file__).resolve().parent
source = here / '../../../middle/pairing_global/COUNTEREXAMPLE.json'
a = json.loads(source.read_text())
E = list(map(frozenset, a['edges']))
assert len(E) == len(set(E)) == 35 and all(len(e)==5 for e in E)
lamb = Counter(p for e in E for p in combinations(sorted(e), 2))
assert len(lamb)==276 and min(lamb.values())>=1
w = [[0]*24 for _ in range(24)]
for (u,v), c in lamb.items(): w[u][v]=w[v][u]=c-1
rows = list(map(sum,w))
assert sum(rows)==148 and min(rows)>=5 and all(d%4==1 for d in rows)
assert all(rows[v]==4*sum(v in e for e in E)-23 for v in range(24))

@lru_cache(None)
def opt(mask):
    if not mask: return (0,1)
    bit=mask&-mask; u=bit.bit_length()-1; rest=mask^bit
    best=-1; count=0; todo=rest
    while todo:
        bj=todo&-todo; todo^=bj; v=bj.bit_length()-1
        val,num=opt(rest^bj); val+=w[u][v]
        if val>best: best,count=val,num
        elif val==best: count+=num
    return best,count

full=(1<<24)-1
best,count=opt(full)
profile_cpu=time.process_time()-started

def optimal(mask, pairs=()):
    if not mask:
        yield pairs; return
    bit=mask&-mask; u=bit.bit_length()-1; rest=mask^bit; target=opt(mask)[0]
    todo=rest
    while todo:
        bj=todo&-todo; todo^=bj; v=bj.bit_length()-1
        if w[u][v]+opt(rest^bj)[0]==target:
            yield from optimal(rest^bj,pairs+((u,v),))

def actual(P):
    pairsets=list(map(frozenset,P))
    q=[sum(p<=e for p in pairsets) for e in E]
    assert all(x<=2 for x in q)
    W=sum(w[u][v] for u,v in P)
    t=q.count(2); h=35-q.count(0)
    assert h==12+W-t
    return {'W':W,'t':t,'h':h,'q_distribution':dict(sorted(Counter(q).items()))}

hist=Counter(); example={}; checked=0
# Enumerate only all maximizers of this fixed 24-point control if the exact
# count already found by DP is small; do not expand to other input graphs.
complete = count<=250000
for P in optimal(full):
    val=actual(P); key=(val['t'],val['h']); hist[key]+=1
    example.setdefault(key,[list(p) for p in P]); checked+=1
    if not complete and checked>=1000: break
known=[(0,4),(1,6),(2,21),(3,7),(5,16),(8,18),(9,10),(11,14),(12,19),(13,15),(17,20),(22,23)]
# Finite adversarial kernel behind the proof: on the 12 unmatched vertices,
# for a weight-one matched edge, the two 0/1 neighbourhoods may coexist only
# as one common singleton. Thus each fork contributes 2 instead of at most12.
kernels=[]
for forks in range(7):
    cross_cap=12*(6-forks)+2*forks
    if cross_cap>=60:
        chosen=6+forks
        chosen_cross=2*forks
        required_internal=5*chosen-chosen_cross
        kernels.append({'forks':forks,'cross_cap':cross_cap,'chosen_vertices':chosen,
                        'required_internal_degree':required_internal,
                        'available_internal_degree_at_most':28,
                        'contradiction':required_internal>28})
assert len(kernels)==2 and all(x['contradiction'] for x in kernels)
# A local 5-uniform trade shows why pair-codegrees do not determine t.
# It is not a new 24/35 input and does not refute a universal 19-hit theorem.
trade_A = [frozenset((0,1)+t) for t in [(2,3,4),(2,5,6),(3,5,7),(4,6,7)]]
trade_B = [frozenset((0,1)+t) for t in [(2,3,5),(2,4,6),(3,4,7),(5,6,7)]]
trade_P = list(map(frozenset,[(0,2),(3,4),(5,6),(1,8),(7,9)]))
trade_lamb = lambda family: Counter(p for e in family for p in combinations(sorted(e),2))
assert trade_lamb(trade_A)==trade_lamb(trade_B)
trade_q = [[sum(p<=e for p in trade_P) for e in family] for family in [trade_A,trade_B]]
assert trade_q==[[2,2,0,0],[1,1,1,1]]
result={'status':'PASS','scope':'one frozen literal H; all optimal weighted matchings if enumeration_complete; no new H',
        'weight_sum':sum(rows)//2,'weighted_degree_rows':rows,'max_weight':best,
        'number_max_weight_perfect_matchings':count,'DP_states':opt.cache_info().currsize,
        'DP_profile_cpu_seconds':profile_cpu,'enumeration_complete':complete,
        'enumerated_maximizers':checked,'optimal_t_h_distribution':[
            {'t':t,'h':h,'count':c,'example':example[t,h]} for (t,h),c in sorted(hist.items())],
        'known_19hit_matching':{'pairs':known,**actual(known)},'integer_proof_fork_kernel':kernels,
        'same_pair_marginals_trade':{'A':[sorted(e) for e in trade_A],
            'B':[sorted(e) for e in trade_B],'P':[sorted(p) for p in trade_P],
            'pair_codegrees_equal':True,'A_q':trade_q[0],'B_q':trade_q[1]},
        'cpu_seconds':time.process_time()-started}
if complete: assert checked==count
(here/'INTEGER_EXCESS_MATCHING_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['weighted_degree_rows','optimal_t_h_distribution','known_19hit_matching','integer_proof_fork_kernel']},indent=2))
print('t/h/count',[(t,h,c) for (t,h),c in sorted(hist.items())])
print('known',actual(known))

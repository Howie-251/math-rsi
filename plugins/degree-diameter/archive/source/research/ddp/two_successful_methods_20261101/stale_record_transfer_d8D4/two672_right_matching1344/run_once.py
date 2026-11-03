"""One complete RIGHT-matching domain on the published Sampels 672 source."""
from pathlib import Path
import json
import math
import resource
import time
from collections import deque

HERE = Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_CPU, (8, 8))
START = time.process_time()
N, NN = 672, 1344
S_PAIRS = [(2,73),(4,23),(5,54),(1,22),(5,71),(1,31),(3,42)]
S = [112*a+b for a,b in S_PAIRS]
FULL = (1 << N)-1


def save(name, d):
    (HERE/name).write_text(json.dumps(d, ensure_ascii=False, indent=2)+'\n')


def cpu():
    return time.process_time()-START


def mul(u, v):
    a,b = divmod(u,112)
    c,d = divmod(v,112)
    return 112*((a+c) % 6)+(b*POW[c]+d) % 112


if (HERE/'ATTEMPT.json').exists():
    raise RuntimeError('one-shot already attempted; no restart')
save('ATTEMPT.json', dict(status='STARTED', CPU_cap=10,
     prior_readgate_charge=.8, preparation_charge=.4))
POW = [pow(39,k,112) for k in range(6)]
assert math.gcd(39,112) == 1 and pow(39,6,112) == 1
assert len(set(S)) == 7 and 0 not in S
TABLE = [[mul(u,v) for v in range(N)] for u in range(N)]
assert all(any(TABLE[s][t] == TABLE[t][s] == 0 for t in S) for s in S)
L = [{0}]
for length in range(1,5):
    L.append({TABLE[u][v] for u in L[-1] for v in S})
balls = [set().union(*L[:k+1]) for k in range(5)]
save('SOURCE_BINDING.json', dict(group='C6_RIGHT_semidirect39_Z112',
     operation='(a,b)(c,d)=(a+c mod6,b*39^c+d mod112)',
     canonical_labels='112*a+b; not claimed to be author raw labels',
     S=S_PAIRS, degree=7, n=672, m=2352,
     inverse_pairs_bound=True, exact_word_endpoint_counts=[len(z) for z in L],
     identity_closed_ball_counts=[len(z) for z in balls],
     source_D4_identity_gate=len(balls[4]) == N,
     new_source_reproduction_not_new_record=True, old684_DP_BFS_reruns=0))
if len(balls[4]) != N:
    save('RESULT.json', dict(status='UNKNOWN_PUBLISHED_RECIPE_D4_BINDING_DISCREPANCY',
         actual_identity_R4=len(balls[4]), graph_generated=False))
    raise RuntimeError('published recipe source binding did not give R4=672')
src = [sorted(TABLE[u][s] for s in S) for u in range(N)]
source_edges = [(u,v) for u in range(N) for v in src[u] if u < v]
assert len(source_edges) == 2352
with (HERE/'SOURCE_GRAPH_CANONICAL.edges').open('w') as f:
    f.write('672 2352\n')
    for u,v in source_edges:
        f.write(f'{u} {v}\n')
checked, hit, timeout = 0, None, False
with (HERE/'ALL_T_RESULTS.tsv').open('w') as rows:
    rows.write('t\tphase\tnormal\tcovered\tfirst_missing\tphase_counts\n')
    for t in range(N):
        if cpu() > 7.0:
            timeout = True
            break
        bits = 0
        for a in range(4):
            for b in range(4-a):
                for x in L[a]:
                    xt = TABLE[x][t]
                    for y in L[b]:
                        bits |= 1 << TABLE[xt][y]
        checked += 1
        missing = FULL ^ bits
        first = (missing & -missing).bit_length()-1 if missing else -1
        phase = [((bits >> (112*k)) & ((1 << 112)-1)).bit_count() for k in range(6)]
        rows.write(f'{t}\t{t//112}\t{t%112}\t{bits.bit_count()}\t{first}\t'+','.join(map(str,phase))+'\n')
        if not missing:
            hit = t
            break
if hit is not None:
    matching = [TABLE[u][hit] for u in range(N)]
    assert len(set(matching)) == N
    edges = source_edges + [(u+N,v+N) for u,v in source_edges]
    edges += [(u,N+matching[u]) for u in range(N)]
    assert len(edges) == len(set(edges)) == 5376
    with (HERE/'candidate_d8_D4_n1344.edges').open('w') as f:
        f.write('1344 5376\n')
        for u,v in sorted(edges):
            f.write(f'{u} {v}\n')
    adj = [[] for _ in range(NN)]
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    assert all(len(z) == len(set(z)) == 8 for z in adj)
    fullpass, roots = True, 0
    with (HERE/'CANDIDATE_ALL_ROOT_STATS.tsv').open('w') as f:
        f.write('root\teccentricity\n')
        for root in range(NN):
            if cpu() > 7.0:
                fullpass = False
                timeout = True
                break
            dist = [-1]*NN
            dist[root] = 0
            queue = deque([root])
            while queue:
                u = queue.popleft()
                for v in adj[u]:
                    if dist[v] < 0:
                        dist[v] = dist[u]+1
                        queue.append(v)
            ecc = max(dist) if -1 not in dist else NN
            f.write(f'{root}\t{ecc}\n')
            roots += 1
            if ecc > 4:
                fullpass = False
                break
    save('PARAMETERS.json', dict(n=1344,m=5376,maxdegree=8,
         source='SOURCE_GRAPH_CANONICAL.edges',S=S_PAIRS,t=divmod(hit,112),
         t_label=hit,matching=matching,old_edges_kept=4704,new_edges=672,
         producer_checked_roots=roots,producer_allroots_pass=fullpass,
         fresh_acceptance='PENDING',new_graph_parameter_Lean=[0,0,0]))
    status = 'CANDIDATE_1344_PRODUCER_ALLROOT_PASS_PENDING_FRESH' if fullpass else 'CANDIDATE_PENDING_COMPLETE_VERIFICATION'
else:
    status = 'UNKNOWN_CPU_CAP' if timeout else 'COMPLETE_NO_FULL672_RIGHTMATCHING_DOMAIN'
result = dict(status=status, checked_parameters=checked, full_domain_size=672,
     source_D4_bound_by_identity_R4=True, source_reproduction_count=1,
     source_reproduction_not_new_graph_result=True, actual_native_CPU=cpu(),
     prior_readgate_charge=.8,new_preparation_charge=.4,
     cumulative_case_CPU=1.2+cpu(),case_CPU_cap=10,hit_t=hit,
     complete_domain_negative=hit is None and not timeout,
     graph_generated=hit is not None, new_graph_parameter_Lean=[0,0,0],
     scope='fixedSampels672RIGHTsource; allM(h)=h*t; notarbitrarymatching/general8D4',
     terminal=True,no_automatic_other_S_action_source_or_t_window=True)
save('RESULT.json', result)
save('TERMINAL.json', result)
print(json.dumps(result,ensure_ascii=False),flush=True)

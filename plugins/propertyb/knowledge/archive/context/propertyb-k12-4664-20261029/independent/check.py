"""Independent complete coverage reconstruction and selected Fraction probability replay.
No imports from the accepted driver's scanner or certificate implementations.
Fraction formula implementation reused from the independently written M4660 audit.
"""
import json,time
from pathlib import Path
from math import comb
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from collections import Counter
ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT.parent/'COMPLETE.json').read_text())
M=4663; K=12; begin=time.monotonic(); cpu=time.process_time()
def C(n, r):
    return comb(n, r) if n >= 0 and 0 <= r <= n else 0

def ceil(a, b):
    return -(-a // b)

def counts_for(mode, p):
    if mode == 'none':
        return [M]
    if mode == 'one':
        d, = p
        return [M - d, d]
    if mode == 'two':
        d, e = p
        return [M - d - e + 1, d - 1, e - 1, 1]
    (a, b, c), triple = p
    return [M - a - b - c + 2, a - 1, b - 1, 0, c - 1, 0, 0, 1] if triple else [M - a - b - c + 3, a - 2, b - 2, 1, c - 2, 1, 1, 0]

def exact(v, mode, p):
    n = counts_for(mode, p)
    s = (len(n) - 1).bit_length()
    N = v - s
    locks = [[], [v // 2], [v // 2, v // 2 + 1], [v // 2 - 1, v // 2, v // 2 + 1]][s]
    total = Q(0)
    overlap = max(0, ceil(M * C(12, 2) - C(v, 2), C(11, 2))) if not s else None
    for h in range(1, v + 1):
        a = h - 1 - sum((t < h for t in locks))
        b = v - h - sum((t > h for t in locks))
        L = sum((1 << j for j, t in enumerate(locks) if t < h))
        R = sum((1 << j for j, t in enumerate(locks) if t > h))
        j = locks.index(h) if h in locks else None
        last = []
        first = []
        pair = {}
        for x in range(len(n)):
            r = 12 - x.bit_count()
            if j is None:
                last.append(Q(r * C(a, r - 1), N * C(N - 1, r - 1)) if r >= 1 and x & ~L == 0 else Q(0))
                first.append(Q(r * C(b, r - 1), N * C(N - 1, r - 1)) if r >= 1 and x & ~R == 0 else Q(0))
            else:
                last.append(Q(C(a, r), C(N, r)) if x & 1 << j and x & ~(1 << j) & ~L == 0 else Q(0))
                first.append(Q(C(b, r), C(N, r)) if x & 1 << j and x & ~(1 << j) & ~R == 0 else Q(0))
            for y in range(len(n)):
                z = 12 - y.bit_count()
                w = Q(0)
                if j is None:
                    if x & ~L == 0 and y & ~R == 0 and (min(r, z) >= 1) and (r + z - 1 <= N):
                        w = Q(C(a, r - 1) * C(b, z - 1), N * C(N - 1, r - 1) * C(N - r, z - 1))
                elif x & y == 1 << j and x & ~(1 << j) & ~L == 0 and (y & ~(1 << j) & ~R == 0) and (r + z <= N):
                    w = Q(C(a, r) * C(b, z), C(N, r) * C(N - r, z))
                pair[x, y] = w
        A = sum((nx * w for nx, w in zip(n, last)), Q(0))
        B = sum((nx * w for nx, w in zip(n, first)), Q(0))
        crit = sum((nx * (ny - int(x == y)) * pair[x, y] for x, nx in enumerate(n) for y, ny in enumerate(n)), Q(0))
        if not s:
            crit -= 2 * overlap * pair[0, 0]
        if j is not None:
            degree = sum((nx for x, nx in enumerate(n) if x & 1 << j))
            needed = ceil(11 * degree - (v - 1), 10)
            assert needed >= 0
            capacities = []
            for x, nx in enumerate(n):
                for y in range(x, len(n)):
                    if x & 1 << j and y & 1 << j:
                        cap = C(nx, 2) if x == y else nx * n[y]
                        if cap:
                            capacities.append((pair[x, y] + pair[y, x], cap))
            for weight, cap in sorted(capacities):
                take = min(needed, cap)
                crit -= take * weight
                needed -= take
                if needed == 0:
                    break
            assert needed == 0
        assert min(A, B, crit) >= 0
        total += min(A, B, crit)
    return total

def check_counts(mode,p):
    ns=counts_for(mode,p);assert sum(ns)==M and min(ns)>=0
    s=(len(ns)-1).bit_length()
    degrees=[sum(n for mask,n in enumerate(ns) if mask&(1<<i)) for i in range(s)]
    if mode=='one':assert degrees==list(p)
    elif mode=='two':assert degrees==list(p)
    elif mode=='three':assert degrees==list(p[0])
    for i in range(s):
        for j in range(i+1,s):assert sum(n for mask,n in enumerate(ns) if mask&(1<<i) and mask&(1<<j))==1

# Independently reconstruct original-input vertex reduction, including newly opened 91,92.
vertices=[]
for v in range(23,12*M+1):
    if v*ceil(v-1,11)>12*M:continue
    if M*(C(v//2,12)+C((v+1)//2,12))<C(v,12):continue
    assert C(v,12)>=M
    vertices.append(v)
assert vertices==list(range(91,783))==DATA['candidate_v']
assert [r['v'] for r in DATA['rows']]==vertices
assert 783*ceil(782,11)>12*M
prefix=json.loads((ROOT.parent/'CONDITIONAL.json').read_text())
tail=json.loads((ROOT.parent/'TAIL.json').read_text())
assert prefix['rows']+tail['rows']==DATA['rows']
assert not DATA['failures'] and not prefix['failures'] and not tail['failures']
assert DATA['complete'] and tail['start_v']==prefix['rows'][-1]['v']+1==694
counts=Counter();summaries=[];candidates=[];all_parameters=0;third_branches=0
for row in DATA['rows']:
    v=row['v'];d0=ceil(v-1,11);upper=12*M//v;n=0;local=Counter();leaves=[]
    if row['mode']=='none':
        n=1;local['none']=1;leaves=[(row['worst_z'],'none',(),{'source':'row'})]
    elif row['mode']=='hybrid123':
        assert [p['d'] for p in row['parts']]==list(range(d0,upper+1))
        for part in row['parts']:
            d=part['d']
            if part['mode']=='one':
                check_counts('one',(d,));n+=1;local['one']+=1
                leaves.append((part['z'],'one',(d,),{'d':d}));continue
            assert part['mode']=='two-or-three'
            sd=2*v-2-11*d;assert sd>0 and part['sd']==sd
            # Reconstruct B by first strict total-degree violation, independently of division.
            B=next(b for b in range(d,M+1) if v*d+sd*(b+1-d)>12*M)
            assert part['B']==B
            assert [z['e'] for z in part['sub']]==list(range(d,B+1))
            for sub in part['sub']:
                e=sub['e']
                if sub['mode']=='two':
                    check_counts('two',(d,e));n+=1;local['two']+=1
                    leaves.append((sub['z'],'two',(d,e),{'d':d,'e':e}));continue
                assert sub['mode']=='three';third_branches+=1
                # Derive the joint unit-neighbour pool by excluding the two existing locks.
                pool=v-2-(11*d-v+1)-(11*e-v+1)
                R=12*M-v*d-(e-d)
                assert pool>0 and R>=0 and (sub['pool'],sub['R'])==(pool,R)
                F=next(f for f in range(d,M+1) if pool*(f+1-d)>R)
                assert sub['F']==F
                for f in range(d,F+1):
                    for flag in (False,True):
                        check_counts('three',(tuple(sorted((d,e,f))),flag));n+=1;local['three']+=1
                assert sub['profiles']==2*(F-d+1)
                wp=sub['worst_profile'];assert wp['mode']=='three' and wp['d']==d and wp['e']==e
                assert d<=wp['f']<=F and wp['sorted']==sorted((d,e,wp['f'])) and isinstance(wp['triple'],bool)
                leaves.append((sub['worst_z'],'three',(tuple(wp['sorted']),wp['triple']),{'d':d,'e':e,'f':wp['f'],'pool':pool,'F':F}))
        assert dict(local)=={k:z for k,z in row['counts'].items() if z}
    else:
        assert row['mode']=='three-global';assert row['d0']==d0
        # Exhaust the complete D domain; compare the least valid value.
        D=next(D for D in range(d0,M+1) if (D+1)*v>12*M and 22*((D+1)*v-12*M)>(11*(D+1)-v+2)**2)
        assert row['D']==D
        for ds in combinations_with_replacement(range(d0,D+1),3):
            for flag in (False,True):check_counts('three',(ds,flag));n+=1;local['three-global']+=1
        wp=row['worst_profile'];assert len(wp[0])==3 and sorted(wp[0])==wp[0] and all(d0<=x<=D for x in wp[0]) and isinstance(wp[1],bool)
        leaves=[(row['worst_z'],'three',(tuple(wp[0]),wp[1]),{'source':'global','D':D})]
    assert row['profiles']==n
    assert max(z[0] for z in leaves)==row['worst_z']<DATA['S']
    assert all(0<=z[0]<DATA['S'] for z in leaves)
    # Preserve only maxima per probability mode, sufficient to select independent replay cases.
    for kind in {z[1] for z in leaves}:
        best=max((z for z in leaves if z[1]==kind),key=lambda z:z[0]);candidates.append((v,*best))
    counts.update(local);all_parameters+=n
    summaries.append(dict(v=v,mode=row['mode'],d0=d0,minimum_degree_upper=upper,profiles=n,counts=dict(local)))
assert all_parameters==664355
coverage=dict(status='PASS',vertex_domain=[91,782],vertex_count=len(vertices),profile_instances=all_parameters,counts=dict(counts),conditional_third_degree_pair_branches=third_branches,all_trace_vectors_verified=True,per_vertex=summaries,cpu_seconds=time.process_time()-cpu)
(ROOT/'DOMAIN_CHECK.json').write_text(json.dumps(coverage,indent=2)+'\n')
print('COVERAGE PASS',all_parameters,dict(counts),'CPU',round(time.process_time()-cpu,3),flush=True)
# Global worst of each probability mode; both sides of accepted-driver switches;
# both sides of third-lock first use and last conditional/global switch.
selected=[]
for kind in ('none','one','two','three'):
    selected.append(max((x for x in candidates if x[2]==kind),key=lambda x:x[1]))
third_vs=[x[0] for x in candidates if x[2]=='three' and x[0]<694]
selected_vs={91,92,497,498,693,694,782,min(third_vs)-1,min(third_vs)}
selected.extend(x for x in candidates if x[0] in selected_vs)
# Endpoint trace tests at the global-tail switch and final vertex count.
for v in (694,782):
    r=DATA['rows'][v-91];D=r['D'];lo=ceil(v-1,11)
    for ds in ((lo,lo,lo),(D,D,D)):
        for flag in (False,True):selected.append((v,r['worst_z'],'three',(ds,flag),{'source':'global-endpoint'}))
# Stress the conditional new-lock pool independently at its smallest pool and largest F.
conditional_leaves=[(r['v'],p['d'],sub) for r in prefix['rows'] if r['mode']=='hybrid123' for p in r['parts'] if p['mode']=='two-or-three' for sub in p['sub'] if sub['mode']=='three']
for v,d,sub in [min(conditional_leaves,key=lambda x:x[2]['pool']),max(conditional_leaves,key=lambda x:x[2]['F'])]:
    e=sub['e'];f=sub['F']
    for flag in (False,True):selected.append((v,sub['worst_z'],'three',(tuple(sorted((d,e,f))),flag),{'source':'conditional-pool-endpoint','d':d,'e':e,'f':f,'pool':sub['pool'],'F':sub['F']}))
seen=set();replays=[]
for v,upper,mode,p,meta in selected:
    key=(v,mode,json.dumps(p))
    if key in seen:continue
    seen.add(key)
    value=exact(v,mode,p)
    assert value<=Q(upper,DATA['S'])<1
    replays.append(dict(v=v,mode=mode,profile=p,metadata=meta,exact_numerator=str(value.numerator),exact_denominator=str(value.denominator),saved_upper_numerator=upper,denominator=DATA['S'],strict=True,exact_below_saved_upper=True))
    print('FRACTION PASS',v,mode,p,'CPU',round(time.process_time()-cpu,3),flush=True)
result=dict(status='PASS_MODULO_IMPORTS',review_independence='same-family',acceptance_status='provisional',coverage=coverage|{'per_vertex':'DOMAIN_CHECK.json'},fraction_replay_count=len(replays),fraction_replays=replays,complete_second_probability_replay=False,imports=['minimum-counterexample pair-cover reduction','conditional permutation and weighted bad-pair certificate theorem','general low-degree independent-lock selection lemma'],cpu_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-begin)
(ROOT/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print('DONE',len(replays),'CPU',result['cpu_seconds'],flush=True)

"""Independent six-point seed and extension generation; independent row arithmetic.
Only original canonicalization is reused, with each returned relabeling verified.
No old seed data and no original probability-weight/quota code are used to compute.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as F
from math import comb
from functools import lru_cache
import sys,json,time
P=Path(__file__).resolve().parent; R=P.parents[3]
S=R/'context/propertyb34/round01/high-math'
sys.dont_write_bytecode=True;sys.path.insert(0,str(S))
from unit_catalogue import canonical
from bare_layout import BareLayout
start=time.monotonic()

def clique_pairs(t):
    return frozenset(combinations([i for i in range(t.bit_length()) if t>>i&1],2))

def complete(big,n):
    used=set();out=list(big)
    for t in big:
        pp=clique_pairs(t);assert not used&pp;used.update(pp)
    out += [(1<<i)|(1<<j) for i,j in combinations(range(n),2) if (i,j) not in used]
    return tuple(sorted(out))

def canon(big,n):
    key,perm=canonical(big,n,with_perm=True)
    assert sorted(perm)==list(range(n))
    image=tuple(sorted(sum(1<<perm[i] for i in range(n) if t>>i&1) for t in big))
    assert image==key
    return key

# All subsets of the 41 possible 3-,4-,5-blocks whose pair sets are disjoint.
# An increasing index gives every compatible family exactly once.
candidates=[t for t in range(64) if 3<=t.bit_count()<=5]
pp=[clique_pairs(t) for t in candidates]
seed=[]
def seeds(j,used,chosen):
    seed.append(chosen)
    for k in range(j,len(candidates)):
        if not used&pp[k]:seeds(k+1,used|pp[k],chosen+(candidates[k],))
seeds(0,frozenset(),())
assert len(seed)==352
level={canon(b,6) for b in seed}
old=json.loads((R/'context/propertyb34-hour1-20261013/high-math/MIXED_SIX_v24_low6_badnone.json').read_text())
oldlevel={canon(tuple(int(t) for t in x['counts'] if int(t).bit_count()>=3),6) for x in old['results']}
assert level==oldlevel and len(level)==9
seed_feasible=[]
for b in seed:
    B=complete(b,6);single=[6-sum(bool(t>>i&1) for t in B) for i in range(6)]
    empty=34-len(B)-sum(single)
    assert min(single+[empty])>=0
    seed_feasible.append((min(single),empty))
coverage=[dict(n=6,labelled=len(seed),orbits=len(level),old_seed_equal=True,
               minimum_single=min(x[0] for x in seed_feasible),minimum_empty=min(x[1] for x in seed_feasible))]

# Independently enumerate every subset of old full blocks, size <=4, whose
# vertex sets are pairwise disjoint. Add new vertex to exactly those blocks.
for n in (6,7,8):
    nxt=set();raw=0
    for oldbig in sorted(level):
        cand=[t for t in complete(oldbig,n) if t.bit_count()<=4]
        def visit(j,used,chosen):
            global raw
            new=tuple(t for t in oldbig if t not in chosen)+tuple(t|(1<<n) for t in chosen)
            nxt.add(canon(new,n+1));raw+=1
            for k in range(j,len(cand)):
                if not cand[k]&used:visit(k+1,used|cand[k],chosen+(cand[k],))
        visit(0,0,())
    original=json.loads((S/f'UNIT_CATALOGUE_{n+1}.json').read_text())
    assert nxt=={tuple(z) for z in original['orbits']}
    coverage.append(dict(n=n+1,parents=len(level),raw_extensions=raw,orbits=len(nxt),original_equal=True))
    level=nxt
    print('coverage',coverage[-1],flush=True)

def C(n,k):return comb(n,k) if 0<=k<=n else 0

@lru_cache(None)
def weights(pos,k,t,u=-1):
    """Direct binomial formulas, independent of multilock/BareLayout."""
    N=25-len(pos);left=sum(1<<i for i,p in enumerate(pos) if p<k)
    right=sum(1<<i for i,p in enumerate(pos) if p>k)
    pivot=sum(1<<i for i,p in enumerate(pos) if p==k)
    a=k-1-left.bit_count();b=25-k-right.bit_count();r=5-t.bit_count()
    if u<0:
        vals=[]
        for allowed,z in ((left,a),(right,b)):
            if pivot:
                vals.append(F(C(z,r),C(N,r)) if t&pivot and not (t^pivot)&~allowed else F())
            else:
                vals.append(F(r*C(z,r-1),N*C(N-1,r-1)) if r>=1 and not t&~allowed else F())
        return tuple(vals)
    q=5-u.bit_count()
    if pivot:
        if t&u!=pivot or (t^pivot)&~left or (u^pivot)&~right or r+q>N:return F()
        return F(C(a,r)*C(b,q),C(N,r)*C(N-r,q))
    if r<1 or q<1 or t&u or t&~left or u&~right or r+q-1>N:return F()
    return F(C(a,r-1)*C(b,q-1),N*C(N-1,r-1)*C(N-r,q-1))

def quota_loss(ns,pos,i):
    # Expand the seven actual incident edge copies; independently try every
    # subset of the 21 unordered pair slots meeting both quotas.
    bit=1<<i;copies=[t for t,m in ns.items() if t&bit for _ in range(m)]
    assert len(copies)==7
    pure=max(0,(4*ns.get(bit,0)-(25-len(pos))+2)//3)
    target=max(2,pure)
    slots=[(weights(pos,pos[i],t,u)+weights(pos,pos[i],u,t),t==u==bit)
           for t,u in combinations(copies,2)]
    valid=[sum((slots[j][0] for j in choice),F())
           for choice in combinations(range(21),target)
           if sum(slots[j][1] for j in choice)>=pure]
    assert valid
    return min(valid),pure

source=json.loads((R/'context/propertyb35-paper/round01/twentyfive/UNIT9_SCREEN.json').read_text())
checks=[];feasible_count=0;rows_checked=0;types_checked=0
for idx,big in enumerate(sorted(level)):
    B=complete(big,9);singles=[7-sum(bool(t>>i&1) for t in B) for i in range(9)]
    empty=35-len(B)-sum(singles)
    feasible=min(singles+[empty])>=0
    saved=source['results'][idx];assert saved['base']==idx and saved['feasible']==feasible
    if not feasible:continue
    feasible_count+=1
    ns={t:1 for t in B};ns.update({1<<i:m for i,m in enumerate(singles) if m});ns[0]=empty
    ns={t:m for t,m in ns.items() if m}
    assert ns=={int(t):m for t,m in saved['counts'].items() if m}
    assert sum(ns.values())==35
    for i,j in combinations(range(9),2):assert sum(m for t,m in ns.items() if t>>i&1 and t>>j&1)==1
    pos=tuple(saved['positions']);losses={};pure_quotas=[]
    for i in range(9):
        losses[pos[i]],q=quota_loss(ns,pos,i);pure_quotas.append(q)
    assert losses=={int(k):F(v) for k,v in saved['losses'].items()}
    _,original_abc=BareLayout(25,pos).bound(ns,True)
    total=F();bare=F()
    for k in range(1,26):
        A=sum((m*weights(pos,k,t)[0] for t,m in ns.items()),F())
        Bv=sum((m*weights(pos,k,t)[1] for t,m in ns.items()),F())
        Cv=sum((m*(z-int(t==u))*weights(pos,k,t,u) for t,m in ns.items() for u,z in ns.items()),F())
        assert (A,Bv,Cv)==original_abc[k-1]
        dd=losses.get(k,F());assert 0<=dd<=Cv
        total+=min(A,Bv,Cv-dd);bare+=min(A,Bv,Cv)
        rows_checked+=1;types_checked+=len(ns)**2
    assert total==F(saved['bound'])<1 and bare==F(saved['bare'])
    checks.append(dict(base=idx,bound=str(total),positions=pos,pure_quotas=pure_quotas))
    weights.cache_clear()
assert feasible_count==183
out=dict(scope=__doc__,review_independence='same-family',acceptance_status='provisional',
         coverage=coverage,feasible=feasible_count,strict=len(checks),
         maximum=max(checks,key=lambda x:F(x['bound'])),rows_checked=rows_checked,
         directed_type_pair_terms_checked=types_checked,quota_checks=9*len(checks),
         seconds=time.monotonic()-start,results=checks)
(P/'AUDIT.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2),flush=True)

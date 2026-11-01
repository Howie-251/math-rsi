"""Independent injection-count/Fraction replay. Imports no submitted numerical module."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations, combinations_with_replacement, product
from math import factorial, comb, lcm
from functools import lru_cache
import json,time
P=Path(__file__).resolve().parent; BASE=P.parent
START=time.process_time(); vectors=0

def ceildiv(n,d):return -(-n//d)
@lru_cache(None)
def fall(n,r):return factorial(n)//factorial(n-r) if 0<=r<=n else 0
@lru_cache(None)
def probs(v,slots,h,t,u=-1):
    # Uniform injections of the named free vertices of an edge or edge union.
    # Return (end,start) for one edge; pair weight when u is supplied.
    s=len(slots);N=v-s
    left=sum(k<h for k in range(1,v+1) if k not in slots)
    right=N-left-(h not in slots)
    lt=sum(1<<i for i,k in enumerate(slots) if k<h)
    rt=sum(1<<i for i,k in enumerate(slots) if k>h)
    bit=1<<slots.index(h) if h in slots else 0
    a=6-t.bit_count()
    if u<0:
        out=[]
        for available,mask in ((left,lt),(right,rt)):
            if bit:
                val=Q(fall(available,a),fall(N,a)) if t&bit and not t&~(mask|bit) else Q(0)
            else:
                val=Q(a*fall(available,a-1),fall(N,a)) if a and not t&~mask else Q(0)
            out.append(val)
        return tuple(out)
    b=6-u.bit_count()
    if bit:
        if t&u!=bit or t&~(lt|bit) or u&~(rt|bit):return Q(0)
        return Q(fall(left,a)*fall(right,b),fall(N,a+b)) if a+b<=N else Q(0)
    if t&~lt or u&~rt or a==0 or b==0:return Q(0)
    return Q(fall(left,a-1)*fall(right,b-1),fall(N,a+b-1)) if a+b-1<=N else Q(0)

def full_delete(v,slots,ell,j):
    bit=1<<j;h=slots[j];d=sum(n for t,n in ell.items() if t&bit)
    need=max(0,ceildiv(5*d-v+1,4));cells=[]
    types=[t for t,n in ell.items() if n and t&bit]
    for a,t in enumerate(types):
        for u in types[a:]:
            cap=comb(ell[t],2) if t==u else ell[t]*ell[u]
            cells.append((probs(v,slots,h,t,u)+probs(v,slots,h,u,t),cap))
    result=Q(0)
    for w,c in sorted(cells):
        take=min(c,need);result+=w*take;need-=take
    assert need==0
    return result

def avoid_delete(v,slots,ell,j):
    # Full rectangular enumeration of ALL integer cell coordinates, including
    # the core, with exact integer objective scaled by an LCM denominator.
    global vectors
    bit=1<<j;h=slots[j];types=[t for t,n in ell.items() if n and t&bit]
    cells=[]
    for a,t in enumerate(types):
        for u in types[a:]:
            cap=comb(ell[t],2) if t==u else ell[t]*ell[u]
            if cap:cells.append((t,u,cap,probs(v,slots,h,t,u)+probs(v,slots,h,u,t)))
    denominator=lcm(*(c[3].denominator for c in cells))
    costs=[int(c[3]*denominator) for c in cells]
    requirements=[]
    for mask in range(1<<len(slots)):
        if mask&bit:continue
        pool=sum(n for t,n in ell.items() if t&bit and not t&mask)
        quota=max(0,ceildiv(5*pool-(v-1-mask.bit_count()),4))
        indices=[i for i,c in enumerate(cells) if not (c[0]|c[1])&mask]
        requirements.append((indices,quota))
    best=None
    for z in product(*(range(c[2]+1) for c in cells)):
        vectors+=1
        if all(sum(z[i] for i in ids)>=q for ids,q in requirements):
            cost=sum(a*b for a,b in zip(z,costs))
            if best is None or cost<best:best=cost
    assert best is not None
    return Q(best,denominator)

def bound(v,slots,ell,avoid=False):
    slots=tuple(slots);ell={int(t):n for t,n in ell.items() if n}
    assert len(set(slots))==len(slots) and all(1<=h<=v for h in slots)
    assert sum(ell.values())==65 and min(ell.values())>=0
    deletion={h:(avoid_delete if avoid else full_delete)(v,slots,ell,j) for j,h in enumerate(slots)}
    out=Q(0)
    for h in range(1,v+1):
        end=sum(n*probs(v,slots,h,t)[0] for t,n in ell.items())
        begin=sum(n*probs(v,slots,h,t)[1] for t,n in ell.items())
        pair=sum(n*(m-(t==u))*probs(v,slots,h,t,u) for t,n in ell.items() for u,m in ell.items())
        assert pair>=deletion.get(h,0)
        out+=min(end,begin,pair-deletion.get(h,0))
    return out

def make(degrees,blocks):
    ell={b:1 for b in blocks}
    for j,d in enumerate(degrees):ell[1<<j]=d-sum(bool(b&(1<<j)) for b in blocks)
    ell[0]=65-sum(ell.values());return ell

def zero(v):
    q=ceildiv(975-comb(v,2),10);ordered=4160-2*q
    return sum(min(65*probs(v,(),h,0)[0],65*probs(v,(),h,0)[1],ordered*probs(v,(),h,0,0)) for h in range(1,v+1))

rows=[]
def add(group,v,ds,slots,ell,expected=None,avoid=False,extra=None):
    value=bound(v,slots,ell,avoid)
    if expected is not None:assert value==Q(expected),(group,v,ds,value,expected)
    assert value<1,(group,v,ds,value)
    rows.append(dict(group=group,v=v,degrees=list(ds),positions=list(slots),ell=ell,U=str(value),**(extra or {})))

# Common reduction arithmetic and full small balanced domain.
assert all(65*Q(comb(v//2,6)+comb(v-v//2,6),comb(v,6))<1 for v in range(11,27))
assert 44*ceildiv(43,5)>390
for v in range(27,32):
    value=zero(v);assert value<1;rows.append(dict(group='zero',v=v,U=str(value)))

submitted=json.loads((BASE/'ROOT_TWO_LOCKS.json').read_text())
# Reconstruct complete partner domain from strict degree-budget inequality.
for v in range(32,37):
    for d in range(ceildiv(v-1,5),390//v+1):
        if (v,d)==(32,12):continue
        surplus=5*d-v+1
        cutoff=next(e for e in range(d,66) if d+(v-1-surplus)*(e+1)+surplus*d>390)
        rr=[r for r in submitted if r['v']==v and r['minimum']==d]
        assert sorted(r['partner'] for r in rr)==list(range(d,cutoff+1)),(v,d,cutoff)
        for r in rr:
            e=r['partner'];ell={0:66-d-e,1:d-1,2:e-1,3:1}
            add('two',v,(d,e),r['positions'],ell,r['U'])
# Min12 at v32: at least 26 degree12 vertices; excess29<25*2.
assert 32-(390-32*12)>=26 and 5*12-31<25*2
for codegree in [1,2]:
    ell={0:65-24+codegree,1:12-codegree,2:12-codegree,3:codegree}
    candidates=[]
    for slots in [(16,17),(16,15),(15,16),(17,16)]:
        candidates.append((bound(32,slots,ell),slots))
    u,slots=min(candidates)
    add('two_min12',32,(12,12),slots,ell,extra={'codegree':codegree})

# Selection for all triple/four-lock domains is arithmetic of a common graph.
selections=[]
for v,D,n in [(37,12,3),(38,11,3),(39,10,3),(40,10,4),(41,9,4),(42,9,4),(43,9,4)]:
    Z=(D+1)*v-390;T=5*(D+1)-v+2;d0=ceildiv(v-1,5)
    rmin=ceildiv(Z,D+1-d0)
    assert 20*Z>(n-1)*T*T
    for r in range(rmin,v+1):assert r*r>(n-1)*(T*r-5*Z)
    selections.append(dict(v=v,D=D,n=n,Z=Z,T=T,rmin=rmin))

v37=json.loads((BASE/'avoided/V37_THREE.json').read_text())['rows']
assert {(tuple(r['degrees']),r['tri']) for r in v37}=={(ds,tri) for ds in combinations_with_replacement(range(8,13),3) for tri in [0,1]}
for r in v37:
    assert sorted(r['ordered_degrees'])==r['degrees']
    assert r['best_positions']==([15,16,17] if r['degrees']==[12,12,12] else [17,18,19])
    ds=r['ordered_degrees'];blocks=[7] if r['tri'] else [3,5,6]
    add('three_avoided',37,ds,r['best_positions'],make(ds,blocks),r['U'],True,{'sorted_degrees':r['degrees'],'tri':r['tri']})
tight=json.loads((BASE/'pilot/tightened.json').read_text())['rows']
for v,D in [(38,11),(39,10)]:
    rr=[r for r in tight if r['v']==v and r['kind']=='three']
    assert {(tuple(r['degrees']),r['tri']) for r in rr}=={(ds,tri) for ds in combinations_with_replacement(range(8,D+1),3) for tri in [0,1]}
    for r in rr:
        ds=r.get('ordered_degrees',r['degrees']);blocks=[7] if r['tri'] else [3,5,6]
        add('three',v,ds,r['positions'],make(ds,blocks),r['U'],extra={'tri':r['tri']})

# Independent K4 classification: all subsets of the eleven possible cliques,
# accepting precisely those whose pair-incidence vector is identically one.
pairs=list(combinations(range(4),2));cliques=[mask for mask in range(1,16) if mask.bit_count()>=2]
patterns=[]
for subset in range(1<<len(cliques)):
    blocks=[b for i,b in enumerate(cliques) if subset>>i&1]
    if all(sum(bool(b>>i&1 and b>>j&1) for b in blocks)==1 for i,j in pairs):patterns.append(tuple(sorted(blocks)))
assert len(patterns)==6
four=json.loads((BASE/'pilot/FOUR.json').read_text())['rows']
for v,D in [(40,10),(41,9),(42,9),(43,9)]:
    d0=ceildiv(v-1,5);rr=[r for r in four if r['v']==v]
    assert {(tuple(r['degrees']),tuple(sorted(r['blocks']))) for r in rr}=={(ds,b) for ds in combinations_with_replacement(range(d0,D+1),4) for b in patterns}
    for r in rr:
        ell=make(r['degrees'],r['blocks']);assert ell=={int(k):n for k,n in r['ell'].items()}
        add('four',v,r['degrees'],r['positions'],ell,r['U'],extra={'blocks':r['blocks']})
summary=[]
for group,v in sorted({(r['group'],r['v']) for r in rows}):
    rr=[r for r in rows if (r['group'],r['v'])==(group,v)]
    summary.append(dict(group=group,v=v,profiles=len(rr),maximum=str(max(Q(r['U']) for r in rr))))
result=dict(status='PASS',review_independence='same-family',acceptance_status='provisional',method='independent uniform injection counts, exhaustive original domain and recorded winning layouts, integer rectangular avoided-cell minimization',profiles=len(rows),avoided_integer_vectors=vectors,cpu_seconds=time.process_time()-START,k4_patterns=patterns,selections=selections,summary=summary,rows=rows)
(P/'RESULTS.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))

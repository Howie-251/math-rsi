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
    a=7-t.bit_count()
    if u<0:
        out=[]
        for available,mask in ((left,lt),(right,rt)):
            if bit:
                val=Q(fall(available,a),fall(N,a)) if t&bit and not t&~(mask|bit) else Q(0)
            else:
                val=Q(a*fall(available,a-1),fall(N,a)) if a and not t&~mask else Q(0)
            out.append(val)
        return tuple(out)
    b=7-u.bit_count()
    if bit:
        if t&u!=bit or t&~(lt|bit) or u&~(rt|bit):return Q(0)
        return Q(fall(left,a)*fall(right,b),fall(N,a+b)) if a+b<=N else Q(0)
    if t&~lt or u&~rt or a==0 or b==0:return Q(0)
    return Q(fall(left,a-1)*fall(right,b-1),fall(N,a+b-1)) if a+b-1<=N else Q(0)

def full_delete(v,slots,ell,j):
    bit=1<<j;h=slots[j];d=sum(n for t,n in ell.items() if t&bit)
    need=max(0,ceildiv(6*d-v+1,5));cells=[]
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
        quota=max(0,ceildiv(6*pool-(v-1-mask.bit_count()),5))
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
    assert sum(ell.values())==130 and min(ell.values())>=0
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
    ell[0]=130-sum(ell.values());return ell

def zero(v):
    q=ceildiv(2730-comb(v,2),15);ordered=16770-2*q
    return sum(min(130*probs(v,(),h,0)[0],130*probs(v,(),h,0)[1],ordered*probs(v,(),h,0,0)) for h in range(1,v+1))

rows=[]
source=json.loads((BASE/'CANDIDATE.json').read_text())['rows']
assert len(source)==424
source_map={(r['v'],r['kind'],tuple(r['degrees']),r.get('tri')):r for r in source}
assert len(source_map)==len(source)

def add(v,kind,ds,ell,avoid=False,tri=None):
    key=(v,kind,tuple(ds),tri);r=source_map[key];slots=tuple(r['positions'])
    assert r['avoid']==avoid and ell=={int(t):n for t,n in r['ell'].items()}
    assert sum(ell.values())==130
    if kind=='two':assert slots in [(v//2,v//2+1),(v//2,v//2-1)]
    elif kind.startswith('three'):assert slots==(v//2-1,v//2,v//2+1)
    value=bound(v,slots,ell,avoid) if slots else zero(v)
    assert value==Q(r['U']),(key,value,r['U'])
    assert value<1,(key,value)
    rows.append(dict(v=v,kind=kind,degrees=list(ds),tri=tri,ell=ell,positions=slots,avoid=avoid,U=str(value)))

# Common actual counterexample degree budget and small/large vertex ranges.
assert 74*ceildiv(73,6)>910
balanced=[]
for v in range(13,37):
    p=Q(130*(comb(v//2,7)+comb(v-v//2,7)),comb(v,7));assert p<1
    balanced.append(dict(v=v,U=str(p)))
for v in range(37,54):add(v,'zero',[],{0:130})
partners=[]
for v in range(54,67):
    for d in range(ceildiv(v-1,6),910//v+1):
        extra=6*d-(v-1);unit=v-1-extra;assert unit>0
        # Derive the threshold from the degree-sum contradiction directly.
        cutoff=next(t for t in range(d,911) if d+extra*d+unit*(t+1)>910)
        partners.append(dict(v=v,minimum=d,unit_neighbors_lower=unit,partner_upper=cutoff))
        for e in range(d,cutoff+1):
            ell=make([d,e],[3]);add(v,'two',[d,e],ell,True)
selections=[]
for v,D in [(67,14),(68,13),(69,13),(70,13)]:
    d0=ceildiv(v-1,6);Z=(D+1)*v-910;T=6*(D+1)-v+2
    lowmin=ceildiv(Z,D+1-d0)
    assert Z>0 and 24*Z>2*T*T
    for lowcount in range(lowmin,v+1):assert lowcount*lowcount>2*(T*lowcount-6*Z)
    selections.append(dict(v=v,D=D,d0=d0,Z=Z,T=T,rmin=lowmin))
    for ds in combinations_with_replacement(range(d0,D+1),3):
        for tri in [0,1]:add(v,'three',ds,make(ds,[7] if tri else [3,5,6]),True,tri)
for v in range(71,74):
    r=13*v-910;aux=73-v;assert ceildiv(r,aux+1)>=3
    for tri in [0,1]:add(v,'three_tail',[12]*3,make([12]*3,[7] if tri else [3,5,6]),False,tri)
assert len(rows)==len(source) and { (r['v'],r['kind'],tuple(r['degrees']),r['tri']) for r in rows}==set(source_map)
summary=[]
for kind in ['zero','two','three','three_tail']:
    rr=[r for r in rows if r['kind']==kind];worst=max(rr,key=lambda r:Q(r['U']))
    summary.append(dict(kind=kind,profiles=len(rr),maximum=worst['U'],worst=worst))
result=dict(status='PASS',review_independence='same-family',acceptance_status='provisional',K=7,M=130,profiles=len(rows),avoided_integer_vectors=vectors,cpu_seconds=time.process_time()-START,method='independent falling-factorial injection counts; complete final parameter domain; rectangular enumeration of all integer avoided-cell coordinates',maximum=str(max(Q(r['U']) for r in rows)),summary=summary,balanced=balanced,partners=partners,selections=selections,rows=rows)
(P/'RESULTS.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k not in ['rows','balanced','partners']},indent=2))

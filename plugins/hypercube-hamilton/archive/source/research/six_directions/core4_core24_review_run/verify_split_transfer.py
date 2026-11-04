"""Independent stdlib certificate verifier; imports no search/construction code."""
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parent
def edge(a,b): return tuple(sorted((a,b)))
def eset(p): return {edge(a,b) for a,b in zip(p,p[1:])}
def short(e): return (e[0]^e[1]).bit_count()==1
def parity(x): return x.bit_count()%2
def matching(es,vertices):
    es=[edge(*e) for e in es]
    flat=[q for e in es for q in e]
    assert len(flat)==len(set(flat)) and set(flat)==set(vertices)
    return set(es)
def route(p,vertices,start,end,forced,allowed):
    assert p[0]==start and p[-1]==end and len(p)==len(set(p))
    assert set(p)==set(vertices)
    e=eset(p)
    assert set(forced)<=e and all(short(t) or t in allowed for t in e)
    return e
def no_half(p,x,y,layer,cut,n):
    mate={a:b for e in p for a,b in (e,e[::-1])}
    assert parity(x)!=parity(y) and mate[x]!=y
    compressed=p-{edge(x,mate[x]),edge(y,mate[y])}|{edge(mate[x],mate[y])}
    for j in range(n):
        if j==cut:continue
        for bit in (0,1):
            half={edge(q,q^(1<<j)) for q in layer
                  if not q&(1<<j) and parity(q)==bit}
            assert len(half)==1<<(n-3)
            assert not half<=compressed

def verify(c,far=False,rectangular=False,generalized=False):
    assert c['status']=='FOUND'
    n,u,v,i=c['n'],c['u'],c['v'],c['cut'];bit=1<<i
    universe=set(range(1<<n));m={edge(*e) for e in c['matching']}
    matched={q for e in m for q in e};holes=universe-matched
    assert len(m)==(1<<(n-1))-2 and len(matched)==2*len(m)
    assert all(parity(p)!=parity(q) for p,q in m)
    if not generalized:assert all(map(short,m))
    z,w,t,a,b,y,r=(c[k] for k in ('z','w','t','a','b','y','r'))
    assert holes=={u,z,w,t} and parity(u)==parity(z)!=parity(w)==parity(t)
    assert v in matched and parity(v)!=parity(u)
    A={q for q in universe if q&bit==u&bit};B=universe-A
    assert {u,w,a,b}<=A and {z,t,y,v}<=B
    assert (a,b,y)==(z^bit,t^bit,w^bit)
    ma={e for e in m if set(e)<=A};mb={e for e in m if set(e)<=B};cross=m-ma-mb
    assert all(e[0]^e[1]==bit for e in cross)
    assert edge(y,r) in mb
    assert a in {q for e in ma for q in e} and b in {q for e in ma for q in e}
    assert edge(a,b) not in ma
    if far:
        assert n==6 and all((h^j).bit_count()==5 for h in (u,z) for j in (w,t))
        # Probe artifacts use the canonical i=0,k=1 geometry.
        assert holes=={0,3,61,62} and u==0
        assert v in (1,2) or v&3==3 and parity(v)==1
    elif rectangular:
        assert n==6 and holes=={0,3,28,31} and u==0
        assert v<32 and v&3 and parity(v)==1 and v!=31
    else:
        assert len({p^q for p,q in ma if a not in (p,q) and b not in (p,q) and short((p,q))})>=2
        assert len({p^q for p,q in mb if y not in (p,q) and v not in (p,q) and short((p,q))})>=2
    aux={edge(*e) for e in c['auxiliary_A']}
    assert edge(u,w) in aux and all(parity(p)!=parity(q) for p,q in aux)
    xa={q for e in cross for q in e if q in A}
    assert matching(aux,xa|{u,w})==aux
    pa=matching(c['P_A'],A);assert pa==ma|aux
    ea=route(c['K_A'],A,a,b,pa,pa)
    no_half(pa,a,b,A,i,n)
    transferred=c['transferred_paths'];internal=[];endpoints=[];te=set()
    for p in transferred:
        assert len(p)==len(set(p)) and all(short(e) or generalized and e in m for e in eset(p))
        assert set(p[1:-1])<=A
        internal.extend(q for q in p if q in A)
        endpoints.extend([p[0],p[-1]])
        te|=eset(p)
    assert len(internal)==len(set(internal)) and set(internal)==A
    xb={q for e in cross for q in e if q in B}
    assert len(endpoints)==len(set(endpoints)) and set(endpoints)=={u,y,z,t}|xb
    assert te==(ea-aux)|cross|{edge(w,y),edge(a,z),edge(b,t)}
    prefix=c['prefix'];q=c['q'];s=c['s']
    assert prefix in transferred or prefix[::-1] in transferred
    assert prefix[0]==u and prefix[-1]==q and q not in (y,v)
    assert parity(q)==parity(u) or q==t
    rp={edge(p[0],p[-1]):p for p in transferred if u not in (p[0],p[-1])}
    assert edge(y,s) in rp
    if far or rectangular:
        ze=next(e for e in rp if z in e)
        assert all(parity(h)==0 for h in ze) and q!=z
    pb=matching(c['P_B'],B)
    assert pb==(mb-{edge(y,r)})|(set(rp)-{edge(y,s)})|{edge(r,s),edge(y,q)}
    route(c['K_B'],B,y,v,pb,pb);no_half(pb,y,v,B,i,n)
    assert c['K_B'][:2]==[y,q]
    expanded={e:p for e,p in rp.items() if e!=edge(y,s)}
    yp=rp[edge(y,s)];yp=yp if yp[0]==y else yp[::-1]
    expanded[edge(r,s)]=[r]+yp
    final=prefix[:]
    for start,end in zip(c['K_B'][1:],c['K_B'][2:]):
        p=expanded.get(edge(start,end),[start,end])
        p=p if p[0]==start else p[::-1]
        assert p[0]==start and p[-1]==end
        final.extend(p[1:])
    assert final==c['path']
    route(final,universe,u,v,m,m if generalized else set())
    return not c.get('Z1_applicable',True)

def main():
    split=json.loads((ROOT/'split_transfer_results.json').read_text(encoding='utf8'))
    far=json.loads((ROOT/'far_holes_results.json').read_text(encoding='utf8'))
    rectangular=json.loads((ROOT/'rectangular_holes_results.json').read_text(encoding='utf8'))
    for c in split['cases']:verify(c)
    outside=sum(verify(c,True) for c in far)
    rectangle_outside=sum(verify(c,rectangular=True) for c in rectangular)
    out={'status':'PASS','Z1_certificates':len(split['cases']),'Z2_certificates':len(far),
         'Z2_outside_Z1':outside,'Z3_certificates':len(rectangular),'Z3_outside_Z1':rectangle_outside,
         'checks':'matching inputs, split hypotheses, both full-K local paths, both compressed half-layer tests, transferred cover, expansion equality, final cube Hamilton path and retention of all M',
         'scope':'individual witnesses only; no exhaustive Q6 proof'}
    (ROOT/'split_transfer_verification.json').write_text(json.dumps(out,indent=2),encoding='utf8')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()

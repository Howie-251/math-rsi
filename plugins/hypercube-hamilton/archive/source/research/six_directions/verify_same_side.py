"""Independent stdlib verification of Z5 inputs, both imported uses, and expansion."""
import json
from pathlib import Path
from verify_split_transfer import edge,eset,short,matching,route,no_half,parity
ROOT=Path(__file__).resolve().parent

def verify(c):
    n,u,v=c['n'],c['u'],c['v'];i=c['cut'];bit=1<<i
    z,w,t,a,cc,r=(c[k] for k in ('z','w','t','a','c','r'))
    assert c['status']=='FOUND'
    m={edge(*e) for e in c['matching']};used={q for e in m for q in e};universe=set(range(1<<n))
    assert len(used)==2*len(m) and universe-used=={u,z,w,t}
    assert all(parity(p)!=parity(q) for p,q in m)
    assert parity(u)==parity(z)!=parity(w)==parity(t)==parity(v) and v in used
    A={q for q in universe if not (q^u)&bit};B=universe-A
    assert {u,w,v,cc}<=A and {z,t,a}<=B and a==w^bit and cc==t^bit
    ma={e for e in m if set(e)<=A};mb={e for e in m if set(e)<=B};cross=m-ma-mb
    assert all(p^q==bit for p,q in cross)
    assert edge(cc,r) in ma and a in {q for e in mb for q in e}
    assert (z^t).bit_count()>1
    assert len({p^q for p,q in ma if cc not in (p,q) and v not in (p,q) and short((p,q))})>=2
    xa={q for e in cross for q in e if q in A};xb={q for e in cross for q in e if q in B}
    d=matching(c['D'],xb);assert all(parity(p)!=parity(q) for p,q in d)
    lb=matching(c['L_B'],B-{z,t});assert lb==mb|d
    pb=matching(c['P_B_full'],B);assert pb==lb|{edge(z,t)}
    x,j=c['x'],c['chosen_direction'];mate={p:q for e in pb for p,q in (e,e[::-1])}
    assert j!=i and x==z^(1<<j) and not ((t^z)&(t^a)&(1<<j)) and x!=mate[a]
    k0=c['intermediate_B'];e0=route(k0,B,x,a,pb,pb);no_half(pb,x,a,B,i,n)
    pos=k0.index(t);assert pos%2==0 and k0[pos+1]==z
    kb=c['K_B'];assert kb==k0[:pos+1][::-1]+k0[pos+1:]
    eb=route(kb,B,t,a,lb,lb);assert eb==(e0-{edge(t,z)})|{edge(x,z)}
    paths=c['transferred_paths'];interior=[];ends=[];te=set()
    for p in paths:
        assert len(p)==len(set(p)) and set(p[1:-1])<=B and {p[0],p[-1]}<=A
        assert all(short(e) or e in m for e in eset(p))
        interior+=p[1:-1];ends += [p[0],p[-1]];te|=eset(p)
    assert len(interior)==len(set(interior)) and set(interior)==B
    assert len(ends)==len(set(ends)) and set(ends)==xa|{cc,w}
    assert te==(eb-d)|cross|{edge(t,cc),edge(a,w)}
    rp={edge(p[0],p[-1]):p for p in paths};s=c['s'];assert edge(cc,s) in rp
    pa=matching(c['P_A'],A)
    assert pa==(ma-{edge(cc,r)})|(set(rp)-{edge(cc,s)})|{edge(r,s),edge(cc,u)}
    ka=c['K_A'];route(ka,A,cc,v,pa,pa);no_half(pa,cc,v,A,i,n)
    assert ka[:2]==[cc,u]
    def orient(p,start):return p if p[0]==start else p[::-1]
    expand={e:p for e,p in rp.items() if e!=edge(cc,s)}
    expand[edge(r,s)]=[r]+orient(rp[edge(cc,s)],cc)
    final=[u]
    for start,end in zip(ka[1:],ka[2:]):
        p=orient(expand[edge(start,end)],start) if edge(start,end) in expand else [start,end]
        assert p[-1]==end;final+=p[1:]
    assert final==c['path'];route(final,universe,u,v,m,m)

def main():
    cs=json.loads((ROOT/'same_side_results.json').read_text(encoding='utf8'))
    for c in cs:verify(c)
    out=dict(status='PASS',certificates=len(cs),scope='individual Z5 certificates, not exhaustive P6',
             checks='split hypotheses, bipartite near-perfect input, safe coordinate, both compressed half-layer tests, both local extensions, all transferred paths and exact expansion')
    (ROOT/'same_side_verification.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

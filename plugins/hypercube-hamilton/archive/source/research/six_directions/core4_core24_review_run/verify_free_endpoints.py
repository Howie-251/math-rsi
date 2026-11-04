"""Independent, standard-library check of F6 intermediate and final witnesses."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def edge(a,b):return tuple(sorted((a,b)))
def edges(p):return {edge(a,b) for a,b in zip(p,p[1:])}
def short(e):return (e[0]^e[1]).bit_count()==1
def route(p,u,v,forced,allowed):
    assert len(p)==64 and set(p)==set(range(64)) and p[0]==u and p[-1]==v
    es=edges(p)
    assert forced<=es and all(short(e) or e in allowed for e in es)
    return es
def main():
    data=json.loads((ROOT/'free_endpoints_results.json').read_text(encoding='utf8'))
    for c in data:
        assert c['status']=='FOUND'
        u,v,z,t,x,y=(c[k] for k in ('u','v','z','t','x','y'))
        m={edge(*e) for e in c['matching']}
        flat=[q for e in m for q in e]
        assert len(m)==30 and len(flat)==len(set(flat)) and all(map(short,m))
        assert set(range(64))-set(flat)=={u,v,z,t}
        assert u.bit_count()%2==z.bit_count()%2!=v.bit_count()%2==t.bit_count()%2
        assert len({a^b for a,b in m})>=4
        l=m|{edge(u,v)};p=l|{edge(z,t)}
        mate={a:b for e in p for a,b in (e,e[::-1])}
        assert len(mate)==64 and short((x,t)) and short((y,z))
        assert x not in (z,mate[y]) and y!=t and x.bit_count()%2!=y.bit_count()%2
        compressed=p-{edge(x,mate[x]),edge(y,mate[y])}|{edge(mate[x],mate[y])}
        for i in range(6):
            for parity in (0,1):
                half={edge(q,q^(1<<i)) for q in range(64) if not q&(1<<i) and q.bit_count()%2==parity}
                assert len(half)==16 and not half<=compressed
        k=c['intermediate_path'];ke=route(k,x,y,p,p)
        pos=k.index(z);assert pos%2==0 and k[pos+1]==t
        h=c['near_perfect_path'];assert h==k[:pos+1][::-1]+k[pos+1:]
        he=route(h,z,y,l,l)
        assert he==(ke-{edge(z,t)})|{edge(x,t)}
        assert edge(y,z) not in he
        ce=he|{edge(y,z)}
        assert len(ce)==64 and edge(u,v) in ce
        final=route(c['path'],u,v,m,set())
        assert final==ce-{edge(u,v)}
    out={'status':'PASS','certificates':len(data),
         'checks':'four-hole input, perfect completion, compressed half-layers, intermediate extension, orientation, first artificial-edge removal/splice, cycle closure, second artificial-edge deletion, final Hamilton path',
         'scope':'witnesses only; not full Q6 enumeration'}
    (ROOT/'free_endpoints_verification.json').write_text(json.dumps(out,indent=2),encoding='utf8')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()

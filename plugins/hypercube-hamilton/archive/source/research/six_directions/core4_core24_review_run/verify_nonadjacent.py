"""Independent stdlib N6 long-edge witness checks, including exact half-layers."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def edge(a,b):return tuple(sorted((a,b)))
def edges(p):return {edge(a,b) for a,b in zip(p,p[1:])}
def short(e):return (e[0]^e[1]).bit_count()==1
def route(p,vertices,a,b,forced,allowed):
    assert len(p)==len(vertices) and set(p)==vertices and p[0]==a and p[-1]==b
    es=edges(p);assert forced<=es and all(short(e) or e in allowed for e in es)
    return es
def main():
    cs=json.loads((ROOT/'nonadjacent_results.json').read_text(encoding='utf8'))
    for c in cs:
        assert c['status']=='FOUND'
        n,r,s,y,x,j=(c[k] for k in ('n','r','s','y','x','chosen_direction'))
        vertices=set(range(1<<n));l={edge(*e) for e in c['L']};flat=[q for e in l for q in e]
        assert len(flat)==len(set(flat)) and set(flat)==vertices-{r,s}
        assert all(a.bit_count()%2!=b.bit_count()%2 and not short((a,b)) for a,b in l)
        assert (r^s).bit_count()>1 and (r.bit_count()-s.bit_count())%2
        assert y!=s and (r.bit_count()-y.bit_count())%2
        p=l|{edge(r,s)};mate={a:b for e in p for a,b in (e,e[::-1])}
        assert x==s^(1<<j) and not ((r^s)&(r^y)&(1<<j)) and x!=mate[y]
        compressed=p-{edge(x,mate[x]),edge(y,mate[y])}|{edge(mate[x],mate[y])}
        for i in range(n):
            for parity in (0,1):
                half={edge(a,a^(1<<i)) for a in vertices if not a&(1<<i) and a.bit_count()%2==parity}
                assert len(half)==1<<(n-2) and not half<=compressed
        k=c['intermediate_path'];ke=route(k,vertices,x,y,p,p);pos=k.index(r)
        assert pos%2==0 and k[pos+1]==s
        h=c['path'];assert h==k[:pos+1][::-1]+k[pos+1:]
        he=route(h,vertices,r,y,l,l);assert he==(ke-{edge(r,s)})|{edge(x,s)}
    out=dict(status='PASS',certificates=len(cs),original_short_edges_per_matching=0,
             scope='specific Q5 complete-bipartite witnesses, not exhaustive and not P6 proof')
    (ROOT/'nonadjacent_verification.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))
if __name__=='__main__':main()

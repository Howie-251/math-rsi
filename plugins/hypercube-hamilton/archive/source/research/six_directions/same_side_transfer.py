"""Z5 criterion/construction. Supports original bipartite long edges inside layers."""
import json
from pathlib import Path
from collections import Counter
from split_transfer import local_path
from single_bridge_probe import verify
ROOT=Path(__file__).resolve().parent
def edge(a,b):return tuple(sorted((a,b)))
def edges(p):return {edge(a,b) for a,b in zip(p,p[1:])}

def criterion(m,u,v,n=6):
    mate={a:b for e in m for a,b in (e,e[::-1])}
    if len(mate)!=2*len(m) or any(a.bit_count()%2==b.bit_count()%2 for a,b in m):return None
    holes=set(range(1<<n))-set(mate)
    if len(holes)!=4 or u not in holes or v not in mate or u.bit_count()%2==v.bit_count()%2:return None
    z=next(q for q in holes if q!=u and q.bit_count()%2==u.bit_count()%2)
    odd=[q for q in holes if q not in (u,z)]
    for i in range(n):
        bit=1<<i
        if (u^v)&bit or not (u^z)&bit or not (odd[0]^odd[1])&bit:continue
        if any((a^b)&bit and a^b!=bit for a,b in m):continue
        w=next(q for q in odd if not (u^q)&bit);t=next(q for q in odd if q!=w)
        a,c=w^bit,t^bit
        if (z^t).bit_count()==1:continue
        ma=[e for e in m if all(not(q^u)&bit for q in e)]
        mb=[e for e in m if all((q^u)&bit for q in e)]
        am={a:b for e in ma for a,b in (e,e[::-1])};bm={a:b for e in mb for a,b in (e,e[::-1])}
        da={p^q for p,q in ma if c not in (p,q) and v not in (p,q) and (p^q).bit_count()==1}
        if c in am and a in bm and len(da)>=2:
            return dict(cut=i,z=z,w=w,t=t,a=a,c=c,r=am[c],directions_A=sorted(da))
    return None

def construct(m,u,v,cert,n=6):
    i=cert['cut'];bit=1<<i;side=bool(u&bit)
    z,w,t,a,c,r=(cert[k] for k in ('z','w','t','a','c','r'))
    ma=[edge(*e) for e in m if all(not(q^u)&bit for q in e)]
    mb=[edge(*e) for e in m if all((q^u)&bit for q in e)]
    cross={edge(*e) for e in m if e[0]^e[1]==bit}
    xb=sorted(q for e in cross for q in e if (q^u)&bit)
    ev=[q for q in xb if not q.bit_count()%2];od=[q for q in xb if q.bit_count()%2]
    assert len(ev)==len(od)
    d=[edge(q,s) for q,s in zip(ev,od)];lb=mb+d;pb=lb+[edge(t,z)]
    mate={q:s for e in pb for q,s in (e,e[::-1])}
    forbidden=(t^z)&(t^a)
    j=next(j for j in range(n) if j!=i and not forbidden&(1<<j) and z^(1<<j)!=mate[a])
    x=z^(1<<j)
    res=local_path(n,i,int(not side),pb,x,a)
    if res['status']!='FOUND':return dict(status='UNKNOWN_B',solver=res)
    kb0=res['path'];pos=kb0.index(t);assert kb0[pos+1]==z
    kb=kb0[:pos+1][::-1]+kb0[pos+1:]
    adj={q:[] for q in kb}
    for p,q in edges(kb)-set(d):adj[p].append(q);adj[q].append(p)
    seen=set();transferred=[]
    for start in sorted(q for q in kb if len(adj[q])==1):
        if start in seen:continue
        path=[start]
        while True:
            nxt=[q for q in adj[path[-1]] if len(path)==1 or q!=path[-2]]
            if not nxt:break
            assert len(nxt)==1;path.append(nxt[0])
        seen.update(path);transferred.append([path[0]^bit]+path+[path[-1]^bit])
    assert seen==set(kb)
    rp={edge(p[0],p[-1]):p for p in transferred}
    cs=next(e for e in rp if c in e);s=next(q for q in cs if q!=c)
    pa=[e for e in ma if e!=edge(c,r)]+[e for e in rp if e!=cs]+[edge(r,s),edge(c,u)]
    assert len(pa)==1<<(n-2) and len({q for e in pa for q in e})==1<<(n-1)
    res=local_path(n,i,int(side),pa,c,v)
    if res['status']!='FOUND':return dict(status='UNKNOWN_A',solver=res)
    ka=res['path'];assert ka[:2]==[c,u]
    def orient(p,start):return p if p[0]==start else p[::-1]
    expand={e:p for e,p in rp.items() if e!=cs}
    expand[edge(r,s)]=[r]+orient(rp[cs],c)
    final=[u]
    for start,end in zip(ka[1:],ka[2:]):
        p=orient(expand[edge(start,end)],start) if edge(start,end) in expand else [start,end]
        final+=p[1:]
    verify(n,m,u,v,final,allowed_long=[edge(*e) for e in m if (e[0]^e[1]).bit_count()!=1])
    return dict(status='FOUND',path=final,D=d,L_B=lb,P_B_full=pb,x=x,chosen_direction=j,
                intermediate_B=kb0,K_B=kb,transferred_paths=transferred,s=s,P_A=pa,K_A=ka)

def main():
    data=json.loads((ROOT/'remaining_samples_after_R.json').read_text(encoding='utf8'))['remaining']
    out=[]
    for c in data:
        cert=criterion(c['matching'],c['u'],c['v'])
        if cert:
            result=construct(c['matching'],c['u'],c['v'],cert)
            out.append(dict(c,**cert,**result))
            (ROOT/'same_side_results.json').write_text(json.dumps(out,indent=2),encoding='utf8')
            print(len(out),c['v'],result['status'],flush=True)
    print('TOTAL',len(out),dict(Counter(c['status'] for c in out)))
if __name__=='__main__':main()

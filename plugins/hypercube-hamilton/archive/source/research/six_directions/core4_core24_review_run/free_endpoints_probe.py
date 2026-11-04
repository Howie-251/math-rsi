"""F6 two-artificial-edge construction; witnesses do not prove universal coverage."""
import json
from pathlib import Path
from single_bridge_probe import solve,verify
ROOT=Path(__file__).resolve().parent

def construct(m,u,v):
    holes=set(range(64))-{q for e in m for q in e}
    z=next(q for q in holes if q!=u and q.bit_count()%2==u.bit_count()%2)
    t=next(q for q in holes if q not in (u,v,z))
    p=m+[(u,v),(z,t)];mate={a:b for e in p for a,b in (e,e[::-1])}
    y=next(z^(1<<i) for i in range(6) if z^(1<<i)!=t)
    x=next(t^(1<<i) for i in range(6) if t^(1<<i) not in (z,mate[y]))
    result=solve(6,p,x,y,5,seconds=10,allowed_long=[e for e in p if (e[0]^e[1]).bit_count()!=1])
    out=dict(n=6,u=u,v=v,z=z,t=t,x=x,y=y,matching=m,status=result['status'])
    if result['status']!='FOUND':return out
    k=result['path'];pos=k.index(z);assert k[pos+1]==t
    h=k[:pos+1][::-1]+k[pos+1:]
    verify(6,m+[(u,v)],z,y,h,allowed_long=[(u,v)])
    assert (z^y).bit_count()==1
    start=h.index(u)
    step=-1 if h[(start+1)%64]==v else 1
    assert h[(start-step)%64]==v
    path=[h[(start+step*j)%64] for j in range(64)]
    verify(6,m,u,v,path)
    out.update(intermediate_path=k,near_perfect_path=h,path=path)
    return out

def main():
    templates={}
    old=json.loads((ROOT/'pilot_results_retry.json').read_text(encoding='utf8'))['cases']
    more=json.loads((ROOT/'far_holes_results.json').read_text(encoding='utf8'))+json.loads((ROOT/'rectangular_holes_results.json').read_text(encoding='utf8'))
    for c in old+more:
        m=sorted(tuple(sorted(e)) for e in c['matching'])
        if c['n']==6 and len(m)==30 and len({a^b for a,b in m})>=4:
            templates[tuple(m)]=m
    results=[]
    for idx,m in enumerate(templates.values()):
        holes=set(range(64))-{q for e in m for q in e}
        for v in sorted(q for q in holes if q.bit_count()%2):
            c=construct(m,0,v);c['template']=idx;results.append(c)
            (ROOT/'free_endpoints_results.json').write_text(json.dumps(results,indent=2),encoding='utf8')
            print(idx,v,c['status'],flush=True)
    print('TOTAL',len(results),'FOUND',sum(c['status']=='FOUND' for c in results))

if __name__=='__main__':main()

"""Candidate criteria for bipartite long-edge split transfer and endpoint reductions."""
import json
from pathlib import Path
from collections import Counter
from one_displaced_edge import old_label,certificate as f1_certificate
from split_transfer import criterion
ROOT=Path(__file__).resolve().parent

def generalized_criterion(m,u,v,n=6):
    mate={a:b for e in m for a,b in (e,e[::-1])}
    if len(mate)!=2*len(m) or any(a.bit_count()%2==b.bit_count()%2 for a,b in m):return None
    holes=set(range(1<<n))-set(mate)
    if len(holes)!=4 or u not in holes or v not in mate or u.bit_count()%2==v.bit_count()%2:return None
    same=[q for q in holes if (q.bit_count()-u.bit_count())%2==0 and q!=u]
    if len(same)!=1:return None
    z=same[0];odd=[q for q in holes if q not in (u,z)]
    for i in range(n):
        bit=1<<i
        if not ((u^z)&bit and (u^v)&bit and (odd[0]^odd[1])&bit):continue
        if any((a^b)&bit and a^b!=bit for a,b in m):continue
        w=next(q for q in odd if (q&bit)==(u&bit));t=next(q for q in odd if q!=w)
        a,b,y=z^bit,t^bit,w^bit
        ma=[e for e in m if all((q&bit)==(u&bit) for q in e)]
        mb=[e for e in m if all((q&bit)!=(u&bit) for q in e)]
        amap={q:r for e in ma for q,r in (e,e[::-1])};bmap={q:r for e in mb for q,r in (e,e[::-1])}
        if a not in amap or b not in amap or y not in bmap or amap[a]==b:continue
        da={q^r for q,r in ma if a not in (q,r) and b not in (q,r) and (q^r).bit_count()==1}
        db={q^r for q,r in mb if y not in (q,r) and v not in (q,r) and (q^r).bit_count()==1}
        if len(da)>=2 and len(db)>=2:
            return dict(cut=i,z=z,w=w,t=t,a=a,b=b,y=y,r=bmap[y],directions_A=sorted(da),directions_B=sorted(db))
    return None

def reduce(m,u,v,n=6):
    mate={a:b for e in m for a,b in (e,e[::-1])}
    if v in mate:
        h=mate[v]
        l=[e for e in m if v not in e]+[(u,v)]
        cert=generalized_criterion(l,h,v,n)
        if cert:return dict(kind='covered_target_rotation',transformed_matching=l,new_root=h,new_target=v,split_certificate=cert)
    else:
        l=m+[(u,v)];holes=set(range(1<<n))-{q for e in l for q in e}
        for root in sorted(holes):
            for i in range(n):
                target=root^(1<<i)
                cert=generalized_criterion(l,root,target,n)
                if cert:return dict(kind='free_target_cycle',transformed_matching=l,new_root=root,new_target=target,split_certificate=cert)
    return None

def main():
    cs=json.loads((ROOT/'pilot_results_retry.json').read_text(encoding='utf8'))['cases']
    out=[];count=Counter()
    for c in cs:
        if c['n']!=6 or old_label(c)!='remaining' or criterion(c['matching'],c['u'],c['v']):continue
        m,u,v=c['matching'],c['u'],c['v']
        free=set(range(64))-{q for e in m for q in e}
        if len(free)==4 and v in free:continue # F6
        if f1_certificate(m,u,v):continue
        cert=reduce(m,u,v)
        if cert:
            out.append(dict(n=6,matching=m,u=u,v=v,**cert));count[(len(m),cert['kind'])]+=1
    (ROOT/'auxiliary_reduction_candidates.json').write_text(json.dumps(out,indent=2),encoding='utf8')
    print('NEW',len(out),dict(count))

if __name__=='__main__':main()

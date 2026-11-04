"""Z1 criterion and constructive two-layer expansion, not exhaustive Q6 enumeration."""
import json
from collections import Counter
from pathlib import Path
from single_bridge_probe import solve,verify as verify_extension
from four_hole_surgery import edge,edges,verify_path
from one_displaced_edge import old_label
ROOT=Path(__file__).resolve().parent

def criterion(m,u,v,n=6):
    mate={a:b for e in m for a,b in (e,e[::-1])}
    holes=set(range(1<<n))-set(mate)
    if len(holes)!=4 or u not in holes or v not in mate:return None
    same=[q for q in holes if (q.bit_count()-u.bit_count())%2==0 and q!=u]
    if len(same)!=1:return None
    z=same[0];odd=[q for q in holes if q not in (u,z)]
    for i in range(n):
        bit=1<<i
        if not ((u^z)&bit and (u^v)&bit and (odd[0]^odd[1])&bit):continue
        w=next(q for q in odd if (q&bit)==(u&bit));t=next(q for q in odd if q!=w)
        a,b,y=z^bit,t^bit,w^bit
        ma=[e for e in m if all((q&bit)==(u&bit) for q in e)]
        mb=[e for e in m if all((q&bit)!=(u&bit) for q in e)]
        amap={q:r for e in ma for q,r in (e,e[::-1])}
        bmap={q:r for e in mb for q,r in (e,e[::-1])}
        if a not in amap or b not in amap or y not in bmap or amap[a]==b:continue
        da={q^r for q,r in ma if a not in (q,r) and b not in (q,r)}
        db={q^r for q,r in mb if y not in (q,r) and v not in (q,r)}
        if len(da)>=2 and len(db)>=2:
            return {'cut':i,'z':z,'w':w,'t':t,'a':a,'b':b,'y':y,
                    'r':bmap[y],'directions_A':sorted(da),'directions_B':sorted(db),
                    'target_is_crossing_endpoint':(mate[v]^v)==bit}
    return None

def local_path(n,cut,side,p,start,end):
    # Delete the fixed split coordinate to identify a layer with Q_(n-1).
    def compress(q):return (q&((1<<cut)-1))|((q>>(cut+1))<<cut)
    def expand(q):return (q&((1<<cut)-1))|(side<<cut)|((q>>cut)<<(cut+1))
    lp=[(compress(a),compress(b)) for a,b in p]
    result=solve(n-1,lp,compress(start),compress(end),0,seconds=8,
                 allowed_long=[e for e in lp if (e[0]^e[1]).bit_count()!=1])
    if result['status']!='FOUND':return result
    return {'status':'FOUND','path':[expand(q) for q in result['path']]}

def construct(m,u,v,cert,n=6,allow_original_long=False):
    i=cert['cut'];bit=1<<i;side=1 if u&bit else 0
    z,w,t,a,b,y,r=(cert[k] for k in ('z','w','t','a','b','y','r'))
    ma=[edge(*e) for e in m if all((q&bit)==(u&bit) for q in e)]
    mb=[edge(*e) for e in m if all((q&bit)!=(u&bit) for q in e)]
    cross=[edge(*e) for e in m if (e[0]^e[1])==bit]
    xa=sorted(q for e in cross for q in e if (q&bit)==(u&bit))
    left=[q for q in xa if q.bit_count()%2==0]
    right=[q for q in xa if q.bit_count()%2==1]
    assert len(left)==len(right)
    auxiliary=[edge(q,s) for q,s in zip(left,right)]+[edge(u,w)]
    pa=ma+auxiliary
    result_a=local_path(n,i,side,pa,a,b)
    if result_a['status']!='FOUND':return {'status':'UNKNOWN_A','solver':result_a}
    ka=result_a['path'];forest_edges=edges(ka)-set(auxiliary)
    adj={q:[] for q in ka}
    for q,s in forest_edges:adj[q].append(s);adj[s].append(q)
    ends=sorted(q for q in ka if len(adj[q])==1)
    assert set(ends)==set(xa)|{u,w,a,b}
    seen=set();transferred=[]
    for start in ends:
        if start in seen:continue
        path=[start]
        while True:
            candidates=[q for q in adj[path[-1]] if len(path)==1 or q!=path[-2]]
            if not candidates:break
            assert len(candidates)==1
            path.append(candidates[0])
        seen.update(path)
        if path[0]!=u:path=[path[0]^bit]+path
        if path[-1]!=u:path=path+[path[-1]^bit]
        transferred.append(path)
    assert seen==set(ka)
    prefix=next(path if path[0]==u else path[::-1] for path in transferred if u in (path[0],path[-1]))
    q=prefix[-1]
    assert q!=y and q!=v
    rpaths={edge(path[0],path[-1]):path for path in transferred if u not in (path[0],path[-1])}
    ys=next(e for e in rpaths if y in e)
    s=next(q0 for q0 in ys if q0!=y)
    pb=[e for e in mb if e!=edge(y,r)]+[e for e in rpaths if e!=ys]+[edge(r,s),edge(y,q)]
    assert len(pb)==1<<(n-2)
    assert len({x0 for e in pb for x0 in e})==1<<(n-1)
    result_b=local_path(n,i,1-side,pb,y,v)
    if result_b['status']!='FOUND':return {'status':'UNKNOWN_B','solver':result_b}
    kb=result_b['path'];assert kb[:2]==[y,q]
    def orient(path,start):return path if path[0]==start else path[::-1]
    expansion={e:path for e,path in rpaths.items() if e!=ys}
    expansion[edge(r,s)]=[r]+orient(rpaths[ys],y)
    expanded=[q]
    for start,end in zip(kb[1:],kb[2:]):
        key=edge(start,end)
        segment=orient(expansion[key],start) if key in expansion else [start,end]
        assert segment[0]==start and segment[-1]==end
        expanded.extend(segment[1:])
    final=prefix[:-1]+expanded
    if allow_original_long:
        verify_extension(n,m,u,v,final,allowed_long=[edge(*e) for e in m if (e[0]^e[1]).bit_count()!=1])
    else:
        assert verify_path(edges(final),m,u,v,n)==final
    return {'status':'FOUND','path':final,'P_A':pa,'K_A':ka,'auxiliary_A':auxiliary,
            'transferred_paths':transferred,'prefix':prefix,'q':q,'s':s,
            'P_B':pb,'K_B':kb}

def main():
    data=json.loads((ROOT/'pilot_results_retry.json').read_text(encoding='utf8'))['cases']
    f1=json.loads((ROOT/'one_displaced_edge_results.json').read_text(encoding='utf8'))['certificates']
    def key(c):return (tuple(tuple(e) for e in c['matching']),c['u'],c['v'])
    f1keys={key(c) for c in f1};counts=Counter();cases=[];criterion_count=0
    for c in data:
        if c['n']!=6:continue
        label=old_label(c)
        if label=='remaining' and key(c) in f1keys:label='F1_one_displaced_edge'
        cert=criterion(c['matching'],c['u'],c['v'])
        if cert:criterion_count+=1
        if label=='remaining' and cert:
            label='Z1_split_transfer'
            result=construct(c['matching'],c['u'],c['v'],cert)
            case={'n':6,'u':c['u'],'v':c['v'],'matching':c['matching'],**cert,**result}
            cases.append(case)
            (ROOT/'split_transfer_results.json').write_text(json.dumps({'cases':cases},indent=2),encoding='utf8')
            print(len(cases),c['v'],cert['cut'],result['status'],flush=True)
        counts[label]+=1
    output={'scope':'original 1152 sampled Q6 cases; classification is not exhaustive P6',
            'criterion_count':criterion_count,'counts':dict(counts),'cases':cases,
            'constructive_status':dict(Counter(c['status'] for c in cases))}
    (ROOT/'split_transfer_results.json').write_text(json.dumps(output,indent=2),encoding='utf8')
    print(json.dumps({k:v for k,v in output.items() if k!='cases'},indent=2))

if __name__=='__main__':main()

"""Bounded two-artificial-edge repair experiments; not an exhaustive P6 proof."""
import itertools,json,random
from pathlib import Path
from single_bridge_probe import solve,random_maximum
ROOT=Path(__file__).resolve().parent

def edge(a,b):return tuple(sorted((a,b)))
def edges(path):return {edge(a,b) for a,b in zip(path,path[1:])}

def verify_path(es,m,u,v,n=6):
    if len(es)!=(1<<n)-1 or any((a^b).bit_count()!=1 for a,b in es):return None
    adj=[[] for _ in range(1<<n)]
    for a,b in es:adj[a].append(b);adj[b].append(a)
    if any(len(adj[a])!=(1 if a in (u,v) else 2) for a in range(1<<n)):return None
    if not {edge(*e) for e in m}<=es:return None
    p=[u];seen={u}
    while p[-1]!=v:
        ns=[z for z in adj[p[-1]] if len(p)==1 or z!=p[-2]]
        if len(ns)!=1 or ns[0] in seen:return None
        p.append(ns[0]);seen.add(ns[0])
    return p if len(p)==1<<n else None

def connector_paths(z,t,n=6,max_cuts=2):
    """All simple odd paths of length 3 or 5, including nongreodesic paths."""
    def rec(p,remaining):
        if remaining==0:
            if p[-1]==t:yield tuple(p)
            return
        if (p[-1]^t).bit_count()>remaining:return
        for j in range(n):
            q=p[-1]^(1<<j)
            if q in p or (q==t and remaining!=1):continue
            yield from rec(p+[q],remaining-1)
    for k in range(1,max_cuts+1):yield from rec([z],2*k+1)

def repair(kpath,m,u,z,w,t,x,v,connectors):
    original=edges(kpath)
    artificial={edge(u,w),edge(z,t)}
    pset={edge(*e) for e in m}|artificial
    for connector in connectors:
        if set(connector)&{u,w,x,v}:continue
        cut={edge(connector[j],connector[j+1]) for j in range(1,len(connector)-1,2)}
        if not cut<=original-pset:continue
        add={edge(x,w)}|{edge(connector[j],connector[j+1]) for j in range(0,len(connector)-1,2)}
        kept=original-artificial-cut
        if add&kept:continue
        final=kept|add
        path=verify_path(final,m,u,v)
        if path is not None:
            return {'path':path,'connector':list(connector),'cut_edges':sorted(cut),
                    'added_edges':sorted(add),'extra_cuts':len(cut)}
    return None

def main():
    rng=random.Random(20261102)
    old=json.loads((ROOT/'pilot_results_retry.json').read_text(encoding='utf8'))['cases']
    templates=[];seen=set()
    for c in old:
        m=c['matching'];key=tuple(tuple(e) for e in m)
        if c['n']!=6 or len(m)!=30 or key in seen:continue
        seen.add(key)
        holes=set(range(64))-{a for e in m for a in e}
        z=next(a for a in holes if a and a.bit_count()%2==0)
        odd=[a for a in holes if a.bit_count()%2]
        if any((z^a).bit_count()==1 for a in odd):continue
        templates.append((m,z,odd,'previous_template'))
    for j in range(4):
        m=random_maximum(6,{0,3,61,62},rng)
        assert len(m)==30
        templates.append((m,3,[61,62],'distance_five_holes'))
    cases=[]
    for ti,(m,z,odd,kind) in enumerate(templates):
        covered={a for e in m for a in e}
        targets=rng.sample(sorted(a for a in covered if a.bit_count()%2),4)
        for v in targets:
            case={'n':6,'u':0,'v':v,'z':z,'holes':[0,z]+odd,'matching':m,
                  'template':ti,'kind':kind,'status':'NO_REPAIR_IN_TESTED_EXTENSIONS','attempts':0}
            for w,t in (odd,odd[::-1]):
                p=m+[(0,w),(z,t)]
                mate={a:b for e in p for a,b in (e,e[::-1])}
                connectors=list(connector_paths(z,t))
                xs=[w^(1<<j) for j in range(6) if (w^(1<<j)) not in (0,z,mate[v])]
                for x in xs[:3]:
                    result=solve(6,p,x,v,5,seconds=4,allowed_long=[(0,w),(z,t)])
                    case['attempts']+=1
                    if result['status']!='FOUND':continue
                    fixed=repair(result['path'],m,0,z,w,t,x,v,connectors)
                    if fixed:
                        case.update(fixed);case.update({'status':'SURGERY_FOUND','w':w,'t':t,'x':x,
                                                       'intermediate_path':result['path']})
                        break
                if case['status']=='SURGERY_FOUND':break
            cases.append(case)
            (ROOT/'four_hole_surgery.json').write_text(json.dumps(cases,indent=2),encoding='utf8')
            print(ti,v,case['status'],case.get('extra_cuts'),case['attempts'],flush=True)
    print(json.dumps({s:sum(c['status']==s for c in cases)
                      for s in ('SURGERY_FOUND','NO_REPAIR_IN_TESTED_EXTENSIONS')}))

if __name__=='__main__':main()

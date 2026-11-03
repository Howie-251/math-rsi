"""Exact tiny H classification and full degree-eight seeds for two HS deletions."""
from hs_augmentation import ROOT,base,dump,verify
import collections,itertools,json,os,time
OUT=ROOT/'computations/dd82/construction/hs59_two_delete'

def distances(n,edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    bad=[(u,v) for u,v in itertools.combinations(range(n),2) if v not in adj[u] and not adj[u]&adj[v]]
    seen={0};todo=[0]
    for u in todo:
        for v in adj[u]-seen:seen.add(v);todo.append(v)
    return adj,bad,len(seen)==n

def classify():
    start=time.process_time();summary={}
    for d in (6,7,8):
        hist=collections.Counter();examples={};count=0;connected=0
        for rest in itertools.combinations(list(itertools.combinations(range(1,9),2)),9-d):
            edges=[(0,i) for i in range(1,d+1)]+list(rest)
            adj,bad,conn=distances(9,edges);count+=1
            if not conn:continue
            connected+=1;hist[len(bad)]+=1
            if len(bad)<=5:
                shape=(tuple(sorted(map(len,adj),reverse=True)),tuple(sorted(collections.Counter(v for e in bad for v in e).values(),reverse=True)))
                key=str(shape)
                if key not in examples:examples[key]=dict(edges=edges,bad_pairs=bad,degrees=list(map(len,adj)),multiplicity=0)
                examples[key]['multiplicity']+=1
        summary[str(d)]=dict(inputs=count,connected=connected,bad_pair_histogram=dict(sorted(hist.items())),surviving_types=list(examples.values()))
    return dict(scope='All H(9,9) with <=5 bad pairs, after analytically proving maximum degree >=6 and normalizing its neighborhood.',cpu_seconds=time.process_time()-start,enumerated_inputs=sum(x['inputs'] for x in summary.values()),degree_cases=summary)

def seed(kind):
    original,ns=base();deleted=[(0,1),(0,4)] if kind=='adjacent' else [(0,1),(2,3)]
    old=[e for e in original if e not in deleted];adj,lost,conn=distances(50,old)
    assert conn
    H=[(a,8) for a in range(8)]+[(6,7)]
    fixed={0:{1,2,3},1:{0,1},4:{0,2}} if kind=='adjacent' else {0:{0,1},1:{0,2},2:{0,3},3:{2,3}}
    hdeg=[sum(a in e for e in H) for a in range(9)]
    caps=[8-hdeg[a]-sum(a in s for s in fixed.values()) for a in range(9)]
    free=[x for x in range(50) if x not in fixed]
    domains={x:set(range(9)) for x in free}
    fixed_ok=True
    for x,y in lost:
        if x in fixed and y in fixed:fixed_ok &= bool(fixed[x]&fixed[y])
        elif x in fixed:domains[y]&=fixed[x]
        elif y in fixed:domains[x]&=fixed[y]
        else:raise AssertionError('unexpected two-singleton repair pair')
    slots=[a for a,c in enumerate(caps) for _ in range(c)];owner={}
    def place(x,seen):
        for i,a in enumerate(slots):
            if a not in domains[x] or i in seen:continue
            seen.add(i)
            if i not in owner or place(owner[i],seen):owner[i]=x;return True
        return False
    success=fixed_ok and all(place(x,set()) for x in sorted(free,key=lambda x:(len(domains[x]),x)))
    ports=dict(fixed)
    if success:ports.update({x:{slots[i]} for i,x in owner.items()})
    else:ports.update({x:{a} for x,a in zip(free,slots)})
    edges=sorted(old+[(50+a,50+b) for a,b in H]+[(x,50+a) for x,s in ports.items() for a in sorted(s)])
    path=OUT/f'{kind}.seed.json'
    dump(path,dict(n=59,deleted_edges=deleted,auxiliary_edges=H,ports={str(x):sorted(s) for x,s in sorted(ports.items())},edges=edges,old_pairs_requiring_repair=lost,repair_capacity_assignment_succeeded=success))
    report=json.loads(verify(path))
    full=json.loads(path.with_suffix('.verification.json').read_text())
    report['bad_pair_types']=dict(collections.Counter(('old' if x<50 else 'new')+'-'+('old' if y<50 else 'new') for row in full['bad_pairs'] for x,y in [row['pair']]))
    report['repair_capacity_assignment_succeeded']=success
    report['old_pairs_requiring_repair']=len(lost)
    assert all(d==8 for d in full['degrees']) and full['edges']==236
    return report

if __name__=='__main__':
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
    OUT.mkdir(parents=True,exist_ok=True)
    assert not (OUT/'results.json').exists(), 'No unchanged repeat'
    catalog=classify();dump(OUT/'H_catalog.json',catalog)
    results=dict(H_catalog_cpu_seconds=catalog['cpu_seconds'],H_inputs=catalog['enumerated_inputs'],seeds={kind:seed(kind) for kind in ['adjacent','disjoint']},status='ANALYTIC_FAMILY_EXCLUSION',solver_run=False)
    dump(OUT/'results.json',results);print(json.dumps(results))

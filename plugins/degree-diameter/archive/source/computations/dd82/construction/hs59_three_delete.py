"""Three HS edge deletions: exact nine-vertex tree catalog and complete seeds."""
from hs_augmentation import ROOT,base,dump,verify
import collections,itertools,json,os,time
import networkx as nx
OUT=ROOT/'computations/dd82/construction/hs59_three_delete'

def catalog():
    start=time.process_time();entries=[]
    for i,T in enumerate(nx.nonisomorphic_trees(9)):
        edges=sorted(tuple(sorted(e)) for e in T.edges())
        adj=[set(T[v]) for v in range(9)]
        bad=[list(e) for e in itertools.combinations(range(9),2) if e[1] not in adj[e[0]] and not adj[e[0]]&adj[e[1]]]
        W=sum(len(s)*(len(s)-1)//2 for s in adj)
        assert len(bad)==28-W
        entries.append(dict(index=i,edges=edges,degrees=[len(s) for s in adj],wedge_count=W,bad_pairs=bad,bad_pair_count=len(bad),passes_global_pair_budget=len(bad)<=9))
    survivors=[x for x in entries if x['passes_global_pair_budget']]
    assert len(entries)==47 and len(survivors)==2
    return dict(networkx_version=nx.__version__,method='networkx.nonisomorphic_trees(9); exact edge/common-neighbor pair coverage',tree_count=len(entries),survivor_count=len(survivors),cpu_seconds=time.process_time()-start,survivors=survivors,all_trees=entries)

def seed(kind):
    original,ns=base();center=0;leaves=sorted(ns[0])[:3]
    deleted=[(0,x) for x in leaves];old=[e for e in original if e not in deleted]
    H=[(a,8) for a in range(8)] if kind=='star' else [(a,8) for a in range(1,8)]+[(0,7)]
    fixed={center:{0,1,2,3},**{v:{0,4+i} for i,v in enumerate(leaves)}}
    hdeg=[sum(a in e for e in H) for a in range(9)]
    caps=[8-hdeg[a]-sum(a in s for s in fixed.values()) for a in range(9)]
    # Three of the four retained center neighbors spend the three remaining
    # slots at color 0; the fourth cannot also use it in an eight-regular seed.
    forced_zero=sorted(ns[0]-set(leaves))[:caps[0]]
    ports=dict(fixed);ports.update({x:{0} for x in forced_zero});caps[0]-=len(forced_zero)
    free=[x for x in range(50) if x not in ports]
    colors=[a for a,c in enumerate(caps) for _ in range(c)]
    assert len(colors)==len(free) and min(caps)>=0
    ports.update({x:{a} for x,a in zip(free,colors)})
    edges=sorted(old+[(x,50+a) for x,s in ports.items() for a in sorted(s)]+[(50+a,50+b) for a,b in H])
    path=OUT/f'{kind}.seed.json'
    dump(path,dict(n=59,deleted_edges=deleted,auxiliary_edges=H,ports={str(x):sorted(s) for x,s in sorted(ports.items())},edges=edges,construction='fixed three-star endpoint ports, three retained center neighbors at color0, then increasing-label capacity fill'))
    compact=json.loads(verify(path));full=json.loads(path.with_suffix('.verification.json').read_text())
    assert full['edges']==236 and all(d==8 for d in full['degrees'])
    compact['bad_pair_types']=dict(collections.Counter(('old' if x<50 else 'new')+'-'+('old' if y<50 else 'new') for row in full['bad_pairs'] for x,y in [row['pair']]))
    compact['deleted_edges']=deleted
    return compact

if __name__=='__main__':
    os.sched_setaffinity(0,{min(os.sched_getaffinity(0))});OUT.mkdir(parents=True,exist_ok=True)
    assert not (OUT/'results.json').exists(), 'No unchanged repeat'
    trees=catalog();dump(OUT/'tree_catalog.json',trees)
    results=dict(status='ANALYTIC_FAMILY_EXCLUSION',solver_run=False,tree_count=trees['tree_count'],survivor_count=trees['survivor_count'],tree_catalog_cpu_seconds=trees['cpu_seconds'],seeds={kind:seed(kind) for kind in ['star','subdivided_star']})
    dump(OUT/'results.json',results);print(json.dumps(results))

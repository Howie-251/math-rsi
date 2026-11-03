"""Read the saved free-matching candidate and identify its actual obstruction."""
from pathlib import Path
import collections,itertools,json
directory=Path(__file__).resolve().parent/'petersen_all_matchings_run'
data=json.loads((directory/'candidate.best.json').read_text())
adj=[set() for _ in range(60)]
for u,v in data['edges']:adj[u].add(v);adj[v].add(u)
assert all(len(s)==8 for s in adj)
def image(u,j):
    row=[v for v in adj[u] if v//10==j];assert len(row)==1
    return row[0]
routes=[[image(image(u,k),5) for u in range(40,50)] for k in range(4)]
assert all(route==routes[0] for route in routes)
phi=routes[0];assert sorted(phi)==list(range(50,60))
assert all((v in adj[u])==(phi[v-40] in adj[phi[u-40]])
           for u,v in itertools.combinations(range(40,50),2))
assert all(adj[u]&set(range(40))==adj[phi[u-40]]&set(range(40))
           for u in range(40,50))
moore=[]
for removed in (4,5):
    vertices=set(range(60))-set(range(10*removed,10*removed+10))
    ns={u:adj[u]&vertices for u in vertices}
    assert all(len(s)==7 for s in ns.values())
    assert all(len(ns[u]&ns[v])==(0 if v in ns[u] else 1)
               for u,v in itertools.combinations(sorted(vertices),2))
    moore.append(dict(removed_fiber=removed,n=50,edges=175,degree=7,diameter=2,girth=5,
                      check='Every adjacent pair has 0 common neighbors and every nonadjacent pair exactly 1'))
bad_by_fibers=collections.Counter()
for u,v in itertools.combinations(range(60),2):
    if v not in adj[u] and not adj[u]&adj[v]:bad_by_fibers[u//10,v//10]+=1
cross_hist=collections.Counter(int(v in adj[u])+len(adj[u]&adj[v])
                              for u in range(40,50) for v in range(50,60))
assert bad_by_fibers=={(4,5):20} and cross_hist=={0:20,1:70,4:10}
result=dict(twin_map_4_to_5=phi,all_four_intermediate_routes=routes,
    twin_internal_graphs_isomorphic=True,twin_core_neighborhoods_identical=True,
    induced_moore_subgraphs=moore,cross_45_route_multiplicity=dict(sorted(cross_hist.items())),
    bad_by_fibers=[dict(fibers=list(k),count=v) for k,v in bad_by_fibers.items()],
    proved_twin_family_bad_pair_lower_bound=20,
    scope='Twin Petersen fibers with identical core neighbors; not all six-Petersen-fiber graphs')
(directory/'double_hs.analysis.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))

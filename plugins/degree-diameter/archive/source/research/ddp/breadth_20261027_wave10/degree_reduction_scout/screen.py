"""Fixed two-source mandatory-edge screen; no candidate pruning or BFS."""
from pathlib import Path
from collections import Counter
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(5,5))
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
started=time.process_time()

def read_graph(path):
    raw=[tuple(map(int,s.split())) for s in path.read_text().splitlines() if s.strip()]
    n,m=raw[0];edges=raw[1:]
    assert len(edges)==m
    adj=[set() for _ in range(n)]
    for u,v in edges:
        assert u!=v and v not in adj[u]
        adj[u].add(v);adj[v].add(u)
    return adj,sorted(tuple(sorted(e)) for e in edges)

def path_is_unique_length3(adj,path):
    u,a,b,v=path
    assert u!=v and v not in adj[u] and not (adj[u]&adj[v])
    mids=[(x,y) for x in adj[u] for y in adj[v] if y in adj[x]]
    assert mids==[(a,b)]

def inspect(tag,source,target_degree,savedL,source_check,cache=None):
    t=time.process_time()
    adj,edges=read_graph(ROOT/source);n=len(adj)
    unique=[]
    if cache:
        data=json.loads((ROOT/cache).read_text())
        for item in data:
            if item['NB3_path_count']==1:
                path=item['paths'][0];path_is_unique_length3(adj,path);unique.append(path)
        path_origin='existing_complete_distance3_paths_cache; local neighbor certificate checked, no BFS'
    else:
        # Root-to-target length3 path counts, restricted to targets outside
        # closed two-hop neighborhoods. These paths are automatically geodesic.
        for u in range(n):
            near={u}|adj[u]
            for a in adj[u]:near.update(adj[a])
            counts=Counter();first={}
            for a in adj[u]:
                for b in adj[a]:
                    if b==u:continue
                    for v in adj[b]:
                        if v>u and v not in near:
                            counts[v]+=1;first.setdefault(v,(u,a,b,v))
            for v,k in counts.items():
                if k==1:unique.append(list(first[v]))
        path_origin='complete direct length3 walk enumeration and closed2hop set test; no BFS'
    forced={}
    for path in unique:
        for u,v in zip(path,path[1:]):forced.setdefault(tuple(sorted((u,v))),path)
    forced_degree=Counter(x for e in forced for x in e)
    blocking=[u for u in range(n) if forced_degree[u]>target_degree]
    witness=None
    if blocking:
        u=blocking[0]
        witness=dict(vertex=u,target_degree=target_degree,forced_degree=forced_degree[u],incident_edges=[])
        for e,path in sorted(forced.items()):
            if u in e:
                path_is_unique_length3(adj,path)
                witness['incident_edges'].append(dict(edge=e,unique3_path=path,
                    endpoints_not_adjacent=True,endpoints_common_neighbors=0,
                    unique_middle_edge=[path[1],path[2]]))
    status='ALL_SPANNING_MAXDEGREE_SUBGRAPHS_BLOCKED' if blocking else 'NECESSARY_FORCED_DEGREE_SCREEN_PASSED_NO_EXISTENCE_CLAIM'
    result=dict(id=tag,status=status,source=source,source_validation_reused=source_check,
        source_n=n,source_m=len(edges),source_degree_histogram=dict(Counter(map(len,adj))),source_known_D=3,
        target_Delta=target_degree,target_D=3,savedL=savedL,order_margin=n-savedL,
        target_Moore_bound=1+target_degree*(1+(target_degree-1)+(target_degree-1)**2),
        n_preserved=True,target_edge_upper_bound=n*target_degree//2,
        minimum_edges_that_must_be_deleted=len(edges)-n*target_degree//2,
        each_vertex_required_deletions=[max(0,len(a)-target_degree) for a in adj],
        unique3_unordered_pairs=len(unique),forced_edge_count=len(forced),all_source_edges_forced=len(forced)==len(edges),
        forced_degree_histogram=dict(Counter(forced_degree[u] for u in range(n))),
        blocking_vertices=len(blocking),witness=witness,path_enumeration=path_origin,
        theorem='Every spanning subgraph with diameter<=3 must retain every edge of each unique source distance3 path; if their union has degree>targetDelta at one vertex no such subgraph exists.',
        scope='All spanning subgraphs of this exact source graph, with arbitrary edge deletions; no added edges, vertex deletions, or rewiring.',
        actual_candidate_graph_generated=False,actual_candidate_D=None,ordinary_candidate_bad_unordered_pairs=None,
        pruning_profiles=0,matching_searches=0,source_BFS_repeated=False,workers=1,CPU_seconds=time.process_time()-t)
    (OUT/f'{tag}.json').write_text(json.dumps(result,indent=2)+'\n')
    (OUT/f'{tag}.forced_edges.json').write_text(json.dumps([dict(edge=e,unique3_path=p) for e,p in sorted(forced.items())],indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['id','status','source_n','source_m','target_Delta','target_D','unique3_unordered_pairs','forced_edge_count','all_source_edges_forced','blocking_vertices','CPU_seconds']}),flush=True)
    return result

items=[inspect('source170_to_degree6',
    'research/ddp/breadth_20261027_wave7/signed_double340/source.edges',6,120,
    'research/ddp/breadth_20261027_wave7/signed_double340/source_check.json',
    'research/ddp/breadth_20261027_wave7/signed_double340/distance3_paths.json'),
    inspect('source253_to_degree7',
    'context/DD_PORTFOLIO_START_20261026/baselines/d8_D3_known.edges',7,170,
    'context/DD_PORTFOLIO_START_20261026/validation/d8_D3.json')]
summary=dict(status='TWO_FIXED_HIGHER_DEGREE_SOURCES_SCREENED_NO_PRUNING_PROFILE',
    candidates=items,source_reduction_history_checked=True,
    old_already_tried_scope_not_repeated='702/720 voltage graphs, four inverse-pair deletions each, eight degree5 graphs, old D6/D7 failures',
    selected_new_sources=2,graphs_generated=0,BFS_runs=0,matching_or_pruning_profiles=0,
    CPU_seconds=time.process_time()-started,workers=1,new_lower_bounds=0,
    next_automatic_action='NONE; do not extend sources/target/radius after these fixed-source failures')
(OUT/'RESULT.json').write_text(json.dumps(summary,indent=2)+'\n')

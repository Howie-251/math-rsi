#!/usr/bin/env python3
"""Run one bounded CPU experiment and independently verify every saved graph by BFS.
No search implementation is imported. Every pair distance is recomputed from edge files.
"""
import collections
import json
import pathlib
import subprocess
import time

ROOT=pathlib.Path(__file__).resolve().parent
PREFIX=ROOT/'n58_annealing_probe'
SEED=ROOT/'brown58_three_switch.seed.edges'

def inspect(path):
    rows=[list(map(int,line.split())) for line in path.read_text().splitlines() if line.strip()]
    n,m=rows[0]
    assert n==58 and m==232 and len(rows)==m+1
    adj=[set() for _ in range(n)]; seen=set()
    for u,v in rows[1:]:
        assert 0<=u<n and 0<=v<n and u!=v
        edge=tuple(sorted((u,v)));assert edge not in seen;seen.add(edge)
        adj[u].add(v);adj[v].add(u)
    degrees=[len(neighbors) for neighbors in adj]
    assert degrees==[8]*58
    hist=collections.Counter();missing=[]
    for u in range(n):
        dist=[-1]*n;dist[u]=0;queue=collections.deque([u])
        while queue:
            v=queue.popleft()
            for w in adj[v]:
                if dist[w]<0:dist[w]=dist[v]+1;queue.append(w)
        for v in range(u+1,n):
            hist[dist[v]]+=1
            if dist[v]<0 or dist[v]>2:missing.append([u,v])
    # This bitset objective is checked against BFS, not used to derive BFS distances.
    masks=[sum(1<<v for v in neighbors) for neighbors in adj]
    fast=0
    for u in range(n):
        covered=(1<<u)|masks[u]
        for v in adj[u]:covered|=masks[v]
        fast+=n-covered.bit_count()
    assert fast%2==0 and fast//2==len(missing)
    return {'n':n,'m':m,'simple':True,'degrees':degrees,
            'distance_histogram':dict(sorted(hist.items())),
            'connected':-1 not in hist,'diameter':max(hist) if -1 not in hist else None,
            'uncovered_pair_count':len(missing),'uncovered_pairs':missing,
            'bitset_objective_matches_independent_bfs':True,
            'valid_degree8_diameter2':not missing,
            'adjacency':[sorted(neighbors) for neighbors in adj]}

brown_rows=[list(map(int,line.split())) for line in (ROOT/'brown57.edges').read_text().splitlines() if line.strip()]
brown_edges={tuple(sorted(edge)) for edge in brown_rows[1:]}
brown_degrees=[sum(v in edge for edge in brown_edges) for v in range(57)]
hub_neighbors=[v for v in range(57) if brown_degrees[v]==7]
seed_rows=[list(map(int,line.split())) for line in SEED.read_text().splitlines() if line.strip()]
assert {tuple(sorted(edge)) for edge in seed_rows[1:]}==brown_edges|{(v,57) for v in hub_neighbors}
initial=inspect(SEED)
assert initial['uncovered_pair_count']==21
command=['taskset','-c','127',str(PREFIX)+'.bin',str(SEED),'60','2026101117',str(PREFIX)]
started=time.monotonic()
with open(str(PREFIX)+'.log','w') as log:
    completed=subprocess.run(command,stdout=log,stderr=subprocess.STDOUT,timeout=75,check=True)
search_wall=time.monotonic()-started
raw=json.loads(pathlib.Path(str(PREFIX)+'.raw.json').read_text())
assert raw['initial_uncovered_pairs']==initial['uncovered_pair_count']
best=inspect(pathlib.Path(str(PREFIX)+'.best.edges'))
assert best['uncovered_pair_count']==raw['best_uncovered_pairs']
for record in raw['rounds']:
    ending=inspect(pathlib.Path(str(PREFIX)+f".round{record['round']}.final.edges"))
    assert ending['uncovered_pair_count']==record['final_uncovered_pairs']
    record['independent_final_bfs']=ending
result={
    'status':'valid_graph_found' if best['valid_degree8_diameter2'] else 'diagnostic_not_a_target_graph',
    'scope':'Six finite stochastic trajectories; no exhaustive or nonexistence claim.',
    'seed_provenance':{'verified_against':'brown57.edges','operation':'retain every Brown57 edge and join vertex57 to exactly the eight degree7 vertices','hub_neighbors':hub_neighbors,'exact_edge_set_equality':True},
    'prior_evidence':'Existing two-switch annealing (5 s) had best 21; the full three-edge-switch neighborhood had minimum 34. This probe changes the move neighborhood to include alternating 4--7 edge cycles and allows uphill steps.',
    'move_definition':'Choose k disjoint existing edges (a_i,b_i), k in {2,4,5,6,7}; replace them by (a_i,b_(i+1 mod k)) when every new edge is absent. Each endpoint loses and gains exactly one edge.',
    'proposal_mix':{'k2':0.6,'k4':0.1,'k5':0.1,'k6':0.1,'k7':0.1},
    'proposal_bias':'Half of proposals attempt to create a path for a currently missing pair; this is an optimization heuristic, not a stationary-distribution sampler.',
    'acceptance':'Accept delta<=0; otherwise accept with probability exp(-delta/T). Each round starts from the actual Brown-plus-hub seed and cools geometrically.',
    'cpu_affinity':[127],'threads':1,'command':command,'process_returncode':completed.returncode,
    'subprocess_wall_seconds':search_wall,'initial_independent_bfs':initial,
    'run':raw,'best_candidate_independent_bfs':best,
    'valid_degree8_diameter2':best['valid_degree8_diameter2'],
}
result['aggregate_move_counts']={k:{field:sum(record['by_cycle_length'][k][field] for record in raw['rounds']) for field in ['proposals','legal','accepted','uphill_accepted']} for k in ['2','4','5','6','7']}
result['best_candidate_identical_to_seed']=pathlib.Path(str(PREFIX)+'.best.edges').read_text()==SEED.read_text()
pathlib.Path(str(PREFIX)+'.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':result['status'],'wall_seconds':search_wall,'initial':initial['uncovered_pair_count'],'best':best['uncovered_pair_count'],'round_finals':[r['final_uncovered_pairs'] for r in raw['rounds']],'legal_moves':sum(s['legal'] for r in raw['rounds'] for s in r['by_cycle_length'].values()),'accepted_uphill':sum(s['uphill_accepted'] for r in raw['rounds'] for s in r['by_cycle_length'].values())},indent=2))

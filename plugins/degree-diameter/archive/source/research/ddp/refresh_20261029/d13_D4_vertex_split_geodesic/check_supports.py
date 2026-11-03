#!/usr/bin/env python3
"""81 exact geodesic-support BFS runs; no changed graph is generated."""
from collections import Counter, deque
from pathlib import Path
import json
import resource
import time

started = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
here = Path(__file__).resolve().parent
project = here.parents[3]
source = project / 'research/ddp/more_graphs_20261027/d13_D4_current6804/source6804.edges'
adj = [[] for _ in range(6804)]
for line in source.read_text().splitlines():
    if not line.strip() or line.startswith('#'):
        continue
    u,v = map(int,line.split())
    adj[u].append(v)
    adj[v].append(u)
for row in adj:
    row.sort()

all_colors = (1<<4096)-1
# Bit k encodes the partition A=1|(k<<1); neighbor 0 is always in A.
truth = [all_colors]
for j in range(1,13):
    block = 1<<(j-1)
    truth.append(sum(((1<<block)-1)<<start for start in range(block,4096,2*block)))
constraint_cache = {}
def bichromatic_assignments(support):
    if support not in constraint_cache:
        same_a = same_b = all_colors
        bits = support
        while bits:
            bit = bits & -bits
            j = bit.bit_length()-1
            same_a &= truth[j]
            same_b &= all_colors ^ truth[j]
            bits ^= bit
        constraint_cache[support] = all_colors ^ (same_a | same_b)
    return constraint_cache[support]

records = []
passing_roots = []
status = 'COMPLETE'
with (here/'ROOTS.jsonl').open('w') as output:
    for root in range(81):
        if time.process_time()-started > 8.5:
            status = 'BUDGET_PARTIAL'
            break
        neighbors = adj[root]
        assert len(neighbors)==13
        first_bit = {v:1<<i for i,v in enumerate(neighbors)}
        distance = [-1]*6804
        support = [0]*6804
        parent = [-1]*6804
        distance[root] = 0
        queue = deque([root])
        while queue:
            u = queue.popleft()
            if distance[u] == 4:
                continue
            nd = distance[u]+1
            for v in adj[u]:
                mask = first_bit[v] if u==root else support[u]
                if distance[v] == -1:
                    distance[v] = nd
                    support[v] = mask
                    parent[v] = u
                    queue.append(v)
                elif distance[v] == nd:
                    support[v] |= mask
        assert min(distance)==0 and max(distance)==4
        far = [v for v,d in enumerate(distance) if d==4]
        histogram = Counter(support[v] for v in far)
        assert all(histogram)
        singletons = [v for v in far if support[v].bit_count()==1]
        witness = None
        if singletons:
            target = singletons[0]
            path = []
            v = target
            while v!=-1:
                path.append(v)
                v=parent[v]
            path.reverse()
            witness = {
                'target':target, 'distance':4, 'support_mask':support[target],
                'only_first_neighbor':neighbors[support[target].bit_length()-1],
                'one_shortest_path':path,
            }
            partitions = []
            property_b_tested = False
        else:
            valid = all_colors
            for mask in sorted(histogram,key=lambda s:(s.bit_count(),s)):
                valid &= bichromatic_assignments(mask)
                if not valid:
                    break
            partitions = []
            while valid:
                bit = valid & -valid
                k = bit.bit_length()-1
                a_mask = 1|(k<<1)
                A = [v for j,v in enumerate(neighbors) if a_mask&(1<<j)]
                B = [v for j,v in enumerate(neighbors) if not a_mask&(1<<j)]
                assert 1<=len(A)<=12 and 1<=len(B)<=12
                partitions.append({'A':A,'B':B,'A_mask':a_mask})
                valid ^= bit
            property_b_tested = True
        row = {
            'root':root,'controller':0,
            'fiber':[(root//3**i)%3 for i in range(4)],
            'ordered_neighbors':neighbors,
            'distance_histogram':dict(sorted(Counter(distance).items())),
            'distance4_targets':len(far),
            'distinct_supports':len(histogram),
            'support_histogram':dict(sorted(histogram.items())),
            'minimum_support_size':min(s.bit_count() for s in histogram),
            'singleton_target_count':len(singletons),
            'singleton_targets':singletons,
            'singleton_witness':witness,
            'property_b_tested':property_b_tested,
            'passing_partition_count':len(partitions),
            'passing_partitions':partitions,
        }
        records.append(row)
        output.write(json.dumps(row,separators=(',',':'))+'\n')
        output.flush()
        if partitions:
            passing_roots.append(root)
            print(json.dumps({'event':'ROOT_GATE_PASS','root':root,'partitions':len(partitions)}),flush=True)

result = {
    'status':status if status!='COMPLETE' else ('COMPLETE_NO_ADJACENT_SPLIT' if not passing_roots else 'COMPLETE_HAS_ROOT_GATE_PASS'),
    'source':str(source.relative_to(project)),
    'representative_roots_completed':len(records),
    'representative_roots_total':81,
    'literal_roots_covered_by_left_action':84*len(records),
    'roots_rejected_by_singleton':sum(bool(r['singleton_target_count']) for r in records),
    'roots_requiring_property_b':sum(r['property_b_tested'] for r in records),
    'property_b_assignment_domain_per_tested_root':4096,
    'passing_roots':passing_roots,
    'passing_partitions_total':sum(r['passing_partition_count'] for r in records),
    'singleton_target_count_min':min(r['singleton_target_count'] for r in records),
    'singleton_target_count_max':max(r['singleton_target_count'] for r in records),
    'bfs_runs':len(records),
    'changed_graphs_generated':0,
    'changed_graph_bfs_runs':0,
    'cpu_seconds':time.process_time()-started,
    'next_root_cursor':len(records),
}
(here/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(here/'TERMINAL.json').write_text(json.dumps({**result,'running':False,'pending':[]},indent=2)+'\n')
print(json.dumps(result,separators=(',',':')))

"""One exact check of the undirected base-four shift graph and additive repair."""
from collections import Counter, deque
from datetime import datetime, timezone
from pathlib import Path
import json
import sys
import time

P = Path(__file__).resolve().parent
assert not (P / 'terminal.json').exists(), 'Reuse this completed check; do not rerun.'
started = time.process_time()
n, alphabet, degree_cap, target = 256, 4, 8, 3
edges = set()
loops = 0
arcs = 0
for x in range(n):
    for digit in range(alphabet):
        arcs += 1
        y = (alphabet*x+digit) % n
        if x == y:
            loops += 1
        else:
            edges.add(tuple(sorted((x,y))))
edges = sorted(edges)
adj = [set() for _ in range(n)]
for u, v in edges:
    adj[u].add(v)
    adj[v].add(u)
degrees = list(map(len, adj))
assert max(degrees) <= degree_cap
spare = [u for u in range(n) if degrees[u] < degree_cap]
distance_rows = []
ordered_histogram = Counter()
for root in range(n):
    dist = [-1]*n
    dist[root] = 0
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if dist[v] < 0:
                dist[v] = dist[u]+1
                queue.append(v)
    assert -1 not in dist
    distance_rows.append(dist)
    ordered_histogram.update(dist)
distance_to_spare = [min(row[v] for v in spare) for row in distance_rows]
def suitable(u, v):
    return distance_rows[u][v] > target and distance_to_spare[u] >= 2 and distance_to_spare[v] >= 2
if suitable(27,73):
    witness = (27,73)
else:
    witness = next(((u,v) for u in range(n) for v in range(u+1,n) if suitable(u,v)), None)
def word(x):
    return ''.join(str((x//(4**k)) % 4) for k in (3,2,1,0))
check = dict(
    n=n, edges=len(edges), raw_directed_arcs=arcs, discarded_loops=loops,
    simple=True, connected=True, minimum_degree=min(degrees), maximum_degree=max(degrees),
    degree_histogram=dict(sorted(Counter(degrees).items())), diameter=max(ordered_histogram),
    roots_checked=n, ordered_distance_histogram=dict(sorted(ordered_histogram.items())),
    target_diameter=target,
    bad_unordered_pairs=sum(c for d,c in ordered_histogram.items() if d>target)//2,
    spare_vertices=spare, spare_base4_words=[word(v) for v in spare],
    spare_degree_slots=sum(degree_cap-degrees[v] for v in spare),
    source_definition='For x in Z256 and a in {0,1,2,3}, add the undirected edge {x,(4*x+a) mod256}; discard loops and merge duplicate edges.',
    method='Ordinary deque BFS independently from every one of the256 vertices; no transitivity assumption.',
    CPU_seconds=time.process_time()-started,
)
obstruction = dict(
    status='VERIFIED_ADDITIVE_REPAIR_OBSTRUCTION' if witness is not None else 'NO_WITNESS_FOUND_NOT_EXCLUDED',
    scope='All simple graphs on the same256 vertices which retain every source edge and have maximum degree at most8. Edge deletion or rewiring is outside this scope.',
    reason='Any new edge must have both endpoints among the vertices of source degree below8. For the witness pair, a path using new edges needs at least two old steps to enter this set, at least one new edge, and at least two old steps to leave it, so has length at least5. A path using no new edges has source distance4.',
    witness=None,
    no_random_augmentation_profile=True,
)
if witness is not None:
    u,v = witness
    obstruction['witness'] = dict(u=u,v=v,base4_words=[word(u),word(v)],source_distance=distance_rows[u][v],distance_u_to_spare=distance_to_spare[u],distance_v_to_spare=distance_to_spare[v],new_edge_path_lower_bound=distance_to_spare[u]+1+distance_to_spare[v],source_u_to_spare_distances={str(x):distance_rows[u][x] for x in spare},source_v_to_spare_distances={str(x):distance_rows[v][x] for x in spare})
assert not check['diameter'] <= target, 'Unexpected target hit: notify parent before continuing.'
assert check['diameter'] == 4
assert Counter(degrees) == Counter({8:240,7:12,6:4})
assert len(spare) == 16
report = '# 256点无向状态移位图：实际检查与度余量补边障碍\n\n'
report += '本次只检查明确的边规则 x—(4x+a) mod256，a=0,1,2,3；去自环、合并重边。没有采信原互审中的可逆模假设：4在模256下没有逆元，反向邻居由入边直接给出。图也不是顶点传递，不能只检查根0。\n\n'
report += f'实际展开256点、{len(edges)}条无向边；度分布为6度4点、7度12点、8度240点。一次普通全256根BFS确认连通、直径4；距离大于3的无序点对有{check["bad_unordered_pairs"]}个。没有得到目标(8,3)的新下界。\n\n'
if witness is not None:
    w=obstruction['witness']
    report += '## 保留旧边时的准确补边障碍\n\n'
    report += f'源中只有16个顶点度数不足8，共20个度余量。任何保留全部源边、最大度仍不超过8的新边，其两端都必须在该16点集合P内。点对({w["u"]},{w["v"]})（四进制{w["base4_words"][0]}/{w["base4_words"][1]}）在源图中的距离是4，两端到P的距离分别为{w["distance_u_to_spare"]}、{w["distance_v_to_spare"]}。故任何使用新增边的连接路线至少需要{w["new_edge_path_lower_bound"]}步；不使用新增边则仍至少4步。由此任何仅填充度余量的补边都不能把直径降到3。\n\n'
else:
    report += '未找到指定类型的度余量障碍；这只表示该检验未闭，没有启动随机补边。\n\n'
report += '本结论只排除固定源的单调补边，不排除删除/重连源边、其他字母表或其他状态图。本次没有匹配优化、随机补边或其他参数搜索。source.edges保存完整边表；source_check.json保存全源结果；obstruction.json保存精确见证。\n'
ROOT=P.parents[3]
sys.path.insert(0,str(ROOT/'aris_repo/tools'))
from capture_filter import screen
assert not screen(report), screen(report)
(P/'source.edges').write_text(f'{n} {len(edges)}\n'+''.join(f'{u} {v}\n' for u,v in edges))
(P/'source_check.json').write_text(json.dumps(check,indent=2)+'\n')
(P/'source_distances.json').write_text(json.dumps(distance_rows)+'\n')
(P/'obstruction.json').write_text(json.dumps(obstruction,indent=2)+'\n')
(P/'REPORT.md').write_text(report)
terminal=dict(status='STOPPED_FIXED_SOURCE_AUGMENTATION_OBSTRUCTION' if witness else 'SOURCE_CHECK_ONLY_NOT_EXCLUDED',running=False,source_graphs_generated=1,source_BFS_roots=256,random_augmentation_profiles=0,source_diameter=check['diameter'],source_bad_pairs=check['bad_unordered_pairs'],augmentation_template_excluded=witness is not None,all_state_shift_graphs_excluded=False,CPU_seconds=time.process_time()-started,CPU_budget_seconds=5,pending=[],restarts=0,completed_at_utc=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'))
assert terminal['CPU_seconds'] < 5
(P/'terminal.json').write_text(json.dumps(terminal,indent=2)+'\n')
print(json.dumps(dict(terminal=terminal,witness=obstruction['witness']),ensure_ascii=False))

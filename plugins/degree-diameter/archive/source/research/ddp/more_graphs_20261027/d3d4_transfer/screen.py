"""Fixed-source degree/slack and forced-class cover screen; no BFS or solver."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import json
import time
import resource

START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (115, 120))
OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]

def histogram(g):
    return {str(k): v for k, v in sorted(Counter(map(len, g)).items())}

def implicit(path):
    rows = [list(map(int, line.split())) for line in path.read_text().splitlines()
            if line.strip() and not line.startswith('#')]
    g = list(map(set, rows))
    assert all(len(row) == len(gs) for row, gs in zip(rows, g))
    assert all(u != v and 0 <= v < len(g) and u in g[v] for u, ns in enumerate(g) for v in ns)
    return g

def raw_adjacency(path, n):
    edges = set()
    seen = set()
    for line in path.read_text().splitlines():
        if not line.strip() or line.startswith('#'):
            continue
        u, *vs = map(int, line.split())
        seen.add(u)
        for v in vs:
            assert 0 <= u < n and 0 <= v < n and u != v
            edges.add(tuple(sorted((u, v))))
    g = [set() for _ in range(n)]
    for u, v in edges:
        g[u].add(v); g[v].add(u)
    return g

def edge_list(path, n):
    rows = [tuple(map(int, line.split())) for line in path.read_text().splitlines()
            if line.strip() and not line.startswith('#')]
    if rows[0][0] == n:
        assert len(rows) - 1 == rows[0][1]
        rows = rows[1:]
    assert all(len(r) == 2 for r in rows)
    assert len(set(tuple(sorted(r)) for r in rows)) == len(rows)
    g = [set() for _ in range(n)]
    for u, v in rows:
        assert u != v and 0 <= u < n and 0 <= v < n
        g[u].add(v); g[v].add(u)
    return g

# Read current official raw sources, without trusting row lengths for NX half-adjacency41.
g650 = implicit(OUT / 'source650.implicit_adj.txt')
g715 = implicit(OUT / 'source715.implicit_adj.txt')
g41 = raw_adjacency(OUT / 'source41_1a.raw_adj.txt', 41)
g72 = implicit(OUT / 'source72.implicit_adj.txt')
g810 = raw_adjacency(OUT / 'source810.raw_adj.txt', 810)
assert len(g650) == 650 and len(g715) == 715

slack = [u for u in range(715) if len(g715[u]) < 11]
S = set(slack)
by_signature = {}
for u in slack:
    by_signature.setdefault(tuple(sorted(g715[u] - S)), []).append(u)
classes = [sorted(v) for _, v in sorted(by_signature.items())]
assert len(classes) == 65 and all(len(c) == 3 for c in classes)
class_of = {v: i for i, c in enumerate(classes) for v in c}
class_records = []
for i, c in enumerate(classes):
    outside = g715[c[0]] - S
    assert len(outside) == 8 and all(g715[u] - S == outside for u in c)
    assert all(not ((g715[u] & S) - set(c)) for u in c)
    class_records.append({'class': i, 'members': c, 'common_saturated_neighbors': sorted(outside),
                          'internal_edges': [[u, v] for u in c for v in c if u < v and v in g715[u]]})
assert all(len(g715[u]) == 11 for u in range(715) if u not in S)
assert all(len({class_of[v] for v in g715[u] & S}) == 1 for u in range(715) if u not in S)
# Literal length0/1/2 walk expansion, not source BFS: verify every eligible pin hits one class.
pin_records = []
all_union = set()
for u in slack:
    r2 = {u} | g715[u]
    for v in g715[u]:
        r2 |= g715[v]
    covered = sorted(r2 & S)
    assert set(covered) == set(classes[class_of[u]])
    all_union |= r2
    pin_records.append({'pin': u, 'class': class_of[u], 'R2_eligible_targets': covered})
canonical = [c[0] for c in classes]
cover = set()
for u in canonical:
    cover |= {u} | g715[u]
    for v in g715[u]:
        cover |= g715[v]
assert len(cover) == 715

# The old585 radius2/slack fact is reused, not recomputed.
old585 = json.loads((ROOT / 'research/ddp/polarity585_replication/SOURCE_PARTITION_CHECK.json').read_text())
oldR2 = json.loads((ROOT / 'research/ddp/breadth_20261027_wave3/tits585_batch_extension/RESULT.json').read_text())
assert old585['degree_histogram'] == {'8': 65, '9': 520}
assert oldR2['radius_two_absolute_count_histogram_A'] == {'1': 65}

observed_regular = []
def add_regular(label, g, cap, D, path):
    hist = histogram(g)
    assert hist == {str(cap): len(g)}
    observed_regular.append({'label': label, 'D': D, 'degree_cap': cap, 'source_n': len(g),
        'source_m': sum(map(len, g)) // 2, 'degree_histogram': hist,
        'eligible_pins': 0, 'mechanism_status': 'CLOSED_NO_SOURCE_DEGREE_SLACK', 'source': path})

add_regular('Allwright41_1a', g41, 4, 3, 'source41_1a.raw_adj.txt')
add_regular('Exoo72', g72, 5, 3, 'source72.implicit_adj.txt')
add_regular('Dhar810', g810, 12, 3, 'source810.raw_adj.txt')
for label, n, cap, D, path in [
    ('Michel120',120,6,3,'context/DD_PORTFOLIO_START_20261026/baselines/d6_D3_known.edges'),
    ('source170',170,7,3,'research/ddp/breadth_20261027_wave7/signed_double340/source.edges'),
    ('CM253',253,8,3,'context/DD_PORTFOLIO_START_20261026/baselines/d8_D3_known.edges'),
    ('Rajiv252',252,5,4,'research/ddp/breadth_20261027_wave7/rajiv252_cell_structure/regenerated252.edges'),
    ('Rajiv441',441,6,4,'research/ddp/second_mechanism/rajiv441.edges'),
    ('Michel684',684,7,4,'research/ddp/m1_sources/graph_7_4_n684.txt'),
    ('Loz1100',1100,8,4,'context/DD_PORTFOLIO_START_20261026/baselines/d8_D4_known.edges'),
    ('Dhar2485',2485,10,4,'context/DD_PORTFOLIO_START_20261026/baselines/d10_D4_known.edges')]:
    add_regular(label, edge_list(ROOT / path, n), cap, D, path)
add_regular('Delorme650_actual_official_source',g650,10,3,'source650.implicit_adj.txt')

structural_D4 = [
    {'degree_cap':4,'n':104,'m':208,'degree_histogram':{'4':104},'evidence_kind':'reused existing raw-source verification','source':'research/ddp/breadth_20261027_wave2/sources/bhakar104_check.json'},
    {'degree_cap':9,'n':1768,'m':7956,'degree_histogram':{'9':1768},'evidence_kind':'derived from official construction counts and maximum degree9','derivation':'m=1700*9/2-191+497=7956=1768*9/2; every degree<=9 implies every degree=9'},
    {'degree_cap':11,'n':3444,'m':18942,'degree_histogram':{'11':3444},'evidence_kind':'official description explicitly11-regular; not re-downloaded'},
    {'degree_cap':12,'n':5832,'m':34992,'degree_histogram':{'12':5832},'evidence_kind':'official description explicitly12-regular route-chart lift; not re-downloaded'}]

result = {
 'status':'COMPLETE_FIXED_SOURCE_MONOTONE_EXTENSION_SCREEN_NO_LIVE_SINGLE_VERTEX_MODEL',
 'baseline_read_UTC_date':datetime.now(timezone.utc).strftime('%Y-%m-%d'),
 'official_table_url':'https://web.mat.upc.edu/francesc.comellas/delta-d/taula_delta_d.html',
 'official_D3_url':'https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html',
 'official_D4_url':'https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html',
 'mechanism':'Retain all edges of one fixed known source; append one vertex or a stated small block at the same maximum-degree cap.',
 'observed_regular_sources':observed_regular,
 'D4_structural_regularity_sources':structural_D4,
 'source585_reused':{'n':585,'m':2600,'degree_cap':9,'degree_histogram':old585['degree_histogram'],
   'eligible_pins':65,'eligible_target_classes':65,'targets_per_class':1,'classes_hit_by_each_eligible_R2':1,
   'minimum_eligible_R2_cover':65,'new_vertex_pin_budget':9,'single_vertex_scope':'All choices of at most9 eligible pins; excluded.',
   'small_block_scope':'Any monotone added block of size<=7 is impossible: every65 class needs an old-new spoke but total spokes<=9t<65.',
   'old_radius2_evidence_reused':True,'source_BFS_repeated':False},
 'source650':{'n':650,'m':3250,'degree_cap':10,'degree_histogram':histogram(g650),'eligible_pins':0,
   'scope':'Every retained old vertex is saturated: no connected monotone extension by any positive number of new vertices at cap10.'},
 'source715':{'n':715,'m':3770,'degree_cap':11,'degree_histogram':histogram(g715),'eligible_pins':195,
   'saturated_vertices':520,'eligible_target_classes':65,'targets_per_class':3,
   'classes_hit_by_each_eligible_R2':1,'eligible_targets_hit_per_R2':3,
   'union_of_all_eligible_R2_size':len(all_union),'canonical65pin_R2_cover_size':len(cover),
   'minimum_eligible_R2_cover':65,'new_vertex_pin_budget':11,
   'canonical65pin_cover':canonical,'classes':class_records,'per_pin_target_certificate':pin_records,
   'single_vertex_scope':'All choices of at most11 eligible pins; excluded by65 disjoint target classes.',
   'small_block_scope':'Any monotone added block of size<=5 is impossible: every65 class needs an old-new spoke but total spokes<=11t<65.',
   'larger_or_cooperative_blocks_closed':False},
 'mathematical_rejection_rule':'A union of all eligible balls covering the source is not a budgeted cover.65 class constraints require65 distinct chosen pins.',
 'new_candidate_graphs_generated':0,'new_lower_bounds':0,'ordinary_bad_unordered_pairs':None,
 'solver_calls':0,'greedy_starts':0,'source_all_pairs_BFS_calls':0,
 'new_length2_walk_checks':195,'CPU_seconds':time.process_time()-START,
 'not_excluded':['Other source graphs or Allwright41 variants not structurally identical to checked source1a.','Deleting or replacing old edges.','Larger cooperative blocks in the nonregular585/715 sources.','Changing degree cap or construction geometry.'],
 'next_action':'Stop these fixed-source single-vertex models; no solver or seed search. Any continuation requires an explicit change to the excluded premises.',
 'pending':[]}
(OUT/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['observed_regular_sources','source715']},ensure_ascii=False,indent=2))
print('SOURCE715_SUMMARY',json.dumps({k:v for k,v in result['source715'].items() if k not in ['classes','per_pin_target_certificate','canonical65pin_cover']},ensure_ascii=False))

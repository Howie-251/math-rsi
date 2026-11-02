"""One frozen two-helper counterfactual, reusing monotone source certificates."""
from collections import deque
import json
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PREDICTION = HERE.parent / 'h9_global_rule/P6_PREDICTION.md'
assert PREDICTION.exists()
started = time.process_time()
old = json.loads((HERE / 'RESULT.json').read_text())
source = ROOT / 'research/ddp/breadth_20261027_wave4/pencil_source/deg12_diam5_n42342.txt'
adj = [set() for _ in range(42342)]
for line in source.read_text().splitlines():
    if not line.strip() or line.lstrip().startswith('#'):
        continue
    v, *neighbors = map(int, line.split())
    adj[v] = set(neighbors)
helpers = {42177, 42291}
base = set(range(42177)) | helpers
static = {row['vertex']: row for row in old['static_rows']}
remaining = set(range(42177, 42342)) - helpers
assert len(remaining) == 163
assert all(static[v]['core_R4_missing'] == 0 for v in helpers)
assert old['static_pair_distance_le3_failed_pairs'] == 1
# The only old pinset pair failing <=3 was (42293,42329), so each
# remaining pinset reaches each helper in <=4. Monotonicity reuses all
# old R4 coverage rows that already succeeded. Only seven need new BFS.
new_rows = []
for v in sorted(remaining):
    row = static[v]
    if row['core_R4_missing'] == 0:
        continue
    pins = adj[v] & base
    seen = set(pins)
    q = deque((a, 0) for a in pins)
    while q:
        a, distance = q.popleft()
        if distance == 4:
            continue
        for b in adj[a]:
            if b in base and b not in seen:
                seen.add(b)
                q.append((b, distance + 1))
    missing = sorted(base - seen)
    new_rows.append(dict(vertex=v, base_R4_missing=len(missing),
                         missing_sample=missing[:12]))
# Reuse all static successful pair certificates. Explicitly check the
# sole failed pair's new three-edge pinset path, from P5's saved witness.
pin_path = [36398, 42291, 14650, 9751]
assert all(x in base for x in pin_path)
assert pin_path[0] in adj[42293] and pin_path[-1] in adj[42329]
assert all(b in adj[a] for a, b in zip(pin_path, pin_path[1:]))
failed = [r['vertex'] for r in new_rows if r['base_R4_missing']]
result = dict(
    prediction='P6_FIXED_TWO_HELPER_GLOBAL_LAYER',
    status='SUPPORTED' if not failed else 'REFUTED',
    old_base_order=42177, helpers=sorted(helpers), base_order=len(base),
    remaining_vertices=len(remaining),
    old_R4_success_rows_reused=sum(static[v]['core_R4_missing'] == 0 for v in remaining),
    remaining_to_both_helpers_R4_certificates_reused=2*len(remaining),
    newly_tested_R4_rows=new_rows,
    all163_R4_pass=not failed,
    failed_vertices=failed,
    all_remaining_pinset_pairs_distance_le3=True,
    formerly_failing_pair=[42293,42329], repaired_pair_pin_path=pin_path,
    helper_base_D5_justification='Reused P1 individual R4 and pair certificates; proven prefix D5 from P3.',
    decision='No third helper or pin changes. Two-helper layer fails globally.' if failed else 'Two-helper batch certificate established for existing source subgraph.',
    new_multisource_BFS_count=len(new_rows),
    full_all_source_BFS_performed=False, new_graphs_generated=0,
    optimization=False, CPU_seconds=time.process_time()-started)
(HERE/'P6_RESULT.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(result, ensure_ascii=False, indent=2))

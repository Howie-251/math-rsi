"""The one formal first-center calibration; never generates another candidate."""
from collections import Counter, deque
from pathlib import Path
import json
import time


def check(here):
    begin = time.process_time()
    formal = json.loads((here / 'first.formal_center.json').read_text())
    source = json.loads((here / 'source.json').read_text())
    U, V, h = source['edge_u'], source['edge_v'], formal['voltages']
    z = formal['center_mask']
    assert len(formal['slots']) == 512
    by_forms = [[-1] * 256 for _ in range(4)]
    for slot, forms in enumerate(formal['slots']):
        root, rem = divmod(slot, 128)
        orbit, q = divmod(rem, 32)
        for mask, constant, length in forms:
            central = constant ^ ((mask & z).bit_count() & 1)
            target = 64 * orbit + q % 16 + 16 * central + 32 * (q // 16)
            old = by_forms[root][target]
            if old < 0 or length < old:
                by_forms[root][target] = length
    assert by_forms == formal['radius3_distances']
    # Independent direct tuple multiplication, not the C++ multiplication table.
    edges = set()
    for u, v, voltage in zip(U, V, h):
        y, t = voltage % 32, voltage // 32
        for x in range(32):
            for s in range(2):
                image_x = (x + (-1) ** s * y + 16 * s * t) % 32
                edges.add((64 * u + x + 32 * s, 64 * v + image_x + 32 * (s ^ t)))
    assert len(edges) == 1024 and all(a < b for a, b in edges)
    adj = [[] for _ in range(256)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    assert all(len(row) == len(set(row)) == 8 for row in adj)
    distances = []
    for root in (0, 64, 128, 192):
        d = [-1] * 256
        d[root] = 0
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if d[v] < 0:
                    d[v] = d[u] + 1
                    queue.append(v)
        distances.append(d)
    clipped = [[x if 0 <= x <= 3 else -1 for x in row] for row in distances]
    assert clipped == by_forms
    missing = [sum(x < 0 or x > 3 for x in row) for row in distances]
    assert missing == formal['score']['root_misses']
    assert sum(missing) == formal['score']['score_sum']
    report = {
        'status': 'COMPLETE', 'scope': 'only first formal entered projection, first legal center mask',
        'projection_cursor': formal['projection_cursor'], 'center_mask': z,
        'n': 256, 'm': 1024, 'simple': True, 'minimum_degree': 8, 'maximum_degree': 8,
        'root_labels': [0, 64, 128, 192], 'roots_checked': 4,
        'all1024_root_target_radius3_distances_match_forms': True,
        'score_reused_in_production': formal['score_reused_in_production'],
        'root_misses': missing, 'bad_unordered_pairs': 32 * sum(missing),
        'connected': all(-1 not in row for row in distances),
        'root_distance_histograms': [dict(sorted(Counter(row).items())) for row in distances],
        'CPU_seconds': time.process_time() - begin,
    }
    (here / 'first.independent_distances.json').write_text(json.dumps(distances) + '\n')
    (here / 'first.independent_check.json').write_text(json.dumps(report, indent=2) + '\n')
    return report


if __name__ == '__main__':
    here = Path(__file__).resolve().parent
    assert not (here / 'first.independent_check.json').exists(), 'Do not repeat the formal calibration.'
    print(json.dumps(check(here)))

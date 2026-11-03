from pathlib import Path
import json, random

P = Path(__file__).resolve().parent
B = P.parent.parent / 'breadth_20261027_wave3' / 'hexagon_partial_fold_scout'
q = json.loads((B / 'Q_data.json').read_text())
w2 = json.loads((B / 'witness12_state.json').read_text())['states']
w3 = json.loads((B / 'partial_fold_source/witnesses/pf_d13_k5_n50750.json').read_text())
N = len(q['Q'])
def bits(s):
    return [(b >> j) & 1 for b in bytes.fromhex(s) for j in range(7, -1, -1)][:N]
s3, c3 = bits(w3['split']), bits(w3['colour'])
d3 = [1 + c3[i] if s3[i] else 0 for i in range(N)]
assert N == 33033 and sum(x != 0 for x in d3) == 17157
rng = random.Random(2026102704)
broken = []
reset = []
for i, st in enumerate(w2):
    do_reset = rng.random() < .5
    reset.append(do_reset)
    split = (rng.random() < .27) if do_reset else bool(st)
    broken.append(1 + rng.randrange(2) if split else 0)
initials = [[0] * N, d3, broken]
with (P / 'input.txt').open('w') as f:
    print(N, file=f)
    for row in q['Q']:
        print(len(row), *row, file=f)
    for state in initials:
        print(*state, file=f)
meta = {
    'state_meaning': ['merged', 'split_color0', 'split_color1'],
    'H3_extra_copies': [0] * 364,
    'target_split_fibers': 8946,
    'worker_count': 1,
    'CPU_seconds_per_start': 50,
    'fixed_search_seeds': [202610270401, 202610270402, 202610270403],
    'initials': [
        {'name': 'all_merged', 'split_fibers': 0},
        {'name': 'delta3_author_soft_constraints', 'split_fibers': sum(bool(x) for x in d3)},
        {'name': 'delta2_global_destruction', 'split_fibers': sum(bool(x) for x in broken),
         'reset_nodes': sum(reset), 'states_changed_from_author': sum(a != b for a, b in zip(w2, broken)),
         'original_split_removed': sum(bool(a) and not b for a, b in zip(w2, broken)),
         'original_merged_split': sum(not a and bool(b) for a, b in zip(w2, broken)),
         'all_retained_split_colors_redrawn': True},
    ],
}
(P / 'preset.json').write_text(json.dumps(meta, indent=2) + '\n')
print(json.dumps(meta['initials']))

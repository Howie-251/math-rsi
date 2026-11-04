"""Finite census of existing samples; never a full Q6 proof."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT/'remaining_samples_after_Z5.json').read_text(encoding='utf8'))
counts = Counter()
face_patterns = Counter()
records = []
for c in data['remaining']:
    m = c['matching']
    u, v = c['u'], c['v']
    holes = set(range(64))-{x for e in m for x in e}
    counts[f'holes_{len(holes)}'] += 1
    if len(holes) != 6:
        continue
    if v in holes:
        branch = 'S1_conditional_on_Z18' if (u ^ v).bit_count() == 1 else 'free_nonadjacent_open'
        cuts = []
    else:
        star_holes = (holes-{u}) | {v}
        cuts = []
        seen_patterns = set()
        for i in range(6):
            ah = {q for q in star_holes if ((q ^ v) >> i) & 1 == 0}
            seen_patterns.add((sum(q.bit_count() % 2 == 0 for q in ah),
                               sum(q.bit_count() % 2 == 1 for q in ah)))
            if len(ah) == 2 and all(q.bit_count() % 2 == v.bit_count() % 2 for q in ah):
                cuts.append(i)
        for pattern in seen_patterns:
            face_patterns[str(pattern)] += 1
        branch = 'S3_auxiliary_four_hole_circle_open' if cuts else 'no_S3_cut_open'
    counts[branch] += 1
    records.append(dict(u=u, v=v, holes=sorted(holes), branch=branch, cuts=cuts))
out = dict(scope='Old 381 sampled endpoint instances only; not full Q6',
           counts=dict(counts), six_hole_cases=records,
           covered_target_face_patterns=dict(sorted(face_patterns.items())),
           S1_depends_on_Z18_audit=True, full_p6_proved=False)
(ROOT/'six_hole_branch_census.json').write_text(json.dumps(out, indent=2), encoding='utf8')
print(json.dumps(out['counts'], indent=2))

"""Independent finite relational replay: source orbits -> all S5 labellings -> set-valued moments.
No discovery-module imports, DP, solver, or position certificates are evaluated.
"""
from pathlib import Path
from fractions import Fraction
from itertools import combinations, permutations
import json, time

HERE = Path(__file__).resolve().parent
SRC = HERE.parents[1] / 'unique6_no7'


def main():
    start = time.monotonic()
    src = json.loads((SRC / 'FIVE_DOMAIN.json').read_text())
    fixed = {r['id']: Fraction(r['bound']) for r in
             json.loads((SRC / 'FIVE_DP.json').read_text())['cases']}
    dual = {r['source_id']: Fraction(r['bound']) for r in
            json.loads((SRC / 'FIVE_JOINT.json').read_text())['results']}
    residual = [r for r in src['orbits']
                if dual.get(r['id'], fixed[r['id']]) >= 1]
    regenerated = set()
    summary = []
    for r in residual:
        counts = {frozenset(i for i in range(6) if int(mask) >> i & 1): n
                  for mask, n in r['counts'].items()}
        inc = {frozenset(S): sum(n for T, n in counts.items() if set(S) <= T)
               for k in range(1, 7) for S in combinations(range(6), k)}
        shape = sorted([b.bit_count() for b in r['center_partition']], reverse=True)
        if shape == [3, 2]:
            nonzero = [(sorted(S), n) for S, n in inc.items()
                       if 0 not in S and len(S) >= 3 and n]
            summary.append(dict(source_id=r['id'], partition=r['center_partition'],
                                pair_values=sorted({inc[frozenset(S)] for S in combinations(range(1, 6), 2)}),
                                nonzero_higher=nonzero))
        if any(n for S, n in inc.items() if 0 in S and len(S) >= 4):
            continue
        for p in permutations(range(1, 6)):
            moved = {frozenset(0 if i == 0 else p[i-1] for i in S): n
                     for S, n in inc.items()}
            regenerated.add(tuple(sorted((tuple(sorted(S)), n) for S, n in moved.items())))

    five_views = list(combinations(range(1, 7), 5))
    projected = []
    for Y in five_views:
        family = []
        for row in regenerated:
            inc = {frozenset(S): n for S, n in row}
            if any(inc[frozenset((i, j))] != (1 if (Y[i-1] == 1 or Y[j-1] == 1) else 2)
                   for i, j in combinations(range(1, 6), 2)):
                continue
            move = {0: 0} | {i: Y[i-1] for i in range(1, 6)}
            family.append({frozenset(move[i] for i in S): n for S, n in inc.items()})
        projected.append((Y, family))
    projected.sort(key=lambda r: len(r[1]))

    current = [{}]
    prefix_sizes = []
    for Y, family in projected:
        old_keys = set(current[0]) if current else set()
        common = sorted(old_keys.intersection(family[0]), key=lambda s: tuple(sorted(s))) if family else []
        idx = {}
        for row in family:
            idx.setdefault(tuple(row[S] for S in common), []).append(row)
        nxt = []
        for old in current:
            for row in idx.get(tuple(old[S] for S in common), []):
                assert all(old[S] == row[S] for S in old.keys() & row.keys())
                nxt.append(old | row)
        current = nxt
        prefix_sizes.append(len(current))
        if not current:
            break
    assert not current
    assert len(summary) == 1 and summary[0]['source_id'] == 12
    assert summary[0]['pair_values'] == [2]
    assert summary[0]['nonzero_higher'] == [([1, 2, 3], 1)]
    report = dict(PASS=True, source_residuals=len(residual),
                  source_three_plus_two=summary,
                  regenerated_matching_five_labels=len(regenerated),
                  view_order=[list(Y) for Y, _ in projected],
                  option_counts=[len(rows) for _, rows in projected],
                  prefix_join_sizes=prefix_sizes, common_full_inputs=0,
                  elapsed_seconds=time.monotonic()-start)
    (HERE / 'INDEPENDENT_POOL_REPLAY.json').write_text(json.dumps(report, indent=2)+'\n')
    print(report)


if __name__ == '__main__':
    main()

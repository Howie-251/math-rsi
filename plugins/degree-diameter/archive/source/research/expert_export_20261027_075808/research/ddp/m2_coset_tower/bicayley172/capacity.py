"""All equal-degree allocations for two regular orbits of D_86, degree7.

Only symbolic reduced walks; no field assignments, graph generation or BFS.
"""
import json
import time
from pathlib import Path

Q, D = 43, 7
OUT = Path(__file__).resolve().parent


def analyze(k, pair0, pair1, odd_cross):
    cross = D - k
    reflections = [k - 2 * pair0, k - 2 * pair1]
    variables = pair0 + pair1 + sum(reflections) + cross - 1
    alphabet = []
    slot = 0
    labels = []

    def basis():
        nonlocal slot
        c = tuple(int(i == slot) for i in range(variables))
        slot += 1
        return c

    for side, pairs in enumerate([pair0, pair1]):
        for index in range(pairs):
            c = basis()
            a = len(alphabet)
            alphabet += [(side, side, 0, c, a + 1),
                         (side, side, 0, tuple(-x % Q for x in c), a)]
            labels.append(f'layer{side}_pair{index}')
        for index in range(reflections[side]):
            a = len(alphabet)
            alphabet.append((side, side, 1, basis(), a))
            labels.append(f'layer{side}_reflection{index}')
    cross_phases = [0] * (cross - odd_cross) + [1] * odd_cross
    for index, phase in enumerate(cross_phases):
        c = (0,) * variables if index == 0 else basis()
        a = len(alphabet)
        inverse_c = tuple((1 if phase else -1) * x % Q for x in c)
        alphabet += [(0, 1, phase, c, a + 1), (1, 0, phase, inverse_c, a)]
        if index:
            labels.append(f'cross{index}')
    assert slot == variables
    allowed = [[i for i, a in enumerate(alphabet) if a[0] == s] for s in range(2)]
    assert list(map(len, allowed)) == [D, D]
    raw = [[[0] * 2 for _ in range(2)] for _ in range(2)]
    forms = [[[set() for _ in range(2)] for _ in range(2)] for _ in range(2)]
    for root in range(2):
        level = [(root, 0, (0,) * variables, -1)]
        raw[root][root][0] = 1
        forms[root][root][0].add((0,) * variables)
        for length in range(1, 4):
            following = []
            for side, phase, coeff, last in level:
                sign = -1 if phase else 1
                for a in allowed[side]:
                    if last >= 0 and a == alphabet[last][4]:
                        continue
                    _, target, ph, c, _ = alphabet[a]
                    endpoint = phase ^ ph
                    values = tuple((x + sign * y) % Q for x, y in zip(coeff, c))
                    following.append((target, endpoint, values, a))
                    raw[root][target][endpoint] += 1
                    forms[root][target][endpoint].add(values)
            assert len(following) == D * (D - 1) ** (length - 1)
            level = following
    counts = [[[len(f) for f in side] for side in root] for root in forms]
    cells = [(r, s, j) for r in range(2) for s in range(2) for j in range(2)]
    witness = min(cells, key=lambda t: (counts[t[0]][t[1]][t[2]], t))
    r, s, j = witness
    return dict(internal_degree=k, cross_degree=cross, internal_pair_counts=[pair0, pair1],
                internal_reflection_counts=reflections, cross_phases=cross_phases,
                variable_labels=labels, field_variable_slots=variables,
                root_raw_counts=raw, root_symbolic_form_counts=counts,
                raw_pass=all(raw[r][s][j] >= Q for r, s, j in cells),
                symbolic_pass=all(counts[r][s][j] >= Q for r, s, j in cells),
                minimum_symbolic_capacity=counts[r][s][j],
                minimum_cell=list(witness),
                minimum_cell_forms=[list(c) for c in sorted(forms[r][s][j])])


def main():
    start = time.process_time()
    rows = []
    for k in range(D):
        for p0 in range(k // 2 + 1):
            for p1 in range(k // 2 + 1):
                for odd_cross in range(D - k):
                    row = analyze(k, p0, p1, odd_cross)
                    row['id'] = len(rows)
                    rows.append(row)
    assert len(rows) == 110
    survivors = [r for r in rows if r['symbolic_pass']]
    result = dict(status='COMPLETE_SYMBOLIC_CAPACITY_ONLY',
                  group='F43 semidirect_{-1} C2', n=172, degree=7, target_diameter=3,
                  saved_public_threshold=170, patterns_checked=len(rows),
                  raw_survivors=sum(r['raw_pass'] for r in rows),
                  symbolic_survivors=len(survivors),
                  branch_counts=[dict(internal_degree=k,
                      patterns=sum(r['internal_degree'] == k for r in rows),
                      raw_survivors=sum(r['internal_degree'] == k and r['raw_pass'] for r in rows),
                      symbolic_survivors=sum(r['internal_degree'] == k and r['symbolic_pass'] for r in rows))
                      for k in range(D)],
                  CPU_seconds=time.process_time()-start,
                  field_assignments=0, graphs_generated=0, BFS_runs=0, rows=rows)
    (OUT/'CAPACITY_RESULTS.json').write_text(json.dumps(result, indent=2)+'\n')
    (OUT/'surviving_patterns.json').write_text(json.dumps(survivors, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'rows'}, indent=2))


if __name__ == '__main__':
    main()

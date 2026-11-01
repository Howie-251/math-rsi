"""Independent complete P4-missing/two-high P-trace domain and actual signed callers.
No imports from another implementation; standard library only.
"""
from pathlib import Path
from itertools import combinations, combinations_with_replacement
from collections import Counter
import json, time

HERE = Path(__file__).resolve().parent
PAIRS = list(combinations(range(7), 2))
F = ((0, 1), (1, 2), (2, 3))
INTERNAL = [127 ^ ((1 << i) | (1 << j)) for i, j in F]
CI = [sum(mask >> v & 1 for mask in INTERNAL) for v in range(7)]
HIGH = [sum(1 << i for i in S) for k in (3, 4) for S in combinations(range(4), k)]


def reverse(mask):
    return sum(1 << (3-i if i < 4 else i) for i in range(7) if mask >> i & 1)


def high_canonical(pair):
    direct = tuple(sorted(pair))
    flipped = tuple(sorted(map(reverse, pair)))
    return min(direct, flipped)


def gate(m4, m3, t, b):
    assert min(m4, m3, t, b) >= 0
    p = m4 + m3
    if m3 == 0:
        if m4 <= 7 and t <= 4 and b <= 35:
            return 'PURE7_T4_B35'
        if m4 <= 6 and t <= 6 and b <= 35:
            return 'PURE6_T6_B35'
        if m4 <= 5 and t <= 10 and b <= 32:
            return 'PURE5_T10_B32'
        if m4 == 8 and t <= 4 and b <= 17:
            return 'PURE8_T4_B17'
        if m4 == 8 and t <= 3 and b <= 20:
            return 'PURE8_T3_B20'
    # All these positives have size three or four, hence zero positive two-sets.
    if p <= 5 and t <= 2:
        return 'SMALL5_T2'
    if p <= 4 and t <= 8 and b <= 32:
        return 'SMALL4_T8_B32'
    if p <= 7 and m3 <= 1 and t <= 1 and b <= 20:
        return 'MIXED7_ONE3_T1_B20'
    if p <= 7 and m3 <= 1 and t == 0 and b <= 21:
        return 'MIXED7_ONE3_T0_B21'
    if m3 == 0 and m4 <= 10 and t == 0 and b <= 27:
        return 'PURE10_T0_B27_ROOT'
    return None


def signed_by_traces(hi, multiplicities, private, blue):
    """Independent color count of all indexed P traces, not degree-sum formulas."""
    counts = Counter()
    for mask, n in ([(m, 1) for m in INTERNAL] + [(m, 1) for m in hi]
                    + [((1 << i) | (1 << j), n) for (i, j), n in zip(PAIRS, multiplicities)]
                    + [(1 << i, n) for i, n in enumerate(private)]):
        if not n:
            continue
        if mask & blue == mask:
            counts[('positive', 5-mask.bit_count())] += n
        elif not mask & blue:
            counts[('negative', 5-mask.bit_count())] += n
    assert set(counts) <= {('positive', 4), ('positive', 3), ('negative', 3), ('negative', 4)}
    return (counts[('positive', 4)], counts[('positive', 3)],
            counts[('negative', 3)], counts[('negative', 4)])


def main():
    start = time.perf_counter()
    all_hi = list(combinations_with_replacement(HIGH, 2))
    representatives = sorted({high_canonical(pair) for pair in all_hi})
    assert len(all_hi) == 15 and len(representatives) == 9
    gate_ids = {}
    stats = []
    grand_total = grand_uncovered = grand_raw = 0
    for oid, hi in enumerate(representatives):
        hs = sum(m.bit_count() for m in hi)
        n2, n1 = 11-hs, 19+hs
        hv = [sum(mask >> v & 1 for mask in hi) for v in range(7)]
        cap = [8-CI[v]-hv[v] for v in range(7)]
        required = {eid for eid, (i, j) in enumerate(PAIRS)
                    if not any(mask >> i & 1 and mask >> j & 1 for mask in INTERNAL + list(hi))}
        blue_options = [(bid, i, j, (1 << i) | (1 << j))
                        for bid, (i, j) in enumerate(PAIRS)
                        if (i, j) not in F
                        and all(mask & ((1 << i) | (1 << j)) for mask in hi)]
        accepted = []
        misses = []
        uses = Counter()
        raw = valid = rejected_cap = rejected_cover = 0
        private_hist = Counter()
        for edges in combinations_with_replacement(range(21), n2):
            raw += 1
            mult = [0] * 21
            degree = [0] * 7
            for eid in edges:
                mult[eid] += 1
                i, j = PAIRS[eid]
                degree[i] += 1
                degree[j] += 1
            if any(d > c for d, c in zip(degree, cap)):
                rejected_cap += 1
                continue
            if any(mult[eid] == 0 for eid in required):
                rejected_cover += 1
                continue
            valid += 1
            private = [c-d for c, d in zip(cap, degree)]
            assert sum(private) == n1
            private_hist[tuple(sorted(private))] += 1
            witness = None
            for bid, i, j, blue in blue_options:
                m4 = private[i] + private[j]
                m3 = mult[bid]
                t = n2-degree[i]-degree[j]+m3
                b = n1-m4
                tag = gate(m4, m3, t, b)
                if tag is not None:
                    # Validate the actual P-trace coloring independently.
                    assert signed_by_traces(hi, mult, private, blue) == (m4, m3, t, b)
                    if tag not in gate_ids:
                        gate_ids[tag] = len(gate_ids)
                    witness = [list(edges), bid, gate_ids[tag]]
                    uses[tag] += 1
                    break
            if witness is None:
                misses.append(list(edges))
            else:
                accepted.append(witness)
        filename = f'ORBIT_{oid:02d}_WITNESSES.json'
        (HERE/filename).write_text(json.dumps(accepted, separators=(',', ':'))+'\n')
        if misses:
            (HERE/f'ORBIT_{oid:02d}_UNCOVERED.json').write_text(json.dumps(misses, separators=(',', ':'))+'\n')
        st = dict(id=oid, high_masks=list(hi), high_sets=[[i for i in range(4) if mask >> i & 1] for mask in hi],
                  n2=n2, n1=n1, private_capacity=cap,
                  required_J_pairs=[list(PAIRS[eid]) for eid in sorted(required)],
                  raw_J_multisets=raw, rejected_cap=rejected_cap, rejected_paircover=rejected_cover,
                  necessary_labelled_J=valid, covered=len(accepted), uncovered=len(misses),
                  gate_uses=dict(uses), witnesses_file=filename)
        stats.append(st)
        grand_total += valid
        grand_uncovered += len(misses)
        grand_raw += raw
        print(oid, hi, 'raw', raw, 'necessary', valid, 'uncovered', len(misses), flush=True)
    report = dict(scope=__doc__, complete=True, missing_pairs=[list(e) for e in F],
                  internal_masks=INTERNAL, internal_degrees=CI, edge_order=[list(e) for e in PAIRS],
                  raw_unordered_high_pairs=15, reversal_high_orbits=9,
                  raw_J_multisets=grand_raw, necessary_labelled_J=grand_total,
                  uncovered=grand_uncovered, gate_ids=gate_ids, orbits=stats,
                  witness_encoding='[nondecreasing J edge-order indices, blue-pair edge-order index, gate id]',
                  elapsed_seconds=time.perf_counter()-start)
    (HERE/'SUMMARY.json').write_text(json.dumps(report, indent=2)+'\n')
    print('TOTAL', grand_total, 'UNCOVERED', grand_uncovered, 'SECONDS', report['elapsed_seconds'])


if __name__ == '__main__':
    main()

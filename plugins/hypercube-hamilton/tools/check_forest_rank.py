#!/usr/bin/env python3
"""Check an A10-type cube forest rank gate; no producer or fixed manifest required."""
import argparse
import json
from pathlib import Path
import time

if not __debug__:
    raise RuntimeError("Run without Python -O: mathematical checks require assertions")


class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def root(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def join(self, x, y):
        a, b = self.root(x), self.root(y)
        if a == b:
            return False
        self.p[a] = b
        return True


def records(path, width):
    raw = path.read_bytes()
    if not raw or len(raw) % width:
        raise ValueError(f'{path}: expected nonempty records of {width} bytes')
    return [list(zip(raw[i:i + width:2], raw[i + 1:i + width:2]))
            for i in range(0, len(raw), width)]


def check(dim, root, holes, forests, columns):
    start = time.perf_counter()
    n = 1 << dim
    # This tool checks precisely the unsigned-byte A10-type encoding.
    assert 2 <= dim <= 8 and root in holes and holes <= set(range(n))
    k = set(range(n)) - holes
    t = len(k)
    assert t >= 4 and t % 2 == 0, 'Requires an even endpoint set of at least four vertices'
    forest_width = 2 * (n - 1 - t // 2)
    ss = records(forests, forest_width)
    xs = records(columns, t)
    ps = []
    for s in ss:
        assert len(set(s)) == len(s), 'Repeated forest edge'
        d, deg = DSU(n), [0] * n
        for a, b in s:
            assert 0 <= a < b < n and root not in (a, b)
            assert (a ^ b).bit_count() == 1, 'Forest edge is not short'
            assert d.join(a, b), 'Cycle in forest'
            deg[a] += 1
            deg[b] += 1
        assert deg[root] == 0
        assert all(deg[v] == (1 if v in k else 2) for v in range(n) if v != root)
        groups = {}
        for v in k:
            groups.setdefault(d.root(v), []).append(v)
        assert len(groups) == t // 2 and all(len(v) == 2 for v in groups.values())
        ps.append([tuple(sorted(v)) for v in groups.values()])
    for x in xs:
        assert all(0 <= a < b < n for a, b in x)
        assert len({v for e in x for v in e}) == t
        assert {v for e in x for v in e} == k, 'Column must match every endpoint exactly once'
    rows, ones = [], 0
    for p in ps:
        bits = 0
        for j, x in enumerate(xs):
            d = DSU(n)
            for a, b in p:
                d.join(a, b)
            for a, b in x:
                d.join(a, b)
            if len({d.root(v) for v in k}) == 1:
                assert not set(p).intersection(x), 'A common edge cannot occur in a connected union for t>=4'
                bits |= 1 << j
                ones += 1
        rows.append(bits)
    work, rank = rows.copy(), 0
    for col in range(len(xs)):
        pivot = next((r for r in range(rank, len(work)) if work[r] >> col & 1), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        for r in range(rank + 1, len(work)):
            if work[r] >> col & 1:
                work[r] ^= work[rank]
        rank += 1
    required = 1 << (t // 2 - 1)
    assert rank <= required, 'Computed rank conflicts with imported CKN bound'
    return dict(status='PASS', dim=dim, root=root, holes=sorted(holes), endpoints=sorted(k),
                forest_record_bytes=forest_width, column_record_bytes=t,
                legal_forests=len(ss), valid_matching_columns=len(xs),
                matrix_bits_recomputed_DSU=len(ss) * len(xs), matrix_ones=ones,
                GF2_rank_low_column_gauss=rank, imported_CKN_rank_upper_bound=required,
                universal_rank_gate_met=rank == required,
                complete_forest_pool_exhaustiveness_required=False,
                scope='A10-type simple cube forests on V minus root, degree1 at K and degree2 at holes minus root; all complete-graph matchings on K',
                seconds=time.perf_counter() - start)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dim', type=int, required=True)
    ap.add_argument('--root', type=int, required=True)
    ap.add_argument('--holes', type=int, nargs='+', required=True)
    ap.add_argument('--forests', type=Path, required=True)
    ap.add_argument('--columns', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    result = check(a.dim, a.root, set(a.holes), a.forests, a.columns)
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

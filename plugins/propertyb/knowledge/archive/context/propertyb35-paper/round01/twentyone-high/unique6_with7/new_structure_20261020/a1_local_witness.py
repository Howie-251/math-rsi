"""One explicit necessary local inventory for the final a1 role; no search or promotion table.
Not an actual 35-edge H and not a noncolorability claim.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction
import json

HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]


def main():
    old = json.loads((BASE/'unique6_no7/FIVE_DOMAIN.json').read_text())['orbits'][12]
    assert old['center_partition'] == [7, 24]
    fixed5 = json.loads((BASE/'unique6_no7/FIVE_DP.json').read_text())['cases'][12]
    joint5 = {r['source_id']: Fraction(r['bound']) for r in
              json.loads((BASE/'unique6_no7/FIVE_JOINT.json').read_text())['results']}
    core_bound = joint5.get(12, Fraction(fixed5['bound']))
    assert core_bound >= 1
    # Old order x,u1,...,u5 -> new order x,p,u1,...,u5.
    def move(m):
        return (m & 1) | ((m >> 1) << 2)
    ns = {move(int(m)): n for m, n in old['counts'].items()}
    def insert_p(t, multiplicity):
        assert ns.get(t, 0) >= multiplicity
        ns[t] -= multiplicity
        ns[t | 2] = ns.get(t | 2, 0) + multiplicity
    insert_p(1, 1)                    # one true x edge also contains p
    insert_p((1 << 2) | (1 << 5), 1) # p,u1,u4
    insert_p((1 << 3) | (1 << 6), 1) # p,u2,u5
    insert_p(1 << 4, 1)             # p,u3
    insert_p(0, 3)                  # three p edges contain no selected U
    ns = {m: n for m, n in ns.items() if n}
    assert sum(ns.values()) == 35 and min(ns.values()) >= 0
    inc = lambda S: sum(n for m, n in ns.items() if all(m >> i & 1 for i in S))
    assert [inc((i,)) for i in range(7)] == [6, 7, 8, 8, 8, 8, 8]
    assert all(inc((0, i)) == 1 for i in range(1, 7))
    assert all(inc((1, i)) == 1 for i in range(2, 7))
    assert all(inc((i, j)) == 2 for i, j in combinations(range(2, 7), 2))

    dom = json.loads((BASE/'unique6_with7/a1/FOUR_DOMAIN.json').read_text())
    dp = json.loads((BASE/'unique6_with7/a1/FOUR_DP.json').read_text())['cases']
    lookup = {tuple(r['counts'].get(str(m), 0) for m in range(16)): r['orbit']
              for r in dom['labelled']}
    views = []
    for i, j in combinations(range(2, 7), 2):
        order = (0, 1, i, j)
        counts = [0] * 16
        for m, n in ns.items():
            mask = sum(1 << k for k, v in enumerate(order) if m >> v & 1)
            counts[mask] += n
        oid = lookup[tuple(counts)]
        bound = Fraction(dp[oid]['bound'])
        assert bound >= 1
        views.append(dict(unit8_pair=[i-1, j-1], orbit=oid, existing_bound=str(bound)))

    star = [
        ['x','u1','u2','u3','B1'],
        ['x','u4','u5','B2','v1'],
        ['x','p','B3','v2','v3'],
        ['x','B1','B2','v4','v5'],
        ['x','B3','B4','v6','v7'],
        ['x','B4','v8','v9','v10'],
    ]
    points = set().union(*map(set, star))
    assert len(points) == 21 and all(len(e) == 5 for e in star)
    assert all(sum(b in e for e in star) == 2 for b in ('B1','B2','B3','B4'))
    assert all(sum(v in e for e in star) == 1 for v in points - {'x','B1','B2','B3','B4'})
    lock = {name: i for i, name in enumerate(['x','p','u1','u2','u3','u4','u5'])}
    projected = {}
    for e in star:
        mask = sum(1 << lock[v] for v in e if v in lock)
        projected[mask] = projected.get(mask, 0) + 1
    assert projected == {m: n for m, n in ns.items() if m & 1}
    result = dict(scope=__doc__, locked_order=list(lock), counts=ns,
                  exact_six_center_edges=star, matched_old_unit8_core=12,
                  old_unit8_core_bound=str(core_bound),
                  old_four_views=views, every_old_four_view_non_strict=True,
                  status='necessary local inventory only; complete H not constructed',
                  unrepresented_vertices_target_degrees={'B1..B4':8,'v1..v10':9},
                  unrepresented_degree_total=122)
    (HERE/'A1_LOCAL_WITNESS.json').write_text(json.dumps(result, indent=2)+'\n')
    print(dict(selected_degrees=[6,7,8,8,8,8,8], views=len(views),
               all_old_four_non_strict=True, orbit_ids=sorted({r['orbit'] for r in views}),
               exact_center_star=True, actual_H_constructed=False))


if __name__ == '__main__':
    main()

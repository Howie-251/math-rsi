"""Exact 65,535-subset certificate for A4 degree completion, not connectivity.

No graph library, numerical solver, or imported mathematical theorem is used
by this finite geometry check. See A4_SPANNING_FACTOR.md for the reduction.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main():
    even = [x for x in range(32) if x.bit_count() % 2 == 0]
    odd = [x for x in range(32) if x.bit_count() % 2 == 1]
    assert even[0] == 0 and len(even) == len(odd) == 16
    neighbor_masks = [sum(1 << i for i, x in enumerate(even)
                          if (x ^ y).bit_count() == 1) for y in odd]
    minimum = [None] * 17
    witnesses = [None] * 17
    checked = 0
    for subset in range(1, 1 << 16):
        n = 0
        leaf_parents = 0
        for neighbors in neighbor_masks:
            intersection = neighbors & subset
            if intersection:
                n += 1
                if intersection & (intersection - 1) == 0:
                    leaf_parents |= intersection
        r = (leaf_parents & ~1).bit_count()  # a=0 cannot meet F
        k = subset.bit_count()
        slack = n - 1 + max(0, n - 14) - r - k - int(bool(subset & 1))
        assert slack >= 0, (subset, n, r, slack)
        if minimum[k] is None or slack < minimum[k]:
            minimum[k] = slack
            witnesses[k] = {'S': [even[i] for i in range(16) if subset >> i & 1],
                            'neighbor_count': n, 'leaf_parent_count_except_a': r,
                            'slack': slack}
        checked += 1
    result = {'status': 'PASS', 'scope': 'finite geometry lemma GF5 only',
              'normalized_minority_hole': 0, 'nonempty_subsets_checked': checked,
              'minimum_slack_by_subset_size': minimum,
              'attaining_subsets': witnesses,
              'empty_subset': 'Hall inequality is 0 <= 0, checked analytically',
              'connected_cycle_proved': False, 'full_p6_proved': False,
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    target = ROOT / 'a4_factor_geometry_verification.json'
    target.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'nonempty_subsets_checked',
                                           'minimum_slack_by_subset_size')}))


if __name__ == '__main__':
    main()

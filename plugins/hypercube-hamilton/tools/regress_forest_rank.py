#!/usr/bin/env python3
"""Small contract regressions for the existing forest-rank consumer."""
import argparse
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from check_forest_rank import check


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    evidence = Path(__file__).resolve().parents[1] / 'evidence'
    outcomes = {}

    # Replay the old positional Python/root interface on its original Q3 data.
    old = evidence / 'small-geometry'
    root = check(3, 7, {0, 1, 2, 7}, old / 'forests.bin', old / 'columns.bin')
    assert root['GF2_rank_low_column_gauss'] == 2 and root['universal_rank_gate_met']
    assert root['omitted'] == [7] and root['covered_vertices'] == 7
    outcomes['legacy_root'] = root

    with TemporaryDirectory() as tmp:
        scratch = Path(tmp)

        def run(forests, columns, *, holes={4, 5, 6, 7}, omitted={4, 5, 6, 7}, root=None, dim=3):
            f, c = scratch / 'forests.bin', scratch / 'columns.bin'
            f.write_bytes(bytes(forests))
            c.write_bytes(bytes(columns))
            return check(dim, root, holes, f, c, omitted=omitted)

        # Two short perfect matchings on one square; all three complete-graph
        # columns. No producer, saved matrix or imported local rank field.
        forests = [0, 1, 2, 3, 0, 2, 1, 3]
        columns = [0, 1, 2, 3, 0, 2, 1, 3, 0, 3, 1, 2]
        multi = run(forests, columns)
        assert multi['universal_rank_gate_met'] and multi['GF2_rank_low_column_gauss'] == 2
        assert multi['covered_vertices'] == 4 and multi['forest_record_bytes'] == 4
        outcomes['multi_omitted_full_gate'] = multi

        # A valid marked three-omission geometry whose selected row pool lacks
        # full rank. Legal data is not itself a universal-certificate PASS.
        partial = run([2, 3, 2, 6, 4, 5],
                      [3, 4, 5, 6, 3, 5, 4, 6, 3, 6, 4, 5],
                      holes={0, 1, 2, 7}, omitted={0, 1, 7})
        assert partial['GF2_rank_low_column_gauss'] == 1 and not partial['universal_rank_gate_met']
        assert partial['covered_vertices'] == 5
        outcomes['legal_rank_deficient'] = partial

        bad = {
            'omitted_outside_holes': lambda: run(forests, columns, omitted={0, 4, 5, 6, 7}),
            'both_root_and_omitted': lambda: run(forests, columns, root=4),
            'forest_touches_omitted': lambda: run([0, 4, 2, 3], columns),
            'repeated_forest_edge': lambda: run([0, 1, 0, 1], columns),
            'long_forest_edge': lambda: run([0, 3, 1, 2], columns),
            'incomplete_component_degrees': lambda: run([0, 1, 0, 2], columns),
            # This all-hole cycle has the correct degree2, separate from two
            # legal endpoint paths; counting only endpoint components misses it.
            'hidden_all_hole_cycle': lambda: run(
                [0, 1, 1, 3, 2, 3, 0, 2, 4, 5, 6, 7], [4, 5, 6, 7],
                holes=set(range(4)) | set(range(8, 16)), omitted=set(range(8, 16)), dim=4),
            'column_reuses_endpoint': lambda: run(forests, [0, 1, 0, 3]),
            'column_wrong_endpoint_domain': lambda: run(forests, [0, 1, 2, 4]),
            'truncated_forest_record': lambda: run([0, 1, 2], columns),
        }
        for name, action in bad.items():
            try:
                action()
            except (AssertionError, ValueError):
                outcomes[name] = 'REJECTED'
            else:
                raise AssertionError(f'{name}: invalid certificate was accepted')

    result = dict(status='PASS', scope='contract regressions, not a new cube theorem', checks=outcomes)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()

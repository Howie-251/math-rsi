"""Unexecuted grid-normalization delta, reusing the full61 encoder unchanged.

Only the proved complete U-Z and Ta-Z adjacency blocks are additionally fixed.
All outputs and subsequent SAT decoding belong to this new directory.
"""
import argparse
import importlib.util
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
BASE = HERE.parent / 'triple_full61_run'
ROOT = HERE.parents[3]
GRID_PROOF = 'proofs/dd82/n61/CONNECTED_TRIPLE_GRID_NORMALIZATION.md'

# Preserve even the old directory's bytecode artifacts when importing its source.
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('triple61_grid_base_encode', BASE / 'encode.py')
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)
base.HERE = HERE
base.SCOPE = ('Full61 triple-defect template with the proved U-by-Ta coordinates on Z; '
              'every original connected triple target has these labels; '
              'no C/sigma choice, B simplicity or graph automorphism assumption')
original_fixed_adjacencies = base.fixed_adjacencies


def grid_fixed_adjacencies():
    fixed, reasons = original_fixed_adjacencies()
    previous_count = len(fixed)

    def fix(u, v, value, reason):
        uv = base.pair(u, v)
        assert uv not in fixed or fixed[uv] == value, (uv, reasons.get(uv), reason)
        fixed[uv] = value
        reasons.setdefault(uv, reason)

    # Grid proof section 1: F is a U transversal. Choose U labels from F,
    # then simultaneously choose matched V labels, retaining A[U,V]=I.
    for j, u in enumerate(base.U):
        for k, z in enumerate(base.F):
            fix(u, z, int(j == k), 'grid proof: F-U identity from available U/V labels')
        for i in range(5):
            for k in range(4):
                fix(u, base.Z[4 + 4*i + k], int(j == k),
                    'grid proof: unique U coordinate of each non-F Z point')

    # Grid proof sections 2-3: all twenty (Ta,U) cells have size exactly one.
    # Ta labels and the three normalized Ta matchings remain unchanged.
    for i, t in enumerate(base.TA):
        for z in base.F:
            fix(t, z, 0, 'inherited exact layer degree: F has no Ta neighbor')
        for h in range(5):
            for j in range(4):
                fix(t, base.Z[4 + 4*h + j], int(i == h),
                    'grid proof: unique Ta coordinate of each non-F Z point')
    assert len(fixed) - previous_count == 216  # Complete 4x24 and 5x24 blocks.
    return fixed, reasons


base.fixed_adjacencies = grid_fixed_adjacencies


def prepare():
    base.prepare()
    path = HERE / 'encoding.json'
    record = json.loads(path.read_text())
    record['mathematical_dependencies'].append(GRID_PROOF)
    # The inherited value describes the old source's delivery, not the
    # current review of this new input. Actual receipts are root-managed.
    record.pop('source_review_status', None)
    record.update(
        source_dependencies=[str((BASE / 'encode.py').relative_to(ROOT)),
                             str(Path(__file__).resolve().relative_to(ROOT)),
                             str(base.HELPER.relative_to(ROOT))],
        grid_normalization=dict(additional_fixed_pairs=216,
            fixed_blocks=['all U-Z entries', 'all Ta-Z entries'],
            non_F_coordinate='Z[4+4*i+j] is adjacent to Ta[i] and U[j]',
            F_coordinate='F[j] is adjacent to U[j]',
            V_Z_fixed_by_delta=False, C_sigma_selected=False,
            both_port_cases_retained=True),
        source_review_delivery_snapshot='Wrapper source prepared for independent delta review; delivery snapshot only, not a current execution/review verdict',
        current_review_receipts='Recorded separately by the root; not inferred from source-generation metadata')
    base.save(path, record)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('prepare', 'decode'))
    parser.add_argument('--log', type=Path, default=HERE / 'solver.log')
    args = parser.parse_args()
    prepare() if args.action == 'prepare' else base.decode(args.log)

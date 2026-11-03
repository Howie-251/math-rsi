"""Bind the r02 contracts to the unchanged 24-leaf symbolic cover."""
from __future__ import annotations
import json
from pathlib import Path
from sat60.round13.contract import ROOTS, REPO, load_contract as load_r01

VERSION = "n60_round13_manual12_r02_20260928_v1"
REVISION = "r02_20260928"
ROUND_NAME = "N60_ROUND13_PRO_TO_CODEX_manual-v1.2-feedback-loop_" + REVISION
DEFAULT_HANDOFF = REPO.parent / "formal_loop" / ROUND_NAME
ORIGINAL_PACKAGE = REPO.parent / (ROUND_NAME + ".zip")
QUESTION = (
    "Decide the full remaining Q038/Q040 ranges after adding accepted R13F "
    "shared-tail, exact row-profile, packing and scoped auxiliary-endpoint conditions. "
    "Keep all twenty old open leaves and their four complementary cubes; inherit "
    "four theory-covered leaves. No relaxed model, new enumeration or performance comparison."
)
MODULES = {
    "R13F-32-SHARED-ONLY": "all distinct u,v,x: B_uv=3 and B_ux=2 imply B_vx=1",
    "R13F-32-TAIL2111": "row32(u) and B_ux=2 imply row2111(x); n2111>=3*n32; no a=0/1 pruning",
    "R13F-32-INDEPENDENT": "B[L,L]=0; n32<=n311 and n32<=2*n221+n2111",
    "R13F-32-EIGHT-PACKING": "n32<=7; n2111+n11111>=4*n32; Q038 only: D<=3, E<=4",
    "R13F-32-MIXED": "PARTIAL: row32 and its actual B3 partner have t=0; partner is row311",
    "R13F-221-TRANSLATION": "PARTIAL: row221 has t=0 and no A edge to a positive B partner; no path/cycle circuit",
    "R13F-038-32-SIMPLE-ENDS": "Q038 only: an E-row32 identity cannot touch an endpoint of any Lambda-weight-2 pair",
}
COMMON_IDS = tuple(k for k in MODULES if k != "R13F-038-32-SIMPLE-ENDS")
Q038_IDS = ("R13F-038-32-SIMPLE-ENDS",)


def normalized_coverage(cover):
    # Preserve the r02 JSON separately; adapt names only for the existing reporter.
    return [{**r, "original_branch_id": r["legacy_branch_id"],
             "current_mathematical_status": r["status"]} for r in cover["records"]]


def load_contract(handoff=DEFAULT_HANDOFF, legacy_bundle=None):
    handoff = Path(handoff).resolve()
    constraints = json.loads((handoff / "CONSTRAINTS.json").read_text())
    cover = json.loads((handoff / "COVERAGE_DELTA.json").read_text())
    if constraints["package_revision"] != REVISION or cover["package_revision"] != REVISION:
        raise ValueError("expected the specified Round13 r02 handoff")
    ids = {r["constraint_id"] for r in constraints["constraints"]}
    if not set(MODULES) <= ids:
        raise ValueError("an implemented R13F contract is absent")
    upstream = handoff / "dependencies/codex_feedback/dependencies/upstream_round13"
    jobs, leaves, families, old_cover, _ = load_r01(upstream, legacy_bundle)
    current = {r["original_branch_id"]: r for r in normalized_coverage(cover)}
    old = {r["original_branch_id"]: r for r in old_cover["records"]}
    if set(current) != set(old):
        raise ValueError("r02 and inherited r01 identify different original leaves")
    for name, row in current.items():
        for field in ("root_id", "current_mathematical_status", "closing_theorem_ids", "original_observed_result"):
            if row[field] != old[name][field]:
                raise ValueError(f"unhandled coverage change: {name} / {field}")
    return jobs, leaves, families, cover, constraints

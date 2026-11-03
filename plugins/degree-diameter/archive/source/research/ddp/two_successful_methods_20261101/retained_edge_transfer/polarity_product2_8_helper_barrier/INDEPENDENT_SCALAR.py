#!/usr/bin/env python3
"""One scalar check of the paper bound; no graph or geometry is constructed."""
import json
from pathlib import Path
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
started = time.process_time()
rows = []
for r in range(5):
    delta = 27 + r
    values = [(2 * (delta-d) * (r+3+d), d) for d in range(delta+1)]
    maximum = max(v for v, _ in values)
    maximizers = [d for v, d in values if v == maximum]
    identity = all(v == 2*((r+15)**2-(d-12)**2) for v, d in values)
    assert identity and maximum == 2*(r+15)**2 and maximizers == [12]
    rows.append({
        "r": r, "cap": delta, "hard_targets": 650,
        "integer_quadratic_maximum": maximum,
        "maximizing_helper_degree": maximizers,
        "hard_targets_minus_bound": 650-maximum,
        "excludes_nonempty_helper_batch": 650 > maximum,
    })
assert [row["integer_quadratic_maximum"] for row in rows] == [450,512,578,648,722]
assert [row["excludes_nonempty_helper_batch"] for row in rows] == [True]*4+[False]
cpu = time.process_time()-started
base = Path(__file__).resolve().parent
result = {
    "status": "SUPPORTED_PAPER_ROUTE_BARRIER_SCALAR_PASS",
    "prediction_file": "PREDICTION_AND_PROOF.md",
    "assumptions": "Genuine looped GQ polarity quotients A(q2), B(q8), the stated absolute sets, all original source and uniform-r full-N clone edges retained, finite simple augmentation at cap 27+r.",
    "source_is_published_abstract_interface_not_generated_here": True,
    "source_order": 8775, "center_count": 325,
    "source_center_degree": 26, "source_noncenter_count": 8450,
    "source_noncenter_degree": 27, "hard_target_count": 650,
    "mandatory_direct_X_bound": 2, "mandatory_radius_two_X_bound": 6,
    "per_helper_necessary_inequality": "650 <= (6+2*r)*p_h + 2*sum_{g~h} p_g",
    "summed_necessary_inequality": "650 <= 2*(r+15)^2",
    "rows": rows,
    "excluded_r": [0,1,2,3], "excluded_caps": [27,28,29,30],
    "first_not_excluded": {"r": 4, "cap": 31, "not_an_existence_result": True},
    "paper_attack": {
        "source_loop_removal": "covered: only absolute-product vertices lose a loop; deleting loops cannot add routes",
        "repeated_clones": "covered by replacing initial clone with its source center for an old-X suffix",
        "arbitrary_free_peer_edges": "covered: first pin uses one of r+1 free slots; at most r peers remain",
        "multiple_helpers_and_repeated_class_ownership": "covered by actual pin counts and undirected double counting",
        "both_endpoint_degree_cost": "each helper-free and free-free edge consumes its actual endpoint slots; unused global consistency can only strengthen the bound",
        "exhaustive_helper_path_types": "first step to F or H; a saturated old noncenter cannot be adjacent to any new helper",
    },
    "complementary_agent": {"name": "/root/f9_56862_independent", "scope": "paper-only independent 2/6 factor-route check", "result": "SUPPORTED", "tools_or_computations": 0},
    "scalar_CPU_seconds": cpu,
    "CPU_measurement_note": "A zero reading means below timing resolution for the tiny scalar loop; preparation/execution is not asserted to have zero cost.",
    "scalar_CPU_limit_seconds": 5,
    "operations": {"scalar_checks": 1, "graph_generation": 0, "graph_parsing": 0,
        "field_or_geometry_computation": 0, "BFS": 0, "Lean": 0,
        "solver": 0, "web_queries": 0, "paid_reviews": 0},
    "scope": "Only the fixed published source, complete uniform copying, mandatory-edge-preserving augmentation, and existence of a nonempty helper batch. No global N(Delta,3), priority, construction or kernel claim.",
}
(base/"INDEPENDENT_RESULT.json").write_text(json.dumps(result, indent=2)+"\n")
terminal = {
    "state": "COMPLETE_SUPPORTED_FIXED_FAMILY_BARRIER",
    "active_processes": False, "further_run_authorized_or_started": False,
    "new_graphs": 0, "new_concrete_Lean_targets": 0,
    "excluded_caps": [27,28,29,30], "cap31": "OPEN_TO_THIS_BOUND_NO_RUN",
    "scalar_CPU_seconds": cpu,
    "CPU_measurement_note": "A zero reading means below timing resolution, not zero actual cost.",
    "root_counts_Wiki_frozen_artifacts_modified": False,
    "existing_three_graph_review_scope_used_as_evidence": False,
}
(base/"INDEPENDENT_TERMINAL.json").write_text(json.dumps(terminal, indent=2)+"\n")
print(json.dumps({"status": result["status"], "rows": rows, "CPU_seconds": cpu}))

"""Selection scalars only: no graphs and no existence claim for an upper bound."""
import json
import time
from pathlib import Path

start = time.process_time()
q = 7
s, t = q - 1, q + 1
source_n = (s + 1) * (t + 1) * (s * t + 1) ** 2
source_degree = (s + 1) * (t + 1)
original_partial_upper = q * q - q + 1
derived_partial_upper = original_partial_upper - 1
spread_size = s * t + 1
centers_upper = derived_partial_upper * spread_size
rows = []
for degree in range(73, 81):
    candidate = 160050 + 1650 * (degree - 64)
    upper = source_n + 49 + (degree - source_degree) * centers_upper
    rows.append(dict(degree=degree, conditional_P33_n=candidate,
                     specified_Payne_rule_upper=upper, P33_minus_upper=candidate-upper))

result = dict(
    date_UTC="2026-11-01",
    status="NO_FULL_OVOID_FOR_STANDARD_PAYNE_W3_7_DERIVATION",
    source_scope="D = W(3,7)^P; no classification of all abstract GQ(6,8)",
    derived_full_ovoid_49_exists=False,
    derived_spread_49_exists=True,
    full_ovoid_and_spread_simultaneous=False,
    original_W_partial_ovoid_upper=original_partial_upper,
    derived_partial_ovoid_upper=derived_partial_upper,
    derived_full_ovoid_required=s*t+1,
    derived_points=q**3,
    source_n=source_n, source_degree=source_degree,
    hypothetical_full_product_centers=49*49,
    hypothetical_full_product_is_public_lower_bound=False,
    specified_partial_product_centers_upper=centers_upper,
    specified_rule_upper_formula="151312 + 2058*(Delta-63)",
    specified_rule_upper_is_constructed_lower_bound=False,
    partial_ovoid_42_existence_asserted=False,
    conditional_P33_formula="160050 + 1650*(Delta-64)",
    continuation_rows=rows,
    P33_beats_specified_Payne_upper_through_80=all(r["P33_minus_upper"]>0 for r in rows),
    new_k_production_authorized=False,
    degrees65_to72_recomputed=False,
    new_primary_query_batches=1, new_primary_queries=3,
    primary_sources=[
        dict(authors="Feng, Li", year=2021, section="2.1",
             URL="https://arxiv.org/html/1908.10659v2#S2.SS1",
             used_for="actual Payne point and line definition"),
        dict(authors="Ceria, De Beule, Pavese, Smaldore", year=2022,
             section="1 / Table1 / reference13",
             URL="https://arxiv.org/html/2203.04553#S1",
             used_for="published restatement of Tallini odd-q W partial-ovoid upper bound",
             Tallini_original_fulltext_read=False),
        dict(author="Delorme", year=1985, section="8(a), print p298",
             URL="https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf",
             used_for="original symplectic spread q^2+1")],
    new_deductions=["derived partial ovoid plus derivation point is original partial ovoid",
                    "derived partial ovoid at most42; full49 impossible",
                    "delete original spreadline through P to obtain derived spread49",
                    "specified rectangular copy rule cannot dominate P33 through80"],
    unresolved_scope=["arbitrary nonrectangular packing or other induced/nested augmentation",
                      "classification of all abstract GQ(6,8) or unknown nonclassical parents",
                      "all other public degree73..80 constructions",
                      "no global record or priority claim"],
    CPU_budget_seconds=5,
    new_graphs=0, large_graph_reads=0, BFS_runs=0, solver_runs=0,
    Lean_runs=0, external_reviews=0, installs=0, hashes=0,
    all_local_processes_terminal=True)
result["scalar_CPU_seconds"] = time.process_time() - start
out = Path(__file__).with_name("PAYNE68_FULL_OVOID_SPREAD_CONTINUATION_GATE_20261101.json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({"status": result["status"], "CPU": result["scalar_CPU_seconds"],
                  "rows": rows, "output": str(out)}, indent=2))

"""Saved-factor categorical products: numeric screen plus synchronized-walk witnesses."""

from itertools import combinations_with_replacement
import json
import math
from pathlib import Path
import resource
import time


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SNAPSHOT = ROOT / "context/DD_PORTFOLIO_START_20261026/registry/cases.json"
ORDERS = {2: {3: 7, 4: 9, 5: 11}, 3: {3: 20, 4: 38, 5: 70},
          4: {3: 41, 4: 104, 5: 364}, 5: {3: 72, 4: 252, 5: 650},
          6: {3: 120, 4: 441, 5: 1518}}


def moore(degree, diameter):
    return 1 + degree * sum((degree - 1) ** j for j in range(diameter))


def witness(factors):
    # All numerical exceeders below have D3 factors. Projecting any product
    # walk to the two chosen coordinates preserves its length.
    assert all(f["diameter"] == 3 for f in factors)
    triangle_free = next((i for i, f in enumerate(factors) if f["degree"] == 2), None)
    if triangle_free is not None:
        reason = "C7 has no triangle, hence no closed3walk at any vertex."
    else:
        triangle_free = next(i for i, f in enumerate(factors) if f["degree"] == 3)
        assert factors[triangle_free]["order"] == 20
        reason = "A subcubic graph with a triangle has at most1+3+4+8=16 vertices within3 of a triangle vertex; order20 and diameter3 force trianglefree."
    far_factor = next(i for i in range(len(factors)) if i != triangle_free)
    far = factors[far_factor]
    assert far["order"] > moore(far["degree"], 2)
    return {"triangle_free_factor_index": triangle_free, "triangle_free_reason": reason,
            "distance3_factor_index": far_factor,
            "distance3_existence_reason": f"order{far['order']}>Moore({far['degree']},2)={moore(far['degree'], 2)}, while source diameter3",
            "endpoint_choice": "Same vertex in trianglefree coordinate; a distance3 pair in the other coordinate; any extra coordinates fixed.",
            "why_no_product_walk_le3": "The distance3 coordinate forces length3; the fixed trianglefree coordinate has no closed3walk.",
            "conclusion": "This product cannot have diameter at most3; disconnectedness would also fail the target."}


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
    started = time.process_time()
    cases = json.loads(SNAPSHOT.read_text())["cases"]
    baseline = {(c["degree_cap"], c["diameter_cap"]): c["baseline_order"] for c in cases}
    factors = [{"degree": d, "diameter": r, "order": ORDERS[d][r],
                "kind": "cycleC" + str(2 * r + 1) if d == 2 else "saved_maintainer_source"}
               for d in range(2, 7) for r in (3, 4, 5)]
    assert all(f["order"] > moore(f["degree"], f["diameter"] - 1) for f in factors)
    patterns = {k: [p for p in combinations_with_replacement(range(2, 7), k) if math.prod(p) <= 12]
                for k in (2, 3)}
    products = []
    for target_D in (3, 4, 5):
        for count in (2, 3):
            for ff in combinations_with_replacement(factors, count):
                degree = math.prod(f["degree"] for f in ff)
                if degree > 12 or max(f["diameter"] for f in ff) > target_D:
                    continue
                n = math.prod(f["order"] for f in ff)
                item = {"factors": ff, "factor_count": count, "degree_bound": degree,
                        "target_diameter": target_D, "order": n,
                        "baseline_at_degree_bound": baseline[(degree, target_D)],
                        "numerically_exceeds_baseline": n > baseline[(degree, target_D)]}
                if item["numerically_exceeds_baseline"]:
                    item["walk_obstruction"] = witness(ff)
                products.append(item)
    # Also compare at every larger degree cap, never assuming monotonicity of
    # the external table to skip a case.
    exceeders, case_results = [], []
    for case in cases:
        degree, diameter, old = case["degree_cap"], case["diameter_cap"], case["baseline_order"]
        eligible = [p for p in products if p["target_diameter"] == diameter and p["degree_bound"] <= degree]
        best = max(p["order"] for p in eligible)
        hits = []
        for p in eligible:
            if p["order"] > old:
                item = {**p, "target_degree_cap": degree, "target_baseline": old,
                        "walk_obstruction": witness(p["factors"])}
                hits.append(item)
                exceeders.append(item)
        case_results.append({"degree_cap": degree, "diameter_cap": diameter, "baseline_order": old,
                             "parameter_products_considered": len(eligible),
                             "maximum_saved_factor_product_order": best,
                             "numerical_exceeders": len(hits), "all_exceeders_have_walk_obstruction": True})
    maximum_order_rows = []
    for count in (2, 3):
        for pattern in patterns[count]:
            row = {"factor_degrees": pattern, "degree_bound": math.prod(pattern), "by_diameter": {}}
            for r in (3, 4, 5):
                n = math.prod(ORDERS[d][r] for d in pattern)
                row["by_diameter"][r] = {"order": n, "baseline": baseline[(math.prod(pattern), r)],
                                         "exceeds": n > baseline[(math.prod(pattern), r)]}
            maximum_order_rows.append(row)
    lower_diameter_check = []
    for count in (2, 3):
        for pattern in patterns[count]:
            upper = max((d * d + 1) * math.prod(ORDERS[e][3] for j, e in enumerate(pattern) if j != i)
                        for i, d in enumerate(pattern))
            old = baseline[(math.prod(pattern), 3)]
            assert upper <= old
            lower_diameter_check.append({"factor_degrees": pattern,
                "one_or_more_factor_diameter_le2_optimistic_order_bound": upper,
                "target_D3_baseline": old})
    result = {
        "status": "COMPLETE_SAVED_FACTOR_TENSOR_SCREEN_ALL_NUMERICAL_EXCEEDERS_BLOCKED",
        "history": {"same_tensor_screen_found": False,
            "old_cartesian_strong_screen": "research/ddp/breadth_20261027/graph_products/REPORT.md",
            "old_report_explicitly_left_tensor_open": True,
            "Kronecker_source_note_is_different_degree18_polarity_construction": "research/ddp/SOURCE_UPDATE_20261026_22.md"},
        "snapshot": str(SNAPSHOT.relative_to(ROOT)), "factor_orders": factors,
        "source_pages": {
            "D3": {"local": "research/ddp/m1_sources/desc_g3.html", "primary": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g3.html"},
            "D4": {"local": "research/ddp/m1_sources/desc_g4.html", "primary": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html"},
            "D5": {"local": "research/ddp/m1_degree5_transfer/desc_g5_source.html", "primary": "https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g5.html"}},
        "factor_degree_range": [2, 6], "factor_diameters_tabulated": [3, 4, 5],
        "factor_counts_screened": [2, 3], "four_factors_impossible_under_degree12": True,
        "two_factor_degree_patterns": patterns[2], "three_factor_degree_patterns": patterns[3],
        "product_parameter_rows_by_target_D_at_degree12": {r: sum(p["target_diameter"] == r for p in products) for r in (3, 4, 5)},
        "all_parameter_products": products, "all27_target_cells": case_results,
        "maximum_order_rows": maximum_order_rows,
        "two_factor_numerical_exceeders": sum(e["factor_count"] == 2 for e in exceeders),
        "three_factor_numerical_exceeders": sum(e["factor_count"] == 3 for e in exceeders),
        "numerical_exceeders": exceeders,
        "lower_diameter_factor_Moore_check": lower_diameter_check,
        "remaining_numerical_exceeders_without_proof": 0,
        "product_graphs_generated": 0, "BFS_performed": False, "new_lower_bounds": 0,
        "CPU_seconds": time.process_time() - started, "workers": 1,
        "CPU_hard_limit_seconds": 10, "pending": [],
        "scope": "Known saved-source orders plus classical odd cycles, degree2..6, plain categorical products; not arbitrary unknown larger factors or product repairs."
    }
    (HERE / "RESULTS.json").write_text(json.dumps(result, indent=2) + "\n")
    summary = {k: v for k, v in result.items() if k not in ("all_parameter_products", "factor_orders", "all27_target_cells", "numerical_exceeders", "maximum_order_rows", "lower_diameter_factor_Moore_check")}
    (HERE / "terminal.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "parameter_rows": result["product_parameter_rows_by_target_D_at_degree12"],
                      "two_factor_numerical_exceeders": result["two_factor_numerical_exceeders"],
                      "three_factor_numerical_exceeders": result["three_factor_numerical_exceeders"],
                      "CPU_seconds": result["CPU_seconds"]}, indent=2))


if __name__ == "__main__":
    main()

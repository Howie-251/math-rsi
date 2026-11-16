"""Read-only receipt/path consistency check; no geometry or distance computation."""
import json
from pathlib import Path
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
HERE = Path(__file__).resolve().parent
WORK = HERE.parent


def receipt(relative):
    return json.loads((WORK / relative).read_text())


def main():
    start = time.monotonic()
    finite = receipt("h9_cross_finite_binding_20261116/RESULT.json")
    assert finite["status"] == "ALL_FINITE_CROSS_ROUTING_INPUTS_PASS"
    for key in ("coordinate_map_injective", "all_points_nonzero_normalized_null",
                "every_line_full_projective_span", "every_line_basis_cross_zero",
                "projective_lines_distinct"):
        assert finite[key] is True, key
    assert finite["points_checked"] == finite["lines_checked"] == 66430
    assert finite["point_incidence_degrees"] == 10
    assert finite["all_local_projective_stars"] == 91
    route = receipt("h9_core_route_certificate_20261116/RESULT.json")
    assert route["status"] == "UNIVERSAL_TRANSPORT_AND_FIXED_ROUTE_DIAGNOSTICS_PASS"
    assert route["actual_incidence_steps"] == 664300
    assert route["edge_steps"] == 664272 and route["stays"] == 28
    assert route["edge_steps"] + route["stays"] == route["actual_incidence_steps"]
    assert route["sigma_bijection_checked"] and route["pi_surjective_on_core"]

    expected_sizes = {
        "h9_exact_binding/point_coords.u8.bin": 66430 * 7,
        "h9_exact_binding/line_points.i32.bin": 66430 * 10 * 4,
        "h9_exact_binding/pi.u16.bin": 66430 * 2,
        "h9_other_orientation/sigma.i32.bin": 66430 * 4,
    }
    for path, size in expected_sizes.items():
        assert (WORK / path).stat().st_size == size, path
    router_source = (WORK / "h9_core_route_certificate_20261116/route_core.py").read_text()
    assert 'WORK / "h9_other_orientation/sigma.i32.bin"' in router_source
    assert 'WORK / "h9_n37632/graph_d11_D5_n37632.edges"' in router_source
    assert 'N, CORE = 66430, 37471' in router_source
    bound = receipt("h9_independent_completion/other37632/BINDING.json")
    assert bound["actual_core_exact_match"] and bound["sigma_bijection"]
    assert bound["actual_core_edges"] == 203747
    final = receipt("h9_n37632/independent/RESULT.json")
    assert final["n"] == 37632 and final["m"] == 205366
    assert final["simple"] and final["maximum_degree"] == 11
    assert final["literal_binding"]["core_unchanged"]
    assert final["literal_binding"]["only_added_edge"] == [31, 37631]
    rows = [json.loads(row) for row in
            (WORK / "h9_n37632/independent/ROOT_RESULTS.jsonl").read_text().splitlines()]
    assert len(rows) == 161
    assert {row["root"] for row in rows} == set(range(37471, 37632))
    assert all(row["eccentricity"] <= 5 and row["unreachable_count"] == 0
               and row["beyond5_count"] == 0 for row in rows)
    result = dict(
        status="STATIC_EXISTING_RECEIPTS_AND_PATHS_CONSISTENT",
        finite_receipt_scope="All actual66430 points/lines and every91-star; reused, not rerun",
        universal_transport_steps=664300,
        actual_sigma="h9_other_orientation/sigma.i32.bin",
        core_vertices=37471,
        final_vertices=37632,
        final_edges=205366,
        actual_exterior_root_summaries_checked=161,
        exact_exterior_root_set=list(range(37471, 37632)),
        binary_sizes_checked=expected_sizes,
        root_summaries_are_Lean_path_certificates=False,
        geometry_recomputed=False, BFS=0, SAT=0, Lean=0,
        CPU_seconds=time.process_time(),
        wall_seconds=time.monotonic() - start,
    )
    (HERE / "STATIC_CHECK.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in
                      ("status", "actual_exterior_root_summaries_checked", "CPU_seconds", "wall_seconds")}))


if __name__ == "__main__":
    main()

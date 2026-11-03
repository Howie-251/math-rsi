"""Prepare the complete free-C5 order-60 graph CNF; never launch a solver.

354 orbit variables partition all 1770 pairs. Degree counters retain
repeated literals, and all 58 real middle vertices are used per pair orbit.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import importlib.util
import json
import os
import shutil
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / "computations/dd82/construction"
OUT = BASE / "cyclic5_full60_run"
SEED = BASE / "cyclic5_twelve_orbits60_signature_lift_run/seed20"
RUN_ID = "dd82-v3-c5-full60-20261013"
HELPER = ROOT / "context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/code/n62/n62_ab_cnf.py"


def save(path, data):
    path.write_text(json.dumps(data, indent=2) + "\n")


def pair(u, v):
    assert u != v
    return (u, v) if u < v else (v, u)


def translate(v, t):
    return 5*(v//5) + (v % 5 + t) % 5


def main():
    cpu, wall = time.process_time(), time.monotonic()
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    OUT.mkdir(exist_ok=True)
    assert not (OUT / "input.cnf").exists(), "Preserve the prepared input"
    spec = importlib.util.spec_from_file_location("cyclic5_full60_exact_helpers", HELPER)
    helper = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = helper
    spec.loader.exec_module(helper)
    em = helper.CNFEmitter(OUT / "input.cnf")

    # Every primary variable represents all five edges in one genuine orbit.
    palette, edge_to_variable, internal = [], {}, {}
    for a in range(12):
        for b in range(a, 12):
            for shift in ((1, 2) if a == b else range(5)):
                q = em.new_var("edge_orbit")
                expanded = sorted({pair(5*a+t, 5*b+(t+shift) % 5) for t in range(5)})
                assert len(expanded) == 5
                for uv in expanded:
                    assert uv not in edge_to_variable
                    edge_to_variable[uv] = q
                representative = pair(5*a, 5*b+shift)
                assert representative in expanded
                palette.append(dict(index=len(palette), variable=q, a=a, b=b,
                    shift=shift, edges=expanded, representative=list(representative)))
                if a == b:
                    internal[a, shift] = q
    assert len(palette) == 354 and em.variable_count == 354
    assert set(edge_to_variable) == set(combinations(range(60), 2))
    assert len(internal) == 24
    assert all(edge_to_variable[pair(translate(u, 1), translate(v, 1))] == q
               for (u, v), q in edge_to_variable.items())

    raw = [tuple(map(int, line.split())) for line in (SEED / "seed.edges").read_text().splitlines()]
    assert raw[0] == (60, 240)
    seed_edges = set(raw[1:])
    assert len(seed_edges) == len(raw)-1 == 240
    assert seed_edges <= set(edge_to_variable)
    seed_degrees = [0] * 60
    for u, v in seed_edges:
        seed_degrees[u] += 1
        seed_degrees[v] += 1
    assert seed_degrees == [8] * 60
    values = {}
    for item in palette:
        chosen = [tuple(uv) in seed_edges for uv in item["edges"]]
        assert len(set(chosen)) == 1
        values[item["variable"]] = chosen[0]
        item["seed_selected"] = chosen[0]
    assert sum(values.values()) == 48
    assert all(sum(values[internal[a, s]] for s in (1, 2)) == 1 for a in range(12))

    # A point has 59 potential neighbours. Its internal orbit variables
    # appear twice in this literal list, correctly contributing weight two.
    degree_records, degree_variables = [], []
    for a in range(12):
        u = 5*a
        neighbours = [v for v in range(60) if v != u]
        inputs = [edge_to_variable[pair(u, v)] for v in neighbours]
        multiplicities = Counter(inputs)
        assert len(inputs) == 59 and len(multiplicities) == 57
        assert {q for q, count in multiplicities.items() if count == 2} == {internal[a, 1], internal[a, 2]}
        assert all(count in (1, 2) for count in multiplicities.values())
        before_var, before_clause = em.variable_count, em.clause_count
        thresholds = helper.unary_thresholds(em, inputs, 9, "degree_threshold")
        em.add_clause(thresholds[7])
        em.add_clause(-thresholds[8])
        next_var, prefix_total = before_var + 1, 0
        for prefix, x in enumerate(inputs, 1):
            prefix_total += values[x]
            for threshold in range(1, min(prefix, 9)+1):
                degree_variables.append([next_var, a, prefix, threshold])
                values[next_var] = prefix_total >= threshold
                next_var += 1
        assert next_var == em.variable_count + 1 and prefix_total == 8
        degree_records.append(dict(orbit=a, vertex=u, neighbours=neighbours,
            inputs=inputs, final_thresholds=thresholds,
            first_variable=before_var+1, last_variable=em.variable_count,
            first_clause=before_clause+1, last_clause=em.clause_count))
    degree_end = em.clause_count
    assert len(degree_variables) == 5940 and degree_end == 22968

    internal_rows = []
    for a in range(12):
        em.add_clause(-internal[a, 1], -internal[a, 2])
        internal_rows.append(dict(orbit=a, clause_id=em.clause_count,
                                  literals=[-internal[a, 1], -internal[a, 2]]))
    normalized_rows = []
    for a in (0, 1):
        for shift in (1, 2):
            em.add_clause(-internal[a, shift])
            normalized_rows.append(dict(orbit=a, shift=shift,
                clause_id=em.clause_count, literal=-internal[a, shift]))

    # Cheap proved quotient multiplicity bounds, with each step separately
    # guarding the fact that its endpoint has internal degree two.
    multiplicity_rows = []
    for a, b in combinations(range(12), 2):
        cross = [x["variable"] for x in palette if x["a"] == a and x["b"] == b]
        assert len(cross) == 5

        def add_bound(kind, guards, subset):
            literals = [-q for q in list(guards) + list(subset)]
            em.add_clause(*literals)
            multiplicity_rows.append([em.clause_count, kind, a, b, list(guards), list(subset)])

        for subset in combinations(cross, 4):
            add_bound("q_le_3", [], subset)
        for endpoint in (a, b):
            for shift in (1, 2):
                for subset in combinations(cross, 3):
                    add_bound("internal_endpoint_q_le_2", [internal[endpoint, shift]], subset)
        for sa in (1, 2):
            for sb in (1, 2):
                for subset in combinations(cross, 2):
                    add_bound("both_internal_q_le_1", [internal[a, sa], internal[b, sb]], subset)
    assert len(multiplicity_rows) == 5610

    # No route deduplication: preserve each of the 58 actual middle vertices.
    and_records, coverage = [], []
    for item in palette:
        u, v = item["representative"]
        direct = edge_to_variable[pair(u, v)]
        assert direct == item["variable"]
        paths = []
        for w in range(60):
            if w == u or w == v:
                continue
            left = edge_to_variable[pair(u, w)]
            right = edge_to_variable[pair(w, v)]
            q = em.new_var("actual_two_edge_path")
            helper.add_iff_and(em, q, left, right)
            and_records.append([q, left, right])
            values[q] = values[left] and values[right]
            paths.append(dict(middle=w, output=q, left=left, right=right))
        assert len(paths) == 58
        em.add_clause(direct, *(p["output"] for p in paths))
        coverage.append(dict(orbit_index=item["index"], pair=[u, v],
            direct=direct, paths=paths, clause_id=em.clause_count))
    em.finish()
    assert len(and_records) == 20532 and len(coverage) == 354
    assert (em.variable_count, em.clause_count) == (26826, 90544)
    assert set(values) == set(range(1, em.variable_count+1))

    save(OUT / "palette.json", dict(orbits=palette, primary_variables=354,
        coordinates="vertex 5*a+t, a in 0..11, t in Z5"))
    save(OUT / "edge_variables.json", dict(format=["u", "v", "variable"],
        rows=[[u, v, q] for (u, v), q in sorted(edge_to_variable.items())]))
    save(OUT / "variables.json", dict(
        primary_variables=[item["variable"] for item in palette],
        degree_record_format=["variable", "orbit", "prefix_length", "threshold"],
        degree_variables=degree_variables, and_record_format=["output", "left", "right"],
        and_variables=and_records))
    save(OUT / "degree_counters.json", degree_records)
    save(OUT / "coverage.json", coverage)
    save(OUT / "necessary_internal_clauses.json", dict(
        at_most_one_circle=internal_rows, two_independent_orbits=normalized_rows,
        normalization="Relabel any two independent vertex orbits as 0 and 1; no quotient fixed"))
    save(OUT / "necessary_multiplicity_clauses.json", dict(
        format=["clause_id", "kind", "orbit_a", "orbit_b", "positive_guards", "positive_selected_subset"],
        interpretation="One clause negating every listed guard and selected literal",
        rows=multiplicity_rows,
        counts=dict(q_le_3=330, internal_endpoint_q_le_2=2640, both_internal_q_le_1=2640)))
    shutil.copyfile(SEED / "seed.edges", OUT / "seed.edges")
    save(OUT / "seed.json", dict(n=60, edges=sorted(seed_edges), source=str(SEED / "seed.edges"),
        valid_target=False, purpose="Consistency seed; expected to violate two-independent-orbit normalization"))
    (OUT / "seed.assignment.txt").write_text("v " + " ".join(
        str(q if values[q] else -q) for q in range(1, em.variable_count+1)) + " 0\n")

    false_ids, clause_count = [], 0
    for line in (OUT / "input.cnf").read_text().splitlines():
        if line.startswith("p "):
            assert line.split() == ["p", "cnf", "26826", "90544"]
            continue
        entries = list(map(int, line.split()))
        assert entries[-1] == 0
        clause_count += 1
        if not any(values[abs(q)] == (q > 0) for q in entries[:-1]):
            false_ids.append(clause_count)
    assert clause_count == em.clause_count
    by_coverage_id = {x["clause_id"]: x for x in coverage}
    normalization_ids = {x["clause_id"] for x in normalized_rows}
    failed_coverage = [by_coverage_id[q] for q in false_ids if q in by_coverage_id]
    failed_normalization = [q for q in false_ids if q in normalization_ids]
    assert len(failed_coverage) == 4 and len(failed_normalization) == 2
    assert set(false_ids) <= set(by_coverage_id) | normalization_ids

    # Read old BFS and its actual old-to-new coordinate permutation. No BFS.
    automorphism = json.loads((SEED / "automorphism.json").read_text())
    old_to_new = automorphism["old_to_new"]
    assert sorted(old_to_new) == list(range(60))
    original_path = BASE / "petersen_all_matchings_run/candidate.best.edges"
    original_rows = [tuple(map(int, s.split())) for s in original_path.read_text().splitlines()]
    assert original_rows[0] == (60, 240)
    assert {pair(old_to_new[u], old_to_new[v]) for u, v in original_rows[1:]} == seed_edges
    old_bfs_path = BASE / "petersen_all_matchings_run/candidate.best.verification.json"
    old_bfs = json.loads(old_bfs_path.read_text())
    expected_bad = {pair(old_to_new[u], old_to_new[v]) for row in old_bfs["bad_pairs"] for u, v in [row["pair"]]}
    expanded_bad = {pair(translate(u, t), translate(v, t))
                    for row in failed_coverage for u, v in [row["pair"]] for t in range(5)}
    assert expanded_bad == expected_bad and len(expanded_bad) == 20
    save(OUT / "sanity.json", dict(
        solver_calls=0, new_bfs_runs=0, n=60, edges=240, all_degrees_eight=True,
        primary_variables=354, selected_orbits=48,
        full_pair_partition_size=1770, every_pair_orbit_has_five_members=True,
        degree_inputs_per_vertex=59, distinct_degree_inputs_per_vertex=57,
        repeated_internal_literal_weight=2,
        all_degree_and_tseitin_clauses_satisfied=True,
        all_internal_at_most_one_clauses_satisfied=True,
        all_5610_multiplicity_clauses_satisfied=True,
        failed_coverage_orbits=[dict(orbit_index=row["orbit_index"], pair=row["pair"],
                                   clause_id=row["clause_id"]) for row in failed_coverage],
        failed_coverage_orbit_count=4, failed_independent_orbit_units=failed_normalization,
        total_false_clause_count=len(false_ids), false_clause_ids=false_ids,
        expanded_bad_pairs=sorted(expanded_bad), expanded_bad_pair_count=20,
        matches_existing_independent_bfs=True, existing_bfs_source=str(old_bfs_path),
        seed_satisfies_new_independence_normalization=False,
        expected_failure="Seed has one internal cycle in each orbit, while normalized target orbits 0 and 1 must be independent"))
    result = dict(run_id=RUN_ID, status="PREPARED_NOT_RUN", solver_calls=0, new_bfs_runs=0,
        scope="All simple order-60 degree-8 diameter-2 graphs with a free C5 action, up to orbit labels; no fixed quotient",
        primary_variables=354, degree_threshold_variables=len(degree_variables),
        path_variables=len(and_records), variables=em.variable_count, clauses=em.clause_count,
        clause_groups=dict(exact_degrees=degree_end, at_most_one_internal_circle=12,
            normalized_two_independent_orbits=4, quotient_multiplicity=5610,
            tseitin_paths=3*len(and_records), pair_orbit_coverage=354),
        edge_to_orbit_mapping_size=1770, degree_constraints=12,
        intermediates_per_pair_orbit=58, route_deduplication=False,
        cnf_bytes=(OUT / "input.cnf").stat().st_size,
        helper_reuse="CNFEmitter, unary_thresholds and add_iff_and definitions only; no old branch search executed",
        preparation_cpu_seconds=time.process_time()-cpu,
        preparation_wall_seconds=time.monotonic()-wall)
    save(OUT / "encoding.json", result)
    print(json.dumps(result))


if __name__ == "__main__":
    main()

"""Complete quartic inverse-closed Cayley scope of the one fixed84-element group."""

from collections import Counter
from itertools import combinations, product
import json
from pathlib import Path
import resource
import time


HERE = Path(__file__).resolve().parent
ELEMENTS = list(product(range(12), range(7)))
INDEX = {g: i for i, g in enumerate(ELEMENTS)}
IDENTITY = (0, 0)
POW3 = [pow(3, u, 7) for u in range(12)]
INVERSE_SYMBOL = (1, 0, 3, 2)
WORDS = [w for w in product(range(4), repeat=4)
         if all(w[i + 1] != INVERSE_SYMBOL[w[i]] for i in range(3))]


def mul(g, h):
    return ((g[0] + h[0]) % 12, (g[1] * POW3[h[0]] + h[1]) % 7)


def inverse(g):
    phase = (-g[0]) % 12
    return (phase, (-g[1] * POW3[phase]) % 7)


def order(g):
    value = IDENTITY
    for k in range(1, 85):
        value = mul(value, g)
        if value == IDENTITY:
            return k
    raise AssertionError(g)


def evaluate(generators):
    endpoints = []
    for word in WORDS:
        g = IDENTITY
        for symbol in word:
            g = mul(g, generators[symbol])
        endpoints.append(g)
    multiplicity = Counter(endpoints)
    missing = [g for g in ELEMENTS if g not in multiplicity]
    return {"generators": generators, "inverse_labels": list(INVERSE_SYMBOL),
            "reduced_words": len(WORDS), "covered_vertices": len(multiplicity),
            "missing_vertices": missing,
            "endpoint_multiplicities": [{"element": g, "walks": n} for g, n in sorted(multiplicity.items())],
            "phase_word_counts": dict(sorted(Counter(g[0] for g in endpoints).items())),
            "status": "HIT" if not missing else "NOT_EXACT_NB4"}


def save_hit(candidate):
    generators = [tuple(g) for g in candidate["generators"]]
    neighbours = [[INDEX[mul(g, s)] for s in generators] for g in ELEMENTS]
    assert all(len(set(row)) == 4 for row in neighbours)
    for u, row in enumerate(neighbours):
        assert u not in row
        for symbol, v in enumerate(row):
            assert neighbours[v][INVERSE_SYMBOL[symbol]] == u
    edges = sorted({(min(u, v), max(u, v)) for u, row in enumerate(neighbours) for v in row})
    assert len(edges) == 168
    graph = {"n": 84, "m": 168, "degree": 4, "element_encoding": "id=7*phase+translation",
             "elements": ELEMENTS, "generators": generators, "inverse_labels": list(INVERSE_SYMBOL),
             "edges": edges, "neighbors_by_symbol": neighbours,
             "exact_NB4_from_identity_covers_all84": True,
             "left_translation_proof": "L_h(g)=h*g sends g--g*s to h*g--(h*g)*s and preserves labels; L_h(identity)=h, so one identity row proves all ordered pairs including diagonal.",
             "prospective_lift_order": 84 * 81, "prospective_lift_degree": 12}
    (HERE / "hit_controller.json").write_text(json.dumps(graph, indent=2) + "\n")
    (HERE / "hit.edges").write_text("84 168\n" + "".join(f"{u} {v}\n" for u, v in edges))
    print("HIT_EXACT_NB4 hit_controller.json", flush=True)


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
    began, wall = time.process_time(), time.monotonic()
    assert len(ELEMENTS) == 84 and len(WORDS) == 108 and pow(3, 12, 7) == 1
    assert all(mul(g, IDENTITY) == g == mul(IDENTITY, g) for g in ELEMENTS)
    assert all(mul(g, inverse(g)) == IDENTITY == mul(inverse(g), g) for g in ELEMENTS)
    involutions = [g for g in ELEMENTS if g != IDENTITY and inverse(g) == g]
    pairs = [(g, inverse(g)) for g in ELEMENTS
             if g != IDENTITY and INDEX[g] < INDEX[inverse(g)]]
    all_pair_choices = list(combinations(range(len(pairs)), 2))
    group = {"order": 84, "elements": ELEMENTS,
             "product": "(x,y)*(u,v)=((x+u) mod12,(y*3^u+v) mod7)",
             "inverse": "(-x mod12,-y*3^(-x mod12) mod7)",
             "nonidentity_involutions": involutions, "noninvolution_inverse_pair_count": len(pairs),
             "noninvolution_inverse_pairs": pairs, "two_pair_choices": len(all_pair_choices),
             "quartic_scope_completeness": "An inverse-closed4set without identity consists of two noninvolution inverse pairs, one such pair plus two involutions, or four involutions. Exactly one nonidentity involution leaves only the first composition.",
             "first_a_order": order((3, 0)), "first_b_order": order((2, 1))}
    (HERE / "group.json").write_text(json.dumps(group, indent=2) + "\n")
    first_file = HERE / "first_probe.json"
    if first_file.exists():
        first = json.loads(first_file.read_text())
        assert first["generators"] == [[3, 0], [9, 0], [2, 1], [10, 3]]
    else:
        first = evaluate([(3, 0), inverse((3, 0)), (2, 1), inverse((2, 1))])
        first_file.write_text(json.dumps(first, indent=2) + "\n")
    if first["covered_vertices"] == 84:
        save_hit(first)
        (HERE / "terminal.json").write_text(json.dumps({
            "status": "FIRST_SPECIFIED_PAIR_HIT_STOPPED", "complete_fixed_group_enumeration": False,
            "quartic_sets_examined": 1, "CPU_seconds": time.process_time() - began,
            "BFS_performed": False, "large_lift_generated": False, "new_lower_bounds": 0,
        }, indent=2) + "\n")
        return
    first_key = tuple(sorted((min(INDEX[(3, 0)], INDEX[inverse((3, 0))]),
                              min(INDEX[(2, 1)], INDEX[inverse((2, 1))]))))
    summaries, best, hit = [], first, None
    phase_rejected, phase_passed, additional_true_evaluations, first_reused = 0, 0, 0, 0
    phase_histogram, true_histogram = Counter(), Counter()
    for ordinal, (i, j) in enumerate(all_pair_choices):
        generators = [pairs[i][0], pairs[i][1], pairs[j][0], pairs[j][1]]
        assert len(set(generators)) == 4 and IDENTITY not in generators
        phases = [g[0] for g in generators]
        phase_counts = [0] * 12
        for word in WORDS:
            phase_counts[sum(phases[s] for s in word) % 12] += 1
        upper_bound = sum(min(c, 7) for c in phase_counts)
        summary = {"ordinal": ordinal, "inverse_pair_indices": [i, j], "generators": generators,
                   "phase_word_counts": phase_counts, "phase_endpoint_capacity_upper_bound": upper_bound}
        phase_histogram[upper_bound] += 1
        if min(phase_counts) < 7:
            phase_rejected += 1
            summary["status"] = "PHASE_WORD_COUNT_LT7_REJECTED"
        else:
            phase_passed += 1
            key = (INDEX[pairs[i][0]], INDEX[pairs[j][0]])
            if key == first_key:
                candidate = first
                first_reused += 1
                summary["first_explicit_true_word_probe_reused"] = True
            else:
                candidate = evaluate(generators)
                additional_true_evaluations += 1
            summary.update({"status": candidate["status"], "covered_vertices": candidate["covered_vertices"],
                            "missing_count": len(candidate["missing_vertices"])})
            true_histogram[candidate["covered_vertices"]] += 1
            if candidate["covered_vertices"] > best["covered_vertices"]:
                best = {**candidate, "inverse_pair_indices": [i, j], "ordinal": ordinal}
            if candidate["covered_vertices"] == 84:
                hit = candidate
                save_hit(candidate)
        summaries.append(summary)
        if hit:
            break
    (HERE / "all_sets.json").write_text(json.dumps(summaries, separators=(",", ":")) + "\n")
    (HERE / "best_word_coverage.json").write_text(json.dumps(best, indent=2) + "\n")
    terminal = {
        "status": "FIXED_GROUP_QUARTIC_CAYLEY_EXACT_NB4_HIT" if hit else "COMPLETE_FIXED_GROUP_QUARTIC_CAYLEY_NO_EXACT_NB4",
        "group_order": 84, "nonidentity_involutions": involutions,
        "inverse_pairs": len(pairs), "quartic_inverse_closed_sets": len(all_pair_choices),
        "sets_examined": len(summaries), "complete_fixed_group_enumeration": not bool(hit),
        "phase_word_capacity_rejected": phase_rejected, "phase_word_capacity_passed": phase_passed,
        "first_specified_pair_true_coverage": first["covered_vertices"],
        "first_specified_true_probe_reused_in_complete_enumeration": first_reused,
        "additional_true_group_word_evaluations": additional_true_evaluations,
        "distinct_generator_sets_evaluated_by_true_group_words": additional_true_evaluations + 1,
        "phase_capacity_upper_bound_histogram": dict(sorted(phase_histogram.items())),
        "true_coverage_histogram_after_phase_filter": dict(sorted(true_histogram.items())),
        "best_actual_word_coverage": best["covered_vertices"], "hits": int(bool(hit)),
        "reduced_words_per_set": 108, "word_length": 4,
        "ordinary_BFS_performed": False, "large_lift_generated": False, "new_lower_bounds": 0,
        "CPU_seconds": time.process_time() - began, "wall_seconds": time.monotonic() - wall,
        "workers": 1, "CPU_hard_limit_seconds": 10,
        "scope": "Every simple quartic inverse-closed Cayley generator set of this one fixed F7 semidirect_3 C12 group; not arbitrary84 controllers or other groups.",
        "pending": [],
    }
    (HERE / "terminal.json").write_text(json.dumps(terminal, indent=2) + "\n")
    print(json.dumps(terminal, indent=2))


if __name__ == "__main__":
    main()

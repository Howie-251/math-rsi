"""Independent bounded exact check of the five/seven/nine component quotients.

Rows are weak compositions of eight, subsequently filtered by divisibility;
the discovery code's gcd parametrization is not used for enumeration. Search
uses forward filtering and a direct complete-matrix identity check. The
discovery module is loaded only after all independent searches have finished,
to compare every row domain. No graph realizability is asserted.
"""

import importlib.util
import itertools
import json
import math
import os
from pathlib import Path
import signal
import time


ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / "computations/dd82/n62"
OUTPUT = DIRECTORY / "large_component_quotients_check.json"
BUDGET_SECONDS = 30


def weak_rows(k):
    """Stars and bars enumerates each nonnegative row of sum eight once."""
    for bars in itertools.combinations(range(8 + k - 1), k - 1):
        bounds = (-1,) + bars + (8 + k - 1,)
        yield tuple(bounds[j + 1] - bounds[j] - 1 for j in range(k))


def size_tuples(k):
    # Every sorted half-size lies between 2 and 31 - 2(k-1).
    return [
        tuple(2 * part for part in parts)
        for parts in itertools.combinations_with_replacement(
            range(2, 31 - 2 * (k - 1) + 1), k
        )
        if sum(parts) == 31
    ]


def candidate_rows(sizes, i, rows, trace):
    result = []
    ni = sizes[i]
    for row in rows:
        if row[i] > trace or row[i] >= ni:
            continue
        column = []
        for value, nj in zip(row, sizes):
            numerator = ni * value
            quotient, remainder = divmod(numerator, nj)
            if remainder or quotient > 8:
                break
            column.append(quotient)
        else:
            if sum(a * b for a, b in zip(row, column)) + row[i] == 10 + ni:
                result.append((row, tuple(column)))
    return result


def compatible(i, left, j, right):
    row, column = left
    other_row, other_column = right
    if row[j] != other_column[i] or other_row[i] != column[j]:
        return False
    # Only one ordered equation is used here: balance implies the reverse
    # equation. All ordered equations are checked again at a complete leaf.
    return sum(a * b for a, b in zip(row, other_column)) + row[j]


def check_matrix(sizes, matrix):
    k = len(sizes)
    assert len(matrix) == k and all(len(row) == k for row in matrix)
    assert all(type(value) is int and value >= 0 for row in matrix for value in row)
    assert all(sum(row) == 8 for row in matrix)
    assert sum(matrix[i][i] for i in range(k)) == (17 - k) // 2
    assert all(matrix[i][i] < sizes[i] for i in range(k))
    for i in range(k):
        for j in range(k):
            assert sizes[i] * matrix[i][j] == sizes[j] * matrix[j][i]
            assert (
                sum(matrix[i][z] * matrix[z][j] for z in range(k))
                + matrix[i][j]
                == sizes[j] + (10 if i == j else 0)
            )


def relabelings(sizes, matrix):
    groups = [tuple(i for i, ni in enumerate(sizes) if ni == size)
              for size in sorted(set(sizes))]
    for image_groups in itertools.product(
        *(itertools.permutations(group) for group in groups)
    ):
        permutation = tuple(itertools.chain.from_iterable(image_groups))
        yield tuple(tuple(matrix[i][j] for j in permutation) for i in permutation)


def enumerate_case(k):
    trace = (17 - k) // 2
    rows = tuple(weak_rows(k))
    assert len(rows) == len(set(rows)) == math.comb(8 + k - 1, k - 1)
    sizes_list = size_tuples(k)
    stored_domains = {}
    solutions = {}
    zero_domain = nodes = maximum_domain = 0
    case_start = time.monotonic()
    for sizes in sizes_list:
        domains = [candidate_rows(sizes, i, rows, trace) for i in range(k)]
        stored_domains[sizes] = domains
        maximum_domain = max(maximum_domain, *(len(domain) for domain in domains))
        if any(not domain for domain in domains):
            zero_domain += 1
            continue

        def search(pending, chosen, diagonal):
            nonlocal nodes
            nodes += 1
            if not pending:
                if diagonal == trace:
                    matrix = tuple(chosen[i][0] for i in range(k))
                    check_matrix(sizes, matrix)
                    matrices = solutions.setdefault(sizes, set())
                    assert matrix not in matrices
                    matrices.add(matrix)
                return
            lower = diagonal + sum(min(item[0][i] for item in options)
                                   for i, options in pending.items())
            upper = diagonal + sum(max(item[0][i] for item in options)
                                   for i, options in pending.items())
            if lower > trace or upper < trace:
                return
            i = min(pending, key=lambda index: (len(pending[index]), index))
            for candidate in pending[i]:
                next_diagonal = diagonal + candidate[0][i]
                if next_diagonal > trace:
                    continue
                remaining = {}
                for j, options in pending.items():
                    if j == i:
                        continue
                    filtered = [other for other in options
                                if compatible(i, candidate, j, other) == sizes[j]]
                    if not filtered:
                        break
                    remaining[j] = filtered
                else:
                    search(remaining, {**chosen, i: candidate}, next_diagonal)

        search(dict(enumerate(domains)), {}, 0)

    canonical = []
    for sizes, matrices in sorted(solutions.items()):
        orbits = {}
        for matrix in matrices:
            representative = min(relabelings(sizes, matrix))
            orbits[representative] = orbits.get(representative, 0) + 1
        for matrix, count in sorted(orbits.items()):
            orbit = set(relabelings(sizes, matrix))
            assert len(orbit) == count and orbit <= matrices
            canonical.append({"sizes": sizes, "R": matrix,
                              "labelled_count": count, "orbit_size": len(orbit)})

    result = {
        "components": k,
        "trace": trace,
        "weak_rows": len(rows),
        "size_partitions_total": len(sizes_list),
        "size_partitions_completed": len(sizes_list),
        "partitions_with_empty_row_domain": zero_domain,
        "maximum_single_row_domain": maximum_domain,
        "forward_search_nodes": nodes,
        "labelled_solutions": sum(map(len, solutions.values())),
        "canonical_count": len(canonical),
        "canonical_quotients": canonical,
        "wall_seconds": time.monotonic() - case_start,
    }
    return result, stored_domains


def main():
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    started = time.monotonic()

    def timeout(_signum, _frame):
        raise TimeoutError("Independent 30-second check did not complete")

    signal.signal(signal.SIGALRM, timeout)
    signal.setitimer(signal.ITIMER_REAL, BUDGET_SECONDS)
    cases = []
    all_domains = {}
    for k in (5, 7, 9):
        result, domains = enumerate_case(k)
        cases.append(result)
        all_domains[k] = domains

    # No discovery rows or reference solutions influenced enumeration above.
    spec = importlib.util.spec_from_file_location(
        "discovery_quotient_search", DIRECTORY / "component_quotient_search.py"
    )
    discovery = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(discovery)
    compared_domains = 0
    for case in cases:
        k = case["components"]
        domains_by_sizes = all_domains[k]
        reference = json.loads((DIRECTORY / f"component_quotients_{k}.json").read_text())
        assert reference["status"] == "COMPLETE_QUOTIENT_SEARCH"
        assert reference["minimum_component_size"] == 4
        assert set(domains_by_sizes) == {
            tuple(2 * part for part in parts) for parts in discovery.partitions(31, k)
        }
        for sizes, domains in domains_by_sizes.items():
            for i, domain in enumerate(domains):
                source_domain = discovery.row_domain(sizes, i, case["trace"])
                assert len(domain) == len(set(domain))
                assert len(source_domain) == len(set(source_domain))
                assert set(domain) == set(source_domain)
                compared_domains += 1
        for field in ("components", "trace", "size_partitions_total",
                      "size_partitions_completed", "partitions_with_empty_row_domain",
                      "maximum_single_row_domain", "labelled_solutions"):
            assert case[field] == reference[field], (k, field)
        expected = set()
        for entry in reference["canonical_quotients"]:
            sizes = tuple(entry["sizes"])
            matrix = tuple(map(tuple, entry["R"]))
            assert len(sizes) == k and sum(sizes) == 62
            assert tuple(sorted(sizes)) == sizes
            assert all(size >= 4 and size % 2 == 0 for size in sizes)
            check_matrix(sizes, matrix)
            assert matrix == min(relabelings(sizes, matrix))
            expected.add((sizes, matrix))
        assert len(expected) == len(reference["canonical_quotients"])
        assert expected == {(entry["sizes"], entry["R"])
                            for entry in case["canonical_quotients"]}
        case["reference_matches"] = True
        case["every_original_row_domain_matches"] = True

    elapsed = time.monotonic() - started
    report = {
        "status": "VERIFIED_EXHAUSTIVE_INTEGER_QUOTIENT_CHECK",
        "minimum_component_size": 4,
        "component_counts": [5, 7, 9],
        "cases": cases,
        "row_domains_compared": compared_domains,
        "independent_enumeration_before_loading_discovery": True,
        "cpu_count": len(os.sched_getaffinity(0)),
        "budget_seconds": BUDGET_SECONDS,
        "wall_seconds": elapsed,
        "scope": "Finite balanced integer quotient classification only",
        "nonclaims": [
            "No graph realizability or graph nonexistence result is certified",
            "The minimum size four uses the external actual-graph B<=2 reduction",
            "D1 annotations and their H,K>=14 imports are not used or certified",
            "Other component counts are outside this check",
            "This is external exact computation, not a Lean theorem",
        ],
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    signal.setitimer(signal.ITIMER_REAL, 0)
    print(json.dumps({"status": report["status"], "wall_seconds": elapsed,
                      "row_domains_compared": compared_domains,
                      "cases": [{key: value for key, value in case.items()
                                 if key != "canonical_quotients"} for case in cases]},
                     indent=2))


if __name__ == "__main__":
    main()

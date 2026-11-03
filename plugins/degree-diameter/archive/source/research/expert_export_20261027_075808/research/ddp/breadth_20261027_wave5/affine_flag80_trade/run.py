"""One vertical-class rainbow trade, first8 lexical exact covers, fixed flag cycles."""

from collections import Counter
from itertools import combinations, permutations, product
import json
from pathlib import Path
import resource
import time


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / "mizuno_d4_source"
INVERSE = (3, 2, 1, 0)


def fmul(a, b):
    value = 0
    while b:
        if b & 1:
            value ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7  # alpha^2=alpha+1, modulus x^2+x+1 overF2
    return value


MUL = [[fmul(a, b) for b in range(4)] for a in range(4)]
FINV = {a: next(b for b in range(1, 4) if MUL[a][b] == 1) for a in range(1, 4)}


def canonical(cycle):
    cycle = tuple(cycle)
    choices = []
    for c in (cycle, cycle[::-1]):
        choices.extend(c[i:] + c[:i] for i in range(len(c)))
    return min(choices)


def colour(p, q):
    x, y, u, v = p // 4, p % 4, q // 4, q % 4
    if x == u:
        return None
    slope = MUL[y ^ v][FINV[x ^ u]]
    intercept = y ^ MUL[slope][x]
    return 4 * slope + intercept


def make_controller(solution, rows, old_lines, good4, reduced2):
    new_cycles = [rows[i][0] for i in solution]
    selected = {}
    new_at = {}
    point_selected = [[] for _ in range(16)]
    for i, cycle in enumerate(new_cycles):
        for p in cycle:
            assert p not in new_at
            new_at[p] = 16 + i
        for j, p in enumerate(cycle):
            q = cycle[(j + 1) % 4]
            c = colour(p, q)
            assert c not in selected
            selected[c] = tuple(sorted((p, q)))
            point_selected[p].append(c)
            point_selected[q].append(c)
    assert set(selected) == set(range(16)) and set(new_at) == set(range(16))
    blocks = [list(p) for p in old_lines] + [sorted(c) for c in new_cycles]
    flags = [(p, line) for line, points in enumerate(blocks) for p in sorted(points)]
    flag_id = {flag: i for i, flag in enumerate(flags)}
    assert len(flags) == 80 and len(flag_id) == 80
    neighbours = [[-1] * 4 for _ in flags]
    a_cycles, b_cycles = [], []
    for line in range(20):
        if line < 16:
            p, q = selected[line]
            r, s = sorted(set(blocks[line]) - {p, q})
            cycle = canonical((p, r, q, s))
        else:
            cycle = new_cycles[line - 16]
        a_cycles.append(cycle)
        for i, p in enumerate(cycle):
            u = flag_id[(p, line)]
            neighbours[u][0] = flag_id[(cycle[(i + 1) % 4], line)]
            neighbours[u][3] = flag_id[(cycle[(i - 1) % 4], line)]
    for p in range(16):
        l1, l2 = sorted(point_selected[p])
        assert l1 != l2 and l1 // 4 != l2 // 4
        old_at = [line for line, points in enumerate(old_lines) if p in points]
        middle = sorted(set(old_at) - {l1, l2})
        assert len(old_at) == 4 and len(middle) == 2
        n = new_at[p]
        # Exactly the lexical smaller of the two undirected middle-chain orders.
        cycle = min(canonical((n, l1, middle[0], middle[1], l2)),
                    canonical((n, l1, middle[1], middle[0], l2)))
        b_cycles.append(cycle)
        for i, line in enumerate(cycle):
            u = flag_id[(p, line)]
            neighbours[u][1] = flag_id[(p, cycle[(i + 1) % 5])]
            neighbours[u][2] = flag_id[(p, cycle[(i - 1) % 5])]
    assert all(-1 not in row and len(set(row)) == 4 and u not in row for u, row in enumerate(neighbours))
    for u, row in enumerate(neighbours):
        for symbol, v in enumerate(row):
            assert neighbours[v][INVERSE[symbol]] == u
    edges = sorted({tuple(sorted((u, v))) for u, row in enumerate(neighbours) for v in row})
    assert len(edges) == 160
    # Explicit32 geometrical five-cycles. Every A-edge occurs in one; each
    # complementary four-step route has2A+2B and is therefore rank-good.
    five_cycles = []
    a_covered = set()
    for line, (p, q) in sorted(selected.items()):
        n = new_at[p]
        assert n == new_at[q]
        for r in sorted(set(blocks[line]) - {p, q}):
            cycle = [flag_id[(p, n)], flag_id[(q, n)], flag_id[(q, line)],
                     flag_id[(r, line)], flag_id[(p, line)]]
            assert len(set(cycle)) == 5
            for i in range(5):
                u, v = cycle[i], cycle[(i + 1) % 5]
                symbol = neighbours[u].index(v)
                if symbol in (0, 3):
                    a_covered.add(tuple(sorted((u, v))))
                    alternate = [cycle[(i - j) % 5] for j in range(5)]
                    word = tuple(neighbours[alternate[j]].index(alternate[j + 1]) for j in range(4))
                    assert word in good4 and sum(s in (0, 3) for s in word) == 2
            five_cycles.append(cycle)
    assert len(a_covered) == 80
    missing, category_counts = [], Counter()
    row_sizes = []
    for u in range(80):
        covered = {u}
        for word in reduced2 + good4:
            v = u
            for symbol in word:
                v = neighbours[v][symbol]
            covered.add(v)
        local = {u} | set(neighbours[u])
        for v in neighbours[u]:
            local.update(neighbours[v])
        assert local <= covered
        row_sizes.append(len(covered))
        missing.extend((u, v) for v in range(80) if v not in covered)
        category_counts["self_or_within_two_neighbour_steps"] += len(local)
    return {"n": 80, "m": 160, "degree": 4, "flags": flags,
            "inverse_labels": list(INVERSE), "neighbors_by_symbol": neighbours, "edges": edges,
            "new_block_A_cycles": new_cycles, "old_line_selected_opposites": selected,
            "all_A_cycles": a_cycles, "all_point_B_cycles": b_cycles,
            "rainbow_line_colours": sorted(selected), "geometric_five_cycles": five_cycles,
            "all80_A_edges_have_good_5cycle_alternatives": True,
            "all_self_adjacent_two_step_pairs_covered": True,
            "wide_route_missing_ordered_pairs": len(missing), "missing_pairs": missing,
            "wide_route_row_sizes": row_sizes, "minimum_row_coverage": min(row_sizes),
            "hit": not missing, "score_rule": "I union12 R2 pencil words union100 RG4 words"}


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
    began, wall = time.process_time(), time.monotonic()
    assert MUL[2][2] == 3 and MUL[2][3] == 1
    source = json.loads((SOURCE / "small_certificate.json").read_text())
    bad4 = {tuple("ABCD".index(c) for c in word) for word in source["exceptional_words"]}
    reduced2 = [w for w in product(range(4), repeat=2) if w[1] != INVERSE[w[0]]]
    reduced4 = [w for w in product(range(4), repeat=4)
                if all(w[i + 1] != INVERSE[w[i]] for i in range(3))]
    good4 = [w for w in reduced4 if w not in bad4]
    assert len(bad4) == 8 and len(good4) == 100 and len(reduced2) == 12
    assert all(sum(s in (0, 3) for s in w) in (1, 3) for w in bad4)
    old_lines = [sorted(4 * x + (MUL[slope][x] ^ intercept) for x in range(4))
                 for slope in range(4) for intercept in range(4)]
    assert all(sum(p in line for line in old_lines) == 4 for p in range(16))
    rows = []
    raw_cycles = 0
    for four in combinations(range(16), 4):
        a = four[0]
        for tail in permutations(four[1:]):
            if tail[0] > tail[-1]:
                continue
            raw_cycles += 1
            cycle = (a,) + tail
            colours = [colour(cycle[i], cycle[(i + 1) % 4]) for i in range(4)]
            if None in colours or len(set(colours)) != 4:
                continue
            pointmask = sum(1 << p for p in cycle)
            colourmask = sum(1 << c for c in colours)
            rows.append((cycle, tuple(colours), pointmask, colourmask))
    assert raw_cycles == 5460
    rows.sort()
    by_point = [[] for _ in range(16)]
    for i, row in enumerate(rows):
        for p in row[0]:
            by_point[p].append(i)
    solutions, nodes = [], 0
    search_start = time.process_time()
    timed_out = False

    def dfs(used_points, used_colours, chosen):
        nonlocal nodes, timed_out
        nodes += 1
        if len(solutions) == 8 or timed_out:
            return
        if nodes % 512 == 0 and time.process_time() - search_start >= 20:
            timed_out = True
            return
        if len(chosen) == 4:
            assert used_points == used_colours == 65535
            solutions.append(list(chosen))
            return
        p = next(p for p in range(16) if not (used_points >> p) & 1)
        for i in by_point[p]:
            _, _, pm, cm = rows[i]
            if pm & used_points or cm & used_colours:
                continue
            dfs(used_points | pm, used_colours | cm, chosen + [i])
            if len(solutions) == 8 or timed_out:
                return

    dfs(0, 0, [])
    exact = {"field": "F2[alpha]/(alpha^2+alpha+1), XOR addition", "point_encoding": "p=4*x+y",
             "retained_line_encoding": "line=4*slope+intercept, y=slope*x+intercept",
             "vertical_parallel_class_removed": [16, 17, 18, 19], "old_lines": old_lines,
             "all_undirected4cycles_before_filter": raw_cycles, "rainbow_cycle_rows": len(rows),
             "exact_cover_columns": 32, "rows_selected_per_solution": 4,
             "search_nodes": nodes, "search_CPU_seconds": time.process_time() - search_start,
             "solution_cap": 8, "solutions_found": len(solutions), "timed_out": timed_out,
             "solution_order": "lex canonical undirected cycles; recurse on least uncovered point",
             "complete_solution_space_enumerated": len(solutions) < 8 and not timed_out,
             "solutions": [{"row_indices": sol, "cycles": [rows[i][0] for i in sol],
                            "cycle_line_colours": [rows[i][1] for i in sol]} for sol in solutions]}
    (HERE / "exact_cover.json").write_text(json.dumps(exact, indent=2) + "\n")
    best, summaries, hit = None, [], False
    for index, solution in enumerate(solutions):
        graph = make_controller(solution, rows, old_lines, good4, reduced2)
        graph["exact_cover_solution_index"] = index
        (HERE / f"controller_{index}.json").write_text(json.dumps(graph, separators=(",", ":")) + "\n")
        summaries.append({"index": index, "missing_ordered_pairs": graph["wide_route_missing_ordered_pairs"],
                          "minimum_row_coverage": graph["minimum_row_coverage"], "hit": graph["hit"]})
        if best is None or graph["wide_route_missing_ordered_pairs"] < best["wide_route_missing_ordered_pairs"]:
            best = graph
        print(f"CONTROLLER {index} missing={graph['wide_route_missing_ordered_pairs']} min_row={graph['minimum_row_coverage']}", flush=True)
        if graph["hit"]:
            hit = True
            print(f"HIT_CONTROLLER controller_{index}.json", flush=True)
            break
    if best is not None:
        (HERE / "best.json").write_text(json.dumps(best, separators=(",", ":")) + "\n")
        (HERE / "best.edges").write_text("80 160\n" + "".join(f"{u} {v}\n" for u, v in best["edges"]))
        (HERE / "best.labels.json").write_text(json.dumps({"inverse": INVERSE, "neighbors_by_symbol": best["neighbors_by_symbol"]}, indent=2) + "\n")
    terminal = {
        "status": "WIDE_ROUTE_CONTROLLER_HIT" if hit else "PREFIX8_CONTROLLER_TRIAL_COMPLETE_NO_HIT" if len(solutions) == 8 else
                  "EXACT_COVER_TIME_LIMIT_PARTIAL_UNKNOWN" if timed_out else "ALL_EXACT_COVERS_EXHAUSTED_NO_HIT",
        "n": 80, "m": 160, "degree": 4, "exact_cover_solutions_found": len(solutions),
        "controllers_scored": len(summaries), "controllers": summaries,
        "best_missing_ordered_pairs": best["wide_route_missing_ordered_pairs"] if best else None,
        "best_controller_index": best["exact_cover_solution_index"] if best else None,
        "all_generated_graphs_simple_four_regular_inverse_labelled": True,
        "all_generated_self_adjacent_two_step_pairs_covered": True,
        "score": "I union12R2 union100RG4, all80 roots", "inverse_labels": INVERSE,
        "parallel_classes_attempted": 1, "B_cycle_order_profiles": 1, "orientation_profiles": 1,
        "CPU_seconds": time.process_time() - began, "wall_seconds": time.monotonic() - wall,
        "workers": 1, "CPU_hard_limit_seconds": 30, "BFS_performed": False,
        "large_lift_generated": False, "new_lower_bounds": 0, "pending": [],
    }
    (HERE / "terminal.json").write_text(json.dumps(terminal, indent=2) + "\n")
    print(json.dumps(terminal, indent=2), flush=True)


if __name__ == "__main__":
    main()

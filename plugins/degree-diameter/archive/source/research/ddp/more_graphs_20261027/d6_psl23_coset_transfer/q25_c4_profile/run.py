"""Exactly78 PSL2(F25)/C4 graphs of the recovered1518 source profile.
Implementation is prepared for root review before its first execution.
Standard library only; no oldq23 graph is loaded or checked.
"""
from collections import Counter, deque
from pathlib import Path
import json
import os
import resource
import time

OUT = Path(__file__).resolve().parent
N = 1950
TOTAL = 78
START = None
STATE = {"completed": 0, "scope": TOTAL, "stage": "not_started"}


class BudgetReached(Exception):
    pass


def cpu():
    return time.process_time() - START


def checkpoint():
    if cpu() > 88.0:
        raise BudgetReached()


def save(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


class PSL25:
    """Fixed F5[u]/(u²-2), encoded a+5b; no configurable field grid."""
    def __init__(self):
        self.neg = [(-x % 5) + 5 * (-(x // 5) % 5) for x in range(25)]
        self.add = [[(x % 5 + y % 5) % 5 + 5 * ((x // 5 + y // 5) % 5)
                     for y in range(25)] for x in range(25)]
        self.fm = [[((x % 5) * (y % 5) + 2 * (x // 5) * (y // 5)) % 5
                    + 5 * (((x % 5) * (y // 5) + (x // 5) * (y % 5)) % 5)
                    for y in range(25)] for x in range(25)]
        self.fi = [0] * 25
        for x in range(1, 25):
            a, b = x % 5, x // 5
            den = pow((a * a - 2 * b * b) % 5, -1, 5)
            self.fi[x] = (a * den) % 5 + 5 * ((-b * den) % 5)
            assert self.fm[x][self.fi[x]] == 1
        self.I = (1, 0, 0, 1)

    def canon(self, matrix):
        negative = tuple(self.neg[x] for x in matrix)
        return min(matrix, negative)

    def mul(self, x, y):
        a, b, c, d = x
        e, f, g, h = y
        A, M = self.add, self.fm
        return self.canon((A[M[a][e]][M[b][g]], A[M[a][f]][M[b][h]],
                           A[M[c][e]][M[d][g]], A[M[c][f]][M[d][h]]))

    def inv(self, matrix):
        a, b, c, d = matrix
        return self.canon((d, self.neg[b], self.neg[c], a))

    def power(self, matrix, exponent):
        value = self.I
        while exponent:
            if exponent & 1:
                value = self.mul(value, matrix)
            matrix = self.mul(matrix, matrix)
            exponent //= 2
        return value

    def fpow(self, x, exponent):
        value = 1
        while exponent:
            if exponent & 1:
                value = self.fm[value][x]
            x = self.fm[x][x]
            exponent //= 2
        return value

    def elements(self):
        result = set()
        for a in range(25):
            checkpoint()
            for c in range(25):
                if not a and not c:
                    continue
                if a:
                    for b in range(25):
                        d = self.fm[self.add[1][self.fm[b][c]]][self.fi[a]]
                        result.add(self.canon((a, b, c, d)))
                else:
                    b = self.neg[self.fi[c]]
                    for d in range(25):
                        result.add(self.canon((0, b, c, d)))
        group = sorted(result)
        group.remove(self.I)
        group.insert(0, self.I)
        assert len(group) == 7800
        return group


def prepare():
    STATE["stage"] = "preparing_fixed_group"
    group = PSL25()
    G = group.elements()
    index = {g: j for j, g in enumerate(G)}
    g = next(x for x in range(1, 25) if group.fpow(x, 24) == 1
             and group.fpow(x, 12) != 1 and group.fpow(x, 8) != 1)
    r = group.canon((g, 0, 0, group.fi[g]))
    W = group.canon((0, group.neg[1], 1, 0))
    assert group.power(r, 12) == group.I
    assert group.power(r, 6) != group.I and group.power(r, 4) != group.I
    H = [group.power(r, 3 * j) for j in range(4)]
    Hinv = [group.inv(h) for h in H]
    normalizer = {group.power(r, j) for j in range(12)}
    normalizer |= {group.mul(group.power(r, j), W) for j in range(12)}
    assert len(set(H)) == 4 and len(normalizer) == 24
    assert group.mul(group.mul(W, r), group.inv(W)) == group.inv(r)
    assert all({group.mul(group.mul(n, h), group.inv(n)) for h in H} == set(H)
               for n in normalizer)

    # Right cosets xH; the action below is left matrix multiplication.
    lookup = [-1] * len(G)
    reps = []
    for x in G:
        if lookup[index[x]] >= 0:
            continue
        j = len(reps)
        members = {index[group.mul(x, h)] for h in H}
        assert len(members) == 4 and all(lookup[z] < 0 for z in members)
        reps.append(x)
        for z in members:
            lookup[z] = j
    assert len(reps) == N and all(z >= 0 for z in lookup)

    U1 = (1, 1, 0, 1)
    Uu = (1, 5, 0, 1)
    generators = [U1, Uu, W]
    generated = {group.I}
    todo = [group.I]
    while todo:
        if len(generated) % 512 == 0:
            checkpoint()
        x = todo.pop()
        for s in generators:
            y = group.mul(s, x)
            if y not in generated:
                generated.add(y)
                todo.append(y)
    assert len(generated) == 7800
    perms = [[lookup[index[group.mul(s, x)]] for x in reps] for s in generators]
    assert all(sorted(p) == list(range(N)) for p in perms)

    reflections = [group.mul(group.power(r, j), W) for j in range(3)]
    root_reflections = [lookup[index[x]] for x in reflections]
    assert len(set(root_reflections)) == 3 and 0 not in root_reflections
    for x in reflections:
        assert group.mul(x, x) == group.I
        assert len({lookup[index[group.mul(h, x)]] for h in H}) == 1
    # All three unordered two-matching choices are equivalent under N conjugation.
    matching_pair_images = set()
    for n in normalizer:
        ni = group.inv(n)
        pair = tuple(sorted(lookup[index[group.mul(group.mul(n, s), ni)]]
                            for s in reflections[:2]))
        matching_pair_images.add(pair)
    assert len(matching_pair_images) == 3

    involutions = {x for x in G[1:] if group.mul(x, x) == group.I}
    invol_N = involutions & normalizer
    outside = involutions - normalizer
    assert len(involutions) == 325 and len(invol_N) == 13 and len(outside) == 312
    remaining = set(outside)
    choices = []
    neighbor_keys = set()
    while remaining:
        t = min(remaining)
        orbit = {group.mul(group.mul(h, t), hi) for h, hi in zip(H, Hinv)}
        assert len(orbit) == 4 and orbit <= outside
        assert orbit <= remaining
        remaining -= orbit
        neighbors = tuple(sorted({lookup[index[group.mul(h, t)]] for h in H}))
        assert len(neighbors) == 4 and 0 not in neighbors
        assert not set(neighbors) & set(root_reflections)
        assert neighbors not in neighbor_keys
        neighbor_keys.add(neighbors)
        choices.append({"id": "T" + str(len(choices)), "involution": t,
                        "H_conjugacy_class": sorted(orbit), "degree": 4,
                        "root_neighbor_set": neighbors,
                        "representative_pair": [0, lookup[index[t]]]})
    assert len(choices) == TOTAL
    matching_items = [{"id": "M" + str(j), "degree": 1,
                       "involution": reflections[j],
                       "representative_pair": [0, root_reflections[j]]}
                      for j in range(2)]
    inputs = {
        "field": "GF25=F5[u]/(u^2-2), code a+5b", "group_order": 7800,
        "canonicalization": "lexmin(M,-M)", "primitive_field_element": g,
        "torus_generator_order12": r, "H": H, "H_order": 4,
        "normalizer": sorted(normalizer), "normalizer_order": 24,
        "right_coset_count": N, "right_coset_representatives": reps,
        "permutation_generators": generators, "generated_group_order_verified": len(generated),
        "total_involutions": 325, "normalizer_involutions": 13,
        "outside_involutions": 312, "all_degree1_matching_root_neighbors": root_reflections,
        "fixed_matching_items": matching_items,
        "two_matching_pairs_in_one_normalizer_orbit": len(matching_pair_images),
        "valence4_items": choices, "total_normalized_source_profile_cases": TOTAL,
        "scope": "Exactly one valence4 orbital plus fixed WH/rWH matchings; all outside involutions modulo H conjugacy; complete 4+1+1 up to N conjugation, not a graph-isomorphism quotient.",
        "source_profile_credit": "Rishabh Rajiv PSL2(23)/C4 source1518; actual stabilizer/profile recovered in ../source_recovery, not reexecuted here.",
        "target_Delta": 6, "target_D": 5, "savedL": 1518,
        "source_q23_BFS": 0, "new_dependencies": False,
    }
    save("inputs.json", inputs)
    STATE["preparation_CPU_seconds"] = cpu()
    return {"perms": perms, "choices": choices, "matching_items": matching_items,
            "inputs": inputs, "cache": {}, "bits": [1 << v for v in range(N)]}


def orbital(item, prep):
    key = item["id"]
    if key in prep["cache"]:
        return prep["cache"][key]
    a, b = item["representative_pair"]
    start = min(a, b) * N + max(a, b)
    seen = {start}
    todo = [start]
    popped = 0
    while todo:
        if popped % 512 == 0:
            checkpoint()
        a, b = divmod(todo.pop(), N)
        popped += 1
        for p in prep["perms"]:
            u, v = p[a], p[b]
            if u > v:
                u, v = v, u
            code = u * N + v
            if code not in seen:
                seen.add(code)
                todo.append(code)
    codes = sorted(seen)
    masks = [0] * N
    for code in codes:
        a, b = divmod(code, N)
        assert a != b
        masks[a] |= prep["bits"][b]
        masks[b] |= prep["bits"][a]
    degree = item["degree"]
    assert len(codes) == N * degree // 2
    assert all(row.bit_count() == degree for row in masks)
    prep["cache"][key] = (masks, codes)
    return masks, codes


def reachable_R5(masks):
    reached = frontier = 1
    for depth in range(5):
        checkpoint()
        nxt = 0
        while frontier:
            bit = frontier & -frontier
            frontier -= bit
            nxt |= masks[bit.bit_length() - 1]
        frontier = nxt & ~reached
        reached |= frontier
    return reached


def calibrate_first(codes, reached, params):
    began = cpu()
    adj = [[] for _ in range(N)]
    for code in codes:
        a, b = divmod(code, N)
        adj[a].append(b)
        adj[b].append(a)
    assert len(codes) == 5850 and all(len(row) == len(set(row)) == 6 for row in adj)
    distances = [-1] * N
    distances[0] = 0
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if distances[v] < 0:
                distances[v] = distances[u] + 1
                queue.append(v)
    ordinary_R5 = sum(1 << v for v, d in enumerate(distances) if 0 <= d <= 5)
    assert ordinary_R5 == reached
    save("first_calibration.json", {
        "formal_case_index": 0, "parameters": params, "graph_n": N,
        "graph_m": 5850, "simple_degree6": True,
        "ordinary_BFS_roots": 1, "ordinary_distances": distances,
        "complete_R5_bitset_match": True, "formal_score_reused": True,
        "first_root_missing_states": N - reached.bit_count(),
        "first_root_eccentricity_if_connected": max(distances) if -1 not in distances else None,
        "calibration_CPU_seconds": cpu() - began,
        "scope": "Only the first formal graph; no all-source BFS or old source revalidation.",
    })


def export_hit(prep, item, codes, case_index):
    ordered = sorted(codes)
    assert len(ordered) == len(set(ordered)) == 5850
    (OUT / "candidate1950.edges").write_text(
        f"{N} {len(ordered)}\n" + "".join(f"{code // N} {code % N}\n" for code in ordered))
    inp = prep["inputs"]
    save("parameters.json", {
        "status": "PRODUCER_R5_FULL_PENDING_ROOT_INDEPENDENT_CHECK",
        "n": N, "m": 5850, "maximum_degree": 6, "target_D": 5,
        "savedL": 1518, "case_index": case_index,
        "field": inp["field"], "canonicalization": inp["canonicalization"],
        "primitive_field_element": inp["primitive_field_element"],
        "r": inp["torus_generator_order12"], "H": inp["H"],
        "coset_ordering": "Identity first, then lex-sorted canonical PSL matrices; first unseen right xH.",
        "fixed_matching_involutions": [x["involution"] for x in prep["matching_items"]],
        "valence4_involution": item["involution"],
        "identity_root_R5_covered": N,
        "diameter_argument": "Left G transitivity makes R5 full at one root sufficient; n1950>Moore6,4=937 forces exact5 once construction is independently accepted.",
        "edgefile": "candidate1950.edges", "source_q23_BFS": 0,
        "pending": ["root-independent-new-parameter-check"],
    })


def run():
    global START
    if (OUT / "terminal.json").exists():
        raise SystemExit("Existing terminal result; this fixed scope is not automatically rerun.")
    START = time.process_time()
    resource.setrlimit(resource.RLIMIT_CPU, (89, 90))
    save("run.json", {"running": True, "pid": os.getpid(), "scope": TOTAL,
                      "stage": "preparing_fixed_q25_C4", "completed": 0})
    prep = prepare()
    base_masks = [0] * N
    base_codes = []
    for item in prep["matching_items"]:
        masks, codes = orbital(item, prep)
        base_masks = [a | b for a, b in zip(base_masks, masks)]
        base_codes += codes
    assert len(base_codes) == 1950 and len(set(base_codes)) == 1950
    assert all(row.bit_count() == 2 for row in base_masks)
    preparation_CPU = cpu()
    STATE.update(stage="formal_profile", preparation_CPU_seconds=preparation_CPU)
    save("prepare.json", {"status": "READY_78_CASES", "group_order": 7800,
                          "cosets": N, "valence4_orbitals": TOTAL,
                          "fixed_valence1_matchings": 2,
                          "full_scope": TOTAL, "preparation_CPU_seconds": preparation_CPU})
    profile_start = cpu()
    hit = False
    forecast_stopped = False
    results = []
    with (OUT / "cases.jsonl").open("w") as log:
        for j, item in enumerate(prep["choices"]):
            checkpoint()
            started = cpu()
            masks4, codes4 = orbital(item, prep)
            masks = [a | b for a, b in zip(base_masks, masks4)]
            assert all(row.bit_count() == 6 for row in masks)
            codes = base_codes + codes4
            assert len(codes) == 5850
            reached = reachable_R5(masks)
            parameters = {"fixed_matching_ids": ["M0", "M1"],
                          "valence4_id": item["id"], "involution": item["involution"]}
            if j == 0:
                calibrate_first(codes, reached, parameters)
            row = {"case_index": j, "parameters": parameters,
                   "identity_root_reached_R5": reached.bit_count(),
                   "identity_root_missing_states": N - reached.bit_count(),
                   "full_hit": reached.bit_count() == N,
                   "evaluation_CPU_seconds": cpu() - started}
            results.append(row)
            log.write(json.dumps(row) + "\n")
            log.flush()
            STATE["completed"] = len(results)
            if row["full_hit"]:
                hit = True
                export_hit(prep, item, codes, j)
                print("HIT", j, item["involution"], "1950 / degree6 / D<=5", flush=True)
                break
            if len(results) == 8:
                profile_CPU = cpu() - profile_start
                forecast = preparation_CPU + profile_CPU * TOTAL / 8
                admit = forecast <= 88.0
                save("profile8.json", {
                    "completed_once": 8, "profile_replayed": False,
                    "preparation_CPU_seconds": preparation_CPU,
                    "first8_profile_CPU_seconds": profile_CPU,
                    "projected_full78_CPU_seconds": forecast,
                    "remaining_cases": TOTAL - 8, "admit_remaining": admit,
                    "CPU_budget_seconds": 90,
                })
                print("PROFILE8", "projected_CPU", forecast, "admit_remaining", admit, flush=True)
                if not admit:
                    forecast_stopped = True
                    break
            if len(results) % 8 == 0:
                save("progress.json", {"running": True, "completed": len(results),
                                       "scope": TOTAL, "CPU_seconds": cpu()})
    complete = len(results) == TOTAL
    status = ("PRODUCER_FULL_HIT_PENDING_ROOT" if hit else
              "PROFILE8_ONLY_REMAINING_SCOPE_UNKNOWN" if forecast_stopped else
              "COMPLETE_78_NORMALIZED_SOURCE_PROFILE_NO_D5")
    terminal = {
        "status": status, "running": False, "target_Delta": 6, "target_D": 5,
        "savedL": 1518, "n": {"actual": N if hit else None, "hypothetical": N},
        "actual_D": None, "ordinary_bad_unordered_pairs": None,
        "finite_scope": TOTAL, "completed_cases": len(results),
        "scope_exhausted": complete, "stopped_at_first_hit": hit,
        "first8_replayed": False, "new_q25_graphs_evaluated": len(results),
        "complete_hits": int(hit), "source_q23_BFS": 0,
        "first_formal_ordinary_root_BFS": 1 if results else 0,
        "all_source_BFS": 0, "preparation_CPU_seconds": preparation_CPU,
        "total_CPU_seconds": cpu(), "CPU_budget_seconds": 90, "workers": 1,
        "pending": ["root-independent-new-parameter-check"] if hit else [],
        "scope": "Only fixed PSL2(F25)/torusC4 and source4+1+1 profile, normalized to WH/rWH. Not other subgroups, fields, degrees or arbitrary1950graphs.",
    }
    save("RESULT.json", terminal)
    save("terminal.json", terminal)
    save("run.json", terminal)
    print(json.dumps(terminal), flush=True)


if __name__ == "__main__":
    try:
        run()
    except BudgetReached:
        terminal = {"status": "PARTIAL_PREFIX_CPU_BUDGET_REACHED", "running": False,
                    "target_Delta": 6, "target_D": 5, "savedL": 1518,
                    "n": {"actual": None, "hypothetical": N}, "actual_D": None,
                    "ordinary_bad_unordered_pairs": None, "finite_scope": TOTAL,
                    "completed_cases": STATE["completed"], "scope_exhausted": False,
                    "stage": STATE["stage"], "total_CPU_seconds": cpu(),
                    "CPU_budget_seconds": 90, "source_q23_BFS": 0,
                    "all_source_BFS": 0, "pending": [],
                    "decision": "No automatic extension or restart; remaining scope unresolved."}
        save("RESULT.json", terminal)
        save("terminal.json", terminal)
        save("run.json", terminal)
        print(json.dumps(terminal), flush=True)

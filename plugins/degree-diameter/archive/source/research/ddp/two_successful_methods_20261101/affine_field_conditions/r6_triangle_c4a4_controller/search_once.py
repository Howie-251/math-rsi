#!/usr/bin/env python3
"""One predeclared C4 x A4 controller family; no fibre construction or BFS."""
import itertools
import json
from pathlib import Path
import resource
import time

OUT = Path(__file__).resolve().parent
START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (5, 5))


def write(name, obj):
    (OUT / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def parity(p):
    return sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) % 2


perms = [p for p in itertools.permutations(range(4)) if parity(p) == 0]
idx = {p: i for i, p in enumerate(perms)}
compose = [[idx[tuple(p[q[i]] for i in range(4))] for q in perms] for p in perms]
invp = [next(j for j in range(12) if compose[i][j] == 0 and compose[j][i] == 0)
        for i in range(12)]
mul = [[12 * ((g // 12 + h // 12) % 4) + compose[g % 12][h % 12]
        for h in range(48)] for g in range(48)]
inv = [12 * ((-(g // 12)) % 4) + invp[g % 12] for g in range(48)]
assert all(mul[g][inv[g]] == mul[inv[g]][g] == 0 for g in range(48))
a = idx[(1, 0, 3, 2)]
c = idx[(1, 2, 0, 3)]
vs = [i for i, p in enumerate(perms) if p in
      [(0, 1, 2, 3), (1, 0, 3, 2), (2, 3, 0, 1), (3, 2, 1, 0)]]
assert len(vs) == 4


def product(*sets):
    r = {0}
    for s in sets:
        r = {mul[x][y] for x in r for y in s}
    return r


def formulas(b, s):
    si = [inv[x] for x in s]
    aa = {a} | product([a], s, si) | product(s, si, [a]) | product(s, [b], si)
    bb = {b} | product([b], si, s) | product(si, s, [b]) | product(si, [a], s)
    ab = set(s) | product([a], s, [b]) | product(s, si, s)
    ba = set(si) | product([b], si, [a]) | product(si, s, si)
    return [aa | {48 + x for x in ab}, ba | {48 + x for x in bb}]


def port_table(b, s):
    si = [inv[x] for x in s]
    return [[mul[g][a]] + [48 + mul[g][x] for x in s] for g in range(48)] + \
           [[48 + mul[g][b]] + [mul[g][x] for x in si] for g in range(48)]


def check_table(nb):
    assert len(nb) == 96
    assert all(len(set(nb[x])) == 6 and x not in nb[x] for x in range(96))
    assert all(nb[nb[x][p]][p] == x for x in range(96) for p in range(6))
    # The explicit triangle A_g -- A_ga -- B_g -- A_g covers both types.
    assert all(mul[g][a] in nb[g] and 48 + g in nb[g] and
               48 + g in nb[mul[g][a]] for g in range(48))


def root_walks(nb, root):
    witnesses, nbwitnesses = {}, {}
    for p, q, r in itertools.product(range(6), repeat=3):
        end = nb[nb[nb[root][p]][q]][r]
        witnesses.setdefault(end, [p, q, r])
        if p != q and q != r:
            nbwitnesses.setdefault(end, [p, q, r])
    assert len(witnesses) <= 96
    # A backtracking three-walk ends at an adjacent vertex. The direct check
    # confirms this on each literal neighbour table, including root-to-self.
    required = set(range(96)) - set(nb[root])
    assert required & witnesses.keys() <= nbwitnesses.keys()
    return witnesses, nbwitnesses


def label(vertex):
    g = vertex % 48
    return {"id": vertex, "type": "AB"[vertex // 48], "c4": g // 12,
            "a4_images": [x + 1 for x in perms[g % 12]]}


trials = []
success = None
for v, t, u in itertools.product(vs, range(12), range(12)):
    b = 24 + v
    s = [0, a, c, 12 + t, 24 + u]
    nb = port_table(b, s)
    check_table(nb)
    roots = [root_walks(nb, root) for root in (0, 48)]
    formula_sets = formulas(b, s)
    assert all(set(roots[k][0]) == formula_sets[k] for k in range(2))
    missing = [[x for x in range(96) if x not in roots[k][0]] for k in range(2)]
    nb_missing = [[x for x in range(96) if x not in nb[root]
                   and x not in roots[k][1]] for k, root in enumerate((0, 48))]
    record = {"trial": len(trials) + 1, "v_index": v, "t_index": t, "u_index": u,
              "threewalk_covered": [len(x[0]) for x in roots],
              "NB3_covered": [len(x[1]) for x in roots],
              "threewalk_missing_count": list(map(len, missing)),
              "required_NB3_missing_count": list(map(len, nb_missing)),
              "first_missing": [x[0] if x else None for x in missing]}
    trials.append(record)
    if not any(missing):
        assert not any(nb_missing)
        success = record
        parameters = {"group": "C4 x A4", "composition": "p o q(i)=p(q(i))",
                      "point_numbering": "type*48+c4*12+lex_even_permutation_index",
                      "A4_lex_images_1based": [[x + 1 for x in p] for p in perms],
                      "a_group_id": a, "b_group_id": b, "S_group_ids_in_port_order": s,
                      "v": [x + 1 for x in perms[v]], "t": [x + 1 for x in perms[t]],
                      "u": [x + 1 for x in perms[u]], "first_success_trial": len(trials),
                      "vertices": [label(x) for x in range(96)],
                      "predicted_fibre_order_only": 96 * 729,
                      "fibre_graph_generated": False}
        write("PARAMETERS.json", parameters)
        write("PORT_TABLE.json", {"rows": nb, "ports": list(range(6))})
        edges = [[x, y, p] for x in range(96) for p, y in enumerate(nb[x]) if x < y]
        assert len(edges) == 288
        write("EDGES.json", {"edge_columns": ["u", "v", "port"], "edges": edges})
        wit = []
        for k, root in enumerate((0, 48)):
            for target in range(96):
                ports = roots[k][1].get(target, roots[k][0][target])
                path = [root]
                for p in ports:
                    path.append(nb[path[-1]][p])
                assert path[-1] == target
                is_nb = ports[0] != ports[1] and ports[1] != ports[2]
                assert target in nb[root] or is_nb
                wit.append({"root": root, "target": target, "ports": ports,
                            "vertices": path, "nonbacktracking": is_nb})
        assert len(wit) == 192
        write("WITNESSES.json", {"roots": [0, 48], "witnesses": wit})
        break

write("TRIALS.json", {"columns_note": "counts refer only to two deck roots, not ordinary allpair bad counts",
                      "trials": trials})
cpu = time.process_time() - START
result = {"status": "PASS_CONTROLLER" if success else "FIXED_FAMILY_EXCLUDED",
          "tested": len(trials), "predeclared_total": 576,
          "success": success, "cpu_seconds_search_including_output_before_result": cpu,
          "compile_cpu_seconds": 0, "worker_count": 1,
          "budget_cpu_seconds": 5, "unvisited": 576 - len(trials),
          "literal_ports_checked_each_trial": True,
          "actual_walks_each_trial": 2 * 216,
          "formula_crosscheck_each_trial": True,
          "triangles_cover_all_vertices_each_trial": True,
          "BFS_runs": 0, "fibre_graph_generated": False,
          "accepted_graph_count_increment": 0}
if not success:
    assert len(trials) == 576
    result["max_two_root_threewalk_covered_sum"] = max(sum(x["threewalk_covered"]) for x in trials)
write("RESULT.json", result)
print(json.dumps(result, ensure_ascii=False))

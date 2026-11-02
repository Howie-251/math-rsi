#!/usr/bin/env python3
"""One bounded binding of saved Petersen words to two parity graphs; no BFS."""
import json
import os
from pathlib import Path
import resource
import time
import traceback

START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (1, 1))
HERE = Path(__file__).resolve().parent
PRIOR = 3.495753483
OTHER_NEW = 0.063725055
PREPARATION = 0.10

def write(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2) + "\n")

def canonical_cycle(cycle):
    seqs = []
    for c in (cycle, list(reversed(cycle))):
        seqs.extend(tuple(c[i:] + c[:i]) for i in range(len(c)))
    return min(seqs)

def edges_of(c):
    return {tuple(sorted((c[i], c[(i + 1) % len(c)]))) for i in range(len(c))}

def determinant(matrix):
    a = [row[:] for row in matrix]
    sign, prev = 1, 1
    for k in range(len(a) - 1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k + 1, len(a)) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k + 1, len(a)):
            for j in range(k + 1, len(a)):
                numerator = a[i][j] * p - a[i][k] * a[k][j]
                assert numerator % prev == 0
                a[i][j] = numerator // prev
            a[i][k] = 0
        prev = p
    return sign * a[-1][-1]

write("STRUCTURE_HANDLE.json", {
    "status": "RUNNING", "pid": os.getpid(), "single_worker": True,
    "wholecase_cap_CPU_seconds": 5, "prior_CPU_seconds": PRIOR,
    "root_and_paper_postprocess_CPU_seconds": OTHER_NEW,
    "new_preparation_charge_CPU_seconds": PREPARATION,
    "new_process_hard_CPU_seconds": 1,
    "stage": "binding saved words to signature21/62 H20 graphs"
})

results = []
try:
    inp = json.loads((HERE / "INPUT_AND_TREE_GAUGE.json").read_text())
    saved = json.loads((HERE / "ALL_NB_WORDS_AND_INTEGER_FORMS.json").read_text())
    base_edges = [tuple(e) for e in inp["edges"]]
    chords = [tuple(e) for e in saved["oriented_cotree_edges"]]
    words = saved["words"]
    for signature in (21, 62):
        out = HERE / f"signature{signature}"
        out.mkdir(exist_ok=True)
        bits = [(signature >> i) & 1 for i in range(6)]
        parity = {e: (bits[chords.index(e)] if e in chords else 0) for e in base_edges}
        h_edges = sorted({tuple(sorted((2*u+p, 2*v+(p ^ parity[(u, v)]))))
                          for u, v in base_edges for p in (0, 1)})
        h_set = set(h_edges)
        assert len(h_edges) == 30
        assert all(sum(v in e for e in h_edges) == 3 for v in range(20))
        (out / "H20.edges").write_text("20 30\n" + "".join(f"{u} {v}\n" for u, v in h_edges))
        root_bindings = []
        all_faces = set()
        for h_root in range(20):
            u, sheet0 = divmod(h_root, 2)
            closed = [w for w in words if w["root"] == u and w["target"] == u
                      and sum(a*b for a, b in zip(w["integer_coefficients"], bits)) % 2 == 0]
            assert len(closed) == 7, (signature, h_root, "closed-count", len(closed))
            bindings = []
            for w in closed:
                sheet = sheet0
                lifted = [h_root]
                for a, b in zip(w["vertices"], w["vertices"][1:]):
                    sheet ^= parity[tuple(sorted((a, b)))]
                    lifted.append(2*b + sheet)
                assert lifted[-1] == h_root
                assert all(tuple(sorted(e)) in h_set for e in zip(lifted, lifted[1:]))
                face = None
                if w["length"]:
                    assert w["length"] == 5 and len(set(lifted[:-1])) == 5, (signature, w)
                    face = canonical_cycle(lifted[:-1])
                    all_faces.add(face)
                bindings.append({"saved_word_id": w["word_id"],
                                 "integer_coefficients": w["integer_coefficients"],
                                 "lifted_vertices": lifted, "face_vertices": face})
            assert sum(b["face_vertices"] is None for b in bindings) == 1
            assert len({b["face_vertices"] for b in bindings if b["face_vertices"] is not None}) == 3
            root_bindings.append({"vertex": h_root, "return_words": bindings})
        faces = sorted(all_faces)
        assert len(faces) == 12, (signature, "face-count", len(faces))
        face_ids = {f: i for i, f in enumerate(faces)}
        face_edges = [edges_of(f) for f in faces]
        edge_faces = {e: [i for i, es in enumerate(face_edges) if e in es] for e in h_edges}
        assert all(len(fs) == 2 for fs in edge_faces.values())
        assert all(sum(v in f for f in faces) == 3 for v in range(20))
        for rb in root_bindings:
            for binding in rb["return_words"]:
                f = binding.pop("face_vertices")
                binding["face_id"] = None if f is None else face_ids[f]
            ids = [b["face_id"] for b in rb["return_words"] if b["face_id"] is not None]
            assert all(ids.count(i) == 2 for i in set(ids))
        face_data = {"signature": signature, "cotree_bits": bits,
                     "vertex_rule": "2*base_vertex+sheet", "faces": [
                         {"face_id": i, "vertices": list(f), "edges": sorted(face_edges[i])}
                         for i, f in enumerate(faces)],
                     "pervertex_saved_return_bindings": root_bindings,
                     "edge_face_incidence": [{"edge": e, "face_ids": edge_faces[e]} for e in h_edges]}
        (out / "FACES_AND_RETURNS.json").write_text(json.dumps(face_data, indent=2) + "\n")
        central = faces[0]
        central_edges = [tuple(sorted((central[i], central[(i+1) % 5]))) for i in range(5)]
        rim = [next(f for f in edge_faces[e] if f != 0) for e in central_edges]
        assert len(set(rim)) == 5
        rim_shared = []
        for i in range(5):
            shared = face_edges[rim[i]] & face_edges[rim[(i+1) % 5]]
            assert len(shared) == 1
            rim_shared.append(sorted(shared)[0])
        assert all(not (face_edges[rim[i]] & face_edges[rim[j]])
                   for i in range(5) for j in range(i+1, 5) if (j-i) not in (1, 4))
        wheel = {"signature": signature, "central_face_id": 0, "central_vertices": central,
                 "rim_face_ids_in_cyclic_order": rim, "central_rim_shared_edges": central_edges,
                 "consecutive_rim_shared_edges": rim_shared,
                 "nonconsecutive_rim_pairs_share_no_edge": True}
        (out / "ODD_WHEEL.json").write_text(json.dumps(wheel, indent=2) + "\n")
        # Deterministic tree selection and exact integer minor, no graph distances.
        parent = list(range(20))
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        tree, cotree = [], []
        for a, b in h_edges:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
                tree.append((a, b))
            else:
                cotree.append((a, b))
        assert len(tree) == 19 and len(cotree) == 11
        cycle_rows = []
        for face in faces:
            row = [0] * 11
            for a, b in zip(face, face[1:] + face[:1]):
                e = tuple(sorted((a, b)))
                if e in cotree:
                    row[cotree.index(e)] += 1 if a < b else -1
            cycle_rows.append(row)
        det = determinant(cycle_rows[:11])
        minor = {"signature": signature, "tree_edges": tree, "oriented_cotree_edges": cotree,
                 "all_twelve_face_cycle_rows": cycle_rows, "selected_face_ids": list(range(11)),
                 "determinant_exact_integer": det,
                 "integer_cycle_lattice_generated_by_selected_faces": abs(det) == 1}
        (out / "FACE_CYCLE_MINOR.json").write_text(json.dumps(minor, indent=2) + "\n")
        results.append({"signature": signature, "vertices": 20, "edges": 30, "faces": 12,
                        "closed_le6_words_each_vertex": 7, "nonempty_return_length": 5,
                        "faces_each_vertex": 3, "faces_each_edge": 2,
                        "wheel_central_face_id": 0, "wheel_rim_face_ids": rim,
                        "integer_minor_determinant": det,
                        "status": "STRUCTURE_PREDICTIONS_PASS"})
    status = "PASS_BOTH_SAVED_WORD_STRUCTURES_AND_EXPLICIT_ODD_WHEELS"
    error = None
except Exception as exc:
    status = "STRUCTURE_PREDICTION_COUNTEREXAMPLE_OR_ERROR"
    error = {"type": type(exc).__name__, "message": str(exc), "traceback": traceback.format_exc()}

actual = time.process_time() - START
total = PRIOR + OTHER_NEW + PREPARATION + actual
result = {"status": status, "results": results, "error": error,
          "scope": "Only signatures21/62 saved-word parity lifts; no C7 assignments or candidate graph",
          "old_words_regenerated": 0, "old_signatures_reevaluated": 0, "graph_BFS_roots": 0,
          "C7_assignments_tested": 0, "new_graph_results": 0,
          "prior_wholecase_CPU_seconds": PRIOR, "other_root_and_paper_CPU_seconds": OTHER_NEW,
          "new_preparation_charge_CPU_seconds": PREPARATION,
          "actual_structure_process_CPU_seconds": actual, "wholecase_CPU_seconds": total,
          "wholecase_CPU_cap_seconds": 5}
write("STRUCTURE_RESULT.json", result)
write("STRUCTURE_TERMINAL.json", {**result, "active_processes": 0, "terminal": True,
                                  "next": "Independent paper owner connects actual face structure to voltage obstruction"})
write("STRUCTURE_HANDLE.json", {"status": status, "pid": os.getpid(), "terminal": True,
                               "active_processes": 0, "wholecase_CPU_seconds": total})
print(json.dumps(result))

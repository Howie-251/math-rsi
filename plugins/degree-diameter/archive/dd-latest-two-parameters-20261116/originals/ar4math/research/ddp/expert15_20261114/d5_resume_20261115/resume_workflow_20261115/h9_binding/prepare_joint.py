"""Reproduce the fixed-S potential-pin gate and SAT-ready actual-label inputs.

Only reads already bound graph/classes/plane maps. No colors are searched,
no graph modified, and no incidence/BFS/SAT/hash operation is called.
"""
from collections import Counter
import json
import lzma
from pathlib import Path
import time

OUT = Path(__file__).resolve().parent
ROOT = next(p for p in OUT.parents if p.name == "ar4math")


def main():
    start = time.process_time()
    old = ROOT / "research/ddp/more_graphs_20261027"
    run = ROOT / "research/ddp/expert15_20261114/d5_resume_20261115"
    classes = json.loads((old / "h9_other_degrees/fold11_classes.json").read_text())
    cls = classes["classes"]
    split = set(classes["split_fold_ids"])
    pin_fiber = {p: f for f in split for p in cls[f]}
    color = {r["fold"]: r["color"] for r in classes["split_color_parity"]}
    source = old / "h9_d11_followups/graph_d11_D5_n37631.edges"
    external = [0] * 37471
    with source.open() as f:
        n, m = map(int, next(f).split())
        assert (n, m) == (37631, 205329)
        for line in f:
            a, b = map(int, line.split())
            if (a < 37471) != (b < 37471):
                external[min(a, b)] += 1
    degrees = (old / "accepted_d11_d12_full_neighborhood_clones/source_degrees_d11.u8.bin").read_bytes()
    assert len(degrees) == n
    edges = []
    same_count = Counter()
    qpath = ROOT / "research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/duality_source/graph_d10k5_n33397.edges.xz"
    with lzma.open(qpath, "rt") as f:
        assert tuple(map(int, next(f).split())) == (33397, 166425)
        for line in f:
            a, b = map(int, line.split())
            if a in split and b in split:
                edges.append([a, b])
                if color[a] == color[b]:
                    same_count[a] += 1
                    same_count[b] += 1
    assert len(edges) == 6006 and len(split) == 4074
    fibers = []
    for f in sorted(split):
        ps = cls[f]
        bound = min(1 - external[p] for p in ps)
        assert bound in (0, 1) and same_count[f] <= bound
        assert all(degrees[p] == 10 + same_count[f] + external[p] for p in ps)
        fibers.append(dict(fold=f, actual_pins=ps, external_loads=[external[p] for p in ps],
                           same_edge_cap=bound, old_parity_color=color[f]))
    pg = json.loads((run / "d12_weighted_plane_cover/PG2_9_INCIDENCE.json").read_text())["line_point_indices"]
    rows = json.loads((run / "d11_weighted_plane_transfer/LINE_PROVIDER_TABLES.json").read_text())["planes"]

    def potential(p):
        return external[p] == 0 if p in pin_fiber else degrees[p] < 11

    candidates = []
    rejected = Counter()
    for row in rows:
        ps = row["actual_pin_ids91"]
        providers = [sorted({ps[j] for j in line if potential(ps[j])}) for line in pg]
        if any(not p for p in providers):
            rejected["immutable_empty_line"] += 1
            continue
        forced = sorted({p[0] for p in providers if len(p) == 1})
        if len(forced) > 11:
            rejected["forced_gt11"] += 1
            continue
        candidates.append(dict(plane_id=row["plane_global_id"], kind=row["kind"],
                               raw_point_ids91=row["raw_point_ids91"], actual_pin_ids91=ps,
                               line_potential_pin_providers=providers, forced_pin_ids=forced,
                               old_empty_line_indices=row["empty_line_indices"]))
    assert len(candidates) == 202
    data = dict(
        status="INPUT_ONLY_NO_COLOR_MODEL_OR_GRAPH",
        source=dict(path=str(source.relative_to(ROOT)), n=n, m=m, core_n=37471,
                    source_degree_file=str((old / "accepted_d11_d12_full_neighborhood_clones/source_degrees_d11.u8.bin").relative_to(ROOT))),
        labels="fiber IDs are original33397 quotient IDs; pin IDs are actual current37471 core IDs; never use generic-list indices as fiber IDs",
        color_scope="old_parity_color only recovers same/different; raw matching orientation not bound",
        split_fibers=fibers, split_edges=edges, plane_candidates=candidates,
        immutable_potential_pins=[dict(pin=p, current_degree=degrees[p], external_load=external[p])
                                  for p in range(37471) if p not in pin_fiber and degrees[p] < 11],
        rejected=dict(rejected),
        constraints=["One color bit per split fiber; same_edge iff endpoint colors equal.",
                     "At each fiber sum incident same_edge <= same_edge_cap.",
                     "For split pin x to be selected: external_load(x)=0 and all incident same_edge of its fiber are0.",
                     "Unsplit/H3 potential pins have fixed current_degree<11; colors do not modify that degree.",
                     "For the same selected plane, select at most11 distinct actual pin IDs and hit all91 provider rows.",
                     "A hit is only a core-certificate and degree necessary candidate; actual peripheral coverage and old160 roots are still untested."],
    )
    (OUT / "JOINT_INPUT.json").write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n")
    result = dict(status=data["status"], source_n=n, source_m=m, split_fibers=len(fibers),
                  split_edges=len(edges), candidates=len(candidates), excluded=dict(rejected),
                  same_edge_cap_histogram=dict(Counter(x["same_edge_cap"] for x in fibers)),
                  CPU_seconds=time.process_time() - start, BFS_calls=0, solver_calls=0,
                  new_graphs=0, color_assignments_generated=0)
    (OUT / "PREP_RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()

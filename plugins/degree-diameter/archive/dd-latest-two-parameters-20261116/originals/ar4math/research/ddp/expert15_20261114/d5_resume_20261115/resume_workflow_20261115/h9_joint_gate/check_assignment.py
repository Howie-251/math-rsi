"""Directly check a proposed color/pin gate against original graph and geometry.

Does not trust encoded capacities/providers, and does not claim actual-graph D5.
"""
from array import array
from collections import Counter
import json
import lzma
from pathlib import Path
import time

ROOT = next(p for p in Path(__file__).resolve().parents if p.name == "ar4math")


def check(candidate, output):
    start = time.process_time()
    old = ROOT / "research/ddp/more_graphs_20261027"
    run = ROOT / "research/ddp/expert15_20261114/d5_resume_20261115"
    data = json.loads((old / "h9_other_degrees/fold11_classes.json").read_text())
    classes, split = data["classes"], set(data["split_fold_ids"])
    color = {int(k): v for k, v in candidate["colors"].items()}
    assert set(color) == split and all(v in (0, 1) for v in color.values())
    pins = candidate["pins"]
    assert len(pins) == len(set(pins)) and len(pins) <= 11
    degrees, external = [0] * 37631, [0] * 37471
    with (old / "h9_d11_followups/graph_d11_D5_n37631.edges").open() as f:
        assert tuple(map(int, next(f).split())) == (37631, 205329)
        for line in f:
            a, b = map(int, line.split());degrees[a] += 1;degrees[b] += 1
            if (a < 37471) != (b < 37471):external[min(a, b)] += 1
    same = Counter()
    with lzma.open(ROOT / "research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/duality_source/graph_d10k5_n33397.edges.xz", "rt") as f:
        assert tuple(map(int, next(f).split())) == (33397, 166425)
        for line in f:
            a, b = map(int, line.split())
            if a in split and b in split and color[a] == color[b]:same[a] += 1;same[b] += 1
    newdegrees = degrees[:]
    for f in split:
        for p in classes[f]:newdegrees[p] = 10 + same[f] + external[p]
    assert all(0 <= p < 37471 for p in pins)
    before_hist = dict(sorted(Counter(newdegrees).items()))
    for p in pins:newdegrees[p] += 1
    assert max(newdegrees) <= 11
    fold = array("H");fold.frombytes((old / "h9_other_degrees/point_to_core11.u16.bin").read_bytes())
    plane_id = candidate["plane_id"]
    if plane_id < 364:
        records = json.loads((old / "h9_baer_plane_pool/planes.json").read_text())["records"]
        record = records[plane_id];raw_ids = record["point_ids91"]
    else:
        records = json.loads((old / "h9_baer_nonflat_F3_pool/nonflat_planes.json").read_text())["records"]
        record = records[plane_id - 364];raw_ids = record["Q9_point_ids91"]
    mapped = [fold[p] for p in raw_ids]
    assert set(pins) <= set(mapped), "selected core pins must belong to the chosen plane"
    lines = json.loads((run / "d12_weighted_plane_cover/PG2_9_INCIDENCE.json").read_text())["line_point_indices"]
    assert len(lines) == 91
    witnesses = [sorted(set(pins) & {mapped[j] for j in line}) for line in lines]
    assert all(witnesses)
    oldc = {x["fold"]: x["color"] for x in data["split_color_parity"]}
    result = dict(status="SAT_JOINT_DEGREE_AND_CORE_GATE_DIRECT_CHECK_PASS_NOT_GRAPH",
                  color_count=len(color), changed_parity_color_count=sum(color[f] != oldc[f] for f in split),
                  plane_id=plane_id, pins=pins, pin_count=len(pins), tail_slots=11-len(pins),
                  old_vertices_degree_model_checked=37631, maximum_degree_after_insertion=max(max(newdegrees), len(pins)),
                  degree_model_histogram_before_new_pin=before_hist, core_lines_checked=91,
                  actual_line_witnesses=witnesses, fully_checked_assignments=1,
                  geometry_orientation_bound=False, new_graphs=0, BFS_calls=0,
                  periphery_160_roots_checked=0, new_root_checked=False,
                  proof_scope="Degree formula and mapped91-line core certificate only; actual sigma incidence, full new-root coverage and all160 peripheral roots remain required.",
                  CPU_seconds=time.process_time()-start)
    (Path(output) / "CHECK_RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser();p.add_argument("candidate", type=Path);p.add_argument("output", type=Path)
    a = p.parse_args();print(json.dumps(check(json.loads(a.candidate.read_text()), a.output)))

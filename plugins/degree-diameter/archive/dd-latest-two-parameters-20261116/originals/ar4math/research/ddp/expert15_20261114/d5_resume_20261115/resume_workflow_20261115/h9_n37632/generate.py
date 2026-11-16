"""Reconstruct the 37632-vertex H9 graph from its fixed mathematical inputs.

The cached incidence is generated and bound by ../h9_exact_binding/build.cpp.
Colors are the accepted 105-fiber modification, not a fresh solver run.
All original exterior edges are retained; the core is reconstructed from sigma.
"""
import argparse
from array import array
import json
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent
WORK = HERE.parent
N = 66430
CORE = 37471
Z = 37631
ANCHOR = 31


def read_array(path, kind):
    values = array(kind)
    values.frombytes(path.read_bytes())
    return values


def generate(output):
    start = time.process_time()
    bound = WORK / "h9_exact_binding"
    tau = read_array(bound / "tau.i32.bin", "i")
    pi = read_array(bound / "pi.u16.bin", "H")
    lines = read_array(bound / "line_points.i32.bin", "i")
    candidate = json.loads((WORK / "h9_other_orientation/CANDIDATE.json").read_text())
    root = next(p for p in HERE.parents if p.name == "ar4math")
    classes = json.loads((root / "research/ddp/more_graphs_20261027/h9_other_degrees/fold11_classes.json").read_text())
    inverse = [0] * (2 * N)
    for u, v in enumerate(tau):
        inverse[v] = u
    eps = bytearray(N)
    for fold in classes["split_fold_ids"]:
        p = classes["point_representatives"][fold]
        eps[p] = eps[tau[tau[p]]] = candidate["colors"][str(fold)]
    edges = set()
    for p in range(N):
        line = tau[p] if eps[p] else inverse[p]
        for q in lines[10 * (line - N):10 * (line - N + 1)]:
            if p == q:
                continue
            u, v = pi[p], pi[q]
            assert u != v
            edges.add((min(u, v), max(u, v)))
    assert len(edges) == 203747
    outside = set()
    with (bound / "source.edges").open() as source:
        assert tuple(map(int, next(source).split())) == (37631, 205329)
        count = 0
        for row in source:
            u, v = map(int, row.split())
            count += 1
            if max(u, v) >= CORE:
                outside.add((min(u, v), max(u, v)))
        assert count == 205329 and len(outside) == 1608
    edges.update(outside)
    pins = sorted(candidate["pins"] + [ANCHOR])
    assert len(pins) == len(set(pins)) == 11
    edges.update((p, Z) for p in pins)
    degrees = [0] * (Z + 1)
    for u, v in edges:
        degrees[u] += 1
        degrees[v] += 1
    assert len(edges) == 205366 and max(degrees) == 11
    assert degrees[Z] == 11
    with output.open("w") as target:
        target.write(f"{Z + 1} {len(edges)}\n")
        for u, v in sorted(edges):
            target.write(f"{u} {v}\n")
    return dict(status="GENERATED_NOT_DISTANCE_VERIFIED", n=Z + 1, m=len(edges),
                maximum_degree=max(degrees), new_pins=pins, anchor=ANCHOR,
                CPU_seconds=time.process_time() - start)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    print(json.dumps(generate(arguments.output)))

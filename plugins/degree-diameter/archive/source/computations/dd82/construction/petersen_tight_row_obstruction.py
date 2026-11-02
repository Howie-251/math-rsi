"""Translate the saved tiny proof and extract an actual cubic obstruction.

This reads the existing proof-reference list and coverage map; it runs no
solver or proof checker. Tight immutable rows forbid internal edge choices.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import time

from hs_augmentation import ROOT, dump
from petersen_four_fiber_reassembly import adjacency, matching

SOURCE = ROOT / "computations/dd82/construction/petersen_fixed_route_repair_run/candidate.json"
PROOF = ROOT / "computations/dd82/construction/petersen_repaired_external_completion_run"
OUT = ROOT / "computations/dd82/construction/petersen_tight_row_obstruction_run"


def analyze(edges):
    ns = adjacency(edges)
    match = {(i,j):matching(ns,i,j) for i in range(6) for j in range(6) if i != j}
    rows, forbidden = [], {}
    F = 0
    for i in range(6):
        for j in range(6):
            if i == j:
                continue
            for u in range(10*i,10*i+10):
                direct = match[i,j][u%10]
                paths = [[u,direct]]
                for k in range(6):
                    if k not in (i,j):
                        w = match[i,k][u%10]
                        paths.append([u,w,match[k,j][w%10]])
                targets = {p[-1] for p in paths}
                F += max(0,4-len(targets))
                if len(targets) != 4:
                    continue
                banned = set()
                for w in range(10*i,10*i+10):
                    if w != u and match[i,j][w%10] in targets:
                        banned.add(tuple(sorted((u,w))))
                for v in targets:
                    if v != direct:
                        banned.add(tuple(sorted((direct,v))))
                assert len(banned) == 6
                record = dict(row=[u,j], fixed_paths=paths, fixed_targets=sorted(targets),
                              forbidden_internal_edges=sorted(banned))
                rows.append(record)
                for edge in banned:
                    forbidden.setdefault(edge,[]).append([u,j])
    allowed = {u:[v for v in range(10*(u//10),10*(u//10)+10)
                  if u != v and tuple(sorted((u,v))) not in forbidden]
               for u in range(60)}
    return dict(external_deficit=F,tight_rows=rows,
                forbidden_internal_edges=[dict(edge=e,rows=r) for e,r in sorted(forbidden.items())],
                allowed_neighbor_lists=allowed,
                cubic_neighbor_deficit=sum(max(0,3-len(vs)) for vs in allowed.values()),
                allowed_degree_histogram=dict(sorted(Counter(map(len,allowed.values())).items())),
                deficient_vertices=[u for u,vs in allowed.items() if len(vs)<3])


def main():
    start, cpu_start = time.monotonic(), time.process_time()
    OUT.mkdir(exist_ok=True)
    edges = {tuple(e) for e in json.loads(SOURCE.read_text())["edges"]}
    diagnostic = analyze(edges)
    assert diagnostic["external_deficit"] == 0
    assert diagnostic["cubic_neighbor_deficit"] == 69
    assert len(diagnostic["forbidden_internal_edges"]) == 213
    assert len(diagnostic["deficient_vertices"]) == 43

    # Read the 64 original coverage clauses actually referenced by the proof.
    refs = json.loads((PROOF / "proof_references.json").read_text())
    coverage = json.loads((PROOF / "coverage.json").read_text())
    encoding = json.loads((PROOF / "encoding.json").read_text())
    var_to_edge = {q:(u,v) for u,v,q in encoding["edge_variables"]}
    clauses = [list(map(int,line.split()[:-1])) for line in (PROOF / "input.cnf").read_text().splitlines()
               if line and line[0] not in "cp"]
    translations = []
    for clause_id in refs["referenced_original_clauses"]:
        if clause_id <= 14220:
            continue
        meaning = coverage[clause_id-14221]
        assert clauses[clause_id-1] == meaning["variables"]
        assert [list(var_to_edge[q]) for q in meaning["variables"]] == [
            meaning["source_internal_edge"],meaning["target_internal_edge"]]
        translations.append(dict(clause_id=clause_id,**meaning,
                                 meaning="At least one of these two internal edges must exist to cover this actual vertex pair."))
    assert len(translations) == 64
    dump(OUT / "proof_binary_clauses.json",translations)

    # A row bans at most three incident edges at any fixed internal vertex;
    # thus at least three tight rows are needed to forbid seven neighbors.
    u = 9
    choices = []
    for row in diagnostic["tight_rows"]:
        banned_neighbors = {b if a==u else a for a,b in row["forbidden_internal_edges"] if u in (a,b)}
        if banned_neighbors:
            choices.append((row,banned_neighbors))
    best = None
    for three in combinations(choices,3):
        banned = set().union(*(entry[1] for entry in three))
        if len(banned) >= 7 and (best is None or len(banned)>len(best[1])):
            best = (three,banned)
    assert best is not None
    witness = dict(vertex=u, rows=[r for r,bs in best[0]],
                   forbidden_neighbors=sorted(best[1]),
                   remaining_possible_neighbors=sorted(set(range(10))-{u}-best[1]),
                   reasoning="Each displayed row has five fixed slots on four targets, so its six internal slots must avoid every fixed target. Their union forbids at least seven of the nine possible neighbors of this vertex, contradicting internal degree three.",
                   independent_of_triangles_and_four_cycles=True)
    dump(OUT / "three_row_witness.json",witness)
    dump(OUT / "all_tight_row_constraints.json",diagnostic)
    resource = dict(operation="Read and translate 64 saved proof clauses; derive tight-row forbidden edges and choose a three-row actual witness",
                    source=str(SOURCE.relative_to(ROOT)),cpu_seconds=time.process_time()-cpu_start,
                    wall_seconds=time.monotonic()-start,solver_calls=0,checker_calls=0,
                    translated_binary_clauses=64,
                    tight_rows=len(diagnostic["tight_rows"]),forbidden_internal_edges=213,
                    deficient_vertices=43,cubic_neighbor_deficit=69,
                    witness_vertex=u,witness_rows=[r["row"] for r in witness["rows"]],
                    witness_forbidden_neighbors=witness["forbidden_neighbors"])
    dump(OUT / "resources.json",resource)
    print(json.dumps(resource))


if __name__ == "__main__":
    main()

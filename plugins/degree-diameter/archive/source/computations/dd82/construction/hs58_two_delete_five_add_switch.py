"""One complete a4 -> a5 addition-switch domain from 40 saved full graphs.

Remove (x,50+a),(y,50+b), add old nonedge xy and missing auxiliary edge ab.
No iterative search; retain the best complete graph for each surviving H type.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import os
import resource
import time

import networkx as nx

from hs_augmentation import base, dump, verify

HERE = Path(__file__).parent
SOURCE = HERE / "hs58_two_delete_four_add_switch_run"
CATALOG = HERE / "hs58_two_delete_five_add_auxiliary_run"
OUT = HERE / "hs58_two_delete_five_add_switch_run"
OLD = (1 << 50) - 1
ALL = (1 << 58) - 1
NEW = ALL ^ OLD


def masks(edges):
    ans = [0] * 58
    for x, y in edges:
        ans[x] |= 1 << y
        ans[y] |= 1 << x
    return ans


def score(ns):
    counts = [0, 0, 0]
    for x, near in enumerate(ns):
        reached = near | (1 << x)
        todo = near
        while todo:
            bit = todo & -todo
            reached |= ns[bit.bit_length() - 1]
            todo ^= bit
        missing = ALL ^ reached
        if x < 50:
            counts[0] += (missing & OLD).bit_count()
            counts[1] += (missing & NEW).bit_count()
        else:
            counts[2] += (missing & NEW).bit_count()
    return counts[0] // 2, counts[1], counts[2] // 2


def main():
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU, (20, 21))
    start_cpu, start_wall = time.process_time(), time.monotonic()
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    OUT.mkdir(exist_ok=True)
    assert not (OUT / "result.json").exists(), "No unchanged rerun"
    original, _ = base()
    original = set(original)
    records = json.loads((CATALOG / "representatives.json").read_text())["representatives"]
    allowed = set(json.loads((CATALOG / "survivor_ids.json").read_text())["remaining_type_ids"])
    representatives = []
    for row in records:
        graph = nx.Graph()
        graph.add_nodes_from(range(8))
        graph.add_edges_from(row["edges"])
        representatives.append((row, graph))
    hcache = {}

    def classify(edges):
        key = tuple(sorted(edges))
        if key in hcache:
            return hcache[key]
        graph = nx.Graph()
        graph.add_nodes_from(range(8))
        graph.add_edges_from(key)
        ds = sorted(dict(graph.degree()).values(), reverse=True)
        for row, representative in representatives:
            if row["sorted_degrees"] != ds:
                continue
            matcher = nx.algorithms.isomorphism.GraphMatcher(graph, representative)
            if matcher.is_isomorphic():
                mapping = [matcher.mapping[a] for a in range(8)]
                mapped = {tuple(sorted((mapping[a], mapping[b]))) for a, b in key}
                assert mapped == {tuple(e) for e in row["edges"]}
                hcache[key] = (row["type_id"], mapping)
                return hcache[key]
        raise AssertionError("H extension must lie in the raw necessary catalog")

    parent_result = json.loads((SOURCE / "result.json").read_text())
    sources = sorted(row["path"] for report in parent_result["results"]
                     for row in report["saved_H_variants"])
    assert len(sources) == 40
    best = {}
    best_old_covered = {}
    reports = []
    counts_by_type = Counter()
    for name in sources:
        seed = json.loads((SOURCE / name).read_text())
        old = {tuple(e) for e in seed["edges"]}
        ns = masks(old)
        assert all(n.bit_count() == 8 for n in ns)
        attachments = sorted(e for e in old if e[0] < 50 <= e[1])
        h = {tuple(e) for e in seed["auxiliary_edges"]}
        total, admitted = 0, 0
        hist = Counter()
        for (x, aa), (y, bb) in combinations(attachments, 2):
            if x == y or aa == bb:
                continue
            xy, ab = tuple(sorted((x, y))), tuple(sorted((aa, bb)))
            if xy in original or xy in old or ab in old:
                continue
            total += 1
            kind, mapping = classify(h | {(ab[0]-50, ab[1]-50)})
            if kind not in allowed:
                continue
            admitted += 1
            counts_by_type[kind] += 1
            edited = ns.copy()
            for u, w in ((x, aa), (y, bb), xy, ab):
                edited[u] ^= 1 << w
                edited[w] ^= 1 << u
            categories = score(edited)
            value = sum(categories)
            hist[value] += 1
            rank = (value, categories, name, x, aa, y, bb)
            candidate = dict(rank=rank, categories=categories, source=name,
                             remove=[(x, aa), (y, bb)], add=[xy, ab],
                             type_id=kind, map_to_representative=mapping)
            if kind not in best or rank < best[kind]["rank"]:
                best[kind] = candidate
            if categories[0] == 0 and (kind not in best_old_covered or rank < best_old_covered[kind]["rank"]):
                best_old_covered[kind] = candidate
        reports.append(dict(source=name, valid_switches=total,
                            surviving_H_switches=admitted, score_histogram=dict(sorted(hist.items()))))

    search_cpu, search_wall = time.process_time()-start_cpu, time.monotonic()-start_wall
    saved = []
    for key, chosen in [(f"type{kind}.best", row) for kind, row in sorted(best.items())] + [
            (f"type{kind}.old_covered", row) for kind, row in sorted(best_old_covered.items())
            if row["rank"] != best[kind]["rank"]]:
        seed = json.loads((SOURCE / chosen["source"]).read_text())
        edges = ({tuple(e) for e in seed["edges"]} - set(chosen["remove"])) | set(chosen["add"])
        old_edges = {e for e in edges if e[1] < 50}
        deleted = sorted(original-old_edges)
        added = sorted(old_edges-original)
        auxiliary = sorted((x-50, y-50) for x,y in edges if x >= 50)
        assert len(deleted) == 2 and len(added) == 5 and len(auxiliary) == 10
        assert len(edges) == 232 and all(n.bit_count() == 8 for n in masks(edges))
        path = OUT / f"{key}.json"
        data = dict(n=58, edges=sorted(edges), old_deletions=deleted,
                    old_additions=added, auxiliary_edges=auxiliary,
                    auxiliary_catalog_type=chosen["type_id"],
                    map_to_representative=chosen["map_to_representative"],
                    source=str(SOURCE/chosen["source"]),
                    transition=dict(remove=chosen["remove"], add=chosen["add"]),
                    enumerated_bad_pair_count=chosen["rank"][0],
                    bad_pair_categories=dict(zip(("old_old", "old_new", "new_new"), chosen["categories"])),
                    scope="Best per H type in the recorded one-switch domain from 40 fixed a4 graphs; not unrestricted a5 search.")
        dump(path, data)
        path.with_suffix(".edges").write_text("".join(f"{x} {y}\n" for x,y in sorted(edges)))
        checked = json.loads(verify(path))
        assert checked["bad_pair_count"] == data["enumerated_bad_pair_count"]
        full = json.loads(path.with_suffix(".verification.json").read_text())
        assert full["degrees"] == [8]*58
        saved.append(dict(path=path.name, type_id=chosen["type_id"],
                          source=chosen["source"], bad_pair_categories=data["bad_pair_categories"],
                          graph_check=checked))
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    result = dict(complete=True, domain="One specified addition switch from each of exactly 40 existing full a4 samples.",
                  source_files=sources, source_count=len(sources), input_survivor_type_ids=sorted(allowed),
                  candidate_switches=sum(r["valid_switches"] for r in reports),
                  admitted_switches=sum(r["surviving_H_switches"] for r in reports),
                  constructed_type_ids=sorted(best), proposals_by_type=dict(sorted(counts_by_type.items())),
                  minimum_bad_pairs=min(row["rank"][0] for row in best.values()),
                  best_graph=min(saved, key=lambda r:r["graph_check"]["bad_pair_count"])["path"],
                  search_cpu_seconds=search_cpu, search_wall_seconds=search_wall,
                  parent_cpu_seconds=time.process_time()-start_cpu,
                  independent_BFS_child_cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
                  wall_seconds=time.monotonic()-start_wall, pinned_cpu=next(iter(os.sched_getaffinity(0))),
                  auxiliary_isomorphism_checks_cached=len(hcache), saved_graphs=saved, parent_reports=reports,
                  no_exclusion_claim=True)
    dump(OUT / "result.json", result)
    print(json.dumps({k:v for k,v in result.items() if k not in ("parent_reports", "source_files", "input_survivor_type_ids", "saved_graphs")}))


if __name__ == "__main__":
    main()

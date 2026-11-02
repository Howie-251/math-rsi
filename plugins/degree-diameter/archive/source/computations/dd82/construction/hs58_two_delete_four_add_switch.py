"""One complete, narrowly specified a=3 -> a=4 construction step.

Delete two old-new edges and add their old-old and new-new partners.
Keep exactly the existing two deleted HS edges. This domain was not part
of the older twin/Brown switch searches. All proposals are expanded.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import json
import resource
import time

from hs_augmentation import base, dump, verify

HERE = Path(__file__).parent
SOURCE = HERE / "hs58_two_delete_three_add_seeds_run" / "old_cover"
OUT = HERE / "hs58_two_delete_four_add_switch_run"


def masks(edges):
    ns = [0] * 58
    for x, y in edges:
        ns[x] |= 1 << y
        ns[y] |= 1 << x
    return ns


def bad_pairs(edges):
    ns = masks(edges)
    return [(x, y) for x, y in combinations(range(58), 2)
            if not ((ns[x] >> y) & 1) and not (ns[x] & ns[y])]


def main():
    resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
    wall, cpu = time.monotonic(), time.process_time()
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    OUT.mkdir(exist_ok=True)
    assert not (OUT / "result.json").exists(), "No unchanged rerun"
    original, _ = base()
    original = set(original)
    reports = []
    for kind in (2, 3):
        seed = json.loads((SOURCE / f"type{kind}.seed.json").read_text())
        old = {tuple(e) for e in seed["edges"]}
        attachment = sorted((x, y) for x, y in old if x < 50 <= y)
        hist = Counter()
        best = None
        best_graph = None
        h_results = {}
        count = 0
        for (x, aa), (y, bb) in combinations(attachment, 2):
            if x == y or aa == bb:
                continue
            xy, ab = tuple(sorted((x, y))), tuple(sorted((aa, bb)))
            if xy in original or xy in old or ab in old:
                continue
            graph = (old - {(x, aa), (y, bb)}) | {xy, ab}
            bad = bad_pairs(graph)
            score = len(bad)
            count += 1
            hist[score] += 1
            # Keep every labeled auxiliary transition's best full graph.
            hkey = ab
            move = dict(remove=[[x, aa], [y, bb]], add=[list(xy), list(ab)])
            if hkey not in h_results or score < h_results[hkey][0]:
                h_results[hkey] = (score, sorted(graph), move)
            if best is None or score < best:
                best, best_graph = score, (sorted(graph), move)
        assert best_graph is not None
        variants = []
        for (aa, bb), (score, graph, move) in sorted(h_results.items()):
            tag = f"parent{kind}_h{aa-50}_{bb-50}"
            target = OUT / f"{tag}.json"
            data = dict(n=58, edges=graph, source=str(SOURCE / f"type{kind}.seed.json"),
                        old_deletions=seed["old_deletions"],
                        old_additions=sorted([list(e) for e in set(graph) - original if e[1] < 50]),
                        auxiliary_edges=[[x-50, y-50] for x, y in graph if x >= 50],
                        transition=move, enumerated_bad_pairs=score,
                        scope="Best in this single old-new/old-new -> old-old/new-new switch domain for this labeled H.")
            assert len(data["old_additions"]) == 4
            assert len(data["auxiliary_edges"]) == 9
            assert len(graph) == 232 and all(s.bit_count() == 8 for s in masks(graph))
            dump(target, data)
            target.with_suffix(".edges").write_text("".join(f"{x} {y}\n" for x, y in graph))
            checked = json.loads(verify(target))
            assert checked["bad_pair_count"] == score
            full = json.loads(target.with_suffix(".verification.json").read_text())
            categories = Counter(("old" if x < 50 else "new") + "_" + ("old" if y < 50 else "new")
                                 for row in full["bad_pairs"] for x, y in [row["pair"]])
            variants.append(dict(path=target.name, added_H_edge=[aa-50, bb-50],
                                 score=score, graph_check=checked,
                                 bad_pair_types=dict(categories), transition=move))
        reports.append(dict(parent_type=kind, complete_proposals=count,
                            score_histogram=dict(sorted(hist.items())), minimum=best,
                            best_transition=best_graph[1], saved_H_variants=variants))
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    result = dict(cpu_budget_seconds=10, parent_cpu_seconds=time.process_time()-cpu,
                  independent_BFS_child_cpu_seconds=after.ru_utime+after.ru_stime-child.ru_utime-child.ru_stime,
                  wall_seconds=time.monotonic()-wall, results=reports,
                  scope="Complete one specified switch from each of two fixed old-cover seeds; no exclusion of all a=4 constructions.")
    dump(OUT / "result.json", result)
    print(json.dumps(result))


if __name__ == "__main__":
    main()

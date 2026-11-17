"""Apply one frozen all-realizations menu pass to the saved D=24 remainder."""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import process_time
from unittest.mock import patch

from PROBE import short_matching

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent
CPU_LIMIT = 120
LIMIT = 1534
sys.path.insert(0, str(PROJECT / "global_bridge_2026_11_15"))
import exception_legacy_menu as old


def read_saved():
    raw = (HERE / "ODD_D24_PREFLIGHT.json").read_bytes()
    data = json.loads(raw)
    assert data["complete"] and data["total"]["outside_checked_gates"] == LIMIT
    assert len(data["families"]) == 8
    inputs = []
    families = []
    for idx, family in enumerate(data["families"]):
        cases = family["surviving_inputs"]
        assert family["counts"].get("outside_checked_gates", 0) == len(cases)
        families.append(dict(t=family["t"], position=family["position"], total=len(cases)))
        inputs.extend((idx, k, case) for k, case in enumerate(cases))
    assert len(inputs) == LIMIT
    return inputs, families, sha256(raw).hexdigest()


def plan_dependencies(plan):
    gate = plan["gate"]
    deps = [old.DEPENDENCIES[gate]]
    if gate == "k3_whole_receiver":
        deps.append(old.K3_DEPENDENCIES[plan["donor"]["kind"]])
    elif gate == "registry_two_return":
        deps.append("R7_E16_MU2_FULL_REVIEW.md")
        if plan["donor"]["kind"] == "T15_exact_core":
            deps.append("Q6_T15_GOOD_ROOT_COMPONENTS_REVIEW.json")
    return deps


def run(inputs, families, source_sha):
    start = process_time()
    positives = []
    hits = Counter()
    visited = Counter()
    passed = Counter()
    failure = None
    next_index = 0
    with patch.object(old, "CPU_LIMIT", CPU_LIMIT), old.legacy_menu(start) as find:
        while next_index < LIMIT:
            if process_time()-start >= CPU_LIMIT:
                failure = dict(status="CPU_LIMIT")
                break
            family, row, case = inputs[next_index]
            colors = tuple(tuple(case[key]) for key in ("even_holes", "odd_holes"))
            delta = old.signed_gaps(colors)
            assert delta == tuple(8-x for x in case["lambda_by_axis"])
            assert min(map(abs, delta)) == 3
            counters = Counter()
            try:
                plan = find(colors, delta, counters)
            except TimeoutError as error:
                failure = dict(status="CPU_LIMIT", error=str(error), interrupted=case,
                               family=family, row=row, counters=counters)
                break
            except (RuntimeError, FileNotFoundError, ImportError) as error:
                failure = dict(status="MENU_ERROR", error=str(error), interrupted=case,
                               family=family, row=row, counters=counters)
                break
            visited[family] += 1
            next_index += 1
            if plan is None or old.requires_edge(plan) or plan["gate"] not in old.DEPENDENCIES:
                reason = "NO_PLAN" if plan is None else "NONUNIVERSAL_OR_UNREGISTERED"
                failure = dict(status=reason, family=family, row=row, input=case,
                               attempted_plan=plan, counters=counters)
                if process_time()-start < CPU_LIMIT:
                    failure["short_matching"] = short_matching(colors)
                break
            gate = plan["gate"]
            deps = plan_dependencies(plan)
            positives.append(dict(family=family, row=row, input=case, delta=delta,
                                  gate=gate, plan=plan, dependencies=deps))
            hits[gate] += 1
            passed[family] += 1
    elapsed = process_time()-start
    for idx, family in enumerate(families):
        family.update(visited=visited[idx], positives=passed[idx],
                      unvisited=family["total"]-visited[idx])
    known_deps = sorted({name for result in positives for name in result["dependencies"]})
    if next_index < LIMIT:
        f, k, w = inputs[next_index]
        checkpoint = dict(family=f, row=k, q=w["q"], C=w["C"], D=w["D"])
    else:
        checkpoint = None
    return dict(candidate_limit=LIMIT, visits_completed=next_index,
                positive_count=len(positives), families=families, gate_counts=hits,
                complete=failure is None and next_index == LIMIT, failure=failure,
                next_unvisited=checkpoint, cpu_limit_seconds=CPU_LIMIT, cpu_seconds=elapsed,
                input_sha256=source_sha,
                legacy_menu_sha256=sha256(Path(old.__file__).read_bytes()).hexdigest(),
                dependency_sha256={name: sha256((PROJECT / name).read_bytes()).hexdigest()
                                   for name in known_deps},
                positives=positives)


def main():
    data = run(*read_saved())
    Path(__file__).with_suffix(".json").write_text(json.dumps(data, separators=(",",":"))+"\n",
                                                  encoding="utf-8")
    print({key: val for key, val in data.items() if key not in ("positives", "dependency_sha256")},
          flush=True)


if __name__ == "__main__":
    main()


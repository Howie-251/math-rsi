#!/usr/bin/env python3
"""Exact two-target-class diagnostic using existing H9 guard columns only."""
import json
from pathlib import Path
import signal
import time

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parents[2]
INPUT = PROJECT / "research/ddp/more_graphs_20261027/h9_redei15/stable_triangle_twist/degree_and_first_extension/items"
START = time.process_time()
ROWS = []


def cover(masks, representatives, target, budget):
    if not target:
        return []
    if budget == 0:
        return None
    unique = {}
    for i, mask in enumerate(masks):
        projected = mask & target
        if projected == target:
            return [representatives[i]]
        if projected and projected not in unique:
            unique[projected] = i
    if budget == 1:
        return None
    entries = list(unique.items())
    support = {}
    for a, (mask, _) in enumerate(entries):
        choice = 1 << a
        remaining = mask
        while remaining:
            bit = remaining & -remaining
            support[bit] = support.get(bit, 0) | choice
            remaining ^= bit
    for mask, original in entries:
        missing = target ^ mask
        candidate = None
        while missing:
            bit = missing & -missing
            column = support.get(bit, 0)
            candidate = column if candidate is None else candidate & column
            if not candidate:
                break
            missing ^= bit
        if candidate:
            other = (candidate & -candidate).bit_length() - 1
            guards = [representatives[original], representatives[entries[other][1]]]
            assert len(set(guards)) == 2
            return guards
    return None


def save(status):
    result = dict(
        status=status, CPU_seconds=time.process_time() - START,
        input_scope="30 saved neighborhoods and guard columns on final42402 only",
        prediction="H9_PROJECTED_GUARD_PREDICTION.md", rows=ROWS,
        completed=len(ROWS), unattempted=30-len(ROWS),
        new_graphs=0, new_balls=0, BFS=0, solver_calls=0,
        original_only_feasible=sum(r["original_only_guards"] is not None for r in ROWS),
        added_only_feasible=sum(r["added_only_guards"] is not None for r in ROWS),
    )
    two = [r for r in ROWS if r["budget"] == 2]
    result["two_guard_cases_completed"] = len(two)
    result["two_guard_original_feasible"] = sum(r["original_only_guards"] is not None for r in two)
    result["prediction_verdict"] = ("SUPPORTED" if result["two_guard_original_feasible"] else
                                    "REFUTED" if len(two) == 5 else "UNRESOLVED")
    (HERE / "H9_PROJECTED_GUARD_RESULT.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    report = f"""# H9 原外围与新增目标的分离诊断

状态：{status}；实际CPU {result['CPU_seconds']:.6f}秒。完成{len(ROWS)}/30，未试{30-len(ROWS)}。
仅复用最终42402图上的已有guard列，没有新球、BFS、求解器或新图。

原外围单独可覆：{result['original_only_feasible']}项；新增点单独可覆：{result['added_only_feasible']}项。
五个两guard项中已完成{len(two)}项，原外围可覆{result['two_guard_original_feasible']}项。
冻结存在预测：{result['prediction_verdict']}。

原始整组联合覆盖已在旧批次失败；本次不重跑联合判定。分别可覆不等于同一guard组可同时覆盖。
每项JSON保留实际budget、原/新增目标标签、各自见证，以及该见证对另一类仍漏哪些点。
原外围已单独不可覆时，单纯去掉后来新增点不能修复同一邻集对这些原目标的距离；在删点图里路径只会减少。
本次guard域是最终图可用集合；移除新增点后的额外空位不在此域，不能据此排所有联合重排。

下一决策：不把旧30项失败只归因于新点间距离，不启动同池重排/补点长搜；数学主线应改变外围覆盖规则或转有明确路线保证的不同机制。
"""
    (HERE / "H9_PROJECTED_GUARD_REPORT.md").write_text(report)
    print(json.dumps({k:v for k,v in result.items() if k != "rows"}, ensure_ascii=False))


def timeout(_signum, _frame):
    save("CPU_BUDGET_PARTIAL")
    raise SystemExit(0)


signal.signal(signal.SIGPROF, timeout)
signal.setitimer(signal.ITIMER_PROF, 15)
for index in range(30):
    meta = INPUT / f"d12_pool{index:05d}.json"
    data = json.loads(meta.read_text())
    labels, representatives = data["missing"], data["representatives"]
    words = data["mask_words_per_row"]
    raw = meta.with_suffix(".masks.u64.bin").read_bytes()
    assert len(raw) == len(representatives) * words * 8
    stride = words * 8
    masks = [int.from_bytes(raw[k:k+stride], "little") for k in range(0, len(raw), stride)]
    original = sum(1 << j for j,t in enumerate(labels) if 41356 <= t < 42342)
    added = sum(1 << j for j,t in enumerate(labels) if 42342 <= t < 42402)
    assert original | added == (1 << len(labels)) - 1
    budget = 12 - len(data["pins"])
    old_witness = cover(masks, representatives, original, budget)
    new_witness = cover(masks, representatives, added, budget)
    lookup = dict(zip(representatives, masks))
    def other_misses(witness, other):
        if witness is None:
            return None
        union = 0
        for guard in witness:
            union |= lookup[guard]
        assert all(guard not in data["pins"] for guard in witness)
        return [t for j,t in enumerate(labels) if (other & (1 << j)) and not (union & (1 << j))]
    if old_witness is not None:
        assert not other_misses(old_witness, original)
    if new_witness is not None:
        assert not other_misses(new_witness, added)
    ROWS.append(dict(
        item=index, budget=budget, original_targets=[t for t in labels if 41356 <= t < 42342],
        added_targets=[t for t in labels if 42342 <= t < 42402],
        original_only_guards=old_witness, added_only_guards=new_witness,
        original_solution_added_misses=other_misses(old_witness, added),
        added_solution_original_misses=other_misses(new_witness, original),
    ))
signal.setitimer(signal.ITIMER_PROF, 0)
save("COMPLETE")

"""Single bounded pass of accepted unconditional gates on the frozen gap-eight basis."""

import json
from collections import Counter
from hashlib import sha256
from pathlib import Path
from time import process_time
from unittest.mock import patch

from E16_MU3_ROUTE_R41_M3_FIXED_PLANS import accepted, first_plan, four_limits


BASE = Path(__file__).with_name("R7_E16_MU3_GAP8_BASE.json")
OUTPUT = Path(__file__).with_suffix(".json")
BASE_HASH = "96149c54ebd15f3a8699ab82cff93be5547714eb243042223cc207052514bc13"
EXPECTED = 4592
CPU_LIMIT = 60
AXES = tuple(range(7))
R32_LOADS = {(2, 0), (2, 1), (3, 1), (3, 2)}


def physical_colors(row):
    colors = (tuple(row["L"]), tuple(sorted(127 ^ point for point in row["V"])))
    return colors[::-1] if colors[0][0].bit_count() % 2 else colors


def face(points, axis, side):
    return tuple(p for p in points if (p >> axis) & 1 == side)


def directed_cuts(colors):
    for outer in AXES[:-1]:
        for side in (0, 1):
            groups = tuple(face(points, outer, side) for points in colors)
            alpha = int(len(groups[1]) > len(groups[0]))
            major, minor = groups[alpha], groups[1 - alpha]
            a_major = face(colors[1 - alpha], outer, 1 - side)
            a_minor = face(colors[alpha], outer, 1 - side)
            yield outer, side, alpha, (a_minor, a_major), (major, minor)


def witness(outer, side, alpha, donor, receiver, **params):
    return dict(outer=outer, donor_side=1 - side, alpha_parity=alpha,
                original_A_by_alpha_beta=donor, original_B_by_alpha_beta=receiver,
                shape=tuple(tuple(map(len, groups)) for groups in (donor, receiver)), **params)


def high_m_witnesses(colors):
    hits = {}
    for outer, side, alpha, donor, receiver in directed_cuts(colors):
        major, minor = receiver
        if len(major) - len(minor) != 3:
            continue
        inner_axes = tuple(i for i in AXES if i != outer)
        if len(minor) == 1:
            root = minor[0]
            loads = tuple((i, len(face(tuple(p ^ root for p in major), i, 1))) for i in inner_axes)
            usable = tuple(i for i, load in loads if load in (1, 2))
            if len(usable) >= 3 and "R41" not in hits:
                hits["R41"] = witness(outer, side, alpha, donor, receiver, root=root,
                                      inner_loads=loads, usable=usable)
        if len(minor) == 2:
            loads = tuple((i, (len(face(major, i, 1)), len(face(minor, i, 1)))) for i in inner_axes)
            usable = tuple(i for i, load in loads if load in R32_LOADS)
            if len(usable) >= 4 and "R32" not in hits:
                hits["R32"] = witness(outer, side, alpha, donor, receiver,
                                      inner_loads=loads, usable=usable)
    return hits


def four_mono(colors):
    for outer, side, alpha, donor, receiver in directed_cuts(colors):
        major, minor = receiver
        if (len(major), len(minor)) == (4, 0):
            split_axes = tuple(i for i in AXES if i != outer and len(face(major, i, 1)) == 2)
            if len(split_axes) >= 3:
                return witness(outer, side, alpha, donor, receiver, gate="four_mono_capacity",
                               split_axes=split_axes)
    return None


def run(start):
    payload = BASE.read_bytes()
    assert sha256(payload).hexdigest() == BASE_HASH
    rows = json.loads(payload)["records"]
    assert len(rows) == EXPECTED
    candidates = []
    positives = []
    failure = None
    status = "complete"
    broad = accepted.joint.broad_returns
    original_surviving = broad.surviving

    def surviving_optional(edge, outer, side, omitted):
        return None if edge is None else original_surviving(edge, outer, side, omitted)

    search = dict(lookup=None, broad=None)
    with (
        patch.object(accepted, "CPU_LIMIT", CPU_LIMIT),
        patch.object(four_limits, "CPU_LIMIT", CPU_LIMIT),
        patch.object(broad, "CPU_LIMIT", CPU_LIMIT),
        patch.object(broad, "surviving", surviving_optional),
        patch.object(broad, "whole_interface", accepted.balanced_whole_wrapper(broad.whole_interface)),
    ):
        for index, row in enumerate(rows):
            colors = physical_colors(row)
            gaps = tuple(len(face(colors[0], i, 1)) - len(face(colors[1], i, 1)) for i in AXES)
            assert min(map(abs, gaps)) == 3 and abs(gaps[-1]) == 8
            high_m = high_m_witnesses(colors)
            assert sorted(high_m) == row["high_m"]
            if high_m:
                positives.append(dict(index=index, plan=dict(gate="accepted_high_m", witnesses=high_m)))
            else:
                candidates.append((index, row, colors, gaps))
        assert len(positives) == 679
        for index, row, colors, gaps in candidates:
            counters = Counter()
            try:
                accepted.check_time(start)
                plan = accepted.joint.counts_orbits(colors) or four_mono(colors)
                if plan is None:
                    plan = first_plan(colors, gaps, search, counters, start)
                accepted.check_time(start)
            except TimeoutError:
                status = "cpu_limit"
                plan = None
            if plan is None:
                if status != "cpu_limit":
                    status = "first_unsupported"
                failure = dict(index=index, representative=row, physical_colors=colors,
                               signed_gaps=gaps, counters=dict(counters))
                break
            assert plan.get("required_forced_edge") is None
            if plan["gate"] in ("controlled_cycle_count", "controlled_cycle_registered_split"):
                assert plan["outer"] != 6
            positives.append(dict(index=index, plan=plan))
    visited = len(positives) + int(failure is not None)
    return dict(status=status, input_representatives=EXPECTED, base_sha256=BASE_HASH,
                visited=visited, unvisited=EXPECTED - visited, cpu_limit_seconds=CPU_LIMIT,
                cpu_seconds=process_time() - start, positives=sorted(positives, key=lambda row: row["index"]),
                plan_counts=dict(Counter(row["plan"]["gate"] for row in positives)),
                first_failure=failure, new_geometries=0, original_matchings_enumerated=0,
                solver_calls=0, rank_runs=0)


if __name__ == "__main__":
    result = run(process_time())
    with OUTPUT.open("x", encoding="utf-8", newline="\n") as file:
        json.dump(result, file, separators=(",", ":"))
        file.write("\n")
    print(json.dumps({key: value for key, value in result.items() if key != "positives"}, indent=2))

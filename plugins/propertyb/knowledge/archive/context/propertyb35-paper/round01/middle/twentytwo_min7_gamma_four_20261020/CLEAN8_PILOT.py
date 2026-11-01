"""Exact degree-eight clean-star probe in the five remaining q3 sources.

This is a bounded diagnostic, not a proof of the whole 22-point branch.
Use the same old five-lock menu and six available slots, at the actual n=22.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import json
import sys
import time

P = Path(__file__).resolve().parent
R = P.parents[4]
sys.dont_write_bytecode = True
sys.path.insert(0, str(R / "context/propertyb34/round01/high-math"))
from subset_position_dp import SubsetEngine


def comps(n, k):
    if k == 1:
        yield (n,)
        return
    for a in range(n + 1):
        for tail in comps(n - a, k - 1):
            yield (a,) + tail


def mapmask(mask, permutation):
    return sum(1 << permutation[i] for i in range(5) if mask >> i & 1)


def image(vector, permutation):
    result = [0] * 5
    for i, value in enumerate(vector):
        result[permutation[i]] = value
    return tuple(result)


def run():
    start = time.process_time()
    sources = json.loads((P / "FIXED_RESULT.json").read_text())["nonstrict"]
    ids = (20, 21, 22, 23, 24)
    menu = [tuple(x["positions"]) for x in
            json.loads((P / "PILOT_RESULT.json").read_text())["all_fixed"]]
    layouts = sorted({(slot,) + p for p in menu
                      for slot in (1, 9, 10, 11, 20, 21) if slot not in p})
    rows = []
    for sid in ids:
        source = sources[sid]
        for inc in comps(3, 5):
            star = tuple(x + 1 for x in inc)
            if any(x > a for x, a in zip(star, source["attachments"])):
                continue
            counts = Counter({int(m) << 1: n for m, n in source["counts"].items()})
            for i, n in enumerate(star):
                counts[1 << (i + 1)] -= n
                counts[(1 << (i + 1)) | 1] += n
            assert sum(counts.values()) == 35 and min(counts.values()) >= 0
            engine = SubsetEngine(22, 6, counts)
            engine.inv = {p: (0, 0, []) for p in engine.inv}
            values = []
            for positions in layouts:
                locks = {k: 1 << v for v, k in enumerate(positions)}
                left = value = 0
                for k in range(1, 23):
                    bit = locks.get(k, 0)
                    value += engine.value(k, left, bit)
                    left |= bit
                values.append((Fraction(value, engine.D), positions))
            bound, positions = min(values)
            rows.append(dict(source=sid, star=star, degree=8,
                             counts=dict(counts), bound=str(bound),
                             positions=positions, strict=bound < 1))
    lookup = {(r["source"], tuple(r["star"])): r for r in rows}
    source_lookup = {tuple(sources[sid]["attachments"]): sid for sid in ids}
    automorphisms = [
        p for p in permutations(range(5))
        if tuple(sorted(mapmask(m, p) for m in (7, 27, 29))) == (7, 27, 29)
    ]
    remaining = []
    for row in rows:
        certificates = []
        for perm in automorphisms:
            target = source_lookup.get(image(sources[row["source"]]["attachments"], perm))
            if target is None:
                continue
            dest = lookup[(target, image(row["star"], perm))]
            if dest["strict"]:
                certificates.append(dict(permutation=perm, target=target,
                                         bound=dest["bound"], positions=dest["positions"]))
        row["transport_strict"] = bool(certificates)
        row["transport_certificate"] = certificates[:1]
        if not certificates:
            remaining.append({k: row[k] for k in ("source", "star", "bound")})
    result = dict(
        status="COMPLETE_BOUNDED_CLEAN8_DIAGNOSTIC",
        scope="Five final q3 profiles, all positive degree-eight clean stars; "
              "old16 five-lock layouts and old6 insertion slots, n22/free16, "
              "zero quotas. Does not assert all clean8 are absent.",
        source_count=5, input_count=len(rows), layout_count=len(layouts),
        remaining=remaining, rows=rows, cpu_seconds=time.process_time() - start,
    )
    (P / "CLEAN8_PILOT_RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "rows"}, indent=2))


if __name__ == "__main__":
    run()

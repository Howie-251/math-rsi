"""Independent star-domain generation and expanded original-edge replay."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import json
import sys
import time

P = Path(__file__).resolve().parent
R = P.parents[4]
sys.dont_write_bytecode = True
sys.path.insert(0, str(R / "computations"))
from independent_structure_bounds import independent_rows

start = time.process_time()
sources = json.loads((P / "FIXED_RESULT.json").read_text())["nonstrict"]
primary = json.loads((P / "CLEAN8_PILOT_RESULT.json").read_text())
domain = {}
for sid in (20, 21, 22, 23, 24):
    source = sources[sid]
    base = [31] + source["traces"] + [
        1 << i for i, a in enumerate(source["attachments"]) for _ in range(a)]
    assert len(base) == 35
    for cuts in combinations(range(1, 8), 4):
        points = (0,) + cuts + (8,)
        star = tuple(points[i + 1] - points[i] for i in range(5))
        if any(x > a for x, a in zip(star, source["attachments"])):
            continue
        left = list(star)
        lifted = []
        for mask in base:
            contains = 0
            if mask.bit_count() == 1:
                i = mask.bit_length() - 1
                if left[i]:
                    left[i] -= 1
                    contains = 1
            lifted.append(2 * mask + contains)
        assert not any(left)
        domain[(sid, star)] = lifted
assert len(domain) == 175
assert set(domain) == {(r["source"], tuple(r["star"])) for r in primary["rows"]}
bounds = []
raw_bounds = []
row_lookup = {(r["source"], tuple(r["star"])): r for r in primary["rows"]}
for row in primary["rows"]:
    masks = domain[(row["source"], tuple(row["star"]))]
    assert Counter(masks) == +Counter({int(m): n for m, n in row["counts"].items()})
    stubs = [frozenset(i + 1 for i in range(6) if mask >> i & 1) for mask in masks]
    values = independent_rows(22, tuple(row["positions"]), stubs)
    bound = sum((min(v["A"], v["B"], v["C"]) for v in values), Fraction())
    assert bound == Fraction(row["bound"])
    assert (bound < 1) == row["strict"]
    raw_bounds.append(str(bound))
    certificate = row["transport_certificate"][0]
    perm = certificate["permutation"]
    target_star = [0] * 5
    for i, value in enumerate(row["star"]):
        target_star[perm[i]] = value
    target = row_lookup[(certificate["target"], tuple(target_star))]
    assert Fraction(target["bound"]) < 1
    transported = [
        (mask & 1) | sum(1 << (perm[i] + 1) for i in range(5)
                         if mask >> (i + 1) & 1)
        for mask in masks
    ]
    assert Counter(transported) == Counter(
        domain[(certificate["target"], tuple(target_star))])
    assert target["positions"] == certificate["positions"]
    assert target["bound"] == certificate["bound"]
    bounds.append(certificate["bound"])
result = dict(
    status="PASS_COMPLETE175_CLEAN8_DOMAIN_AND_ORIGINAL35_REPLAY",
    scope="All positive clean8 stars in sources20..24, actual22/free16, "
          "35 distinct original edge indices,1190 ordered distinct pairs at22 pivots.",
    inputs=len(domain), replayed_rows=22 * len(domain),
    maximum_transported_bound=str(max(map(Fraction, bounds))),
    raw_nonstrict=sum(Fraction(x) >= 1 for x in raw_bounds),
    bounds=bounds, cpu_seconds=time.process_time() - start,
)
(P / "VERIFY_CLEAN8_RESULT.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k: v for k, v in result.items() if k != "bounds"}, indent=2))

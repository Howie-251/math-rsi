"""Literal check of the single-partition events used in the fixed-high proof."""
from itertools import combinations
from math import comb
from pathlib import Path
from time import process_time
import json

def main():
    start = process_time()
    blocks = [sum(1 << x for x in range(4*i, 4*i+4)) for i in range(4)]
    triple = sum(1 << x for x in range(16, 19))
    counts = dict(A=0, BR=0, BB=0, A_BR=0, A_BB=0, union_R=0, union_RB=0)
    total = 0
    for blue_points in combinations(range(19), 9):
        blue = sum(1 << x for x in blue_points)
        has_blue = any((blue & q) == q for q in blocks)
        has_red = any((blue & q) == 0 for q in blocks)
        a = has_blue and has_red
        br = (blue & triple) == 0 and has_blue
        bb = (blue & triple) == triple and has_red
        assert not (br and bb)
        values = (a, br, bb, a and br, a and bb, a or br, a or br or bb)
        for key, value in zip(counts, values):
            counts[key] += value
        total += 1
    expected = dict(A=5226, BR=3120, BB=3528, A_BR=624, A_BB=264,
                    union_R=7722, union_RB=10986)
    assert counts == expected
    assert total == comb(19, 9) == 92378
    fixed = 16*3003 + 4*5005
    pair = counts["union_RB"] + counts["A"]
    bound = fixed + counts["union_R"] + pair
    assert fixed == 68068 and pair == 16212 and bound == 92002
    assert total - bound == 376
    result = dict(status="PASS", scope="one four-block partition on 19 points; all nine-blue samples",
                  samples=total, counts=counts, fixed_bound=fixed,
                  single_center_bound=counts["union_R"], pair_bound=pair,
                  overall_bound=bound, strict_margin=total-bound,
                  cpu_seconds=process_time()-start)
    Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()

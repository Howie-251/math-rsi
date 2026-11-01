"""Small integer implications in TIGHT_ALL_BLUE_SIZES; no H enumeration."""
from pathlib import Path
from time import process_time
import json

start = process_time()
rows = []
for b in range(8, 14):
    L = (b * (25 - b) - 136) // 2
    K = (b * b - 43 * b + 408) // 2
    t = 15 - b
    base_rho = 25 - K + t
    assert L - 9 - base_rho == 87 - 8 * b
    allowable_c = []
    for c in range(100):
        N3, N4 = L + c - t, 34 - b - L - c
        delta, rho = K - t - c, base_rho + c
        if min(N3, N4, delta, rho) < 0 or delta > 25:
            continue
        assert b + t + N3 + N4 == 34
        allowable_c.append(c)
    rows.append({
        "b": b, "t": t, "L": L, "K": K,
        "red_excess_minus_c": base_rho,
        "forced_low_sinks": 87 - 8 * b,
        "nonnegative_color_degree_c": allowable_c,
    })
assert rows[0]["nonnegative_color_degree_c"] == []
assert rows[1]["forced_low_sinks"] == 15
assert rows[2]["forced_low_sinks"] == 7
assert rows[3]["red_excess_minus_c"] == 1

# Shared price 2a+q <= t+3 from integer a(a-1)<=2(t-q).
shared_trials = 0
for t in range(2, 8):
    for a in range(35):
        for q in range(t + 1):
            if a * (a - 1) <= 2 * (t - q):
                shared_trials += 1
                assert 2 * a + q <= t + 3

# All positive-c b11 roles after the common graph enforces ell<=1.
b11_roles = []
for c in rows[3]["nonnegative_color_degree_c"]:
    if c == 0:
        continue
    for low in (0, 1):
        for high in range(15 - low):
            if low + high < c or 3 * high > 2 * c:
                continue
            b11_roles.append([c, low, high])
assert b11_roles == [[1, 1, 0], [2, 1, 1], [3, 1, 2]]
survivors = {"A": [], "B": []}
for c, low, high in b11_roles:
    # A: two high N3 neighbors, each price>=5.
    if high >= 2 and 3 * high + 4 <= 2 * c:
        survivors["A"].append([c, low, high])
    # B: one high N3 neighbor, price>=5; others price>=3.
    if high >= 1 and 3 * high + 2 <= 2 * c:
        survivors["B"].append([c, low, high])
assert survivors == {"A": [], "B": []}

# Low endpoint row equations on b11.
for kind, n2, expected in (("A", 2, (1, 2)), ("B", 1, (3, 1))):
    solutions = [(n3, n4) for n3 in range(7) for n4 in range(7)
                 if 1 + n2 + n3 + n4 == 6
                 and n2 + 2 * n3 + 3 * n4 == 10]
    assert solutions == [expected], (kind, solutions)

result = {
    "status": "PASS",
    "scope": "u0,N2=15-b tight face, 8<=b<=13; small integer implications only",
    "arithmetic_rows": rows,
    "shared_price_integer_trials": shared_trials,
    "b11_positive_c_roles": b11_roles,
    "b11_price_survivors": survivors,
    "b11_c0_paper_obligation": "unique high red vertex contradicts all unit codegrees",
    "b12_b13_status": "declared complete canonical proof imports, not recomputed here",
    "whole_twentyfive_branch_claimed": False,
    "hypergraphs_enumerated": 0,
    "probability_layouts_added": 0,
    "review_independence": "same-family",
    "acceptance_status": "provisional",
    "cpu_seconds": process_time() - start,
}
Path(__file__).with_name("TIGHT_ALL_BLUE_RESULT.json").write_text(
    json.dumps(result, indent=2) + "\n"
)
print(json.dumps(result))

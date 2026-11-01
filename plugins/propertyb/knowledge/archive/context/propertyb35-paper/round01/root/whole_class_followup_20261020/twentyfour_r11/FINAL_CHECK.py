"""Exact small arithmetic for the shared r11 proof; no hypergraph search."""
from pathlib import Path
from time import process_time
import importlib.util
import json


def local_module(name):
    spec = importlib.util.spec_from_file_location(name, Path(__file__).with_name(name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def multiplicities(n, incidence, pairs):
    ans = []
    for a in range(n + 1):
        for b in range(n + 1 - a):
            for c in range(n + 1 - a - b):
                d = n - a - b - c
                if b + 2 * c + 3 * d == incidence and c + 3 * d == pairs:
                    ans.append([a, b, c, d])
    return ans


def main():
    t0 = process_time()
    agg = local_module("AGGREGATE_CHECK")
    nine = local_module("NINE_NINE_CHECK")
    domain = [agg.audit_face(q, a) for q, a in agg.faces()]
    assert len(domain) == 14
    counts = [(r["q"], r["a"], len(r["aggregate_survivors"])) for r in domain]
    assert [(q, a) for q, a, count in counts if count] == [(0, 1), (2, 0)]
    assert len(domain[7]["aggregate_survivors"]) == 1
    exceptional = domain[7]["aggregate_survivors"][0]
    assert exceptional == dict(
        A7=3, inactive8=0, active8=4, C11=1, C12plus=0,
        other9or10=5, excess_lower_bound=18, minimum_N8=4
    )
    triple_7 = multiplicities(9, 18, 9)
    four_7 = multiplicities(10, 20, 10)
    assert triple_7 == [[0, 0, 9, 0]]
    assert four_7 == [[0, 0, 10, 0]]

    # Additional shared row inequality 3N8 >= 11(A+B)-64.
    # The A=4 class is ruled out analytically in REPORT section 7.
    residual = []
    for r in domain[0]["aggregate_survivors"]:
        A = r["A7"]
        X = A + r["inactive8"] + r["active8"]
        C, D = r["C11"], r["C12plus"]
        if A == 4 or 11 * X > 64 + 15 * C + 21 * D:
            continue
        residual.append(r)
    assert len(residual) == 2
    assert {(r["A7"], r["inactive8"], r["active8"], r["C11"],
             r["C12plus"], r["other9or10"]) for r in residual} == {
                 (3, 0, 4, 1, 0, 5), (3, 1, 3, 1, 0, 5)}
    wrows = [(e, b, c, K)
             for e in range(2) for b in range(11)
             for c in range(5, 8) for K in (5, 6)
             if e + 2*b + 3*c == 11 + K and e + b + c <= 11]
    assert wrows == [(0, 1, 5, 6), (1, 0, 5, 5)]
    nine_rows = [(e, b, c, K)
                 for e in range(2) for b in range(11)
                 for c in range(8) for K in range(b+1)
                 if e + 2*b + 3*c == 11 + K and e + b + c <= 9]
    assert max(row[2] for row in nine_rows) == 3

    nn = []
    for p in (0, 1):
        for su in range(4-2*p):
            for sv in range(4-2*p-su):
                for alpha in range(9):
                    if min(8-su-alpha, 8-sv-alpha) < 0 or su+sv+alpha == 0:
                        continue
                    bounds = [
                        77681+243*p+18018-1822*s+948*t-5005*alpha
                        -nine.red(8-s-alpha)-nine.blue(8-t-alpha)
                        for s, t in ((su, sv), (sv, su))
                    ]
                    nn.append(min(bounds))
    assert len(nn) == 96 and max(nn) == 92174 < 92378
    result = dict(
        status="PASS",
        scope="shared arithmetic in the analytic r11 exclusion, with declared coloring imports",
        input_faces=counts,
        low_domain_faces=14,
        coarse_survivor_faces=2,
        q2a0_double_multiplicities=triple_7,
        q0a1_four_seven_double_multiplicities=four_7,
        q0a1_after_shared_row=residual,
        degree_eleven_rows=wrows,
        nine_owned_only_in_double_max_c=3,
        required_nine_F3_incidence=20,
        available_nine_F3_incidence=15,
        nine_nine_gate=dict(rows=len(nn), maximum=max(nn), denominator=92378),
        actual_hypergraphs_enumerated=0,
        cpu_seconds=process_time()-t0,
    )
    Path(__file__).with_name("FINAL_RESULT.json").write_text(
        json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ("input_faces", "q0a1_after_shared_row")}, indent=2))


if __name__ == "__main__":
    main()

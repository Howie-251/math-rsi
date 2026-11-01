"""Reuse saved layouts; test Boolean affine upper bounds on three actual families.

No layout search is performed.  All empty-trace counts are held at the fixed
five-low value, including the synthetic baseline used to recover coefficients.
"""
from pathlib import Path
from fractions import Fraction
from collections import Counter
import json
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
SOURCE = ROOT / "context/propertyb34/round01/high-math"
sys.path.insert(0, str(SOURCE))
from bare_layout import BareLayout


def run_family(family, rows, bounds, stop_universal=False):
    full = family["full"]
    inc = [sum(bool(t & (1 << i)) for t in full) for i in range(9)]
    empty = sum(inc) - len(full) - 24
    assert empty >= 0
    lows = [tuple(low) for low in family["lows"]]

    def counts(low):
        return {0: empty, **{1 << i: 7 - inc[i] - int(i in low) for i in range(9)},
                **{t: 1 for t in full}}

    def fixed_value(layout, ns, choice):
        _, abc = layout.bound(ns, True)
        return sum((r[c] for r, c in zip(abc, choice)), Fraction(0))

    candidates = []
    seen = set()
    for row in rows:
        saved = bounds[row["target"]]
        original_pos = tuple(saved["positions"][j] for j in row["permutation"])
        if max(original_pos) - min(original_pos) != 8:
            continue
        layout = BareLayout(25, original_pos)
        value, abc = layout.bound(counts(row["low"]), True)
        assert value == Fraction(saved["bound"]), (row, value, saved["bound"])
        choice = tuple(min(range(3), key=lambda c: r[c]) for r in abc)
        key = original_pos, choice
        if key in seen:
            continue
        seen.add(key)
        const = fixed_value(layout, counts(()), choice)
        coeffs = [fixed_value(layout, counts((i,)), choice) - const for i in range(9)]
        prediction = lambda low: const + sum((coeffs[i] for i in low), Fraction(0))
        assert prediction(row["low"]) == value
        covered = {low for low in lows if prediction(low) < 1}
        candidates.append(dict(target=row["target"], source_low=row["low"],
            permutation=row["permutation"], positions=original_pos, choices=choice,
            constant=const, coefficients=coeffs, covered=covered,
            family_max=max(map(prediction, lows))))
        if stop_universal and len(covered) == len(lows):
            break

    remaining = set(lows)
    chosen = []
    while remaining:
        best = max(candidates, key=lambda c: len(c["covered"] & remaining), default=None)
        if best is None or not (best["covered"] & remaining):
            break
        fresh = sorted(best["covered"] & remaining)
        # Independent direct formula checks for every coloring assigned to this
        # selected saved layout, not just the 0/1 interpolation inputs.
        layout = BareLayout(25, best["positions"])
        for low in lows:
            actual = fixed_value(layout, counts(low), best["choices"])
            predicted = best["constant"] + sum((best["coefficients"][i] for i in low), Fraction(0))
            assert actual == predicted, (family["base"], best["target"], low, actual, predicted)
        selected = {k: v for k, v in best.items() if k != "covered"}
        selected["assigned_lows"] = fresh
        selected["covers_total"] = len(best["covered"])
        selected["assigned_max"] = max(best["constant"] + sum((best["coefficients"][i] for i in low), Fraction(0)) for low in fresh)
        top_five = sorted(family["eligible"], key=lambda i: best["coefficients"][i], reverse=True)[:5]
        selected["top_five"] = top_five
        selected["top_five_bound"] = best["constant"] + sum((best["coefficients"][i] for i in top_five), Fraction(0))
        assert selected["top_five_bound"] == selected["family_max"]
        chosen.append(selected)
        remaining.difference_update(best["covered"])
    return dict(base=family["base"], large_blocks=family["large_blocks"], full=full,
        eligible=family["eligible"], incidences=inc, empty_count=empty,
        low_count=len(lows), distinct_contiguous_saved_layouts=len(candidates),
        largest_single_cover=max((len(c["covered"]) for c in candidates), default=0),
        universal_saved_layouts=sum(c["family_max"] < 1 for c in candidates),
        chosen=chosen, uncovered=sorted(remaining))


if __name__ == "__main__":
    started = time.monotonic()
    cert = json.loads((HERE / "Q5_COLORED_CERTIFICATES.json").read_text())
    bounds = json.loads((SOURCE / "V25_NINE_Q5_BOUNDS.json").read_text())["results"]
    full_run = "--all" in sys.argv
    selected_families = list(range(374)) if full_run else [127, 200, 365]
    results = []
    for base in selected_families:
        fam = cert["families"][base]
        rows = [r for r in cert["rows"] if r["base"] == base]
        if "rejection" in fam:
            results.append(dict(base=base, status="degree_rejected", rejection=fam["rejection"]))
        elif not fam["lows"]:
            results.append(dict(base=base, status="fewer_than_five_eligible", eligible=fam["eligible"]))
        elif any("target" not in row for row in rows):
            assert all("target" not in row for row in rows)
            inc = [sum(bool(t & (1 << i)) for t in fam["full"]) for i in range(9)]
            empty = sum(inc) - len(fam["full"]) - 24
            assert empty < 0
            results.append(dict(base=base, status="budget_rejected", empty_count=empty,
                full=fam["full"], incidences=inc, low_count=len(fam["lows"])))
        else:
            r = run_family(fam, rows, bounds, stop_universal=full_run)
            r["status"] = "covered" if not r["uncovered"] else "incomplete"
            results.append(r)
    report = dict(method="existing saved layouts only; fixed A/B/C choice; exact rationals",
        all_saved_contiguous=dict(Counter(str(max(r["positions"]) - min(r["positions"]) == 8) for r in bounds)),
        budget_rejected_families=dict(Counter(r["base"] for r in cert["rows"] if "target" not in r)),
        families=results, wall_seconds=time.monotonic() - started)
    output = "Q5_AFFINE_FAMILY_ALL.json" if full_run else "Q5_AFFINE_FAMILY_PILOT.json"
    (HERE / output).write_text(json.dumps(report, indent=2, default=str) + "\n")
    print(json.dumps({"wall_seconds": report["wall_seconds"], "families": [
        {k: r[k] for k in ("base", "status", "low_count", "distinct_contiguous_saved_layouts",
            "largest_single_cover", "universal_saved_layouts", "uncovered") if k in r} |
        {"chosen": len(r.get("chosen", []))} for r in results]}, indent=2))

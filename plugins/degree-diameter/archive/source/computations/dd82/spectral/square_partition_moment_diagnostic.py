#!/usr/bin/env python3
"""Exact certificate for the conditional n61 interval/five-moment test.

This verifies a positive real atomic measure; its weights are not asserted
to be integer eigenvalue multiplicities. No optimization is run here.
"""

from fractions import Fraction


ATOMS = tuple(Fraction(n, 4) for n in (-15, -13, 7, 9, 11))
WEIGHTS = tuple(
    Fraction(n, 4576) for n in (5238, 108095, 101374, 15314, 44539)
)
EXPECTED = tuple(Fraction(n) for n in (60, -8, 424, -512, 3712))


def inside_proposed_intervals(x: Fraction) -> bool:
    """Check strict membership without approximating either square root."""
    between_outer_roots = (2 * x + 1) ** 2 < 45
    negative_interval = x < -3 and between_outer_roots
    positive_interval = x > 0 and x * x > 3 and between_outer_roots
    return negative_interval or positive_interval


def main() -> None:
    assert len(set(ATOMS)) == 5
    assert all(w > 0 for w in WEIGHTS)
    assert all(inside_proposed_intervals(x) for x in ATOMS)
    moments = tuple(
        sum((w * x**k for x, w in zip(ATOMS, WEIGHTS)), Fraction(0))
        for k in range(5)
    )
    assert moments == EXPECTED, (moments, EXPECTED)
    print("PASS: five distinct interior atoms, positive weights, exact five moments")
    print("atoms:", ", ".join(map(str, ATOMS)))
    print("weights:", ", ".join(map(str, WEIGHTS)))
    print("moments:", ", ".join(map(str, moments)))
    print("Scope: real-measure moment feasibility; no integral-spectrum or graph claim")


if __name__ == "__main__":
    main()

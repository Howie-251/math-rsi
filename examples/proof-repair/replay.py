"""Replay the input's false independence step using exact finite arithmetic.

This checks one intermediate counterexample and union-bound arithmetic.
The universal theorem is the analytic proof in reference/PROOF.md.
Run from any directory with Python 3.9+; no external dependencies or writes.
"""

from fractions import Fraction
from itertools import product


def monochromatic(coloring, edge):
    return len({coloring[vertex] for vertex in edge}) == 1


def main():
    colorings = list(product((0, 1), repeat=5))
    edge_e, edge_f = (0, 1, 2, 3), (0, 1, 2, 4)
    count = len(colorings)
    p_e = Fraction(sum(monochromatic(c, edge_e) for c in colorings), count)
    p_f = Fraction(sum(monochromatic(c, edge_f) for c in colorings), count)
    p_both = Fraction(
        sum(monochromatic(c, edge_e) and monochromatic(c, edge_f) for c in colorings),
        count,
    )
    assert (p_e, p_f, p_both) == (Fraction(1, 8), Fraction(1, 8), Fraction(1, 16))
    assert p_both != p_e * p_f
    print(
        f"32 colorings: P(Be)={p_e}, P(Bf)={p_f}, P(both)={p_both}; "
        f"independence product={p_e * p_f}"
    )
    print("Counterexample to the input's event-independence claim verified.")

    lower_bounds = [1 - Fraction(m, 8) for m in range(8)]
    assert all(bound >= Fraction(1, 8) > 0 for bound in lower_bounds)
    assert min(lower_bounds) == Fraction(1, 8)
    print(
        "Union-bound arithmetic checked for m=0,...,7; "
        f"minimum good-coloring bound={min(lower_bounds)}."
    )
    print(
        "The universal theorem is established by reference/PROOF.md, "
        "not by this finite replay."
    )


if __name__ == "__main__":
    main()

"""Recheck the original proof's false independence subclaim on 32 colorings."""
from itertools import product
from fractions import Fraction

colorings = list(product((0, 1), repeat=5))
e, f = (0, 1, 2, 3), (0, 1, 2, 4)
def mono(c, edge):
    return len({c[v] for v in edge}) == 1
p_e = Fraction(sum(mono(c, e) for c in colorings), len(colorings))
p_f = Fraction(sum(mono(c, f) for c in colorings), len(colorings))
p_both = Fraction(sum(mono(c, e) and mono(c, f) for c in colorings), len(colorings))
assert (p_e, p_f, p_both) == (Fraction(1,8), Fraction(1,8), Fraction(1,16))
assert p_both != p_e * p_f
print(f"32 colorings: P(Be)={p_e}, P(Bf)={p_f}, P(both)={p_both}; independence product={p_e*p_f}")
print("Counterexample to original intermediate claim verified; this is not a theorem-domain enumeration.")

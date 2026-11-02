# Prediction before the one finite gate

Inherit the accepted source106 and actual order-seven generator; do not rerun
its diameter, common-neighbor, automorphism, or previous experiment checks.
The case has consumed 10.585169327 CPU seconds of its unchanged 20-second
budget. This batch has at most 2 CPU seconds including preparation/failures.

Prediction: every invariant pin set S of size10 or11 is one of the fourteen
seven-orbits together with three or four of the eight fixed vertices. None
can yield107/max11/D2 when only old edges inside S can change, even when the
new internal graph does not preserve C7.

Test all 14*(C(8,3)+C(8,4))=1764 choices only through necessary conditions:

1. The source closed neighborhood of S must cover all106 old vertices.
2. Frozen outside degree plus the new z-edge must be at most11.
3. If that sum already equals11, all final internal incidences of that pin
   are forced absent. Every other pin must still be capable of degree10
   after these forced absences, since107/max11/D2 forces minimum degree10.

Prediction: zero choices pass all three. Save explicit failure counts and
per-choice witnesses, not merely a best aggregate. This is not a rewiring
enumeration, solver call or full graph acceptance. If any choice passes,
retain it as unresolved and revisit the paper prediction without claiming
the full rule excluded.

The independent symbolic proof is paper_pinset_invariant/NOTE.md. Its new
interface uses r (source degree inside the seven-orbit), k (fixed neighbors)
and h (selected fixed neighbors), and bounds the closed union by
92+7q-7(r+k+h). This finite test checks the proposed consequence on the
actual14 orbits; it does not replace or generalize that proof.

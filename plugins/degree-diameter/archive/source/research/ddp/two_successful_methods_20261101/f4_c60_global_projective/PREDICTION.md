# One complete global-conic PGL2(F4) gate

Frozen 2026-11-01 before the single numerical call. Input is only the saved
literal C60 with inverse ports1,0,3,2,4. Field F4=F2[w]/(w²+w+1), element
codes0,1,w,w+1. Directions are conic points in order infinity,0,1,w,w+1.
This ordering is fixed; no controller, field, GL3 matrix, offset or seed scan.

**Prediction:** inverse-compatible quotient projectivities can jointly cover
all3300 nonadjacent/equal controller pairs by a full-rank NB3 word. We will
also test the stronger sufficient certificate that all adjacent-edge pencils
cover all five projective quotient directions. Either prediction can fail.

Exhaustive domain:60 choices for port0 quotient projectivity (port1 inverse),
60 for port2 (port3 inverse), and every port4 projectivity admitting a genuine
involutory linear lift. All candidates are checked, not sampled. Forced-rank
cells from the previous1260 unique-distance-three witnesses may prune only
after recording each candidate. Projectivities forget longitudinal matrix
coefficients, which do not affect the rank/pencil conditions being tested.

Completeness guard: compute actual NB2 and NB3 counts for every required
controller pair. If a nonadjacent distinct pair has at most one NB2 and three
NB3 routes, and all NB3 ranks are at most2, the zero-source union has size at
most1+4(16-1)=61<64. For a self pair with at most three NB3 routes, its five
backtrack lines add at most15 nonzero points, giving at most61. Thus a
full-rank route is necessary throughout this **purely linear** scope when
the literal count guard holds. Affine offsets are not covered by this bound.

Scope correction agreed with root: full adjacent pencils are necessary for
ports0,1,4 only if their literal edges have no triangle/C4 routes. Ports2,3
belong to triangles; their extra two-step routes must not be silently
discarded. Record separately (i) rank-only necessary solutions,
(ii) rank plus external-pencil necessary solutions, and
(iii) rank plus every-pencil sufficient solutions. A zero count only in(iii)
does not prove nonexistence in(i) or(ii).

One worker; single hard10CPU call including checks, full projectivity sweep,
and optional first complete graph generation. If(iii) has a solution, lift
it to five explicit matrices, save the3840-vertex20-regular graph and route
certificate, then notify root for the sole independent validation. Otherwise
save the exact negative scope and stop; no continuation by random matrices.

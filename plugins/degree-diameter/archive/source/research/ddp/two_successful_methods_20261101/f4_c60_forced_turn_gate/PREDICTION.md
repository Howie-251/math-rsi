# C60/F4 unique-route forced-rank gate

Frozen 2026-11-01 before the sole numerical call. This tests only the literal
60-vertex controller already bound to the Bhakar author recipe in
`../f7_c60_d35/PARAMETERS.json`. No field matrices, graph lift, graph BFS,
random search, or alternate controller will be generated.

**Prediction to refute:** at least one directed controller edge has so many
forced full-rank turns that its remaining 4-by-4 turn cells cannot contain a
matching of size three, ruling out the five-port F4 arc-frame construction.

For every ordered pair at controller distance exactly three with a unique
nonbacktracking three-word, record its central edge and turn. Its sole fiber
route must have rank three to cover all 64 targets from any source. At each
central edge, five incident directions with every triple independent project
to four distinct points of PG(1,4) on either side. These two four-subsets of a
five-point line intersect in at least three points. Bad turns therefore form
a matching of at least three cells. Forced cells cannot be bad. Compute the
maximum matching of the complement, first per literal edge (arbitrary
edge-dependent charts/local arc frames), then unions for global port charts.

The local frame is allowed to differ by controller vertex, but is shared by
all darts incident at that vertex, with reverse noise-line consistency.
Unrelated incoming/outgoing line systems or non-arc directions are outside
this gate. Passing a matching test is only necessary, not a construction.

One worker, hard CPU limit five seconds, single deterministic run. Save all
forced cells and literal unique-path witnesses. Stop after this gate.

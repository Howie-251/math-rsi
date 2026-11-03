# Michel120/F5 six-port candidate: stopped by the first gate

The proposed `(30,3)` order15000 lift is strictly excluded for the fixed
Michel120 controller, full `F5^3` fibers, full5point affine-line edges,
and no within-fiber edges. This includes arbitrary invertible edge maps
and affine offsets with exact reverse inverse relations.

The new literal-source check found a simple degree6 graph with120
vertices and360 edges. Its actual triangle count is0; the vertex triangle
histogram is `{0:120}`. Vertex0 has neighbors
`[3,78,83,88,92,103]`, with no edges among them. A same-fiber path of
length at most3 therefore projects only to the zero-step word or one of
six two-step backtracks. Each backtrack reaches one5point line through
the source coordinate, because exact inverse maps cancel the affine
offset. Same-fiber radius3 is at most `1+6*4=25`, leaving at least100 of125
targets uncovered. See `PROOF.md`.

The prediction was saved in `PRED.json` before execution. The only new
run used one worker and0.001604957CPU seconds, below the30CPU budget.
There were0 source fetches,0 source/fiber BFS runs,0 fiber graphs,
0 quotient enumerations,0 solver calls, and0 Lean runs. Source provenance
and its known diameter3 were inherited from the existing `m1_sources`
records, without refetching or repeating source verification.

This is a negative route-capacity result, not a constructed graph or an
accepted lower bound. The accepted116/13 counts, stage12/10 counts, and
10 concrete formula Lean instances are unchanged. The conditional
unique-distance3/PGL2(F5) interface was not executed because this first
gate failed. No119/111 controller, within-fiber variant, field/group/seed
ladder, or further search was opened.

Saved artifacts are `check_once.py`, `PRED.json`,
`CONTROLLER_TRIANGLE_PROFILE.json`, `TRIANGLE_FREE_WITNESS.json`,
`RESULT.json`, `TERMINAL.json`, and `PROOF.md`.

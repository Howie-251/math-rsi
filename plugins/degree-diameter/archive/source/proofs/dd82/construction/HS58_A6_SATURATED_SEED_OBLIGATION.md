# HS58 saturated a6: one complete failure witness and the remaining port obligation

Date: 2026-10-12. This bounded task generated one complete graph directly,
with no search, flow, SAT, or auxiliary enumeration. The assignment was
already known to violate a zero-row condition; it is retained as an explicit
failure witness, not as a promising unexcluded completion.

The setting and four zero sets / 56 addition matchings are those of
[HS58_SATURATED_DISJOINT_ALL_ADDITIONS.md](HS58_SATURATED_DISJOINT_ALL_ADDITIONS.md).
Here the original HS labels are 0 through 49, and new label a means vertex
50+a.

## Complete deterministic graph

Take D={01,10-11} and

\[
A=\{25\! -\!26,35\! -\!41,4\! -\!36,45\! -\!46,
14\! -\!33,32\! -\!42\}.
\]

These are six original nonedges forming a matching. Its twelve endpoints
are a mixed saturated zero set. The auxiliary graph is

\[
E(H)=\{02,03,04,05,06,07,12,13,14,15,67\}.
\]

Its degrees are (6,4,2,2,2,2,2,2), so the required old-column sizes are
(2,4,6,6,6,6,6,6). Its only pairs at distance greater than two are 16 and 17.
Set B0=B10={1,6} and B1=B11={1,7}. Give old vertices 30,40,39,48 label 7
and old vertices 2,31,12,49 label 6. These eight assignments cover the
broken old paths, while the four endpoint pairs cover both auxiliary bad
pairs. All twelve zero vertices receive no port.

The remaining 26 old vertices, in increasing order, receive respectively
two copies of label 0 followed by six copies of each label 2,3,4,5. This
fills the exact columns without a flow algorithm or choice procedure.

The saved expanded graph has **58 vertices, 232 edges, every degree 8,
diameter 3, and 89 bad pairs**. Independent BFS finds no old-old or
new-new bad pairs: all 89 are old-new.

Artifacts:

- Generator: `computations/dd82/construction/hs58_a6_saturated_seed.py`.
- Complete labeled graph and attachments:
  `computations/dd82/construction/hs58_a6_saturated_seed_run/seed.json`.
- Plain edge table: the same directory's `seed.edges`.
- Independent BFS, all degrees and all bad pairs: `seed.verification.json`.
- Exact column counts and failure witness: `analysis.json`.
- Resources and outcome: `result.json`.

One successful construction used 0.003694 CPU seconds; the independent
edge-list BFS used 0.030875 CPU seconds. Combined wall time was 0.040412
seconds on one pinned CPU. No solver or flow was started.

## A failure forced before the arbitrary final column filling

Old vertex 33 is zero and has old neighbors
{3,7,11,14,15,24,30,31}. Its eight neighbor-port slots in the saved graph
are 0,2,1,7,2,4,7,6, so new labels 3 and 5 are missed.

In fact some failure is unavoidable for these endpoint ports, regardless
of the final 26 assignments. The old pair (1,30) lost its unique Q path
1-0-30. Neither endpoint has an added old edge, so B30 must lie in
B1={1,7}. Column 1 is already full at the four deletion endpoints, forcing
B30={7}. But B11 also contains 7. Thus zero 33 has a repeated label among
exactly eight available slots and cannot reach all eight new vertices.
This is the local zero-cycle obstruction of
[HS58_A6_SATURATED_PORT_PALETTES.md](HS58_A6_SATURATED_PORT_PALETTES.md).

## Rejected auxiliary proposals were not searches

The trial C8 with opposite chords 15,26,37 has bad pair 04 with degree
sum 4, violating the already proved no-cross endpoint condition in
[HS58_NO_CROSS_ENDPOINT_COVERAGE.md](HS58_NO_CROSS_ENDPOINT_COVERAGE.md).
No assignment calculation was launched for it.

The proposed eleven-edge graph
{02,13,04,24,05,25,06,36,17,27,67} was directly checked on eight vertices.
Its bad pairs are 01,14,15,23,34,35. Four have degree sum 4, and the six
bad pairs also exceed the four available shared-port pairs in this
saturated disjoint-deletion setting. It was withdrawn before any flow
or full-graph generation. Neither proposal is counted as an auxiliary
catalog search or a completion attempt.

## Independent reading of the repeated-palette obstruction

The proof in `HS58_A6_SATURATED_PORT_PALETTES.md` was read independently,
including the mixed-zero edge-budget cases (c,r,e)=(3,8,0),(2,9,0),(2,8,1).
Here c counts edges between the two two-label palettes, r counts their
edges to the four neutral labels, and e includes *all* remaining edges:
inside either palette and inside the neutral set. Thus the three cases
are exhaustive when c>=2, r>=8, and |E(H)|=11.

The final case correctly separates the extra edge inside a palette from
one inside the neutral set. In the first, an on-matching neutral type
still misses the opposite palette vertex. In the second, the missing
cross-palette pair still requires an actual shared neutral neighbor;
the extra neutral edge cannot supply that two-step route. This forces
the opposite type and a forbidden bad pair with an untouched neutral
vertex. The preceding two edge-budget cases and the pure-zero degree
bounds also check out.

That theorem excludes B0=B1 and B10=B11 jointly, for every H with eleven
edges and all four zero sets; its two-list condition first forces the
two repeated palettes to be disjoint. The present concrete seed instead
has B0=B10 and B1=B11 and fails the earlier local two-list condition.
These are distinct restricted endpoint patterns.

The remaining saturated a6 obligation is to assign unequal but
intersecting endpoint pairs for at least one deleted edge, then satisfy
all zero-row colors, exact columns, eleven auxiliary edges and all pair
coverage simultaneously. For example, the formal six-label pattern
B0={a,b}, B1={a,c}, B10={d,e}, B11={d,f} survives the two mixed-zero list
conditions; no full completion is asserted. General a6/a7 are not
excluded by this failed seed or the repeated-palette theorem. This task
stops here without another auxiliary choice, flow, or solver run.

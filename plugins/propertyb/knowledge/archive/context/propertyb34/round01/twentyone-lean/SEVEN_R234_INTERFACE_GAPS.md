# Minimum degree seven: r=2,3,4 interface handoff

2026-10-14. Read-only inspection during the final bounded work interval. Here
r is the number of degree-seven vertices of an actual pair-covering 21-point,
34-edge hypergraph with minimum degree seven. This report does not record any
new branch proof or numeric generation.

The existing sources do not reduce any of r=2,3,4 to one final API repair.
The shortest future branch is r=4, because its vertex selection is immediate
and the new promotion/reconstruction interfaces match its complete paper
classification. It still needs substantial finite coverage and certificate
work. The current single `77778Batch000` contains only 16 strict profiles,
not the full r=4 family.

| Branch | Existing actual H interfaces | Missing connection |
|---|---|---|
| r=2 | `TwentyOneSevenSelection.two_sevens`: at least 15 degree-eight points, at least `6+codegree(x,y)` unit neighbors, mutual codegree two and capacity two on every root edge. `TwentyOneSevenTriples.residual778` bounds all involved seven/eight pairs by two. | Complete `(7,7,8,8,8)` 565-profile classification and residual consequences; the `(7,7,8,8,8,8)` 99-representative classification; actual A/B/C/D pattern bounds and two-matching contradiction. No corresponding `77888`/`778888` formal families were present in the inspected tree. |
| r=3 | `degree_count_budget` gives at least 13 eights. `residual777`, `residual778`, and `unit_neighbors_pair_le_two` supply initial actual pair bounds. | Repeated-pattern selection; complete 1,722-representative `(7,7,7,8,8)` classification and its three residues; four common unit neighbors; 67 labelled `(7,7,7,8,8,8)` extensions and final contradiction. No corresponding `77788`/`777888` formal families were present. |
| r=4 | `degree_count_budget` gives at least 11 eights. `TwentyOneSevenQuads.residual` is the intended actual normalization to nine four-seven residues. `residual778` bounds every pair to a selected eighth-degree point. `TwentyOneSevenFive77778Batch000.propertyB_of_counts` is built for 16 specified profiles. | Complete promotion coverage of all nine old residues, 1,993 strict single-layout witnesses plus seven joint witnesses, their renaming, and dispatch to actual counts. |

For r=4, use this exact route after the quad actual theorem is built:

1. Choose one real degree-eight point using the degree budget. Its degree
   makes it distinct from the four seven-degree points. Extend the normalized
   four-lock embedding by this point as index `Fin.last 4`.
2. Build the nonempty old trace inventory from the selected residual. For the
   promotion capacity use total new degree 8 and four pair capacities bounded
   by 2 (or the exact one/two values).
3. Apply `PromotionCatalog.actual_mem_of_old H f entries cap`. Its assumptions
   are no duplicate entries, old actual counts bounded by the stored inventory,
   and actual new degree/codegrees bounded by `cap`. They come from the old
   residual equality and the actual pair/degree lemmas above.
4. `PromotionCatalog.decode_nonempty` reads the actual promotion back from
   the finite allocation. Then `PromotionReconstruction.extend_actual H f μ p 8`
   recovers every five-lock count, including the empty/new-singleton counts.
5. A complete finite dispatcher must map that recovered profile, after a
   proved degree-preserving permutation, to a strict ordinary or joint caller.
   The 16 existing `77778Batch000` profiles are only a reusable initial part.

`FOUR_SEVEN_EXTEND.json` records exactly 2,000 extensions and
`FOUR_SEVEN_EXTEND_JOINT.json` seven joint witnesses. The paper source is
`../twentyone-math/AT_LEAST_THREE_SEVENS.md`; the r=2 source is
`../twentyone-math/TWO_SEVENS.md`. These saved finite results do not substitute
for Lean coverage.

The `77778Batch000` build is
`build-queue-TwentyOneSevenFive77778Batch000-r19.log`: successful, 1,011 jobs;
its numeric module took 65 seconds and its actual-count caller 1.3 seconds,
with standard three axioms. This demonstrates that extrapolating the same
per-profile expansion to the missing family is not a small final connection.

At inspection, `TwentyOneSevenQuadCoverage` was built in the r25 log, while
`TwentyOneSevenQuads` itself had one count-representation rewrite error and
its source was being repaired by the unique executor. Use the next successful
actual-module log before counting its `residual` theorem as verified. This
status note is an inspection timestamp, not a claim that the pending repair
will remain open.

The existing degree-six files named `TWO_SEVENS_HELPER.md`,
`TwentyOneSixTwoSevens`, and `TwentyOneSixManySevens` prove different branches
with a degree-six vertex. They cannot close these minimum-seven inputs.

# Fixed GF(4) chart: exact short-route inventory and C19 obstruction

Only the cached INTERFACE.json was read. The 16384-vertex source was
not parsed again. No graph, controller search or BFS was performed.
The multiplication tables reuse the source probe's encoding:
GF(4)={0,1,w,w+1}, w²=w+1, with a fiber byte x0+4x1+16x2+64x3.
The inverse types are 0↔3 and 1↔2. All four canonical matrices have
rank 3. They were never inverted or treated as bijections.

A route is composed as the actual relation y=Mx+lambda*d. Its output
direction space is updated by applying the next M to the previous
space and adjoining the next d. Consequently a word's fixed-source
image has exactly 4^rank points. Singular canonical representatives
cause no problem for this relation computation.

| Length | Reduced words | Reduced image-rank inventory |
|---|---:|---|
| 0 | 1 | one rank 0 |
| 1 | 4 | four rank 1 |
| 2 | 12 | twelve rank 2 |
| 3 | 36 | thirty-six rank 3 |
| 4 | 108 | ninety-six rank 4, twelve rank 3 |

The twelve deficient reduced four-words are 0022,0113,0223,1101,1102,
1133,1322,1331,2002,2200,2322,3311. Each has a 64-point hyperplane
image; its exact missing-direction normal is recorded in RESULT.json.
The other 96 four-words individually cover all 256 fiber points for
every source vector.

Capacity bounds retain all 341 words of length at most 4, including
controller backtracks. An inverse letter pair does not cancel as a
fiber relation: it may return to another point of the same fiber.
The sum of individual image cardinalities is 35201, giving only the
necessary controller bound n≤137. A sharper safe bound groups words
by free reduction solely because their controller endpoints coincide;
it takes the union of all actual images within each class, without
discarding any backtracking route. These 161 class unions have total
cardinality 30914. Every zero-source image contains 0. Thus, if all n
controller fibers are fully covered,

    255*n <= sum_classes(|image_union|-1) = 30753,

so n≤120. This is a necessary bound, not a construction or sufficient
certificate. It leaves room above the source's 64 fibers; it does not
show that such a controller exists. Its scope is these fixed zero-
constant relations and inverse-consistent deterministic controller
ports. WORD_IMAGES.json preserves every word's exact zero-source image.

The separate agent's fixed C19/76-controller experiment was diagnosed
using only those cached images and its saved controller transition
table. All 963 first-root missing fiber points match its native graph
result exactly, including all nonreduced routes. This is an explanation
of that existing experiment, not a second graph experiment or method.

Four targets have a unique route of length at most 4:

| Target controller | Only word | Image | Missing |
|---:|---|---:|---:|
| 30 | 0022 | 64 | 192 |
| 32 | 3311 | 64 | 192 |
| 42 | 2002 | 64 | 192 |
| 47 | 2322 | 64 | 192 |

These are rank-3 route obstructions, not merely failure of a full-rank
sufficient test. For this old fixed controller, changing affine offsets
alone cannot enlarge a unique word's rank-3 image beyond 64. This
statement does not concern other controllers or all subsequent batches.

The reduced-two-word target 61, reached by word20, has eleven actual
words including backtracks. Its eight rank-3 routes represent four
distinct 64-point hyperplanes with a common 16-point core; all three
rank-2 routes lie in their union. Their union is exactly
16+4*(64−16)=208, leaving 48 points. GF(4) needs the fifth member of
this pencil to fill the fiber. This is the concrete distinction from
the analogous four-member GF(3) pencil. Targets2,17,39 each cover220
and miss36. Target0 has35 words: identity, eight rank1, twenty-four
rank2 and two rank3; their union is217, leaving39. All bases, word
lists and exact missing IDs are in C19_SLOT_ANALYSIS.json.

The word inventory used 0.105964 CPU seconds; cached C19 classification
used 0.006315 seconds. No further chart, offset or controller trial was
started here. Both analyses are terminal with no pending computation.

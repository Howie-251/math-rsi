# q41 coset tower: two complete finite generator families

The prescribed q41 batch is **complete with no diameter-5 solution**. It
handled all **15,560 type-A candidates** and **7,372 type-B candidates**.
The necessary head-to-head test excluded 7,742 candidates; all remaining
15,190 were scored exactly from the three group orbits. There was no
restart, additional parameter, or free-port search.

The saved best among candidates passing the head-to-head test has

`S={(1,6),(16,14),(34,7),(26,13)}`,

comprising two inverse pairs. Its leaf, block and head root missing counts
are **84, 64 and 60**. An independent agent parsed the complete edge list
and ran the existing generic checker from **all 1,066 vertices**. This
confirmed a **simple, connected, 5-regular graph with 2,665 edges, diameter
7 and 42,230 unordered pairs at distance greater than 5**. The independent
result agrees exactly with the weighted three-root score. See
`search.best.edges`, `search.best.json` and `best.independent_verify.json`.

At the parent's request, exactly three additional ordinary BFS runs on this
saved graph decomposed each root's missing targets by layer:

| Root layer | Missing leaf targets | Missing block targets | Missing head targets | Total |
|---|---:|---:|---:|---:|
| Leaf | 69 | 13 | 2 | 84 |
| Block | 52 | 8 | 4 | 64 |
| Head | 40 | 20 | 0 | 60 |

With orbit sizes 820,205,41, these give **28,290 leaf–leaf**, **10,660
leaf–block**, **1,640 leaf–head**, **820 block–block**, **820 block–head** and
**zero head–head** bad unordered pairs. The head-head condition is fully
satisfied, but all five other layer-pair classes still contain failures.
The largest remaining counts are leaf–leaf and leaf–block.

`best.three_root_targets.json` retains the target-layer distance histograms
and every missing vertex ID and group coordinate. This diagnosis used
0.002834 CPU seconds and did not rerun the candidate enumeration.

## Exact reconstruction of the source650 graph

Before the new search, the new C++ implementation reconstructed the q25,
r=2 graph using

`S={(21,9),(17,11),(1,10),(10,10)}`.

Its leaf label is `x+25*i`, block label `500+x+25*b`, and head label
`625+x`. The supplied original source uses block label `500+5*x+b`.
Applying exactly this block-label permutation, leaving all leaves and heads
unchanged, made **all 1,625 reconstructed edges equal to the original
`rithwik650_source.edges`**, with no missing or extra edge. The three orbit
roots all had missing count zero. The existing generic checker additionally
verified all 650 roots, degree 5 and diameter 5. `preflight.json` records
the comparison and `q25_source_check.edges` preserves the new labelling.

This baseline uses `Z_25`, not the field with 25 elements. The new q41
enumeration uses the prime field / cyclic additive group `Z_41`.

## Graph definition and exact scoring

Use `G=Z_q semidirect C20`, with

`(x,i)(y,j)=(x+r^i*y mod q, i+j mod20)`.

There are `20q` leaves labelled `x+q*i`, `5q` blocks labelled
`20q+x+q*b`, and q heads labelled `25q+x`. Leaf `(x,i)` is attached to
block `(x,i mod5)`; block `(x,b)` is attached to head x. The four leaf
neighbours of `(x,i)` are its right products by S. Distinct, nonidentity,
inverse-closed S gives a simple 5-regular graph on `26q` vertices.

Left multiplication acts on the three layers, corresponding to `G`,
`G/H` and `G/K` for `H=<(0,5)>` and `K={(0,i):i in C20}`. It preserves
the Cayley edges and both parent maps. Thus one leaf, one block and one
head root give exact distance-5 missing counts `a,b,c`. At q41 the total
number of bad unordered pairs is exactly

`(820*a+205*b+41*c)/2`.

The implementation uses full ordinary BFS to depth 5 from these three
roots, and optimizes that weighted count. It asserts that the weighted
ordered count is even. The independent final check uses the complete edge
list and all roots, without orbit inference.

## Candidate preservation and declared limits

The only normalization used is simultaneous scaling `x -> lambda*x` for
nonzero lambda in `F_41`. It preserves the subgroups H and K. No inner
conjugation by a translation, free port permutation, or other parameter
reduction was applied.

There are 820 group elements, one identity and 41 involutions. The other
778 elements form exactly **389 noninvolutory inverse pairs**. The
representative is the smaller integer leaf label in each pair; the list is
saved in `search.inverse_pairs.json`. This includes all nine pairs with
translation x=0.

- **Type A:** one noninvolutory inverse pair and two distinct involutions.
  At least one of the involutions has nonzero translation, so scale it to
  `(1,10)`. The other is `(v,10)` for all `v!=1`, including v=0. There are
  `40*389=15,560` candidates.
- **Type B:** two distinct noninvolutory inverse pairs. If every generator
  has x=0, neither leaf nor tree edges connect different x values, so D5
  is impossible. Otherwise choose a nonzero-translation element and scale
  it to `(1,i)`, for every `i!=10`. For each of these 19 choices, visit all
  389 second-pair representatives and reject exactly the one equal to the
  fixed first pair. This gives `19*389=7,391` loop slots, 19 invalid
  duplicates, and **7,372 valid candidates**.

**Four-involution generating sets were not enumerated here.** Any separate
structural exclusion of that third type belongs to the parent's mathematical
coverage argument. This report's computational scope is exactly A and B;
it does not claim that the program searched all inverse-closed S.

## Head-to-head filter and exact counts

A path of length at most 5 from one head to another distinct head must
descend two tree edges, cross exactly one leaf edge, and ascend two tree
edges. Consequently the reachable differences between head labels are
exactly the union of `s_x*<2>` for nonzero generator translations `s_x`.
Since 2 has order 20 in `F_41*`, this group has two multiplicative orbits,
the square and nonsquare classes. Every D5 candidate must meet both.
This condition is sufficient only for the head-head pairs, not for D5 of
the full graph.

The filter counts can also be derived without running the candidate loop.
Of the 389 inverse pairs, 190 have square nonzero translation, 190 have
nonsquare translation, and nine have zero translation. Taking inverses
preserves the class because `-1=2^10`. In A, 20 possible second involution
translations are nonsquares and automatically complete the head coverage;
the other 20 require a nonsquare inverse pair. In B, the first normalized
pair has square translation, so its second pair must be one of the 190
nonsquare pairs. The observed counts match these formulas exactly:

| Type | Raw loop slots | Invalid duplicate pairs | Valid candidates | HH excluded | Exact three-root scores | Best scored bad pairs |
|---|---:|---:|---:|---:|---:|---:|
| A | 15,560 | 0 | 15,560 | 3,980 | 11,580 | 46,330 |
| B | 7,391 | 19 | 7,372 | 3,762 | 3,610 | 42,230 |
| Total | 22,951 | 19 | 22,932 | 7,742 | 15,190 | 42,230 |

HH-excluded graphs were not fully scored. Thus the reported best is a
minimum over **HH-passing candidates**, not a claimed minimum bad-pair
count over all 22,932 candidates. The exclusion of D5 in both complete
families is nonetheless valid, because the skipped candidates necessarily
fail a head-head pair.

Type A's best is also saved: `S={(1,10),(23,10),(34,2),(12,18)}`, with
three-root missing counts 84,88,140 and 46,330 bad pairs. Its parameters
and complete graph are `search.A.best.json/.edges`; type B is saved as
`search.B.best.json/.edges`. Only the overall saved best received the
requested independent final full-root verification.

## Profile, budget and terminal

The first **1,000 loop slots** formed the requested profile and were not
rerun. They included 602 fully scored candidates and used **0.031922 CPU
seconds**. Charging every remaining slot at the observed cost per scored
candidate estimated **1.19591 CPU seconds** total, well below the available
118.214 seconds. The same process therefore continued from slot 1,000.

Actual search CPU was **0.414966 seconds**. Compilation, source reconstruction,
source verification, profile, full search and orchestration together used
**1.70 CPU seconds**, against the single-worker 120-second limit. The final
independent best-graph checker reported approximately 0.01579 seconds.

The terminal is `COMPLETE_NO_SOLUTION`, with cursor 22,951 and no next
parameter. Stop-on-D5 was enabled; no hit occurred. `search.profile.json`
and `search.terminal.json` retain the actual profile, all count categories,
both complete score histograms and terminal cursor. `terminal.json` combines
the preflight, runtime and independent validation references. `run.log`,
the source and executable are preserved. All new files are confined to this
directory; Wiki and HTML were not changed.

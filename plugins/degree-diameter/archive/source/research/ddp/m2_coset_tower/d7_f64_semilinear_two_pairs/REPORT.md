# Semilinear F64: complete two-pair/two-involution branch

All **41,490,060 normalized inputs** are complete, with **no diameter-5
solution**. Of them, **38,982,510 passed HH** and **18,524 passed exact BB**;
all 18,524 received ordinary three-root BFS on the actual 3,200-point
graph. None achieved simultaneous head-root and block-root coverage.

The best graph **among the BB-passing, fully scored candidates** has
**38,976 bad unordered pairs**. Independent BFS from all 3,200 vertices
confirms a simple connected 7-regular graph, 11,200 edges and **diameter
6**. This is a negative result for the complete declared construction
branch, not a new degree-diameter record or a claim about arbitrary
3,200-point graphs.

## Complete range and actual stage counts

The group remains the faithful semilinear group

`(x,a,e)*(y,b,f)=(x+r^a*y^(8^e),a+8^e*b mod21,e+f mod2)`

over `F2[t]/(t^6+t+1)`, with r=t^3 of order 21. The tower subgroups are
K of order 42 and `H=<r^7,Frob8>` of order 6. The true group inverse,
the complete lists of 87 involutions and 1,300 noninvolutory inverse
pairs, and the three layer sizes 2,688/448/64 were retained.

The normalization proof and exact orbit lists are in [SCOPE.md](SCOPE.md)
and `normalization_inputs.json`. The implementation compared every
involution, both complete second-involution orbit lists and all their
members, and the 45 type-II involutions with those independent lists
before execution. All comparisons matched.

| Type | Raw = legal | HH passes | HH failures | BB passes = three-root BFS |
|---|---:|---:|---:|---:|
| I: at least one A21 involution | 33,774,000 | 31,274,334 | 2,499,666 | 17,821 |
| II: no A21 involution | 7,716,060 | 7,708,176 | 7,884 | 703 |
| Total | **41,490,060** | **38,982,510** | **2,507,550** | **18,524** |

There were **zero invalid inputs**. The actual total and per-anchor HH
counts agree with the independent scope formulas. Type I has 40 anchors:
two normalized first involutions, each with 20 Frobenius2 representatives
for the second involution. Each anchor includes all C(1300,2) different
unordered inverse-pair choices. Type II has six normalized first inverse
pairs; each anchor includes all 990 unordered choices of two of the 45
non-A21 involutions and all 1,299 remaining inverse pairs.

The allowed Frobenius action is `(x,a,e)->(x^2,2a mod21,e)`. No arbitrary
field scaling, old cyclic inverse, or extra projective reduction was
used. The two actual involutions and the two actual inverse pairs are
distinct within every generator set. Full candidate-preservation
parameters and the enumeration order remain in `profile_metadata.json`
and `generated_scope.json`.

All **46 anchors are complete**. Their raw/legal/HH/BB/scored counts,
root-zero counts, component minima, best scored values and exact cursor
intervals are in [ANCHOR_COUNTS.csv](ANCHOR_COUNTS.csv), with structured
records also in `terminal.json`. These are counts of normalized inputs,
not nonisomorphic graphs.

## Root statistics and the remaining coverage failure

The following root statistics are conditional on the BB passes that
actually received complete three-root BFS. Component minima need not
occur for the same generator set.

| Type | Best scored bad pairs | Min root misses L/B/H | Root-zero counts L/B/H | Joint H+B zero |
|---|---:|---|---|---:|
| I | 38,976 | 24 / 9 / 0 | 0 / 0 / 2,481 | 0 |
| II | 154,560 | 103 / 54 / 0 | 0 / 0 / 171 | 0 |

Thus **2,652 scored candidates** have complete head-root coverage, while
no scored block root has complete coverage. The 2,652 count is not a
count of all head-zero inputs in the raw range. However, simultaneous
head-and-block coverage is zero across the complete normalized range:
an HH failure precludes full head-root coverage, and a BB failure
precludes full block-root coverage. Every remaining input was fully
scored and also failed the joint condition.

The exact BB filter is `H W3 H union K W1 H union H W1 K`, with the actual
three- and six-point H orbits and both head-mediated terms. HH and BB
failures were rejected by necessary conditions; they were not counted
as full BFS checks. Every BB pass was checked in the actual graph, using
the exact weight

`(2688*missing_leaf + 448*missing_block + 64*missing_head)/2`.

This full-score minimum is claimed only over the 18,524 scored inputs.
Filtered inputs were not scored for their total bad-pair count.

## Saved best graph and independent full-source check

The first saved best has cursor **24,215,550**, type-I anchor **28**, and
inverse-pair table indices `(563,1180)`. Its two involutions and two
inverse pairs expand to

`[(1,0,1),(33,0,0),(51,9,0),(8,12,0),(36,11,1),(12,17,1)]`.

Its exact root misses are **24,30,0**, with zero BB missing blocks, giving
**38,976 bad unordered pairs**. The complete graph and parameters are
`production.best.edges` and `production.best.json`.

The source agent ran the existing generic full-source checker **once**
on that saved graph. `best.independent_verify.json` records all 3,200
roots checked, n=3,200, m=11,200, minimum and maximum degree 7, no
unreachable pairs, **D=6**, and exactly **38,976 pairs at distance 6**.
The checker took 0.269335 seconds. Its `valid=false` means the graph fails
the requested D5 bound. The old preflight graph was not rechecked.

The failure layers follow from the verified root data and transitivity,
without another BFS. Head-root missing zero means all head-involving
pairs are covered. BB is also covered. Hence the block root's 30 missing
vertices are all leaves. Undirected double counting gives
`448*30/2688=5` missing blocks from a leaf root; the other `24-5=19`
missing vertices are leaves. Consequently:

| Bad-pair type | Count |
|---|---:|
| Leaf–leaf | 25,536 |
| Leaf–block | 13,440 |
| Leaf–head, block–block, block–head, head–head | 0 |
| Total | **38,976** |

This is a deduction from the already checked graph, not a separate
claimed computation. The saved best solves all head routes and BB, while
leaf–leaf and leaf–block coverage remain incomplete.

## Profile, uninterrupted continuation and resources

Exactly one new graph containing involutions was used for preflight.
Its independently reconstructed 11,200-edge set matched; all 448 BB
targets matched the exact formula, and a full-source check gave D6 and
368,928 bad pairs. `preflight.independent_check.json` and
`preflight.independent_verify.json` preserve that calibration. No old
three-pair preflight or historical candidate enumeration was repeated.

The original profile covered `[0,2000)`, found no BB pass and stopped.
Its timing was too short for a reliable direct extrapolation, so the
production decision used the completed same-group three-pair run's
approximately **86-second frontend** cost reference. This reasoning is
preserved in `PROFILE_REPORT.md` and `cost_estimate.json`.

The separately authorized single-worker continuation covered
`[2000,41490060)` in one process. At global cursor **1,000,000**, it had
processed 998,000 new raw inputs, 980,069 HH passes and 1,323 BB passes
in **2.15007 CPU seconds**. Stage costs were HH 0.16399, BB 1.01994,
three-root BFS 0.148014 and other loop/timing work 0.801462 seconds.
This actual observation is saved in `production.first_million.json`.
Later progress observations were logged without stopping or restarting.

The continuation executable used **85.679821 CPU seconds**. Including
the original profile, independent list/sample checks, preparation and
the continuation compilation, cumulative charged CPU was **89.786032
seconds**. The final independent best-graph checker was a separate
0.269335-second run. The work stayed comfortably within the authorized
300-second cumulative budget. Stop-on-D5 was active; no hit occurred.

The final cursor is **41,490,060**, with no next parameters, and the
status is `COMPLETE_NO_SOLUTION`. The original prefix remains preserved
in `profile.run.json`; the final `terminal.json` contains complete
per-type and per-anchor results and the independent verification. No
extra parameter, generator composition or proof-assistant certification
was started by this batch.

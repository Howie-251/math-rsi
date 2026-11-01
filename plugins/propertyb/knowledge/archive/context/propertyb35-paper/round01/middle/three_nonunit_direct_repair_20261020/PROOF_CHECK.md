# qΓ(F)=3: complete threshold-domain diagnostic

This is a complete diagnosis of the specified one-red-in-F / uniform outside color / arbitrary red-event-tree bound. It is **not** a proof that Γ-degree3 forces Property B. No original hypergraph, outer four-set layout, LP, permutation-layout search or Lean build was generated.

Fix the actual original edge F on five vertices. Its three exceptional original edges have traces T of sizes0,2,3,4; repeated traces are allowed. The other31 original edges meet F exactly once, so the attachment counts a_v are nonnegative with sum31. Given v as F's unique red vertex, choose r red vertices uniformly among the16 outside vertices.

The union bound is

`U_v(a,r)=a*C(12,r−4)+(31−a)*C(12,r)−max(a−1,0)*C(8,r−8)+ΣE(T,v,r)`.

The red attached original edges are distinct, and their exterior four-sets have pairwise union at most8. Every red pair therefore has at least C(8,r−8) joint bad samples. Hunter's tree inequality subtracts a−1 such terms. The exceptional bad sample counts are exactly those specified by the parent: zero if a nonempty trace contains v; C(11,r−5)+C(11,r) for an empty trace; and C(11+j,r) when v is absent and trace size j≥2. Thus every strict integer inequality U<C(16,r) certifies proper coloring of the original H.

## Thresholds do not hide nonmonotonicity

For every one of the35 unordered residual-type triples from {P,0,2,3,4}, `VERIFY.py` scans every a0…31 and every r0…16 using exact integer counts and Fraction comparisons. It records the entire safe and failed a sets, and the best exact (r,U,D) at every a. The first failed a is k; an additional algebraic calculation derives the same safe prefix from the r≥9 branches.

For r≥9, both first increment R−B and later slope R−B−J are nonnegative. The fixed r displayed in `THRESHOLDS.md` therefore certifies all a≤k−1 from the strict certificate at a=k−1. At r8 the later slope is −1, so claiming monotonic increase there would be wrong; the code directly proves the whole r8 domain is non-strict. All r≤7 branches were independently checked in the full finite a/r scan, and any safe large-a tails are retained in the exact composition filter. We never infer that a≥k means failure without checking the full safe set.

## Two different complete trace domains

There are26 allowable five-bit traces and C(28,3)=3276 unordered triples with repetition. The first implementation directly applies all120 actual S5 permutations to every triple and obtains91 orbits, retaining exact label multiplicities.

Independently, the three traces partition F into eight incidence cells, indexed by their membership in the three exceptions. Enumerate all weak compositions of five into eight cells, retain row sizes0/2/3/4, and quotient by the six S3 permutations of exception indices. The resulting91 cell orbits match the first domain. Their labeled unordered triple counts, derived from vertex multinomials and repeated-row multiplicities, match separately on **every orbit**, and total3276. This verifies repeated traces and all actual relabelings without assuming the exceptional original edges are Γ-leaves.

For each trace orbit, the five actual attachment coordinates have their fully computed failed a sets. A sum-index convolution counts exactly the failed choices with total31 and returns a witness. This represents all C(35,4)=52360 attachment compositions per orbit, without materializing them. It closes68/91 orbits. The23 remaining orbits have only119 failed attachment compositions altogether. Their first-failure threshold sums are at least28, so generating the remaining31−Σk≤3 units gives a small second exact reconstruction, and reproduces all119 counts.

## Actual A2/A3 necessary constraints

The second script evaluates original F-degrees as `d_v=1+a_v+h_v`, where h_v is the number of exceptional traces containing v. It then keeps only degree≥6, at most one degree6, and `Σ_F max(d_v−9,0)≤4`. The latter follows from the parent's global high-excess bound, but is used solely as a necessary local restriction here. It also separately reports the count satisfying at most two / at most three degree7 vertices in F, appropriate to the respective role spectra. No assumption F contains the unique six-degree vertex is made.

The local restrictions leave16 trace orbits and83 attachment compositions. Thus even this actual necessary domain is not closed by the specified generic bound. `TAIL_TABLE.md` gives all23 residual rows, their five k values, five h values, original degrees at the minimal failed vector, high excess, and surviving tail counts. `TAIL_RESULT.json` lists every one of the119 generic and83 actual-necessary tail compositions.

One concrete actual-necessary witness is traces `(7,11,28)` with a=`(6,6,6,6,7)`. The traces are `{0,1,2}`, `{0,1,3}`, `{2,3,4}`. Their membership counts are h=`(2,2,2,2,1)`, so all five original F-degrees are9 and the local high excess is0. Every v and every r0…16 fails this union upper-bound criterion. This is not an original-H realization or a noncolorable example.

A second prominent tail is `(7,25,30)` with a=`(4,6,6,6,9)`, giving original F-degrees `(7,9,9,9,12)` and high excess3. Its orbit has35 actual-necessary tail compositions, the largest remaining family.

## Reproduction and budget

```
python3 VERIFY.py
python3 FILTER_TAIL.py
```

The recorded complete finite threshold/orbit calculation used0.139927 CPU seconds, and the actual-tail filter0.001461 CPU seconds, well within the authorized15 CPU seconds. No larger domain was explored. Output is same-family/provisional as a review; exact event formulas, full finite domains, per-orbit multiplicity agreement and integer/Fraction results are the reproducible evidence.

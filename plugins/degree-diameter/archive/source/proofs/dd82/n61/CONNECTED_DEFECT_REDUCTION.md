# Arbitrary order61 targets have connected weighted defect

## Theorem and exact scope

Let G be a finite simple undirected graph on61 vertices, of maximum
degree at most8 and diameter at most2. For its actual adjacency A, put

`B=A^2+A-7I61-J61`.

Then the positive support of B is connected.

This is a computer-assisted structural theorem about every order61
target. It does not prove that such a target exists or that order61 is
impossible. B is not assumed binary. No automorphism, prescribed
partition, triangle restriction, CP02 H/no-O guard, or historical RAW
closure is an assumption. The connected case remains an original-graph
problem. No Lean proof of this new theorem is claimed.

Status: integrated after the three actual joint-enumeration batches and
their saved-model/input-coverage check completed. Scoped integration received reused-agent same-family PASS, sound-modulo-imports;
same-thread Gemini round4 accepted this theorem and closing the disconnected-defect mechanism
(reviews/dd82/20261013_V3_n61_connected_defect_review.json). Prior independent local
checks of the lifting lemmas and code are explicit imports below.

## 1. Exhaustive mathematical alternatives

The original radius-two bound gives degree8 at every vertex, since a
vertex of degree at most7 reaches at most57 vertices. Thus B is symmetric
nonnegative integral, has zero diagonal and row sum4, and AB=BA.
Its four-eigenspace consists exactly of vectors constant on each positive
support component. Commutation makes that partition equitable for A.

With component sizes n_i and adjacency quotient Q, the same original A
therefore gives

`Q1=8*1`, `n_i*q_ij=n_j*q_ji`, `Q^2+Q-11I=1*n^T`,
`sum n_i=61`, `n_i>=2`, `0<=q_ii<n_i`, `n_i*q_ii even`.

The rational contrast space has conjugate eigenvalues
`(-1+3sqrt(5))/2` and `(-1-3sqrt(5))/2` with equal multiplicity m.
Consequently `c=2m+1`, `trace Q=8-m`, and `m<=8`. The exhaustive
component-count alternatives are c=1,3,5,7,9,11,13,15,17.
Full derivation: [GENERAL_THREE_DEFECT_COMPONENT_QUOTIENTS.md](GENERAL_THREE_DEFECT_COMPONENT_QUOTIENTS.md).

The c=3 alternative is already excluded: its full91,125-matrix
classification leaves only sizes(6,25,30) and(12,21,28), and both actual
lifts are impossible. The scoped combined proof and dependencies are
[prompts/26101310-1/final.md](../../../prompts/26101310-1/final.md).
Neither its classification nor its completed calculations were rerun.

## 2. Complete necessary size domain for c>=5

[LARGE_DEFECT_COMPONENT_QUOTIENT_DOMAIN.md](LARGE_DEFECT_COMPONENT_QUOTIENT_DOMAIN.md)
proves that every size is7-smooth, has3-adic valuation at most2, and is at
most `floor(8(65-2c)/9)`. For each diagonal d it also proves the exact test

`(122d-17n_i+61)^2 <=45(61-n_i)^2`.

For each unordered interface, g=gcd(n_i,n_j) gives the full domain

`q_ij=(n_j/g)t`, `q_ji=(n_i/g)t`,
`0<=t<=min(g,floor(8g/n_i),floor(8g/n_j))`.

The exact row sums and diagonal polynomial entries require, using the
same t choices within each row,

`sum q_ij=8-d`, `sum q_ij*q_ji=n_i+11-d-d^2`.

The necessary global norm theorem in
[COMPONENT_QUOTIENT_GLOBAL_OBSTRUCTIONS.md](COMPONENT_QUOTIENT_GLOBAL_OBSTRUCTIONS.md)
further gives `product n_i=a^2 or5a^2`. The successive complete integer
screens retain every actual quotient's size tuple and actual diagonals:

| Stage | Inputs | Survivors | Actual CPU seconds |
|---|---:|---:|---:|
| Sorted size-domain count | — |36143|0.001083823|
| Diagonal, trace, support and capacity screen |36143|25196|2.908794415|
| Joint row-sum/diagonal-moment screen and trace support |25196|142|4.428952082|
| Global quadratic-norm screen |142|65|0.000041169|

The final65 domains by c=5,7,9,11,13,15,17 number
`4,3,10,11,18,10,9`. Their complete sizes and retained per-row diagonal
domains are in `computations/dd82/n61/component_norm_screen.result.json`.
Per-row trace support is necessary, not a list of jointly feasible
diagonal tuples; the next search enforces the actual common trace.

## 3. Actual exhaustive joint quotient enumeration

The source `computations/dd82/n61/component_joint_quotient.py` assigns
complete rows using the full balanced interface domains, exact two-moment
suffix DP, common assigned interfaces and trace. Every newly completed
row tests every off-diagonal polynomial entry against previously assigned
rows. Nonnegative partial dot products only reject when exceeding the
necessary target. Once complete, direct integer matrix multiplication
checks all equations. Matching-edge diagnostics are post-model only.

The original modes enumerate all labelled Q. The final unresolved mode
retains at least one representative under simultaneous permutations
fixing assigned indices and the current row. It sorts current entries
only among unassigned columns with identical size, original diagonal
domain and all assigned-row column entries. These permutations preserve
the assigned state, sizes, domains and equations; sorting then retains a
completion. Induction proves coverage. It need not yield unique
representatives. The full proof is in the companion source plan.

Actual disjoint completed coverage is:

| Batch | Complete size domains | Actual result | CPU / wall seconds |
|---|---:|---|---|
| profile |7 (all c5,c7)|3 labelled Q in2 size types|0.005236232 /0.008298770|
| remaining |40 (all c9,c11,c13 and first c15)|no Q in these40|57.002655322 /57.617550682|
| unresolved, stabilizer reduction |18 (other c15 and all c17)|no Q|0.382438874 /0.387258556|

The remaining batch interrupted its next input. That interruption is
not exclusion evidence: only its40 completed domains are used. The
changed final search handled exactly the18 unfinished domains, preserving
the old outputs and rerunning none of the47 completed domains. Its
dedicated two-positive-example sanity check retained both known Q types.

Raw files are `component_joint_quotient.profile.json`, `.remaining.json`
and `.unresolved.json` in the same directory. The independent saved-result
checker `component_joint_results_check.py/.result.json` confirms exactly
65 distinct completed domains, no missing or duplicate completed domain,
unchanged input diagonal domains, all returned Q equations, and membership
of all three labelled outputs in the two lifting cases below. Its actual
CPU was0.002639634 seconds. It does not independently rerun or certify
search exhaustion: that part rests on the reviewed exhaustive algorithm
and its terminal records. This is not a solver UNSAT or Lean certificate.

The source review and stabilizer-delta review are
`component_joint_quotient_code_review.md` and
`component_joint_quotient_symmetry_delta_review.md`. They are scoped
same-family provisional reviews. They found no blocking defect.

## 4. Every surviving abstract quotient is unliftable

The three labelled outputs form precisely these two types up to
simultaneous equal-size relabeling:

```text
n=(2,5,6,18,30)
Q=0 5 3 0 0
  2 0 0 0 6
  1 0 1 6 0
  0 0 2 1 5
  0 1 0 3 4

n=(3,3,15,15,25)
Q=0 3 5 0 0
  3 0 0 5 0
  1 0 2 0 5
  0 1 0 2 5
  0 0 3 3 2
```

For the first, the size6 and18 induced adjacencies are matchings S,T,
and their positive quotient edge has no common third support neighbor.
The actual binary cross-block satisfies `SX+XT+X=J`. The matching
involutions force `SX=X=XT`, hence `3X=J`, impossible.
See [COMPONENT_MATCHING_EDGE_OBSTRUCTION.md](COMPONENT_MATCHING_EDGE_OBSTRUCTION.md).

For the second, its actual size15 block is C15 and each cycle of the
size25 block has length5,10,15,20 or25. The block Sylvester equation
and the exact five-entry resonance calculation imply that every binary
column has only periods5 and3. Its column weight3 excludes period3,
so every column has period5. Three identical rows of weight5 contribute
at least `2*(5-1)=8` to a defect row of sum4, a contradiction.
See [COMPONENT_PERIODIC_COLUMN_OBSTRUCTION.md](COMPONENT_PERIODIC_COLUMN_OBSTRUCTION.md).

These are obstructions to the same actual A and B. They do not deny that
the abstract integer Q exist. Both persist under component relabeling.
The fresh scoped proof-checker in
`reviews/dd82/proof-checker-n61-norm-lifting-20261013/` checked the full
norm and lifting arguments, including one independent exact check of
the new five-entry resonance table. The size-two capacity lemma is an
additional explanation of the prior bottleneck, not a dependency of
the completed final search or of this theorem.

## 5. Conclusion and next original-graph obligation

Every possible c>=5 actual quotient is covered by the complete necessary
domain and joint search, and every returned quotient has no actual lift.
Thus c>=5 is impossible. Together with the inherited c3 exclusion and
the exhaustive odd-count alternative, this forces c=1.

For c=1 the quotient is merely Q=(8); further quotient-size enumeration
has no content. Close the disconnected-defect mechanism after actual
result review. Any continuation at61 must concern a connected symmetric
weighted row-four B coming from the same binary eight-regular A, or an
actual graph construction. Do not extend the historical simple-defect
CP02 classification to weighted B without proof. Arbitrary58,59,60 and
61 targets remain unresolved; the project interval is still57<=N(8,2)<=61.

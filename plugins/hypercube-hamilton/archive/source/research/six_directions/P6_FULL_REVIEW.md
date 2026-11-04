# Independent final audit of complete P6

Reviewer: `/root/p6_final_independent_audit`, requested GPT-6.1-sol/high.
Same-family review; semantic acceptance is provisional and relative to the
explicit imports below. The served backend model is not independently attested.

**PASS: complete P6 is proved relative to the explicit accepted imports.**
All nine complete layers and the root-preserving range reduction are accepted.
There are zero remaining predecessor conditions or hole levels.

## Exact quantified obligation

For every matching M in the short-edge graph Q6, every u outside V(M), and
every v of opposite Hamming parity, a Hamilton u-v path containing M exists.
There is no condition that v be free. The intermediate use of arbitrary
complete-graph matching edges in local imported proofs does not enlarge the
original matching domain or permit long physical edges in the final path.
If M is perfect there is no eligible u, so that case is vacuous. Empty and
all smaller matchings are within the reduction's quantifier scope.

## Independent semantic check of the final implication

Fix an eligible triple (M,u,v). Every edge of M lies in Q6-u. Add cube edges
whose endpoints are both free until an inclusion-maximal matching L in Q6-u
is reached. Termination follows from strict increase of its cardinality in
a finite graph. Every intermediate matching contains M and leaves u free.
The construction makes no restriction on v; in particular it can cover v.

There are two exhaustive cases. If every neighbor of u is covered by L,
no edge can be added in full Q6: edges away from u are excluded by deleted-
root maximality, and edges at u are excluded by the covered other endpoint.
Thus the explicit full-cube maximal-matching theorem gives |L|>=24.
Otherwise select a free cube neighbor a of u. The matching L+ua is maximal
in full Q6. An edge with both endpoints still free could touch neither u
nor a and would contradict maximality of L in Q6-u. Hence |L|+1>=24 and
|L|>=23. The temporary ua is discarded; it is never an added requirement
on the Hamilton path. The upper bound |L|<=31 follows from the free root.

Therefore L has exactly one of 2,4,6,8,10,12,14,16,18 holes. Apply the
corresponding complete endpoint theorem with this same u and v. The layer
has the correct exact cardinality, its required edges are cube edges, its
root is free, and its target is of opposite parity. Its covered-target
scope is essential when augmentation has covered v. The resulting path
contains L and therefore M. Its endpoints remain the prescribed u,v.
This implication contains no induction assumption or hidden uniform choice
of an auxiliary witness. The chosen L and subsequent local witnesses can
depend on M,u,v.

## Scoped import and condition ledger

| Holes | Matching size | Complete gate and scope |
|---:|---:|---|
|2|31|GENERAL_NEAR_PERFECT_REVIEW, N10; short near-perfect M has one free vertex of each parity, so N10 target parity equals opposite-to-u|
|4|30|FOUR_HOLE_SOL_HIGH_REVIEW, Z18; every short M and every eligible root/target|
|6|29|SIX_HOLE_CLOSURE_CONSEQUENCES_REVIEW; free and covered branches exhaust targets, with canonical A4 premise supplied|
|8|28|EIGHT_HOLE_FULL_REVIEW; complete free branch plus exact covered census, marked cores and EP0 consequence|
|10|27|TEN_HOLE_FULL_REVIEW; complete free branch plus exact covered union, including safe forced T17 hypothesis discharge|
|12|26|TWELVE_HOLE_FULL_REVIEW; complete free branch plus exact covered chain and complete finite maximal-A domain|
|14|25|FOURTEEN_HOLE_FULL_REVIEW; complete12 predecessor discharged, both endpoint branches complete|
|16|24|SIXTEEN_EIGHTEEN_FULL_REVIEW; complete14=>complete16=>complete18 predecessors discharged|
|18|23|SIXTEEN_EIGHTEEN_FULL_REVIEW; complete14=>complete16=>complete18 predecessors discharged|

These gates are imported at their precise theorem scopes. This review does
not rerun all historical finite connectivity matrices, censuses or local
certificates, and does not infer their universal conclusions from samples.
The imported review scopes explicitly include every realizing original
short matching, with arbitrary compressed local matchings where required.
The final assembly's semantic argument above was checked independently.

The higher source gates prove conditional implications, not unconditional
layers. Complete12 discharges the predecessor in the full14 assembly;
complete14 must then discharge the full16 reductions; complete16 discharges
the independently proved implication complete16=>complete18. An earlier
immutable report's contemporaneous 'not established' or 'full P6 open'
statement is not a new hypothesis once the precise antecedent is supplied.
Historical auxiliary proof status statements are never used as conclusions.

The restricted R4_DOUBLE_BRIDGE_REVIEW import allows only its checked bridge
labels. Its actual uses are confined to core4/core24 and their eight-hole
assembly; the complete core audits explicitly discharge the exclusions.
No unrestricted opening/rank claim is inferred from a deficient matrix.

## Explicit external mathematical inputs

Havel and Krivanek (1982), 'On maximal matchings in Q6 and a conjecture of
R. Forcade', Theorem2, printed page125: every inclusion-maximal matching
in full Q6 has at least24 edges. This is an explicit literature import,
bound via ROOTED_RANGE_REVIEW and its proof; its original classification
proof is not re-proved here. A maximum-cardinality statement would not
suffice. Source: https://dml.cz/bitstream/handle/10338.dmlcz/106137/CommentatMathUnivCarol_023-1982-1_10.pdf

The lower proof packages explicitly import Fink's perfect-matching
extension result, the Fink-Muetze extension/avoidance/endpoint theorems
(including Theorems2,8,9,12 where used), their short-added-edge convention,
the established five-direction endpoint theorem, and the individually
audited Q4/Q5 classifications and finite witnesses. Source statements and
their precise hypotheses remain those bound by the respective lower
reviews, not an unconditional full T15/T17 theorem or an arbitrary
complete-graph version of P6. Fink-Muetze author source:
https://tmuetze.de/papers/match.pdf

Cygan, Kratsch and Nederlof, *Fast Hamiltonicity checking via bases of
perfect matchings*, JACM65(3), Article12 (2018), Theorem3.4 and Corollary3.5:
the complete matching-connectivity matrix on even t labelled vertices has
GF(2) rank 2^(t/2-1). Its rows/columns range over all complete-graph perfect
matchings, not just bipartite matchings; the two-terminal double-labelled
edge has the stated two-edge-cycle convention. The rank upper bound is
essential to the imported universal row-space arguments. It is an explicit
literature premise, not inferred by the finite computations. Its source and
conventions are bound in A10_ORBIT3_UNIVERSAL_PRIMARY_SOURCE.md and the
dependent accepted rank reviews. DOI: https://doi.org/10.1145/3148227

## Counterexample and reproducibility checks

The adversarial pass targeted: perfect M with no free root; empty M;
augmentation covering the target; an uncovered neighbor of u; confusion
between maximal and maximum matching; accidentally retaining ua; skipping
hole levels23 through31 edges; reversing the direction of full16=>full18;
substituting free-target results for covered-target predecessors; and
circular import of full P6. The proof handles each boundary explicitly.
No counterexample to a used final implication was found.

The independent checker reconstructs all2,048 ordered opposite-parity
endpoint normalizations and their cube adjacency preservation. It checks
the rooted23-edge extremal witness directly, including all addable edges
and all six maximal full-cube completions. The witness confirms consistency
of the endpoint of the range; it is not used to prove the universal bound.

The recursive checker rehashes declared source/evidence bindings, handles
nested legacy maps as maps rather than filenames, resolves digest aliases,
and checks report dependency acyclicity. Auxiliary comparison evidence is
not promoted to a theorem premise. No live RUN_STATE/PROOF_CHECK_STATE or
A6_CONSEQUENCES_STATE_REVIEW is used. The publisher's future mutation of
research ledgers therefore cannot stale a theorem premise in this audit.
Frozen proofs, existing certificates and research ledgers are unchanged.

This audit is same-family/provisional, not cross-family semantic acceptance,
Lean verification, peer review, a novelty claim, or a theorem about all
complete-graph matchings on64 vertices.

## Final checked result

The final independent run rehashed 5155 distinct bound files,
traversed 96 accepted review nodes and 386
bound report edges, and checked 2274 auxiliary evidence bindings.
There are no missing/stale bindings, dependency cycles or unresolved imported
conditions in the supported declared schemas. Directly bound manifest input/output
files are checked; arbitrary undocumented metadata is not recursively interpreted.
The final14 source is exactly the independently reconstructed disjoint20/5 orbit
union. On each target, the final16 star and small-cut retained sets partition
the same source exactly and have empty intersection; their positive union
therefore leaves no record. The complete16 antecedent discharges the precise
complete16=>complete18 implication. Final14, final16 and final18 each have
zero free and covered residuals.

This closes the original arbitrary short-matching theorem with every free
root and every opposite-parity target, including targets covered before or
during augmentation. All substantive imported premises remain explicit; no
full original literature proof or large historical finite computation was
repeated here. No fatal, critical, major or minor open issue remains in
this final assembly at the stated import and assurance boundary.

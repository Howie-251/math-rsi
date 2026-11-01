# Avoided-lock quotas, five-lock coverage, and one actual 24-point caller

2026-10-13. This round closes the general actual-input connection described in
`round01/large-math/REFINED_DELETION_CERTIFICATES.md` and exercises it in a
nontrivial five-lock branch. It also proves the complete 32-case labelled
large-trace classification for any five pairwise unit-codegree locks. It does
not yet prove the full 23- or 24-point case.

## Checked mathematical connection

`formal/Aris4Math/ThirtyThree/AvoidedLink.lean` defines `avoidedEdges H x R`
as the actual incident edges of `H` disjoint from `R`, and `avoidedBadPairs` as
a literal filter of the existing `H.badLinkPairs x`.

For `x ∉ R`, `avoided_bad_pair_budget` proves

\[
4|F_R|\le 3|B_R|+(|V|-1-|R|).
\]

The proof double-counts incidences outside `R ∪ {x}`. Two distinct five-element
edges through `x` share at most three noncenter vertices. No pair-covering,
degree, or edge-count hypothesis is used. Natural-number arithmetic then gives
the nonnegative rounded quota `(4 * |F_R| + 2 - (|V| - 1 - |R|)) / 3`.

`formal/Aris4Math/ThirtyThree/RefinedDeletion.lean` proves a finite dual
inequality for arbitrarily many overlapping edge-subfamily quotas. Each
unordered pair receives the sum of all applicable nonnegative multipliers.
Any deficiency of its actual two-direction weight is paid by one half in
each direction. The nonnegative penalty is bounded using **all actual distinct
incident pairs**, so overlapping quotas are not independently subtracted.

The actual-to-numeric connections are:

1. `realized_avoided_count`: from `RealizesProfile`, the actual cardinality of
   `F_R` equals `avoidedCount` of precisely those types containing the center
   and avoiding the positional image of `R`.
2. `realized_penalty_sum`: aggregates the full actual penalty using
   `pair_sum_by_table`. Ordered type capacities are exactly
   `n_t * (n_u - if t = u then 1 else 0)`. Its half-penalties therefore match
   `choose(n_t,2)` and `n_t*n_u` unordered capacities.
3. `realized_refined_deduction`: derives every actual quota from the first
   module, then proves a lower bound on the existing `directedBadPairs` sum.
   The caller supplies only finite nonnegative coefficients, integer quota
   comparisons and a finite rational inequality; actual quotas are not assumed.
4. `propertyB_of_refined_deletion`: applies that result at actual correction
   centers and calls `CustomDeletion.propertyB_of_custom_deletion`, returning
   `PropertyB H` for the same original hypergraph.

R is supplied as a finite set of lock indices. Its images in actual vertices
and one-based positions are proved equivalent using the two embeddings. The
embedding also proves that cardinality is preserved. Sets may overlap; an
empty set of avoided locks includes the ordinary total-link quota.

## Concrete branch connected through all interfaces

`formal/Aris4Math/ThirtyThree/TwentyFourRefinedExample.lean` uses the existing
`AVOIDED_LOCK_QUOTAS.json` group 13. The final theorem is
`TwentyFourRefinedExample.propertyB_of_mixed_quad_trace`.

Its premises are an actual simple five-uniform hypergraph on `Fin 24`, exactly
33 edges, an embedding of five locks, their degrees `(6,6,7,7,7)`, unit codegree
for every two distinct locks, and the exact large-trace condition: the only
trace of size at least three is `{0,2,3,4}`, with multiplicity one.
Its conclusion is `PropertyB H`. There is **no** realizer, quota, numeric bound,
or certificate premise at this branch theorem.

`MultiLockRecovery.realizes_recovered` constructs the true profile from those
structural premises. The chosen one-based positions are `(12,13,14,15,16)`.
At each high-degree center there are two overlapping subquotas:

- avoid three specified other locks: 6 actual edges, quota 2, multiplier
  `55/8398`;
- avoid all four other locks: 5 actual edges, quota 1, multiplier `55/25194`.

The resulting loss per high center is `385/25194`. Kernel reduction checks
all finite quota and dual conditions, profile validity, and the exact full
position-bound sum

\[
\sum_{k=1}^{24}\min\{A_k,B_k,C_k-L_k\}=75163/75582<1.
\]

The full 24-point argument still has to supply a proved strict bound in every
remaining branch. This result validates a concrete finite caller and the
complete actual-input path. The concrete large-trace function is proved equal
to case 14 of the complete labelled classification below.

## All 32 labelled five-lock unit-codegree trace families

`formal/Aris4Math/ThirtyThree/FiveLockClassification.lean` proves the complete
large-trace domain for arbitrary `H : Simple5Hypergraph (Fin v)` and a five-lock
embedding with unit codegrees. It uses this mathematical argument:

1. Any actual trace of size at least three has multiplicity at most one,
   because two locks in it already have total codegree one.
2. Distinct actual large traces intersect in at most one lock: two shared
   locks would force their underlying edges to be equal.
3. Two such large traces already cover all five locks. Any third large trace
   meeting each in at most one lock would have size at most two. Thus the
   actual large-trace family has cardinality at most two.
4. The explicit table contains the empty family, the 16 single large traces,
   and the 15 compatible pairs of triples. Small finite single/pair checks
   verify this table, after the analytical cardinality argument. There is no
   scan of all `2^32` possible set families and no scan of hypergraphs.

`actual_high_in_table` produces an index `i : Fin 32` and the true multiplicity
of **every** large trace. `actual_recovered_in_table` calls the shared recovery
theorem to recover every pair, singleton and empty multiplicity from that index
and actual low-order data. `families_admissible` and `families_injective` also
verify that the 32 entries are legal and distinct. These indices are labelled
cases; no isomorphism or colored-orbit assumption is used.

## Verification and interface for assembly

Use the pinned project environment:

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd /Users/rfy_naiveai/Desktop/aris4math/formal
lake build Aris4Math.ThirtyThree.RefinedDeletion
lake build Aris4Math.ThirtyThree.TwentyFourRefinedExample
lake env lean ../context/propertyb33/round02/avoided-link/ImportAudit.lean
```

`build.log` records the successful 991-job shared-interface build (exit 0).
`example-build.log` records the first concrete caller build. `final-build.log`
records the complete 1004-job build after integrating the 32-case classifier
(exit 0; new classifier 4.2 seconds, concrete caller 5.0 seconds).
`import-audit.log`
prints the actual exported types and transitive axiom dependencies. All audited
results use only `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx`,
new axiom or `native_decide` is introduced.

This is implementation and kernel evidence by a Codex subagent. It is not a
cross-family review; Grok/Gemini review remains the parent run's responsibility.
The parent owns `MultiLockRecovery.lean`; this task changed only its four new
modules plus this evidence directory.

Next assembly action: reuse `realized_refined_deduction` for the remaining
23-point exact dual certificates, and `propertyB_of_refined_deletion` when all
corrected centers are treated by avoided-lock quotas. Mixed actual selected-pair
and dual corrections can continue to use `CustomDeletion` with one proved
`center_lower` case for each mechanism.

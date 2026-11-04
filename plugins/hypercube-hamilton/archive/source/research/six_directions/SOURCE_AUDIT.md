# Upstream source audit: scope of zero-omitting path verification

Date: 2026-10-31. Scope: source inspection and small independently enumerated coverage examples. This is not a disproof of Conjecture 2, Theorem 4, or the paper's complete proof chain.

Repository: https://gitlab.com/jirka.fink/matching_of_five_directions
GitLab project ID: 66089704. Observed main commit: 068b760f636432fded776b8e08457372f7df13ce.
Local inspected artifacts: upstream/bin.rs, upstream/lib.rs, upstream/sat.zig, upstream/README.md; paper.txt Appendix B.

## 1. Entry-point tracing

README batch command:

    test-all-matchings-for-simple-hamilton-path -d <dim> -o

bin.rs lines184–232 selects only zero-to-odd terminal pairs, then calls generate_maximal_matchings_up_to_isomorphism(dimension, omit_zero). Lines20–23 choose GenerateMaximalMatchings::new_omitting_zero directly. There is no intermediate step enumerating full maximal matchings and removing the edge incident to zero.

The stdin branch consumes exactly the supplied edges and tests them. It does not remove a zero edge either. The separate TestMatchingsForFirstSubsetAllowingAll command recursively removes edges, but is not invoked by this zero-omitting batch route. README places that command in a separate General Path Conjecture workflow.

The inspected GitLab recursive tree contained no additional shell wrapper doing a deletion transformation. The README links thesis.pdf, but that file was not present in the observed tree. This does not rule out unpublished scripts or other historical revisions.

## 2. Exact generator scope

lib.rs lines1634–1644 marks zero Forbidden and every neighbor ToMatch. The iterator preserves that coverage requirement. Thus it enumerates matchings maximal in the full cube Q_d, subject to leaving zero uncovered.

sat.zig lines376–403 imposes coverage(a) OR coverage(b) on EVERY cube edge, including edges incident to zero. Setting coverage(0)=false consequently forces all its neighbors covered. The explicit neighbor clauses repeat the same condition.

These are not all matchings maximal in Q_d−{0}. The latter is the maximality notion that directly supports monotone extension for the unrestricted zero-avoiding matching claim.

## 3. Concrete coverage counterexamples, not theorem counterexamples

In Q2, M={(2,3)} is maximal in Q2−{0}; vertices0 and1 are uncovered. It cannot be extended further without covering zero. Yet it is not maximal in Q2 because edge(0,1) can be added. It is omitted by both generator rules above.

This is not a Hamilton-path obstruction: 0–1–3–2 contains M, and 0–2–3–1 contains M, covering both possible odd endpoints.

An independent exhaustive Python enumeration of ALL subsets of the edge set avoiding0, filtered by matching and maximality, gave:

| dimension | maximal in Q_d−0 | full-Q_d maximal avoiding0 |
|---|---:|---:|
|2|2|0|
|3|11|2|

Thus the dedicated -o generator has no output at d=2, even though nonempty instances of Conjecture2 exist. This is a demonstrable coverage limitation of this route, not a failing conjecture instance.

The same basic omitted family exists in every dimension: take a single-direction perfect matching and delete its zero-incident edge. This gives a matching maximal in Q_d−0, with only zero and its neighbor uncovered. Such instances are mathematically covered by the perfect-matching extension theorem, but that separate justification must be stated if used to repair coverage.

## 4. Symmetry audit

bin.rs uses AutomorphismFilter::new_for_dimension. lib.rs lines1475–1493 uses ALL cube automorphisms, including translations, and returns the lexicographically minimal transformed matching.

Because MatchingVertexReference::Uncovered precedes Vertex in the derived ordering (lines376–385), a non-perfect matching's globally minimal representative has zero uncovered. Therefore it would be incorrect to claim this canonicalization necessarily makes zero covered.

However, the actual problem is pointed: (M,u) with u uncovered. Different uncovered vertices need not be equivalent under the stabilizer of M. Testing all zero-to-odd paths for one unpointed matching representative does not by itself establish the property for every uncovered start vertex in that matching. A proof that all relevant pointed orbits are represented, or a separate test of all uncovered start vertices, is needed. No such argument was found in this code path. This is an unfulfilled coverage obligation, not a demonstrated Hamilton failure.

The SAT generator similarly blocks all automorphisms while the -o verifier fixes the distinguished vertex. The same pointed-orbit issue must be addressed if those tools are combined that way.

## 5. Correct coverage routes for our P6 work

Route A: enumerate maximal matchings of Q6−{0}. In SAT, omit maximality clauses for edges incident to0. For an explicit generator, zero is excluded from legal additions and does not force neighbor coverage. Quotient only by coordinate permutations fixing0, or prove an equivalent pointed canonicalization. Test all32 odd endpoints.

Route B: enumerate full-Q6 maximal matchings N. If zero is uncovered, test N; otherwise test N minus its unique zero-incident edge. Why this suffices: every zero-avoiding M extends to some full-maximal N; deleting the zero edge never removes an edge of M. Any Hamilton path containing the reduced N therefore contains M. With unpointed matching representatives, perform this construction for every vertex u, then test all opposite-parity endpoints, or quotient pointed pairs correctly.

Route B may admit more redundancy; it is a correctness-preserving reduction, not an efficiency promise.

## 6. Limit of the finding

Appendix B also describes an independent broader Conjecture5 verification with exceptional subsets. Since a genuinely uncovered endpoint rules out the stated covered-endpoint obstructions, a sound complete verification of that stronger statement could separately establish P5. We have not audited that entire workflow, the path-search engine, or historical run artifacts. Therefore the defensible conclusion is: the dedicated zero-omitting maximal-generation route alone does not demonstrate the claimed unrestricted coverage; our P6 implementation should avoid inheriting this reduction without repair.


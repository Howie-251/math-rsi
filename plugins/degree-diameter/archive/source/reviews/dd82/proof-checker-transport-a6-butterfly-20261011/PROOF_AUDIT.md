# Transport, butterfly, and Brown a6 proof audit

**Verdict: PASS for the four submitted claims, same-family / provisional.** No fatal, critical, major, or minor mathematical issue remains. This is a paper-proof review with an independently reproduced finite Brown check; it is not Lean verification or cross-family acceptance.

The fresh reviewer is `/root/proof_review_transport_a6_butterfly`, created with `fork_turns: none`. The parent reports an explicit request for `gpt-6-astra`, reasoning effort `ultra`. The agent interface returned the canonical task name only; no opaque agent identifier or backend model attestation was supplied. This report records the requested route and does not invent actual backend metadata. Task framing supplied by the parent contained a brief description of the new local argument; conclusions here were obtained by reading the full artifacts directly, rather than treating that description as evidence.

## Exact accepted paper scope

1. `nonzero_support_transport_20261011.md`: in a simple legal59-vertex graph with the actual N15 matching row at **every zero-triangle vertex**, the three support/weight statements and exact formula `e_r=5+Q_N(r)−s_N(r)−K_r` hold for every root. The fifth-trace substitution and coupling sum are correct. N15 at a nonzero root is not used.
2. `two_triangles_shared_vertex_reduction_20261011.md`: assuming that the graph's only triangles share precisely one vertex, the stated actual row parameters necessarily belong to the three displayed templates, up to butterfly relabeling. The private-neighborhood interpretation is correct. This remains a necessary reduction, with no realizability claim, and is superseded as an exclusion route by the next paper.
3. `two_triangles_shared_vertex_exclusion_20261011.md`: under explicit global zero-row N15, exactly two triangles sharing precisely one vertex are impossible. Its reusable local obstruction is valid under its stated assumptions: one triangle at the root, six private zero neighbors, and exactly two weight-two zero nonedge repeats. The decisive final count is `s=570`, giving `8C₄=900`.
4. `BROWN_R9_SIX_III_OBSTRUCTION.md`: a legal order58 graph on the fixed57 labeled Brown vertices and one new vertex cannot have exactly nine old deletions that destroy exactly six distinct III triangles. Arbitrary added old edges are included in the reduction. The proof rests on the independently verified finite fact that none of the14 prescribed41-point candidate systems has a constrained dominating eight-set.

The n59 premises are not asserted for arbitrary graphs. This audit does not close the disjoint-two-triangle case, higher triangle counts, general H5, arbitrary order59 or order58 nonexistence, or `exactN(8,2)`. The Brown result does not establish that ten deletions are necessary and does not close the other r9 branches.

## Main checks

The full hypothesis and dependency ledger is `PROOF_SKELETON.md`. The actual endpoint lemma and original four/five-trace derivations were read and re-derived only to the extent needed by these papers. The shared-edge paper was read to check the final conditional corollary of the new exclusion. No prior audit verdict was used as mathematical evidence.

Transport relies on the induced matching condition, including the absence of edges between the unequal-weight endpoints. From N15 at the zero endpoint and `AB=BA`, the support-sum equality follows at an arbitrary root. The matching and independent-set conclusions then use only nonnegativity and the definition of a zero vertex. The square/edge-sum cancellation counts unordered support edges correctly.

The butterfly reduction's congruence and all integer branches were checked. `s=570+4k` forces `k∈{1,3}`; the fifth trace and commutation exclude `k=3`. The remaining relabelings preserve the actual two-triangle graph, and the stated three rows exhaust the parameter solutions. The statement about nonempty private-neighborhood blocks being matchings is valid because their relevant roots are1111 rows; the unique22 row has empty specified blocks.

The new local22 contradiction does not assume there are no other triangles globally. Once transport forces the two heavy repeats adjacent, their zero status forces disjoint three-parent sets, and the complete root defect support makes every other outside vertex single-parent. Two light endpoints at a private zero point are then forced inside an independent original neighborhood, contradicting N15. In the butterfly application every private neighbor is zero, so every hypothesis is discharged. The final four-cycle integrality step uses a standard closed-walk identity explicitly re-derived in the ledger.

In the Brown branch, exact internal coverage forces disjoint triangle blocks; the finite claim that the omitted internal points form an III triangle is checked directly, not inferred from the family count. The deletion matching implies all available degree deficits are one, which is precisely why no new old edge can touch the new vertex's neighbor set. Testing domination in the original graph is a valid relaxation of domination after deletion.

The C++ recursion was inspected: removal of prior dominator choices partitions completions without excluding a feasible set; block updates enforce exactly the necessary restrictions; both availability and optimistic-coverage prunes have the correct direction; and already dominated states continue to size eight. The later deletion-partner filter is not load-bearing because the earlier domination count is zero. The fixed input has14 correctly enumerated III triangles, so the code's hard-coded loop limit is valid for this declared input.

## Finite execution evidence

The independent Python source is preserved as executable text in `INDEPENDENT_CHECK.md`, and its full result is `INDEPENDENT_CHECK.json`. It uses a different decomposition from the submitted C++: enumerate possible external selected subsets in each of the three five-point blocks; force every absolute point not dominated by those external vertices; then search remaining absolute/internal selections with Python sets. These forced absolute choices are sound because no absolute vertex has an absolute or internal neighbor. All external subsets have sizes at most two and satisfy the same adjacency restriction, so the decomposition is exhaustive.

The independent run reconstructed the degree classes, all56 triangles,14 III triangles,42 IEE triangles, every internal triangle incidence, the old-edge triangle bound, the14 six-III families, the omitted III triangles, nine disjoint blocks per family, and candidate size41. It returned zero solutions for all14 families and all `14·343=4802` external cases. It used0.126039 CPU seconds,0.126054 reported wall seconds, and12460 KiB peak RSS, one process and no SAT solver. Every external case was rejected at the initial completion state by the exact tests in the preserved source.

The submitted C++ was compiled and run once against the same edge list. It exited zero and reproduced:

```text
nodes_by_family = [83,85,83,84,93,83,81,87,91,83,84,83,84,85]
TOTAL families=14 nodes=1189 dominating=0 feasible=0
```

Both executions were bounded by `timeout 30s`; the compiler plus submitted-program command took1.259 seconds according to the execution tool. No GPU, SAT queue, network service, or added-edge completion search was used.

## Counterexample attempts and closure

- Unequal adjacent zero support weights would force both opposite inequalities; equality eliminates all additional support neighbors. Isolated weight-two zeros facing a unit-weight clique are impossible by the exact sum and independence conditions.
- The possibility of an additional cross-triangle common neighbor was preserved and then ruled out by a forbidden heavy center endpoint; no missing cross-pair case was assumed away.
- A local22 row with further global triangles was considered explicitly: the proof needs only its stated zero vertices and the complete root row, so unrelated triangles do not invalidate it.
- All outer row partitions of four into allowed weights were retained (`22`, `211`, `1111`); all center pair/no-pair cases and both odd values of `k` were checked. The new exclusion eliminates all outer22 cases without relying on template realizability.
- Brown overlap, extra old additions, and smaller dominating subsets were checked against the actual hypotheses. Coverage equality excludes overlap in this branch, the unit-deficit argument excludes added incidences at `S`, and the submitted search preserves extensions of smaller dominating sets to exactly eight.

No algebraically verified counterexample or unresolved candidate was found. The obligations in the ledger are discharged; statement/conclusion matching and the dependency DAG show no cycle or silent strengthening. No author paper or formal file was edited. Historical wording describing the earlier partial butterfly reduction should be read in its document's local scope; it does not weaken the new exclusion.

## Workflow and artifacts

The project-local `.agents/skills/proof-checker/SKILL.md` and its reviewer-routing, reviewer-independence, assurance-contract, and fan-out references were read. The user's explicit instructions override their default hash and TeX/PDF/HTML packaging steps: this audit contains only Markdown and JSON, with no checksums or artifact manifests. The requested route remains same-family/provisional even though the finite computations are deterministic.

The review invocation itself is the parent's fresh Codex reviewer call. No further verdict-bearing reviewer was spawned; all four available team slots were occupied. The machine-readable audit records exact inputs, commands, resource evidence, route metadata, and claim scopes. Wiki claim-node integration is delegated to the parent to avoid concurrent writes to the shared wiki; that does not alter this audit's verdict.

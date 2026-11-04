# Bounded same-family review

Date: 2026-10-31
Reviewer: delegated Codex agent /root/open_problems
review_independence: same-family
acceptance_status: provisional
Scope: PROOF_PACKAGE.md; lift_templates.py; export_obligations.py; supporting JSON/CNF artifacts. This review is not a proof of full P6 or T6 and is not cross-model mathematical acceptance.

## Findings

No actionable mathematical or implementation errors found within the requested bounded scope.

1. Conditional T6: Lemmas1–3 correctly reduce to rooted relative-maximal matchings and establish a local cycle from P6. Lemma4 maintains the local endpoint parity through an even number of fibres. For the Q1 exterior case, the two connectors have different local parity and hence distinct endpoints, so no simple edge is reused. The n<6 known-result boundary is explicitly stated.
2. Certified restricted theorem: the class C retains its distinguished root. Translations and coordinate permutations transport all32 required root-to-opposite-parity witnesses; taking submatchings preserves them. Every noninitial fibre only requires an extension cycle, whereas the initial fibre requires the rooted path property. The proof uses exactly these capabilities. Perfect fibres are handled through the stated external perfect-matching theorem.
3. Relative-maximal CNF: its186 variables are exactly the cube edges avoiding0. Pairwise incident-edge exclusions encode a matching. The union-of-incidence positive clause for each allowed edge encodes maximality in Q6−0. Clauses exclude only submatchings of an actual certified terminal path. The endpoint branches1,7,31 cover the three odd-weight classes when each branch checks all matchings. The document correctly says SAT is an uncovered candidate and only certified UNSAT could close a branch.
4. The scope statements correctly distinguish finite templates from universal P6 and give no unsupported claim of complete six-direction proof or novelty.

## Independent artifact checks performed in this review

A separate short Python checker, without importing either generation script, checked vertex permutations, adjacency, endpoint0, requested terminal, and matching inclusion for all1326 stored paths. It grouped exactly36 distinct six-dimensional matching templates, each with32 odd terminal witnesses;20 templates use all six directions.

It independently checked the emitted Q7/Q8 cyclic vertex sequences, closure, distinctness, adjacency and matching inclusion: respectively57 and117 matching edges, both using six directions.

It checked the CNF variable edge universe, emitted clause counts, terminal identity, and all path-exclusion clauses against their stored witnesses: each branch contains1137 clauses and36 path clauses. This was artifact validation, not SAT solving. The base formula's equivalence was checked by reading its construction and the mathematical argument, not by an exhaustive Q6 assignment run.

The initial search artifact independently reports960 six-dimensional FOUND cases and192 UNKNOWN cases, consistent with the proof package. The later artifact has1152 six-dimensional FOUND cases plus174 low-dimensional cases. The reported432-case exhaustive search regression is outside this review's fresh execution scope; its test was not rerun here.

## Remaining boundary

Full P6 remains unproved. The current finite witness family and emitted CNFs do not establish complete matching-space coverage. This review found the conditional reduction and restricted certificate claim internally consistent, assuming the cited external perfect-matching theorem and existing five-direction theorem.

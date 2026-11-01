# T34: orbit compression and the strong-codegree entry

2026-10-13. The underlying hypergraph is held fixed throughout relabeling.
`ThirtyFour.LockRelabel.count_comp_perm` proves

    count H (σ.toEmbedding.trans f) T = count H f (T.map σ.toEmbedding).

It compiled on its first build in 1.2 seconds; the log is
`../twentyone-lean/build-queue-LockRelabel-r8.log`. For any finite number of
selected locks, a representative certificate therefore applies after the
same proved label transport. This does not identify distinct hypergraphs.

The 21-point minimum-degree-eight work already uses this interface. Its
pure four-lock profiles reduce from 356 to 31 representatives, and its
joint four-lock profiles from 24 to one. Numeric representatives and the
full four-lock coverage theorem have compiled; the complete actual-H minimum-eight branch has now compiled and entered
Assembly. The updated Assembly has 1183 jobs and the independent EightAudit
passes with four standard-three-axiom queries. The coverage theorem quantifies
over the full 15,552 parameter domain, with an explicit representative and
permutation lookup. The lookup is only a proposed witness until Lean checks
the equality for every legal input.

For the new 22/23-point high-codegree entry, the original first-hour exact
witnesses remain the data source:
`context/propertyb34-hour1-20261013/MIDDLE_THRESHOLDS_VERIFIED.json`.
`generate_strong_triples.py` reuses the existing single-layout exporter,
recomputes the exact quota deductions, and writes only relabeling
representatives. The target modules are `TwentyTwoStrongCodegree` and
`TwentyThreeStrongCodegree`.

| Vertices | Full labelled triple profiles | Probability representatives | Maximum bound |
|---|---:|---:|---:|
| 22 | 46 | 16 | 230247/230945 |
| 23 | 91 | 26 | 82689/83980 |

Both `StrongTriple777` modules, including the actual multiplicity-to-coloring
callers, have compiled. `generate_strong_coverage.py` additionally emits the
full labelled coverage theorem and the actual pair/triple selection bridge.
Both final targets compiled successfully (1023 jobs each), with only
propext, Classical.choice and Quot.sound. Logs are
`../twentyone-lean/build-queue-TwentyTwoStrongCodegree-r16.log` and
`build-queue-TwentyThreeStrongCodegree-r16.log` in the same directory.
The numerical modules were unchanged during the small elaboration fixes.

The compiled exported `codegree_le` starts from actual H, pair coverage,
34 edges, at least three degree-seven vertices and an assumed absence of
Property B. It proves that each pair of distinct degree-seven vertices has
codegree at most two (22 vertices) or three (23 vertices). This is an
internal structural reduction, not a full coloring proof at either size.

The full T34 theorem, final type/axiom audit and final cross-family C review
remain unfinished. No full-hypergraph enumeration is used here.

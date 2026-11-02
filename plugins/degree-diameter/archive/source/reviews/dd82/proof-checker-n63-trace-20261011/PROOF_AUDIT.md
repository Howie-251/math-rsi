# Fresh adversarial audit: N63, n59 trace, and C5/C7/C8/C9

**Verdict: PASS, same-family provisional.** No mathematical counterexample or substantive proof gap was found in the stated original-graph results. One cosmetic notation collision was found and corrected by the author during the audit; the reviewer reread the corrected trace proof in full. This changed no hypotheses or mathematics.

Requested reviewer: `gpt-6-astra`, reasoning `ultra`; actual backend model and effort are not independently attested. Reviewer task: `/root/proof_review_n63_trace`. The project-local proof-checker skill and reviewer-routing/independence/assurance references were read. User overrides suppress hashes, manifests, TeX/PDF/HTML generation, approval rituals, and source/formal edits by this reviewer. Existing reviews and `N63_SPECTRAL_ROUTE_REVIEW` were not read. Research-wiki recording is left to the parent.

## Scoped verdicts

| Primary source | Verdict | Established scope |
|---|---|---|
| `proofs/dd82/FOUNDATIONS.md` | PASS | Original root bound, regularity for n>57, actual defect identities, and elementary paper exclusions of 64 and 65. Formal-status prose was not independently checked. |
| `proofs/dd82/construction/N63_CYCLOTOMIC_SPECTRAL_OBSTRUCTION.md` | PASS | Paper exclusion of an arbitrary simple undirected 63-vertex graph with maximum degree≤8 and diameter≤2. Finite norm arithmetic and the graph-to-field bridge were both checked. No complete Lean theorem is inferred. |
| `computations/dd82/construction/n63_cyclotomic_norms.py`, `.json`, `.table.md` | PASS | All 63 rows match the required polynomial identities/norms; exactly conductor 3 is the square-norm exception. Source generator was read but neither run nor imported. |
| `proofs/dd82/n59/matching_zero_global_trace_obstruction_20261011.md` | PASS after cosmetic correction | Exact fifth-cycle identity/congruence when matching 2211 rows are assumed only at zero-triangle vertices; impossibility of the all-zero triangle-free subcase. |
| `proofs/dd82/n59/matching_zero_r2_c5_exclusion_20261011.md` | PASS | Only the simple length-5 R2 cycle on matching zero vertices is excluded. |
| `proofs/dd82/n59/matching_zero_r2_c7_exclusion_20261011.md` | PASS | Only the corresponding length-7 cycle is excluded. |
| `proofs/dd82/n59/matching_zero_r2_c8_exclusion_20261011.md` | PASS | Only the corresponding length-8 cycle is excluded. |
| `proofs/dd82/n59/matching_zero_r2_c9_exclusion_20261011.md` | PASS | Only the corresponding length-9 cycle is excluded, with extra internal chords and all external-neighborhood cases handled. |

The cycle vertices are interpreted as pairwise distinct, as required by a simple cycle. H5 and N15 definitions/imports were outside this audit, so the H5+N15 corollaries remain conditional on their stated bridge. No conclusion excludes H5 as a whole, all n59 graphs, mixed-type cycles/paths, or longer all-zero cycles. No exact value of N(8,2), formal upper bound 62, or historical RAW certification is asserted.

## Main mathematical checks

For N63, the degree bound is derived before using `A1=8·1`. Nonnegative integral row sum two with zero diagonal really gives only doubled edges and ordinary cycles; the conductor of every cycle eigenvalue divides its cycle length. Different primitive roots give conjugate μ and the same discriminant norm. The exceptional conductor is exactly 3; the doubled-edge eigenvalues ±2 are included, as is the extra μ=2 space inside the orthogonal complement of constants.

The field argument does not confuse conjugate real roots with equal multiplicities. The space defined by `Bv=μv` and `Σv_i=0` over `K=Q(μ)` extends to the full real eigenspace by rank invariance of a matrix over K. Since A is rational and commutes with B, it acts K-linearly there. Irreducibility of the quadratic gives a genuine quadratic-field vector-space structure, forcing trace `−dim/2`; it is valid with repeated eigenvalues and for the zero space. The constant direction contributes 8 separately. The exceptional 2/−3 multiplicities give `46=5(p−q)`, an actual integer contradiction.

For the trace package, independent expansion gives

`s = tr(A⁴) + 12T − 126n`,

`w = tr(A⁵) + 2tr(A⁴) − 78T − 680n` (n=59),

and hence `tr(A⁵)=428n+w−2s+102T`. A nonsimple five-step closed walk has used-edge support a triangle or that triangle with one doubled incident edge. In a general simple graph its correction is `10 Σ_triangles(deg u+deg v+deg w−3)`; at degree 8 this is `210T`. Chords and an external endpoint adjacent to several triangle vertices do not create duplicate assignment, because the used edges determine the triangle. Consequently the coefficient −108T before division, −54T after division, and the remainder 4 modulo 5 are correct. Matching zero rows contribute `s_v=w_v=10`; no moment value is imposed on nonzero rows.

For C5, the two external common neighbors are forced to be precisely the two light endpoints of another selected zero vertex; their required edge creates a triangle. For C7, internal B entries are completely fixed before external neighborhoods are classified, and the 21 distinct external points charge distinct cross-block B entries against a total budget of 14. For C8, antipodal light endpoints eliminate all initially possible step-three edges; the ensuing parity restriction is only local. The common-neighbor demand is eight and the actual capacity six. For C9, the chord exclusion uses an external common neighbor that must exist even when both possible internal common neighbors occur. The later six-neighbor saturation is exact; the only two-edge subset orbit is `{0,1,4,5}`, and its forced light pair is an actual nonedge. The uncovered pair 0,3 then gives the contradiction.

## Issue and correction

**PC-01 — MINOR / UNCLEAR / COSMETIC / NORMALIZATION_MISMATCH (notation).** The initial trace source used `e_v` for a basis vector in `Be_v` and the scalar correction `Q2(v)−s_v+5` at lines 11 and 33. No false equality or downstream mathematical failure follows once the intended types are distinguished. Minimal fix: label the basis vector `\mathbf e_v` and define it explicitly. The author made that correction; current lines 11, 33, 35, 97, and 99 were checked in a full reread. Status: RESOLVED. No assumption or theorem scope changed. No re-testing was needed for this typographical change.

## Bounded falsification and arithmetic evidence

The executable check is `audit_checks.py`, with a hard 60 CPU-second limit. Its output is `audit_checks.json`; exit code 0, reported CPU time about 0.173 seconds. It does not invoke or import the source generator.

- All 63 lifted polynomials satisfy the independent divisor-product identities `∏[d|ℓ] Φ_d(t)=t^ℓ−1`; degrees match the elementary totient count.
- Each norm was independently computed as the exact Bareiss determinant of multiplication by `29+4μ` in the power basis. All stored norms, square brackets, residue sets, residues, exception flags, and Markdown rows agree.
- All 1,099 labeled simple graphs of orders 1 through 5 satisfy the general degree-dependent fifth-walk formula. This covers triangles, repeated-vertex walks, chords, and multiple triangles; no discrepancy was found.
- An 8-regular circulant on 59 vertices checks the fourth/fifth trace algebra with `T=354`, `s=14278`, `w=86966`, `tr(A⁵)=119770`. It does not satisfy the diameter-two assumptions and is explicitly only an algebra check, not a graph counterexample.
- Internal common-neighbor arrays for C5/C7/C8/C9 were checked exactly. All 512 subsets of the C9 positions were checked for the local 1-regular/step-two-independent conditions; the allowed subset counts are one empty, nine single-edge, and nine two-edge sets, exactly the claimed two-edge orbit.

Counterexample attacks also considered disconnected B, multiple constant-on-component eigenvectors, repeated cyclotomic eigenvalues, the square-discriminant exception, nonzero correction rows, extra C8 edges, multiple C9 chords, and multi-edge external neighborhoods. The proof handles these cases with the stated hypotheses. No algebraically verified counterexample or unresolved candidate remains. These finite checks corroborate the subclaims; the proof arguments, not unsuccessful search, discharge the general obligations.

## Provenance and commands

Working directory: `/inspire/hdd/global_user/mahaitong-240108120090/ar4math`. All ten input files listed in the verdict table were read in full, including every field of the norm JSON (compact serialization of every row). The root `AGENTS.md`, `.agents/skills/proof-checker/SKILL.md`, and `.agents/skills/shared-references/{reviewer-routing,reviewer-independence,assurance-contract}.md` were read. Local subordinate AGENTS locations were checked directly; none existed in the relevant proof directories. An initial broad `rg --files -g AGENTS.md …` search was cancelled without output; it provided no mathematical input.

Commands executed included `cat`/`nl -ba` on the listed proof, generator, table, skill, and reference files; `wc -l` on the ten declared inputs; a standard-library Python JSON read/compact print of all rows; `pwd`; `date -u +%Y-%m-%dT%H:%M:%SZ`; directory creation; and the sole substantive arithmetic command:

```text
timeout 65s python3 reviews/dd82/proof-checker-n63-trace-20261011/audit_checks.py
```

The saved script is the complete executed arithmetic command body. The corrected trace source was reread with `nl -ba`. Audit files alone were created by this reviewer. No heavy SAT, graph enumeration at order 59/63, formal build, network lookup, hashes, checksums, or manifests were used.

The detailed dependency DAG, hypothesis ledger, symbol types, and micro-claim inventory are in `PROOF_SKELETON.md`. All semantic judgments remain same-family provisional; deterministic arithmetic checks do not promote the proof audit to cross-family acceptance.

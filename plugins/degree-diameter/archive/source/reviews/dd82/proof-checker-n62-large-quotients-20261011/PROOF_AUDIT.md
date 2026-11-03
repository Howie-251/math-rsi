# Fresh audit of the five-, seven-, and nine-component quotient search

Date: 2026-10-11. Reviewer: `/root/proof_review_n62_quotient_search`.
Skill: project-local `.agents/skills/proof-checker/SKILL.md`.

**Verdict: PASS for the specified finite integer classification.** No fatal,
critical, major, or minor mathematical defect was found. An independent exact
implementation reproduced every quotient and every row domain in 12.15 seconds
on one CPU. This is external deterministic computation, not a Lean theorem.
The semantic proof review is **same-family / provisional**.

The original search and its three reports were preserved. This audit does not
review the separate new argument excluding realization of the five- and
seven-component quotients.

## Audited statement and inputs

For each `k` in `{5,7,9}`, classify pairs `(n,R)`, up to simultaneous component
relabeling, satisfying:

- `n` is an increasing (not necessarily strictly increasing) tuple of even
  integers at least four, with sum 62;
- `R` is a nonnegative integer `k` by `k` matrix;
- every row of `R` sums to eight;
- `trace(R) = (17-k)/2`;
- `n_i R_ij = n_j R_ji` for every ordered pair;
- `R^2 + R = 10 I + 1 n^T`;
- `R_ii < n_i` for every component.

Inputs inspected directly:

- `computations/dd82/n62/component_quotient_search.py`, especially lines 18–52
  and 60–128;
- `computations/dd82/n62/component_quotients_5.json`;
- `computations/dd82/n62/component_quotients_7.json`;
- `computations/dd82/n62/component_quotients_9.json`;
- Section 3 of `proofs/dd82/n62/GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md` for the
  actual-graph quotient interface.

No previous audit verdict was used as proof evidence. No hashes or checksums
were generated. Reports are Markdown/JSON only, as requested.

## Result and independent evidence

| Components | Size partitions | Empty-domain partitions | Labelled solutions | Canonical quotients | Sizes of the unique quotient |
|---|---:|---:|---:|---:|---|
| 5 | 221 | 218 | 2 | 1 | 4, 8, 10, 20, 20 |
| 7 | 201 | 193 | 6 | 1 | 4, 4, 4, 10, 10, 10, 20 |
| 9 | 94 | 88 | 0 | 0 | none |

Independent implementation:
`computations/dd82/n62/check_large_component_quotients.py`.
Complete machine-readable result:
`computations/dd82/n62/large_component_quotients_check.json`.

The independent checker constructs size tuples by combinations with
replacement, rather than the original recursive partition generator. It
constructs all nonnegative rows of sum eight by stars and bars: respectively
495, 3,003, and 12,870 rows for `k=5,7,9`. Divisibility of `n_i R_ij` by `n_j`
then gives the candidate column. No gcd parametrization from the original
implementation is used in this enumeration.

The second search uses forward filtering of unchosen row domains and bounds
the remaining trace from their smallest/largest diagonal entries. It uses one
ordered off-diagonal equation per pair; balance makes the reverse equation
equivalent. At every accepted leaf it separately checks **all** entries of
the full matrix equation and every other stated hypothesis. Its search-node
counts, 12/53/6, differ from the original 20/218/3,390 because these are
different search algorithms.

Only after all three independent enumerations finish does the checker load
the original module and reference JSON. It then compares all **3,358** row
domains exactly, including their proposed columns and absence of duplicate
rows. All domains agree. It also compares the size partitions, empty-domain
counts, maximum domain sizes (9/92/665), labelled counts, canonical matrices,
and canonical orbit sizes. Every comparison passed.

The checker has one-CPU affinity and a hard 30-second real-time alarm. It
completed in **12.1474 seconds**. Reproduction command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 computations/dd82/n62/check_large_component_quotients.py
```

The original implementation was also rerun with its report writes intercepted
in memory. Every nontiming field matched each stored report, including search
nodes 20/218/3,390. Rerun times were 0.0223/0.1746/0.9287 seconds on one CPU.
A zero-budget run returned `TIME_BUDGET_EXHAUSTED` and zero completed size
partitions. These checks did not rewrite the original reports.

## Proof obligations and their discharge

### Q1. Actual-graph interface and the minimum size

Section 3 starts from a symmetric nonnegative integer repeat matrix `B` with
zero diagonal and row sum three, and an integer graph adjacency matrix `A`
commuting with `B`. The quadratic-form identity for `3I-B` says that the
3-eigenspace consists exactly of functions constant on the positive-support
components. Commutation makes this subspace invariant under `A`, giving the
equitable quotient and its integer neighbor counts.

Restricting the actual matrix identity to this subspace gives the quoted row
sum and quadratic identity. Counting original edges between two components
gives balance. With `D=diag(n)`, the matrix `D^(1/2) R D^(-1/2)` is symmetric.
Also `n^T R=8n^T`, so `n^T x=0` is invariant, and its restriction satisfies
`R^2+R=10I`. The complementary principal vector has eigenvalue eight. Since
`x^2+x-10` is irreducible over the rationals and the characteristic polynomial
of `R` is integral, its two roots have equal multiplicities. This proves the
odd component count and trace formula. There is no missing eigenvalue-eight
subspace: eight is not a root of this quadratic.

The total repeat weight in a component is `3n_i`, twice its integer unordered
edge weight, so `n_i` is even. A two-vertex component would have its only
off-diagonal repeat entry equal to three. Thus **the exclusion of size two
uses the imported actual-graph bound `B<=2`**, derived from triple-repeat
elimination. Evenness alone does not give size at least four. The internal
bound `R_ii<n_i` follows from the absence of graph loops.

This audit verifies the Section 3 deduction from these hypotheses; it does
not independently establish all upstream local graph reductions. None of the
D1 size bounds is required for Q1 or the enumeration.

### Q2. Size-partition coverage

The original `partitions(31,k)` lists every nondecreasing `k`-tuple of integers
at least two summing to 31, once. The first coordinate ranges from its current
lower bound to `floor(total/count)`, which is necessary and sufficient for
some sorted completion; recursion imposes the same condition on the tail.
Doubling is a bijection to the declared size tuples. Sorting loses no
quotient because component indices can be simultaneously permuted. The
independent combinations-with-replacement enumeration gives the same sets.

### Q3. Balanced row-domain coverage and diagonal identity

Fix a row index `i`. For `j!=i`, let `g=gcd(n_i,n_j)`, `a=n_j/g`, and
`b=n_i/g`. Since `a,b` are coprime, the nonnegative integer solutions of
`n_i r=n_j c` are exactly `(r,c)=(at,bt)` for integer `t>=0`. The original
loop bound imposes `r<=8-used` and `c<=8`. Both are necessary: the former
comes from the row being built, the latter from the eventual nonnegative
row containing the transpose entry. No possible completion is removed.

At a leaf, `d=8-used>=0` is the unique diagonal entry compatible with the row
sum. The tests `d<=trace` and `d<n_i` are necessary. The remaining equation
is exactly

`d^2 + d + sum_(j!=i) R_ij R_ji = n_i + 10`.

All summands are nonnegative. Therefore pruning when an accumulated square
sum exceeds `n_i+10` is sound, and `break` is valid because `ab t^2` increases
with `t`. Every admissible row/column pair is generated once. The independent
weak-composition/divisibility construction confirms this for every domain
actually used.

### Q4. Pair checks and complete backtracking

For assigned rows `i,j`, their stored columns are determined by balance with
every component size, including unassigned indices. The two entry-equality
tests match the proposed transpose entries. The next tests are exactly

`row_i dot column_j + R_ij = n_j`,

`row_j dot column_i + R_ji = n_i`.

Thus they check both ordered off-diagonal entries of the target quadratic
identity. The sums require no guesses about future rows: a balanced complete
matrix must have the already determined columns. Testing these equations
early cannot reject a valid completion.

Each size partition has a fixed ordering of all row indices; the backtracking
visits every possible domain selection consistent with the tests. A partial
diagonal sum above the target can never decrease. At a leaf the exact trace
is required. Each diagonal equation came from its row domain, and each
ordered off-diagonal equation was checked when its second row was assigned.
Hence every accepted leaf satisfies all hypotheses, and every matrix
satisfying the hypotheses occurs as a leaf.

### Q5. Deadline status and completion

A size partition is marked complete only after an empty row domain proves
it impossible or its entire search has returned. A caught timeout sets
`TIME_BUDGET_EXHAUSTED`; it never sets the completed-search status. The three
stored reports and fresh reruns complete all their listed partitions. The
completion claim is consequently justified.

Operational observation: the original `--seconds` is a cooperative target,
not a hard runtime cap. Polling occurs between partitions and every 256
search nodes, excluding row generation and canonicalization. A run can finish
after the nominal deadline yet truthfully report completion. This does not
undermine completeness, and the reviewed runs each took under one second.
The independent check supplies its own hard alarm.

### Q6. Relabeling and canonicalization

For fixed sorted `n`, a simultaneous relabeling preserves that ordered size
tuple exactly when `n_(p(i))=n_i` for every index. The original generator
tests every permutation and retains precisely these. Lexicographically
minimizing the simultaneously permuted rows and columns therefore picks one
representative from each allowed orbit. The tuple `(n,flat_R)` prevents
merging different size tuples.

The independent checker generates the same group as the direct product of
permutations within equal-size blocks. It explicitly checks that the orbit
of each canonical quotient equals its enumerated labelled solutions. The
orbit sizes are two and six. Both reference matrices already are the
canonical representatives. There are no nine-component solutions to
canonicalize.

### Q7. D1 annotations and scope

`necessary_D1_pairs` is computed only after a full quotient is accepted. It
does not filter row domains, partitions, or matrices and cannot affect the
classification. It records possible index locations satisfying bounds that
would be necessary for a D1 incidence under the external `H,K>=14` chain;
it does **not** prove that any listed incidence or any graph exists. This
audit neither uses nor certifies that additional chain.

The result classifies the stated integer quotient candidates. In particular,
the nine-component quotient domain is empty. The five- and seven-component
matrices still require a separate graph-realizability argument. Counts outside
`{5,7,9}`, original graph existence/nonexistence as a whole, order 63–65,
and Lean formalization are outside this audit.

## Changes and closure

Added the independent checker, its JSON result, and this fresh audit's
Markdown/JSON reports. No mathematical source fix was required; no original
search output or proof was altered. No new axioms were introduced. All Q1–Q7
obligations are discharged within their explicitly stated imported
hypotheses and finite-computation scope. Cross-family semantic review remains
outside this same-family provisional audit.

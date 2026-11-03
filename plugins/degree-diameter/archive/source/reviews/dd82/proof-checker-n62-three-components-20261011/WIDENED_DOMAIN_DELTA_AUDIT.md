# Widened-domain delta: positive even component sizes

**PASS within this exact-classification scope.** Allowing every positive even component size, including two, still gives **9108 tested matrices, 18 labelled solutions, and exactly three canonical quotients**. There is no size-two survivor. The deterministic exact check is accepted; the audit remains labelled **same-family / provisional**.

## Provenance and changed scope

This is the same reused reviewer agent `/root/proof_review_n62_d1_reduction/sixteen_pure_arithmetic`, following its completed two-target review. It is a delta, not a fresh fork. Root reported an independent widened run; this agent adapted its own earlier row-composition checker without using root code. The saved checker was authored by this reviewer, so this audit does not claim a fresh independent semantic review of that newly saved source.

Requested model/effort: `gpt-6-astra` / `ultra`. Actual runtime model and effort are not independently attested. The previously read project proof-checker skill supplies the obligation format; the explicit request limits output to the two new checker artifacts and these two delta-audit files.

The prior minimum-four discovery script, its JSON, and `PROOF_AUDIT.md/.json` remain unchanged. The widened run is saved separately:

- `computations/dd82/n62/check_three_component_quotients.py`
- `computations/dd82/n62/three_component_quotients_check.json`

This delta concerns exact integer quotient classification only. D1 marks, original-graph exclusion proofs, other component counts and Lean are outside scope.

## Canonical claim

For every nonnegative integer 3-by-3 matrix R with row sums eight and trace seven, require R²+R−10I=1 nᵀ, each n_i a positive even integer, and n_i r_ij=n_j r_ji. Up to simultaneous permutation of component sizes and both R axes, exactly the following three pairs occur:

| Sizes n | Quotient R, by rows | Labelled solutions |
|---|---|---|
| (6,24,32) | (0,8,0); (2,2,4); (0,3,5) | 6 |
| (8,24,30) | (2,6,0); (2,1,5); (0,4,4) | 6 |
| (12,20,30) | (3,0,5); (0,2,6); (2,4,2) | 6 |

The reference comparison concerns only sizes and matrices; it does not inspect D1 annotations.

## Obligation ledger

### 3CQ-MIN2-COVERAGE

Discharged. There are exactly 45 nonnegative integer rows (a,b,8-a-b), using a=0..8 and b=0..8-a. Their triple product enumerates every nonnegative integer row-sum-eight 3x3 matrix exactly once (91125 matrices). Filtering the diagonal sum equal to seven leaves exactly 9108 matrices; no prior component-size restriction enters this coverage.

### 3CQ-MIN2-EXACT-DOMAIN

Discharged. For every trace-seven candidate, the checker computes Q=R^2+R-10I by integer arithmetic. Three identical Q rows define n uniquely. It retains exactly positive even n_i>=2 and checks n_i r_ij=n_j r_ji for all pairs. Row sums imply sum(n)=64+8-10=62, also asserted. There is no n_i>=4, B<=2, D1, or original-graph-exclusion filter.

### 3CQ-MIN2-CANONICAL

Discharged. All six permutations act simultaneously on n and both axes of R; the lexicographic minimum identifies exactly the component-relabelling orbit. The independent row-first enumeration finds 18 labelled solutions, three orbits of six, with sizes (6,24,32), (8,24,30), and (12,20,30). No survivor has size two.

### 3CQ-MIN2-REFERENCE-MATCH

Discharged. The checker reads the original JSON solely after enumeration. It asserts exact equality of the canonical (sizes,R) set and asserts no repeated reference orbit. It also asserts 9108 tested, 18 labelled solutions and three orbits. D1 labels are ignored and are not part of the comparison.

### 3CQ-MIN2-SIZE-PREMISE

Discharged. For any positive-support component C of a symmetric nonnegative integer zero-diagonal repeat matrix with row sum three, 3|C| is twice its total unordered internal repeat weight. Thus |C| is a positive even integer, automatically at least two, without a bound on individual repeat entries. Consequently the new classification domain does not import triple-repeat elimination or B<=2.

### 3CQ-MIN2-PROVENANCE

Discharged. The new reusable checker and new min-two output are separate files. The prior discovery script, prior minimum-four JSON and original two-target audit remain unchanged. One standard-library checker run was pinned to one CPU and exited zero.

## Dependency delta

For a repeat-support component C, symmetry, integrality, zero diagonal and repeat row sum three give 3|C|=2 times its total unordered internal repeat weight. Thus |C| is positive and even, hence at least two. This elementary premise needs no B≤2 bound. The widened enumeration admits precisely this automatic size domain, so the quotient classification no longer requires triple-repeat elimination to justify discarding two-vertex components.

This replaces the old minimum-four prerequisite only for the new widened classification. It does not reinterpret or modify the historical minimum-four run, nor discharge any additional assumption in a separate original-graph theorem.

## Execution evidence

Ran once from the project root, with one available CPU selected through process affinity:

```bash
python computations/dd82/n62/check_three_component_quotients.py
```

Exit code: `0`. Checker wall time: `0.09996482357382774` seconds. The full output is also retained in the separate JSON result and in the machine-readable delta audit.

```json
{
  "status": "VERIFIED_EXHAUSTIVE_INTEGER_QUOTIENT_CHECK",
  "minimum_component_size": 2,
  "candidate_rows": 45,
  "row_triples_before_trace_filter": 91125,
  "tested_matrices": 9108,
  "raw_survivors": 18,
  "canonical_count": 3,
  "canonical_quotients": [
    {
      "sizes": [
        6,
        24,
        32
      ],
      "R": [
        [
          0,
          8,
          0
        ],
        [
          2,
          2,
          4
        ],
        [
          0,
          3,
          5
        ]
      ],
      "labelled_count": 6
    },
    {
      "sizes": [
        8,
        24,
        30
      ],
      "R": [
        [
          2,
          6,
          0
        ],
        [
          2,
          1,
          5
        ],
        [
          0,
          4,
          4
        ]
      ],
      "labelled_count": 6
    },
    {
      "sizes": [
        12,
        20,
        30
      ],
      "R": [
        [
          3,
          0,
          5
        ],
        [
          0,
          2,
          6
        ],
        [
          2,
          4,
          2
        ]
      ],
      "labelled_count": 6
    }
  ],
  "size_two_canonical_quotients": 0,
  "matches_original_quotient_list": true,
  "reference_json": "computations/dd82/n62/three_component_quotients.json",
  "D1_marks_checked": false,
  "cpu_count": 1,
  "wall_seconds": 0.09996482357382774,
  "scope": "All nonnegative integer 3x3 matrices with row sums 8, trace 7, R^2+R-10I having identical positive even rows, and balance. Component sizes 2 are included.",
  "nonclaims": [
    "No retained quotient is asserted graph-realizable",
    "No B<=2 or D1 minimum-size assumption is used",
    "D1 annotations and actual-graph exclusions are outside this check",
    "Other numbers of repeat-support components are outside this check"
  ]
}
```

All assertions passed. No concrete gap or counterexample was found in the widened classification. The potentially omitted size-two case is now part of the exhaustive domain and produces zero surviving quotient classes.

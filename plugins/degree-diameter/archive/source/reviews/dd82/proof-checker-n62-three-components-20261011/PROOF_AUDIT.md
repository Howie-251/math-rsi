# Bounded audit: three-component quotients and the 6/24/32 exclusion

**Outcome: PASS within the declared scope; same-family / provisional.** No concrete mathematical or enumeration gap found. The independent exact integer check is accepted as a deterministic result; the semantic proof review remains provisional.

## Review provenance and boundaries

- Reviewer thread: `/root/proof_review_n62_d1_reduction/sixteen_pure_arithmetic`.
- This is a reused-agent delta review, not a fresh fork. The reviewer previously checked only Sections 4–5 of the twelve-by-sixteen exclusion and did not author either new target. No prior audit output was used as proof evidence.
- Requested model/effort: `gpt-6-astra` / `ultra`; actual model and effort are not independently attested by runtime metadata.
- Applied `.agents/skills/proof-checker/SKILL.md`. The explicit bounded assignment overrides fresh-agent fan-out and ancillary artifacts: only this Markdown and its JSON companion are written. No source edits, hashes, HTML, PDF, TeX, or wiki updates.
- This is not a whole-paper-family or order-62 verdict. The D1 minimum-size result is a conditional import for labels only. The minimum-four enumeration domain imports exclusion of size-two components, for example from `B<=2`.

## Inputs

- `computations/dd82/n62/three_component_quotients.py`
- `computations/dd82/n62/three_component_quotients.json`
- `proofs/dd82/n62/THREE_COMPONENT_6_24_32_EXCLUSION.md`

Dependencies read directly:

- `proofs/dd82/n62/GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`
- `proofs/dd82/n62/TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md`
- `proofs/dd82/n62/S_TOUCH_SATURATED_ROW_EXCLUSION.md`

## Explicit statements and assumptions

For every nonnegative integer 3-by-3 matrix R with row sums eight and trace seven, form Q=R²+R−10I. Among those with three identical Q rows n, even n_i≥4, and n_i r_ij=n_j r_ji, there are exactly three simultaneous component-permutation classes. This is a quotient classification, not graph existence.

For every actual simple order-62 graph with maximum degree eight and diameter at most two, the specified actual repeat-support components of sizes 6,24,32 and matrix [[0,8,0],[2,2,4],[0,3,5]] are impossible. The graph proof uses the actual identities and triangle-pairing theorem, independently of enumeration completeness.

A is the symmetric 0/1 adjacency matrix; B=A²+A−7I−J is symmetric, nonnegative, integral, zero-diagonal, and row-sum three. R is the nonnegative integer equitable quotient, n its component-size vector. H,K,L are distinct B-support components. P(v) is the two-element subset N_G(v)∩H for v∈K. These meanings stay fixed throughout.

The spectral/equitability dependency is checked in Section 3 of the global quotient paper. The actual-graph identities follow from the Moore degree count and exact B definition. On n-perpendicular, the quotient polynomial x²+x−10 is irreducible over the rationals; equal multiplicities of its two conjugate roots yield trace seven for k=3.

No analytic interchanges, probability modes, asymptotics, or parameter-uniformity claims occur in the audited arguments.

## Obligation ledger

### 3CQ-FOUNDATIONS

Location: `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md:138-172`.

Discharged in declared scope. The B-eigenvalue-three space consists exactly of vectors constant on support components, by the weighted Dirichlet identity. AB=BA makes it A-invariant. Thus R has nonnegative integer entries, row sum eight, balance, and R^2+R=10I+1 n^T. On n-perpendicular the polynomial is x^2+x-10. Integer characteristic polynomial forces equal conjugate multiplicities, so three components give trace seven. Even component sizes follow from weighted degree three. Section 3 uses no D1 bound or global B<=2.

### 3CQ-ENUM-COVERAGE

Location: `three_component_quotients.py:20-28`.

Discharged in declared scope. All diagonal entries a,e,i are nonnegative with a+e+i=7, so each is at most seven. Therefore range(8) for a,e omits no candidate. Given a,e,i, the independent choices b=0..8-a, d=0..8-e, g=0..8-i determine exactly every nonnegative row-sum-eight matrix once. The sum of (9-a)(9-e)(9-i) over a+e+i=7 is 9108.

### 3CQ-EXACT-FILTERS

Location: `three_component_quotients.py:29-38`.

Discharged in declared scope. Integer Q=R^2+R-10I is computed entrywise. Equal rows mean Q=1 n^T with n uniquely determined. The explicit n>=4 and even tests specify the retained domain; Q1=62 1 makes sum(n)=62 automatic. The balance test checks every ordered pair. Component minimum four is conditional on excluding size-two repeat components, for example by B<=2; this task does not reprove that imported exclusion.

### 3CQ-CANONICALIZATION

Location: `three_component_quotients.py:39-45`.

Discharged in declared scope. Every permutation simultaneously reorders n, R rows and R columns. The minimum over all six permutations gives the same key exactly for component relabellings; it neither merges distinct orbits nor drops any. All retained n have distinct entries, and each of the three observed orbits contains six labelled matrices.

### 3CQ-INDEPENDENT-RESULT

Location: `three_component_quotients.json`.

Discharged in declared scope. A separately written checker enumerated all 45 nonnegative length-three rows summing to eight, then all row triples, filtering trace seven. It checked 9108 matrices, retained 18 labelled matrices and exactly three canonical orbits, exactly matching all saved sizes and matrices. Exit code zero; CPU affinity one.

### 3CQ-D1-CONDITIONAL-MARKS

Location: `three_component_quotients.py:47-61; GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md:184-200`.

Discharged in declared scope. The ordered marks use assumed current-paper |H|,|K|>=14, plus r_HK>=4 and r_KH>=3 for H!=K, or r_HH>=4 for H=K. These are necessary conditions only. Independent marking reproduces every JSON pair. The current-paper size bounds are flagged imports, not newly accepted by this task; no marked pair is asserted realizable.

### 3CQ-62432-PARENT-PARTITION

Location: `THREE_COMPONENT_6_24_32_EXCLUSION.md:81-97`.

Discharged in declared scope. For h in H, v in K, B_hv=0 because components are distinct. All neighbors of h lie in K, and v has exactly two K-neighbors. Thus c(h,v) is exactly the sum of membership indicators in their parent pairs. The distinct-vertex identity gives those indicators equal 1 minus membership in P(v), proving a disjoint partition of the six H vertices.

### 3CQ-62432-UNIQUE-PAIR

Location: `THREE_COMPONENT_6_24_32_EXCLUSION.md:99-115`.

Discharged in declared scope. A nonnegative integral repeat row of sum three cannot be positive at all five other H vertices. Choose h2 with B_h1h2=0. H is G-independent, so h1,h2 have exactly one common neighbor, which lies in K. Because K vertices have exactly two H-neighbors, the corresponding parent pair occurs at exactly that one vertex.

### 3CQ-62432-TRIANGLE

Location: `THREE_COMPONENT_6_24_32_EXCLUSION.md:117-136`.

Discharged in declared scope. The simple 2-regular induced graph G[K] supplies distinct v0,v1,v2 on a nonbacktracking length-two walk and then the other neighbor v3 of v2. Consecutive disjoint partitions imply P(v3)=H minus (P(v1) union P(v2))=P(v0). Uniqueness forces v3=v0, making an actual triangle on three distinct vertices.

### 3CQ-TRIANGLE-PAIRING-IMPORT

Location: `TRIANGLE_PAIRING_SIMPLE_REPEAT_EXCLUSION.md:15-112; S_TOUCH_SATURATED_ROW_EXCLUSION.md:25-75`.

Discharged in declared scope. For an actual triangle, t(v)<=1 makes its two incident triangle-repeat entries exactly one, leaving one unit mate. The S_TOUCH contradiction applies to this saturated root structure without using global simple B: each fixed row follows from specified unit entries exhausting sum three. Commutation then makes mates distinct and outside the triangle neighborhood; the indicator identity forces their three vertices to form another G-triangle. Matching unit repeats and internal triangle unit repeats exhaust all six rows, giving a closed connected six-vertex B-support component. No B<=2 or triple-repeat exclusion is used.

### 3CQ-62432-COMPONENT-CONTRADICTION

Location: `THREE_COMPONENT_6_24_32_EXCLUSION.md:138-164`.

Discharged in declared scope. The original triangle lies in K. Pairing places it in a connected closed six-vertex repeat-support component. Components sharing a vertex coincide, so K would have size six, contrary to 24. This proof does not depend on enumeration completeness, D1 classification/minimum size, or B<=2.

## Independent exact check

The checker uses all row compositions and filters the trace, independently of the source script’s diagonal-first loops. It does not execute or rewrite the source script. It ran once, pinned to one available CPU, using only the Python standard library. Exit code: `0`. Tool-reported wall time: `0.005598339` seconds.

Exact command:

```bash
python - <<'PY'
import itertools
import json
import os
from pathlib import Path

os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
rows = [(a,b,8-a-b) for a in range(9) for b in range(9-a)]
tested = 0
raw = []
canonical = {}
for R in itertools.product(rows, repeat=3):
    if sum(R[j][j] for j in range(3)) != 7:
        continue
    tested += 1
    Q = tuple(tuple(sum(R[i][k]*R[k][j] for k in range(3)) + R[i][j] - (10 if i == j else 0) for j in range(3)) for i in range(3))
    if len(set(Q)) != 1:
        continue
    n = Q[0]
    if not all(v >= 4 and v % 2 == 0 for v in n):
        continue
    if not all(n[i]*R[i][j] == n[j]*R[j][i] for i in range(3) for j in range(3)):
        continue
    assert sum(n) == 62
    raw.append((n,R))
    forms = [(tuple(n[i] for i in p), tuple(tuple(R[i][j] for j in p) for i in p)) for p in itertools.permutations(range(3))]
    key = min(forms)
    canonical[key] = canonical.get(key, 0) + 1

expected = json.loads(Path('computations/dd82/n62/three_component_quotients.json').read_text())
expected_keys = {(tuple(q['sizes']), tuple(map(tuple,q['R']))) for q in expected['canonical_quotients']}
assert tested == expected['tested_matrices'] == 9108
assert set(canonical) == expected_keys
for q in expected['canonical_quotients']:
    n,R = q['sizes'],q['R']
    independently_marked = []
    for h in range(3):
        for k in range(3):
            if min(n[h],n[k]) < 14 or R[h][k] < 4:
                continue
            if h != k and R[k][h] < 3:
                continue
            independently_marked.append([h,k])
    assert independently_marked == q['necessary_D1_component_pairs']
print(json.dumps({'candidate_rows':len(rows),'tested_trace7':tested,'raw_survivors':len(raw),'canonical_count':len(canonical),'orbits':[{'sizes':n,'R':R,'labelled_count':count} for (n,R),count in sorted(canonical.items())],'json_matrices_and_D1_marks_match':True,'cpu_affinity_count':len(os.sched_getaffinity(0))},indent=2))
PY
```

Exact printed output:

```json
{
  "candidate_rows": 45,
  "tested_trace7": 9108,
  "raw_survivors": 18,
  "canonical_count": 3,
  "orbits": [
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
  "json_matrices_and_D1_marks_match": true,
  "cpu_affinity_count": 1
}
```

The three quotient matrices and all saved conditional D1 pair lists match. The deterministic check does not establish graph realizability.

## Counterexample attempts and boundary checks

- **3CQ-BOUNDARY-DIAGONAL8** — Could a diagonal entry eight be omitted by range(8)? No: all diagonal entries are nonnegative and their sum is seven.
- **3CQ-PERMUTATION-LOSS** — Could simultaneous relabelling merge a different quotient or miss an orbit? All six permutations are enumerated on n and both R axes; independent full-row enumeration reproduces all 18 labelled survivors.
- **3CQ-MIN2-DOMAIN** — Could a positive even size-two component be silently omitted? It is explicitly outside the retained n>=4 domain. Coverage of actual graphs therefore imports the no-size-two consequence of B<=2; the pure graph exclusion does not.
- **3CQ-CYCLE6** — Could a longer K-cycle carry period-three parent labels without a triangle? Such cycles can have periodic labels, but any repeated label equals P(v0) after three steps. Its unique representative forces the vertex itself to return. This is exactly the added hypothesis that rules out a longer cycle through v0.
- **3CQ-WALK-COLLISION** — Could a short walk repeat vertices before the claimed triangle? Simplicity excludes loops; the other-neighbor choice excludes v2=v0 and v3=v1. The forced v3=v0 closes a triangle with three distinct vertices.
- **3CQ-PAIRING-EXTERNAL-REPEATS** — Could extra weighted repeat entries join the paired triangles to the rest of K? Each of the six vertices already has three distinct unit entries, exhausting its nonnegative repeat row of sum three. The paired support is connected and closed.

No counterexample found, and no claim is discharged merely by failure to find one: the proof obligations above give the deductive reasons.

## Dependency and scope closure

The graph argument is acyclic: actual identities and the specified quotient imply the parent-pair partition; a zero repeat pair in H gives one uniquely represented parent pair; a three-step walk then gives an actual triangle; the independently read triangle-pairing argument gives a closed connected six-vertex B-component, contradicting |K|=24. It imports neither the quotient enumeration nor any D1 minimum-size result.

The triangle-pairing proof’s S_TOUCH reference was inspected at the argument level: its local row saturations and commutation suffice without its globally stated simple-B premise. Thus the graph exclusion needs no B≤2 assumption or triple-repeat elimination. The separate diagnostic’s n_i≥4 restriction does retain its stated conditional import.

No fixes were needed. Remaining scope: the other two quotients, other component counts, realizability of retained quotients, a separate cross-family semantic overlay, and any Lean formalization remain outside this review.

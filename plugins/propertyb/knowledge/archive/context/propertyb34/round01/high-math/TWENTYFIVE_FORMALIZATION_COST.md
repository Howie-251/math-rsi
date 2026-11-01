# T34: shared coefficients for the 25-point formalization

2026-10-14. Scope: read the saved witnesses and existing Lean interfaces;
identify a small reusable arithmetic bridge. No catalogue search, DP search,
large numeric export, or whole-branch proof was run in this investigation.

The useful change is to prove one A/B/C grouping identity, then check a common
table for the 33 possible nine-lock row geometries. It is unnecessary to
re-expand binomial formulas for each of the 11,692 profiles. The existing
actual-hypergraph probability interface already accepts the resulting rows.

## Saved witnesses and the actual remaining inputs

`CANDIDATE_TWENTYFIVE.md` gives 11,692 q=5 profiles, of which 11,334 use five
fixed bare layouts and 358 use saved position-search witnesses. Reading
`V25_NINE_Q5_BOUNDS.json` confirms these counts and 104 distinct saved layouts:
five bare layouts and 99 layouts among the 358 other witnesses. Positions in
these JSON files are one-based; their order is the lock-label order.

| Bare positions | Assigned saved witnesses |
|---|---:|
| 9 through 17 | 79 |
| 8 through 16 | 1 |
| 10 through 18 | 5,268 |
| 11 through 19 | 5,831 |
| 17 through 25 | 155 |

These are counts of the first successful saved choice, not a new computation
of which other layouts would also succeed. The q=8 file has 840 witnesses and
603 distinct layouts; the q=9 file has 147 and 140. All these nine-lock
profiles can share the same numerical coefficient table.

The q=5 exporter deliberately removes `rows` and `certificates` from successful
DP witnesses. It retains their exact positions, counts and bound. Therefore,
the 358 corrected callers still need their quota multipliers and deductions
exported from those fixed positions. `SubsetEngine.verify` and
`pure_quota.certificate` show how to recover them without rerunning position
search. This investigation did not execute that recovery. The q=8/q=9 files
already retain rows and certificates.

## Existing Lean interfaces

The actual current file is `ThirtyFour/SingleLayoutApplication.lean`; there is
no `SingleLayoutProfile.lean` in the inspected tree.

* `LocalProfiles.realizes` takes arbitrary actual `H`, actual lock vertices,
  a position embedding, a complete no-duplicate label list, and equations
  `count H vertices T = μ T`. Given the finite `validProfile` check, it proves
  `RealizesProfile`. This is the existing actual-count binding to reuse.
* `Numeric.edgeWeight` and `Numeric.pairWeight` read only the profile's `v`
  and `positions`, and the edge types' lock lists. They do not read the
  profile's type counts, empty-pair cap or correction centers. The new probe
  proves this by definitional equality, for arbitrary profiles and types.
* `Numeric.boundA` and `boundB` are linear sums of those coefficients.
  `boundC`, when `emptyPairCap = none`, is the ordered quadratic sum with
  capacity `μ(T) * (μ(U) - if T = U then 1 else 0)`. The probe proves the
  exact separated formula without discarding the diagonal correction.
* `ProfileApplication.endpoint_sum_eq` and `critical_sum_le`, followed by
  `ConditionalUnion.propertyB_of_position_bounds`, consume arbitrary A/B/C
  rows for the actual locked experiment. Bare layouts need no deletion
  theorem. `propertyB_of_uncorrected_profile` is another existing entry when
  one prefers to return to `Numeric.totalBound`.
* `SingleLayoutApplication.propertyB_of_single_layout` is the existing
  corrected-row caller. It takes actual profile realization, avoided quotas,
  nonnegative multipliers, a certified loss, and the strict sum with the loss
  inside C before taking the minimum. `MixedLayoutApplication` is available
  for genuine mixed-layout certificates; the five bare layouts do not require
  it merely because there are five alternatives.

`LocalProfiles.executableType_eq` and `weights_eq` already connect executable
lock lists to the canonical representation. They do not cache A/B/C numerical
coefficients or prove the residual-size grouping below. No existing generic
row-grouping/cached-coefficient theorem was found in the inspected modules.

## The smaller common table

Fix nine injected lock labels and an actual position K in 1 through 25. Let
L, P, R be the labels strictly left of K, exactly at K, and strictly right
of K. Injectivity gives `|P| = 0` or `1`. Put

\[
 N=16,\qquad a=K-1-|L|,\qquad b=25-K-|R|.
\]

At a locked position, `a+b=16`; at a free position, `a+b=15`. The numerical
coefficients depend only on this choice, a, and residual sizes r and q. They
do not depend on the identities in L/P/R, the complete layout, or μ.

For each r define

\[
 \ell_r=\sum_{T:\ P\subseteq T,\ T\setminus P\subseteq L,\ |T|+r=5}\mu_T,
 \qquad
 u_r=\sum_{T:\ P\subseteq T,\ T\setminus P\subseteq R,\ |T|+r=5}\mu_T.
\]

Only positive actual traces of size at most five are needed. Use r,q in
0 through 5 at locked positions, and 1 through 5 at free positions. The
coefficients, directly in the convention of `Numeric`, are as follows.

At locked positions:

\[
 A_r={\binom a r\over\binom{16}r},\quad
 B_r={\binom b r\over\binom{16}r},\quad
 C_{r,q}={\binom a r\binom b q\over
                 \binom{16}r\binom{16-r}q}.
\]

At free positions:

\[
 A_r={r\binom a{r-1}\over16\binom{15}{r-1}},\quad
 B_r={r\binom b{r-1}\over16\binom{15}{r-1}},\quad
 C_{r,q}={\binom a{r-1}\binom b{q-1}\over
                 16\binom{15}{r-1}\binom{16-r}{q-1}}.
\]

The required generic grouping identity is

\[
 A(K)=\sum_r\ell_r A_r,\qquad B(K)=\sum_r u_r B_r,
\]
\[
 C(K)=\sum_{r,q}\ell_r u_q C_{r,q}
       -\mu_P C_{5-|P|,5-|P|}.
\]

Why the last term is exact: an ordered compatible pair has its non-pivot
locks on disjoint sides. If its two traces are equal, both must be P. The
product counts that diagonal as μ(P)^2, while distinct actual edges require
μ(P)(μ(P)-1). The probe's `diagonal_count` proves the needed natural-to-rational
identity even at μ(P)=0. There is no independence assumption about the two
free sets and no extra r*q multiplier in C.

There are 17 locked geometries and 16 free geometries. Keeping all 6 locked
residual sizes and 5 free residual sizes requires at most
`17*(2*6+6*6) + 16*(2*5+5*5) = 1376` A/B/C scalars, including zeros. A uniform
`Fin 6` implementation can instead store 1584 entries and set unused free
r=0 coefficients to zero. Both sizes are far smaller than a dense
layout-by-position-by-512-by-512 trace-pair table.

The nine-lock coefficient table is reusable for q=5,8,9 and all their saved
layouts. The ten-lock extensions have N=15 and can use an analogous separate
table. No need to implement the ten-lock table before the nine-lock caller
works.

## A precise Lean bridge and a checked caller probe

`TwentyFiveCoefficientProbe.lean` is a separate interface experiment, not an
import of the production target. It contains these exact reusable equalities:

```lean
edgeWeight_geometry (p : Numeric.Profile) (t : Numeric.EdgeType)
  (k : ℕ) (last : Bool) :
  Numeric.edgeWeight p t k last =
    Numeric.edgeWeight (geometry p.v p.positions) ⟨t.locks,0⟩ k last

pairWeight_geometry (p : Numeric.Profile) (t u : Numeric.EdgeType) (k : ℕ) :
  Numeric.pairWeight p t u k =
    Numeric.pairWeight (geometry p.v p.positions) ⟨t.locks,0⟩ ⟨u.locks,0⟩ k

profile_geometry (labels : List (Finset (Fin n)))
  (positions : Fin n ↪ Fin v) (μ : Finset (Fin n) → ℕ) (centers : List ℕ) :
  geometry (profile labels positions μ centers).v
    (profile labels positions μ centers).positions =
    geometry v (canonicalType positions Finset.univ)
```

`boundA_geometry`, `boundB_geometry` and `boundC_geometry` lift these to the
linear/quadratic sums over positive profile rows. These equalities already
allow sparse fixed-layout coefficient tables as a first implementation. For
the 33-row compression, add one general theorem with the following interface:

```lean
-- Intended next theorem, not yet implemented:
cached_rows_eq
  (positions : Fin 9 ↪ Fin 25)
  (labels : List (Finset (Fin 9)))
  (nodup : labels.Nodup) (all : ∀ T, T ∈ labels)
  (μ : Finset (Fin 9) → ℕ)
  (valid : Numeric.validProfile (profile labels positions μ []) 34)
  (k : Fin 25) :
  Numeric.boundA (profile labels positions μ []) (k.val+1) = cachedA positions μ k ∧
  Numeric.boundB (profile labels positions μ []) (k.val+1) = cachedB positions μ k ∧
  Numeric.boundC (profile labels positions μ []) (k.val+1) = cachedC positions μ k
```

Here `cachedA/B/C` are the explicit slice sums and diagonal correction above.
Prove this once by grouping the existing sums by residual size. Zero-count
pruning contributes zero; the corresponding diagonal term is also zero.
The actual label-list and position-type injectivity facts already live in
`MultiLockRecovery` and `LocalProfiles`. The cached coefficient equalities
should be proved once for the small geometric domain, and then rewritten
before each finite profile check. Merely putting the original combinatorial
function in a `let` does not establish such reuse for kernel reduction.

The probe's `propertyB_of_cached_rows` is an actual caller: it takes arbitrary
`H : Simple5Hypergraph (Fin 25)`, two `Fin 9` embeddings, the complete label
list and actual `count H vertices T = μ T` equations, the finite profile
validity, A/B/C row identities, and the strict sum of minima. It constructs
`RealizesProfile` internally and returns `PropertyB H` via the existing event
semantics. Thus no new probability theorem or assumed realization is needed.
The row identities, validity and strict inequality are explicit remaining
finite obligations, not silently assumed proofs of the whole branch.

## Execution cost and recommended next step

First implement the generic grouping theorem and the 33-row coefficient
table, then test one saved q=5 bare witness through the existing actual
caller. Use positive profile rows to form the 6+6 slice sums; do not scan a
512-by-512 matrix for every profile. Once row equality is established, each
profile check consists of integer/rational additions and small quadratic
sums, with no fresh binomial derivation.

For the large bare batch, a common scale D=16! removes repeated rational
normalization. The integer coefficients are

* locked A: `(a)_r * (16-r)!`, and B with b;
* free A: `r*(a)_(r-1)*(16-r)!`, and B with b;
* locked C: `(a)_r*(b)_q*(16-r-q)!`;
* free C: `(a)_(r-1)*(b)_(q-1)*(17-r-q)!`.

Here `(a)_r` is the falling factorial, zero if r>a. Keep the C subtraction
in integers until its proved equality to the nonnegative rational row;
do not silently replace it by truncated subtraction. One generic positive-D
lemma changes strictness to `sum min(A_D,B_D,C_D) < D`. The integer scaling
lemma and grouping identity are proposed next work, not claims that this
probe has already verified them.

The 358 corrected witnesses still use ordered capacities, both-direction
pair weights and the actual avoided-quota deductions. Their A/B/C part
shares this table, but the residual-size grouping of bare C alone does not
justify grouping their quota penalties. Preserve the existing sparse
type-pair `penaltySum` interface for those corrections unless a separate
grouping lemma is proved.

The full classification coverage, relabeling, validity and saved witness
strictness remain needed. This investigation changes their proposed
arithmetic cost, not their scope or truth status. No runtime improvement is
claimed before a representative formal numeric caller has been measured.

## Verification record

The unique regular Lean executor ran the probe using the existing imported
artifacts, from `formal/`:

```sh
lake env lean ../context/propertyb34/round01/high-math/TwentyFiveCoefficientProbe.lean
```

`TwentyFiveCoefficientProbe-r4.log` is the successful final run, exit 0. Its
three axiom queries for `boundC_geometry`, `diagonal_count` and
`propertyB_of_cached_rows` all contain exactly `propext`, `Classical.choice`
and `Quot.sound`. The helper author inspected the saved output and did not
launch a parallel Lean process. This is a local incremental interface check,
not a classification proof or numeric verification of the 11,692 profiles.

The first three failed runs remain beside it. The first lacked the ring
tactic import, the second selected the unbuilt aggregate `Ring` module, and
the third used `ring` while the already-built `Ring.Basic` exposes `ring1`.
The final source imports `Mathlib.Tactic.Ring.Basic` and uses `ring1`; no
mathematical statement or caller premise was changed to obtain the result.

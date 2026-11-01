# Fresh semantic audit, round 8

Date: 2026-10-06. Reviewer: fresh Codex sub-agent `/root/formal_semantic_adversary`.

`review_independence: same-family`  
`acceptance_status: provisional`

Result within scope: **no concrete semantic defect found**. This is not acceptance of the full theorem T. I did not review the complete 19–25 structural case assembly or independently discharge the corrected-profile center inequalities. In particular, I did not treat the generic application interfaces as proofs that their profile or deletion hypotheses hold for every hypergraph.

## Inputs and actual scope

Read the local `AGENTS.md`, `FORMAL_SPEC.md`, the proof-checker skill, and the complete sources `formal/Aris4Math.lean`, `Reduction.lean`, `SmallVertices.lean`, `ProfileProbability.lean`, `TypeCounting.lean`, and `ProfileApplication.lean`. Followed the relevant definitions and arguments in `Structure`, `Counting`, `JointCounting`, `EndpointCounting`, `CriticalCounting`, `Greedy`, `ConditionalUnion`, `Numeric`, and `ProfileDeletion`. These dependency reads were targeted, not a claim to have audited every theorem in those modules. No prior review verdict was used as mathematical evidence. No shared proof source was edited.

The questions were whether the formal statement is the original finite, simple, five-uniform coloring problem; whether the finite reduction is sound without extra hypotheses; and whether the profile arithmetic bounds the same conditional permutation events that yield a legal coloring.

## Original target and finite reduction

`Aris4Math.lean:25–39` encodes a finite set of finite vertex sets with each edge of cardinality five. Finsets exclude duplicate edges and repeated vertices. `PropertyB` requires a Boolean coloring whose true-colored vertices number between one and four in every edge; it therefore excludes both monochromatic colors, without imposing balance. `Target.{u}` ranges over all `Fintype` vertex types in universe `u` and all such hypergraphs with at most 32 edges. This is FORMAL_SPEC T. The empty vertex and empty edge cases are included. The choice of a `Fintype` enumeration is not a mathematical restriction on a finite set.

`Reduction.lean:22–62` proves exactly the needed edgewise-injective image construction and count-preserving pullback of colors. The merge at lines 105–170 identifies only two vertices that never occur together in an edge, proves edgewise injectivity, and permits image edges to collapse. I tested the latter possibility conceptually with edges `{0,2,3,4,5}` and `{1,2,3,4,5}` merged along `1 → 0`: the two image edges coincide. This does not break the actual argument, because minimality is among **all counterexamples with at most 32 edges** (`182–235`), not among exactly-32-edge counterexamples or a preselected structural family.

Padding at `Reduction.lean:260–292` uses the original `Fin v` vertex set, produces five-element edges, preserves inclusion of the old edge set, and carries noncolorability by restriction of a hypothetical coloring. Pair coverage is inherited by retaining its old witnessing edges. There is no need to preserve noncolorability under an arbitrary vertex expansion or to assume the literature baseline.

The upper vertex bound is obtained from actual edge incidences in `Structure.lean:23–93`. Here the implementation uses the sufficient inequality `v(v−1) ≤ 640`, already contradicted by `v ≥ 26`; it need not duplicate the ceiling-degree presentation in the specification. `SmallVertices.lean:42–115` counts monochromatic events in the full permutation sample and explicitly constructs the pullback coloring, while lines 119–142 apply only the ten scalar inequalities for 9–18 vertices and the separate ≤8 argument. This uses balanced colorings as a sufficient construction, not as an equivalence for arbitrary colorability.

`SmallVertices.lean:147–184` consequently gives exactly the 19–25, exactly-32-edge, pair-covering finite goal. The forward implication of `target_iff_finite_goal` explicitly uses `ULift.{u}`; it does not silently specialize a universe-polymorphic assumption to an unavailable smaller-universe type. The reverse implication returns the original universe-polymorphic target through relabeling.

## Conditional sample and actual events

The sample is literally `{σ : Perm (Fin v) // ∀ i, σ (vertices i) = positions i}` (`EndpointCounting.lean:14–21`). Both maps are embeddings, so both vertex and position locks are distinct. The count `(v−|ι|)!` is proved by extending the prescribed bijection, not assumed (`Counting.lean:75–99`). In particular the denominator is nonzero, including the fully locked case `0! = 1`; `ConditionalUnion.lean:105–110` invokes this positivity when passing from probability below one to a successful permutation.

The permutation is consistently vertex → position. `Greedy.lean:17–31` defines the scan, `119–208` derives the critical ordered pair from its actual flip history, and `241–285` pulls the resulting coloring back to the original edges and proves the literal red-count bounds. `ConditionalUnion.lean:39–126` applies endpoint, pair, and failure union bounds in that same locked sample. It never assumes the converse “critical pair implies algorithm failure.”

I independently re-derived the factors. Write `N` for the number of free vertices, `a,b` for free slots before/after the center, and `r,q` for the numbers of free vertices in the two edges. For a fixed singleton intersection at a free center, the center has probability `1/N` of occupying its specified free position. The remaining disjoint vertex groups have sizes `r−1,q−1`, so their contribution is

\[
\frac{\binom a{r-1}\binom b{q-1}}
 {N\binom{N-1}{r-1}\binom{N-r}{q-1}}.
\]

There is no `r*q` factor for this fixed ordered edge pair. At a locked center the factor is instead `binom(a,r) binom(b,q) / [binom(N,r) binom(N−r,q)]`. A free **single-edge endpoint** has `r` disjoint possible endpoint vertices, which explains its separate `r` factor. These are the formulas identified by `ProfileProbability.lean:179–214,302–395`, through actual event-count theorems. Feasibility and free-group capacity are derived from the actual sets (`246–279,321–335,373–378`). Larger or empty intersections, and inconsistent center locks, are treated as zero actual probability, with only a nonnegative type upper bound (`400–439`).

The locks are parameters fixed before the sample is formed. The theorems do not choose them separately for each sampled permutation.

## Profile matching, directed coefficients, and deductions

`TypeCounting.lean:23–53` converts each edge's actual locked vertices to a sorted list of **one-based locked positions**. `RealizesProfile` requires the correct vertex count, valid lock data, equality with the image of the position embedding, coverage of every actual edge type, unique type labels, and exact fiber cardinalities. Thus the table is not a list of stipulated coefficients unrelated to H. The temporary `EdgeType` values with `count = 0` passed to weight formulas cause no problem: `edgeWeight` and `pairWeight` use the locks, while actual multiplicities are separately restored by the table equalities.

The indexing conversion is explicit at `ProfileProbability.lean:58–115`: `k.val + 1`, the number of free slots on each side, and `N` all match the Numeric inputs. `TypeCounting.lean:125–137` sums exactly positions 1 through v. Equality of `positions.toFinset` loses list order but not any quantity used here, since validity provides no duplicates, and each count depends only on membership or a filter predicate. Actual edge-type lists themselves are canonical sorted lists.

`TypeCounting.lean:56–80,99–120,155–209` counts actual ordered distinct pairs. Its coefficient is `m_t (m_u − [t=u])`, including zero- and one-member fibers. It neither divides by two nor identifies opposite directional weights. For example, a two-member single type yields two directed pairs, whereas two different singleton types yield one pair in each direction.

An attempted misuse is worth separating from a defect: `validProfile` alone permits the empty-type cap `some 0` for a 20-vertex, 32-edge no-lock profile. Its numerical C is zero, although an actual singleton-intersection pair can have positive critical probability. The inspected ordinary aggregation and both profile application theorems explicitly require `emptyPairCap = none` (`TypeCounting.lean:196–209`, `ProfileApplication.lean:47–51,70–79`), so this counterexample does **not** satisfy their hypotheses. The special v20 cap argument was outside this audit.

The corrected-profile application retains a concrete obligation at `ProfileApplication.lean:74–78`: every designated locked center must supply the stated weighted lower bound over its actual `directedBadPairs`. `ProfileDeletion.lean:17–104` assigns exactly that set at the unique corresponding locked position and the empty set elsewhere. `ConditionalUnion.lean:131–156` removes each actual directed pair at most once and proves its actual event has probability zero. It does not assume a lower bound on each deleted directional weight or forbid zero weights. Finally, the code subtracts D from C **before** taking the minimum (`Numeric.lean:115–119`, `ProfileApplication.lean:80–103`), so it does not assume that the final minimum drops by the full D.

These are genuine conditional interfaces, with explicit realization and center obligations. I found no circular use of T, PropertyB, or a desired event bound in the inspected discharge chain.

## Executed checks and limits

Used project-local Lean 4.24.0 through `lake env lean --stdin` to import `Aris4Math.SmallVertices` and `Aris4Math.ProfileApplication`, print the original target and the exact three relevant theorem declarations, and inspect axioms. `target_iff_finite_goal`, `propertyB_of_uncorrected_profile`, and `propertyB_of_corrected_profile` depend only on `propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx` or custom theorem assumption appears in these transitive axiom lists. The five inspected module sources with compiled artifacts were not newer than their corresponding `.olean` files. This was an import/axiom inspection, not a clean rebuild of the project.

Executed a separate Python rational-count probe over five local cases on nine vertices. The primary edges were `A={0,1,2,3,4}` and `B={4,5,6,7,8}`, with zero-based vertex/position labels. The probe enumerated actual remaining permutations, counted minima/maxima and the exact ordered critical event, and compared against the independently written combinatorial formulas above:

| Case | Vertex → position locks | Sample size | Critical occurrences |
|---|---|---:|---:|
| Free center | `0→1, 8→7` | 5,040 | 36 |
| Locked center | `0→1, 4→4, 8→7` | 720 | 36 |
| Incompatible orientation | `0→7, 8→1` | 5,040 | 0 |
| Whole first edge locked | `i→i` for `i=0,…,4` | 24 | 24 |
| Nonsingleton intersection | `0→1, 8→7`, with `B={3,4,5,6,8}` | 5,040 | 0 |

All 135 endpoint/pair comparisons held across 15,864 permutations. The fourth case has critical probability exactly one and checks that complete edge locking cannot accidentally manufacture a zero denominator or zero event. These are targeted reverse tests of the formulas, not evidence that all hypergraphs are colorable, and they do not replace the quantified Lean arguments.

No repair request results from this scope. The remaining full-target assessment must concern the actual structural realizations and corrected-center inequalities used in every case, and their final assembly; this record makes no judgment that those remaining obligations are complete.

## Scope extension after the first successful Main build

The parent subsequently supplied the completed `Main.lean` assembly and requested a final inspection of the new 22/23 branches. This section supersedes the earlier statement that no assessment of the completed assembly or these particular structural realizations had been made. The review remains same-family/provisional; the internal proofs of the 19/20/21/24/25 branches were not freshly re-audited in this extension.

Additional sources read completely: `Main.lean`, `TwentyTwo.lean`, `TwentyThree.lean`, `DoubleTripleLockProfiles.lean`, `TripleLockProfiles.lean`, `LowDegree.lean`, `LinkWeightCertificates.lean`, and `LinkCounting.lean`. Also read the unordered/directed conversion and exception-capacity arguments in `LinkDeletion.lean:1–215`.

### The completed theorem has the original quantifiers

`Main.lean:16–25` proves the finite goal by all seven cases, 19 through 25, and calls the actual branch theorems on the same H. `Main.lean:29–30` applies the previously audited finite reduction. `Main.lean:33–38` expands the conclusion into the literal Boolean red-count predicate.

I independently imported `Aris4Math.Main` and printed the theorem declarations, the elaborated seven-case assembly, and transitive axiom lists. The printed top-level statement is universe-polymorphic:

```lean
Aris4Math.two_colorable_of_at_most_thirty_two.{u}
  (V : Type u) [Fintype V] (H : Aris4Math.Simple5Hypergraph V)
  (edges : H.edges.card ≤ 32) :
  ∃ c, ∀ e ∈ H.edges,
    1 ≤ {x ∈ e | c x = true}.card ∧
    {x ∈ e | c x = true}.card ≤ 4
```

There is **no** remaining pair-covering, bounded vertex-count, degree, profile, deletion, or probability hypothesis at this level. `propertyB_of_at_most_thirty_two.{u}` is a theorem of `Target.{u}`, not a redefinition or weakening of Target. Its expanded theorem, the Target theorem itself, and both 22/23 branch theorems report exactly `[propext, Classical.choice, Quot.sound]`.

As an extra statement-alignment check, I successfully elaborated the following independent restatement through stdin, without adding a source file:

```lean
theorem semantic_audit_raw_finite_statement (V : Type u) [Finite V]
    (E : Finset (Finset V)) (five : ∀ e ∈ E, e.card = 5)
    (edge_bound : E.card ≤ 32) :
    ∃ c : V → Bool, ∀ e ∈ E,
      1 ≤ (e.filter (fun x => c x = true)).card ∧
      (e.filter (fun x => c x = true)).card ≤ 4 := by
  classical
  letI := Fintype.ofFinite V
  exact Aris4Math.two_colorable_of_at_most_thirty_two V ⟨E, five⟩ edge_bound
```

Its axiom list is again the same three standard axioms. Thus the result applies to an arbitrary finite type without the user supplying a chosen enumeration, and directly to an arbitrary finite family of five-element vertex sets. This is FORMAL_SPEC T. The new compiled artifacts inspected were not older than their corresponding sources.

### 22/23 selection is derived from actual incidences

`LowDegree.lean:84–146` obtains an actual codegree-one pair on 22 vertices with degrees `(6,6)`, `(6,7)`, or `(7,7)`. I rechecked the budgets: pair coverage gives minimum degree six. If x has degree six, at most three other vertices have codegree greater than one, leaving at least eighteen good partners. If all such partners had degree at least eight, the total degree would be at least `6·22 + 2·18 = 168 > 160`. If no vertex has degree six, at least sixteen have degree seven, whereas a degree-seven vertex plus its bad partners exclude at most eight vertices. A second degree-seven good partner therefore exists. None of these conclusions is an extra assumption on H.

`LowDegree.lean:159–238` derives both complete alternatives on 23 vertices. Since the minimum degree is six and `7·23 > 160`, an actual degree-six x exists. It has at least twenty codegree-one partners W. Either one also has degree six, giving the first alternative, or W has minimum degree seven. In the latter case the incidence budget forces at least eighteen degree-seven members S of W. Choose y in S, and the unique edge e through x,y. The excluded set `{y} ∪ badPartners(y) ∪ e` has size at most twelve, leaving z in S outside it. This yields three distinct vertices, degrees `(6,7,7)`, all three pair codegrees one, and no edge through all three: such an edge would equal e by codegree-one uniqueness, contradicting z outside e. In particular, `noTriple` is obtained from the actual selection rather than silently assumed.

### The tables are the actual fibers, and correction premises close

The two-lock positions are Fin values 10 and 11, corresponding to one-based positions 11 and 12 (`DoubleTripleLockProfiles.lean:11–45`). The four edge fibers are split by membership of x,y. Their exact counts (`76–104`) are

\[
\bigl(m_{\varnothing},m_x,m_y,m_{xy}\bigr)
  = \bigl(33-d(x)-d(y),\ d(x)-1,\ d(y)-1,\ 1\bigr).
\]

These follow from a partition of all 32 actual edges and the actual codegree-one condition. Lines 108–172 convert that partition to `RealizesProfile`; the validity assumption of the general helper is discharged by the corresponding closed Numeric validity theorem in each concrete instance.

For three locks, `TripleLockProfiles.lean:30–106` groups the actual H.edges by all eight subsets of the three lock indices. The cardinality, degree, and codegree equations plus the proved absent triple force counts

\[
(m_{\varnothing},m_x,m_y,m_z,m_{xy},m_{xz},m_{yz},m_{xyz})
 = (15,4,5,5,1,1,1,0).
\]

For example, all pair-only counts equal one, the single counts are `6−2,7−2,7−2`, and the remaining count is `32−(4+5+5+3)=15`. Lines 109–131 prove injectivity and exact fiber transport into the one-based position lists `[11]`, `[12]`, `[13]`; lines 194–252 prove complete realization. The eight-label case distinction concerns only subsets of three specified locks, not enumeration of hypergraphs.

`TwentyTwo.lean:51–57` and `TwentyThree.lean:43–50` invoke the proved selection theorems and eliminate each disjunct. Their printed signatures retain only H, `H.PairCovering`, and `H.edges.card = 32`. The internal subcase assumptions are supplied by the selection outputs. Each probability application supplies the realized profile, proves `noCap` by reduction, and supplies its closed strict Numeric theorem; no desired probability inequality is passed in from the caller.

The corrected branches supply every `center_lower` obligation. I checked `LinkWeightCertificates.lean:116–232` and the last-center exception at `303–334`. The actual unordered bad-link count comes from pair-incidence double counting (`LinkCounting.lean:59–137`), using at most three common vertices other than the center for two distinct five-element edges. The resulting count is `ceil((4d−(v−1))/3)`: three slots for degree seven at v22, one slot for degree six at v23, and two slots for degree seven at v23. Closed type comparisons bound the **sum of both directional weights** of each charged slot; exact type multiplicities rule out selecting two distinct edges from a type of size one.

At position 13 of the 677 profile, the two exceptional types `[11,13]` and `[12,13]` each have exactly one actual edge. Their union S has at most two edges and therefore contributes at most one unordered exceptional pair. `LinkDeletion.lean:178–215` proves the capacity bound and charges only pairs not contained in S, keeping nonnegative weights for the exception. Since at least two bad slots exist, at least one remains chargeable at `3/323`. This handles the actual zero-weight bad-pair possibility; it does not assume every bad slot has positive weight. The Numeric deduction is then bounded by the charged amount before the previously audited minimum operation.

**Extension result:** no concrete mismatch or undischarged application hypothesis found in the new scope. The completed Main declaration proves the original T under the three standard Lean axioms, and the inspected new 22/23 structural, fiber-count, and correction connections explain why no profile or probability premise survives at the top level. This is a positive finding about the actual declaration and inspected dependency paths, not a claim that this one reviewer has separately re-read every branch module.

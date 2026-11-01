### Statement-Fidelity Comparative Review

This review compares the blind back-translation in [`grok_lean_blind_translation_r4.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/reviews/research/grok_lean_blind_translation_r4.md) against the four source files ([`Aris4Math.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math.lean), [`Greedy.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Greedy.lean), [`Counting.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Counting.lean), [`SevenPoint.lean`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/SevenPoint.lean)) and the paper specifications in [`FORMAL_SPEC.md`](file:///Users/rfy_naiveai/Desktop/aris4math/FORMAL_SPEC.md), [`PROBABILITY_LEMMAS.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md), and [`STRUCTURE_24_25.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/STRUCTURE_24_25.md).

---

### 1. Summary Finding

- **Mathematical Claim Fidelity:** **No mismatch found.** Every formal Lean statement in the four files faithfully encodes its intended local mathematical claim.
- **Blind Translation Fidelity:** **No concrete error found.** Grok's blind translation accurately characterizes the exact semantic definitions, quantifier scopes, assumptions, and directional limitations across all declarations.
- **Scope Boundary:** As correctly recognized by both the Lean code comments and Grok's translation, these four files **do not prove** [`Target`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math.lean#L37-L39). They establish local machinery: abstract pigeonhole/weighted deletion interfaces, the deterministic greedy algorithm and its one-sided critical-pair cover on $\mathrm{Fin}\;v$, exact permutation counting lemmas under injections/subsets, and the isolated seven-point triple deletion contradiction.

---

### 2. Detailed Dimension Audit

#### A. Target: Arbitrary Finite Type, $\le 32$ Edges, No Monochromatic Edges
- **Intended Claim ([`FORMAL_SPEC.md`](file:///Users/rfy_naiveai/Desktop/aris4math/FORMAL_SPEC.md#L9-L40) D1, D2, T):**
  $H=(V,E)$ on arbitrary finite $V$; simple 5-uniform hypergraph ($E \subseteq \binom{V}{5}$); $|E| \le 32 \implies \exists c: V \to \{0,1\}$ such that no edge is monochromatic ($1 \le \sum_{u \in e} c(u) \le 4$).
- **Formal Statements:**
  - [`Simple5Hypergraph`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math.lean#L25-L27): `edges : Finset (Finset V)` with `∀ e ∈ edges, e.card = 5`.
  - [`PropertyB`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math.lean#L31-L35): `∃ c : V → Bool, ∀ e ∈ H.edges, 1 ≤ (e.filter (fun x => c x = true)).card ∧ (e.filter (fun x => c x = true)).card ≤ 4`.
  - [`Target`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math.lean#L37-L39): `∀ (V : Type u) [Fintype V] (H : Simple5Hypergraph V), H.edges.card ≤ 32 → PropertyB H`.
- **Fidelity & Translation:**
  The Lean statements impose no extra conditions (no vertex count restriction, pair-covering, or regularity on $V$). Grok explicitly confirms: $V$ is universe-polymorphic, edges are size 5, Property B is non-monochromatic 2-coloring, and [`Target`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math.lean#L37-L39) is a proposition definition with no proof or instance in these files.

#### B. Permutation Direction
- **Intended Claim ([`FORMAL_SPEC.md`](file:///Users/rfy_naiveai/Desktop/aris4math/FORMAL_SPEC.md#L133-L146) M1/M2, [`PROBABILITY_LEMMAS.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md#L59-L90) P1):**
  A permutation assigns vertex $\to$ position, $\operatorname{pos}_\sigma(x) = \sigma(x)$. Positions $0, \dots, v-1$ are scanned in increasing order; vertex $x$ is processed when its position $\sigma(x)$ is reached.
- **Formal Statements:**
  - [`orderedEdges`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Greedy.lean#L177-L179): `E.image (fun e => e.map σ.toEmbedding)` pushes edges forward to position-space.
  - [`blueAfter`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Greedy.lean#L23-L31): scans positions $t \in \{0, \dots, v-1\}$ in natural numeric order on $\mathrm{Fin}\;v$.
  - [`CriticalPair`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Greedy.lean#L109-L115): $A \ne B$, $x = \max A = \min B$, $A \cap B = \{x\}$.
  - [`FailureAt`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Greedy.lean#L188-L189) & [`CriticalAt`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Greedy.lean#L192-L196): formulated on pushforward images $\sigma(A), \sigma(B)$ at position $k$.
  - [`propertyB_of_successful_permutation`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Greedy.lean#L241-L286): pulls back the coloring to original vertices via $c(x) := \mathrm{decide}(\sigma(x) \notin \mathrm{blue})$.
- **Fidelity & Translation:**
  Lean's pushforward matches the paper's scan order $\sigma^{-1}(0), \dots, \sigma^{-1}(v-1)$. Grok translates this duality accurately: *"$\sigma$ is applied to vertices first, and the greedy scan then runs in increasing numeric order on the image hypergraph. Equivalently, original vertex $x$ is considered at time $\sigma(x)$."*

#### C. Failure-to-Critical: Only One Implication
- **Intended Claim ([`PROBABILITY_LEMMAS.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md#L59-L90) P1):**
  Greedy algorithm failure implies the presence of a critical pair: $\mathrm{Fail} \subseteq \bigcup_{k=1}^v Q_k$. The converse does not hold.
- **Formal Statements:**
  - [`uniform_failure_covered`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Greedy.lean#L163-L174): `Failure E → ∃ A B x, CriticalPair A B x`.
  - [`failureAt_covered`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Greedy.lean#L198-L209): `FailureAt E σ → ∃ k, CriticalAt E σ k`.
  - [`failure_event_cover`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Greedy.lean#L227-L238): `badPermutations E sample ⊆ (Finset.univ).biUnion (criticalPermutations E sample)`.
- **Fidelity & Translation:**
  Only the forward inclusion is proved. Grok correctly notes that the converse is unproved and mathematically false, giving a separating 5-uniform counterexample:
  $v=9, \sigma=\mathrm{id}, E=\{\{0,1,2,3,4\}, \{4,5,6,7,8\}\}$, where $\mathrm{CriticalAt}$ holds at $k=4$, but the greedy coloring succeeds with blue set $\{4\}$ (each edge contains both blue and non-blue vertices).

#### D. Sample Cardinality versus Probability
- **Intended Claim ([`PROBABILITY_LEMMAS.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md#L198-L253) P6/P7):**
  Probabilistic upper bound $\Pr(\mathrm{Fail}) \le \sum \min(A_k, B_k, C'_k) < 1$. In a finite sample space $\Omega$, clearing denominators yields $\sum \min(A_k |\Omega|, \dots) < |\Omega|$.
- **Formal Statements:**
  - [`exists_outside_bad_of_min_bounds`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math.lean#L58-L85) & [`exists_outside_bad_of_weighted_deletion`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math.lean#L144-L172): bounds $A, B, C, D : K \to \mathbb{Q}$ bound event *cardinalities* (`(event k).card ≤ A k`), and the strict condition compares against `(sample.card : ℚ)`.
  - [`image_subset_ratio`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Counting.lean#L232-L243): computes the exact probability ratio $\binom{|allowed|}{|s|} / \binom{|\alpha|}{|s|}$ over the full symmetric group $\mathrm{Perm}(\alpha)$ (cardinality $|\alpha|!$).
- **Fidelity & Translation:**
  The Lean theorems operate directly on rational cardinalities and pigeonhole counting without requiring Mathlib probability space structures. Grok observes this: the interfaces use counts and compare to $|\mathrm{sample}|$, [`image_subset_ratio`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Counting.lean#L232-L243) is over the full symmetric group, and the four files leave the instantiation of $A, B, C, D$ with counting ratios completely disconnected.

#### E. Pointwise Distinct Lock Embeddings
- **Intended Claim ([`PROBABILITY_LEMMAS.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md#L18-L21)):**
  Locking $s$ distinct source vertices to $s$ distinct target positions leaves $(v - s)!$ extending permutations.
- **Formal Statements:**
  - [`card_prescribed_images`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/Counting.lean#L75-L100):
    `(vertices positions : ι ↪ α) : Fintype.card {σ : Perm α // ∀ i, σ (vertices i) = positions i} = (Fintype.card α - Fintype.card ι).factorial`.
- **Fidelity & Translation:**
  The parameter types are embeddings `ι ↪ α`, which enforces injectivity for both vertices and positions. Grok correctly notes: *"Injectivity of both embeddings is a type constraint... This is a pointwise prescription on $k = |\iota|$ distinct source points, sent to $k$ distinct image points."*

#### F. Seven-Point Theorem's Limited Scope
- **Intended Claim ([`STRUCTURE_24_25.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/STRUCTURE_24_25.md#L189-L217) Section 7):**
  Double-counting block absences on a 7-element set: if every point were omitted by exactly 2 triples, then $14 = 4 \cdot |\mathrm{blocks}|$, contradicting integrality of $|\mathrm{blocks}|$.
- **Formal Statements:**
  - [`absent_incidence_count`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/SevenPoint.lean#L18-L26): $\sum_{u \in W} |\{B : u \notin B\}| = \sum_{B \in \mathrm{blocks}} |W \setminus B|$.
  - [`exists_deletion_not_two`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math/SevenPoint.lean#L29-L54): for $|W| = 7$ and blocks of size 3, $\exists u \in W, |\{B : u \notin B\}| \ne 2$.
- **Fidelity & Translation:**
  The Lean module contains only this isolated double-counting contradiction. It contains no hypergraph, no degree-6 assumptions, no K6-4 classification, and no deletion operator. Grok highlights these exact limitations: the theorem does not give a direction ($\le 1$ or $\ge 3$), allows empty blocks, and does not connect to Property B or 5-edges.

---

### 3. Conclusion

1. **No Statement-Fidelity Mismatch:** The Lean declarations faithfully implement the exact local mathematical claims specified in [`FORMAL_SPEC.md`](file:///Users/rfy_naiveai/Desktop/aris4math/FORMAL_SPEC.md), [`PROBABILITY_LEMMAS.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/PROBABILITY_LEMMAS.md), and [`STRUCTURE_24_25.md`](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/STRUCTURE_24_25.md).
2. **No Blind Translation Errors:** Grok's translation in [`grok_lean_blind_translation_r4.md`](file:///Users/rfy_naiveai/Desktop/aris4math/context/reviews/research/grok_lean_blind_translation_r4.md) accurately reflects the Lean code's structure, semantics, and unproved obligations.
3. **Absence of Target Proof:** As both the formal files and Grok reflect, [`Target`](file:///Users/rfy_naiveai/Desktop/aris4math/formal/Aris4Math.lean#L37-L39) is defined but not proved within this four-file snapshot.


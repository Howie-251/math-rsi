The four files define `Target` and prove supporting lemmas. They do not contain a theorem of type `Target`.

Notation below: `|·|` is `Finset.card` or `Fintype.card`. For `x : Fin v`, the order is the usual order on `{0,1,…,v-1}`. `Perm α` is the set of bijections `α → α`. I did not execute Lean.

## 1. `Simple5Hypergraph`, `PropertyB`, `Target`

**Defined, not proved.**

`Simple5Hypergraph V` is a finite set `E` of finite subsets of `V` such that every `e ∈ E` has `|e| = 5`. There is no further axiom. The word “Simple” does not add an intersection condition, a declared ground set, or a ban on isolated vertices. Duplicate edges cannot occur because `E` is a finset. `V` itself need not be finite.

`PropertyB H` means: there exists `c : V → {true, false}` such that for every edge `e`,

\[
1 \le |\{x \in e : c(x) = \mathrm{true}\}| \le 4.
\]

Because every edge has size 5, this is exactly the existence of a 2-coloring with no monochromatic edge. The definition text quantifies over `H.edges` only; size 5 is the structure field.

`Target` is the proposition

\[
\forall\, V\ \text{finite},\ \forall\, H : \mathrm{Simple5Hypergraph}\, V,\quad |E(H)| \le 32 \Rightarrow \mathrm{PropertyB}\, H.
\]

It is universe-polymorphic in the universe of `V`. It is a definition of a `Prop`. No declaration in these four files has type `Target` or mentions `Target`.

The same file proves five general lemmas that do not mention hypergraphs, colorings, or 32:

- If `bad ⊆ ⋃_{k ∈ K₀} event(k)`, then `|bad| ≤ ∑_{k ∈ K₀} |event(k)|`.
- If in addition `|event(k)| ≤ A(k)`, `|event(k)| ≤ B(k)`, and `|event(k)| ≤ C(k) - D(k)` for every `k ∈ K₀`, and

\[
\sum_{k \in K_0} \min\bigl(A(k),\min(B(k), C(k)-D(k))\bigr) < |\mathrm{sample}|,
\]

then some element of `sample` lies outside `bad`. Events need not be subsets of `sample`, and `bad` need not be a subset of `sample`. The proof is the pigeonhole `|bad| < |sample|`. The outcome is outside `bad`, not necessarily outside every `event(k)`.

- If `C, D ⊆ U` are disjoint, weights on `U` are `≥ 0`, and `d ≤ ∑_{p ∈ D} w(p)`, then `∑_{p ∈ C} w(p) ≤ (∑_{p ∈ U} w(p)) - d`.
- For rationals `L, C` and `d ≥ 0`,

\[
\min(L,C) - \min(L, C-d) = \max\bigl(0,\ d - \max(0, C-L)\bigr).
\]

This identity is not used by any other declaration in the four files.

- A combined interface: if `bad` is covered by the `event(k)`, each `|event(k)|` is `≤ A(k)`, `≤ B(k)`, and `≤ ∑_{p ∈ C_k} w_k(p)`, the sets `C_k, D_k ⊆ U_k` are disjoint, weights are nonnegative on `U_k`, and `D(k) ≤ ∑_{p ∈ D_k} w_k(p)`, and

\[
\sum_k \min\Bigl(A(k),\min\bigl(B(k),\textstyle\sum_{p \in U_k} w_k(p) - D(k)\bigr)\Bigr) < |\mathrm{sample}|,
\]

then some element of `sample` lies outside `bad`. The numeric strict inequality, the weights, and the two set-bounds are hypotheses. Nothing in these files instantiates them.

## 2. The greedy algorithm and the three named statements

Vertex domain throughout `Greedy.lean` is `Fin v`, not an arbitrary finite type.

**Algorithm.** Fix a finite edge family `E` on `Fin v`. Set `Blue(0) = ∅`. For `t = 0, …, v-1`, let `x` be the vertex with value `t`, and let `Blue(t)` be the set so far. Insert `x` if and only if `FlipWitness` holds: some `A ∈ E` has `x ∈ A`, `y ≤ x` for every `y ∈ A` (so `x = max A`), and `A ∩ Blue(t) = ∅`. Otherwise leave the set unchanged. For times `≥ v` the set is constant. Final blue set: `Blue_E(v)`.

Every vertex that becomes blue does so at its own time, because of a witness edge present then. `Blue_E(t)` contains only vertices `< t`. The blue set only grows.

**Proved auxiliary facts used later.**

- Every nonempty `e ∈ E` meets `Blue_E(v)`. If not, `x = max e` would have been a witness when it was processed.
- `CriticalPair A B x` means: `A ≠ B`, `x ∈ A ∩ B`, `x = max A`, `x = min B`, and `A ∩ B = {x}`.
- If `|B| ≥ 2` and `B ⊆ Blue_E(v)`, then some `A ∈ E` and some `x` satisfy `CriticalPair A B x`. Here `B` is not required to be an edge. The proof takes `x = min B`, takes a witness edge `A` for `x` having been flipped, and checks the intersection. The “witness edge was all non-blue at time `x`” component is not used beyond guaranteeing that such an `A` exists.
- `Failure E` means some `e ∈ E` is disjoint from `Blue_E(v)` or contained in `Blue_E(v)`.

**`uniform_failure_covered`.** Assume every member of `E` has size `n ≥ 2`, and assume `Failure E`. Then there exist `A, B ∈ E` and a vertex `x` with `CriticalPair A B x`.

The all-non-blue disjunct of `Failure` contradicts the nonempty-edge fact above, so that branch produces no pair. The all-blue disjunct, applied to that failing edge `B` (which has size `n ≥ 2`), produces `A` and `x`. So `B` in the conclusion is a monochromatic blue edge, and `A` is a flip-witness edge for `x = min B`. The stated `CriticalPair` predicate does not retain “`B` is blue”.

`Failure` is not a critical-pair hypothesis. The pair is derived. No smuggling. The `n = 5` case is included; the statement is for every `n ≥ 2`.

**Permutation direction.** For `σ ∈ Perm(Fin v)`,

\[
E^\sigma = \{\,\sigma(e) : e \in E\,\}, \qquad \sigma(e) = \{\sigma(y) : y \in e\}.
\]

`FailureAt E σ` means `Failure(E^σ)`. `CriticalAt E σ k` means there exist distinct `A, B ∈ E` such that `CriticalPair` holds for `σ(A)`, `σ(B)`, and `k`.

So `σ` is applied to vertices first, and the greedy scan then runs in increasing numeric order on the image hypergraph. Equivalently, original vertex `x` is considered at time `σ(x)`. All linear orders arise by ranging over all permutations. Uniformity `n` is preserved. Because `σ` is bijective, distinct edges stay distinct.

**`failure_event_cover`.** Assume `E` is `n`-uniform with `n ≥ 2`. Let `sample` be any finite set of permutations of `Fin v`. Define

\[
\mathrm{bad}(E,\mathrm{sample}) = \{\sigma \in \mathrm{sample} : \mathrm{FailureAt}\, E\, \sigma\},
\]

\[
\mathrm{crit}(E,\mathrm{sample},k) = \{\sigma \in \mathrm{sample} : \mathrm{CriticalAt}\, E\, \sigma\, k\}.
\]

The theorem proved is the inclusion

\[
\mathrm{bad}(E,\mathrm{sample}) \subseteq \bigcup_{k \in \mathrm{Fin}\, v} \mathrm{crit}(E,\mathrm{sample},k).
\]

The union runs over every vertex of `Fin v`, not over a subset. Both sides are filtered to `sample`; `sample` need not be all of `Perm(Fin v)`. The hypotheses are only uniformity and `n ≥ 2`. The inclusion is derived from “failure implies some critical index”. It is not a premise.

It is one inclusion. `CriticalAt` does not retain that an edge is blue, and these files do not prove `CriticalAt ⇒ FailureAt`.

That converse is false already for 5-uniform data. Let `v = 9`, `σ = id`, and

\[
E = \bigl\{\{0,1,2,3,4\},\, \{4,5,6,7,8\}\bigr\}.
\]

Both edges have size 5. The only vertices that can ever flip are the two maxima, 4 and 8. At time 4 the blue set is still empty, so 4 flips. At time 8 the edge `{4,5,6,7,8}` already contains blue vertex 4, so 8 stays non-blue. Final blue set `{4}`. Each edge meets that set and also meets its complement, so `FailureAt` is false. But the two image edges form a `CriticalPair` at 4, so `CriticalAt` is true. Thus a covering event can contain a successful permutation. The proved inclusion is still valid; it bounds a superset of the failing set.

**`propertyB_of_successful_permutation`.** Assume `H` is a `Simple5Hypergraph` on `Fin v`, and assume `¬ FailureAt(E(H), σ)`. Then `PropertyB H`.

The coloring is built, not assumed: let `Blue` be the final blue set of `E(H)^σ`, and set

\[
c(x) = \mathrm{true} \iff \sigma(x) \notin \mathrm{Blue}.
\]

For an original edge `e`, success forbids `σ(e) ⊆ Blue`, so some vertex of `e` has color true. The general nonempty-edge fact gives a vertex of `σ(e)` in `Blue`, so some vertex `b ∈ e` has color false. The true vertices of `e` then lie in `e \ {b}`, and `|e| = 5` gives count `≤ 4`. Together with the lower bound `≥ 1`, this is `PropertyB`.

The hypothesis is algorithmic non-failure for one given `σ`. It is not the statement `PropertyB H`. The implication is only “this `σ` succeeds ⇒ `PropertyB`”. Existence of such a `σ` is not proved. The edge-count hypothesis `|E| ≤ 32` is not used. The vertex type is `Fin v`, not an arbitrary finite `V`.

## 3. The three counting statements

Ambient data: `α` is finite with decidable equality. All counts are cardinalities of sets of permutations of the whole of `α`. The sample space of the ratio is the full symmetric group, whose cardinality is `|α|!`. There is no hypergraph in this file, and this file does not import the others.

Supporting facts the three statements expand into:

- Permutations fixing a finset `s` pointwise: `(|α| - |s|)!`.
- Permutations agreeing with one fixed permutation on `s`: the same count. Agreement is always possible because the reference map is bijective.
- Permutations preserving a set `s` setwise: `|s|! · (|α| - |s|)!`.
- If `|s| = |t|`, permutations with `σ(s) = t`: the same count. The set is empty when the cardinalities differ; the factorial formula is stated only under `|s| = |t|`.

**`card_prescribed_images`.** Let `ι` be finite, and let `vertices, positions : ι ↪ α` be injections. Then

\[
\bigl|\{\sigma \in \mathrm{Perm}\,\alpha : \forall i,\ \sigma(\mathrm{vertices}(i)) = \mathrm{positions}(i)\}\bigr| = \bigl(|\alpha| - |\iota|\bigr)!.
\]

This is a pointwise prescription on `k = |ι|` distinct source points, sent to `k` distinct image points. Injectivity of both embeddings is a type constraint, so `k ≤ |α|` whenever the statement applies. The count depends on `α` and `ι` only through those two cardinalities. It is not multiplied by `k!`: the bijection between the two `k`-sets is fixed, and only the complement is free.

Boundaries: `k = 0` gives `|α|!` (no constraint). `k = |α|` gives `0! = 1`. If `k > |α|`, no embedding `ι ↪ α` exists, so the statement has no instance.

**`card_image_subset`.** For finsets `s, allowed` of `α`,

\[
\bigl|\{\sigma : \sigma(s) \subseteq \mathrm{allowed}\}\bigr| = \binom{|\mathrm{allowed}|}{|s|} \cdot |s|! \cdot \bigl(|\alpha| - |s|\bigr)!.
\]

No hypothesis `|s| ≤ |allowed|` is required. If `|s| > |allowed|`, the binomial coefficient is 0 and the set is empty. If `s = ∅`, both sides equal `|α|!`. The proof partitions by the exact image `t = σ(s)`, ranging over the `|s|`-subsets of `allowed`, and applies the exact-image count to each. Each `σ` has one image, so there is no overcount.

**`image_subset_ratio`.**

\[
\frac{|\{\sigma : \sigma(s) \subseteq \mathrm{allowed}\}|}{|\mathrm{Perm}\,\alpha|} = \frac{\binom{|\mathrm{allowed}|}{|s|}}{\binom{|\alpha|}{|s|}}.
\]

The denominator on the left is `|α|!`. The identity `binom(|α|,|s|) · |s|! · (|α|-|s|)! = |α|!` is applied under `|s| ≤ |α|`, which holds for any finset of `α`. The cancelled factor `|s|! · (|α|-|s|)!` is never zero. When `|s| > |allowed|`, both sides are 0. The binomial denominator is never zero for a finset `s`.

This ratio is over the full symmetric group. It does not, by itself, bound a proportion inside a proper subset of permutations. `Greedy`’s `sample` is an arbitrary finset of permutations, and neither file instantiates one statement with the other.

## 4. `SevenPoint.exists_deletion_not_two`

`absent_incidence_count` is the general double count, with no size hypotheses: for any finite `W` and any finite family `blocks` of finite subsets of `α`,

\[
\sum_{u \in W} |\{B \in \mathrm{blocks} : u \notin B\}| = \sum_{B \in \mathrm{blocks}} |W \setminus B|.
\]

**`exists_deletion_not_two`.** Assume `|W| = 7`, every block is a subset of `W`, and every block has size 3. Then some `u ∈ W` satisfies

\[
|\{B \in \mathrm{blocks} : u \notin B\}| \ne 2.
\]

The family is an arbitrary set of 3-element subsets of a fixed 7-element set. No balance, intersection, covering, or nonemptiness assumption is present. Duplicate blocks are excluded because the family is a finset.

The proof shows that “every point of `W` is omitted by exactly two blocks” would give `14 = 4 · |blocks|`, which is impossible in the naturals. The argument is by contradiction and does not select a specific point.

What this guarantees is only that inequality. It does not give a direction: the omission count can be strictly less than 2 for every point. The empty family gives count 0 for every `u`. A single triple gives counts in `{0,1}`. It also does not forbid some other point from having count exactly 2. Two disjoint triples on a 7-set omit the seventh point twice and omit each of the other six points once.

There is no deletion operator in the file. The count is the number of blocks avoiding `u`, not the number containing `u`. The file does not mention `PropertyB`, 5-uniform edges, permutations, or `Target`. The import of `Aris4Math` is unused.

## 5. Is `Target` proved, and what is still required?

These files do not prove `Target`. The constant 32 occurs only inside the definition of `Target`. No proved lemma assumes `|E| ≤ 32`.

The interfaces that are actually proved connect only this far:

- For a 5-uniform family on `Fin v` and any finite sample of permutations, `failure_event_cover` is the cover hypothesis required by the two existence engines, with positions equal to all of `Fin v` and with events equal to the critical-permutation sets.
- If a producer proves the engines’ numeric hypothesis for that sample, the engine returns a permutation in the sample outside `bad`, hence a `σ` with `¬ FailureAt`.
- `propertyB_of_successful_permutation` turns one such `σ` into `PropertyB`, for vertex type `Fin v` only.

Still unproved from the exposed interfaces:

1. Choose the sample and prove the strict numeric inequality. For the plain engine that means functions `A, B, C, D` with `|crit(k)|` bounded by `A(k)`, `B(k)`, and `C(k)-D(k)`, and the sum of the minima strictly less than `|sample|`. For the weighted engine it means, at each `k`, sets `U_k`, contributing `C_k`, deleted `D_k`, nonnegative weights, disjointness, `|crit(k)| ≤ ∑_{C_k} w_k`, a lower bound `D(k)` on the deleted weight, and the same strict sum. None of these objects are defined.
2. Put `|E| ≤ 32` into that inequality. The counting lemmas are not applied to `CriticalAt`. A critical event is an existential quantification over distinct edge pairs; bounding it requires a further union over pairs and a specialization of the pointwise or image-subset counts to the constraints `max σ(A) = min σ(B) = k` and `σ(A) ∩ σ(B) = {k}`. That specialization is not present.
3. If the sample is a proper subset of `Perm(Fin v)`, `image_subset_ratio` does not apply unchanged. If the sample is the full symmetric group, that choice is still not written, though `|Perm(Fin v)| = v!` is the standard fact used inside the counting file.
4. Transport an arbitrary finite vertex type `V` to `Fin |V|`, including invariance of `PropertyB` under bijection. Every greedy and permutation statement is on `Fin v`.
5. `minimum_decrease` is not part of either existence proof. A producer who wants that decrease formula has to apply it.
6. `exists_deletion_not_two` supplies only “some point of a 7-set is omitted by a number of triples other than 2”. A producer who uses it must still build `W` and the triple family from the hypergraph and prove that this undirected inequality implies the needed weight or deletion bound. The files contain no such construction.

The proved chain is conditional existence machinery plus a translation from greedy success on `Fin v` into `PropertyB`. The numeric discharge of that machinery, the constant 32, and the passage to an arbitrary finite vertex type are producer obligations.

This is a reading of the four source files only, not a certificate that the proofs compile or that no other error exists.The four files do not contain a theorem of type `Target`. They define that statement, prove a greedy coloring implication under an undischarged success hypothesis, prove a one-sided cover of failures by a static critical-pair event, and prove general counting lemmas that are never applied to those events.

## 1. `Simple5Hypergraph`, `PropertyB`, `Target`

`Simple5Hypergraph V` is a definition. It is a finite set `E` of finite subsets of `V` such that every member has cardinality 5. Edges are sets, so there are no repeated vertices inside an edge and no duplicate edges. There is no intersection condition, no finiteness requirement on `V`, and no requirement that every vertex lies in an edge.

`PropertyB H` is a definition. It asserts that there exists a map `c : V → {false, true}` such that for every edge `e`,
\[
1 \le |\{x\in e:c(x)=\mathrm{true}\}| \le 4.
\]
For an edge of size 5, that is exactly the condition that `e` is not monochromatic. The definition does not require `V` to be finite.

`Target` is also a definition, not a theorem. As a universe-polymorphic proposition it says: for every finite type `V` and every simple 5-uniform hypergraph `H` on `V`, if `|E(H)| ≤ 32`, then `PropertyB H`. The literal `32` occurs only here. Nothing instantiates or proves `Target`.

## 2. The greedy algorithm and the three named theorems

The ground set in `Greedy.lean` is exactly `Fin v = {0,1,…,v-1}` with the usual numeric order. For a finite family `E` of subsets of `Fin v`, the blue set is built as follows.

- `blue₀ = ∅`.
- At step `t = 0,…,v-1`, let `x` be the vertex `t`. If there exists `A ∈ E` with `x ∈ A`, `max A = x`, and `A ∩ blue_t = ∅`, put `blue_{t+1} = blue_t ∪ {x}`. Otherwise leave the set unchanged.
- For every later time the set stays equal to `blue_v`.

Membership is deterministic: several witness edges only affect whether the current vertex is inserted. A vertex can enter only at its own step, and the blue set only grows. The proved structural facts are:

- Every nonempty edge meets `blue_v`. So the algorithm never leaves a nonempty all-red edge.
- If `x ∈ blue_v`, then at time `x`, some edge `A ∋ x` had maximum `x` and was disjoint from the blue set then.
- Consequently, if every edge is nonempty, failure is exactly the existence of an all-blue edge. The all-red disjunct in the definition is impossible in that case.

`Failure E` means some edge of `E` is disjoint from `blue_v` or contained in `blue_v`.

For `σ ∈ Sym(Fin v)`, the ordered hypergraph is the pushforward
\[
E_σ = \{\sigma(e):e\in E\},\qquad \sigma(e)=\{\sigma(x):x\in e\}.
\]
The scan order stays `0<1<⋯<v-1` on this image. Equivalently, the original vertices are scanned in the order `σ⁻¹(0),…,σ⁻¹(v-1)`. The files use the pushforward formulation.

`CriticalPair A B x` means `A ≠ B`, `x ∈ A ∩ B`, `max A = x`, `min B = x`, and `A ∩ B = {x}`. Thus `A` lies entirely on the low side of `x` and `B` entirely on the high side. The structure itself does not require `A` or `B` to be edges.

`CriticalAt E σ k` means there exist distinct `A,B ∈ E` such that `CriticalPair` holds for `σ(A)`, `σ(B)`, and `k`. This predicate does not mention `blueAfter`.

**`uniform_failure_covered`.** Assume `n ≥ 2`, every member of `E` has size `n`, and `Failure E`. Then there exist `A,B ∈ E` and a vertex `x` with `CriticalPair A B x`. The proof deletes the all-red case by the lemma above, takes an all-blue edge `B`, sets `x = min B`, and takes `A` to be a flip witness for `x`. The orientation is fixed: the all-blue edge is the high-side set `B`, and `A` is the low-side witness. From the witness condition, every vertex of `A` other than `x` stays permanently red. Assumptions `n ≥ 2` and uniformity are used to obtain `|B| ≥ 2`, hence `A ≠ B`. No bound on `|E|` enters.

**`failure_event_cover`.** For the same `n ≥ 2` and `n`-uniform `E`, and for an arbitrary finite sample `S ⊆ Sym(Fin v)`,
\[
\{\sigma\in S:\mathrm{Failure}(E_σ)\}
\subseteq
\bigcup_{k\in\mathrm{Fin}\,v}
\{\sigma\in S:\mathrm{CriticalAt}(E,\sigma,k)\}.
\]
The inclusion is one-sided. A permutation can satisfy `CriticalAt` at some `k` without the greedy coloring of `E_σ` failing, because `CriticalAt` is only an existential order condition on a pair of images. Both sides are intersected with the given sample. The sample need not be the full symmetric group, and the vertex index runs through all of `Fin v`, including isolated vertices.

**`propertyB_of_successful_permutation`.** Assume `H` is a simple 5-uniform hypergraph on `Fin v`, and assume `¬ Failure(H_σ)` for a given permutation `σ`. Then `PropertyB H`. The coloring is constructed, not assumed: let `blue = blue_v(H_σ)` and set
\[
c(x)=\mathrm{true}\iff \sigma(x)\notin blue.
\]
For each original edge `e`, the image `σ(e)` has size 5. The success hypothesis supplies a point of `σ(e)` outside `blue`, giving at least one `true`. The general no-all-red lemma supplies a point of `σ(e)` inside `blue`, so the `true` set omits at least that vertex and has size at most 4. The success hypothesis is strictly stronger than the conclusion: it says that this particular greedy run has no monochromatic image edge. It is not implied by `PropertyB` anywhere in these files, and no theorem produces a `σ` satisfying it.

For a 5-uniform family the hypotheses of the cover specialize with `n = 5`, but that specialization is not given as a separate theorem.

## 3. The counting statements

Throughout, `α` is a finite decidable type and permutations are elements of `Sym(α)`, whose cardinality is `|α|!`.

- The number of permutations fixing a finite set `s` pointwise is `(|α|-|s|)!`.
- For any reference permutation `ρ`, the number agreeing with `ρ` on `s` is also `(|α|-|s|)!`.
- **`card_prescribed_images`.** For a finite index type `ι` and embeddings `v,p : ι ↪ α`,
  \[
  |\{\sigma\in\mathrm{Sym}(\alpha):\forall i,\;\sigma(v_i)=p_i\}|
  =(|\alpha|-|\iota|)!.
  \]
  Injectivity of both embeddings is an assumption of the statement and is what makes the prescription a partial injection. The source points are `v(ι)` and the prescribed images are `p(ι)`; the two images may overlap. If `|ι|=0`, the count is `|α|!`. If `|ι|=|α|`, the count is `1`. An embedding forces `|ι| ≤ |α|`, so the subtraction does not saturate.

- If `|s|=|t|`, the number of permutations with exact image `σ(s)=t` is `|s|!(|α|-|s|)!`, and the number stabilizing `s` setwise is the same quantity.
- **`card_image_subset`.** For arbitrary finite `s,allowed ⊆ α`,
  \[
  |\{\sigma:\sigma(s)\subseteq allowed\}|
  =
  \binom{|allowed|}{|s|}\,|s|!\,(|\alpha|-|s|)!.
  \]
  Here `σ(s)` is the direct image. If `|s| > |allowed|`, both sides are 0. If `s=∅`, both sides equal `|α|!`, including the case `allowed=∅`. There is no hypothesis that `s ⊆ allowed`.
- **`image_subset_ratio`.** In `ℚ`, with the full symmetric group as sample space,
  \[
  \frac{|\{\sigma:\sigma(s)\subseteq allowed\}|}{|\mathrm{Sym}(\alpha)|}
  =
  \frac{\binom{|allowed|}{|s|}}{\binom{|\alpha|}{|s|}}.
  \]
  The denominator is nonzero because `|s| ≤ |α|`. This is a ratio over all permutations of `α`, not over a proper sample finset. These counting theorems are not applied to `CriticalAt`, to `badPermutations`, or to a hypergraph.

## 4. `SevenPoint.exists_deletion_not_two`

For an arbitrary decidable type, let `W` be a 7-element finite set and let `blocks` be any finite family of 3-element subsets of `W`. The theorem says there exists `u ∈ W` such that the number of blocks not containing `u` is different from 2.

The proof is double counting. The sum over `u ∈ W` of the number of blocks avoiding `u` equals the sum over blocks `B` of `|W\B|`. The constant value 2 would make the left side `14` and the right side `4|blocks|`, which is impossible.

The empty family is allowed: every absence count is 0. The theorem does not identify `u`, does not force the absence count to be at least 3 or at most 1, and does not constrain how many blocks contain `u`. It assumes nothing about pairwise intersections. It does not mention colorings, permutations, 5-edges, deletion weights, or `Target`. The companion identity `absent_incidence_count` is the same double count with no size hypotheses. `SevenPoint.lean` imports `Aris4Math` but does not use those declarations.

## 5. What is still required before `Target` can be produced

The interfaces do not assemble. A producer still has to supply all of the following.

- A transport from an arbitrary finite vertex type to `Fin v`, together with invariance of `PropertyB` under that transport. Every theorem that yields `PropertyB` is stated only for `Fin v`.
- Existence of one successful permutation: for each simple 5-uniform `H` on `Fin v` with at most 32 edges, some `σ` with `¬ Failure(H_σ)`. `propertyB_of_successful_permutation` then gives `PropertyB`.
- If that existence is derived from the cover, a sample `S` must be chosen and its cardinality identified. The natural choice is the full symmetric group, but the equality of that finset cardinality with `v!` is not recorded.
- `failure_event_cover` at `n=5` gives only `bad ⊆ ⋃_k critical_k`. The abstract lemma `card_event_cover_le` then gives `|bad| ≤ ∑_k |critical_k|`. One still needs bounds on those summands, and the strict inequality required by `exists_outside_bad_of_min_bounds`: the sum of the rational upper bounds must be strictly less than `|S|`. A non-strict bound does not meet the hypothesis.
- `CriticalAt` quantifies over distinct edge pairs. No union bound over pairs `A,B ∈ E` is proved, and no theorem counts, for fixed `A,B,k`, the permutations whose images satisfy the low-side, high-side, and singleton-intersection conditions. `image_subset_ratio` and `card_prescribed_images` are applicable only after that event is encoded into an image restriction or a complete finite prescription. That encoding is not present.
- The arithmetic that turns those bounds into a number strictly less than the sample size when `|E| ≤ 32` is not present. The threshold 32 is not derived from the counting lemmas.
- `exists_outside_bad_of_weighted_deletion` additionally requires, position by position, a weight function, a contributing set, a deleted set, disjointness, nonnegativity, an upper bound of the event by the contributing weight, and a lower bound `D` on the deleted weight. None of these data are defined for edges or permutations. The proved identity `minimum_decrease` is not used by any other declaration.
- `exists_deletion_not_two` can be used only after a producer defines a 7-set and a family of triples and connects a vertex whose absence count is not 2 to one of those weights or permutation events. The files contain no such connection.

The general existence lemmas do what they say: if a bad set is covered by events and the sum of the supplied minima is strictly smaller than the sample, then some sample point lies outside the bad set. They do not know what a hypergraph, a critical pair, or the number 32 is. No proof of `Target` is implicit in the definitions.

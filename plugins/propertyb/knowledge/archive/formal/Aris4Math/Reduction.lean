import Aris4Math
import Aris4Math.Structure
import Mathlib.Data.Fintype.EquivFin
import Mathlib.Data.Finset.Powerset

/-!
# Vertex relabeling and merging for the minimal-counterexample reduction

The hypergraphs and Property B predicate are those of the original target.
An edgewise-injective vertex map preserves five-uniformity, never increases
the number of distinct edges, and pulls every legal coloring back.
-/

namespace Aris4Math.Reduction

universe u w

variable {V : Type u} {W : Type w}

/-- Map vertices and remove duplicate image edges. Edgewise injectivity is
exactly the condition needed to preserve five vertices in each edge. -/
noncomputable def pushforward (H : Simple5Hypergraph V) (f : V → W)
    (edge_injective : ∀ e ∈ H.edges, Set.InjOn f (e : Set V)) :
    Simple5Hypergraph W := by
  classical
  refine ⟨H.edges.image (fun e => e.image f), ?_⟩
  intro e he
  obtain ⟨a, ha, rfl⟩ := Finset.mem_image.mp he
  rw [Finset.card_image_of_injOn (edge_injective a ha)]
  exact H.five_uniform a ha

/-- Removing duplicate image edges cannot increase the edge count. -/
theorem pushforward_edge_count_le (H : Simple5Hypergraph V) (f : V → W)
    (edge_injective : ∀ e ∈ H.edges, Set.InjOn f (e : Set V)) :
    (pushforward H f edge_injective).edges.card ≤ H.edges.card := by
  classical
  exact Finset.card_image_le

/-- A map injective on one edge preserves its red-vertex count under pullback. -/
theorem red_count_image [DecidableEq W] (e : Finset V) (f : V → W)
    (hinj : Set.InjOn f (e : Set V)) (c : W → Bool) :
    ((e.image f).filter (fun y => c y = true)).card =
      (e.filter (fun x => c (f x) = true)).card := by
  rw [Finset.filter_image]
  apply Finset.card_image_of_injOn
  intro a ha b hb hab
  exact hinj (Finset.mem_filter.mp ha).1 (Finset.mem_filter.mp hb).1 hab

/-- Any legal coloring of an edgewise-injective image pulls back to the
original hypergraph. This remains valid when image edges were deduplicated. -/
theorem propertyB_pullback (H : Simple5Hypergraph V) (f : V → W)
    (edge_injective : ∀ e ∈ H.edges, Set.InjOn f (e : Set V))
    (h : PropertyB (pushforward H f edge_injective)) : PropertyB H := by
  classical
  obtain ⟨c, hc⟩ := h
  refine ⟨fun x => c (f x), ?_⟩
  intro e he
  have himage : e.image f ∈ (pushforward H f edge_injective).edges :=
    Finset.mem_image.mpr ⟨e, he, rfl⟩
  have hcounts := hc (e.image f) himage
  rw [red_count_image e f (edge_injective e he) c] at hcounts
  exact hcounts

/-- Relabel the vertex type along any equivalence. -/
noncomputable def relabel (H : Simple5Hypergraph V) (e : V ≃ W) :
    Simple5Hypergraph W :=
  pushforward H e (fun _ _ => e.injective.injOn)

/-- A bijective vertex relabeling preserves the number of distinct edges. -/
theorem relabel_edge_count (H : Simple5Hypergraph V) (e : V ≃ W) :
    (relabel H e).edges.card = H.edges.card := by
  classical
  apply Finset.card_image_of_injective
  intro a b hab
  exact Finset.image_injective e.injective hab

/-- Property B is invariant under arbitrary vertex-type equivalences. -/
theorem propertyB_relabel_iff (H : Simple5Hypergraph V) (e : V ≃ W) :
    PropertyB (relabel H e) ↔ PropertyB H := by
  classical
  constructor
  · exact propertyB_pullback H e (fun _ _ => e.injective.injOn)
  · rintro ⟨c, hc⟩
    refine ⟨fun y => c (e.symm y), ?_⟩
    intro a ha
    obtain ⟨b, hb, rfl⟩ := Finset.mem_image.mp ha
    have hr := red_count_image b e e.injective.injOn (fun y => c (e.symm y))
    simp only [Equiv.symm_apply_apply] at hr
    rw [hr]
    exact hc b hb

/-- Canonical finite-label representative; isolated vertices are retained. -/
noncomputable def toFin [Fintype V] (H : Simple5Hypergraph V) :
    Simple5Hypergraph (Fin (Fintype.card V)) :=
  relabel H (Fintype.equivFin V)

theorem toFin_edge_count [Fintype V] (H : Simple5Hypergraph V) :
    (toFin H).edges.card = H.edges.card :=
  relabel_edge_count H (Fintype.equivFin V)

theorem propertyB_toFin_iff [Fintype V] (H : Simple5Hypergraph V) :
    PropertyB (toFin H) ↔ PropertyB H :=
  propertyB_relabel_iff H (Fintype.equivFin V)

/-- Identify y with x, with codomain the original vertex type minus y. -/
noncomputable def mergeVertex (x y : V) (hxy : x ≠ y) (z : V) :
    {z : V // z ≠ y} := by
  classical
  exact if hz : z = y then ⟨x, hxy⟩ else ⟨z, hz⟩

/-- If x,y occur together in no edge, this merge is injective on every edge. -/
theorem mergeVertex_edge_injective (H : Simple5Hypergraph V) (x y : V)
    (hxy : x ≠ y) (not_together : ∀ e ∈ H.edges, ¬(x ∈ e ∧ y ∈ e)) :
    ∀ e ∈ H.edges, Set.InjOn (mergeVertex x y hxy) (e : Set V) := by
  classical
  intro e he a ha b hb hab
  have hval := congrArg Subtype.val hab
  by_cases hay : a = y
  · subst a
    by_cases hby : b = y
    · exact hby.symm
    · have hxb : x = b := by simpa [mergeVertex, hby] using hval
      exact False.elim (not_together e he ⟨hxb ▸ hb, ha⟩)
  · by_cases hby : b = y
    · subst b
      have hax : a = x := by simpa [mergeVertex, hay] using hval
      exact False.elim (not_together e he ⟨hax ▸ ha, hb⟩)
    · simpa [mergeVertex, hay, hby] using hval

/-- The merged simple five-uniform hypergraph. Five-uniformity is proved by
`mergeVertex_edge_injective`, not supplied as a certificate assumption. -/
noncomputable def merge (H : Simple5Hypergraph V) (x y : V) (hxy : x ≠ y)
    (not_together : ∀ e ∈ H.edges, ¬(x ∈ e ∧ y ∈ e)) :
    Simple5Hypergraph {z : V // z ≠ y} :=
  pushforward H (mergeVertex x y hxy)
    (mergeVertex_edge_injective H x y hxy not_together)

theorem merge_edge_count_le (H : Simple5Hypergraph V) (x y : V) (hxy : x ≠ y)
    (not_together : ∀ e ∈ H.edges, ¬(x ∈ e ∧ y ∈ e)) :
    (merge H x y hxy not_together).edges.card ≤ H.edges.card :=
  pushforward_edge_count_le H (mergeVertex x y hxy)
    (mergeVertex_edge_injective H x y hxy not_together)

theorem propertyB_of_merge (H : Simple5Hypergraph V) (x y : V) (hxy : x ≠ y)
    (not_together : ∀ e ∈ H.edges, ¬(x ∈ e ∧ y ∈ e))
    (h : PropertyB (merge H x y hxy not_together)) : PropertyB H :=
  propertyB_pullback H (mergeVertex x y hxy)
    (mergeVertex_edge_injective H x y hxy not_together) h

/-- The merge deletes an actual vertex, so the finite vertex count drops. -/
theorem merge_vertex_count_lt [Fintype V] [DecidableEq V] (y : V) :
    Fintype.card {z : V // z ≠ y} < Fintype.card V :=
  Fintype.card_subtype_lt (x := y) (by simp)

/-- Every noncolorable hypergraph with an uncovered pair produces a genuinely
smaller noncolorable simple five-uniform hypergraph, without increasing edges. -/
theorem smaller_counterexample_of_uncovered_pair
    [Fintype V] [DecidableEq V] (H : Simple5Hypergraph V)
    (hnotB : ¬ PropertyB H) (x y : V) (hxy : x ≠ y)
    (not_together : ∀ e ∈ H.edges, ¬(x ∈ e ∧ y ∈ e)) :
    ∃ H' : Simple5Hypergraph (Fin (Fintype.card {z : V // z ≠ y})),
      H'.edges.card ≤ H.edges.card ∧ ¬ PropertyB H' ∧
      Fintype.card {z : V // z ≠ y} < Fintype.card V := by
  let H' := merge H x y hxy not_together
  refine ⟨toFin H', ?_, ?_, merge_vertex_count_lt y⟩
  · rw [toFin_edge_count]
    exact merge_edge_count_le H x y hxy not_together
  · intro h
    exact hnotB (propertyB_of_merge H x y hxy not_together
      ((propertyB_toFin_iff H').mp h))

/-- Establishing all finite-label cases is sufficient for the original
universe-polymorphic target, with no loss of isolated vertices or edge count. -/
theorem target_of_fin_cases
    (hfin : ∀ v : ℕ, ∀ H : Simple5Hypergraph (Fin v),
      H.edges.card ≤ 32 → PropertyB H) : Aris4Math.Target.{u} := by
  intro V _ H hsize
  apply (propertyB_toFin_iff H).mp
  apply hfin (Fintype.card V) (toFin H)
  simpa only [toFin_edge_count] using hsize

/-- Starting from any actual counterexample, choose the least possible number
of vertices among *all* counterexamples with at most 32 edges. -/
theorem exists_minimal_counterexample [Fintype V]
    (H : Simple5Hypergraph V) (hsize : H.edges.card ≤ 32)
    (hnotB : ¬ PropertyB H) :
    ∃ v : ℕ, ∃ K : Simple5Hypergraph (Fin v),
      K.edges.card ≤ 32 ∧ ¬ PropertyB K ∧
      (∀ w < v, ∀ L : Simple5Hypergraph (Fin w),
        L.edges.card ≤ 32 → PropertyB L) := by
  classical
  let P : ℕ → Prop := fun v => ∃ K : Simple5Hypergraph (Fin v),
    K.edges.card ≤ 32 ∧ ¬ PropertyB K
  have hex : ∃ v, P v := by
    refine ⟨Fintype.card V, toFin H, ?_, ?_⟩
    · simpa only [toFin_edge_count] using hsize
    · intro hp
      exact hnotB ((propertyB_toFin_iff H).mp hp)
  obtain ⟨K, hKsize, hKnotB⟩ := Nat.find_spec hex
  refine ⟨Nat.find hex, K, hKsize, hKnotB, ?_⟩
  intro w hw L hLsize
  by_contra hLnotB
  have hleast := Nat.find_min' hex (show P w from ⟨L, hLsize, hLnotB⟩)
  exact (not_le_of_gt hw) hleast

/-- The least-vertex counterexample covers every pair of different vertices.
The conclusion is the explicit formula defining `H.PairCovering` in Structure. -/
theorem minimal_counterexample_pair_covering {v : ℕ}
    (H : Simple5Hypergraph (Fin v)) (hsize : H.edges.card ≤ 32)
    (hnotB : ¬ PropertyB H)
    (minimal : ∀ w < v, ∀ K : Simple5Hypergraph (Fin w),
      K.edges.card ≤ 32 → PropertyB K) :
    ∀ x y : Fin v, x ≠ y → ∃ e ∈ H.edges, x ∈ e ∧ y ∈ e := by
  classical
  intro x y hxy
  by_contra hnone
  have not_together : ∀ e ∈ H.edges, ¬(x ∈ e ∧ y ∈ e) := by
    intro e he hboth
    exact hnone ⟨e, he, hboth⟩
  obtain ⟨K, hKsize, hKnotB, hless⟩ :=
    smaller_counterexample_of_uncovered_pair H hnotB x y hxy not_together
  have hless' : Fintype.card {z : Fin v // z ≠ y} < v := by simpa using hless
  exact hKnotB (minimal _ hless' K (hKsize.trans hsize))

/-- Every counterexample yields a pair-covering finite-label counterexample.
Pair coverage is a derived conclusion, not an added assumption on the target. -/
theorem exists_pair_covering_counterexample [Fintype V]
    (H : Simple5Hypergraph V) (hsize : H.edges.card ≤ 32)
    (hnotB : ¬ PropertyB H) :
    ∃ v : ℕ, ∃ K : Simple5Hypergraph (Fin v),
      K.edges.card ≤ 32 ∧ ¬ PropertyB K ∧
      (∀ x y : Fin v, x ≠ y → ∃ e ∈ K.edges, x ∈ e ∧ y ∈ e) := by
  obtain ⟨v, K, hKsize, hKnotB, hminimal⟩ :=
    exists_minimal_counterexample H hsize hnotB
  exact ⟨v, K, hKsize, hKnotB,
    minimal_counterexample_pair_covering K hKsize hKnotB hminimal⟩

/-- A usable reduction of the original target to pair-covering cases.
Further vertex bounds can restrict this case theorem without altering T. -/
theorem target_of_pair_covering_cases
    (hpair : ∀ v : ℕ, ∀ H : Simple5Hypergraph (Fin v),
      H.edges.card ≤ 32 →
      (∀ x y : Fin v, x ≠ y → ∃ e ∈ H.edges, x ∈ e ∧ y ∈ e) →
      PropertyB H) : Aris4Math.Target.{u} := by
  classical
  intro V _ H hsize
  by_contra hnotB
  obtain ⟨v, K, hKsize, hKnotB, hKpair⟩ :=
    exists_pair_covering_counterexample H hsize hnotB
  exact hKnotB (hpair v K hKsize hKpair)

/-- Deleting constraints preserves any legal coloring. -/
theorem propertyB_of_edges_subset (H K : Simple5Hypergraph V)
    (hsub : H.edges ⊆ K.edges) (hK : PropertyB K) : PropertyB H := by
  obtain ⟨c, hc⟩ := hK
  exact ⟨c, fun e he => hc e (hsub he)⟩

/-- On at least eight vertices, there are enough distinct five-sets to add
edges up to exactly 32 on the same vertex set. -/
theorem exists_extension_32 {v : ℕ} (hv : 8 ≤ v)
    (H : Simple5Hypergraph (Fin v)) (hsize : H.edges.card ≤ 32) :
    ∃ K : Simple5Hypergraph (Fin v), H.edges ⊆ K.edges ∧ K.edges.card = 32 := by
  classical
  let allEdges := (Finset.univ : Finset (Fin v)).powersetCard 5
  have hsub : H.edges ⊆ allEdges := by
    intro e he
    exact Finset.mem_powersetCard.mpr ⟨Finset.subset_univ e, H.five_uniform e he⟩
  have hcapacity : 32 ≤ allEdges.card := by
    have hchoose := Nat.choose_le_choose 5 hv
    have hsmall : Nat.choose 8 5 = 56 := by decide
    simp only [allEdges, Finset.card_powersetCard, Finset.card_univ, Fintype.card_fin]
    omega
  obtain ⟨edges, hHedges, hedgesAll, hcard⟩ :=
    Finset.exists_subsuperset_card_eq hsub hsize hcapacity
  let K : Simple5Hypergraph (Fin v) :=
    ⟨edges, fun e he => (Finset.mem_powersetCard.mp (hedgesAll he)).2⟩
  exact ⟨K, hHedges, hcard⟩

/-- Same-vertex padding preserves both noncolorability and pair coverage. -/
theorem exists_pair_covering_extension_32 {v : ℕ} (hv : 8 ≤ v)
    (H : Simple5Hypergraph (Fin v)) (hsize : H.edges.card ≤ 32)
    (hnotB : ¬ PropertyB H)
    (hpair : ∀ x y : Fin v, x ≠ y → ∃ e ∈ H.edges, x ∈ e ∧ y ∈ e) :
    ∃ K : Simple5Hypergraph (Fin v), K.edges.card = 32 ∧ ¬ PropertyB K ∧
      (∀ x y : Fin v, x ≠ y → ∃ e ∈ K.edges, x ∈ e ∧ y ∈ e) := by
  obtain ⟨K, hsub, hcard⟩ := exists_extension_32 hv H hsize
  refine ⟨K, hcard, ?_, ?_⟩
  · intro hK
    exact hnotB (propertyB_of_edges_subset H K hsub hK)
  · intro x y hxy
    obtain ⟨e, he, hboth⟩ := hpair x y hxy
    exact ⟨e, hsub he, hboth⟩

/-- The small-vertex part of R4: split vertices at position four. Both color
classes have at most four vertices, so every five-edge meets both colors. -/
theorem propertyB_of_vertices_le_eight {v : ℕ} (hv : v ≤ 8)
    (H : Simple5Hypergraph (Fin v)) : PropertyB H := by
  classical
  let c : Fin v → Bool := fun x => decide (x.val < 4)
  refine ⟨c, ?_⟩
  intro e he
  have hred : (e.filter (fun x => x.val < 4)).card ≤ 4 := by
    calc
      _ ≤ (Finset.range 4).card := Finset.card_le_card_of_injOn
        (fun x : Fin v => x.val)
        (by
          intro x hx
          exact Finset.mem_range.mpr (Finset.mem_filter.mp hx).2)
        (by intro x _ y _ hxy; exact Fin.ext hxy)
      _ = 4 := Finset.card_range 4
  have hblue : (e.filter (fun x => ¬ x.val < 4)).card ≤ 4 := by
    calc
      _ ≤ (Finset.range 4).card := Finset.card_le_card_of_injOn
        (fun x : Fin v => x.val - 4)
        (by
          intro x hx
          have hxge := (Finset.mem_filter.mp hx).2
          have hxlt := x.isLt
          apply Finset.mem_range.mpr
          change x.val - 4 < 4
          omega)
        (by
          intro x hx y hy hxy
          have hxge := (Finset.mem_filter.mp hx).2
          have hyge := (Finset.mem_filter.mp hy).2
          change x.val - 4 = y.val - 4 at hxy
          apply Fin.ext
          omega)
      _ = 4 := Finset.card_range 4
  have hpartition := Finset.filter_card_add_filter_neg_card_eq_card
    (s := e) (fun x : Fin v => x.val < 4)
  have hfive := H.five_uniform e he
  simp only [c, decide_eq_true_eq]
  omega

/-- The currently unconditional finite reduction: an arbitrary counterexample
would yield a 9–25 vertex pair-covering counterexample with exactly 32 edges.
The remaining improvement of the lower endpoint to 19 is a separate obligation. -/
theorem exists_finite_counterexample [Fintype V]
    (H : Simple5Hypergraph V) (hsize : H.edges.card ≤ 32)
    (hnotB : ¬ PropertyB H) :
    ∃ v : ℕ, 9 ≤ v ∧ v ≤ 25 ∧ ∃ K : Simple5Hypergraph (Fin v),
      K.edges.card = 32 ∧ ¬ PropertyB K ∧ K.PairCovering := by
  obtain ⟨v, K, hKsize, hKnotB, hKpair⟩ :=
    exists_pair_covering_counterexample H hsize hnotB
  have hcover : K.PairCovering := hKpair
  have hupper : v ≤ 25 := by
    simpa using K.card_le_twenty_five hcover hKsize
  have hlower : 9 ≤ v := by
    by_contra hsmall
    exact hKnotB (propertyB_of_vertices_le_eight (by omega) K)
  obtain ⟨L, hLsize, hLnotB, hLpair⟩ :=
    exists_pair_covering_extension_32 (by omega) K hKsize hKnotB hKpair
  exact ⟨v, hlower, hupper, L, hLsize, hLnotB, hLpair⟩

/-- The original target follows if these finite cases are proved. This theorem
is a proved reduction, not a claim that its finite-case premise is discharged. -/
theorem target_of_finite_cases
    (hcases : ∀ v : ℕ, 9 ≤ v → v ≤ 25 → ∀ H : Simple5Hypergraph (Fin v),
      H.edges.card = 32 → H.PairCovering → PropertyB H) : Aris4Math.Target.{u} := by
  classical
  intro V _ H hsize
  by_contra hnotB
  obtain ⟨v, hlower, hupper, K, hKsize, hKnotB, hKpair⟩ :=
    exists_finite_counterexample H hsize hnotB
  exact hKnotB (hcases v hlower hupper K hKsize hKpair)

/-- Assembly interface matching FORMAL_SPEC F. The 9–18 vertex theorem and the
19–25 vertex structural/probability theorem remain explicit separate inputs. -/
theorem target_of_nineteen_to_twenty_five
    (small : ∀ v : ℕ, 9 ≤ v → v ≤ 18 → ∀ H : Simple5Hypergraph (Fin v),
      H.edges.card ≤ 32 → PropertyB H)
    (finite : ∀ v : ℕ, 19 ≤ v → v ≤ 25 → ∀ H : Simple5Hypergraph (Fin v),
      H.edges.card = 32 → H.PairCovering → PropertyB H) : Aris4Math.Target.{u} := by
  apply target_of_finite_cases
  intro v hlower hupper H hsize hcover
  by_cases hv : v ≤ 18
  · exact small v hlower hv H (by omega)
  · exact finite v (by omega) hupper H hsize hcover

end Aris4Math.Reduction

#print axioms Aris4Math.Reduction.propertyB_pullback
#print axioms Aris4Math.Reduction.propertyB_relabel_iff
#print axioms Aris4Math.Reduction.propertyB_toFin_iff
#print axioms Aris4Math.Reduction.mergeVertex_edge_injective
#print axioms Aris4Math.Reduction.merge_edge_count_le
#print axioms Aris4Math.Reduction.propertyB_of_merge
#print axioms Aris4Math.Reduction.merge_vertex_count_lt
#print axioms Aris4Math.Reduction.smaller_counterexample_of_uncovered_pair
#print axioms Aris4Math.Reduction.target_of_fin_cases
#print axioms Aris4Math.Reduction.exists_minimal_counterexample
#print axioms Aris4Math.Reduction.minimal_counterexample_pair_covering
#print axioms Aris4Math.Reduction.exists_pair_covering_counterexample
#print axioms Aris4Math.Reduction.target_of_pair_covering_cases
#print axioms Aris4Math.Reduction.exists_extension_32
#print axioms Aris4Math.Reduction.exists_pair_covering_extension_32
#print axioms Aris4Math.Reduction.propertyB_of_vertices_le_eight
#print axioms Aris4Math.Reduction.exists_finite_counterexample
#print axioms Aris4Math.Reduction.target_of_finite_cases
#print axioms Aris4Math.Reduction.target_of_nineteen_to_twenty_five

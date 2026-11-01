import Aris4Math.Counting
import Aris4Math.Reduction
import Mathlib.Tactic.IntervalCases

/-!
# R4: all hypergraphs on at most eighteen vertices are colorable

A fixed set of red positions is pulled back along a uniformly chosen
permutation. The proof counts the monochromatic-edge events analytically,
using the general permutation fibre theorem, and applies the finite union
bound. Only the ten scalar inequalities for v = 9,...,18 are evaluated.
-/

namespace Aris4Math.SmallVertices

open scoped BigOperators

universe u

variable {V : Type u} [Fintype V] [DecidableEq V]

/-- Permutations placing every vertex of e in the specified color class. -/
noncomputable def monochromaticPermutations (e allowed : Finset V) :
    Finset (Equiv.Perm V) := by
  classical
  exact Finset.univ.filter (fun σ => e.map σ.toEmbedding ⊆ allowed)

/-- Exact event size, inherited from the general permutation-fibre proof. -/
theorem monochromaticPermutations_card (e allowed : Finset V) :
    (monochromaticPermutations e allowed).card =
      allowed.card.choose e.card *
        (e.card.factorial * (Fintype.card V - e.card).factorial) := by
  classical
  calc
    _ = Fintype.card {σ : Equiv.Perm V // e.map σ.toEmbedding ⊆ allowed} :=
      (Fintype.card_subtype _).symm
    _ = _ := Counting.card_image_subset e allowed

/-- A general balanced-coloring criterion before choosing any vertex count.
The right side is the full permutation sample size; the left side is the
analytic union bound for all monochromatic-edge events. -/
theorem propertyB_of_partition_count_bound (H : Simple5Hypergraph V)
    (red : Finset V)
    (strict : H.edges.card *
      ((red.card.choose 5 + (Fintype.card V - red.card).choose 5) *
        (Nat.factorial 5 * (Fintype.card V - 5).factorial)) <
      (Fintype.card V).factorial) : PropertyB H := by
  classical
  let event := fun e => monochromaticPermutations e red ∪
    monochromaticPermutations e redᶜ
  let bad := H.edges.biUnion event
  let C := (red.card.choose 5 + (Fintype.card V - red.card).choose 5) *
    (Nat.factorial 5 * (Fintype.card V - 5).factorial)
  have event_bound (e : Finset V) (he : e ∈ H.edges) : (event e).card ≤ C := by
    calc
      _ ≤ (monochromaticPermutations e red).card +
          (monochromaticPermutations e redᶜ).card := Finset.card_union_le _ _
      _ = C := by
        rw [monochromaticPermutations_card, monochromaticPermutations_card,
          H.five_uniform e he, Finset.card_compl]
        exact (Nat.add_mul _ _ _).symm
  have bad_bound : bad.card ≤ H.edges.card * C := by
    calc
      _ ≤ ∑ e ∈ H.edges, (event e).card := Finset.card_biUnion_le
      _ ≤ ∑ _e ∈ H.edges, C := Finset.sum_le_sum event_bound
      _ = H.edges.card * C := by simp
  have strict_sample : bad.card < (Finset.univ : Finset (Equiv.Perm V)).card := by
    rw [Finset.card_univ, Fintype.card_perm]
    exact lt_of_le_of_lt bad_bound strict
  obtain ⟨σ, _, hgood⟩ := Finset.exists_mem_notMem_of_card_lt_card strict_sample
  let c : V → Bool := fun x => decide (σ x ∈ red)
  refine ⟨c, ?_⟩
  intro e he
  have not_red : ¬ e.map σ.toEmbedding ⊆ red := by
    intro hmono
    apply hgood
    apply Finset.mem_biUnion.mpr
    refine ⟨e, he, Finset.mem_union_left _ ?_⟩
    exact Finset.mem_filter.mpr ⟨Finset.mem_univ σ, hmono⟩
  have not_blue : ¬ e.map σ.toEmbedding ⊆ redᶜ := by
    intro hmono
    apply hgood
    apply Finset.mem_biUnion.mpr
    refine ⟨e, he, Finset.mem_union_right _ ?_⟩
    exact Finset.mem_filter.mpr ⟨Finset.mem_univ σ, hmono⟩
  have red_witness : ∃ x ∈ e, σ x ∈ red := by
    by_contra hnone
    apply not_blue
    intro p hp
    obtain ⟨x, hx, rfl⟩ := Finset.mem_map.mp hp
    exact Finset.mem_compl.mpr (fun hr => hnone ⟨x, hx, hr⟩)
  have blue_witness : ∃ x ∈ e, σ x ∉ red := by
    by_contra hnone
    apply not_red
    intro p hp
    obtain ⟨x, hx, rfl⟩ := Finset.mem_map.mp hp
    by_contra hn
    exact hnone ⟨x, hx, hn⟩
  obtain ⟨r, hre, hrred⟩ := red_witness
  obtain ⟨b, hbe, hbblue⟩ := blue_witness
  have hrcolor : c r = true := by simp [c, hrred]
  have hbcolor : c b = false := by simp [c, hbblue]
  have lower : 1 ≤ (e.filter (fun x => c x = true)).card :=
    Finset.card_pos.mpr ⟨r, Finset.mem_filter.mpr ⟨hre, hrcolor⟩⟩
  have subset_erase : e.filter (fun x => c x = true) ⊆ e.erase b := by
    intro y hy
    obtain ⟨hye, hycolor⟩ := Finset.mem_filter.mp hy
    apply Finset.mem_erase.mpr
    refine ⟨?_, hye⟩
    intro hyb
    subst y
    simp [hbcolor] at hycolor
  have upper := Finset.card_le_card subset_erase
  rw [Finset.card_erase_of_mem hbe, H.five_uniform e he] at upper
  exact ⟨lower, upper⟩

/-- These are ten scalar inequalities, after multiplying the probability
bound by v!. No hypergraph or coloring is enumerated. -/
theorem balanced_count_strict (v : ℕ) (hlower : 9 ≤ v) (hupper : v ≤ 18) :
    32 * (((v / 2).choose 5 + (v - v / 2).choose 5) *
      (Nat.factorial 5 * (v - 5).factorial)) < v.factorial := by
  interval_cases v <;> decide

/-- R4 for every hypergraph in the entire 9–18 vertex range. -/
theorem propertyB_nine_to_eighteen {v : ℕ} (hlower : 9 ≤ v) (hupper : v ≤ 18)
    (H : Simple5Hypergraph (Fin v)) (hsize : H.edges.card ≤ 32) : PropertyB H := by
  classical
  have hhalf : v / 2 ≤ (Finset.univ : Finset (Fin v)).card := by
    simpa using Nat.div_le_self v 2
  obtain ⟨red, _, hred⟩ := Finset.exists_subset_card_eq hhalf
  apply propertyB_of_partition_count_bound H red
  simp only [Fintype.card_fin, hred]
  exact lt_of_le_of_lt (Nat.mul_le_mul_right _ hsize)
    (balanced_count_strict v hlower hupper)

/-- Every simple five-uniform hypergraph with at most 32 edges on at most
eighteen vertices has Property B. This has no pair-covering assumption. -/
theorem propertyB_of_vertices_le_eighteen {v : ℕ} (hv : v ≤ 18)
    (H : Simple5Hypergraph (Fin v)) (hsize : H.edges.card ≤ 32) : PropertyB H := by
  by_cases hsmall : v ≤ 8
  · exact Reduction.propertyB_of_vertices_le_eight hsmall H
  · exact propertyB_nine_to_eighteen (by omega) hv H hsize

omit [DecidableEq V] in
/-- Full FORMAL_SPEC finite counterexample reduction, now with lower bound 19.
Every step, including the small-vertex exclusion, is proved in imported modules. -/
theorem exists_nineteen_to_twenty_five_counterexample
    (H : Simple5Hypergraph V) (hsize : H.edges.card ≤ 32) (hnotB : ¬ PropertyB H) :
    ∃ v : ℕ, 19 ≤ v ∧ v ≤ 25 ∧ ∃ K : Simple5Hypergraph (Fin v),
      K.edges.card = 32 ∧ ¬ PropertyB K ∧ K.PairCovering := by
  obtain ⟨v, _, hupper, K, hKsize, hKnotB, hKcover⟩ :=
    Reduction.exists_finite_counterexample H hsize hnotB
  have hlower : 19 ≤ v := by
    by_contra hn
    exact hKnotB (propertyB_of_vertices_le_eighteen (by omega) K (by omega))
  exact ⟨v, hlower, hupper, K, hKsize, hKnotB, hKcover⟩

/-- Only the seven 19–25 vertex cases remain as input to the original target.
This is a reduction interface, not a declaration that those cases are proved. -/
theorem target_of_finite_goal
    (finite : ∀ v : ℕ, 19 ≤ v → v ≤ 25 → ∀ H : Simple5Hypergraph (Fin v),
      H.edges.card = 32 → H.PairCovering → PropertyB H) : Aris4Math.Target.{u} := by
  apply Reduction.target_of_nineteen_to_twenty_five
  · exact fun _ hlower hupper H hsize => propertyB_nine_to_eighteen hlower hupper H hsize
  · exact finite

/-- F as a proposition, with exactly the vertex, edge and pair-covering
conditions in FORMAL_SPEC. This definition is not a proof of those cases. -/
def FiniteGoal : Prop :=
  ∀ v : ℕ, 19 ≤ v → v ≤ 25 → ∀ H : Simple5Hypergraph (Fin v),
    H.edges.card = 32 → H.PairCovering → PropertyB H

/-- The formal equivalence T ↔ F, including arbitrary universe levels in T.
The forward direction lifts finite labels into the chosen universe; the
reverse direction uses the complete proved counterexample reduction. -/
theorem target_iff_finite_goal : Aris4Math.Target.{u} ↔ FiniteGoal := by
  constructor
  · intro htarget v _ _ H hsize _
    let e : Fin v ≃ ULift.{u} (Fin v) := Equiv.ulift.symm
    have hlift : (Reduction.relabel H e).edges.card ≤ 32 := by
      rw [Reduction.relabel_edge_count, hsize]
    have hPB := htarget (ULift.{u} (Fin v)) (Reduction.relabel H e) hlift
    exact (Reduction.propertyB_relabel_iff H e).mp hPB
  · exact target_of_finite_goal

end Aris4Math.SmallVertices

#print axioms Aris4Math.SmallVertices.monochromaticPermutations_card
#print axioms Aris4Math.SmallVertices.propertyB_of_partition_count_bound
#print axioms Aris4Math.SmallVertices.balanced_count_strict
#print axioms Aris4Math.SmallVertices.propertyB_nine_to_eighteen
#print axioms Aris4Math.SmallVertices.propertyB_of_vertices_le_eighteen
#print axioms Aris4Math.SmallVertices.exists_nineteen_to_twenty_five_counterexample
#print axioms Aris4Math.SmallVertices.target_of_finite_goal
#print axioms Aris4Math.SmallVertices.target_iff_finite_goal

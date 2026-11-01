import Aris4Math.ThirtyThree.Target
import Aris4Math.SmallVertices

/-!
# Reduction of the 33-edge target to 19–25 vertices

Only the generic merging, incidence and balanced-permutation counting results
are reused. None of the still-open 33-edge branches is assumed internally.
The final assembly theorem exposes those seven branches as its explicit premise.
-/

namespace Aris4Math.ThirtyThree

open scoped BigOperators

universe u

variable {V : Type u}

/-- The integer degree bound rules out 26 vertices already: every degree is
at least seven, so the total degree would be at least 182, exceeding 165. -/
theorem card_le_twenty_five [Fintype V] [DecidableEq V]
    (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edge_bound : H.edges.card ≤ 33) : Fintype.card V ≤ 25 := by
  by_contra hn
  have vertices : 26 ≤ Fintype.card V := by omega
  have minimum (x : V) : 7 ≤ H.degree x := by
    have h := H.pairCovering_degree_bound cover x
    omega
  have h := Finset.sum_le_sum (s := Finset.univ) (fun x _ => minimum x)
  simp only [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, Nat.cast_id] at h
  rw [H.sum_degrees] at h
  omega

/-- Ten explicit scalar inequalities, not an enumeration of hypergraphs or
colorings. They are the union bound multiplied by the permutation count. -/
theorem balanced_count_strict (v : ℕ) (hlower : 9 ≤ v) (hupper : v ≤ 18) :
    33 * (((v / 2).choose 5 + (v - v / 2).choose 5) *
      (Nat.factorial 5 * (v - 5).factorial)) < v.factorial := by
  interval_cases v <;> decide

/-- The generic balanced-permutation argument with the new edge budget. -/
theorem propertyB_nine_to_eighteen {v : ℕ} (hlower : 9 ≤ v) (hupper : v ≤ 18)
    (H : Simple5Hypergraph (Fin v)) (hsize : H.edges.card ≤ 33) : PropertyB H := by
  classical
  have hhalf : v / 2 ≤ (Finset.univ : Finset (Fin v)).card := by
    simpa using Nat.div_le_self v 2
  obtain ⟨red, _, hred⟩ := Finset.exists_subset_card_eq hhalf
  apply SmallVertices.propertyB_of_partition_count_bound H red
  simp only [Fintype.card_fin, hred]
  exact lt_of_le_of_lt (Nat.mul_le_mul_right _ hsize)
    (balanced_count_strict v hlower hupper)

/-- All simple five-uniform hypergraphs on at most 18 vertices with at most
33 edges are colorable. Pair coverage is not required. -/
theorem propertyB_of_vertices_le_eighteen {v : ℕ} (hv : v ≤ 18)
    (H : Simple5Hypergraph (Fin v)) (hsize : H.edges.card ≤ 33) : PropertyB H := by
  by_cases hsmall : v ≤ 8
  · exact Reduction.propertyB_of_vertices_le_eight hsmall H
  · exact propertyB_nine_to_eighteen (by omega) hv H hsize

/-- Choose the least vertex count among all counterexamples with at most
33 edges. The starting input is an arbitrary finite vertex type. -/
theorem exists_minimal_counterexample [Fintype V]
    (H : Simple5Hypergraph V) (hsize : H.edges.card ≤ 33)
    (hnotB : ¬ PropertyB H) :
    ∃ v : ℕ, ∃ K : Simple5Hypergraph (Fin v),
      K.edges.card ≤ 33 ∧ ¬ PropertyB K ∧
      (∀ w < v, ∀ L : Simple5Hypergraph (Fin w),
        L.edges.card ≤ 33 → PropertyB L) := by
  classical
  let P : ℕ → Prop := fun v => ∃ K : Simple5Hypergraph (Fin v),
    K.edges.card ≤ 33 ∧ ¬ PropertyB K
  have hex : ∃ v, P v := by
    refine ⟨Fintype.card V, Reduction.toFin H, ?_, ?_⟩
    · simpa only [Reduction.toFin_edge_count] using hsize
    · intro hp
      exact hnotB ((Reduction.propertyB_toFin_iff H).mp hp)
  obtain ⟨K, hKsize, hKnotB⟩ := Nat.find_spec hex
  refine ⟨Nat.find hex, K, hKsize, hKnotB, ?_⟩
  intro w hw L hLsize
  by_contra hLnotB
  have hleast := Nat.find_min' hex (show P w from ⟨L, hLsize, hLnotB⟩)
  exact (not_le_of_gt hw) hleast

/-- An uncovered pair would merge to a smaller counterexample. -/
theorem minimal_counterexample_pair_covering {v : ℕ}
    (H : Simple5Hypergraph (Fin v)) (hsize : H.edges.card ≤ 33)
    (hnotB : ¬ PropertyB H)
    (minimal : ∀ w < v, ∀ K : Simple5Hypergraph (Fin w),
      K.edges.card ≤ 33 → PropertyB K) : H.PairCovering := by
  classical
  intro x y hxy
  by_contra hnone
  have not_together : ∀ e ∈ H.edges, ¬(x ∈ e ∧ y ∈ e) := by
    intro e he hboth
    exact hnone ⟨e, he, hboth⟩
  obtain ⟨K, hKsize, hKnotB, hless⟩ :=
    Reduction.smaller_counterexample_of_uncovered_pair H hnotB x y hxy not_together
  have hless' : Fintype.card {z : Fin v // z ≠ y} < v := by simpa using hless
  exact hKnotB (minimal _ hless' K (hKsize.trans hsize))

/-- Every actual counterexample yields a pair-covering finite-label one.
Thus pair coverage is derived, not an extra premise of the original target. -/
theorem exists_pair_covering_counterexample [Fintype V]
    (H : Simple5Hypergraph V) (hsize : H.edges.card ≤ 33)
    (hnotB : ¬ PropertyB H) :
    ∃ v : ℕ, ∃ K : Simple5Hypergraph (Fin v),
      K.edges.card ≤ 33 ∧ ¬ PropertyB K ∧ K.PairCovering := by
  obtain ⟨v, K, hKsize, hKnotB, hminimal⟩ :=
    exists_minimal_counterexample H hsize hnotB
  exact ⟨v, K, hKsize, hKnotB,
    minimal_counterexample_pair_covering K hKsize hKnotB hminimal⟩

/-- There are enough distinct five-sets to pad to exactly 33 edges without
changing the vertex set. This does not use the old 32-edge main theorem. -/
theorem exists_extension_33 {v : ℕ} (hv : 8 ≤ v)
    (H : Simple5Hypergraph (Fin v)) (hsize : H.edges.card ≤ 33) :
    ∃ K : Simple5Hypergraph (Fin v), H.edges ⊆ K.edges ∧ K.edges.card = 33 := by
  classical
  let allEdges := (Finset.univ : Finset (Fin v)).powersetCard 5
  have hsub : H.edges ⊆ allEdges := by
    intro e he
    exact Finset.mem_powersetCard.mpr ⟨Finset.subset_univ e, H.five_uniform e he⟩
  have hcapacity : 33 ≤ allEdges.card := by
    have hchoose := Nat.choose_le_choose 5 hv
    have hsmall : Nat.choose 8 5 = 56 := by decide
    simp only [allEdges, Finset.card_powersetCard, Finset.card_univ, Fintype.card_fin]
    omega
  obtain ⟨edges, hHedges, hedgesAll, hcard⟩ :=
    Finset.exists_subsuperset_card_eq hsub hsize hcapacity
  let K : Simple5Hypergraph (Fin v) :=
    ⟨edges, fun e he => (Finset.mem_powersetCard.mp (hedgesAll he)).2⟩
  exact ⟨K, hHedges, hcard⟩

/-- Padding preserves noncolorability and pair coverage. -/
theorem exists_pair_covering_extension_33 {v : ℕ} (hv : 8 ≤ v)
    (H : Simple5Hypergraph (Fin v)) (hsize : H.edges.card ≤ 33)
    (hnotB : ¬ PropertyB H) (hpair : H.PairCovering) :
    ∃ K : Simple5Hypergraph (Fin v), K.edges.card = 33 ∧ ¬ PropertyB K ∧
      K.PairCovering := by
  obtain ⟨K, hsub, hcard⟩ := exists_extension_33 hv H hsize
  refine ⟨K, hcard, ?_, ?_⟩
  · intro hK
    exact hnotB (Reduction.propertyB_of_edges_subset H K hsub hK)
  · intro x y hxy
    obtain ⟨e, he, hboth⟩ := hpair x y hxy
    exact ⟨e, hsub he, hboth⟩

/-- The complete new counterexample reduction: arbitrary finite input to a
19–25 vertex, exactly-33-edge, pair-covering counterexample. -/
theorem exists_nineteen_to_twenty_five_counterexample [Fintype V]
    (H : Simple5Hypergraph V) (hsize : H.edges.card ≤ 33) (hnotB : ¬ PropertyB H) :
    ∃ v : ℕ, 19 ≤ v ∧ v ≤ 25 ∧ ∃ K : Simple5Hypergraph (Fin v),
      K.edges.card = 33 ∧ ¬ PropertyB K ∧ K.PairCovering := by
  obtain ⟨v, K, hKsize, hKnotB, hKcover⟩ :=
    exists_pair_covering_counterexample H hsize hnotB
  have hupper : v ≤ 25 := by
    simpa using card_le_twenty_five K hKcover hKsize
  have hlower : 19 ≤ v := by
    by_contra hn
    exact hKnotB (propertyB_of_vertices_le_eighteen (by omega) K hKsize)
  obtain ⟨L, hLsize, hLnotB, hLcover⟩ :=
    exists_pair_covering_extension_33 (by omega) K hKsize hKnotB hKcover
  exact ⟨v, hlower, hupper, L, hLsize, hLnotB, hLcover⟩

/-- The seven unresolved finite branches. This definition supplies no proof. -/
def FiniteGoal : Prop :=
  ∀ v : ℕ, 19 ≤ v → v ≤ 25 → ∀ H : Simple5Hypergraph (Fin v),
    H.edges.card = 33 → H.PairCovering → PropertyB H

/-- A proof of all seven new branches would prove the original T33.
The finite-case argument is an explicit premise, not an asserted result. -/
theorem target_of_finite_goal (finite : FiniteGoal) : Aris4Math.Target33.{u} := by
  classical
  intro V _ H hsize
  by_contra hnotB
  obtain ⟨v, hlower, hupper, K, hKsize, hKnotB, hKcover⟩ :=
    exists_nineteen_to_twenty_five_counterexample H hsize hnotB
  exact hKnotB (finite v hlower hupper K hKsize hKcover)

/-- T33 is equivalent to the finite reduction, in any vertex universe. -/
theorem target_iff_finite_goal : Aris4Math.Target33.{u} ↔ FiniteGoal := by
  constructor
  · intro htarget v _ _ H hsize _
    let e : Fin v ≃ ULift.{u} (Fin v) := Equiv.ulift.symm
    have hlift : (Reduction.relabel H e).edges.card ≤ 33 := by
      rw [Reduction.relabel_edge_count, hsize]
    have hPB := htarget (ULift.{u} (Fin v)) (Reduction.relabel H e) hlift
    exact (Reduction.propertyB_relabel_iff H e).mp hPB
  · exact target_of_finite_goal

end Aris4Math.ThirtyThree

#print axioms Aris4Math.ThirtyThree.card_le_twenty_five
#print axioms Aris4Math.ThirtyThree.balanced_count_strict
#print axioms Aris4Math.ThirtyThree.propertyB_of_vertices_le_eighteen
#print axioms Aris4Math.ThirtyThree.exists_nineteen_to_twenty_five_counterexample
#print axioms Aris4Math.ThirtyThree.target_of_finite_goal
#print axioms Aris4Math.ThirtyThree.target_iff_finite_goal

import Aris4Math.ThirtyFour.Target
import Aris4Math.ThirtyFour.SmallVertices
import Aris4Math.ThirtyFour.Nineteen

/-!
# Reduction of the 34-edge target to 19–25 vertices

Only the generic merging, incidence and balanced-permutation counting results
are reused. None of the still-open 34-edge branches is assumed internally.
The final assembly theorem exposes those seven branches as its explicit premise.
-/

namespace Aris4Math.ThirtyFour

open scoped BigOperators

universe u

variable {V : Type u}

/-- The integer degree bound rules out 26 vertices already: every degree is
at least seven, so the total degree would be at least 182, exceeding 170. -/
theorem card_le_twenty_five [Fintype V] [DecidableEq V]
    (H : Simple5Hypergraph V) (cover : H.PairCovering)
    (edge_bound : H.edges.card ≤ 34) : Fintype.card V ≤ 25 := by
  by_contra hn
  have vertices : 26 ≤ Fintype.card V := by omega
  have minimum (x : V) : 7 ≤ H.degree x := by
    have h := H.pairCovering_degree_bound cover x
    omega
  have h := Finset.sum_le_sum (s := Finset.univ) (fun x _ => minimum x)
  simp only [Finset.sum_const, Finset.card_univ, nsmul_eq_mul, Nat.cast_id] at h
  rw [H.sum_degrees] at h
  omega

/-- The small-vertex boundary includes an actual strict overlap at 17/18. -/
theorem propertyB_of_vertices_le_eighteen {v : ℕ} (hv : v ≤ 18)
    (H : Simple5Hypergraph (Fin v)) (hsize : H.edges.card ≤ 34) : PropertyB H :=
  SmallVertices.propertyB_of_vertices_le_eighteen hv H hsize

/-- Choose the least vertex count among all counterexamples with at most
34 edges. The starting input is an arbitrary finite vertex type. -/
theorem exists_minimal_counterexample [Fintype V]
    (H : Simple5Hypergraph V) (hsize : H.edges.card ≤ 34)
    (hnotB : ¬ PropertyB H) :
    ∃ v : ℕ, ∃ K : Simple5Hypergraph (Fin v),
      K.edges.card ≤ 34 ∧ ¬ PropertyB K ∧
      (∀ w < v, ∀ L : Simple5Hypergraph (Fin w),
        L.edges.card ≤ 34 → PropertyB L) := by
  classical
  let P : ℕ → Prop := fun v => ∃ K : Simple5Hypergraph (Fin v),
    K.edges.card ≤ 34 ∧ ¬ PropertyB K
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
    (H : Simple5Hypergraph (Fin v)) (hsize : H.edges.card ≤ 34)
    (hnotB : ¬ PropertyB H)
    (minimal : ∀ w < v, ∀ K : Simple5Hypergraph (Fin w),
      K.edges.card ≤ 34 → PropertyB K) : H.PairCovering := by
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
    (H : Simple5Hypergraph V) (hsize : H.edges.card ≤ 34)
    (hnotB : ¬ PropertyB H) :
    ∃ v : ℕ, ∃ K : Simple5Hypergraph (Fin v),
      K.edges.card ≤ 34 ∧ ¬ PropertyB K ∧ K.PairCovering := by
  obtain ⟨v, K, hKsize, hKnotB, hminimal⟩ :=
    exists_minimal_counterexample H hsize hnotB
  exact ⟨v, K, hKsize, hKnotB,
    minimal_counterexample_pair_covering K hKsize hKnotB hminimal⟩

/-- There are enough distinct five-sets to pad to exactly 34 edges without
changing the vertex set. This does not use the old 32-edge main theorem. -/
theorem exists_extension_34 {v : ℕ} (hv : 8 ≤ v)
    (H : Simple5Hypergraph (Fin v)) (hsize : H.edges.card ≤ 34) :
    ∃ K : Simple5Hypergraph (Fin v), H.edges ⊆ K.edges ∧ K.edges.card = 34 := by
  classical
  let allEdges := (Finset.univ : Finset (Fin v)).powersetCard 5
  have hsub : H.edges ⊆ allEdges := by
    intro e he
    exact Finset.mem_powersetCard.mpr ⟨Finset.subset_univ e, H.five_uniform e he⟩
  have hcapacity : 34 ≤ allEdges.card := by
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
theorem exists_pair_covering_extension_34 {v : ℕ} (hv : 8 ≤ v)
    (H : Simple5Hypergraph (Fin v)) (hsize : H.edges.card ≤ 34)
    (hnotB : ¬ PropertyB H) (hpair : H.PairCovering) :
    ∃ K : Simple5Hypergraph (Fin v), K.edges.card = 34 ∧ ¬ PropertyB K ∧
      K.PairCovering := by
  obtain ⟨K, hsub, hcard⟩ := exists_extension_34 hv H hsize
  refine ⟨K, hcard, ?_, ?_⟩
  · intro hK
    exact hnotB (Reduction.propertyB_of_edges_subset H K hsub hK)
  · intro x y hxy
    obtain ⟨e, he, hboth⟩ := hpair x y hxy
    exact ⟨e, hsub he, hboth⟩

/-- The complete new counterexample reduction: arbitrary finite input to a
19–25 vertex, exactly-34-edge, pair-covering counterexample. -/
theorem exists_nineteen_to_twenty_five_counterexample [Fintype V]
    (H : Simple5Hypergraph V) (hsize : H.edges.card ≤ 34) (hnotB : ¬ PropertyB H) :
    ∃ v : ℕ, 19 ≤ v ∧ v ≤ 25 ∧ ∃ K : Simple5Hypergraph (Fin v),
      K.edges.card = 34 ∧ ¬ PropertyB K ∧ K.PairCovering := by
  obtain ⟨v, K, hKsize, hKnotB, hKcover⟩ :=
    exists_pair_covering_counterexample H hsize hnotB
  have hupper : v ≤ 25 := by
    simpa using card_le_twenty_five K hKcover hKsize
  have hlower : 19 ≤ v := by
    by_contra hn
    exact hKnotB (propertyB_of_vertices_le_eighteen (by omega) K hKsize)
  obtain ⟨L, hLsize, hLnotB, hLcover⟩ :=
    exists_pair_covering_extension_34 (by omega) K hKsize hKnotB hKcover
  exact ⟨v, hlower, hupper, L, hLsize, hLnotB, hLcover⟩

/-- The seven unresolved finite branches. This definition supplies no proof. -/
def FiniteGoal : Prop :=
  ∀ v : ℕ, 19 ≤ v → v ≤ 25 → ∀ H : Simple5Hypergraph (Fin v),
    H.edges.card = 34 → H.PairCovering → PropertyB H

/-- A proof of all seven new branches would prove the original T34.
The finite-case argument is an explicit premise, not an asserted result. -/
theorem target_of_finite_goal (finite : FiniteGoal) : Aris4Math.Target34.{u} := by
  classical
  intro V _ H hsize
  by_contra hnotB
  obtain ⟨v, hlower, hupper, K, hKsize, hKnotB, hKcover⟩ :=
    exists_nineteen_to_twenty_five_counterexample H hsize hnotB
  exact hKnotB (finite v hlower hupper K hKsize hKcover)

/-- T34 is equivalent to the finite reduction, in any vertex universe. -/
theorem target_iff_finite_goal : Aris4Math.Target34.{u} ↔ FiniteGoal := by
  constructor
  · intro htarget v _ _ H hsize _
    let e : Fin v ≃ ULift.{u} (Fin v) := Equiv.ulift.symm
    have hlift : (Reduction.relabel H e).edges.card ≤ 34 := by
      rw [Reduction.relabel_edge_count, hsize]
    have hPB := htarget (ULift.{u} (Fin v)) (Reduction.relabel H e) hlift
    exact (Reduction.propertyB_relabel_iff H e).mp hPB
  · exact target_of_finite_goal

/-- Nineteen vertices are already fully discharged; these six branches are
exactly the open mathematical content, not additional original hypotheses. -/
def RemainingGoal : Prop :=
  ∀ v : ℕ, 20 ≤ v → v ≤ 25 → ∀ H : Simple5Hypergraph (Fin v),
    H.edges.card = 34 → H.PairCovering → PropertyB H

theorem target_iff_remaining_goal : Aris4Math.Target34.{u} ↔ RemainingGoal := by
  rw [target_iff_finite_goal]
  constructor
  · intro finite v lower upper H size cover
    exact finite v (by omega) upper H size cover
  · intro remaining v lower upper H size cover
    by_cases h19 : v = 19
    · subst v
      exact nineteen_propertyB_of_eq H cover size
    · exact remaining v (by omega) upper H size cover

end Aris4Math.ThirtyFour

#print axioms Aris4Math.ThirtyFour.card_le_twenty_five
#print axioms Aris4Math.ThirtyFour.propertyB_of_vertices_le_eighteen
#print axioms Aris4Math.ThirtyFour.exists_nineteen_to_twenty_five_counterexample
#print axioms Aris4Math.ThirtyFour.target_of_finite_goal
#print axioms Aris4Math.ThirtyFour.target_iff_finite_goal

#print axioms Aris4Math.ThirtyFour.target_iff_remaining_goal

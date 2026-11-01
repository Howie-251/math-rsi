import Aris4Math.ThirtyThree.TwentyThreeSelection
import Aris4Math.ThirtyThree.MultiLockRecovery
import Aris4Math.ThirtyThree.QuadProfiles

/-! Actual bounded inputs for four degree-six locks on 23 vertices.
The large traces are multiplicities, including the possible repeated triple.
No finite catalog or probability conclusion is assumed here. -/
namespace Aris4Math.ThirtyThree.TwentyThreeFourLowStructure
open scoped BigOperators
open Aris4Math.ThirtyThree.MultiLockRecovery

theorem trace_excess_budget (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (vertices : Fin 4 ↪ Fin 23)
    (degrees : ∀ i, H.degree (vertices i) = 6)
    (T : Finset (Fin 4)) (i : Fin 4) (hi : i ∈ T) :
    (T.card - 1) * (count H vertices T - 1) ≤ 2 := by
  have cap := TwentyThreeSelection.indexed_six_excess_le_two H cover
    (Fintype.card_fin 23) vertices vertices.injective i (degrees i)
  have sub : T.erase i ⊆ Finset.univ.erase i := by
    intro j hj
    exact Finset.mem_erase.mpr ⟨(Finset.mem_erase.mp hj).1, Finset.mem_univ j⟩
  have lower : (∑ j ∈ T.erase i, (count H vertices T - 1)) ≤
      ∑ j ∈ T.erase i, (H.codegree (vertices i) (vertices j) - 1) := by
    apply Finset.sum_le_sum
    intro j hj
    exact Nat.sub_le_sub_right
      (count_le_codegree H vertices T i j hi (Finset.mem_erase.mp hj).2) 1
  have upper := Finset.sum_le_sum_of_subset sub
    (f := fun j => H.codegree (vertices i) (vertices j) - 1)
  have h := lower.trans (upper.trans cap)
  simpa only [Finset.sum_const, Finset.card_erase_of_mem hi, smul_eq_mul] using h

theorem high_count_le_two (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (vertices : Fin 4 ↪ Fin 23)
    (degrees : ∀ i, H.degree (vertices i) = 6)
    (T : Finset (Fin 4)) (large : 3 ≤ T.card) : count H vertices T ≤ 2 := by
  obtain ⟨i,hi⟩ := Finset.card_pos.mp (by omega : 0 < T.card)
  have h := trace_excess_budget H cover vertices degrees T i hi
  have left : 2 ≤ T.card - 1 := by omega
  have step := Nat.mul_le_mul_right (count H vertices T - 1) left
  omega

theorem quad_count_le_one (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (vertices : Fin 4 ↪ Fin 23)
    (degrees : ∀ i, H.degree (vertices i) = 6) :
    count H vertices Finset.univ ≤ 1 := by
  have h := trace_excess_budget H cover vertices degrees Finset.univ 0 (Finset.mem_univ 0)
  simp only [Finset.card_univ,Fintype.card_fin] at h
  omega

/-- The actual high-trace vector lies in the finite domain 3⁴ × 2.
The first four entries are allowed to equal two. -/
theorem actual_high_bounds (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (vertices : Fin 4 ↪ Fin 23)
    (degrees : ∀ i, H.degree (vertices i) = 6) :
    (∀ i : Fin 4, count H vertices (QuadProfiles.highLabels i.castSucc) < 3) ∧
      count H vertices (QuadProfiles.highLabels 4) < 2 := by
  constructor
  · intro i
    have size : 3 ≤ (QuadProfiles.highLabels i.castSucc).card := by fin_cases i <;> decide
    have h := high_count_le_two H cover vertices degrees _ size
    omega
  · have h := quad_count_le_one H cover vertices degrees
    have same : QuadProfiles.highLabels 4 = (Finset.univ : Finset (Fin 4)) := by decide
    rw [same]
    omega

end Aris4Math.ThirtyThree.TwentyThreeFourLowStructure

#print axioms Aris4Math.ThirtyThree.TwentyThreeFourLowStructure.actual_high_bounds

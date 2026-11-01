import Aris4Math.ProfileProbability
import Aris4Math.ConditionalUnion
import Aris4Math.ProfileDeletion

/-! Apply a realized numerical profile to the actual hypergraph. All single
event formulas and all multiplicities are discharged in imported theorems. -/

namespace Aris4Math.ProfileApplication

open TypeCounting EndpointCounting CriticalCounting ProfileProbability

variable {v : ℕ} {ι : Type*} [Fintype ι] [DecidableEq ι]

theorem endpoint_sum_eq (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Numeric.Profile)
    (hp : RealizesProfile H vertices positions p) (k : Fin v) (last : Bool) :
    (∑ e ∈ H.edges, lockedRatio vertices positions (fun σ => EndpointAt e σ k last)) =
      if last then Numeric.boundA p (k.val+1) else Numeric.boundB p (k.val+1) := by
  calc
    _ = ∑ e ∈ H.edges, Numeric.edgeWeight p ⟨positionType vertices positions e, 0⟩
        (k.val+1) last := by
      apply Finset.sum_congr rfl
      intro e he
      exact endpoint_ratio_numeric H vertices positions p hp e he _ rfl k last
    _ = _ := edge_sum_numeric H.edges _ p hp.table _ last

theorem critical_sum_le (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Numeric.Profile)
    (hp : RealizesProfile H vertices positions p) (noCap : p.emptyPairCap = none)
    (k : Fin v) :
    (∑ d ∈ H.edges.offDiag, lockedRatio vertices positions (fun σ =>
      Greedy.CriticalPair (d.1.map σ.toEmbedding) (d.2.map σ.toEmbedding) k)) ≤
      Numeric.boundC p (k.val+1) := by
  calc
    _ ≤ ∑ d ∈ H.edges.offDiag, Numeric.pairWeight p
        ⟨positionType vertices positions d.1, 0⟩
        ⟨positionType vertices positions d.2, 0⟩ (k.val+1) := by
      apply Finset.sum_le_sum
      intro d hd
      obtain ⟨h1,h2,hne⟩ := Finset.mem_offDiag.mp hd
      exact critical_ratio_le_numeric H vertices positions p hp d.1 d.2 h1 h2 hne
        _ _ rfl rfl k
    _ = _ := pair_sum_numeric H.edges _ p hp.table noCap _

/-- A structural realization of an uncorrected profile and its kernel-checked
strict bound now suffice for the original PropertyB conclusion. -/
theorem propertyB_of_uncorrected_profile (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Numeric.Profile)
    (hp : RealizesProfile H vertices positions p)
    (noCap : p.emptyPairCap = none) (noCorrection : p.correctionCenters = [])
    (strict : Numeric.totalBound p < 1) : PropertyB H := by
  apply ConditionalUnion.propertyB_of_position_bounds H vertices positions
    (fun k => Numeric.boundA p (k.val+1))
    (fun k => Numeric.boundB p (k.val+1))
    (fun k => Numeric.boundC p (k.val+1))
  · intro k
    exact le_of_eq (endpoint_sum_eq H vertices positions p hp k true)
  · intro k
    exact le_of_eq (endpoint_sum_eq H vertices positions p hp k false)
  · exact critical_sum_le H vertices positions p hp noCap
  · have heq := totalBound_eq_sum_of_eq p v hp.vertex_count
    simp only [Numeric.positionBound, Numeric.deduction, noCorrection,
      List.not_mem_nil, ↓reduceIte, sub_zero] at heq
    rw [← heq]
    exact strict

/-- Apply the exact realized profile with the actual link deletion at each
correction center. The center inequalities refer to concrete edge pairs;
all event semantics, type multiplicities, and min placement are proved. -/
theorem propertyB_of_corrected_profile (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Numeric.Profile)
    (hp : RealizesProfile H vertices positions p)
    (noCap : p.emptyPairCap = none)
    (center_lower : ∀ j, (positions j).val + 1 ∈ p.correctionCenters →
      Numeric.deduction p ((positions j).val + 1) ≤
        ∑ d ∈ LinkDeletion.directedBadPairs H (vertices j),
          LinkWeightCertificates.typeWeight p (positionType vertices positions)
            ((positions j).val + 1) d)
    (strict : Numeric.totalBound p < 1) : PropertyB H := by
  apply ConditionalUnion.propertyB_of_weighted_position_bounds H vertices positions
    (fun k => Numeric.boundA p (k.val+1))
    (fun k => Numeric.boundB p (k.val+1))
    (fun k => Numeric.boundC p (k.val+1))
    (fun k => Numeric.deduction p (k.val+1))
    (fun k => LinkWeightCertificates.typeWeight p (positionType vertices positions) (k.val+1))
    (ProfileDeletion.correctionDeleted H vertices positions p)
  · intro k
    exact le_of_eq (endpoint_sum_eq H vertices positions p hp k true)
  · intro k
    exact le_of_eq (endpoint_sum_eq H vertices positions p hp k false)
  · intro k d hd
    obtain ⟨h1,h2,hne⟩ := Finset.mem_offDiag.mp hd
    exact critical_ratio_le_numeric H vertices positions p hp d.1 d.2 h1 h2 hne
      _ _ rfl rfl k
  · intro k
    exact le_of_eq (pair_sum_numeric H.edges _ p hp.table noCap (k.val+1))
  · exact ProfileDeletion.correctionDeleted_subset H vertices positions p
  · exact ProfileDeletion.correctionDeleted_bad H vertices positions p
  · exact ProfileDeletion.all_position_deletion_lower H vertices positions p hp center_lower
  · have heq := totalBound_eq_sum_of_eq p v hp.vertex_count
    change (∑ k : Fin v, Numeric.positionBound p (k.val+1)) < 1
    rw [← heq]
    exact strict

end Aris4Math.ProfileApplication

#print axioms Aris4Math.ProfileApplication.endpoint_sum_eq
#print axioms Aris4Math.ProfileApplication.critical_sum_le
#print axioms Aris4Math.ProfileApplication.propertyB_of_uncorrected_profile
#print axioms Aris4Math.ProfileApplication.propertyB_of_corrected_profile

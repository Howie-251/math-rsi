import Aris4Math.ProfileApplication

/-! Apply a realized profile with a mathematically proved custom deletion.
The numeric profile supplies actual endpoint and pair formulas; the loss is
separately connected to the same real bad-link deletion sets. -/

namespace Aris4Math.ThirtyThree.CustomDeletion

open Aris4Math.TypeCounting Aris4Math.EndpointCounting
open Aris4Math.ProfileProbability Aris4Math.LinkWeightCertificates
open Aris4Math.LinkDeletion Aris4Math.ProfileDeletion
open scoped BigOperators

variable {v edgeCount : ℕ} {ι : Type*} [Fintype ι] [DecidableEq ι]

theorem propertyB_of_custom_deletion (H : Simple5Hypergraph (Fin v))
    (vertices positions : ι ↪ Fin v) (p : Numeric.Profile)
    (real : RealizesProfile H vertices positions p edgeCount)
    (noCap : p.emptyPairCap = none) (loss : ℕ → ℚ)
    (center_lower : ∀ j, (positions j).val + 1 ∈ p.correctionCenters →
      loss ((positions j).val + 1) ≤
        ∑ d ∈ directedBadPairs H (vertices j),
          typeWeight p (positionType vertices positions) ((positions j).val + 1) d)
    (zeroOutside : ∀ k, k ∉ p.correctionCenters → loss k = 0)
    (strict : (∑ k : Fin v, min (Numeric.boundA p (k.val+1))
      (min (Numeric.boundB p (k.val+1)) (Numeric.boundC p (k.val+1) - loss (k.val+1)))) < 1) :
    PropertyB H := by
  apply ConditionalUnion.propertyB_of_weighted_position_bounds H vertices positions
    (fun k => Numeric.boundA p (k.val+1))
    (fun k => Numeric.boundB p (k.val+1))
    (fun k => Numeric.boundC p (k.val+1))
    (fun k => loss (k.val+1))
    (fun k => typeWeight p (positionType vertices positions) (k.val+1))
    (correctionDeleted H vertices positions p)
  · intro k
    exact le_of_eq (ProfileApplication.endpoint_sum_eq H vertices positions p real k true)
  · intro k
    exact le_of_eq (ProfileApplication.endpoint_sum_eq H vertices positions p real k false)
  · intro k d hd
    obtain ⟨h1,h2,hne⟩ := Finset.mem_offDiag.mp hd
    exact critical_ratio_le_numeric H vertices positions p real d.1 d.2 h1 h2 hne
      _ _ rfl rfl k
  · intro k
    exact le_of_eq (pair_sum_numeric H.edges _ p real.table noCap (k.val+1))
  · exact correctionDeleted_subset H vertices positions p
  · exact correctionDeleted_bad H vertices positions p
  · intro k
    by_cases hc : k.val + 1 ∈ p.correctionCenters
    · obtain ⟨j, hj⟩ := correction_is_locked H vertices positions p real k hc
      subst k
      rw [correctionDeleted_at H vertices positions p j hc]
      exact center_lower j hc
    · rw [correctionDeleted_empty H vertices positions p k hc, zeroOutside _ hc]
      simp
  · exact strict

end Aris4Math.ThirtyThree.CustomDeletion

#print axioms Aris4Math.ThirtyThree.CustomDeletion.propertyB_of_custom_deletion

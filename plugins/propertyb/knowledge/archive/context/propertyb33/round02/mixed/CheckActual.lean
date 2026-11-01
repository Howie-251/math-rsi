import Aris4Math.ThirtyThree.TwentyFourMixedFacts
import Aris4Math.ThirtyThree.TwentyFourSelection

namespace Aris4Math.ThirtyThree.TwentyFourMixed
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TwentyFourMixedData
open Aris4Math.ThirtyThree.TwentyFourMixedFacts
open Aris4Math.ThirtyThree.TwentyFourMixedFacts

theorem actual_profile (H : Simple5Hypergraph (Fin 24))
    (vertices : Fin 5 ↪ Fin 24) (c : Config)
    (actual : ∀ T, count H vertices T = counts (family c) T) :
    RealizesProfile H vertices (positions c) (p c) 33 := by
  have valid := profile_valid c
  rw [profiles_calculated, calculated_eq_profile] at valid ⊢
  refine ⟨rfl, valid, ?_, TripleProfiles.table_pruneZero _ _ _
    (raw_table H vertices (positions c) labels labels_nodup labels_all
      (counts (family c)) actual _)⟩
  simp [profile, TripleProfiles.pruneZero, rawProfile, canonicalType]

theorem actual_classification (H : Simple5Hypergraph (Fin 24))
    (vertices : Fin 5 ↪ Fin 24) (edges33 : H.edges.card = 33)
    (degrees : ∀ j, H.degree (vertices j) = degreeData j)
    (unit : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1) :
    ∃ t : Fin 32, ∀ T, count H vertices T = counts t T := by
  have hlow : ∀ T, T.card ≤ 2 → upperCount H vertices T = low T := by
    apply upper_eq_of_low_data
    · simpa only [low, if_pos rfl] using edges33.symm
    · intro i
      rw [degrees]
      fin_cases i <;> decide +kernel
    · intro i j hij
      rw [unit i j hij]
      simp [low, Finset.card_pair hij]
  obtain ⟨t, ht⟩ := FiveLockClassification.actual_recovered_in_table
    H vertices unit low hlow
  exact ⟨t, fun T => (ht T).trans (counts_eq_recovered t T).symm⟩

end Aris4Math.ThirtyThree.TwentyFourMixed

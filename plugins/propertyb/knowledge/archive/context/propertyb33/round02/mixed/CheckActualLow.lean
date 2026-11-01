import Aris4Math.ThirtyThree.TwentyFourMixedFacts
import Aris4Math.ThirtyThree.TwentyFourSelection

namespace Aris4Math.ThirtyThree.TwentyFourMixed
open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TwentyFourMixedData
open Aris4Math.ThirtyThree.TwentyFourMixedFacts
open Aris4Math.ThirtyThree.TwentyFourMixedFacts

def slotWeight (c : Config) (j : Fin 2) (z : Finset (Fin 5) × Finset (Fin 5)) : ℚ :=
  Numeric.pairWeight (p c) ⟨executableType (positions c) z.1,0⟩
    ⟨executableType (positions c) z.2,0⟩ ((positions c (j.castLE (by omega))).val+1) +
  Numeric.pairWeight (p c) ⟨executableType (positions c) z.2,0⟩
    ⟨executableType (positions c) z.1,0⟩ ((positions c (j.castLE (by omega))).val+1)


theorem actual_low_slot (H : Simple5Hypergraph (Fin 24)) (cover : H.PairCovering)
    (vertices : Fin 5 ↪ Fin 24) (t : Fin 32)
    (actual : ∀ T, count H vertices T = counts t T)
    (degrees : ∀ j, H.degree (vertices j) = degreeData j)
    (unit : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1)
    (j : Fin 2)
    (avoid : ∀ P ∈ H.badLinkPairs (vertices (j.castLE (by omega))),
      ∃ E ∈ P, Disjoint E (({2,3,4} : Finset (Fin 5)).image vertices)) :
    ∃ b : Fin 8, ∀ c : Config,
      slotWeight c j (slot t j b) ≤
        ∑ d ∈ directedBadPairs H (vertices (j.castLE (by omega))),
          typeWeight (p c) (positionType vertices (positions c))
            ((positions c (j.castLE (by omega))).val+1) d := by
  let j5 : Fin 5 := j.castLE (by omega)
  have degree6 : H.degree (vertices j5) = 6 := by
    rw [degrees]
    exact if_pos j.isLt
  have cardpos := H.link_bad_pair_lower_bound cover (vertices j5)
  rw [Fintype.card_fin, degree6] at cardpos
  have nonempty : (H.badLinkPairs (vertices j5)).Nonempty :=
    Finset.card_pos.mp (by norm_num at cardpos ⊢; omega)
  obtain ⟨T,U,E,F,bad,hE,hF,adm⟩ := ActualBadSlot.exists_actual_slot H vertices j5
    (fun i hij => unit j5 i (Ne.symm hij)) nonempty
  have avoidTU := ActualBadSlot.slot_avoids_of_pair_avoids vertices E F {2,3,4}
    (avoid {E,F} bad)
  rw [hE,hF] at avoidTU
  have adm' : ActualBadSlot.Admissible (counts t) j5 T U := by
    simpa only [ActualBadSlot.Admissible, actual] using adm
  obtain ⟨b,hb⟩ := slot_complete t j T U adm' avoidTU
  refine ⟨b, fun c => ?_⟩
  have bound := ActualBadSlot.slot_weight_lower H vertices (positions c) (p c) j5
    E F T U bad hE hF
  rcases hb with ⟨rfl,rfl⟩ | ⟨rfl,rfl⟩
  · simpa only [slotWeight, executableType_eq, j5] using bound
  · simpa only [slotWeight, executableType_eq, j5, add_comm] using bound

end Aris4Math.ThirtyThree.TwentyFourMixed

import Aris4Math.ThirtyFour.MixedLayoutApplication
import Aris4Math.ThirtyThree.FiveProfiles

namespace Aris4Math.ThirtyFour.MixedLayoutFive
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.FiveProfiles
open Aris4Math.ThirtyThree.TripleProfiles (table_pruneZero pruneZero)
open Aris4Math.ThirtyThree.MultiLockRecovery (count)
variable {v m : ℕ} {L : Type*}

def executableWeights (positions : L → Fin 5 ↪ Fin v) (p : L → Numeric.Profile)
    (l : L) (j : Fin 5) (T U : Finset (Fin 5)) : ℚ :=
  Numeric.pairWeight (p l) ⟨executableType (positions l) T,0⟩
    ⟨executableType (positions l) U,0⟩ ((positions l j).val+1)

theorem weights_eq (positions : L → Fin 5 ↪ Fin v) (p : L → Numeric.Profile) :
    MixedLayoutApplication.weights positions p=executableWeights positions p := by
  funext l j T U
  simp only [executableWeights,MixedLayoutApplication.weights,executableType_eq]
  rfl

theorem realizes (H : Simple5Hypergraph (Fin v)) (vertices positions : Fin 5 ↪ Fin v)
    (μ : Finset (Fin 5) → ℕ) (hμ : ∀ T, count H vertices T=μ T)
    (centers : List ℕ) (valid : Numeric.validProfile (profile positions μ centers) m) :
    RealizesProfile H vertices positions (profile positions μ centers) m := by
  refine ⟨rfl,valid,?_,table_pruneZero _ _ _ (raw_table H vertices positions μ hμ centers)⟩
  simp [profile,pruneZero,rawProfile,canonicalType]
end Aris4Math.ThirtyFour.MixedLayoutFive

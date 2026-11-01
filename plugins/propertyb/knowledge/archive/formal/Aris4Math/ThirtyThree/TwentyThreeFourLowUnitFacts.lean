import Aris4Math.ThirtyThree.TwentyThreeFourLowUnitData
import Aris4Math.ThirtyThree.TwentyThreeFourLowCatalog
namespace Aris4Math.ThirtyThree.TwentyThreeFourLowUnitFacts
open TwentyThreeFourLowUnitData

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem counts_eq_catalog : ∀ k : Fin 3, ∀ T,
    counts k T = TwentyThreeFourLowCatalog.counts (k.castLE (by omega)) T := by decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem slot_complete : ∀ k : Fin 3, ∀ j : Fin 4, ∀ T U : Finset (Fin 4),
    ActualBadSlot.Admissible (counts k) j T U →
    ∃ b : Fin 7, (T = (slot k j b).1 ∧ U = (slot k j b).2) ∨
      (U = (slot k j b).1 ∧ T = (slot k j b).2) := by
  intro k
  fin_cases k <;> decide +kernel

def calculated (c : Config) : Numeric.Profile :=
  TripleProfiles.pruneZero ⟨23, QuadProfiles.executableType (positions c) Finset.univ,
    QuadProfiles.labels.map fun T => ⟨QuadProfiles.executableType (positions c) T, counts (family c) T⟩,
    none, List.ofFn fun j => (positions c j).val+1⟩

private theorem profile_ext (a b : Numeric.Profile)
    (hv : a.v = b.v) (hp : a.positions = b.positions) (ht : a.types = b.types)
    (hc : a.emptyPairCap = b.emptyPairCap) (hk : a.correctionCenters = b.correctionCenters) :
    a = b := by
  cases a
  cases b
  simp_all

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem profiles_calculated : ∀ c : Config, p c = calculated c := by
  intro c
  fin_cases c <;> apply profile_ext <;> decide +kernel

theorem calculated_eq_profile (c : Config) : calculated c =
    QuadProfiles.profile (positions c) (counts (family c))
      (List.ofFn fun j => (positions c j).val+1) := by
  simp only [calculated, QuadProfiles.executableType_eq, QuadProfiles.profile,
    QuadProfiles.rawProfile]

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem profile_valid : ∀ c : Config, Numeric.validProfile (p c) 33 := by
  unfold Numeric.validProfile
  intro c
  fin_cases c <;> decide +kernel

end Aris4Math.ThirtyThree.TwentyThreeFourLowUnitFacts

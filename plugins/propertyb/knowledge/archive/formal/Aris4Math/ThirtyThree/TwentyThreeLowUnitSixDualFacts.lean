import Aris4Math.ThirtyThree.TwentyThreeLowUnitSixDualData

namespace Aris4Math.ThirtyThree.TwentyThreeLowUnitSixDualFacts
open scoped BigOperators
open Aris4Math.TypeCounting MultiLockRecovery
open TwentyThreeLowUnitSixDualData

def calculated (c : Case) : Numeric.Profile :=
  TripleProfiles.pruneZero ⟨23, TwentyThreeHighSixProfiles.executableType (positions c) Finset.univ,
    TwentyThreeHighSixProfiles.labels.map fun T => ⟨TwentyThreeHighSixProfiles.executableType (positions c) T, counts c T⟩,
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
theorem profiles_calculated : ∀ c : Case, p c = calculated c := by
  intro c
  fin_cases c <;> apply profile_ext <;> decide +kernel

theorem calculated_eq_profile (c : Case) : calculated c =
    TwentyThreeHighSixProfiles.profile (positions c) (counts c) (List.ofFn fun j => (positions c j).val+1) := by
  simp only [calculated, TwentyThreeHighSixProfiles.executableType_eq, TwentyThreeHighSixProfiles.profile,
    TwentyThreeHighSixProfiles.rawProfile]

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem profile_valid : ∀ c : Case, Numeric.validProfile (p c) 33 := by
  unfold Numeric.validProfile
  intro c
  fin_cases c <;> decide +kernel


end Aris4Math.ThirtyThree.TwentyThreeLowUnitSixDualFacts

import Aris4Math.ThirtyThree.TwentyFourMixedData

namespace Aris4Math.ThirtyThree.TwentyFourMixedFacts

open scoped BigOperators
open Aris4Math.TypeCounting Aris4Math.LinkDeletion Aris4Math.LinkWeightCertificates
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TwentyFourMixedData

def degreeData (j : Fin 5) : ℕ := if j.val < 2 then 6 else 7
def low (T : Finset (Fin 5)) : ℕ :=
  if T = ∅ then 33 else if T.card = 1 then
    if 0 ∈ T ∨ 1 ∈ T then 6 else 7 else 1

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem counts_eq_recovered : ∀ r : Fin 32, ∀ T : Finset (Fin 5),
    counts r T = recovered low (FiveLockClassification.high r) T := by
  intro r
  fin_cases r <;> decide +kernel

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem slot_complete : ∀ r : Fin 32, ∀ j : Fin 2, ∀ T U : Finset (Fin 5),
    ActualBadSlot.Admissible (counts r) (j.castLE (by omega)) T U →
    (Disjoint T ({2,3,4} : Finset (Fin 5)) ∨ Disjoint U ({2,3,4} : Finset (Fin 5))) →
    ∃ b : Fin 8, (T = (slot r j b).1 ∧ U = (slot r j b).2) ∨
      (U = (slot r j b).1 ∧ T = (slot r j b).2) := by
  intro r
  fin_cases r <;> decide +kernel

def executableType (positions : Fin 5 ↪ Fin 24) (T : Finset (Fin 5)) : List ℕ :=
  (((List.finRange 5).filter fun j => j ∈ T).map fun j => (positions j).val+1).insertionSort (· ≤ ·)

theorem executableType_eq (positions : Fin 5 ↪ Fin 24) (T : Finset (Fin 5)) :
    executableType positions T = canonicalType positions T := by
  have hn : (((List.finRange 5).filter fun j => j ∈ T).map
      fun j => (positions j).val+1).Nodup :=
    (List.nodup_finRange 5).filter _ |>.map (fun i j h =>
      positions.injective (Fin.ext (Nat.add_right_cancel h)))
  apply List.eq_of_perm_of_sorted (r := (· ≤ ·))
  · apply (List.perm_ext_iff_of_nodup
      ((List.perm_insertionSort _ _).nodup_iff.mpr hn)
      (Finset.sort_nodup _ _)).mpr
    intro n
    simp [executableType,canonicalType,List.mem_insertionSort,List.mem_finRange]
  · exact List.sorted_insertionSort _ _
  · exact Finset.sort_sorted _ _

def calculated (c : Config) : Numeric.Profile :=
  TripleProfiles.pruneZero ⟨24, executableType (positions c) Finset.univ,
    labels.map fun T => ⟨executableType (positions c) T, counts (family c) T⟩,
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
    profile labels (positions c) (counts (family c)) (List.ofFn fun j => (positions c j).val+1) := by
  simp only [calculated, executableType_eq, profile, rawProfile]

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem profile_valid : ∀ c : Config, Numeric.validProfile (p c) 33 := by
  unfold Numeric.validProfile
  intro c
  fin_cases c <;> decide +kernel


end Aris4Math.ThirtyThree.TwentyFourMixedFacts
#print axioms Aris4Math.ThirtyThree.TwentyFourMixedFacts.slot_complete

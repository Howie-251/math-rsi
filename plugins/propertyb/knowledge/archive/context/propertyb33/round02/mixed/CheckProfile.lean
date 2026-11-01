import Aris4Math.ThirtyThree.TwentyFourMixedData
open Aris4Math.ThirtyThree.TwentyFourMixedData Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math Aris4Math.ThirtyThree
namespace Test
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
example : ∀ c : Config, p c = calculated c := by
 intro c
 fin_cases c <;> apply profile_ext <;> decide +kernel
end Test

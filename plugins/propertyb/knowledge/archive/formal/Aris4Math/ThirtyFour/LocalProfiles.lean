import Aris4Math.ThirtyFour.MixedLayoutApplication
namespace Aris4Math.ThirtyFour.LocalProfiles
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TripleProfiles (table_pruneZero pruneZero)
variable {n v m : ℕ} {L : Type*}
def executableType (positions : Fin n ↪ Fin v) (T : Finset (Fin n)) : List ℕ :=
  (((List.finRange n).filter fun j => j ∈ T).map fun j => (positions j).val+1).insertionSort (· ≤ ·)

theorem executableType_eq (positions : Fin n ↪ Fin v) (T : Finset (Fin n)) :
    executableType positions T = canonicalType positions T := by
  have hn : (((List.finRange n).filter fun j => j ∈ T).map
      fun j => (positions j).val+1).Nodup :=
    (List.nodup_finRange n).filter _ |>.map (fun i j h =>
      positions.injective (Fin.ext (Nat.add_right_cancel h)))
  apply List.eq_of_perm_of_sorted (r := (· ≤ ·))
  · apply (List.perm_ext_iff_of_nodup
      ((List.perm_insertionSort _ _).nodup_iff.mpr hn)
      (Finset.sort_nodup _ _)).mpr
    intro n
    simp [executableType,canonicalType,List.mem_insertionSort,List.mem_finRange]
  · exact List.sorted_insertionSort _ _
  · exact Finset.sort_sorted _ _

def executableWeights (positions : L → Fin n ↪ Fin v) (p : L → Numeric.Profile)
    (l : L) (j : Fin n) (T U : Finset (Fin n)) : ℚ :=
  Numeric.pairWeight (p l) ⟨executableType (positions l) T,0⟩
    ⟨executableType (positions l) U,0⟩ ((positions l j).val+1)

theorem weights_eq (positions : L → Fin n ↪ Fin v) (p : L → Numeric.Profile) :
    MixedLayoutApplication.weights positions p=executableWeights positions p := by
  funext l j T U
  simp only [executableWeights,MixedLayoutApplication.weights,executableType_eq]


theorem realizes (H : Simple5Hypergraph (Fin v)) (vertices positions : Fin n ↪ Fin v)
    (labels : List (Finset (Fin n))) (nodup : labels.Nodup) (all : ∀ T, T∈labels)
    (μ : Finset (Fin n) → ℕ) (hμ : ∀ T, count H vertices T=μ T)
    (centers : List ℕ) (valid : Numeric.validProfile (profile labels positions μ centers) m) :
    RealizesProfile H vertices positions (profile labels positions μ centers) m := by
  refine ⟨rfl,valid,?_,table_pruneZero _ _ _ (raw_table H vertices positions labels nodup all μ hμ centers)⟩
  simp [profile,pruneZero,rawProfile,canonicalType]
end Aris4Math.ThirtyFour.LocalProfiles

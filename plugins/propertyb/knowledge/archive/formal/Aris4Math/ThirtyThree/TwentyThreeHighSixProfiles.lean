import Aris4Math.ThirtyThree.MultiLockRecovery

/-! Executable complete six-lock profiles, with actual-H realization. -/
namespace Aris4Math.ThirtyThree.TwentyThreeHighSixProfiles
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero table_pruneZero)
open Aris4Math.ThirtyThree.MultiLockRecovery (count)

def labels : List (Finset (Fin 6)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3},{4},{0,4},{1,4},{0,1,4},{2,4},{0,2,4},{1,2,4},{0,1,2,4},{3,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4},{5},{0,5},{1,5},{0,1,5},{2,5},{0,2,5},{1,2,5},{0,1,2,5},{3,5},{0,3,5},{1,3,5},{0,1,3,5},{2,3,5},{0,2,3,5},{1,2,3,5},{0,1,2,3,5},{4,5},{0,4,5},{1,4,5},{0,1,4,5},{2,4,5},{0,2,4,5},{1,2,4,5},{0,1,2,4,5},{3,4,5},{0,3,4,5},{1,3,4,5},{0,1,3,4,5},{2,3,4,5},{0,2,3,4,5},{1,2,3,4,5},{0,1,2,3,4,5}]
theorem labels_nodup : labels.Nodup := by decide +kernel
theorem label_univ : (Finset.univ : Finset (Finset (Fin 6))) = labels.toFinset := by decide +kernel
theorem mem_labels (T : Finset (Fin 6)) : T ∈ labels := by
  have h := Finset.mem_univ T
  rw [label_univ] at h
  exact List.mem_toFinset.mp h

variable {v : ℕ}

/-- Canonical increasing one-based position signature of an abstract label. -/
def canonicalType (positions : Fin 6 ↪ Fin v) (T : Finset (Fin 6)) : List ℕ :=
  (T.image fun i => (positions i).val + 1).sort (· ≤ ·)

/-- An executable representative of the canonical type; unlike the quotient
sort implementation this finite insertion sort reduces in the kernel. -/
def executableType (positions : Fin 6 ↪ Fin v) (T : Finset (Fin 6)) : List ℕ :=
  (((List.finRange 6).filter fun j => j ∈ T).map fun j => (positions j).val+1).insertionSort (· ≤ ·)

theorem executableType_eq (positions : Fin 6 ↪ Fin v) (T : Finset (Fin 6)) :
    executableType positions T = canonicalType positions T := by
  have hn : (((List.finRange 6).filter fun j => j ∈ T).map
      fun j => (positions j).val+1).Nodup :=
    (List.nodup_finRange 6).filter _ |>.map (fun i j h =>
      positions.injective (Fin.ext (Nat.add_right_cancel h)))
  apply List.eq_of_perm_of_sorted (r := (· ≤ ·))
  · apply (List.perm_ext_iff_of_nodup
      ((List.perm_insertionSort _ _).nodup_iff.mpr hn)
      (Finset.sort_nodup _ _)).mpr
    intro n
    simp [executableType,canonicalType,List.mem_insertionSort,List.mem_finRange]
  · exact List.sorted_insertionSort _ _
  · exact Finset.sort_sorted _ _

theorem canonicalType_injective (positions : Fin 6 ↪ Fin v) :
    Function.Injective (canonicalType positions) := by
  intro A B h
  have hs := congrArg List.toFinset h
  simp only [canonicalType, Finset.sort_toFinset] at hs
  exact Finset.image_injective (fun i j hij =>
    positions.injective (Fin.ext (Nat.add_right_cancel hij))) hs

theorem position_fiber_count (H : Simple5Hypergraph (Fin v))
    (vertices positions : Fin 6 ↪ Fin v) (T : Finset (Fin 6)) :
    multiplicity H.edges (positionType vertices positions) (canonicalType positions T) =
      count H vertices T := by
  unfold multiplicity fiber count
  congr 1
  apply Finset.filter_congr
  intro e _
  change (canonicalType positions (lockSignature vertices e) = canonicalType positions T) ↔ _
  exact (canonicalType_injective positions).eq_iff

def rawProfile (positions : Fin 6 ↪ Fin v) (μ : Finset (Fin 6) → ℕ)
    (centers : List ℕ) : Numeric.Profile where
  v := v
  positions := canonicalType positions Finset.univ
  types := labels.map fun T => ⟨canonicalType positions T, μ T⟩
  correctionCenters := centers

def profile (positions : Fin 6 ↪ Fin v) (μ : Finset (Fin 6) → ℕ)
    (centers : List ℕ) : Numeric.Profile := pruneZero (rawProfile positions μ centers)

theorem raw_table (H : Simple5Hypergraph (Fin v)) (vertices positions : Fin 6 ↪ Fin v)
    (μ : Finset (Fin 6) → ℕ) (hμ : ∀ T, count H vertices T = μ T) (centers : List ℕ) :
    TableRealization H.edges (positionType vertices positions) (rawProfile positions μ centers) := by
  constructor
  · change ((labels.map (fun T => (⟨canonicalType positions T, μ T⟩ : Numeric.EdgeType))).map
      Numeric.EdgeType.locks).Nodup
    simpa only [List.map_map, Function.comp_def] using
      labels_nodup.map (canonicalType_injective positions)
  · intro e _
    apply List.mem_map.mpr
    refine ⟨⟨canonicalType positions (lockSignature vertices e), μ (lockSignature vertices e)⟩, ?_, rfl⟩
    exact List.mem_map.mpr ⟨lockSignature vertices e,mem_labels _,rfl⟩
  · intro t ht
    obtain ⟨T,_,rfl⟩ := List.mem_map.mp ht
    exact (position_fiber_count H vertices positions T).trans (hμ T)

/-- The actual-H table is built here; finite validity is checked by each caller. -/
theorem realizes_profile (H : Simple5Hypergraph (Fin v)) (vertices positions : Fin 6 ↪ Fin v)
    (μ : Finset (Fin 6) → ℕ) (hμ : ∀ T, count H vertices T = μ T) (centers : List ℕ)
    (valid : Numeric.validProfile (profile positions μ centers) 33) :
    RealizesProfile H vertices positions (profile positions μ centers) 33 := by
  refine ⟨rfl,valid,?_,table_pruneZero _ _ _ (raw_table H vertices positions μ hμ centers)⟩
  simp [profile, pruneZero, rawProfile, canonicalType]

end Aris4Math.ThirtyThree.TwentyThreeHighSixProfiles

#print axioms Aris4Math.ThirtyThree.TwentyThreeHighSixProfiles.realizes_profile

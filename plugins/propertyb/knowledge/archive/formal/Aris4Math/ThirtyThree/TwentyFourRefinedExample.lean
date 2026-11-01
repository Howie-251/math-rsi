import Aris4Math.ThirtyThree.RefinedDeletion
import Aris4Math.ThirtyThree.MultiLockRecovery
import Aris4Math.ThirtyThree.FiveLockClassification

/-! A concrete five-lock caller at 24 vertices. The sole large trace is
{0,2,3,4}; degrees are (6,6,7,7,7), and all lock-pair codegrees are one.
The two overlapping avoided-lock quotas at each high center prove a strict
bound. Source: round01/small-math/AVOIDED_LOCK_QUOTAS.json, group 13. -/
namespace Aris4Math.ThirtyThree.TwentyFourRefinedExample

open scoped BigOperators
open Aris4Math.TypeCounting
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.RefinedDeletion

def positionFn : Fin 5 → Fin 24 := ![11,12,13,14,15]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 5 ↪ Fin 24 := ⟨positionFn, positionFn_injective⟩

def p : Numeric.Profile := ⟨24, [12,13,14,15,16],
  [⟨[],7⟩, ⟨[12],4⟩, ⟨[13],2⟩, ⟨[12,13],1⟩,
   ⟨[14],5⟩, ⟨[13,14],1⟩, ⟨[15],5⟩, ⟨[13,15],1⟩,
   ⟨[16],5⟩, ⟨[13,16],1⟩, ⟨[12,14,15,16],1⟩], none, [14,15,16]⟩

def avoided : Fin 5 → Fin 2 → Finset (Fin 5) :=
  ![![∅,∅], ![∅,∅], ![{0,3,4},{0,1,3,4}],
    ![{0,2,4},{0,1,2,4}], ![{0,2,3},{0,1,2,3}]]
def multipliers : Fin 5 → Fin 2 → ℚ :=
  ![![0,0], ![0,0], ![55/8398,55/25194],
    ![55/8398,55/25194], ![55/8398,55/25194]]
def quotas : Fin 5 → Fin 2 → ℕ := ![![0,0], ![0,0], ![2,1], ![2,1], ![2,1]]
def loss (k : ℕ) : ℚ := if k ∈ [14,15,16] then 385/25194 else 0

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem certificates :
    Numeric.validProfile p 33 ∧
    (∑ k : Fin 24, min (Numeric.boundA p (k.val+1))
      (min (Numeric.boundB p (k.val+1)) (Numeric.boundC p (k.val+1)-loss (k.val+1)))) =
        (75163/75582 : ℚ) ∧
    ∀ j : Fin 5, (positions j).val+1 ∈ p.correctionCenters →
      (∀ i, 0 ≤ multipliers j i) ∧ (∀ i, j ∉ avoided j i) ∧
      (∀ i, quotas j i ≤
        (4 * avoidedCount p ((positions j).val+1) (avoidedPositions positions (avoided j i))
          + 2 - (24 - 1 - (avoided j i).card)) / 3) ∧
      loss ((positions j).val+1) ≤ (∑ i, (quotas j i : ℚ) * multipliers j i) -
        penaltySum p ((positions j).val+1)
          (fun i => avoidedPositions positions (avoided j i)) (multipliers j) := by
  unfold Numeric.validProfile
  decide +kernel

def labels : List (Finset (Fin 5)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{0,1,2},{3},{0,3},{1,3},{0,1,3},{2,3},{0,2,3},{1,2,3},{0,1,2,3},{4},{0,4},{1,4},{0,1,4},{2,4},{0,2,4},{1,2,4},{0,1,2,4},{3,4},{0,3,4},{1,3,4},{0,1,3,4},{2,3,4},{0,2,3,4},{1,2,3,4},{0,1,2,3,4}]

theorem labels_nodup : labels.Nodup := by decide +kernel
theorem labels_all : ∀ T : Finset (Fin 5), T ∈ labels := by decide +kernel

def degreeData (j : Fin 5) : ℕ := if j.val < 2 then 6 else 7

def low (T : Finset (Fin 5)) : ℕ :=
  if T = ∅ then 33 else if T.card = 1 then
    if 0 ∈ T ∨ 1 ∈ T then 6 else 7 else 1

def high (T : Finset (Fin 5)) : ℕ := if T = {0,2,3,4} then 1 else 0

/-- The concrete caller is case 14 of the complete labelled unit-pair domain. -/
theorem high_eq_case_fourteen : high = FiveLockClassification.high 14 := by
  funext T
  have h : ∀ T : Finset (Fin 5), high T = FiveLockClassification.high 14 T := by decide +kernel
  exact h T

def executableType (T : Finset (Fin 5)) : List ℕ :=
  (((List.finRange 5).filter fun j => j ∈ T).map fun j => (positions j).val+1).insertionSort (· ≤ ·)

theorem executableType_eq (T : Finset (Fin 5)) :
    executableType T = canonicalType positions T := by
  have hn : (((List.finRange 5).filter fun j => j ∈ T).map
      fun j => (positions j).val+1).Nodup :=
    (List.nodup_finRange 5).filter _ |>.map (fun i j h =>
      positions.injective (Fin.ext (Nat.add_right_cancel h)))
  apply List.eq_of_perm_of_sorted (r := (· ≤ ·))
  · apply (List.perm_ext_iff_of_nodup
      ((List.perm_insertionSort _ _).nodup_iff.mpr hn)
      (Finset.sort_nodup _ _)).mpr
    intro n
    simp [List.mem_insertionSort,List.mem_finRange]
  · exact List.sorted_insertionSort _ _
  · exact Finset.sort_sorted _ _

def recoveredProfile : Numeric.Profile :=
  TripleProfiles.pruneZero ⟨24, executableType Finset.univ,
    labels.map fun T => ⟨executableType T, recovered low high T⟩,
    none, [14,15,16]⟩

theorem recoveredProfile_eq : recoveredProfile =
    profile labels positions (recovered low high) [14,15,16] := by
  simp only [recoveredProfile, executableType_eq, profile, rawProfile]

set_option maxHeartbeats 0 in
set_option maxRecDepth 100000 in
theorem recoveredProfile_eq_p : recoveredProfile = p := by rfl

/-- The profile supplied to the probability caller is constructed from the
actual total, degrees, codegrees, and exact large traces of H. -/
theorem actual_profile (H : Simple5Hypergraph (Fin 24)) (vertices : Fin 5 ↪ Fin 24)
    (edges33 : H.edges.card = 33)
    (degrees : ∀ j, H.degree (vertices j) = degreeData j)
    (codegrees : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1)
    (large : ∀ T, 3 ≤ T.card → count H vertices T = high T) :
    RealizesProfile H vertices positions p 33 := by
  have hlow : ∀ T, T.card ≤ 2 → upperCount H vertices T = low T := by
    apply upper_eq_of_low_data
    · simpa only [low, if_pos rfl] using edges33.symm
    · intro i
      rw [degrees]
      fin_cases i <;> decide +kernel
    · intro i j hij
      rw [codegrees i j hij]
      simp [low, Finset.card_pair hij]
  rw [← recoveredProfile_eq_p, recoveredProfile_eq]
  apply realizes_recovered H vertices positions labels labels_nodup labels_all low high hlow large
  rw [← recoveredProfile_eq, recoveredProfile_eq_p]
  exact certificates.1

/-- A genuine 24-vertex local branch, with no certificate, probability, type
realizer, or quota premise left to the caller. The large-trace premise is the
structural branch that future selection/classification must supply. -/
theorem propertyB_of_mixed_quad_trace (H : Simple5Hypergraph (Fin 24))
    (vertices : Fin 5 ↪ Fin 24) (edges33 : H.edges.card = 33)
    (degrees : ∀ j, H.degree (vertices j) = degreeData j)
    (codegrees : ∀ i j, i ≠ j → H.codegree (vertices i) (vertices j) = 1)
    (large : ∀ T, 3 ≤ T.card → count H vertices T = high T) : PropertyB H := by
  have real := actual_profile H vertices edges33 degrees codegrees large
  apply propertyB_of_refined_deletion H vertices positions p real rfl loss
    avoided multipliers quotas
  · intro j hc
    exact (certificates.2.2 j hc).1
  · intro j hc
    exact (certificates.2.2 j hc).2.1
  · intro j hc
    exact (certificates.2.2 j hc).2.2.1
  · intro j hc
    exact (certificates.2.2 j hc).2.2.2
  · intro k hk
    exact if_neg hk
  · rw [certificates.2.1]
    norm_num

end Aris4Math.ThirtyThree.TwentyFourRefinedExample

#print axioms Aris4Math.ThirtyThree.TwentyFourRefinedExample.certificates

#print axioms Aris4Math.ThirtyThree.TwentyFourRefinedExample.propertyB_of_mixed_quad_trace

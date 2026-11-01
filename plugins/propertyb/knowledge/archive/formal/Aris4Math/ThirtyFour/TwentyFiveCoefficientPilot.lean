import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.CachedCoefficients16
namespace Aris4Math.ThirtyFour.TwentyFiveCoefficientPilot
open Aris4Math.ThirtyThree.MultiLockRecovery
open Aris4Math.ThirtyThree.TripleProfiles (pruneZero)
open LocalProfiles CachedRows
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
/- Saved q=5 bare witness 4423, with the smallest successful margin in that
bare batch. This theorem closes this actual trace input, not all 25-point H. -/
def positions : Fin 9 ↪ Fin 25 :=
  ⟨fun j => ⟨j.val+8,by omega⟩, fun i j h => Fin.ext (by
    have := congrArg Fin.val h; simp only at this; omega)⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{4},{0,4},{2,4},{3,4},{5},{0,1,2,3,5},{6},{0,6},{3,6},{5,6},{7},{0,7},{2,7},{5,7},{1,4,6,7},{8},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then ( if T={0} then 1 else if T={1} then 3 else if T={2} then 2 else if T={3} then 2 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 3 else if T={0,1,2,3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={1,4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile :=
  ⟨25,executableType positions Finset.univ,
    labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,16,17],[⟨[9],1⟩,⟨[10],3⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],3⟩,⟨[9,10,11,12,14],1⟩,⟨[15],2⟩,⟨[9,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[9,16],1⟩,⟨[11,16],1⟩,⟨[14,16],1⟩,⟨[10,13,15,16],1⟩,⟨[17],2⟩,⟨[9,17],1⟩,⟨[10,17],1⟩,⟨[13,14,17],1⟩,⟨[11,15,17],1⟩,⟨[12,16,17],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel

def locked (k : Fin 25) : Bool := decide (k.val+1 ∈ computed.positions)
def leftSlots (k : Fin 25) : Fin 17 :=
  ⟨Numeric.leftCount computed (k.val+1),by fin_cases k <;> decide +kernel⟩
def rightSlots (k : Fin 25) : Fin 17 :=
  ⟨Numeric.rightCount computed (k.val+1),by fin_cases k <;> decide +kernel⟩
def tableA (k : Fin 25) (last : Bool) (r : Fin 6) : ℚ :=
  CachedCoefficients16.edgeTable
    (CachedCoefficients16.index (locked k) (if last then leftSlots k else rightSlots k)) r
def tableC (k : Fin 25) (r q : Fin 6) : ℚ :=
  CachedCoefficients16.pairTable (CachedCoefficients16.index (locked k) (leftSlots k)) r q

theorem aCoeff_eq (k : Fin 25) (last : Bool) (r : Fin 6) :
    aCoeff computed (k.val+1) last r = tableA k last r := by
  unfold tableA
  rw [← CachedCoefficients16.edgeTable_eq]
  cases last <;> rfl

theorem cCoeff_eq (k : Fin 25) (r q : Fin 6) :
    cCoeff computed (k.val+1) r q = tableC k r q := by
  have geometry : Numeric.rightCount computed (k.val+1) =
      (if locked k then 16 else 15)-(leftSlots k).val := by fin_cases k <;> decide +kernel
  unfold tableC
  rw [← CachedCoefficients16.pairTable_eq]
  unfold cCoeff
  rw [geometry]
  rfl

/-- Only sparse integer masses and already checked coefficient lookups remain. -/
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (12869/12870 : ℚ) := by
  rw [p_eq_computed]
  simp only [cachedA,cachedC,cachedDiagonal]
  simp_rw [aCoeff_eq,cCoeff_eq]
  decide +kernel

theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (vertices : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H vertices T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H vertices positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Aris4Math.ThirtyFour.TwentyFiveCoefficientPilot
#print axioms Aris4Math.ThirtyFour.TwentyFiveCoefficientPilot.propertyB_of_counts

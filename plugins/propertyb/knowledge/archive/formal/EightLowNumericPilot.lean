import Aris4Math.ThirtyFour.CachedSparseApplication
namespace Aris4Math.ThirtyFour.EightLowPilot
open Aris4Math.ThirtyThree.MultiLockRecovery LocalProfiles CachedRows
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case1
def positionFn : Fin 9 → Fin 25 := ![9,22,10,14,11,13,12,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{4},{2,4},{0,3,4},{5},{2,5},{1,3,5},{4,5},{6},{0,6},{3,6},{1,4,6},{7},{1,7},{3,7},{0,5,7},{2,6,7},{8},{0,8},{1,8},{2,3,8},{5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={1,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={0,5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,23,24,25],[⟨[],6⟩,⟨[10],1⟩,⟨[23],1⟩,⟨[11],1⟩,⟨[10,11,23],1⟩,⟨[15],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[10,12,15],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[14,15,23],1⟩,⟨[12,14],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[13,15],1⟩,⟨[12,13,23],1⟩,⟨[24],1⟩,⟨[23,24],1⟩,⟨[15,24],1⟩,⟨[10,14,24],1⟩,⟨[11,13,24],1⟩,⟨[25],2⟩,⟨[10,25],1⟩,⟨[23,25],1⟩,⟨[11,15,25],1⟩,⟨[13,14,25],1⟩,⟨[12,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1
namespace Case1
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (2841/2860 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case1

#print axioms Case1.propertyB_of_counts
end Aris4Math.ThirtyFour.EightLowPilot

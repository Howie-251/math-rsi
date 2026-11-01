import Aris4Math.ThirtyFour.CachedSparseApplication
namespace Aris4Math.ThirtyFour.TwentyFiveNineLow
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles CachedRows
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case0
def positionFn : Fin 9 → Fin 25 := ![8,9,11,10,12,13,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{4},{0,3,4},{5},{1,3,5},{6},{2,3,6},{4,5,6},{7},{1,4,7},{2,5,7},{0,6,7},{8},{2,4,8},{0,5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={0,1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={0,3,4} then 1 else if T={5} then 2 else if T={1,3,5} then 1 else if T={6} then 2 else if T={2,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={1,4,7} then 1 else if T={2,5,7} then 1 else if T={0,6,7} then 1 else if T={8} then 2 else if T={2,4,8} then 1 else if T={0,5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],4⟩,⟨[9],2⟩,⟨[10],2⟩,⟨[12],2⟩,⟨[9,10,12],1⟩,⟨[11],2⟩,⟨[13],2⟩,⟨[9,11,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],2⟩,⟨[11,12,15],1⟩,⟨[13,14,15],1⟩,⟨[24],2⟩,⟨[10,13,24],1⟩,⟨[12,14,24],1⟩,⟨[9,15,24],1⟩,⟨[25],2⟩,⟨[12,13,25],1⟩,⟨[9,14,25],1⟩,⟨[10,15,25],1⟩,⟨[11,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case0

namespace Case1
def positionFn : Fin 9 → Fin 25 := ![10,13,8,22,9,12,11,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{4},{2,4},{0,3,4},{5},{2,5},{1,3,5},{4,5},{6},{0,6},{1,6},{2,3,6},{7},{0,7},{3,7},{1,4,7},{5,6,7},{8},{1,8},{3,8},{0,5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={1,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={3,7} then 1 else if T={1,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 1 else if T={1,8} then 1 else if T={3,8} then 1 else if T={0,5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],7⟩,⟨[11],1⟩,⟨[14],1⟩,⟨[9],1⟩,⟨[9,11,14],1⟩,⟨[23],1⟩,⟨[10],1⟩,⟨[9,10],1⟩,⟨[10,11,23],1⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[13,14,23],1⟩,⟨[10,13],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[12,14],1⟩,⟨[9,12,23],1⟩,⟨[24],1⟩,⟨[11,24],1⟩,⟨[23,24],1⟩,⟨[10,14,24],1⟩,⟨[12,13,24],1⟩,⟨[25],1⟩,⟨[14,25],1⟩,⟨[23,25],1⟩,⟨[11,13,25],1⟩,⟨[10,12,25],1⟩,⟨[9,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1

end Aris4Math.ThirtyFour.TwentyFiveNineLow

namespace Aris4Math.ThirtyFour.TwentyFiveNineLow
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles CachedRows
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case1
theorem value : (∑ k : Fin 25, min (cachedA p (k.val+1) true)
    (min (cachedA p (k.val+1) false) (cachedC p (k.val+1)))) = (2141/2145 : ℚ) := by
  rw [p_eq_computed]
  decide +kernel
theorem propertyB_of_counts (H : Simple5Hypergraph (Fin 25)) (f : Fin 9 ↪ Fin 25)
    (counts : ∀ T,count H f T=μ T) : PropertyB H := by
  apply CachedSparseApplication.propertyB_of_sparse_counts H f positions labels labels_nodup μ support counts
  · rw [← p_eq_profile]; exact valid
  · rw [← p_eq_profile,value]; norm_num
end Case1

end Aris4Math.ThirtyFour.TwentyFiveNineLow
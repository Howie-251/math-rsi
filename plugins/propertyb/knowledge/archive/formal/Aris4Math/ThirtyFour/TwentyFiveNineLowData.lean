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

namespace Case2
def positionFn : Fin 9 → Fin 25 := ![8,10,13,22,11,9,12,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{4},{2,4},{0,3,4},{5},{0,5},{1,3,5},{4,5},{6},{0,6},{1,6},{2,3,6},{7},{2,7},{3,7},{1,4,7},{5,6,7},{8},{1,8},{3,8},{2,5,8},{4,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={1,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 1 else if T={1,8} then 1 else if T={3,8} then 1 else if T={2,5,8} then 1 else if T={4,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],7⟩,⟨[9],1⟩,⟨[11],1⟩,⟨[14],1⟩,⟨[9,11,14],1⟩,⟨[23],1⟩,⟨[12],1⟩,⟨[12,14],1⟩,⟨[9,12,23],1⟩,⟨[10],1⟩,⟨[9,10],1⟩,⟨[10,11,23],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[11,13],1⟩,⟨[13,14,23],1⟩,⟨[24],1⟩,⟨[14,24],1⟩,⟨[23,24],1⟩,⟨[11,12,24],1⟩,⟨[10,13,24],1⟩,⟨[25],1⟩,⟨[11,25],1⟩,⟨[23,25],1⟩,⟨[10,14,25],1⟩,⟨[12,13,25],1⟩,⟨[9,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2

namespace Case3
def positionFn : Fin 9 → Fin 25 := ![10,8,12,23,9,11,13,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{2,3},{4},{1,4},{0,3,4},{5},{0,5},{1,3,5},{6},{0,6},{2,4,6},{5,6},{7},{1,7},{4,7},{2,5,7},{3,6,7},{8},{2,8},{3,8},{4,5,8},{1,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={4,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[11],1⟩,⟨[9],1⟩,⟨[13],1⟩,⟨[9,11,13],1⟩,⟨[24],1⟩,⟨[13,24],1⟩,⟨[10],1⟩,⟨[9,10],1⟩,⟨[10,11,24],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[9,12,24],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[10,13,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[10,15],1⟩,⟨[12,13,15],1⟩,⟨[14,15,24],1⟩,⟨[25],1⟩,⟨[13,25],1⟩,⟨[24,25],1⟩,⟨[10,12,25],1⟩,⟨[9,14,25],1⟩,⟨[11,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3

namespace Case4
def positionFn : Fin 9 → Fin 25 := ![8,11,10,12,14,9,13,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1,2},{2,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{1,3,5},{4,5},{0,6},{1,6},{3,6},{5,6},{0,7},{1,7},{3,7},{4,7},{2,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 10 else if T={0,1,2} then 1 else if T={2,3} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={1,3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={4,7} then 1 else if T={2,6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],10⟩,⟨[9,11,12],1⟩,⟨[11,13],1⟩,⟨[12,15],1⟩,⟨[11,15],1⟩,⟨[9,13,15],1⟩,⟨[9,10],1⟩,⟨[10,11],1⟩,⟨[10,12,13],1⟩,⟨[10,15],1⟩,⟨[9,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[10,14],1⟩,⟨[9,24],1⟩,⟨[12,24],1⟩,⟨[13,24],1⟩,⟨[15,24],1⟩,⟨[11,14,24],1⟩,⟨[9,25],1⟩,⟨[12,25],1⟩,⟨[11,25],1⟩,⟨[13,25],1⟩,⟨[14,15,25],1⟩,⟨[10,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4

namespace Case5
def positionFn : Fin 9 → Fin 25 := ![10,22,13,8,12,9,11,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1,2},{3},{1,3},{2,3},{4},{1,4},{2,4},{0,3,4},{5},{0,5},{2,5},{6},{0,6},{2,6},{1,5,6},{7},{0,7},{1,7},{3,5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],8⟩,⟨[11,14,23],1⟩,⟨[9],1⟩,⟨[9,23],1⟩,⟨[9,14],1⟩,⟨[13],1⟩,⟨[13,23],1⟩,⟨[13,14],1⟩,⟨[9,11,13],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[10,14],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[12,14],1⟩,⟨[10,12,23],1⟩,⟨[24],1⟩,⟨[11,24],1⟩,⟨[23,24],1⟩,⟨[9,10,24],1⟩,⟨[12,13,24],1⟩,⟨[25],1⟩,⟨[11,25],1⟩,⟨[23,25],1⟩,⟨[10,13,25],1⟩,⟨[9,12,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case5

namespace Case6
def positionFn : Fin 9 → Fin 25 := ![10,11,7,12,8,9,13,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1,2},{1,3},{2,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{4,5},{0,6},{2,6},{3,6},{1,5,6},{0,7},{1,7},{4,7},{3,5,7},{6,7},{0,8},{1,8},{3,8},{5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 10 else if T={0,1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={1,5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={4,7} then 1 else if T={3,5,7} then 1 else if T={6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[8,9,10,11,12,13,14,24,25],[⟨[],10⟩,⟨[8,11,12],1⟩,⟨[12,13],1⟩,⟨[8,13],1⟩,⟨[9,12],1⟩,⟨[8,9],1⟩,⟨[9,11,13],1⟩,⟨[10,11],1⟩,⟨[8,10],1⟩,⟨[9,10],1⟩,⟨[11,14],1⟩,⟨[8,14],1⟩,⟨[13,14],1⟩,⟨[10,12,14],1⟩,⟨[11,24],1⟩,⟨[12,24],1⟩,⟨[9,24],1⟩,⟨[10,13,24],1⟩,⟨[14,24],1⟩,⟨[11,25],1⟩,⟨[12,25],1⟩,⟨[13,25],1⟩,⟨[10,25],1⟩,⟨[9,14,25],1⟩,⟨[8,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6

namespace Case7
def positionFn : Fin 9 → Fin 25 := ![11,23,8,9,12,14,13,24,10]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,1,2},{3},{2,3},{4},{0,4},{2,4},{1,3,4},{5},{0,5},{3,5},{6},{0,6},{1,6},{2,5,6},{7},{0,7},{1,7},{4,5,7},{3,6,7},{8},{0,3,8},{1,5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={1,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={4,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={0,3,8} then 1 else if T={1,5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[24],1⟩,⟨[9],1⟩,⟨[9,12,24],1⟩,⟨[10],1⟩,⟨[9,10],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[9,13],1⟩,⟨[10,13,24],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[10,15],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[14,24],1⟩,⟨[9,14,15],1⟩,⟨[25],1⟩,⟨[12,25],1⟩,⟨[24,25],1⟩,⟨[13,15,25],1⟩,⟨[10,14,25],1⟩,⟨[11],2⟩,⟨[10,11,12],1⟩,⟨[11,15,24],1⟩,⟨[11,13,14],1⟩,⟨[9,11,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7

namespace Case8
def positionFn : Fin 9 → Fin 25 := ![8,13,9,11,10,14,12,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{1,3},{2,3},{4},{0,4},{2,4},{5},{0,5},{1,5},{6},{0,3,6},{4,5,6},{7},{1,4,7},{3,5,7},{2,6,7},{8},{3,4,8},{2,5,8},{1,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={6} then 2 else if T={0,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={1,4,7} then 1 else if T={3,5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 2 else if T={3,4,8} then 1 else if T={2,5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[9],1⟩,⟨[14],1⟩,⟨[10],1⟩,⟨[9,10,14],1⟩,⟨[12],1⟩,⟨[12,14],1⟩,⟨[10,12],1⟩,⟨[11],1⟩,⟨[9,11],1⟩,⟨[10,11],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[14,15],1⟩,⟨[13],2⟩,⟨[9,12,13],1⟩,⟨[11,13,15],1⟩,⟨[24],2⟩,⟨[11,14,24],1⟩,⟨[12,15,24],1⟩,⟨[10,13,24],1⟩,⟨[25],2⟩,⟨[11,12,25],1⟩,⟨[10,15,25],1⟩,⟨[13,14,25],1⟩,⟨[9,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8

namespace Case9
def positionFn : Fin 9 → Fin 25 := ![11,8,10,9,12,13,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1,2},{1,3},{2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{3,5},{4,5},{6},{1,6},{2,6},{0,3,6},{7},{0,7},{2,7},{1,4,7},{5,6,7},{8},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 9 else if T={0,1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={0,3,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],9⟩,⟨[9,11,12],1⟩,⟨[9,10],1⟩,⟨[10,11],1⟩,⟨[12,13],1⟩,⟨[11,13],1⟩,⟨[10,13],1⟩,⟨[12,14],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[11,15],1⟩,⟨[10,12,15],1⟩,⟨[24],1⟩,⟨[12,24],1⟩,⟨[11,24],1⟩,⟨[9,13,24],1⟩,⟨[14,15,24],1⟩,⟨[25],1⟩,⟨[12,25],1⟩,⟨[9,25],1⟩,⟨[11,14,25],1⟩,⟨[13,15,25],1⟩,⟨[10,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9

namespace Case10
def positionFn : Fin 9 → Fin 25 := ![8,14,12,11,13,10,9,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1,2},{1,3},{2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{2,5},{4,5},{6},{1,6},{2,6},{0,3,6},{7},{0,7},{3,7},{1,4,7},{5,6,7},{8},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 9 else if T={0,1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={0,3,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={3,7} then 1 else if T={1,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],9⟩,⟨[9,13,15],1⟩,⟨[12,15],1⟩,⟨[12,13],1⟩,⟨[9,14],1⟩,⟨[13,14],1⟩,⟨[12,14],1⟩,⟨[9,11],1⟩,⟨[11,15],1⟩,⟨[11,13],1⟩,⟨[11,14],1⟩,⟨[10],1⟩,⟨[10,15],1⟩,⟨[10,13],1⟩,⟨[9,10,12],1⟩,⟨[24],1⟩,⟨[9,24],1⟩,⟨[12,24],1⟩,⟨[14,15,24],1⟩,⟨[10,11,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[15,25],1⟩,⟨[11,12,25],1⟩,⟨[10,14,25],1⟩,⟨[13,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10

namespace Case11
def positionFn : Fin 9 → Fin 25 := ![8,11,10,14,13,12,9,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1,2},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,5},{6},{2,6},{0,3,6},{4,6},{7},{0,7},{3,7},{4,5,7},{1,6,7},{8},{0,8},{1,8},{3,4,8},{5,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 9 else if T={0,1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={2,6} then 1 else if T={0,3,6} then 1 else if T={4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={3,7} then 1 else if T={4,5,7} then 1 else if T={1,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,4,8} then 1 else if T={5,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],9⟩,⟨[9,11,12],1⟩,⟨[12,15],1⟩,⟨[11,15],1⟩,⟨[9,14],1⟩,⟨[12,14],1⟩,⟨[11,14],1⟩,⟨[9,13],1⟩,⟨[12,13],1⟩,⟨[11,13],1⟩,⟨[13,15],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[9,10,15],1⟩,⟨[10,14],1⟩,⟨[24],1⟩,⟨[9,24],1⟩,⟨[15,24],1⟩,⟨[13,14,24],1⟩,⟨[10,12,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[12,25],1⟩,⟨[14,15,25],1⟩,⟨[10,13,25],1⟩,⟨[11,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11

namespace Case12
def positionFn : Fin 9 → Fin 25 := ![7,11,12,14,8,9,10,24,13]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,1,2},{3},{1,3},{2,3},{4},{0,4},{5},{0,5},{4,5},{6},{0,6},{2,6},{1,4,6},{3,5,6},{7},{0,7},{1,7},{3,4,7},{2,5,7},{8},{0,3,8},{2,4,8},{1,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,4,6} then 1 else if T={3,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={2,5,7} then 1 else if T={8} then 2 else if T={0,3,8} then 1 else if T={2,4,8} then 1 else if T={1,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[8,9,10,11,12,13,14,15,25],[⟨[],7⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[8,12,13],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[9],1⟩,⟨[8,9],1⟩,⟨[10],1⟩,⟨[8,10],1⟩,⟨[9,10],1⟩,⟨[11],1⟩,⟨[8,11],1⟩,⟨[11,13],1⟩,⟨[9,11,12],1⟩,⟨[10,11,15],1⟩,⟨[25],1⟩,⟨[8,25],1⟩,⟨[12,25],1⟩,⟨[9,15,25],1⟩,⟨[10,13,25],1⟩,⟨[14],2⟩,⟨[8,14,15],1⟩,⟨[9,13,14],1⟩,⟨[10,12,14],1⟩,⟨[11,14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case12

namespace Case13
def positionFn : Fin 9 → Fin 25 := ![8,11,10,12,14,13,9,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{6},{2,6},{3,4,6},{5,6},{7},{1,7},{4,7},{3,5,7},{0,6,7},{8},{0,8},{3,8},{4,5,8},{1,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 9 else if T={0,1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={4,7} then 1 else if T={3,5,7} then 1 else if T={0,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={3,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],9⟩,⟨[9,11,12],1⟩,⟨[9,13],1⟩,⟨[12,13],1⟩,⟨[11,13],1⟩,⟨[9,15],1⟩,⟨[12,15],1⟩,⟨[11,15],1⟩,⟨[9,14],1⟩,⟨[12,14],1⟩,⟨[11,14],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[10,13,15],1⟩,⟨[10,14],1⟩,⟨[24],1⟩,⟨[12,24],1⟩,⟨[15,24],1⟩,⟨[13,14,24],1⟩,⟨[9,10,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[13,25],1⟩,⟨[14,15,25],1⟩,⟨[10,12,25],1⟩,⟨[11,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case13

namespace Case14
def positionFn : Fin 9 → Fin 25 := ![9,10,21,22,23,12,24,13,11]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1,2},{1,3},{2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{7},{0,7},{1,7},{3,5,7},{4,6,7},{8},{0,3,8},{1,4,8},{5,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 9 else if T={0,1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,3,8} then 1 else if T={1,4,8} then 1 else if T={5,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,22,23,24,25],[⟨[],9⟩,⟨[10,11,22],1⟩,⟨[11,23],1⟩,⟨[22,23],1⟩,⟨[10,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[13,22],1⟩,⟨[13,24],1⟩,⟨[10,25],1⟩,⟨[11,25],1⟩,⟨[22,25],1⟩,⟨[23,25],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[13,14,23],1⟩,⟨[14,24,25],1⟩,⟨[12],2⟩,⟨[10,12,23],1⟩,⟨[11,12,24],1⟩,⟨[12,13,25],1⟩,⟨[12,14,22],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case14

namespace Case15
def positionFn : Fin 9 → Fin 25 := ![22,11,13,8,12,9,10,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1,2},{3},{0,1,3},{2,3},{4},{1,4},{0,2,4},{3,4},{5},{0,5},{2,5},{6},{0,6},{2,6},{1,5,6},{7},{0,7},{1,7},{3,5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={1,2} then 1 else if T={3} then 1 else if T={0,1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],8⟩,⟨[12,14],1⟩,⟨[9],1⟩,⟨[9,12,23],1⟩,⟨[9,14],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[13,14,23],1⟩,⟨[9,13],1⟩,⟨[10],1⟩,⟨[10,23],1⟩,⟨[10,14],1⟩,⟨[11],1⟩,⟨[11,23],1⟩,⟨[11,14],1⟩,⟨[10,11,12],1⟩,⟨[24],1⟩,⟨[23,24],1⟩,⟨[12,24],1⟩,⟨[9,10,24],1⟩,⟨[11,13,24],1⟩,⟨[25],1⟩,⟨[23,25],1⟩,⟨[12,25],1⟩,⟨[10,13,25],1⟩,⟨[9,11,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case15

namespace Case16
def positionFn : Fin 9 → Fin 25 := ![12,11,13,8,9,14,10,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{3},{0,1,3},{4},{2,4},{3,4},{5},{1,5},{3,5},{0,4,5},{6},{0,6},{2,6},{1,4,6},{7},{0,7},{1,7},{2,3,7},{5,6,7},{8},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,1,3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,3,7} then 1 else if T={5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[13,14],1⟩,⟨[12,14],1⟩,⟨[9],1⟩,⟨[9,12,13],1⟩,⟨[10],1⟩,⟨[10,14],1⟩,⟨[9,10],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[9,15],1⟩,⟨[10,13,15],1⟩,⟨[11],1⟩,⟨[11,13],1⟩,⟨[11,14],1⟩,⟨[10,11,12],1⟩,⟨[24],1⟩,⟨[13,24],1⟩,⟨[12,24],1⟩,⟨[9,14,24],1⟩,⟨[11,15,24],1⟩,⟨[25],1⟩,⟨[13,25],1⟩,⟨[12,25],1⟩,⟨[14,15,25],1⟩,⟨[9,11,25],1⟩,⟨[10,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case16

namespace Case17
def positionFn : Fin 9 → Fin 25 := ![11,12,13,8,9,10,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{3},{0,1,3},{2,3},{4},{2,4},{3,4},{5},{1,5},{0,4,5},{6},{0,6},{1,4,6},{5,6},{7},{0,7},{1,7},{2,5,7},{3,6,7},{8},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={0,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,5,8} then 1 else if T={2,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[9],1⟩,⟨[9,12,13],1⟩,⟨[9,14],1⟩,⟨[10],1⟩,⟨[10,14],1⟩,⟨[9,10],1⟩,⟨[11],1⟩,⟨[11,13],1⟩,⟨[10,11,12],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[10,13,15],1⟩,⟨[11,15],1⟩,⟨[24],1⟩,⟨[12,24],1⟩,⟨[13,24],1⟩,⟨[11,14,24],1⟩,⟨[9,15,24],1⟩,⟨[25],1⟩,⟨[12,25],1⟩,⟨[13,25],1⟩,⟨[9,11,25],1⟩,⟨[14,15,25],1⟩,⟨[10,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case17

namespace Case18
def positionFn : Fin 9 → Fin 25 := ![14,13,11,23,10,8,9,24,12]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{3},{0,1,3},{2,3},{4},{1,4},{3,4},{5},{1,5},{0,4,5},{6},{0,6},{2,4,6},{5,6},{7},{0,7},{2,7},{3,5,7},{1,6,7},{8},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={0,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,5,7} then 1 else if T={1,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[12,15],1⟩,⟨[12,14],1⟩,⟨[24],1⟩,⟨[14,15,24],1⟩,⟨[12,24],1⟩,⟨[11],1⟩,⟨[11,14],1⟩,⟨[11,24],1⟩,⟨[9],1⟩,⟨[9,14],1⟩,⟨[9,11,15],1⟩,⟨[10],1⟩,⟨[10,15],1⟩,⟨[10,11,12],1⟩,⟨[9,10],1⟩,⟨[25],1⟩,⟨[15,25],1⟩,⟨[12,25],1⟩,⟨[9,24,25],1⟩,⟨[10,14,25],1⟩,⟨[13],1⟩,⟨[13,15],1⟩,⟨[13,14],1⟩,⟨[9,12,13],1⟩,⟨[10,13,24],1⟩,⟨[11,13,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case18

namespace Case19
def positionFn : Fin 9 → Fin 25 := ![11,10,13,8,9,12,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{3},{0,1,3},{4},{1,4},{3,4},{5},{0,5},{3,5},{2,4,5},{6},{1,6},{2,6},{0,4,6},{7},{0,7},{2,7},{1,5,7},{3,6,7},{8},{0,8},{1,8},{2,3,8},{5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,1,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={0,4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[12,14],1⟩,⟨[11,14],1⟩,⟨[9],1⟩,⟨[9,11,12],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[9,10],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[9,13],1⟩,⟨[10,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[14,15],1⟩,⟨[10,12,15],1⟩,⟨[24],1⟩,⟨[12,24],1⟩,⟨[14,24],1⟩,⟨[11,13,24],1⟩,⟨[9,15,24],1⟩,⟨[25],1⟩,⟨[12,25],1⟩,⟨[11,25],1⟩,⟨[9,14,25],1⟩,⟨[13,15,25],1⟩,⟨[10,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case19

namespace Case20
def positionFn : Fin 9 → Fin 25 := ![8,9,12,11,13,10,23,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{1,3},{0,2,3},{0,4},{1,4},{2,4},{3,4},{5},{3,5},{6},{2,6},{0,1,5,6},{7},{0,7},{3,7},{2,5,7},{4,6,7},{8},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={3,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,1,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={3,7} then 1 else if T={2,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[10,13],1⟩,⟨[10,12],1⟩,⟨[9,12,13],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[12,14],1⟩,⟨[11],2⟩,⟨[11,12],1⟩,⟨[24],2⟩,⟨[13,24],1⟩,⟨[9,10,11,24],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[12,15],1⟩,⟨[11,13,15],1⟩,⟨[14,15,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[13,25],1⟩,⟨[11,14,25],1⟩,⟨[12,24,25],1⟩,⟨[10,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case20

namespace Case21
def positionFn : Fin 9 → Fin 25 := ![10,13,8,12,9,14,11,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{1,2},{3},{1,3},{0,2,3},{4},{0,4},{2,4},{5},{0,5},{3,5},{6},{0,6},{1,6},{4,5,6},{7},{1,4,7},{2,5,7},{3,6,7},{8},{3,4,8},{1,5,8},{2,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={1,4,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={3,4,8} then 1 else if T={1,5,8} then 1 else if T={2,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[11,14],1⟩,⟨[9],1⟩,⟨[9,14],1⟩,⟨[13],1⟩,⟨[13,14],1⟩,⟨[9,11,13],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[9,10],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[12,14],1⟩,⟨[10,12,15],1⟩,⟨[24],2⟩,⟨[10,14,24],1⟩,⟨[9,15,24],1⟩,⟨[12,13,24],1⟩,⟨[25],2⟩,⟨[10,13,25],1⟩,⟨[14,15,25],1⟩,⟨[9,12,25],1⟩,⟨[11,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case21

namespace Case22
def positionFn : Fin 9 → Fin 25 := ![8,9,12,14,11,13,23,10,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,2},{0,3},{1,2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{7},{3,7},{2,4,7},{5,6,7},{8},{2,8},{3,5,8},{4,6,8},{0,1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={1} then 1 else if T={0,2} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={7} then 2 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 2 else if T={2,8} then 1 else if T={3,5,8} then 1 else if T={4,6,8} then 1 else if T={0,1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[10],1⟩,⟨[9,13],1⟩,⟨[9,15],1⟩,⟨[10,13,15],1⟩,⟨[9,12],1⟩,⟨[10,12],1⟩,⟨[12,15],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[12,14],1⟩,⟨[9,24],1⟩,⟨[10,24],1⟩,⟨[13,24],1⟩,⟨[15,24],1⟩,⟨[11],2⟩,⟨[11,15],1⟩,⟨[11,12,13],1⟩,⟨[11,14,24],1⟩,⟨[25],2⟩,⟨[13,25],1⟩,⟨[14,15,25],1⟩,⟨[12,24,25],1⟩,⟨[9,10,11,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case22

namespace Case23
def positionFn : Fin 9 → Fin 25 := ![23,8,9,10,13,11,12,24,14]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,2,3},{4},{3,4},{5},{1,5},{0,4,5},{6},{2,6},{1,4,6},{5,6},{7},{0,7},{4,7},{2,5,7},{3,6,7},{8},{2,4,8},{3,5,8},{0,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={0,1,2,3} then 1 else if T={4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={0,4,5} then 1 else if T={6} then 1 else if T={2,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={4,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={0,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],5⟩,⟨[24],2⟩,⟨[9],2⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[9,10,11,24],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[12,14,24],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[9,13,14],1⟩,⟨[12,13],1⟩,⟨[25],1⟩,⟨[24,25],1⟩,⟨[14,25],1⟩,⟨[10,12,25],1⟩,⟨[11,13,25],1⟩,⟨[15],2⟩,⟨[10,14,15],1⟩,⟨[11,12,15],1⟩,⟨[13,15,24],1⟩,⟨[9,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case23

namespace Case24
def positionFn : Fin 9 → Fin 25 := ![8,22,9,10,12,13,11,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,2,3},{4},{2,4},{3,4},{5},{1,5},{0,4,5},{6},{0,6},{1,4,6},{5,6},{7},{0,7},{1,7},{2,5,7},{3,6,7},{8},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={0,1,2,3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={0,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,5,8} then 1 else if T={2,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],6⟩,⟨[9],1⟩,⟨[23],1⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[9,10,11,23],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[14,23],1⟩,⟨[9,13,14],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[12,13,23],1⟩,⟨[12,14],1⟩,⟨[24],1⟩,⟨[9,24],1⟩,⟨[23,24],1⟩,⟨[10,14,24],1⟩,⟨[11,12,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[23,25],1⟩,⟨[11,14,25],1⟩,⟨[10,12,25],1⟩,⟨[13,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case24

namespace Case25
def positionFn : Fin 9 → Fin 25 := ![8,9,10,23,12,11,14,13,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,2,3},{2,4},{3,4},{1,5},{2,5},{3,5},{0,4,5},{0,6},{1,6},{3,6},{4,6},{0,7},{1,7},{2,7},{4,7},{5,6,7},{8},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={0,1,2,3} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[24],1⟩,⟨[9,10,11,24],1⟩,⟨[11,13],1⟩,⟨[13,24],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[12,24],1⟩,⟨[9,12,13],1⟩,⟨[9,15],1⟩,⟨[10,15],1⟩,⟨[15,24],1⟩,⟨[13,15],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[13,14],1⟩,⟨[12,14,15],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[10,13,25],1⟩,⟨[12,25],1⟩,⟨[11,15,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case25

namespace Case26
def positionFn : Fin 9 → Fin 25 := ![8,9,10,23,11,14,12,13,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{2},{3},{0,1,2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{3,5},{2,4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,7},{4,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 9 else if T={2} then 1 else if T={3} then 1 else if T={0,1,2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={2,4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={4,7} then 1 else if T={3,6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],9⟩,⟨[11],1⟩,⟨[24],1⟩,⟨[9,10,11,24],1⟩,⟨[9,12],1⟩,⟨[10,12],1⟩,⟨[12,24],1⟩,⟨[9,15],1⟩,⟨[10,15],1⟩,⟨[15,24],1⟩,⟨[11,12,15],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[13,15],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14,24],1⟩,⟨[9,25],1⟩,⟨[10,25],1⟩,⟨[11,25],1⟩,⟨[24,25],1⟩,⟨[12,13,25],1⟩,⟨[14,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case26

namespace Case27
def positionFn : Fin 9 → Fin 25 := ![22,8,9,10,11,13,12,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,2,3},{4},{1,4},{5},{0,5},{4,5},{6},{1,6},{3,6},{0,4,6},{2,5,6},{7},{0,7},{2,7},{3,4,7},{1,5,7},{8},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={0,1,2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={0,4,6} then 1 else if T={2,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={1,5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],6⟩,⟨[23],1⟩,⟨[9],1⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[9,10,11,23],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[14],1⟩,⟨[14,23],1⟩,⟨[12,14],1⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[11,13],1⟩,⟨[12,13,23],1⟩,⟨[10,13,14],1⟩,⟨[24],1⟩,⟨[23,24],1⟩,⟨[10,24],1⟩,⟨[11,12,24],1⟩,⟨[9,14,24],1⟩,⟨[25],1⟩,⟨[23,25],1⟩,⟨[9,25],1⟩,⟨[10,12,25],1⟩,⟨[11,14,25],1⟩,⟨[13,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case27

namespace Case28
def positionFn : Fin 9 → Fin 25 := ![8,9,10,23,12,13,11,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,2,3},{1,4},{3,4},{0,5},{2,5},{4,5},{1,6},{2,6},{3,6},{0,4,6},{5,6},{0,7},{2,7},{3,7},{4,7},{1,5,7},{8},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={0,1,2,3} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={4,7} then 1 else if T={1,5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[24],1⟩,⟨[9,10,11,24],1⟩,⟨[10,13],1⟩,⟨[13,24],1⟩,⟨[9,14],1⟩,⟨[11,14],1⟩,⟨[13,14],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[12,24],1⟩,⟨[9,12,13],1⟩,⟨[12,14],1⟩,⟨[9,15],1⟩,⟨[11,15],1⟩,⟨[15,24],1⟩,⟨[13,15],1⟩,⟨[10,14,15],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[10,25],1⟩,⟨[11,13,25],1⟩,⟨[14,24,25],1⟩,⟨[12,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case28

namespace Case29
def positionFn : Fin 9 → Fin 25 := ![22,8,9,10,12,13,11,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,1,2,3},{4},{0,4},{5},{0,5},{4,5},{6},{0,6},{3,6},{1,4,6},{2,5,6},{7},{0,7},{1,7},{2,4,7},{3,5,7},{8},{0,8},{2,8},{3,4,8},{1,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={0,1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={2,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={3,5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={1,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],6⟩,⟨[9],2⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[9,10,11,23],1⟩,⟨[13],1⟩,⟨[13,23],1⟩,⟨[14],1⟩,⟨[14,23],1⟩,⟨[13,14],1⟩,⟨[12],1⟩,⟨[12,23],1⟩,⟨[11,12],1⟩,⟨[9,12,13],1⟩,⟨[10,12,14],1⟩,⟨[24],1⟩,⟨[23,24],1⟩,⟨[9,24],1⟩,⟨[10,13,24],1⟩,⟨[11,14,24],1⟩,⟨[25],1⟩,⟨[23,25],1⟩,⟨[10,25],1⟩,⟨[11,13,25],1⟩,⟨[9,14,25],1⟩,⟨[12,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case29

namespace Case30
def positionFn : Fin 9 → Fin 25 := ![8,23,9,10,12,11,13,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,2,3},{0,4},{1,4},{2,4},{3,4},{5},{2,5},{3,5},{6},{1,6},{3,6},{0,5,6},{7},{0,7},{2,7},{1,5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={0,1,2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={0,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9],1⟩,⟨[24],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[9,10,11,24],1⟩,⟨[9,13],1⟩,⟨[13,24],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[14],1⟩,⟨[14,24],1⟩,⟨[11,14],1⟩,⟨[9,12,14],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[10,15],1⟩,⟨[12,15,24],1⟩,⟨[13,14,15],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[24,25],1⟩,⟨[12,13,25],1⟩,⟨[10,14,25],1⟩,⟨[11,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case30

namespace Case31
def positionFn : Fin 9 → Fin 25 := ![23,8,9,10,11,13,24,12,14]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,2,3},{4},{0,4},{3,4},{5},{0,5},{1,5},{6},{0,6},{2,6},{4,5,6},{7},{1,4,7},{2,5,7},{3,6,7},{8},{2,4,8},{3,5,8},{1,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={0,1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={1,4,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],5⟩,⟨[24],1⟩,⟨[9],2⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[9,10,11,24],1⟩,⟨[12],1⟩,⟨[12,24],1⟩,⟨[11,12],1⟩,⟨[14],1⟩,⟨[14,24],1⟩,⟨[9,14],1⟩,⟨[25],1⟩,⟨[24,25],1⟩,⟨[10,25],1⟩,⟨[12,14,25],1⟩,⟨[13],2⟩,⟨[9,12,13],1⟩,⟨[10,13,14],1⟩,⟨[11,13,25],1⟩,⟨[15],2⟩,⟨[10,12,15],1⟩,⟨[11,14,15],1⟩,⟨[9,15,25],1⟩,⟨[13,15,24],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case31

namespace Case32
def positionFn : Fin 9 → Fin 25 := ![8,9,10,13,22,23,24,11,12]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,2,3},{4},{3,4},{5},{1,5},{6},{2,6},{0,4,5,6},{7},{0,7},{1,4,7},{2,5,7},{3,6,7},{8},{0,8},{2,4,8},{3,5,8},{1,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={0,1,2,3} then 1 else if T={4} then 2 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,4,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,4,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={1,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],4⟩,⟨[9],2⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[14],2⟩,⟨[9,10,11,14],1⟩,⟨[23],2⟩,⟨[14,23],1⟩,⟨[24],2⟩,⟨[10,24],1⟩,⟨[25],2⟩,⟨[11,25],1⟩,⟨[9,23,24,25],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[10,12,23],1⟩,⟨[11,12,24],1⟩,⟨[12,14,25],1⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[11,13,23],1⟩,⟨[13,14,24],1⟩,⟨[10,13,25],1⟩,⟨[12,13],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case32

namespace Case33
def positionFn : Fin 9 → Fin 25 := ![8,9,10,13,22,23,24,11,12]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,2,3},{4},{3,4},{5},{1,5},{6},{2,6},{0,4,5,6},{7},{1,4,7},{2,5,7},{3,6,7},{8},{2,4,8},{3,5,8},{1,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 3 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={0,1,2,3} then 1 else if T={4} then 2 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,4,5,6} then 1 else if T={7} then 2 else if T={1,4,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],3⟩,⟨[9],3⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[14],2⟩,⟨[9,10,11,14],1⟩,⟨[23],2⟩,⟨[14,23],1⟩,⟨[24],2⟩,⟨[10,24],1⟩,⟨[25],2⟩,⟨[11,25],1⟩,⟨[9,23,24,25],1⟩,⟨[12],2⟩,⟨[10,12,23],1⟩,⟨[11,12,24],1⟩,⟨[12,14,25],1⟩,⟨[13],2⟩,⟨[11,13,23],1⟩,⟨[13,14,24],1⟩,⟨[10,13,25],1⟩,⟨[9,12,13],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case33

namespace Case34
def positionFn : Fin 9 → Fin 25 := ![10,22,8,11,9,23,24,13,12]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,1,2,3},{4},{0,4},{3,4},{5},{0,5},{2,5},{6},{0,6},{2,6},{3,6},{1,4,5,6},{0,7},{1,7},{3,7},{2,4,7},{5,7},{0,8},{1,8},{2,8},{4,8},{3,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={0,1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={1,4,5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={4,8} then 1 else if T={3,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],7⟩,⟨[23],2⟩,⟨[9],1⟩,⟨[12],1⟩,⟨[9,11,12,23],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[10,12],1⟩,⟨[24],1⟩,⟨[11,24],1⟩,⟨[9,24],1⟩,⟨[25],1⟩,⟨[11,25],1⟩,⟨[9,25],1⟩,⟨[12,25],1⟩,⟨[10,23,24,25],1⟩,⟨[11,14],1⟩,⟨[14,23],1⟩,⟨[12,14],1⟩,⟨[9,10,14],1⟩,⟨[14,24],1⟩,⟨[11,13],1⟩,⟨[13,23],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[12,13,24],1⟩,⟨[13,14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case34

namespace Case35
def positionFn : Fin 9 → Fin 25 := ![8,23,9,10,13,11,12,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,1,2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{7},{0,7},{2,7},{1,4,7},{5,6,7},{8},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={0,1,2,3} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[24],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[9,10,11,24],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[9,12],1⟩,⟨[12,24],1⟩,⟨[11,12],1⟩,⟨[12,14],1⟩,⟨[9,13],1⟩,⟨[13,24],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[10,15],1⟩,⟨[14,15,24],1⟩,⟨[12,13,15],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[24,25],1⟩,⟨[10,12,25],1⟩,⟨[13,14,25],1⟩,⟨[11,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case35

namespace Case36
def positionFn : Fin 9 → Fin 25 := ![8,10,11,23,9,13,14,24,12]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,2,3},{4},{1,4},{2,4},{3,4},{5},{0,5},{2,5},{3,5},{6},{0,6},{1,6},{3,6},{7},{0,7},{1,7},{2,7},{4,5,6,7},{8},{0,4,8},{1,5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={0,1,2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={4,5,6,7} then 1 else if T={8} then 2 else if T={0,4,8} then 1 else if T={1,5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[9],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[24],1⟩,⟨[9,11,12,24],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[10,12],1⟩,⟨[10,24],1⟩,⟨[14],1⟩,⟨[9,14],1⟩,⟨[12,14],1⟩,⟨[14,24],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[11,15],1⟩,⟨[15,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[11,25],1⟩,⟨[12,25],1⟩,⟨[10,14,15,25],1⟩,⟨[13],2⟩,⟨[9,10,13],1⟩,⟨[11,13,14],1⟩,⟨[12,13,15],1⟩,⟨[13,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case36

namespace Case37
def positionFn : Fin 9 → Fin 25 := ![11,10,12,13,8,14,9,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{4},{0,1,4},{2,4},{3,4},{5},{0,5},{1,5},{6},{1,6},{3,6},{2,5,6},{7},{0,7},{2,7},{3,5,7},{4,6,7},{8},{2,3,8},{4,5,8},{0,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={2,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={2,3,8} then 1 else if T={4,5,8} then 1 else if T={0,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[12,13],1⟩,⟨[11,13],1⟩,⟨[12,14],1⟩,⟨[11,14],1⟩,⟨[9],1⟩,⟨[9,11,12],1⟩,⟨[9,13],1⟩,⟨[9,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[11,15],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[10,14],1⟩,⟨[10,13,15],1⟩,⟨[24],1⟩,⟨[12,24],1⟩,⟨[13,24],1⟩,⟨[14,15,24],1⟩,⟨[9,10,24],1⟩,⟨[25],2⟩,⟨[13,14,25],1⟩,⟨[9,15,25],1⟩,⟨[10,12,25],1⟩,⟨[11,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case37

namespace Case38
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,8,14,9,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1,2},{0,3},{1,3},{2,3},{4},{0,1,4},{2,4},{3,4},{5},{0,5},{1,5},{6},{0,6},{2,6},{3,5,6},{7},{0,7},{1,7},{2,5,7},{4,6,7},{8},{0,2,8},{4,5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,2,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[9],1⟩,⟨[9,11,12],1⟩,⟨[9,13],1⟩,⟨[9,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[10,13],1⟩,⟨[10,14,15],1⟩,⟨[24],1⟩,⟨[11,24],1⟩,⟨[12,24],1⟩,⟨[13,15,24],1⟩,⟨[9,10,24],1⟩,⟨[25],2⟩,⟨[11,13,25],1⟩,⟨[9,15,25],1⟩,⟨[10,12,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case38

namespace Case39
def positionFn : Fin 9 → Fin 25 := ![21,9,22,23,10,13,24,12,11]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{2,3},{4},{0,1,4},{3,4},{5},{1,5},{4,5},{6},{0,6},{2,6},{3,5,6},{7},{0,7},{1,7},{2,5,7},{4,6,7},{8},{2,4,8},{0,5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={2,4,8} then 1 else if T={0,5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,22,23,24,25],[⟨[],8⟩,⟨[22,23],1⟩,⟨[10,23],1⟩,⟨[22,24],1⟩,⟨[10,24],1⟩,⟨[23,24],1⟩,⟨[11],1⟩,⟨[10,11,22],1⟩,⟨[11,24],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[25],1⟩,⟨[22,25],1⟩,⟨[23,25],1⟩,⟨[14,24,25],1⟩,⟨[13],1⟩,⟨[13,22],1⟩,⟨[10,13],1⟩,⟨[13,14,23],1⟩,⟨[11,13,25],1⟩,⟨[12],2⟩,⟨[11,12,23],1⟩,⟨[12,14,22],1⟩,⟨[10,12,25],1⟩,⟨[12,13,24],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case39

namespace Case40
def positionFn : Fin 9 → Fin 25 := ![8,12,11,13,9,10,23,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{0,2},{0,3},{1,3},{2,3},{4},{1,2,4},{3,4},{5},{2,5},{6},{1,6},{0,4,5,6},{7},{0,7},{2,7},{1,5,7},{3,6,7},{8},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,1} then 1 else if T={0,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={1,2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,4,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,5,8} then 1 else if T={2,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9,13],1⟩,⟨[9,12],1⟩,⟨[9,14],1⟩,⟨[13,14],1⟩,⟨[12,14],1⟩,⟨[10],2⟩,⟨[10,12,13],1⟩,⟨[10,14],1⟩,⟨[11],2⟩,⟨[11,12],1⟩,⟨[24],2⟩,⟨[13,24],1⟩,⟨[9,10,11,24],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[12,15],1⟩,⟨[11,13,15],1⟩,⟨[14,15,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[13,25],1⟩,⟨[11,14,25],1⟩,⟨[12,24,25],1⟩,⟨[10,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case40

namespace Case41
def positionFn : Fin 9 → Fin 25 := ![22,8,9,12,10,11,13,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,3},{1,3},{2,3},{4},{0,1,2,4},{3,4},{5},{0,5},{2,5},{6},{0,6},{2,6},{1,5,6},{7},{0,7},{1,7},{3,5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={1} then 1 else if T={2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,1,2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],7⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[13,23],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[11],2⟩,⟨[9,10,11,23],1⟩,⟨[11,13],1⟩,⟨[12],1⟩,⟨[12,23],1⟩,⟨[10,12],1⟩,⟨[14],1⟩,⟨[14,23],1⟩,⟨[10,14],1⟩,⟨[9,12,14],1⟩,⟨[24],1⟩,⟨[23,24],1⟩,⟨[9,24],1⟩,⟨[12,13,24],1⟩,⟨[11,14,24],1⟩,⟨[25],1⟩,⟨[23,25],1⟩,⟨[9,25],1⟩,⟨[11,12,25],1⟩,⟨[13,14,25],1⟩,⟨[10,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case41

namespace Case42
def positionFn : Fin 9 → Fin 25 := ![10,13,11,8,12,9,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{0,2},{1,2},{3},{4},{0,3,4},{5},{1,3,5},{6},{2,3,6},{4,5,6},{7},{1,4,7},{2,5,7},{0,6,7},{8},{2,4,8},{0,5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={0,3,4} then 1 else if T={5} then 2 else if T={1,3,5} then 1 else if T={6} then 2 else if T={2,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={1,4,7} then 1 else if T={2,5,7} then 1 else if T={0,6,7} then 1 else if T={8} then 2 else if T={2,4,8} then 1 else if T={0,5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],5⟩,⟨[11],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[12,14],1⟩,⟨[9],2⟩,⟨[13],2⟩,⟨[9,11,13],1⟩,⟨[10],2⟩,⟨[9,10,14],1⟩,⟨[15],2⟩,⟨[9,12,15],1⟩,⟨[10,13,15],1⟩,⟨[24],2⟩,⟨[13,14,24],1⟩,⟨[10,12,24],1⟩,⟨[11,15,24],1⟩,⟨[25],2⟩,⟨[12,13,25],1⟩,⟨[10,11,25],1⟩,⟨[14,15,25],1⟩,⟨[9,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case42

namespace Case43
def positionFn : Fin 9 → Fin 25 := ![11,12,13,10,8,9,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{0,2},{1,2},{3},{4},{2,4},{0,3,4},{5},{2,5},{1,3,5},{4,5},{6},{0,6},{3,6},{1,4,6},{7},{1,7},{3,7},{0,5,7},{2,6,7},{8},{0,8},{1,8},{2,3,8},{5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={1,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={0,5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[12,13],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[11],1⟩,⟨[9],1⟩,⟨[9,14],1⟩,⟨[9,11,12],1⟩,⟨[10],1⟩,⟨[10,14],1⟩,⟨[10,11,13],1⟩,⟨[9,10],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[11,15],1⟩,⟨[9,13,15],1⟩,⟨[24],1⟩,⟨[13,24],1⟩,⟨[11,24],1⟩,⟨[10,12,24],1⟩,⟨[14,15,24],1⟩,⟨[25],1⟩,⟨[12,25],1⟩,⟨[13,25],1⟩,⟨[11,14,25],1⟩,⟨[10,15,25],1⟩,⟨[9,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case43

namespace Case44
def positionFn : Fin 9 → Fin 25 := ![11,14,12,10,8,13,23,9,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{0,2},{1,2},{3},{2,3},{4},{2,4},{0,3,4},{5},{0,5},{1,3,5},{6},{0,6},{1,4,6},{5,6},{7},{1,7},{4,7},{2,5,7},{3,6,7},{8},{1,8},{3,8},{4,5,8},{2,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={4,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={1,8} then 1 else if T={3,8} then 1 else if T={4,5,8} then 1 else if T={2,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[12,15],1⟩,⟨[12,13],1⟩,⟨[13,15],1⟩,⟨[11],1⟩,⟨[11,13],1⟩,⟨[9],1⟩,⟨[9,13],1⟩,⟨[9,11,12],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[11,14,15],1⟩,⟨[24],1⟩,⟨[12,24],1⟩,⟨[9,15,24],1⟩,⟨[14,24],1⟩,⟨[10],1⟩,⟨[10,15],1⟩,⟨[9,10],1⟩,⟨[10,13,14],1⟩,⟨[10,11,24],1⟩,⟨[25],1⟩,⟨[15,25],1⟩,⟨[11,25],1⟩,⟨[9,14,25],1⟩,⟨[13,24,25],1⟩,⟨[10,12,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case44

namespace Case45
def positionFn : Fin 9 → Fin 25 := ![12,11,14,10,13,8,9,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{0,2},{1,2},{3},{2,3},{4},{1,4},{0,3,4},{5},{0,5},{1,3,5},{6},{0,6},{2,4,6},{5,6},{7},{1,7},{4,7},{2,5,7},{3,6,7},{8},{2,8},{3,8},{4,5,8},{1,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={4,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[12,13],1⟩,⟨[13,15],1⟩,⟨[12,15],1⟩,⟨[11],1⟩,⟨[11,15],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[11,13,14],1⟩,⟨[9],1⟩,⟨[9,13],1⟩,⟨[9,11,12],1⟩,⟨[10],1⟩,⟨[10,13],1⟩,⟨[10,14,15],1⟩,⟨[9,10],1⟩,⟨[24],1⟩,⟨[12,24],1⟩,⟨[14,24],1⟩,⟨[9,15,24],1⟩,⟨[10,11,24],1⟩,⟨[25],1⟩,⟨[15,25],1⟩,⟨[11,25],1⟩,⟨[9,14,25],1⟩,⟨[10,12,25],1⟩,⟨[13,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case45

namespace Case46
def positionFn : Fin 9 → Fin 25 := ![8,9,10,12,14,11,13,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{2,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{1,3,5},{4,5},{0,6},{1,6},{3,6},{5,6},{0,7},{1,7},{3,7},{4,7},{2,6,7},{8},{0,1,2,8},{3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={2,3} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={1,3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={4,7} then 1 else if T={2,6,7} then 1 else if T={8} then 2 else if T={0,1,2,8} then 1 else if T={3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[11,13],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[9,13,15],1⟩,⟨[9,12],1⟩,⟨[11,12],1⟩,⟨[10,12,13],1⟩,⟨[12,15],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[12,14],1⟩,⟨[9,24],1⟩,⟨[10,24],1⟩,⟨[13,24],1⟩,⟨[15,24],1⟩,⟨[11,14,24],1⟩,⟨[25],2⟩,⟨[9,10,11,25],1⟩,⟨[13,25],1⟩,⟨[14,15,25],1⟩,⟨[12,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case46

namespace Case47
def positionFn : Fin 9 → Fin 25 := ![11,12,13,8,10,14,9,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{0,2},{1,2},{3},{4},{2,4},{1,3,4},{5},{1,5},{0,3,5},{4,5},{6},{2,6},{3,6},{0,4,6},{7},{0,7},{3,7},{2,5,7},{1,6,7},{8},{0,8},{1,8},{2,3,8},{5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={1,3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={0,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={0,4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={3,7} then 1 else if T={2,5,7} then 1 else if T={1,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[12,13],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[9],1⟩,⟨[11],1⟩,⟨[11,14],1⟩,⟨[9,11,13],1⟩,⟨[15],1⟩,⟨[13,15],1⟩,⟨[9,12,15],1⟩,⟨[11,15],1⟩,⟨[10],1⟩,⟨[10,14],1⟩,⟨[9,10],1⟩,⟨[10,11,12],1⟩,⟨[24],1⟩,⟨[12,24],1⟩,⟨[9,24],1⟩,⟨[14,15,24],1⟩,⟨[10,13,24],1⟩,⟨[25],1⟩,⟨[12,25],1⟩,⟨[13,25],1⟩,⟨[9,14,25],1⟩,⟨[10,15,25],1⟩,⟨[11,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case47

namespace Case48
def positionFn : Fin 9 → Fin 25 := ![8,9,10,14,11,12,13,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,3},{2,3},{0,4},{2,4},{1,3,4},{0,5},{1,5},{3,5},{4,5},{0,6},{1,6},{2,6},{4,6},{7},{0,1,2,7},{3,7},{5,6,7},{8},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={1} then 1 else if T={2} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={1,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={7} then 2 else if T={0,1,2,7} then 1 else if T={3,7} then 1 else if T={5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[9,15],1⟩,⟨[11,15],1⟩,⟨[9,12],1⟩,⟨[11,12],1⟩,⟨[10,12,15],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[13,15],1⟩,⟨[12,13],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[24],2⟩,⟨[9,10,11,24],1⟩,⟨[15,24],1⟩,⟨[13,14,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[10,25],1⟩,⟨[11,13,25],1⟩,⟨[14,15,25],1⟩,⟨[12,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case48

namespace Case49
def positionFn : Fin 9 → Fin 25 := ![8,22,12,9,10,11,13,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{3},{2,3},{4},{2,4},{0,1,3,4},{5},{0,5},{1,5},{6},{0,6},{1,6},{2,5,6},{7},{0,7},{1,7},{3,5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={0,1,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],7⟩,⟨[9,13],1⟩,⟨[13,23],1⟩,⟨[10],2⟩,⟨[10,13],1⟩,⟨[11],2⟩,⟨[11,13],1⟩,⟨[9,10,11,23],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[12,23],1⟩,⟨[14],1⟩,⟨[9,14],1⟩,⟨[14,23],1⟩,⟨[12,13,14],1⟩,⟨[24],1⟩,⟨[9,24],1⟩,⟨[23,24],1⟩,⟨[10,12,24],1⟩,⟨[11,14,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[23,25],1⟩,⟨[11,12,25],1⟩,⟨[10,14,25],1⟩,⟨[13,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case49

namespace Case50
def positionFn : Fin 9 → Fin 25 := ![8,9,22,10,13,11,12,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{2,3},{4},{2,4},{0,1,3,4},{5},{1,5},{6},{1,6},{0,2,5,6},{7},{0,7},{3,5,7},{4,6,7},{8},{0,8},{4,5,8},{3,6,8},{1,2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={0,1,3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,2,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={1,2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],3⟩,⟨[9],2⟩,⟨[10],2⟩,⟨[23],2⟩,⟨[11],2⟩,⟨[11,23],1⟩,⟨[14],2⟩,⟨[14,23],1⟩,⟨[9,10,11,14],1⟩,⟨[12],2⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[10,13],1⟩,⟨[9,12,13,23],1⟩,⟨[24],2⟩,⟨[9,24],1⟩,⟨[11,12,24],1⟩,⟨[13,14,24],1⟩,⟨[25],2⟩,⟨[9,25],1⟩,⟨[12,14,25],1⟩,⟨[11,13,25],1⟩,⟨[10,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case50

namespace Case51
def positionFn : Fin 9 → Fin 25 := ![8,22,23,10,11,12,13,9,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{2,3},{4},{2,4},{0,1,3,4},{5},{1,5},{4,5},{6},{1,6},{3,6},{0,2,5,6},{7},{0,7},{4,7},{3,5,7},{6,7},{8},{0,8},{3,8},{5,8},{4,6,8},{1,2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={0,1,3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={0,2,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={4,7} then 1 else if T={3,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={1,2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],5⟩,⟨[9],2⟩,⟨[23],2⟩,⟨[24],2⟩,⟨[11],1⟩,⟨[11,24],1⟩,⟨[12],1⟩,⟨[12,24],1⟩,⟨[9,11,12,23],1⟩,⟨[13],1⟩,⟨[13,23],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[14,23],1⟩,⟨[11,14],1⟩,⟨[9,13,14,24],1⟩,⟨[10],1⟩,⟨[9,10],1⟩,⟨[10,12],1⟩,⟨[10,11,13],1⟩,⟨[10,14],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[11,25],1⟩,⟨[13,25],1⟩,⟨[12,14,25],1⟩,⟨[10,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case51

namespace Case52
def positionFn : Fin 9 → Fin 25 := ![11,22,8,9,12,23,24,10,13]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{2,3},{4},{2,4},{0,1,3,4},{5},{0,5},{6},{0,6},{1,2,5,6},{7},{0,7},{1,7},{3,5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={1} then 2 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={0,1,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,2,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],5⟩,⟨[23],2⟩,⟨[9],1⟩,⟨[9,12],1⟩,⟨[10],2⟩,⟨[9,10],1⟩,⟨[13],2⟩,⟨[9,13],1⟩,⟨[10,12,13,23],1⟩,⟨[24],2⟩,⟨[12,24],1⟩,⟨[25],2⟩,⟨[12,25],1⟩,⟨[9,23,24,25],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[11,23],1⟩,⟨[10,11,24],1⟩,⟨[11,13,25],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[14,23],1⟩,⟨[13,14,24],1⟩,⟨[10,14,25],1⟩,⟨[9,11,14],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case52

namespace Case53
def positionFn : Fin 9 → Fin 25 := ![23,8,13,9,10,12,11,24,14]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{2,3},{4},{2,4},{0,1,3,4},{5},{0,5},{2,5},{6},{0,6},{1,6},{3,5,6},{7},{0,7},{1,7},{4,5,7},{2,6,7},{8},{0,2,8},{1,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={0,1,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={4,5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 2 else if T={0,2,8} then 1 else if T={1,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[24],1⟩,⟨[9],1⟩,⟨[9,14],1⟩,⟨[10],2⟩,⟨[10,14],1⟩,⟨[11],2⟩,⟨[11,14],1⟩,⟨[9,10,11,24],1⟩,⟨[13],1⟩,⟨[13,24],1⟩,⟨[13,14],1⟩,⟨[12],1⟩,⟨[12,24],1⟩,⟨[9,12],1⟩,⟨[10,12,13],1⟩,⟨[25],1⟩,⟨[24,25],1⟩,⟨[9,25],1⟩,⟨[11,13,25],1⟩,⟨[12,14,25],1⟩,⟨[15],2⟩,⟨[14,15,24],1⟩,⟨[9,13,15],1⟩,⟨[11,12,15],1⟩,⟨[10,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case53

namespace Case54
def positionFn : Fin 9 → Fin 25 := ![8,9,13,23,10,24,11,12,14]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{3},{4},{2,4},{0,1,3,4},{5},{1,5},{3,5},{6},{0,6},{2,6},{4,5,6},{7},{0,7},{1,7},{2,5,7},{3,6,7},{8},{2,3,8},{0,5,8},{1,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={2,4} then 1 else if T={0,1,3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={4,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={2,3,8} then 1 else if T={0,5,8} then 1 else if T={1,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[24],2⟩,⟨[11],2⟩,⟨[11,14],1⟩,⟨[9,10,11,24],1⟩,⟨[25],1⟩,⟨[10,25],1⟩,⟨[24,25],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[12,14],1⟩,⟨[11,12,25],1⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[13,14,25],1⟩,⟨[12,13,24],1⟩,⟨[15],2⟩,⟨[14,15,24],1⟩,⟨[9,15,25],1⟩,⟨[10,12,15],1⟩,⟨[11,13,15],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case54

namespace Case55
def positionFn : Fin 9 → Fin 25 := ![23,11,8,9,10,14,12,13,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{3},{1,3},{4},{1,4},{0,2,3,4},{5},{0,1,5},{2,5},{6},{0,6},{1,2,6},{5,6},{7},{0,7},{1,7},{3,5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={2} then 2 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={0,2,3,4} then 1 else if T={5} then 1 else if T={0,1,5} then 1 else if T={2,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,2,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[24],1⟩,⟨[9],2⟩,⟨[10],2⟩,⟨[10,12],1⟩,⟨[11],2⟩,⟨[11,12],1⟩,⟨[9,10,11,24],1⟩,⟨[15],1⟩,⟨[12,15,24],1⟩,⟨[9,15],1⟩,⟨[13],1⟩,⟨[13,24],1⟩,⟨[9,12,13],1⟩,⟨[13,15],1⟩,⟨[14],1⟩,⟨[14,24],1⟩,⟨[12,14],1⟩,⟨[10,14,15],1⟩,⟨[11,13,14],1⟩,⟨[25],1⟩,⟨[24,25],1⟩,⟨[12,25],1⟩,⟨[11,15,25],1⟩,⟨[10,13,25],1⟩,⟨[9,14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case55

namespace Case56
def positionFn : Fin 9 → Fin 25 := ![8,13,22,9,10,23,12,24,11]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{3},{4},{1,4},{0,2,3,4},{5},{1,2,5},{3,5},{6},{1,6},{2,6},{0,5,6},{7},{0,7},{1,3,7},{5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={4} then 2 else if T={1,4} then 1 else if T={0,2,3,4} then 1 else if T={5} then 1 else if T={1,2,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={0,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],6⟩,⟨[9],1⟩,⟨[9,14],1⟩,⟨[23],2⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[11,14],1⟩,⟨[9,10,11,23],1⟩,⟨[24],1⟩,⟨[14,23,24],1⟩,⟨[10,24],1⟩,⟨[13],1⟩,⟨[13,14],1⟩,⟨[13,23],1⟩,⟨[9,13,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[10,14,25],1⟩,⟨[24,25],1⟩,⟨[11,13,25],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[12,14],1⟩,⟨[11,12,24],1⟩,⟨[10,12,13],1⟩,⟨[12,23,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case56

namespace Case57
def positionFn : Fin 9 → Fin 25 := ![8,13,9,22,10,11,12,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{3},{4},{1,4},{0,2,3,4},{5},{1,5},{2,5},{6},{1,6},{3,6},{0,5,6},{7},{0,7},{1,2,7},{3,5,7},{4,6,7},{8},{0,8},{1,3,8},{4,5,8},{2,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={4} then 2 else if T={1,4} then 1 else if T={0,2,3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={0,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={4,5,8} then 1 else if T={2,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],6⟩,⟨[9],1⟩,⟨[9,14],1⟩,⟨[10],2⟩,⟨[23],2⟩,⟨[11],2⟩,⟨[11,14],1⟩,⟨[9,10,11,23],1⟩,⟨[12],1⟩,⟨[12,14],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[13,14],1⟩,⟨[13,23],1⟩,⟨[9,12,13],1⟩,⟨[24],1⟩,⟨[9,24],1⟩,⟨[10,14,24],1⟩,⟨[12,23,24],1⟩,⟨[11,13,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[14,23,25],1⟩,⟨[11,12,25],1⟩,⟨[10,13,25],1⟩,⟨[24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case57

namespace Case58
def positionFn : Fin 9 → Fin 25 := ![8,22,9,10,13,23,24,11,12]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{1,3},{4},{1,4},{0,2,3,4},{5},{0,5},{6},{0,6},{1,2,5,6},{7},{0,7},{1,7},{3,5,7},{4,6,7},{8},{0,1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={0,2,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,2,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],4⟩,⟨[9],1⟩,⟨[23],1⟩,⟨[10],3⟩,⟨[11],2⟩,⟨[11,23],1⟩,⟨[14],2⟩,⟨[14,23],1⟩,⟨[9,10,11,14],1⟩,⟨[24],2⟩,⟨[9,24],1⟩,⟨[25],2⟩,⟨[9,25],1⟩,⟨[10,23,24,25],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[12,23],1⟩,⟨[11,12,24],1⟩,⟨[12,14,25],1⟩,⟨[13],2⟩,⟨[9,13,23],1⟩,⟨[13,14,24],1⟩,⟨[11,13,25],1⟩,⟨[10,12,13],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case58

namespace Case59
def positionFn : Fin 9 → Fin 25 := ![8,11,9,10,23,12,24,13,14]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{3},{1,3},{4},{1,4},{0,2,3,4},{5},{0,5},{6},{0,6},{1,2,5,6},{7},{0,7},{1,7},{3,5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={0,2,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,2,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],5⟩,⟨[9,12],1⟩,⟨[10],3⟩,⟨[11],2⟩,⟨[11,12],1⟩,⟨[24],2⟩,⟨[12,24],1⟩,⟨[9,10,11,24],1⟩,⟨[13],2⟩,⟨[9,13],1⟩,⟨[25],2⟩,⟨[9,25],1⟩,⟨[10,12,13,25],1⟩,⟨[14],1⟩,⟨[9,14],1⟩,⟨[12,14],1⟩,⟨[11,13,14],1⟩,⟨[14,24,25],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[12,15],1⟩,⟨[13,15,24],1⟩,⟨[11,15,25],1⟩,⟨[10,14,15],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case59

namespace Case60
def positionFn : Fin 9 → Fin 25 := ![11,13,12,8,23,9,14,24,10]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{1,2},{3},{1,3},{4},{1,4},{0,2,3,4},{5},{0,5},{3,5},{4,5},{6},{0,6},{2,6},{4,6},{7},{0,7},{2,7},{3,7},{1,5,6,7},{8},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,2,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={1,5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[12,14],1⟩,⟨[13],1⟩,⟨[13,14],1⟩,⟨[9],1⟩,⟨[9,14],1⟩,⟨[24],1⟩,⟨[14,24],1⟩,⟨[9,12,13,24],1⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[9,10],1⟩,⟨[10,24],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[15,24],1⟩,⟨[25],1⟩,⟨[12,25],1⟩,⟨[13,25],1⟩,⟨[9,25],1⟩,⟨[10,14,15,25],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[11,14],1⟩,⟨[10,11,13],1⟩,⟨[9,11,15],1⟩,⟨[11,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case60

namespace Case61
def positionFn : Fin 9 → Fin 25 := ![13,8,23,9,10,11,12,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,3},{4},{0,4},{1,2,3,4},{5},{0,5},{1,5},{6},{0,6},{2,6},{3,5,6},{7},{0,1,7},{2,5,7},{4,6,7},{8},{0,2,8},{4,5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={1,2,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,5,6} then 1 else if T={7} then 2 else if T={0,1,7} then 1 else if T={2,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,2,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],5⟩,⟨[9],2⟩,⟨[24],2⟩,⟨[10],2⟩,⟨[10,14],1⟩,⟨[11],2⟩,⟨[11,14],1⟩,⟨[9,10,11,24],1⟩,⟨[12],1⟩,⟨[12,14],1⟩,⟨[9,12],1⟩,⟨[13],1⟩,⟨[13,14],1⟩,⟨[13,24],1⟩,⟨[10,12,13],1⟩,⟨[15],2⟩,⟨[9,14,15],1⟩,⟨[12,15,24],1⟩,⟨[11,13,15],1⟩,⟨[25],2⟩,⟨[14,24,25],1⟩,⟨[11,12,25],1⟩,⟨[9,13,25],1⟩,⟨[10,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case61

namespace Case62
def positionFn : Fin 9 → Fin 25 := ![9,21,22,23,24,10,13,11,12]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,1,2,3,4},{5},{2,5},{3,5},{6},{1,6},{3,6},{0,5,6},{7},{0,7},{2,7},{1,5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={4} then 3 else if T={0,1,2,3,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={0,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,22,23,24,25],[⟨[],4⟩,⟨[10],2⟩,⟨[22],2⟩,⟨[23],2⟩,⟨[24],2⟩,⟨[25],3⟩,⟨[10,22,23,24,25],1⟩,⟨[11],1⟩,⟨[11,23],1⟩,⟨[11,24],1⟩,⟨[14],1⟩,⟨[14,22],1⟩,⟨[14,24],1⟩,⟨[10,11,14],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[12,23],1⟩,⟨[11,12,22],1⟩,⟨[12,14,25],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[13,22],1⟩,⟨[11,13,25],1⟩,⟨[13,14,23],1⟩,⟨[12,13,24],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case62

namespace Case63
def positionFn : Fin 9 → Fin 25 := ![7,8,9,10,23,12,13,11,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,1,2,3,4},{0,5},{3,5},{4,5},{0,6},{2,6},{4,6},{1,5,6},{0,7},{1,7},{3,7},{2,5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={4} then 2 else if T={0,1,2,3,4} then 1 else if T={0,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={1,5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,5,7} then 1 else if T={6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[8,9,10,11,12,13,14,24,25],[⟨[],6⟩,⟨[8],1⟩,⟨[9],2⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[24],2⟩,⟨[8,9,10,11,24],1⟩,⟨[8,13],1⟩,⟨[11,13],1⟩,⟨[13,24],1⟩,⟨[8,14],1⟩,⟨[10,14],1⟩,⟨[14,24],1⟩,⟨[9,13,14],1⟩,⟨[8,12],1⟩,⟨[9,12],1⟩,⟨[11,12],1⟩,⟨[10,12,13],1⟩,⟨[12,14],1⟩,⟨[8,25],1⟩,⟨[9,25],1⟩,⟨[10,25],1⟩,⟨[13,25],1⟩,⟨[11,14,25],1⟩,⟨[12,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case63

namespace Case64
def positionFn : Fin 9 → Fin 25 := ![21,9,22,23,24,10,13,11,12]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,1,2,3,4},{5},{0,5},{2,5},{6},{0,6},{2,6},{1,5,6},{7},{0,7},{1,7},{3,5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={3} then 3 else if T={4} then 3 else if T={0,1,2,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,22,23,24,25],[⟨[],4⟩,⟨[22],1⟩,⟨[10],2⟩,⟨[23],2⟩,⟨[24],3⟩,⟨[25],3⟩,⟨[10,22,23,24,25],1⟩,⟨[11],1⟩,⟨[11,22],1⟩,⟨[11,23],1⟩,⟨[14],1⟩,⟨[14,22],1⟩,⟨[14,23],1⟩,⟨[10,11,14],1⟩,⟨[12],1⟩,⟨[12,22],1⟩,⟨[10,12],1⟩,⟨[11,12,24],1⟩,⟨[12,14,25],1⟩,⟨[13],1⟩,⟨[13,22],1⟩,⟨[10,13],1⟩,⟨[11,13,25],1⟩,⟨[13,14,24],1⟩,⟨[12,13,23],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case64

namespace Case65
def positionFn : Fin 9 → Fin 25 := ![21,22,9,23,24,10,12,11,13]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,1,2,3,4},{5},{0,5},{1,5},{6},{0,6},{1,6},{2,5,6},{7},{0,7},{1,7},{3,5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={2} then 3 else if T={3} then 3 else if T={4} then 3 else if T={0,1,2,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,22,23,24,25],[⟨[],4⟩,⟨[22],1⟩,⟨[23],1⟩,⟨[10],3⟩,⟨[24],3⟩,⟨[25],3⟩,⟨[10,22,23,24,25],1⟩,⟨[11],1⟩,⟨[11,22],1⟩,⟨[11,23],1⟩,⟨[13],1⟩,⟨[13,22],1⟩,⟨[13,23],1⟩,⟨[10,11,13],1⟩,⟨[12],1⟩,⟨[12,22],1⟩,⟨[12,23],1⟩,⟨[11,12,24],1⟩,⟨[12,13,25],1⟩,⟨[14],1⟩,⟨[14,22],1⟩,⟨[14,23],1⟩,⟨[11,14,25],1⟩,⟨[13,14,24],1⟩,⟨[10,12,14],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case65

namespace Case66
def positionFn : Fin 9 → Fin 25 := ![9,21,22,23,24,13,11,10,12]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,1,2,3,4},{1,5},{3,5},{4,5},{0,6},{2,6},{4,6},{5,6},{7},{2,7},{3,7},{0,5,7},{1,6,7},{8},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={4} then 2 else if T={0,1,2,3,4} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={0,5,7} then 1 else if T={1,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,22,23,24,25],[⟨[],5⟩,⟨[10],2⟩,⟨[22],2⟩,⟨[23],2⟩,⟨[24],2⟩,⟨[25],2⟩,⟨[10,22,23,24,25],1⟩,⟨[14,22],1⟩,⟨[14,24],1⟩,⟨[14,25],1⟩,⟨[10,12],1⟩,⟨[12,23],1⟩,⟨[12,25],1⟩,⟨[12,14],1⟩,⟨[11],1⟩,⟨[11,23],1⟩,⟨[11,24],1⟩,⟨[10,11,14],1⟩,⟨[11,12,22],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[13,22],1⟩,⟨[13,14,23],1⟩,⟨[12,13,24],1⟩,⟨[11,13,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case66

namespace Case67
def positionFn : Fin 9 → Fin 25 := ![7,8,9,10,23,11,13,24,12]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,1,2,3,4},{0,5},{1,5},{3,5},{4,5},{0,6},{1,6},{2,6},{4,6},{0,7},{1,7},{2,7},{3,7},{5,6,7},{8},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={4} then 2 else if T={0,1,2,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[8,9,10,11,12,13,14,24,25],[⟨[],6⟩,⟨[8],1⟩,⟨[9],1⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[24],2⟩,⟨[8,9,10,11,24],1⟩,⟨[8,12],1⟩,⟨[9,12],1⟩,⟨[11,12],1⟩,⟨[12,24],1⟩,⟨[8,14],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[14,24],1⟩,⟨[8,25],1⟩,⟨[9,25],1⟩,⟨[10,25],1⟩,⟨[11,25],1⟩,⟨[12,14,25],1⟩,⟨[13],1⟩,⟨[8,13],1⟩,⟨[9,13],1⟩,⟨[10,12,13],1⟩,⟨[11,13,14],1⟩,⟨[13,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case67

namespace Case68
def positionFn : Fin 9 → Fin 25 := ![7,8,9,10,23,12,13,24,11]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,1,2,3,4},{5},{0,5},{3,5},{4,5},{6},{0,6},{2,6},{4,6},{7},{0,7},{2,7},{3,7},{1,5,6,7},{8},{0,8},{1,8},{2,5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 3 else if T={2} then 2 else if T={3} then 2 else if T={4} then 2 else if T={0,1,2,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={1,5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[8,9,10,11,12,13,14,24,25],[⟨[],4⟩,⟨[8],1⟩,⟨[9],3⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[24],2⟩,⟨[8,9,10,11,24],1⟩,⟨[13],1⟩,⟨[8,13],1⟩,⟨[11,13],1⟩,⟨[13,24],1⟩,⟨[14],1⟩,⟨[8,14],1⟩,⟨[10,14],1⟩,⟨[14,24],1⟩,⟨[25],1⟩,⟨[8,25],1⟩,⟨[10,25],1⟩,⟨[11,25],1⟩,⟨[9,13,14,25],1⟩,⟨[12],1⟩,⟨[8,12],1⟩,⟨[9,12],1⟩,⟨[10,12,13],1⟩,⟨[11,12,14],1⟩,⟨[12,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case68

namespace Case69
def positionFn : Fin 9 → Fin 25 := ![8,10,11,12,23,9,13,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,1,2,3,4},{0,5},{1,5},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{4,6},{0,7},{1,7},{2,7},{3,7},{4,7},{0,8},{1,8},{2,8},{3,8},{4,8},{5,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={4} then 1 else if T={0,1,2,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={4,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,8} then 1 else if T={5,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[24],1⟩,⟨[9,11,12,13,24],1⟩,⟨[9,10],1⟩,⟨[10,11],1⟩,⟨[10,12],1⟩,⟨[10,13],1⟩,⟨[10,24],1⟩,⟨[9,14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[14,24],1⟩,⟨[9,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[15,24],1⟩,⟨[9,25],1⟩,⟨[11,25],1⟩,⟨[12,25],1⟩,⟨[13,25],1⟩,⟨[24,25],1⟩,⟨[10,14,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case69

namespace Case70
def positionFn : Fin 9 → Fin 25 := ![13,10,8,9,11,12,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{3},{0,3},{2,3},{4},{0,4},{1,4},{5},{1,2,5},{6},{1,3,6},{4,5,6},{7},{2,4,7},{3,5,7},{0,6,7},{8},{3,4,8},{0,5,8},{2,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={1,2,5} then 1 else if T={6} then 2 else if T={1,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={2,4,7} then 1 else if T={3,5,7} then 1 else if T={0,6,7} then 1 else if T={8} then 2 else if T={3,4,8} then 1 else if T={0,5,8} then 1 else if T={2,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[11],1⟩,⟨[11,14],1⟩,⟨[9],1⟩,⟨[9,14],1⟩,⟨[10],1⟩,⟨[10,14],1⟩,⟨[9,10],1⟩,⟨[12],1⟩,⟨[12,14],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[9,11,13],1⟩,⟨[15],2⟩,⟨[10,11,15],1⟩,⟨[12,13,15],1⟩,⟨[24],2⟩,⟨[9,12,24],1⟩,⟨[10,13,24],1⟩,⟨[14,15,24],1⟩,⟨[25],2⟩,⟨[10,12,25],1⟩,⟨[13,14,25],1⟩,⟨[9,15,25],1⟩,⟨[11,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case70

namespace Case71
def positionFn : Fin 9 → Fin 25 := ![8,9,22,10,23,11,12,13,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{2,3},{4},{1,4},{3,4},{0,5},{1,2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{5,6},{7},{2,7},{0,1,3,7},{4,6,7},{8},{1,8},{0,2,4,8},{3,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 2 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={0,1,3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={0,2,4,8} then 1 else if T={3,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],6⟩,⟨[9],2⟩,⟨[10],1⟩,⟨[23],1⟩,⟨[11],1⟩,⟨[11,23],1⟩,⟨[24],1⟩,⟨[10,24],1⟩,⟨[11,24],1⟩,⟨[9,12],1⟩,⟨[10,12,23],1⟩,⟨[11,12],1⟩,⟨[12,24],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[13,23],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[14,23],1⟩,⟨[9,10,11,14],1⟩,⟨[13,14,24],1⟩,⟨[25],2⟩,⟨[10,25],1⟩,⟨[9,23,24,25],1⟩,⟨[11,13,25],1⟩,⟨[12,14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case71

namespace Case72
def positionFn : Fin 9 → Fin 25 := ![23,8,9,13,11,10,14,12,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,3},{2,3},{0,4},{1,4},{2,4},{5},{0,1,2,5},{3,5},{6},{2,6},{0,3,6},{4,6},{7},{0,7},{3,7},{4,5,7},{1,6,7},{8},{0,8},{1,8},{3,4,8},{5,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={2,6} then 1 else if T={0,3,6} then 1 else if T={4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={3,7} then 1 else if T={4,5,7} then 1 else if T={1,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,4,8} then 1 else if T={5,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[24],1⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[12,24],1⟩,⟨[9,12],1⟩,⟨[10,12],1⟩,⟨[11],2⟩,⟨[9,10,11,24],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[14,15,24],1⟩,⟨[12,15],1⟩,⟨[13],1⟩,⟨[13,24],1⟩,⟨[13,14],1⟩,⟨[11,12,13],1⟩,⟨[9,13,15],1⟩,⟨[25],1⟩,⟨[24,25],1⟩,⟨[9,25],1⟩,⟨[12,14,25],1⟩,⟨[11,15,25],1⟩,⟨[10,13,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case72

namespace Case73
def positionFn : Fin 9 → Fin 25 := ![23,8,9,13,11,10,14,12,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{5},{0,1,2,5},{6},{2,6},{0,3,6},{5,6},{7},{0,7},{3,7},{4,5,7},{1,6,7},{8},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={0,1,2,5} then 1 else if T={6} then 1 else if T={2,6} then 1 else if T={0,3,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={3,7} then 1 else if T={4,5,7} then 1 else if T={1,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[24],1⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[12,24],1⟩,⟨[9,12],1⟩,⟨[10,12],1⟩,⟨[12,14],1⟩,⟨[11],2⟩,⟨[9,10,11,24],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[14,15,24],1⟩,⟨[11,15],1⟩,⟨[13],1⟩,⟨[13,24],1⟩,⟨[13,14],1⟩,⟨[11,12,13],1⟩,⟨[9,13,15],1⟩,⟨[25],1⟩,⟨[24,25],1⟩,⟨[9,25],1⟩,⟨[11,14,25],1⟩,⟨[12,15,25],1⟩,⟨[10,13,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case73

namespace Case74
def positionFn : Fin 9 → Fin 25 := ![8,23,9,12,13,10,14,11,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,3},{2,3},{0,4},{2,4},{3,4},{5},{0,1,2,5},{4,5},{6},{0,6},{3,6},{1,4,6},{7},{1,7},{2,7},{0,3,7},{5,6,7},{8},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={0,1,2,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={0,3,7} then 1 else if T={5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,5,8} then 1 else if T={2,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9],1⟩,⟨[24],1⟩,⟨[10],1⟩,⟨[13,24],1⟩,⟨[10,13],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[11],2⟩,⟨[9,10,11,24],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[13,15],1⟩,⟨[14,15,24],1⟩,⟨[12],1⟩,⟨[12,24],1⟩,⟨[10,12],1⟩,⟨[9,12,13],1⟩,⟨[11,12,15],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[24,25],1⟩,⟨[11,13,25],1⟩,⟨[10,15,25],1⟩,⟨[12,14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case74

namespace Case75
def positionFn : Fin 9 → Fin 25 := ![8,9,10,12,13,23,24,11,14]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{5},{0,1,2,5},{6},{2,6},{3,4,6},{5,6},{7},{1,7},{4,7},{3,5,7},{0,6,7},{8},{0,8},{3,8},{4,5,8},{1,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={0,1,2,5} then 1 else if T={6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={4,7} then 1 else if T={3,5,7} then 1 else if T={0,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={3,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[24],2⟩,⟨[9,10,11,24],1⟩,⟨[25],1⟩,⟨[11,25],1⟩,⟨[13,14,25],1⟩,⟨[24,25],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[12,14],1⟩,⟨[12,13,24],1⟩,⟨[9,12,25],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[13,15],1⟩,⟨[14,15,24],1⟩,⟨[10,15,25],1⟩,⟨[11,12,15],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case75

namespace Case76
def positionFn : Fin 9 → Fin 25 := ![8,12,9,13,10,23,14,24,11]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{2,3},{4},{1,4},{3,4},{5},{2,5},{0,1,3,5},{4,5},{0,6},{1,6},{2,6},{5,6},{7},{1,7},{0,2,4,7},{3,6,7},{8},{0,8},{1,2,8},{3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 2 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={0,1,3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,2,4,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[9],2⟩,⟨[13],1⟩,⟨[10],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11],1⟩,⟨[11,13],1⟩,⟨[11,14],1⟩,⟨[24],1⟩,⟨[10,24],1⟩,⟨[9,13,14,24],1⟩,⟨[11,24],1⟩,⟨[9,15],1⟩,⟨[13,15],1⟩,⟨[10,15],1⟩,⟨[15,24],1⟩,⟨[25],2⟩,⟨[13,25],1⟩,⟨[9,10,11,25],1⟩,⟨[14,15,25],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[10,12,13],1⟩,⟨[12,14],1⟩,⟨[11,12,15],1⟩,⟨[12,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case76

namespace Case77
def positionFn : Fin 9 → Fin 25 := ![8,9,12,11,13,10,23,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{5},{2,3,5},{6},{2,6},{0,1,5,6},{7},{0,2,7},{3,7},{5,7},{4,6,7},{8},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={2,3,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,1,5,6} then 1 else if T={7} then 1 else if T={0,2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[10,13],1⟩,⟨[9,12],1⟩,⟨[10,12],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[12,14],1⟩,⟨[11],2⟩,⟨[11,12,13],1⟩,⟨[24],2⟩,⟨[13,24],1⟩,⟨[9,10,11,24],1⟩,⟨[15],1⟩,⟨[9,13,15],1⟩,⟨[12,15],1⟩,⟨[11,15],1⟩,⟨[14,15,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[13,25],1⟩,⟨[11,14,25],1⟩,⟨[12,24,25],1⟩,⟨[10,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case77

namespace Case78
def positionFn : Fin 9 → Fin 25 := ![8,12,9,23,13,10,24,11,14]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{3},{4},{3,4},{5},{1,5},{0,2,3,5},{6},{0,6},{1,2,4,6},{7},{0,7},{1,7},{4,5,7},{3,6,7},{8},{1,3,8},{0,4,8},{5,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={4} then 2 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={0,2,3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,2,4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={4,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={1,3,8} then 1 else if T={0,4,8} then 1 else if T={5,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],4⟩,⟨[9],1⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[10],3⟩,⟨[24],2⟩,⟨[14],2⟩,⟨[14,24],1⟩,⟨[11],2⟩,⟨[11,13],1⟩,⟨[9,10,11,24],1⟩,⟨[25],2⟩,⟨[9,25],1⟩,⟨[10,13,14,25],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[12,13],1⟩,⟨[11,12,14],1⟩,⟨[12,24,25],1⟩,⟨[15],2⟩,⟨[13,15,24],1⟩,⟨[9,14,15],1⟩,⟨[11,15,25],1⟩,⟨[10,12,15],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case78

namespace Case79
def positionFn : Fin 9 → Fin 25 := ![11,10,12,13,8,9,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{4},{2,4},{3,4},{5},{1,5},{3,5},{0,4,5},{6},{0,6},{2,6},{1,4,6},{7},{0,7},{1,7},{2,5,7},{3,6,7},{8},{0,1,8},{2,3,8},{5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={0,1,8} then 1 else if T={2,3,8} then 1 else if T={5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[12,13],1⟩,⟨[11,13],1⟩,⟨[12,14],1⟩,⟨[11,14],1⟩,⟨[9],1⟩,⟨[9,13],1⟩,⟨[9,14],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[10,14],1⟩,⟨[9,10,12],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[9,11,15],1⟩,⟨[24],1⟩,⟨[12,24],1⟩,⟨[11,24],1⟩,⟨[10,13,24],1⟩,⟨[14,15,24],1⟩,⟨[25],2⟩,⟨[11,12,25],1⟩,⟨[13,14,25],1⟩,⟨[10,15,25],1⟩,⟨[9,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case79

namespace Case80
def positionFn : Fin 9 → Fin 25 := ![22,23,9,12,13,10,14,24,11]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{0,2},{1,3},{2,3},{4},{2,4},{3,4},{5},{1,5},{3,5},{0,4,5},{6},{0,6},{2,6},{1,4,6},{7},{0,7},{1,7},{2,5,7},{3,6,7},{8},{1,2,8},{0,3,8},{5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={1,2,8} then 1 else if T={0,3,8} then 1 else if T={5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,23,24,25],[⟨[],8⟩,⟨[23,24],1⟩,⟨[10,23],1⟩,⟨[13,24],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[11],1⟩,⟨[11,24],1⟩,⟨[11,13],1⟩,⟨[11,14,23],1⟩,⟨[15],1⟩,⟨[15,23],1⟩,⟨[10,15],1⟩,⟨[14,15,24],1⟩,⟨[25],1⟩,⟨[23,25],1⟩,⟨[24,25],1⟩,⟨[10,11,25],1⟩,⟨[13,15,25],1⟩,⟨[12],2⟩,⟨[10,12,24],1⟩,⟨[12,13,23],1⟩,⟨[11,12,15],1⟩,⟨[12,14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case80

namespace Case81
def positionFn : Fin 9 → Fin 25 := ![10,8,11,13,12,9,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{0,2},{1,2},{0,3},{1,3},{2,3},{4},{3,4},{5},{1,5},{0,4,5},{6},{2,6},{1,4,6},{5,6},{7},{0,7},{4,7},{2,5,7},{3,6,7},{8},{2,4,8},{3,5,8},{0,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={0,4,5} then 1 else if T={6} then 1 else if T={2,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={4,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={0,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[9,11],1⟩,⟨[11,12],1⟩,⟨[9,12],1⟩,⟨[11,14],1⟩,⟨[9,14],1⟩,⟨[12,14],1⟩,⟨[13],1⟩,⟨[13,14],1⟩,⟨[10],1⟩,⟨[9,10],1⟩,⟨[10,11,13],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[9,13,15],1⟩,⟨[10,15],1⟩,⟨[24],1⟩,⟨[11,24],1⟩,⟨[13,24],1⟩,⟨[10,12,24],1⟩,⟨[14,15,24],1⟩,⟨[25],2⟩,⟨[12,13,25],1⟩,⟨[10,14,25],1⟩,⟨[11,15,25],1⟩,⟨[9,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case81

namespace Case82
def positionFn : Fin 9 → Fin 25 := ![8,23,13,12,9,10,14,11,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,2},{0,3},{1,3},{2,3},{4},{2,4},{5},{2,5},{0,1,4,5},{6},{0,6},{1,2,6},{3,6},{7},{0,7},{1,7},{3,4,7},{5,6,7},{8},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={1} then 1 else if T={0,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={0,1,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,2,6} then 1 else if T={3,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[24],1⟩,⟨[9,14],1⟩,⟨[9,13],1⟩,⟨[13,24],1⟩,⟨[13,14],1⟩,⟨[10],2⟩,⟨[10,14],1⟩,⟨[11],2⟩,⟨[11,14],1⟩,⟨[9,10,11,24],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[14,15,24],1⟩,⟨[13,15],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[12,24],1⟩,⟨[10,12,13],1⟩,⟨[11,12,15],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[24,25],1⟩,⟨[11,13,25],1⟩,⟨[10,15,25],1⟩,⟨[12,14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case82

namespace Case83
def positionFn : Fin 9 → Fin 25 := ![8,9,22,13,10,23,11,24,12]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,2},{1,2},{0,3},{1,3},{4},{3,4},{5},{2,5},{0,1,4,5},{6},{0,6},{3,6},{2,4,6},{7},{0,7},{2,7},{3,5,7},{1,6,7},{8},{0,8},{1,8},{2,3,8},{5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={3,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={0,1,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,5,7} then 1 else if T={1,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],7⟩,⟨[10],1⟩,⟨[9,23],1⟩,⟨[10,23],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[11],2⟩,⟨[11,14],1⟩,⟨[24],2⟩,⟨[23,24],1⟩,⟨[9,10,11,24],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[12,14],1⟩,⟨[11,12,23],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[23,25],1⟩,⟨[14,24,25],1⟩,⟨[10,12,25],1⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[13,14,23],1⟩,⟨[12,13,24],1⟩,⟨[11,13,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case83

namespace Case84
def positionFn : Fin 9 → Fin 25 := ![8,9,22,11,10,13,23,24,12]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,3},{1,3},{2,3},{4},{2,4},{5},{2,5},{0,1,4,5},{6},{1,6},{3,4,6},{7},{1,7},{3,5,7},{0,2,6,7},{8},{0,8},{1,2,8},{3,8},{5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 2 else if T={1} then 1 else if T={2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={0,1,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,4,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={3,8} then 1 else if T={5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],5⟩,⟨[9],2⟩,⟨[10],1⟩,⟨[23],1⟩,⟨[9,12],1⟩,⟨[10,12],1⟩,⟨[12,23],1⟩,⟨[11],2⟩,⟨[11,23],1⟩,⟨[14],2⟩,⟨[14,23],1⟩,⟨[9,10,11,14],1⟩,⟨[24],2⟩,⟨[10,24],1⟩,⟨[11,12,24],1⟩,⟨[25],2⟩,⟨[10,25],1⟩,⟨[12,14,25],1⟩,⟨[9,23,24,25],1⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[10,13,23],1⟩,⟨[12,13],1⟩,⟨[13,14,24],1⟩,⟨[11,13,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case84

namespace Case85
def positionFn : Fin 9 → Fin 25 := ![10,11,8,22,23,9,24,13,12]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{1,2},{3},{0,3},{1,3},{4},{5},{0,1,4,5},{6},{2,3,4,6},{5,6},{7},{1,7},{3,7},{2,5,7},{0,6,7},{8},{0,8},{2,8},{3,5,8},{1,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 3 else if T={5} then 2 else if T={0,1,4,5} then 1 else if T={6} then 2 else if T={2,3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,5,7} then 1 else if T={0,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={3,5,8} then 1 else if T={1,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],5⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[9],1⟩,⟨[9,11],1⟩,⟨[9,12],1⟩,⟨[23],1⟩,⟨[11,23],1⟩,⟨[12,23],1⟩,⟨[24],3⟩,⟨[10],2⟩,⟨[10,11,12,24],1⟩,⟨[25],2⟩,⟨[9,23,24,25],1⟩,⟨[10,25],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[14,23],1⟩,⟨[9,10,14],1⟩,⟨[11,14,25],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[9,13],1⟩,⟨[10,13,23],1⟩,⟨[12,13,25],1⟩,⟨[13,14,24],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case85

namespace Case86
def positionFn : Fin 9 → Fin 25 := ![8,9,11,13,23,10,24,12,14]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,2},{1,2},{0,3},{1,3},{2,3},{4},{5},{3,5},{0,1,4,5},{6},{0,6},{4,6},{2,5,6},{7},{0,7},{2,7},{3,4,7},{1,6,7},{8},{0,8},{1,8},{2,4,8},{3,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={5} then 2 else if T={3,5} then 1 else if T={0,1,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={4,6} then 1 else if T={2,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={1,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={3,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[10],1⟩,⟨[9,12],1⟩,⟨[10,12],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[24],2⟩,⟨[11],2⟩,⟨[11,14],1⟩,⟨[9,10,11,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[24,25],1⟩,⟨[11,12,25],1⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[12,13],1⟩,⟨[13,14,24],1⟩,⟨[10,13,25],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[10,15],1⟩,⟨[12,15,24],1⟩,⟨[14,15,25],1⟩,⟨[11,13,15],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case86

namespace Case87
def positionFn : Fin 9 → Fin 25 := ![10,11,8,13,9,23,14,24,12]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{4},{2,4},{3,4},{5},{2,5},{3,5},{0,1,4,5},{6},{0,6},{1,6},{5,6},{7},{0,7},{1,7},{4,7},{2,3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,1,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={4,7} then 1 else if T={2,3,6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[9,11],1⟩,⟨[9,12],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[10],1⟩,⟨[9,10],1⟩,⟨[10,14],1⟩,⟨[24],1⟩,⟨[9,24],1⟩,⟨[14,24],1⟩,⟨[10,11,12,24],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[15,24],1⟩,⟨[25],1⟩,⟨[11,25],1⟩,⟨[12,25],1⟩,⟨[10,25],1⟩,⟨[9,14,15,25],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[9,13],1⟩,⟨[13,14],1⟩,⟨[10,13,15],1⟩,⟨[13,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case87

namespace Case88
def positionFn : Fin 9 → Fin 25 := ![12,13,8,14,9,11,10,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{2},{1,2},{3},{0,3},{2,3},{4},{0,4},{1,4},{5},{0,5},{1,5},{2,4,5},{6},{0,6},{1,6},{3,4,6},{7},{0,1,7},{3,5,7},{2,6,7},{8},{0,2,8},{1,3,8},{5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,4,6} then 1 else if T={7} then 2 else if T={0,1,7} then 1 else if T={3,5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 2 else if T={0,2,8} then 1 else if T={1,3,8} then 1 else if T={5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9],1⟩,⟨[9,14],1⟩,⟨[15],1⟩,⟨[13,15],1⟩,⟨[9,15],1⟩,⟨[10],1⟩,⟨[10,13],1⟩,⟨[10,14],1⟩,⟨[12],1⟩,⟨[12,13],1⟩,⟨[12,14],1⟩,⟨[9,10,12],1⟩,⟨[11],1⟩,⟨[11,13],1⟩,⟨[11,14],1⟩,⟨[10,11,15],1⟩,⟨[24],2⟩,⟨[13,14,24],1⟩,⟨[12,15,24],1⟩,⟨[9,11,24],1⟩,⟨[25],2⟩,⟨[9,13,25],1⟩,⟨[14,15,25],1⟩,⟨[11,12,25],1⟩,⟨[10,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case88

namespace Case89
def positionFn : Fin 9 → Fin 25 := ![8,9,12,13,11,10,23,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{5},{3,5},{2,4,5},{6},{2,6},{0,1,5,6},{7},{1,7},{0,2,7},{4,7},{3,6,7},{8},{0,8},{2,8},{1,3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,1,5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={0,2,7} then 1 else if T={4,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[10,13],1⟩,⟨[9,14],1⟩,⟨[13,14],1⟩,⟨[9,12],1⟩,⟨[10,12],1⟩,⟨[12,14],1⟩,⟨[11],2⟩,⟨[11,14],1⟩,⟨[11,12,13],1⟩,⟨[24],2⟩,⟨[13,24],1⟩,⟨[9,10,11,24],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[9,13,15],1⟩,⟨[12,15],1⟩,⟨[14,15,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[13,25],1⟩,⟨[10,14,25],1⟩,⟨[12,24,25],1⟩,⟨[11,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case89

namespace Case90
def positionFn : Fin 9 → Fin 25 := ![21,22,9,23,10,13,11,12,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,4},{1,4},{3,4},{0,5},{1,5},{3,5},{2,4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,7},{4,7},{3,6,7},{8},{0,1,2,3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={0,4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={2,4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={4,7} then 1 else if T={3,6,7} then 1 else if T={8} then 3 else if T={0,1,2,3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,22,23,24,25],[⟨[],6⟩,⟨[22],1⟩,⟨[23],1⟩,⟨[10],2⟩,⟨[24],2⟩,⟨[11,22],1⟩,⟨[11,23],1⟩,⟨[11,24],1⟩,⟨[14,22],1⟩,⟨[14,23],1⟩,⟨[14,24],1⟩,⟨[10,11,14],1⟩,⟨[12,22],1⟩,⟨[12,23],1⟩,⟨[10,12],1⟩,⟨[12,14],1⟩,⟨[13,22],1⟩,⟨[13,23],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[12,13,24],1⟩,⟨[25],3⟩,⟨[10,22,23,24,25],1⟩,⟨[11,12,25],1⟩,⟨[13,14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case90

namespace Case91
def positionFn : Fin 9 → Fin 25 := ![8,12,9,13,10,23,24,11,14]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{3},{0,3},{2,3},{4},{5},{1,5},{0,2,4,5},{6},{0,6},{1,3,4,6},{7},{0,1,7},{2,7},{3,7},{5,6,7},{8},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 3 else if T={5} then 2 else if T={1,5} then 1 else if T={0,2,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,3,4,6} then 1 else if T={7} then 1 else if T={0,1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,5,8} then 1 else if T={2,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],5⟩,⟨[9],1⟩,⟨[13],1⟩,⟨[10],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[11],3⟩,⟨[24],2⟩,⟨[13,24],1⟩,⟨[9,10,11,24],1⟩,⟨[25],2⟩,⟨[9,25],1⟩,⟨[11,13,14,25],1⟩,⟨[12],1⟩,⟨[9,12,13],1⟩,⟨[10,12],1⟩,⟨[12,14],1⟩,⟨[12,24,25],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[13,15],1⟩,⟨[14,15,24],1⟩,⟨[10,15,25],1⟩,⟨[11,12,15],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case91

namespace Case92
def positionFn : Fin 9 → Fin 25 := ![11,8,9,10,12,23,14,13,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{3},{0,3},{4},{1,4},{3,4},{5},{1,5},{3,5},{0,2,4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,7},{4,7},{3,6,7},{8},{0,8},{1,2,3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={0,2,4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={4,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9,12],1⟩,⟨[10],2⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[11,13],1⟩,⟨[24],1⟩,⟨[9,24],1⟩,⟨[11,24],1⟩,⟨[10,12,13,24],1⟩,⟨[12,15],1⟩,⟨[9,15],1⟩,⟨[10,15],1⟩,⟨[15,24],1⟩,⟨[12,14],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[11,14,15],1⟩,⟨[25],2⟩,⟨[12,25],1⟩,⟨[9,10,11,25],1⟩,⟨[13,15,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case92

namespace Case93
def positionFn : Fin 9 → Fin 25 := ![8,9,12,14,13,10,23,11,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{5},{2,5},{3,4,5},{6},{2,6},{0,1,5,6},{7},{1,7},{0,2,7},{4,7},{3,6,7},{8},{0,8},{1,2,8},{3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,1,5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={0,2,7} then 1 else if T={4,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[9,15],1⟩,⟨[10,15],1⟩,⟨[13,15],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[11],2⟩,⟨[11,13],1⟩,⟨[11,14,15],1⟩,⟨[24],2⟩,⟨[13,24],1⟩,⟨[9,10,11,24],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[9,12,13],1⟩,⟨[12,14],1⟩,⟨[12,15,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[10,13,25],1⟩,⟨[15,25],1⟩,⟨[14,24,25],1⟩,⟨[11,12,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case93

namespace Case94
def positionFn : Fin 9 → Fin 25 := ![8,9,12,14,13,10,23,11,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{5},{3,4,5},{6},{2,6},{0,1,5,6},{7},{0,2,7},{4,7},{5,7},{3,6,7},{8},{0,8},{3,8},{2,5,8},{4,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={3,4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,1,5,6} then 1 else if T={7} then 1 else if T={0,2,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={3,8} then 1 else if T={2,5,8} then 1 else if T={4,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[10,13],1⟩,⟨[9,15],1⟩,⟨[10,15],1⟩,⟨[13,15],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[11],2⟩,⟨[11,14,15],1⟩,⟨[24],2⟩,⟨[13,24],1⟩,⟨[9,10,11,24],1⟩,⟨[12],1⟩,⟨[9,12,13],1⟩,⟨[12,14],1⟩,⟨[11,12],1⟩,⟨[12,15,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[15,25],1⟩,⟨[11,13,25],1⟩,⟨[14,24,25],1⟩,⟨[10,12,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case94

namespace Case95
def positionFn : Fin 9 → Fin 25 := ![11,13,8,12,9,14,23,10,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{3},{0,3},{2,3},{4},{1,4},{2,4},{5},{0,5},{1,5},{3,4,5},{6},{0,6},{1,6},{2,5,6},{7},{0,2,7},{1,3,7},{4,6,7},{8},{1,2,8},{0,4,8},{3,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,5,6} then 1 else if T={7} then 2 else if T={0,2,7} then 1 else if T={1,3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={1,2,8} then 1 else if T={0,4,8} then 1 else if T={3,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[12,14],1⟩,⟨[9],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[9,13],1⟩,⟨[10],1⟩,⟨[10,14],1⟩,⟨[9,10],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[10,13,15],1⟩,⟨[24],1⟩,⟨[12,24],1⟩,⟨[14,24],1⟩,⟨[9,15,24],1⟩,⟨[11],2⟩,⟨[9,11,12],1⟩,⟨[11,13,14],1⟩,⟨[10,11,24],1⟩,⟨[25],2⟩,⟨[9,14,25],1⟩,⟨[10,12,25],1⟩,⟨[13,24,25],1⟩,⟨[11,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case95

namespace Case96
def positionFn : Fin 9 → Fin 25 := ![8,10,11,9,14,12,13,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,7},{4,7},{3,6,7},{8},{0,1,2,8},{3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 9 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={4,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={0,1,2,8} then 1 else if T={3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],9⟩,⟨[9,10],1⟩,⟨[10,11],1⟩,⟨[10,12],1⟩,⟨[9,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[9,13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[10,13,15],1⟩,⟨[9,14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[9,24],1⟩,⟨[11,24],1⟩,⟨[12,24],1⟩,⟨[15,24],1⟩,⟨[10,14,24],1⟩,⟨[25],2⟩,⟨[9,11,12,25],1⟩,⟨[10,25],1⟩,⟨[14,15,25],1⟩,⟨[13,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case96

namespace Case97
def positionFn : Fin 9 → Fin 25 := ![8,12,13,9,10,23,24,11,14]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{1,3},{2,3},{4},{2,4},{5},{1,5},{0,3,4,5},{6},{0,1,2,6},{3,6},{7},{0,7},{2,7},{1,4,7},{5,6,7},{8},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 2 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={0,3,4,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={3,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],5⟩,⟨[9],2⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[10],1⟩,⟨[10,13],1⟩,⟨[10,14],1⟩,⟨[11],2⟩,⟨[11,14],1⟩,⟨[24],2⟩,⟨[13,24],1⟩,⟨[9,10,11,24],1⟩,⟨[25],2⟩,⟨[9,13,14,25],1⟩,⟨[10,25],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[12,14],1⟩,⟨[11,12,13],1⟩,⟨[12,24,25],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[13,15],1⟩,⟨[14,15,24],1⟩,⟨[11,15,25],1⟩,⟨[10,12,15],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case97

namespace Case98
def positionFn : Fin 9 → Fin 25 := ![8,12,13,9,10,23,11,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{2,3},{4},{1,4},{5},{1,5},{0,3,4,5},{6},{0,6},{2,6},{1,3,6},{7},{0,7},{1,7},{2,4,7},{5,6,7},{8},{0,1,8},{2,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={0,3,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,3,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 2 else if T={0,1,8} then 1 else if T={2,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[9],1⟩,⟨[9,14],1⟩,⟨[13,14],1⟩,⟨[10],2⟩,⟨[10,14],1⟩,⟨[11],2⟩,⟨[11,13],1⟩,⟨[24],2⟩,⟨[13,24],1⟩,⟨[9,10,11,24],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[12,14],1⟩,⟨[10,12,13],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[13,15],1⟩,⟨[11,14,15],1⟩,⟨[12,15,24],1⟩,⟨[25],2⟩,⟨[9,13,25],1⟩,⟨[14,24,25],1⟩,⟨[11,12,25],1⟩,⟨[10,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case98

namespace Case99
def positionFn : Fin 9 → Fin 25 := ![8,12,13,9,10,23,24,11,14]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{3},{4},{2,4},{5},{1,5},{0,3,4,5},{6},{0,6},{1,2,3,6},{7},{0,7},{2,7},{1,4,7},{5,6,7},{8},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 3 else if T={4} then 2 else if T={2,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={0,3,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,2,3,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],5⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[14],1⟩,⟨[9,14],1⟩,⟨[10],3⟩,⟨[11],2⟩,⟨[11,14],1⟩,⟨[24],2⟩,⟨[13,24],1⟩,⟨[9,10,11,24],1⟩,⟨[25],2⟩,⟨[9,25],1⟩,⟨[10,13,14,25],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[12,14],1⟩,⟨[11,12,13],1⟩,⟨[12,24,25],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[13,15],1⟩,⟨[14,15,24],1⟩,⟨[11,15,25],1⟩,⟨[10,12,15],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case99

namespace Case100
def positionFn : Fin 9 → Fin 25 := ![8,13,12,9,10,23,11,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{0,2},{1,2},{3},{4},{1,4},{5},{2,5},{0,3,4,5},{6},{1,6},{3,6},{2,4,6},{7},{0,7},{2,7},{1,3,7},{5,6,7},{8},{2,3,8},{1,5,8},{0,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={1,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={0,3,4,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,3,7} then 1 else if T={5,6,7} then 1 else if T={8} then 2 else if T={2,3,8} then 1 else if T={1,5,8} then 1 else if T={0,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[9],1⟩,⟨[9,14],1⟩,⟨[9,13],1⟩,⟨[13,14],1⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[11,14],1⟩,⟨[24],2⟩,⟨[13,24],1⟩,⟨[9,10,11,24],1⟩,⟨[12],1⟩,⟨[12,14],1⟩,⟨[10,12],1⟩,⟨[11,12,13],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[13,15],1⟩,⟨[10,14,15],1⟩,⟨[12,15,24],1⟩,⟨[25],2⟩,⟨[10,13,25],1⟩,⟨[14,24,25],1⟩,⟨[9,12,25],1⟩,⟨[11,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case100

namespace Case101
def positionFn : Fin 9 → Fin 25 := ![8,9,10,22,11,12,23,24,13]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,3},{4},{0,4},{2,4},{5},{0,5},{2,5},{1,3,4,5},{6},{0,6},{1,6},{5,6},{7},{0,7},{1,7},{4,7},{2,3,6,7},{8},{0,1,2,8},{3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={1,3,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={4,7} then 1 else if T={2,3,6,7} then 1 else if T={8} then 2 else if T={0,1,2,8} then 1 else if T={3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],5⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[23],2⟩,⟨[9,23],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[11,13],1⟩,⟨[10,12,13,23],1⟩,⟨[24],1⟩,⟨[9,24],1⟩,⟨[10,24],1⟩,⟨[13,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[10,25],1⟩,⟨[12,25],1⟩,⟨[11,23,24,25],1⟩,⟨[14],2⟩,⟨[9,10,11,14],1⟩,⟨[14,23],1⟩,⟨[12,14,24],1⟩,⟨[13,14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case101

namespace Case102
def positionFn : Fin 9 → Fin 25 := ![7,8,12,9,10,23,13,24,11]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{3},{4},{2,4},{5},{2,5},{0,1,3,4,5},{6},{0,6},{1,6},{5,6},{7},{0,7},{1,7},{4,7},{2,3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={4} then 2 else if T={2,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={0,1,3,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={4,7} then 1 else if T={2,3,6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[8,9,10,11,12,13,14,24,25],[⟨[],5⟩,⟨[8],1⟩,⟨[9],1⟩,⟨[8,13],1⟩,⟨[9,13],1⟩,⟨[10],3⟩,⟨[11],2⟩,⟨[11,13],1⟩,⟨[24],2⟩,⟨[13,24],1⟩,⟨[8,9,10,11,24],1⟩,⟨[14],1⟩,⟨[8,14],1⟩,⟨[9,14],1⟩,⟨[14,24],1⟩,⟨[25],1⟩,⟨[8,25],1⟩,⟨[9,25],1⟩,⟨[11,25],1⟩,⟨[10,13,14,25],1⟩,⟨[8,12],1⟩,⟨[9,12],1⟩,⟨[12,13],1⟩,⟨[10,12],1⟩,⟨[11,12,14],1⟩,⟨[12,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case102

namespace Case103
def positionFn : Fin 9 → Fin 25 := ![13,14,8,9,23,10,12,24,11]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,3},{1,3},{4},{0,4},{1,4},{5},{2,3,4,5},{0,6},{1,6},{2,6},{4,6},{7},{2,7},{0,1,5,7},{3,6,7},{8},{0,8},{1,2,8},{3,8},{5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 3 else if T={2,3,4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={0,1,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={3,8} then 1 else if T={5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[15],1⟩,⟨[9],1⟩,⟨[9,14],1⟩,⟨[10],1⟩,⟨[10,14],1⟩,⟨[10,15],1⟩,⟨[24],1⟩,⟨[14,24],1⟩,⟨[15,24],1⟩,⟨[11],3⟩,⟨[9,10,11,24],1⟩,⟨[13,14],1⟩,⟨[13,15],1⟩,⟨[9,13],1⟩,⟨[13,24],1⟩,⟨[25],2⟩,⟨[9,25],1⟩,⟨[11,14,15,25],1⟩,⟨[10,13,25],1⟩,⟨[12],1⟩,⟨[12,14],1⟩,⟨[9,12,15],1⟩,⟨[10,12],1⟩,⟨[11,12,13],1⟩,⟨[12,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case103

namespace Case104
def positionFn : Fin 9 → Fin 25 := ![11,12,8,9,10,23,14,13,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{2},{3},{0,3},{1,3},{4},{0,4},{1,4},{5},{0,5},{1,5},{2,3,4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,7},{4,7},{3,6,7},{8},{0,1,2,8},{3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,3,4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={4,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={0,1,2,8} then 1 else if T={3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9],2⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[10,13],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[11,13],1⟩,⟨[24],1⟩,⟨[12,24],1⟩,⟨[13,24],1⟩,⟨[9,10,11,24],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[9,15],1⟩,⟨[15,24],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[9,14],1⟩,⟨[11,14],1⟩,⟨[10,14,15],1⟩,⟨[25],2⟩,⟨[9,12,13,25],1⟩,⟨[10,25],1⟩,⟨[11,15,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case104

namespace Case105
def positionFn : Fin 9 → Fin 25 := ![11,12,8,9,23,10,14,13,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{3},{0,3},{1,3},{4},{0,4},{1,4},{5},{2,3,4,5},{0,6},{1,6},{2,6},{4,6},{0,7},{1,7},{2,7},{3,7},{5,6,7},{8},{2,8},{0,1,5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 3 else if T={2,3,4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,6,7} then 1 else if T={8} then 2 else if T={2,8} then 1 else if T={0,1,5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9,12],1⟩,⟨[9,13],1⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[10,13],1⟩,⟨[24],1⟩,⟨[12,24],1⟩,⟨[13,24],1⟩,⟨[11],3⟩,⟨[9,10,11,24],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[9,15],1⟩,⟨[15,24],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[11,14,15],1⟩,⟨[25],2⟩,⟨[9,25],1⟩,⟨[11,12,13,25],1⟩,⟨[10,15,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case105

namespace Case106
def positionFn : Fin 9 → Fin 25 := ![8,9,13,10,11,14,12,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,3},{1,3},{4},{0,4},{2,4},{5},{1,5},{2,5},{6},{0,1,6},{2,3,6},{4,5,6},{7},{0,2,7},{1,4,7},{3,5,7},{8},{1,2,8},{3,4,8},{0,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 2 else if T={0,1,6} then 1 else if T={2,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={0,2,7} then 1 else if T={1,4,7} then 1 else if T={3,5,7} then 1 else if T={8} then 2 else if T={1,2,8} then 1 else if T={3,4,8} then 1 else if T={0,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[14],1⟩,⟨[11],1⟩,⟨[9,11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[14,15],1⟩,⟨[13],2⟩,⟨[9,10,13],1⟩,⟨[11,13,14],1⟩,⟨[12,13,15],1⟩,⟨[24],2⟩,⟨[9,14,24],1⟩,⟨[10,12,24],1⟩,⟨[11,15,24],1⟩,⟨[25],2⟩,⟨[10,14,25],1⟩,⟨[11,12,25],1⟩,⟨[9,15,25],1⟩,⟨[13,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case106

namespace Case107
def positionFn : Fin 9 → Fin 25 := ![10,8,9,13,11,14,12,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{3},{0,3},{4},{0,4},{3,4},{5},{1,5},{2,5},{6},{0,1,6},{2,3,6},{4,5,6},{7},{0,2,7},{1,4,7},{3,5,7},{8},{1,3,8},{2,4,8},{0,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 2 else if T={0,1,6} then 1 else if T={2,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={0,2,7} then 1 else if T={1,4,7} then 1 else if T={3,5,7} then 1 else if T={8} then 2 else if T={1,3,8} then 1 else if T={2,4,8} then 1 else if T={0,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[11],1⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[9,10],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[10,15],1⟩,⟨[13],2⟩,⟨[9,11,13],1⟩,⟨[10,13,14],1⟩,⟨[12,13,15],1⟩,⟨[24],2⟩,⟨[10,11,24],1⟩,⟨[9,12,24],1⟩,⟨[14,15,24],1⟩,⟨[25],2⟩,⟨[9,14,25],1⟩,⟨[10,12,25],1⟩,⟨[11,15,25],1⟩,⟨[13,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case107

namespace Case108
def positionFn : Fin 9 → Fin 25 := ![11,8,10,14,12,13,9,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1,2},{0,3},{1,3},{0,4},{2,4},{3,4},{0,5},{1,5},{2,5},{6},{0,1,6},{2,3,6},{4,6},{5,6},{7},{1,7},{0,2,7},{3,7},{4,5,7},{8},{0,8},{2,8},{1,4,8},{3,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 9 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 1 else if T={0,1,6} then 1 else if T={2,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={0,2,7} then 1 else if T={3,7} then 1 else if T={4,5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,4,8} then 1 else if T={3,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],9⟩,⟨[9,11],1⟩,⟨[12,15],1⟩,⟨[9,15],1⟩,⟨[12,13],1⟩,⟨[11,13],1⟩,⟨[13,15],1⟩,⟨[12,14],1⟩,⟨[9,14],1⟩,⟨[11,14],1⟩,⟨[10],1⟩,⟨[9,10,12],1⟩,⟨[10,11,15],1⟩,⟨[10,13],1⟩,⟨[10,14],1⟩,⟨[24],1⟩,⟨[9,24],1⟩,⟨[11,12,24],1⟩,⟨[15,24],1⟩,⟨[13,14,24],1⟩,⟨[25],1⟩,⟨[12,25],1⟩,⟨[11,25],1⟩,⟨[9,13,25],1⟩,⟨[14,15,25],1⟩,⟨[10,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case108

namespace Case109
def positionFn : Fin 9 → Fin 25 := ![8,11,12,14,10,13,9,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{2,4},{3,4},{0,5},{1,5},{4,5},{6},{0,1,6},{2,3,6},{4,6},{5,6},{7},{1,7},{3,7},{0,4,7},{2,5,7},{8},{0,8},{2,8},{1,4,8},{3,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 9 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,1,6} then 1 else if T={2,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={0,4,7} then 1 else if T={2,5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,4,8} then 1 else if T={3,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],9⟩,⟨[9,13],1⟩,⟨[12,13],1⟩,⟨[9,15],1⟩,⟨[12,15],1⟩,⟨[11,13],1⟩,⟨[11,15],1⟩,⟨[9,14],1⟩,⟨[12,14],1⟩,⟨[11,14],1⟩,⟨[10],1⟩,⟨[9,10,12],1⟩,⟨[10,13,15],1⟩,⟨[10,11],1⟩,⟨[10,14],1⟩,⟨[24],1⟩,⟨[12,24],1⟩,⟨[15,24],1⟩,⟨[9,11,24],1⟩,⟨[13,14,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[13,25],1⟩,⟨[11,12,25],1⟩,⟨[14,15,25],1⟩,⟨[10,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case109

namespace Case110
def positionFn : Fin 9 → Fin 25 := ![8,12,10,14,13,11,9,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{1,4},{2,4},{0,5},{3,5},{4,5},{6},{0,1,6},{2,3,6},{4,6},{5,6},{7},{1,7},{3,7},{0,4,7},{2,5,7},{8},{0,8},{2,8},{3,4,8},{1,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 9 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,1,6} then 1 else if T={2,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={0,4,7} then 1 else if T={2,5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={1,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],9⟩,⟨[9,11],1⟩,⟨[11,13],1⟩,⟨[9,15],1⟩,⟨[13,15],1⟩,⟨[13,14],1⟩,⟨[11,14],1⟩,⟨[9,12],1⟩,⟨[12,15],1⟩,⟨[12,14],1⟩,⟨[10],1⟩,⟨[9,10,13],1⟩,⟨[10,11,15],1⟩,⟨[10,14],1⟩,⟨[10,12],1⟩,⟨[24],1⟩,⟨[13,24],1⟩,⟨[15,24],1⟩,⟨[9,14,24],1⟩,⟨[11,12,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[11,25],1⟩,⟨[14,15,25],1⟩,⟨[12,13,25],1⟩,⟨[10,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case110

namespace Case111
def positionFn : Fin 9 → Fin 25 := ![8,14,11,13,10,12,9,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{6},{0,1,6},{3,6},{2,4,6},{7},{1,7},{0,2,7},{3,5,7},{6,7},{8},{0,8},{2,8},{1,3,8},{5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 9 else if T={1,2} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,1,6} then 1 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={0,2,7} then 1 else if T={3,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,3,8} then 1 else if T={5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],9⟩,⟨[12,15],1⟩,⟨[9,14],1⟩,⟨[12,14],1⟩,⟨[9,11],1⟩,⟨[11,15],1⟩,⟨[11,14],1⟩,⟨[9,13],1⟩,⟨[13,15],1⟩,⟨[12,13],1⟩,⟨[11,13],1⟩,⟨[10],1⟩,⟨[9,10,15],1⟩,⟨[10,14],1⟩,⟨[10,11,12],1⟩,⟨[24],1⟩,⟨[15,24],1⟩,⟨[9,12,24],1⟩,⟨[13,14,24],1⟩,⟨[10,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[12,25],1⟩,⟨[14,15,25],1⟩,⟨[10,13,25],1⟩,⟨[11,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case111

namespace Case112
def positionFn : Fin 9 → Fin 25 := ![8,11,10,14,12,13,9,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{4,5},{6},{0,1,6},{2,6},{3,4,6},{7},{1,7},{0,2,7},{3,5,7},{6,7},{8},{0,8},{1,2,8},{3,8},{5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 9 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={0,2,7} then 1 else if T={3,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={3,8} then 1 else if T={5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],9⟩,⟨[9,15],1⟩,⟨[12,15],1⟩,⟨[11,15],1⟩,⟨[9,13],1⟩,⟨[12,13],1⟩,⟨[11,13],1⟩,⟨[9,14],1⟩,⟨[12,14],1⟩,⟨[11,14],1⟩,⟨[13,14],1⟩,⟨[10],1⟩,⟨[9,10,12],1⟩,⟨[10,11],1⟩,⟨[10,13,15],1⟩,⟨[24],1⟩,⟨[12,24],1⟩,⟨[9,11,24],1⟩,⟨[14,15,24],1⟩,⟨[10,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[11,12,25],1⟩,⟨[15,25],1⟩,⟨[10,14,25],1⟩,⟨[13,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case112

namespace Case113
def positionFn : Fin 9 → Fin 25 := ![8,12,11,14,13,10,9,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1,2},{0,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{3,5},{4,5},{6},{1,6},{0,2,6},{3,4,6},{7},{0,7},{1,3,7},{2,5,7},{6,7},{8},{0,1,8},{2,8},{3,8},{5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 9 else if T={1,2} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={0,2,6} then 1 else if T={3,4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={2,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],9⟩,⟨[12,13],1⟩,⟨[9,15],1⟩,⟨[12,15],1⟩,⟨[9,14],1⟩,⟨[13,14],1⟩,⟨[12,14],1⟩,⟨[9,11],1⟩,⟨[11,13],1⟩,⟨[11,15],1⟩,⟨[11,14],1⟩,⟨[10],1⟩,⟨[10,13],1⟩,⟨[9,10,12],1⟩,⟨[10,14,15],1⟩,⟨[24],1⟩,⟨[9,24],1⟩,⟨[13,15,24],1⟩,⟨[11,12,24],1⟩,⟨[10,24],1⟩,⟨[25],1⟩,⟨[9,13,25],1⟩,⟨[12,25],1⟩,⟨[15,25],1⟩,⟨[10,11,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case113

namespace Case114
def positionFn : Fin 9 → Fin 25 := ![10,11,8,14,12,13,23,9,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{4,5},{6},{0,1,2,6},{3,6},{7},{0,7},{1,7},{3,4,7},{5,6,7},{8},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={3,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[9],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[9,15],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[9,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[9,14],1⟩,⟨[13,14],1⟩,⟨[24],2⟩,⟨[9,11,12,24],1⟩,⟨[15,24],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[10,12],1⟩,⟨[10,13,15],1⟩,⟨[10,14,24],1⟩,⟨[25],1⟩,⟨[11,25],1⟩,⟨[12,25],1⟩,⟨[14,15,25],1⟩,⟨[13,24,25],1⟩,⟨[9,10,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case114

namespace Case115
def positionFn : Fin 9 → Fin 25 := ![8,9,10,11,12,13,23,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,3},{2,3},{0,4},{2,4},{3,4},{0,5},{1,5},{2,5},{4,5},{6},{0,1,2,6},{3,6},{7},{0,7},{1,7},{3,5,7},{4,6,7},{8},{0,3,8},{1,4,8},{5,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={3,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,3,8} then 1 else if T={1,4,8} then 1 else if T={5,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[9,13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[13,14],1⟩,⟨[24],2⟩,⟨[9,10,11,24],1⟩,⟨[12,24],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[10,15],1⟩,⟨[12,14,15],1⟩,⟨[13,15,24],1⟩,⟨[25],2⟩,⟨[9,12,25],1⟩,⟨[10,13,25],1⟩,⟨[14,24,25],1⟩,⟨[11,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case115

namespace Case116
def positionFn : Fin 9 → Fin 25 := ![10,11,13,8,9,12,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{0,2},{1,2},{3},{1,3},{2,3},{4},{0,4},{2,4},{5},{0,5},{1,5},{6},{0,3,6},{4,5,6},{7},{1,4,7},{3,5,7},{2,6,7},{8},{3,4,8},{2,5,8},{1,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={6} then 2 else if T={0,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={1,4,7} then 1 else if T={3,5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 2 else if T={3,4,8} then 1 else if T={2,5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[11,12],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[9],1⟩,⟨[9,12],1⟩,⟨[9,14],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[10,14],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[15],2⟩,⟨[9,11,15],1⟩,⟨[10,13,15],1⟩,⟨[24],2⟩,⟨[10,12,24],1⟩,⟨[9,13,24],1⟩,⟨[14,15,24],1⟩,⟨[25],2⟩,⟨[9,10,25],1⟩,⟨[13,14,25],1⟩,⟨[12,15,25],1⟩,⟨[11,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case116

namespace Case117
def positionFn : Fin 9 → Fin 25 := ![8,9,22,10,11,23,13,12,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{2,3},{4},{1,4},{3,4},{5},{0,5},{3,5},{4,5},{6},{2,6},{0,1,3,6},{7},{1,7},{0,2,4,7},{5,6,7},{8},{0,8},{1,2,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,1,3,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,2,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],4⟩,⟨[9],2⟩,⟨[10],2⟩,⟨[23],2⟩,⟨[11],1⟩,⟨[11,23],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[24],1⟩,⟨[9,24],1⟩,⟨[11,24],1⟩,⟨[12,24],1⟩,⟨[14],2⟩,⟨[14,23],1⟩,⟨[9,10,11,14],1⟩,⟨[13],2⟩,⟨[10,13],1⟩,⟨[9,12,13,23],1⟩,⟨[13,14,24],1⟩,⟨[25],2⟩,⟨[9,25],1⟩,⟨[10,23,24,25],1⟩,⟨[12,14,25],1⟩,⟨[11,13,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case117

namespace Case118
def positionFn : Fin 9 → Fin 25 := ![11,8,9,12,10,13,23,24,14]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{2,3},{4},{0,4},{3,4},{0,5},{1,5},{3,5},{4,5},{6},{2,6},{0,1,3,6},{7},{0,7},{1,2,4,7},{5,6,7},{8},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={1} then 2 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,1,3,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,2,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[9],2⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[11,13],1⟩,⟨[12,14],1⟩,⟨[9,14],1⟩,⟨[13,14],1⟩,⟨[11,14],1⟩,⟨[24],2⟩,⟨[10,24],1⟩,⟨[9,12,13,24],1⟩,⟨[25],2⟩,⟨[12,25],1⟩,⟨[9,10,11,25],1⟩,⟨[14,24,25],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[9,15],1⟩,⟨[10,14,15],1⟩,⟨[11,15,24],1⟩,⟨[13,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case118

namespace Case119
def positionFn : Fin 9 → Fin 25 := ![10,13,12,8,9,14,11,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{1,2},{3},{1,3},{4},{0,4},{3,4},{5},{0,5},{2,5},{6},{0,6},{1,6},{2,3,6},{4,5,6},{7},{0,2,7},{1,4,7},{3,5,7},{8},{0,3,8},{2,4,8},{1,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={0,2,7} then 1 else if T={1,4,7} then 1 else if T={3,5,7} then 1 else if T={8} then 2 else if T={0,3,8} then 1 else if T={2,4,8} then 1 else if T={1,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[11,14],1⟩,⟨[13],1⟩,⟨[13,14],1⟩,⟨[9],1⟩,⟨[9,14],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[9,10],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[12,14],1⟩,⟨[9,12,13],1⟩,⟨[10,12,15],1⟩,⟨[24],2⟩,⟨[11,13,24],1⟩,⟨[10,14,24],1⟩,⟨[9,15,24],1⟩,⟨[25],2⟩,⟨[9,11,25],1⟩,⟨[10,13,25],1⟩,⟨[14,15,25],1⟩,⟨[12,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case119

namespace Case120
def positionFn : Fin 9 → Fin 25 := ![12,11,13,8,9,14,23,10,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{1,2},{3},{0,3},{4},{0,4},{3,4},{5},{1,5},{2,5},{6},{0,6},{1,6},{2,3,6},{4,5,6},{7},{0,2,7},{1,4,7},{3,5,7},{8},{1,3,8},{2,4,8},{0,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={0,2,7} then 1 else if T={1,4,7} then 1 else if T={3,5,7} then 1 else if T={8} then 2 else if T={1,3,8} then 1 else if T={2,4,8} then 1 else if T={0,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[9],1⟩,⟨[9,13],1⟩,⟨[10],1⟩,⟨[10,13],1⟩,⟨[9,10],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[24],1⟩,⟨[13,24],1⟩,⟨[12,24],1⟩,⟨[9,14,24],1⟩,⟨[10,15,24],1⟩,⟨[11],2⟩,⟨[11,13,14],1⟩,⟨[10,11,12],1⟩,⟨[9,11,15],1⟩,⟨[25],2⟩,⟨[9,12,25],1⟩,⟨[10,14,25],1⟩,⟨[13,15,25],1⟩,⟨[11,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case120

namespace Case121
def positionFn : Fin 9 → Fin 25 := ![8,9,10,11,22,23,24,13,12]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{3},{1,3},{4},{0,4},{3,4},{5},{0,5},{2,5},{6},{0,2,3,6},{1,4,5,6},{0,1,7},{2,7},{3,7},{4,7},{5,7},{8},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={6} then 3 else if T={0,2,3,6} then 1 else if T={1,4,5,6} then 1 else if T={0,1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],6⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[23],1⟩,⟨[9,23],1⟩,⟨[12,23],1⟩,⟨[24],1⟩,⟨[9,24],1⟩,⟨[11,24],1⟩,⟨[25],3⟩,⟨[9,11,12,25],1⟩,⟨[10,23,24,25],1⟩,⟨[9,10,14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[14,23],1⟩,⟨[14,24],1⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[11,13,23],1⟩,⟨[12,13,24],1⟩,⟨[13,14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case121

namespace Case122
def positionFn : Fin 9 → Fin 25 := ![10,22,8,11,9,23,24,13,12]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{1,2},{3},{1,3},{4},{0,4},{3,4},{5},{0,5},{2,5},{6},{0,2,3,6},{1,4,5,6},{0,7},{1,7},{3,7},{2,4,7},{5,7},{0,8},{1,8},{2,8},{4,8},{3,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={6} then 3 else if T={0,2,3,6} then 1 else if T={1,4,5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={4,8} then 1 else if T={3,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],7⟩,⟨[11,23],1⟩,⟨[9],1⟩,⟨[9,23],1⟩,⟨[12],1⟩,⟨[12,23],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[10,12],1⟩,⟨[24],1⟩,⟨[11,24],1⟩,⟨[9,24],1⟩,⟨[25],3⟩,⟨[9,11,12,25],1⟩,⟨[10,23,24,25],1⟩,⟨[11,14],1⟩,⟨[14,23],1⟩,⟨[12,14],1⟩,⟨[9,10,14],1⟩,⟨[14,24],1⟩,⟨[11,13],1⟩,⟨[13,23],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[12,13,24],1⟩,⟨[13,14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case122

namespace Case123
def positionFn : Fin 9 → Fin 25 := ![21,9,22,23,13,11,24,10,12]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,4},{2,4},{3,4},{0,5},{1,5},{3,5},{4,5},{6},{0,1,2,3,6},{7},{0,7},{2,7},{1,4,7},{5,6,7},{8},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={0,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={0,1,2,3,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,22,23,24,25],[⟨[],5⟩,⟨[22],1⟩,⟨[10],2⟩,⟨[23],2⟩,⟨[24],2⟩,⟨[14,22],1⟩,⟨[14,23],1⟩,⟨[14,24],1⟩,⟨[12,22],1⟩,⟨[10,12],1⟩,⟨[12,24],1⟩,⟨[12,14],1⟩,⟨[25],3⟩,⟨[10,22,23,24,25],1⟩,⟨[11],1⟩,⟨[11,22],1⟩,⟨[11,23],1⟩,⟨[10,11,14],1⟩,⟨[11,12,25],1⟩,⟨[13],1⟩,⟨[13,22],1⟩,⟨[10,13],1⟩,⟨[12,13,23],1⟩,⟨[13,14,25],1⟩,⟨[11,13,24],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case123

namespace Case124
def positionFn : Fin 9 → Fin 25 := ![9,21,22,23,10,13,24,12,11]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{2,3},{4},{1,4},{5},{0,5},{4,5},{6},{2,6},{3,6},{0,4,6},{1,5,6},{7},{0,7},{1,7},{2,4,7},{3,5,7},{8},{0,1,8},{3,4,8},{2,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={0,4,6} then 1 else if T={1,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={3,5,7} then 1 else if T={8} then 2 else if T={0,1,8} then 1 else if T={3,4,8} then 1 else if T={2,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,22,23,24,25],[⟨[],8⟩,⟨[10,23],1⟩,⟨[22,23],1⟩,⟨[10,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[11],1⟩,⟨[11,22],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[25],1⟩,⟨[23,25],1⟩,⟨[24,25],1⟩,⟨[10,11,25],1⟩,⟨[14,22,25],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[13,22],1⟩,⟨[11,13,23],1⟩,⟨[13,14,24],1⟩,⟨[12],2⟩,⟨[10,12,22],1⟩,⟨[11,12,24],1⟩,⟨[12,14,23],1⟩,⟨[12,13,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case124

namespace Case125
def positionFn : Fin 9 → Fin 25 := ![21,9,22,23,13,10,12,24,11]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{2,3},{4},{1,4},{5},{0,5},{4,5},{6},{1,6},{3,6},{0,4,6},{2,5,6},{7},{0,7},{2,7},{3,4,7},{1,5,7},{8},{0,1,8},{2,4,8},{3,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={0,4,6} then 1 else if T={2,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={1,5,7} then 1 else if T={8} then 2 else if T={0,1,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,22,23,24,25],[⟨[],8⟩,⟨[22,23],1⟩,⟨[10,23],1⟩,⟨[22,24],1⟩,⟨[10,24],1⟩,⟨[23,24],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11],1⟩,⟨[11,22],1⟩,⟨[11,14],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[13,24],1⟩,⟨[13,14,22],1⟩,⟨[11,13,23],1⟩,⟨[25],1⟩,⟨[22,25],1⟩,⟨[23,25],1⟩,⟨[14,24,25],1⟩,⟨[10,11,25],1⟩,⟨[12],2⟩,⟨[10,12,22],1⟩,⟨[12,14,23],1⟩,⟨[11,12,24],1⟩,⟨[12,13,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case125

namespace Case126
def positionFn : Fin 9 → Fin 25 := ![8,9,12,11,23,13,10,24,14]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{0,3},{1,3},{2,3},{4},{5},{4,5},{6},{2,6},{0,1,4,6},{3,5,6},{7},{1,7},{3,4,7},{0,2,5,7},{8},{0,8},{3,8},{2,4,8},{1,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 2 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={5} then 2 else if T={4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,1,4,6} then 1 else if T={3,5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={0,2,5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={3,8} then 1 else if T={2,4,8} then 1 else if T={1,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],5⟩,⟨[9],2⟩,⟨[10],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[9,12],1⟩,⟨[10,12],1⟩,⟨[12,13],1⟩,⟨[24],2⟩,⟨[14],2⟩,⟨[14,24],1⟩,⟨[11],2⟩,⟨[11,13],1⟩,⟨[9,10,11,24],1⟩,⟨[11,12,14],1⟩,⟨[25],2⟩,⟨[10,25],1⟩,⟨[12,24,25],1⟩,⟨[9,13,14,25],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[12,15],1⟩,⟨[13,15,24],1⟩,⟨[10,14,15],1⟩,⟨[11,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case126

namespace Case127
def positionFn : Fin 9 → Fin 25 := ![8,9,12,13,11,23,10,24,14]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{6},{3,6},{2,4,6},{7},{2,7},{3,5,7},{0,1,6,7},{8},{0,2,8},{1,3,8},{5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={3,5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={0,2,8} then 1 else if T={1,3,8} then 1 else if T={5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[10,13],1⟩,⟨[9,14],1⟩,⟨[13,14],1⟩,⟨[9,12],1⟩,⟨[10,12],1⟩,⟨[12,14],1⟩,⟨[9,24],1⟩,⟨[10,24],1⟩,⟨[13,24],1⟩,⟨[12,24],1⟩,⟨[11],2⟩,⟨[11,14],1⟩,⟨[11,12,13],1⟩,⟨[25],2⟩,⟨[13,25],1⟩,⟨[14,24,25],1⟩,⟨[9,10,11,25],1⟩,⟨[15],2⟩,⟨[9,13,15],1⟩,⟨[10,14,15],1⟩,⟨[11,15,24],1⟩,⟨[12,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case127

namespace Case128
def positionFn : Fin 9 → Fin 25 := ![8,9,14,12,13,11,10,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{6},{3,6},{2,4,6},{7},{2,7},{3,5,7},{0,1,6,7},{8},{0,8},{1,8},{2,3,8},{5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={3,5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[9,15],1⟩,⟨[10,15],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[9,12],1⟩,⟨[10,12],1⟩,⟨[12,15],1⟩,⟨[12,14],1⟩,⟨[11],2⟩,⟨[11,13],1⟩,⟨[11,14,15],1⟩,⟨[24],2⟩,⟨[15,24],1⟩,⟨[12,13,24],1⟩,⟨[9,10,11,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[10,25],1⟩,⟨[13,15,25],1⟩,⟨[11,12,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case128

namespace Case129
def positionFn : Fin 9 → Fin 25 := ![13,8,9,10,11,12,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{6},{3,6},{2,4,6},{7},{2,7},{3,5,7},{0,1,6,7},{8},{0,8},{1,2,3,8},{5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={1} then 2 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={3,5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,3,8} then 1 else if T={5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[9],2⟩,⟨[10],1⟩,⟨[10,14],1⟩,⟨[11],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[9,12],1⟩,⟨[11,12],1⟩,⟨[13,14],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[10,12,15],1⟩,⟨[24],2⟩,⟨[10,24],1⟩,⟨[11,13,24],1⟩,⟨[9,14,15,24],1⟩,⟨[25],2⟩,⟨[14,25],1⟩,⟨[9,10,11,25],1⟩,⟨[13,15,25],1⟩,⟨[12,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case129

namespace Case130
def positionFn : Fin 9 → Fin 25 := ![8,22,9,23,10,11,13,24,12]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{3},{0,3},{2,3},{4},{0,5},{1,5},{2,5},{3,5},{6},{1,6},{0,2,4,6},{7},{0,7},{1,3,4,7},{5,6,7},{8},{0,1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 3 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,2,4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 2 else if T={0,1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],5⟩,⟨[9],1⟩,⟨[23],1⟩,⟨[10],1⟩,⟨[10,23],1⟩,⟨[24],1⟩,⟨[9,24],1⟩,⟨[10,24],1⟩,⟨[11],3⟩,⟨[9,12],1⟩,⟨[12,23],1⟩,⟨[10,12],1⟩,⟨[12,24],1⟩,⟨[14],2⟩,⟨[14,23],1⟩,⟨[9,10,11,14],1⟩,⟨[25],2⟩,⟨[9,25],1⟩,⟨[11,23,24,25],1⟩,⟨[12,14,25],1⟩,⟨[13],2⟩,⟨[9,13,23],1⟩,⟨[11,12,13],1⟩,⟨[13,14,24],1⟩,⟨[10,13,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case130

namespace Case131
def positionFn : Fin 9 → Fin 25 := ![8,11,9,12,10,13,23,24,14]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{1,2},{3},{0,3},{2,3},{4},{0,5},{1,5},{2,5},{3,5},{6},{1,6},{0,2,4,6},{7},{0,7},{1,3,4,7},{5,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 3 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,2,4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[9,12],1⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[11],3⟩,⟨[9,14],1⟩,⟨[12,14],1⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[24],2⟩,⟨[12,24],1⟩,⟨[9,10,11,24],1⟩,⟨[25],2⟩,⟨[9,25],1⟩,⟨[11,12,13,25],1⟩,⟨[14,24,25],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[12,15],1⟩,⟨[11,14,15],1⟩,⟨[13,15,24],1⟩,⟨[10,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case131

namespace Case132
def positionFn : Fin 9 → Fin 25 := ![11,13,8,23,9,10,12,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{0,2},{1,2},{3},{2,3},{4},{1,4},{5},{0,5},{6},{1,6},{2,6},{0,3,4,6},{5,6},{7},{0,7},{2,7},{4,7},{1,3,5,7},{8},{0,8},{1,8},{3,8},{2,4,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={0,3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={4,7} then 1 else if T={1,3,5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,8} then 1 else if T={2,4,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[12,14],1⟩,⟨[9,12],1⟩,⟨[9,14],1⟩,⟨[24],2⟩,⟨[9,24],1⟩,⟨[10],2⟩,⟨[10,14],1⟩,⟨[11],2⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[13,14],1⟩,⟨[9,13],1⟩,⟨[10,12,13,24],1⟩,⟨[11,13],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[9,15],1⟩,⟨[10,15],1⟩,⟨[11,14,15,24],1⟩,⟨[25],1⟩,⟨[12,25],1⟩,⟨[14,25],1⟩,⟨[24,25],1⟩,⟨[9,10,11,25],1⟩,⟨[13,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case132

namespace Case133
def positionFn : Fin 9 → Fin 25 := ![8,9,14,11,12,10,23,13,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{5},{2,5},{6},{2,6},{0,1,5,6},{7},{1,7},{0,2,7},{3,5,7},{4,6,7},{8},{0,8},{1,2,8},{4,5,8},{3,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,1,5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={0,2,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[9,12],1⟩,⟨[10,12],1⟩,⟨[12,15],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[13,15],1⟩,⟨[12,13],1⟩,⟨[11],2⟩,⟨[11,15],1⟩,⟨[24],2⟩,⟨[15,24],1⟩,⟨[9,10,11,24],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[9,14,15],1⟩,⟨[11,12,14],1⟩,⟨[13,14,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[10,15,25],1⟩,⟨[11,13,25],1⟩,⟨[12,24,25],1⟩,⟨[14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case133

namespace Case134
def positionFn : Fin 9 → Fin 25 := ![8,9,11,14,12,10,23,13,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{2,3},{0,4},{1,4},{2,4},{3,4},{5},{2,5},{6},{3,6},{0,1,5,6},{7},{1,7},{0,2,7},{3,5,7},{4,6,7},{8},{0,8},{1,3,8},{4,5,8},{2,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={0,1,5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={0,2,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={4,5,8} then 1 else if T={2,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[9,15],1⟩,⟨[12,15],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[13,15],1⟩,⟨[11],2⟩,⟨[11,12],1⟩,⟨[24],2⟩,⟨[15,24],1⟩,⟨[9,10,11,24],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[9,12,14],1⟩,⟨[11,14,15],1⟩,⟨[13,14,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[10,15,25],1⟩,⟨[11,13,25],1⟩,⟨[12,24,25],1⟩,⟨[14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case134

namespace Case135
def positionFn : Fin 9 → Fin 25 := ![8,13,9,11,12,10,23,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{5},{1,5},{6},{1,6},{0,2,5,6},{7},{0,7},{3,5,7},{4,6,7},{8},{0,8},{4,5,8},{3,6,8},{1,2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,1} then 1 else if T={2} then 2 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,2,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={1,2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[9,14],1⟩,⟨[10],2⟩,⟨[9,12],1⟩,⟨[12,14],1⟩,⟨[10,12],1⟩,⟨[9,13],1⟩,⟨[13,14],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[11],2⟩,⟨[11,14],1⟩,⟨[24],2⟩,⟨[14,24],1⟩,⟨[9,10,11,24],1⟩,⟨[15],2⟩,⟨[9,15],1⟩,⟨[11,12,15],1⟩,⟨[13,15,24],1⟩,⟨[25],2⟩,⟨[9,25],1⟩,⟨[11,13,25],1⟩,⟨[12,24,25],1⟩,⟨[10,14,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case135

namespace Case136
def positionFn : Fin 9 → Fin 25 := ![21,22,9,11,12,23,24,10,13]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{5},{6},{0,1,2,5,6},{7},{0,7},{1,7},{3,5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 3 else if T={6} then 3 else if T={0,1,2,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,22,23,24,25],[⟨[],5⟩,⟨[22],1⟩,⟨[23],1⟩,⟨[10],2⟩,⟨[12,22],1⟩,⟨[12,23],1⟩,⟨[10,12],1⟩,⟨[13,22],1⟩,⟨[13,23],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[24],3⟩,⟨[25],3⟩,⟨[10,22,23,24,25],1⟩,⟨[11],1⟩,⟨[11,22],1⟩,⟨[11,23],1⟩,⟨[11,12,24],1⟩,⟨[11,13,25],1⟩,⟨[14],1⟩,⟨[14,22],1⟩,⟨[14,23],1⟩,⟨[13,14,24],1⟩,⟨[12,14,25],1⟩,⟨[10,11,14],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case136

namespace Case137
def positionFn : Fin 9 → Fin 25 := ![11,8,10,12,13,14,23,9,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{5},{0,5},{1,5},{6},{0,6},{2,6},{3,5,6},{7},{0,1,7},{2,5,7},{4,6,7},{8},{0,2,8},{4,5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,5,6} then 1 else if T={7} then 2 else if T={0,1,7} then 1 else if T={2,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,2,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[9,11],1⟩,⟨[12,13],1⟩,⟨[9,13],1⟩,⟨[11,13],1⟩,⟨[12,14],1⟩,⟨[9,14],1⟩,⟨[11,14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[9,15],1⟩,⟨[24],1⟩,⟨[12,24],1⟩,⟨[11,24],1⟩,⟨[13,15,24],1⟩,⟨[10],2⟩,⟨[9,10,12],1⟩,⟨[10,11,15],1⟩,⟨[10,14,24],1⟩,⟨[25],2⟩,⟨[11,12,25],1⟩,⟨[14,15,25],1⟩,⟨[9,24,25],1⟩,⟨[10,13,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case137

namespace Case138
def positionFn : Fin 9 → Fin 25 := ![8,9,10,11,12,14,13,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{4,6},{3,5,6},{7},{0,1,2,7},{3,7},{4,5,7},{8},{0,8},{1,3,8},{2,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={1} then 1 else if T={2} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={3,5,6} then 1 else if T={7} then 2 else if T={0,1,2,7} then 1 else if T={3,7} then 1 else if T={4,5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[9,12],1⟩,⟨[11,12],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[9,15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[13,14],1⟩,⟨[12,14,15],1⟩,⟨[24],2⟩,⟨[9,10,11,24],1⟩,⟨[12,24],1⟩,⟨[13,15,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[10,12,25],1⟩,⟨[11,13,25],1⟩,⟨[15,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case138

namespace Case139
def positionFn : Fin 9 → Fin 25 := ![8,10,11,12,13,9,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{5},{1,5},{3,5},{6},{0,6},{2,6},{4,5,6},{7},{0,1,7},{2,5,7},{3,6,7},{8},{2,3,8},{0,5,8},{1,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={0,1,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={2,3,8} then 1 else if T={0,5,8} then 1 else if T={1,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[9,12],1⟩,⟨[11,12],1⟩,⟨[9,13],1⟩,⟨[11,13],1⟩,⟨[9,14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[10,13],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[12,15],1⟩,⟨[10,14,15],1⟩,⟨[24],2⟩,⟨[9,11,24],1⟩,⟨[10,12,24],1⟩,⟨[13,15,24],1⟩,⟨[25],2⟩,⟨[12,13,25],1⟩,⟨[9,10,25],1⟩,⟨[11,15,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case139

namespace Case140
def positionFn : Fin 9 → Fin 25 := ![8,11,14,12,9,10,23,13,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{0,2},{1,2},{0,3},{1,3},{2,3},{4},{3,4},{5},{1,5},{6},{2,6},{0,4,5,6},{7},{0,7},{1,4,7},{2,5,7},{3,6,7},{8},{0,8},{2,4,8},{3,5,8},{1,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,4,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,4,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={1,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],7⟩,⟨[9,12],1⟩,⟨[9,15],1⟩,⟨[12,15],1⟩,⟨[9,13],1⟩,⟨[12,13],1⟩,⟨[13,15],1⟩,⟨[10],2⟩,⟨[10,13],1⟩,⟨[11],2⟩,⟨[11,12],1⟩,⟨[24],2⟩,⟨[15,24],1⟩,⟨[9,10,11,24],1⟩,⟨[14],1⟩,⟨[9,14],1⟩,⟨[10,12,14],1⟩,⟨[11,14,15],1⟩,⟨[13,14,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[10,15,25],1⟩,⟨[11,13,25],1⟩,⟨[12,24,25],1⟩,⟨[14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case140

namespace Case141
def positionFn : Fin 9 → Fin 25 := ![8,12,11,13,9,10,23,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{0,2},{1,2},{0,3},{1,3},{2,3},{4},{3,4},{5},{1,5},{6},{2,6},{0,4,5,6},{7},{1,4,7},{2,5,7},{3,6,7},{8},{2,4,8},{3,5,8},{1,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,4,5,6} then 1 else if T={7} then 2 else if T={1,4,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[9],1⟩,⟨[9,13],1⟩,⟨[9,12],1⟩,⟨[12,13],1⟩,⟨[9,14],1⟩,⟨[13,14],1⟩,⟨[12,14],1⟩,⟨[10],2⟩,⟨[10,14],1⟩,⟨[11],2⟩,⟨[11,13],1⟩,⟨[24],2⟩,⟨[12,24],1⟩,⟨[9,10,11,24],1⟩,⟨[15],2⟩,⟨[10,13,15],1⟩,⟨[11,12,15],1⟩,⟨[14,15,24],1⟩,⟨[25],2⟩,⟨[10,12,25],1⟩,⟨[11,14,25],1⟩,⟨[13,24,25],1⟩,⟨[9,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case141

namespace Case142
def positionFn : Fin 9 → Fin 25 := ![8,9,23,12,13,11,14,10,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{7},{0,1,2,7},{3,5,7},{4,6,7},{8},{0,8},{1,3,8},{2,4,8},{5,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={1} then 1 else if T={2} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={7} then 2 else if T={0,1,2,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={2,4,8} then 1 else if T={5,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],8⟩,⟨[10],1⟩,⟨[24],1⟩,⟨[9,13],1⟩,⟨[13,24],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[9,12],1⟩,⟨[10,12],1⟩,⟨[12,24],1⟩,⟨[12,14],1⟩,⟨[9,15],1⟩,⟨[10,15],1⟩,⟨[15,24],1⟩,⟨[13,15],1⟩,⟨[11],2⟩,⟨[9,10,11,24],1⟩,⟨[11,12,13],1⟩,⟨[11,14,15],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[10,13,25],1⟩,⟨[14,24,25],1⟩,⟨[12,15,25],1⟩,⟨[11,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case142

namespace Case143
def positionFn : Fin 9 → Fin 25 := ![8,12,23,9,10,14,11,13,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{1,3},{2,3},{4},{1,4},{2,4},{0,5},{2,5},{4,5},{0,6},{1,6},{3,6},{5,6},{7},{0,1,2,7},{3,5,7},{4,6,7},{8},{0,3,4,8},{1,5,8},{2,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 2 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,1,2,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,3,4,8} then 1 else if T={1,5,8} then 1 else if T={2,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,24,25],[⟨[],6⟩,⟨[9],2⟩,⟨[13],1⟩,⟨[24],1⟩,⟨[10],1⟩,⟨[10,13],1⟩,⟨[10,24],1⟩,⟨[11],1⟩,⟨[11,13],1⟩,⟨[11,24],1⟩,⟨[9,15],1⟩,⟨[15,24],1⟩,⟨[11,15],1⟩,⟨[9,12],1⟩,⟨[12,13],1⟩,⟨[10,12],1⟩,⟨[12,15],1⟩,⟨[14],2⟩,⟨[9,13,14,24],1⟩,⟨[10,14,15],1⟩,⟨[11,12,14],1⟩,⟨[25],2⟩,⟨[9,10,11,25],1⟩,⟨[13,15,25],1⟩,⟨[12,24,25],1⟩,⟨[14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case143

namespace Case144
def positionFn : Fin 9 → Fin 25 := ![7,8,9,13,11,12,23,10,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,6},{7},{3,4,7},{5,6,7},{8},{3,5,8},{4,6,8},{0,1,2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={7} then 3 else if T={3,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 3 else if T={3,5,8} then 1 else if T={4,6,8} then 1 else if T={0,1,2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[8,9,10,11,12,13,14,24,25],[⟨[],6⟩,⟨[8],1⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[8,14],1⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[8,12],1⟩,⟨[9,12],1⟩,⟨[10,12],1⟩,⟨[8,13],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[8,24],1⟩,⟨[9,24],1⟩,⟨[10,24],1⟩,⟨[14,24],1⟩,⟨[11],3⟩,⟨[11,12,14],1⟩,⟨[11,13,24],1⟩,⟨[25],3⟩,⟨[13,14,25],1⟩,⟨[12,24,25],1⟩,⟨[8,9,10,11,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case144

namespace Case145
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,8,22,9,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{0,5},{1,5},{2,5},{3,5},{6},{4,6},{5,6},{7},{2,7},{3,7},{0,1,6,7},{8},{0,8},{1,8},{2,3,6,8},{4,5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={3,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,6,8} then 1 else if T={4,5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,23,24,25],[⟨[],7⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[9,11],1⟩,⟨[9,12],1⟩,⟨[9,13],1⟩,⟨[9,14],1⟩,⟨[11,23],1⟩,⟨[12,23],1⟩,⟨[13,23],1⟩,⟨[14,23],1⟩,⟨[10],2⟩,⟨[9,10],1⟩,⟨[10,23],1⟩,⟨[24],2⟩,⟨[13,24],1⟩,⟨[14,24],1⟩,⟨[10,11,12,24],1⟩,⟨[25],2⟩,⟨[11,25],1⟩,⟨[12,25],1⟩,⟨[10,13,14,25],1⟩,⟨[9,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case145

namespace Case146
def positionFn : Fin 9 → Fin 25 := ![6,7,8,9,10,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,4},{1,4},{2,4},{3,4},{5},{0,5},{1,5},{2,5},{3,5},{6},{0,6},{1,6},{2,6},{3,6},{7},{0,7},{1,7},{2,7},{3,7},{8},{0,1,2,3,8},{4,5,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={8} then 4 else if T={0,1,2,3,8} then 1 else if T={4,5,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[7,8,9,10,11,22,23,24,25],[⟨[],4⟩,⟨[7],1⟩,⟨[8],1⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[7,11],1⟩,⟨[8,11],1⟩,⟨[9,11],1⟩,⟨[10,11],1⟩,⟨[22],1⟩,⟨[7,22],1⟩,⟨[8,22],1⟩,⟨[9,22],1⟩,⟨[10,22],1⟩,⟨[23],1⟩,⟨[7,23],1⟩,⟨[8,23],1⟩,⟨[9,23],1⟩,⟨[10,23],1⟩,⟨[24],1⟩,⟨[7,24],1⟩,⟨[8,24],1⟩,⟨[9,24],1⟩,⟨[10,24],1⟩,⟨[25],4⟩,⟨[7,8,9,10,25],1⟩,⟨[11,22,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case146
def μ : Fin 147 → Finset (Fin 9) → ℕ := ![Case0.μ,Case1.μ,Case2.μ,Case3.μ,Case4.μ,Case5.μ,Case6.μ,Case7.μ,Case8.μ,Case9.μ,Case10.μ,Case11.μ,Case12.μ,Case13.μ,Case14.μ,Case15.μ,Case16.μ,Case17.μ,Case18.μ,Case19.μ,Case20.μ,Case21.μ,Case22.μ,Case23.μ,Case24.μ,Case25.μ,Case26.μ,Case27.μ,Case28.μ,Case29.μ,Case30.μ,Case31.μ,Case32.μ,Case33.μ,Case34.μ,Case35.μ,Case36.μ,Case37.μ,Case38.μ,Case39.μ,Case40.μ,Case41.μ,Case42.μ,Case43.μ,Case44.μ,Case45.μ,Case46.μ,Case47.μ,Case48.μ,Case49.μ,Case50.μ,Case51.μ,Case52.μ,Case53.μ,Case54.μ,Case55.μ,Case56.μ,Case57.μ,Case58.μ,Case59.μ,Case60.μ,Case61.μ,Case62.μ,Case63.μ,Case64.μ,Case65.μ,Case66.μ,Case67.μ,Case68.μ,Case69.μ,Case70.μ,Case71.μ,Case72.μ,Case73.μ,Case74.μ,Case75.μ,Case76.μ,Case77.μ,Case78.μ,Case79.μ,Case80.μ,Case81.μ,Case82.μ,Case83.μ,Case84.μ,Case85.μ,Case86.μ,Case87.μ,Case88.μ,Case89.μ,Case90.μ,Case91.μ,Case92.μ,Case93.μ,Case94.μ,Case95.μ,Case96.μ,Case97.μ,Case98.μ,Case99.μ,Case100.μ,Case101.μ,Case102.μ,Case103.μ,Case104.μ,Case105.μ,Case106.μ,Case107.μ,Case108.μ,Case109.μ,Case110.μ,Case111.μ,Case112.μ,Case113.μ,Case114.μ,Case115.μ,Case116.μ,Case117.μ,Case118.μ,Case119.μ,Case120.μ,Case121.μ,Case122.μ,Case123.μ,Case124.μ,Case125.μ,Case126.μ,Case127.μ,Case128.μ,Case129.μ,Case130.μ,Case131.μ,Case132.μ,Case133.μ,Case134.μ,Case135.μ,Case136.μ,Case137.μ,Case138.μ,Case139.μ,Case140.μ,Case141.μ,Case142.μ,Case143.μ,Case144.μ,Case145.μ,Case146.μ]
end Aris4Math.ThirtyFour.TwentyFiveNineLow

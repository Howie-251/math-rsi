import Aris4Math.ThirtyFour.CachedSparseApplication
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowTenth
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles CachedRows
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case0
def positionFn : Fin 10 → Fin 25 := ![12,20,21,9,10,13,11,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{3},{4},{5},{0,3,5},{1,4,5},{6},{1,3,6},{2,4,6},{7},{2,3,7},{0,4,7},{5,6,7},{8},{3,4,8},{2,5,8},{0,6,8},{1,7,8},{0,1,2,9},{3,9},{4,9},{5,9},{6,9},{7,9},{8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={4} then 1 else if T={5} then 1 else if T={0,3,5} then 1 else if T={1,4,5} then 1 else if T={6} then 1 else if T={1,3,6} then 1 else if T={2,4,6} then 1 else if T={7} then 1 else if T={2,3,7} then 1 else if T={0,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 2 else if T={3,4,8} then 1 else if T={2,5,8} then 1 else if T={0,6,8} then 1 else if T={1,7,8} then 1 else if T={0,1,2,9} then 1 else if T={3,9} then 1 else if T={4,9} then 1 else if T={5,9} then 1 else if T={6,9} then 1 else if T={7,9} then 1 else if T={8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,21,22,23,24,25],[⟨[],3⟩,⟨[13],2⟩,⟨[21],2⟩,⟨[22],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[14],1⟩,⟨[10,13,14],1⟩,⟨[11,14,21],1⟩,⟨[12],1⟩,⟨[10,12,21],1⟩,⟨[11,12,22],1⟩,⟨[23],1⟩,⟨[10,22,23],1⟩,⟨[11,13,23],1⟩,⟨[12,14,23],1⟩,⟨[24],2⟩,⟨[10,11,24],1⟩,⟨[14,22,24],1⟩,⟨[12,13,24],1⟩,⟨[21,23,24],1⟩,⟨[13,21,22,25],1⟩,⟨[10,25],1⟩,⟨[11,25],1⟩,⟨[14,25],1⟩,⟨[12,25],1⟩,⟨[23,25],1⟩,⟨[24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case0

namespace Case1
def positionFn : Fin 10 → Fin 25 := ![12,20,9,13,10,11,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{3},{0,2,3},{4},{1,2,4},{5},{1,3,5},{6},{0,4,6},{2,5,6},{7},{3,4,7},{0,5,7},{1,6,7},{8},{4,5,8},{3,6,8},{2,7,8},{2,9},{3,9},{4,9},{5,9},{6,9},{7,9},{0,1,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 2 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={1,2,4} then 1 else if T={5} then 1 else if T={1,3,5} then 1 else if T={6} then 1 else if T={0,4,6} then 1 else if T={2,5,6} then 1 else if T={7} then 1 else if T={3,4,7} then 1 else if T={0,5,7} then 1 else if T={1,6,7} then 1 else if T={8} then 3 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else if T={2,9} then 1 else if T={3,9} then 1 else if T={4,9} then 1 else if T={5,9} then 1 else if T={6,9} then 1 else if T={7,9} then 1 else if T={0,1,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,21,22,23,24,25],[⟨[],3⟩,⟨[13],2⟩,⟨[21],2⟩,⟨[10],1⟩,⟨[14],1⟩,⟨[10,13,14],1⟩,⟨[11],1⟩,⟨[10,11,21],1⟩,⟨[12],1⟩,⟨[12,14,21],1⟩,⟨[22],1⟩,⟨[11,13,22],1⟩,⟨[10,12,22],1⟩,⟨[23],1⟩,⟨[11,14,23],1⟩,⟨[12,13,23],1⟩,⟨[21,22,23],1⟩,⟨[24],3⟩,⟨[11,12,24],1⟩,⟨[14,22,24],1⟩,⟨[10,23,24],1⟩,⟨[10,25],1⟩,⟨[14,25],1⟩,⟨[11,25],1⟩,⟨[12,25],1⟩,⟨[22,25],1⟩,⟨[23,25],1⟩,⟨[13,21,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1

namespace Case2
def positionFn : Fin 10 → Fin 25 := ![15,16,17,18,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{3},{4},{5},{0,2,5},{1,3,5},{6},{1,2,6},{0,4,6},{7},{0,3,7},{1,4,7},{5,6,7},{8},{4,5,8},{3,6,8},{2,7,8},{9},{2,3,4,9},{5,9},{6,9},{7,9},{0,1,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={4} then 2 else if T={5} then 1 else if T={0,2,5} then 1 else if T={1,3,5} then 1 else if T={6} then 1 else if T={1,2,6} then 1 else if T={0,4,6} then 1 else if T={7} then 1 else if T={0,3,7} then 1 else if T={1,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 3 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else if T={9} then 2 else if T={2,3,4,9} then 1 else if T={5,9} then 1 else if T={6,9} then 1 else if T={7,9} then 1 else if T={0,1,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[16,17,18,19,20,21,22,23,24,25],[⟨[],1⟩,⟨[16],2⟩,⟨[17],2⟩,⟨[18],2⟩,⟨[19],2⟩,⟨[20],2⟩,⟨[21],1⟩,⟨[16,18,21],1⟩,⟨[17,19,21],1⟩,⟨[22],1⟩,⟨[17,18,22],1⟩,⟨[16,20,22],1⟩,⟨[23],1⟩,⟨[16,19,23],1⟩,⟨[17,20,23],1⟩,⟨[21,22,23],1⟩,⟨[24],3⟩,⟨[20,21,24],1⟩,⟨[19,22,24],1⟩,⟨[18,23,24],1⟩,⟨[25],2⟩,⟨[18,19,20,25],1⟩,⟨[21,25],1⟩,⟨[22,25],1⟩,⟨[23,25],1⟩,⟨[16,17,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2

namespace Case3
def positionFn : Fin 10 → Fin 25 := ![15,16,17,18,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{3},{4},{5},{6},{0,1,6},{2,3,6},{4,5,6},{7},{0,2,7},{1,4,7},{3,5,7},{8},{1,3,8},{2,4,8},{0,5,8},{6,7,8},{9},{0,3,4,9},{1,2,5,9},{6,9},{7,9},{8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={4} then 2 else if T={5} then 2 else if T={6} then 1 else if T={0,1,6} then 1 else if T={2,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 1 else if T={0,2,7} then 1 else if T={1,4,7} then 1 else if T={3,5,7} then 1 else if T={8} then 2 else if T={1,3,8} then 1 else if T={2,4,8} then 1 else if T={0,5,8} then 1 else if T={6,7,8} then 1 else if T={9} then 2 else if T={0,3,4,9} then 1 else if T={1,2,5,9} then 1 else if T={6,9} then 1 else if T={7,9} then 1 else if T={8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[16,17,18,19,20,21,22,23,24,25],[⟨[],1⟩,⟨[16],2⟩,⟨[17],2⟩,⟨[18],2⟩,⟨[19],2⟩,⟨[20],2⟩,⟨[21],2⟩,⟨[22],1⟩,⟨[16,17,22],1⟩,⟨[18,19,22],1⟩,⟨[20,21,22],1⟩,⟨[23],1⟩,⟨[16,18,23],1⟩,⟨[17,20,23],1⟩,⟨[19,21,23],1⟩,⟨[24],2⟩,⟨[17,19,24],1⟩,⟨[18,20,24],1⟩,⟨[16,21,24],1⟩,⟨[22,23,24],1⟩,⟨[25],2⟩,⟨[16,19,20,25],1⟩,⟨[17,18,21,25],1⟩,⟨[22,25],1⟩,⟨[23,25],1⟩,⟨[24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3

namespace Case4
def positionFn : Fin 10 → Fin 25 := ![20,11,21,22,9,12,10,13,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{1},{2},{1,3},{2,3},{0,4},{0,5},{1,4,5},{0,6},{2,4,6},{3,5,6},{7},{0,7},{3,4,7},{2,5,7},{1,6,7},{1,8},{2,8},{0,3,8},{4,8},{5,8},{6,8},{9},{0,1,2,9},{3,9},{4,9},{5,9},{6,9},{7,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={1} then 1 else if T={2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={0,5} then 1 else if T={1,4,5} then 1 else if T={0,6} then 1 else if T={2,4,6} then 1 else if T={3,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={2,5,7} then 1 else if T={1,6,7} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={0,3,8} then 1 else if T={4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={9} then 1 else if T={0,1,2,9} then 1 else if T={3,9} then 1 else if T={4,9} then 1 else if T={5,9} then 1 else if T={6,9} then 1 else if T={7,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,21,22,23,24,25],[⟨[],6⟩,⟨[12],1⟩,⟨[22],1⟩,⟨[12,23],1⟩,⟨[22,23],1⟩,⟨[10,21],1⟩,⟨[13,21],1⟩,⟨[10,12,13],1⟩,⟨[11,21],1⟩,⟨[10,11,22],1⟩,⟨[11,13,23],1⟩,⟨[14],1⟩,⟨[14,21],1⟩,⟨[10,14,23],1⟩,⟨[13,14,22],1⟩,⟨[11,12,14],1⟩,⟨[12,24],1⟩,⟨[22,24],1⟩,⟨[21,23,24],1⟩,⟨[10,24],1⟩,⟨[13,24],1⟩,⟨[11,24],1⟩,⟨[25],1⟩,⟨[12,21,22,25],1⟩,⟨[23,25],1⟩,⟨[10,25],1⟩,⟨[13,25],1⟩,⟨[11,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4

namespace Case5
def positionFn : Fin 10 → Fin 25 := ![9,10,12,13,21,22,11,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{1},{2},{1,2},{3},{1,3},{4},{0,4},{5},{0,5},{0,6},{2,4,6},{3,5,6},{7},{0,7},{3,4,7},{2,5,7},{1,6,7},{0,1,8},{2,8},{3,8},{4,8},{5,8},{6,8},{9},{0,2,3,9},{1,4,5,9},{6,9},{7,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={0,6} then 1 else if T={2,4,6} then 1 else if T={3,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={2,5,7} then 1 else if T={1,6,7} then 1 else if T={0,1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={9} then 3 else if T={0,2,3,9} then 1 else if T={1,4,5,9} then 1 else if T={6,9} then 1 else if T={7,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,22,23,24,25],[⟨[],4⟩,⟨[11],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[22],1⟩,⟨[10,22],1⟩,⟨[23],1⟩,⟨[10,23],1⟩,⟨[10,12],1⟩,⟨[12,13,22],1⟩,⟨[12,14,23],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[14,15,22],1⟩,⟨[13,15,23],1⟩,⟨[11,12,15],1⟩,⟨[10,11,24],1⟩,⟨[13,24],1⟩,⟨[14,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[12,24],1⟩,⟨[25],3⟩,⟨[10,13,14,25],1⟩,⟨[11,22,23,25],1⟩,⟨[12,25],1⟩,⟨[15,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case5

namespace Case6
def positionFn : Fin 10 → Fin 25 := ![8,9,10,11,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0,1,4},{2,4},{3,4},{0,5},{1,5},{2,3,5},{6},{0,2,6},{1,3,6},{7},{1,2,7},{0,3,7},{5,7},{4,6,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,8},{0,9},{1,9},{2,9},{3,9},{4,9},{5,6,9},{7,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,3,5} then 1 else if T={6} then 1 else if T={0,2,6} then 1 else if T={1,3,6} then 1 else if T={7} then 1 else if T={1,2,7} then 1 else if T={0,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,5,8} then 1 else if T={6,8} then 1 else if T={0,9} then 1 else if T={1,9} then 1 else if T={2,9} then 1 else if T={3,9} then 1 else if T={4,9} then 1 else if T={5,6,9} then 1 else if T={7,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,20,21,22,23,24,25],[⟨[],7⟩,⟨[9,10,20],1⟩,⟨[11,20],1⟩,⟨[12,20],1⟩,⟨[9,21],1⟩,⟨[10,21],1⟩,⟨[11,12,21],1⟩,⟨[22],1⟩,⟨[9,11,22],1⟩,⟨[10,12,22],1⟩,⟨[23],1⟩,⟨[10,11,23],1⟩,⟨[9,12,23],1⟩,⟨[21,23],1⟩,⟨[20,22,23],1⟩,⟨[9,24],1⟩,⟨[10,24],1⟩,⟨[11,24],1⟩,⟨[12,24],1⟩,⟨[20,21,24],1⟩,⟨[22,24],1⟩,⟨[9,25],1⟩,⟨[10,25],1⟩,⟨[11,25],1⟩,⟨[12,25],1⟩,⟨[20,25],1⟩,⟨[21,22,25],1⟩,⟨[23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6

namespace Case7
def positionFn : Fin 10 → Fin 25 := ![20,21,22,9,10,12,11,13,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0,1,2},{1,4},{2,4},{0,3,4},{0,5},{3,5},{6},{1,3,6},{2,5,6},{7},{2,3,7},{4,7},{1,5,7},{0,6,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,8},{0,9},{1,9},{2,9},{3,9},{5,9},{4,6,9},{7,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,1,2} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={1,3,6} then 1 else if T={2,5,6} then 1 else if T={7} then 1 else if T={2,3,7} then 1 else if T={4,7} then 1 else if T={1,5,7} then 1 else if T={0,6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,5,8} then 1 else if T={6,8} then 1 else if T={0,9} then 1 else if T={1,9} then 1 else if T={2,9} then 1 else if T={3,9} then 1 else if T={5,9} then 1 else if T={4,6,9} then 1 else if T={7,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,21,22,23,24,25],[⟨[],7⟩,⟨[21,22,23],1⟩,⟨[11,22],1⟩,⟨[11,23],1⟩,⟨[10,11,21],1⟩,⟨[13,21],1⟩,⟨[10,13],1⟩,⟨[12],1⟩,⟨[10,12,22],1⟩,⟨[12,13,23],1⟩,⟨[14],1⟩,⟨[10,14,23],1⟩,⟨[11,14],1⟩,⟨[13,14,22],1⟩,⟨[12,14,21],1⟩,⟨[21,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[10,24],1⟩,⟨[11,13,24],1⟩,⟨[12,24],1⟩,⟨[21,25],1⟩,⟨[22,25],1⟩,⟨[23,25],1⟩,⟨[10,25],1⟩,⟨[13,25],1⟩,⟨[11,12,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7

namespace Case8
def positionFn : Fin 10 → Fin 25 := ![21,22,9,12,13,10,11,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{2,3},{2,4},{0,5},{1,5},{3,4,5},{6},{0,3,6},{1,4,6},{7},{1,3,7},{0,4,7},{5,7},{2,6,7},{0,8},{1,8},{3,8},{4,8},{2,5,8},{6,8},{9},{0,1,2,9},{3,9},{4,9},{5,6,9},{7,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={2,3} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,4,5} then 1 else if T={6} then 1 else if T={0,3,6} then 1 else if T={1,4,6} then 1 else if T={7} then 1 else if T={1,3,7} then 1 else if T={0,4,7} then 1 else if T={5,7} then 1 else if T={2,6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,8} then 1 else if T={4,8} then 1 else if T={2,5,8} then 1 else if T={6,8} then 1 else if T={9} then 2 else if T={0,1,2,9} then 1 else if T={3,9} then 1 else if T={4,9} then 1 else if T={5,6,9} then 1 else if T={7,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,22,23,24,25],[⟨[],5⟩,⟨[22],1⟩,⟨[23],1⟩,⟨[10],1⟩,⟨[10,13],1⟩,⟨[10,14],1⟩,⟨[11,22],1⟩,⟨[11,23],1⟩,⟨[11,13,14],1⟩,⟨[12],1⟩,⟨[12,13,22],1⟩,⟨[12,14,23],1⟩,⟨[15],1⟩,⟨[13,15,23],1⟩,⟨[14,15,22],1⟩,⟨[11,15],1⟩,⟨[10,12,15],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[13,24],1⟩,⟨[14,24],1⟩,⟨[10,11,24],1⟩,⟨[12,24],1⟩,⟨[25],2⟩,⟨[10,22,23,25],1⟩,⟨[13,25],1⟩,⟨[14,25],1⟩,⟨[11,12,25],1⟩,⟨[15,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8

namespace Case9
def positionFn : Fin 10 → Fin 25 := ![9,10,11,19,12,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{1,3},{2,3},{4},{0,3,4},{5},{0,1,5},{2,4,5},{6},{0,2,6},{3,6},{1,4,6},{7},{0,7},{1,2,7},{5,6,7},{0,8},{1,8},{2,8},{4,8},{5,8},{3,7,8},{9},{0,9},{1,9},{2,9},{3,5,9},{4,7,9},{6,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,1,5} then 1 else if T={2,4,5} then 1 else if T={6} then 1 else if T={0,2,6} then 1 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={5,6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={4,8} then 1 else if T={5,8} then 1 else if T={3,7,8} then 1 else if T={9} then 1 else if T={0,9} then 1 else if T={1,9} then 1 else if T={2,9} then 1 else if T={3,5,9} then 1 else if T={4,7,9} then 1 else if T={6,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,20,21,22,23,24,25],[⟨[],6⟩,⟨[11,20],1⟩,⟨[12,20],1⟩,⟨[13],1⟩,⟨[10,13,20],1⟩,⟨[21],1⟩,⟨[10,11,21],1⟩,⟨[12,13,21],1⟩,⟨[22],1⟩,⟨[10,12,22],1⟩,⟨[20,22],1⟩,⟨[11,13,22],1⟩,⟨[23],1⟩,⟨[10,23],1⟩,⟨[11,12,23],1⟩,⟨[21,22,23],1⟩,⟨[10,24],1⟩,⟨[11,24],1⟩,⟨[12,24],1⟩,⟨[13,24],1⟩,⟨[21,24],1⟩,⟨[20,23,24],1⟩,⟨[25],1⟩,⟨[10,25],1⟩,⟨[11,25],1⟩,⟨[12,25],1⟩,⟨[20,21,25],1⟩,⟨[13,23,25],1⟩,⟨[22,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9

namespace Case10
def positionFn : Fin 10 → Fin 25 := ![9,20,21,10,22,11,12,13,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{1,3},{2,3},{4},{1,2,4},{0,3,4},{5},{0,1,5},{6},{0,2,6},{3,6},{4,5,6},{7},{0,7},{2,5,7},{1,6,7},{0,8},{1,8},{2,8},{4,8},{5,8},{3,7,8},{9},{0,9},{1,9},{2,9},{3,5,9},{4,7,9},{6,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,2,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,1,5} then 1 else if T={6} then 1 else if T={0,2,6} then 1 else if T={3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,5,7} then 1 else if T={1,6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={4,8} then 1 else if T={5,8} then 1 else if T={3,7,8} then 1 else if T={9} then 1 else if T={0,9} then 1 else if T={1,9} then 1 else if T={2,9} then 1 else if T={3,5,9} then 1 else if T={4,7,9} then 1 else if T={6,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,21,22,23,24,25],[⟨[],6⟩,⟨[11,21],1⟩,⟨[11,22],1⟩,⟨[23],1⟩,⟨[21,22,23],1⟩,⟨[10,11,23],1⟩,⟨[12],1⟩,⟨[10,12,21],1⟩,⟨[13],1⟩,⟨[10,13,22],1⟩,⟨[11,13],1⟩,⟨[12,13,23],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14,22],1⟩,⟨[13,14,21],1⟩,⟨[10,24],1⟩,⟨[21,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[12,24],1⟩,⟨[11,14,24],1⟩,⟨[25],1⟩,⟨[10,25],1⟩,⟨[21,25],1⟩,⟨[22,25],1⟩,⟨[11,12,25],1⟩,⟨[14,23,25],1⟩,⟨[13,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10

namespace Case11
def positionFn : Fin 10 → Fin 25 := ![9,10,20,12,21,11,22,13,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0,1,2},{1,3},{2,3},{4},{0,3,4},{5},{1,4,5},{6},{3,6},{2,4,6},{0,5,6},{7},{0,7},{2,5,7},{1,6,7},{0,8},{1,8},{2,8},{4,8},{5,8},{3,7,8},{9},{0,9},{1,9},{2,9},{3,5,9},{4,7,9},{6,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={1,4,5} then 1 else if T={6} then 1 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={0,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,5,7} then 1 else if T={1,6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={4,8} then 1 else if T={5,8} then 1 else if T={3,7,8} then 1 else if T={9} then 1 else if T={0,9} then 1 else if T={1,9} then 1 else if T={2,9} then 1 else if T={3,5,9} then 1 else if T={4,7,9} then 1 else if T={6,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,21,22,23,24,25],[⟨[],6⟩,⟨[10,11,21],1⟩,⟨[11,13],1⟩,⟨[13,21],1⟩,⟨[22],1⟩,⟨[10,13,22],1⟩,⟨[12],1⟩,⟨[11,12,22],1⟩,⟨[23],1⟩,⟨[13,23],1⟩,⟨[21,22,23],1⟩,⟨[10,12,23],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14,21],1⟩,⟨[11,14,23],1⟩,⟨[10,24],1⟩,⟨[11,24],1⟩,⟨[21,24],1⟩,⟨[22,24],1⟩,⟨[12,24],1⟩,⟨[13,14,24],1⟩,⟨[25],1⟩,⟨[10,25],1⟩,⟨[11,25],1⟩,⟨[21,25],1⟩,⟨[12,13,25],1⟩,⟨[14,22,25],1⟩,⟨[23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11

namespace Case12
def positionFn : Fin 10 → Fin 25 := ![9,21,22,10,12,13,11,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{1,4},{2,4},{0,3,4},{0,5},{3,5},{6},{1,3,6},{2,5,6},{7},{2,3,7},{4,7},{1,5,7},{0,6,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,8},{9},{0,1,2,9},{3,9},{5,9},{4,6,9},{7,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={1,3,6} then 1 else if T={2,5,6} then 1 else if T={7} then 1 else if T={2,3,7} then 1 else if T={4,7} then 1 else if T={1,5,7} then 1 else if T={0,6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,5,8} then 1 else if T={6,8} then 1 else if T={9} then 2 else if T={0,1,2,9} then 1 else if T={3,9} then 1 else if T={5,9} then 1 else if T={4,6,9} then 1 else if T={7,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,22,23,24,25],[⟨[],5⟩,⟨[10],1⟩,⟨[22],1⟩,⟨[23],1⟩,⟨[13,22],1⟩,⟨[13,23],1⟩,⟨[10,11,13],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[12],1⟩,⟨[11,12,22],1⟩,⟨[12,14,23],1⟩,⟨[15],1⟩,⟨[11,15,23],1⟩,⟨[13,15],1⟩,⟨[14,15,22],1⟩,⟨[10,12,15],1⟩,⟨[10,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[11,24],1⟩,⟨[13,14,24],1⟩,⟨[12,24],1⟩,⟨[25],2⟩,⟨[10,22,23,25],1⟩,⟨[11,25],1⟩,⟨[14,25],1⟩,⟨[12,13,25],1⟩,⟨[15,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case12

namespace Case13
def positionFn : Fin 10 → Fin 25 := ![20,21,22,9,10,12,11,13,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0,1,2},{1,4},{0,3,4},{0,5},{2,5},{3,5},{6},{1,3,6},{2,4,6},{7},{2,3,7},{4,7},{1,5,7},{0,6,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,8},{0,9},{1,9},{2,9},{3,9},{4,9},{5,6,9},{7,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,1,2} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={1,3,6} then 1 else if T={2,4,6} then 1 else if T={7} then 1 else if T={2,3,7} then 1 else if T={4,7} then 1 else if T={1,5,7} then 1 else if T={0,6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,5,8} then 1 else if T={6,8} then 1 else if T={0,9} then 1 else if T={1,9} then 1 else if T={2,9} then 1 else if T={3,9} then 1 else if T={4,9} then 1 else if T={5,6,9} then 1 else if T={7,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,21,22,23,24,25],[⟨[],7⟩,⟨[21,22,23],1⟩,⟨[11,22],1⟩,⟨[10,11,21],1⟩,⟨[13,21],1⟩,⟨[13,23],1⟩,⟨[10,13],1⟩,⟨[12],1⟩,⟨[10,12,22],1⟩,⟨[11,12,23],1⟩,⟨[14],1⟩,⟨[10,14,23],1⟩,⟨[11,14],1⟩,⟨[13,14,22],1⟩,⟨[12,14,21],1⟩,⟨[21,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[10,24],1⟩,⟨[11,13,24],1⟩,⟨[12,24],1⟩,⟨[21,25],1⟩,⟨[22,25],1⟩,⟨[23,25],1⟩,⟨[10,25],1⟩,⟨[11,25],1⟩,⟨[12,13,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case13

namespace Case14
def positionFn : Fin 10 → Fin 25 := ![20,11,21,9,10,12,13,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{2,4},{0,3,4},{0,5},{1,5},{3,5},{6},{2,3,6},{1,4,6},{7},{2,7},{1,3,7},{4,5,7},{0,6,7},{0,8},{1,8},{3,8},{4,8},{2,5,8},{6,8},{9},{0,1,2,9},{3,9},{4,9},{5,6,9},{7,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={2,3,6} then 1 else if T={1,4,6} then 1 else if T={7} then 1 else if T={2,7} then 1 else if T={1,3,7} then 1 else if T={4,5,7} then 1 else if T={0,6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,8} then 1 else if T={4,8} then 1 else if T={2,5,8} then 1 else if T={6,8} then 1 else if T={9} then 2 else if T={0,1,2,9} then 1 else if T={3,9} then 1 else if T={4,9} then 1 else if T={5,6,9} then 1 else if T={7,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,21,22,23,24,25],[⟨[],5⟩,⟨[21],1⟩,⟨[12],1⟩,⟨[22],1⟩,⟨[11,22],1⟩,⟨[10,11,21],1⟩,⟨[13,21],1⟩,⟨[12,13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14,22],1⟩,⟨[11,12,14],1⟩,⟨[23],1⟩,⟨[22,23],1⟩,⟨[10,12,23],1⟩,⟨[11,13,23],1⟩,⟨[14,21,23],1⟩,⟨[21,24],1⟩,⟨[12,24],1⟩,⟨[10,24],1⟩,⟨[11,24],1⟩,⟨[13,22,24],1⟩,⟨[14,24],1⟩,⟨[25],2⟩,⟨[12,21,22,25],1⟩,⟨[10,25],1⟩,⟨[11,25],1⟩,⟨[13,14,25],1⟩,⟨[23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case14

namespace Case15
def positionFn : Fin 10 → Fin 25 := ![9,21,22,10,13,11,14,12,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{1,3},{2,3},{4},{0,3,4},{5},{1,4,5},{6},{3,6},{2,4,6},{0,5,6},{7},{0,7},{2,5,7},{1,6,7},{0,8},{1,8},{2,8},{4,8},{5,8},{3,7,8},{9},{0,1,2,9},{3,5,9},{4,7,9},{6,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={1,4,5} then 1 else if T={6} then 1 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={0,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,5,7} then 1 else if T={1,6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={4,8} then 1 else if T={5,8} then 1 else if T={3,7,8} then 1 else if T={9} then 3 else if T={0,1,2,9} then 1 else if T={3,5,9} then 1 else if T={4,7,9} then 1 else if T={6,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,22,23,24,25],[⟨[],4⟩,⟨[10],1⟩,⟨[22],1⟩,⟨[23],1⟩,⟨[11,22],1⟩,⟨[11,23],1⟩,⟨[14],1⟩,⟨[10,11,14],1⟩,⟨[12],1⟩,⟨[12,14,22],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[14,15,23],1⟩,⟨[10,12,15],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[12,13,23],1⟩,⟨[13,15,22],1⟩,⟨[10,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[14,24],1⟩,⟨[12,24],1⟩,⟨[11,13,24],1⟩,⟨[25],3⟩,⟨[10,22,23,25],1⟩,⟨[11,12,25],1⟩,⟨[13,14,25],1⟩,⟨[15,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case15

namespace Case16
def positionFn : Fin 10 → Fin 25 := ![9,10,11,19,20,21,22,12,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0,3},{1,3},{2,3},{4},{0,1,4},{5},{0,2,5},{3,4,5},{6},{1,2,6},{5,6},{7},{2,4,7},{1,5,7},{0,6,7},{0,8},{1,8},{2,8},{4,8},{3,6,8},{7,8},{9},{0,9},{1,9},{2,9},{4,6,9},{3,7,9},{5,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 1 else if T={1,2,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={2,4,7} then 1 else if T={1,5,7} then 1 else if T={0,6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={4,8} then 1 else if T={3,6,8} then 1 else if T={7,8} then 1 else if T={9} then 1 else if T={0,9} then 1 else if T={1,9} then 1 else if T={2,9} then 1 else if T={4,6,9} then 1 else if T={3,7,9} then 1 else if T={5,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,20,21,22,23,24,25],[⟨[],6⟩,⟨[10,20],1⟩,⟨[11,20],1⟩,⟨[12,20],1⟩,⟨[21],1⟩,⟨[10,11,21],1⟩,⟨[22],1⟩,⟨[10,12,22],1⟩,⟨[20,21,22],1⟩,⟨[23],1⟩,⟨[11,12,23],1⟩,⟨[22,23],1⟩,⟨[13],1⟩,⟨[12,13,21],1⟩,⟨[11,13,22],1⟩,⟨[10,13,23],1⟩,⟨[10,24],1⟩,⟨[11,24],1⟩,⟨[12,24],1⟩,⟨[21,24],1⟩,⟨[20,23,24],1⟩,⟨[13,24],1⟩,⟨[25],1⟩,⟨[10,25],1⟩,⟨[11,25],1⟩,⟨[12,25],1⟩,⟨[21,23,25],1⟩,⟨[13,20,25],1⟩,⟨[22,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case16

namespace Case17
def positionFn : Fin 10 → Fin 25 := ![21,22,11,9,10,12,13,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{1,4},{0,3,4},{0,5},{2,5},{3,5},{6},{1,3,6},{2,4,6},{7},{2,3,7},{4,7},{1,5,7},{0,6,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,8},{9},{0,1,2,9},{3,9},{4,9},{5,6,9},{7,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={1,3,6} then 1 else if T={2,4,6} then 1 else if T={7} then 1 else if T={2,3,7} then 1 else if T={4,7} then 1 else if T={1,5,7} then 1 else if T={0,6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,5,8} then 1 else if T={6,8} then 1 else if T={9} then 2 else if T={0,1,2,9} then 1 else if T={3,9} then 1 else if T={4,9} then 1 else if T={5,6,9} then 1 else if T={7,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,22,23,24,25],[⟨[],5⟩,⟨[22],1⟩,⟨[23],1⟩,⟨[12],1⟩,⟨[11,23],1⟩,⟨[10,11,22],1⟩,⟨[13,22],1⟩,⟨[12,13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14,23],1⟩,⟨[11,12,14],1⟩,⟨[15],1⟩,⟨[10,12,15],1⟩,⟨[11,15],1⟩,⟨[13,15,23],1⟩,⟨[14,15,22],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[12,24],1⟩,⟨[10,24],1⟩,⟨[11,13,24],1⟩,⟨[14,24],1⟩,⟨[25],2⟩,⟨[12,22,23,25],1⟩,⟨[10,25],1⟩,⟨[11,25],1⟩,⟨[13,14,25],1⟩,⟨[15,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case17

namespace Case18
def positionFn : Fin 10 → Fin 25 := ![9,20,10,13,11,12,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{1},{1,2},{1,3},{0,2,3},{0,4},{0,5},{1,4,5},{0,6},{2,4,6},{3,5,6},{0,7},{3,4,7},{2,5,7},{1,6,7},{2,8},{3,8},{4,8},{5,8},{6,8},{7,8},{2,9},{3,9},{4,9},{5,9},{6,9},{7,9},{0,1,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={1} then 1 else if T={1,2} then 1 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={0,4} then 1 else if T={0,5} then 1 else if T={1,4,5} then 1 else if T={0,6} then 1 else if T={2,4,6} then 1 else if T={3,5,6} then 1 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={2,5,7} then 1 else if T={1,6,7} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else if T={2,9} then 1 else if T={3,9} then 1 else if T={4,9} then 1 else if T={5,9} then 1 else if T={6,9} then 1 else if T={7,9} then 1 else if T={0,1,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,21,22,23,24,25],[⟨[],7⟩,⟨[21],1⟩,⟨[11,21],1⟩,⟨[14,21],1⟩,⟨[10,11,14],1⟩,⟨[10,12],1⟩,⟨[10,13],1⟩,⟨[12,13,21],1⟩,⟨[10,22],1⟩,⟨[11,12,22],1⟩,⟨[13,14,22],1⟩,⟨[10,23],1⟩,⟨[12,14,23],1⟩,⟨[11,13,23],1⟩,⟨[21,22,23],1⟩,⟨[11,24],1⟩,⟨[14,24],1⟩,⟨[12,24],1⟩,⟨[13,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[11,25],1⟩,⟨[14,25],1⟩,⟨[12,25],1⟩,⟨[13,25],1⟩,⟨[22,25],1⟩,⟨[23,25],1⟩,⟨[10,21,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case18

namespace Case19
def positionFn : Fin 10 → Fin 25 := ![9,10,21,12,13,22,11,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{1},{2},{1,2},{3},{0,3},{4},{0,4},{0,1,5},{2,5},{0,6},{2,3,6},{4,5,6},{0,7},{2,4,7},{3,5,7},{1,6,7},{1,8},{3,8},{4,8},{5,8},{6,8},{7,8},{9},{1,3,4,9},{5,9},{6,9},{7,9},{0,2,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={0,1,5} then 1 else if T={2,5} then 1 else if T={0,6} then 1 else if T={2,3,6} then 1 else if T={4,5,6} then 1 else if T={0,7} then 1 else if T={2,4,7} then 1 else if T={3,5,7} then 1 else if T={1,6,7} then 1 else if T={1,8} then 1 else if T={3,8} then 1 else if T={4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else if T={9} then 2 else if T={1,3,4,9} then 1 else if T={5,9} then 1 else if T={6,9} then 1 else if T={7,9} then 1 else if T={0,2,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,22,23,24,25],[⟨[],5⟩,⟨[11],1⟩,⟨[22],1⟩,⟨[11,22],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[10,11,23],1⟩,⟨[22,23],1⟩,⟨[10,12],1⟩,⟨[12,13,22],1⟩,⟨[12,14,23],1⟩,⟨[10,15],1⟩,⟨[14,15,22],1⟩,⟨[13,15,23],1⟩,⟨[11,12,15],1⟩,⟨[11,24],1⟩,⟨[13,24],1⟩,⟨[14,24],1⟩,⟨[23,24],1⟩,⟨[12,24],1⟩,⟨[15,24],1⟩,⟨[25],2⟩,⟨[11,13,14,25],1⟩,⟨[23,25],1⟩,⟨[12,25],1⟩,⟨[15,25],1⟩,⟨[10,22,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case19
def μ : Fin 20 → Finset (Fin 10) → ℕ := ![Case0.μ,Case1.μ,Case2.μ,Case3.μ,Case4.μ,Case5.μ,Case6.μ,Case7.μ,Case8.μ,Case9.μ,Case10.μ,Case11.μ,Case12.μ,Case13.μ,Case14.μ,Case15.μ,Case16.μ,Case17.μ,Case18.μ,Case19.μ]
end Aris4Math.ThirtyFour.TwentyFiveEightLowTenth

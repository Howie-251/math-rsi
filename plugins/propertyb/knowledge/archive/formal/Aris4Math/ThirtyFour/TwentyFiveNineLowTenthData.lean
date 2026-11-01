import Aris4Math.ThirtyFour.CachedSparseApplication
namespace Aris4Math.ThirtyFour.TwentyFiveNineLowTenth
open Aris4Math.ThirtyThree.MultiLockRecovery
open LocalProfiles CachedRows
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case0
def positionFn : Fin 10 → Fin 25 := ![7,10,22,8,9,23,11,12,13,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{3},{4},{5},{6},{0,1,6},{2,3,6},{4,5,6},{7},{0,2,7},{1,4,7},{3,5,7},{8},{1,3,8},{2,4,8},{0,5,8},{6,7,8},{9},{0,3,4,9},{1,2,5,9},{6,9},{7,9},{8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={4} then 2 else if T={5} then 2 else if T={6} then 1 else if T={0,1,6} then 1 else if T={2,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 1 else if T={0,2,7} then 1 else if T={1,4,7} then 1 else if T={3,5,7} then 1 else if T={8} then 1 else if T={1,3,8} then 1 else if T={2,4,8} then 1 else if T={0,5,8} then 1 else if T={6,7,8} then 1 else if T={9} then 1 else if T={0,3,4,9} then 1 else if T={1,2,5,9} then 1 else if T={6,9} then 1 else if T={7,9} then 1 else if T={8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[8,9,10,11,12,13,14,23,24,25],[⟨[],3⟩,⟨[8],2⟩,⟨[11],2⟩,⟨[23],2⟩,⟨[9],2⟩,⟨[10],2⟩,⟨[24],2⟩,⟨[12],1⟩,⟨[8,11,12],1⟩,⟨[9,12,23],1⟩,⟨[10,12,24],1⟩,⟨[13],1⟩,⟨[8,13,23],1⟩,⟨[10,11,13],1⟩,⟨[9,13,24],1⟩,⟨[14],1⟩,⟨[9,11,14],1⟩,⟨[10,14,23],1⟩,⟨[8,14,24],1⟩,⟨[12,13,14],1⟩,⟨[25],1⟩,⟨[8,9,10,25],1⟩,⟨[11,23,24,25],1⟩,⟨[12,25],1⟩,⟨[13,25],1⟩,⟨[14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case0

namespace Case1
def positionFn : Fin 10 → Fin 25 := ![15,16,17,18,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{0,1,2},{3},{4},{0,3,4},{5},{1,3,5},{6},{2,4,6},{7},{2,5,7},{3,6,7},{8},{4,5,8},{1,6,8},{0,7,8},{9},{0,5,6,9},{1,4,7,9},{2,3,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={0,1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={0,3,4} then 1 else if T={5} then 2 else if T={1,3,5} then 1 else if T={6} then 2 else if T={2,4,6} then 1 else if T={7} then 2 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else if T={9} then 3 else if T={0,5,6,9} then 1 else if T={1,4,7,9} then 1 else if T={2,3,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[16,17,18,19,20,21,22,23,24,25],[⟨[],1⟩,⟨[16],2⟩,⟨[17],2⟩,⟨[18],2⟩,⟨[16,17,18],1⟩,⟨[19],2⟩,⟨[20],2⟩,⟨[16,19,20],1⟩,⟨[21],2⟩,⟨[17,19,21],1⟩,⟨[22],2⟩,⟨[18,20,22],1⟩,⟨[23],2⟩,⟨[18,21,23],1⟩,⟨[19,22,23],1⟩,⟨[24],2⟩,⟨[20,21,24],1⟩,⟨[17,22,24],1⟩,⟨[16,23,24],1⟩,⟨[25],3⟩,⟨[16,21,22,25],1⟩,⟨[17,20,23,25],1⟩,⟨[18,19,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1

namespace Case2
def positionFn : Fin 10 → Fin 25 := ![12,13,11,8,9,10,14,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{3},{4},{0,3,4},{5},{1,3,5},{6},{2,3,6},{4,5,6},{7},{1,4,7},{2,5,7},{0,6,7},{8},{2,4,8},{0,5,8},{1,6,8},{3,7,8},{0,1,2,9},{3,9},{4,9},{5,9},{6,9},{7,9},{8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={1,3,5} then 1 else if T={6} then 1 else if T={2,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 1 else if T={1,4,7} then 1 else if T={2,5,7} then 1 else if T={0,6,7} then 1 else if T={8} then 1 else if T={2,4,8} then 1 else if T={0,5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else if T={0,1,2,9} then 1 else if T={3,9} then 1 else if T={4,9} then 1 else if T={5,9} then 1 else if T={6,9} then 1 else if T={7,9} then 1 else if T={8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,23,24,25],[⟨[],4⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[12],2⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[9,10,13],1⟩,⟨[11],1⟩,⟨[9,11,14],1⟩,⟨[15],1⟩,⟨[9,12,15],1⟩,⟨[10,11,15],1⟩,⟨[23],1⟩,⟨[10,14,23],1⟩,⟨[11,12,23],1⟩,⟨[13,15,23],1⟩,⟨[24],1⟩,⟨[10,12,24],1⟩,⟨[11,13,24],1⟩,⟨[14,15,24],1⟩,⟨[9,23,24],1⟩,⟨[12,13,14,25],1⟩,⟨[9,25],1⟩,⟨[10,25],1⟩,⟨[11,25],1⟩,⟨[15,25],1⟩,⟨[23,25],1⟩,⟨[24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2

namespace Case3
def positionFn : Fin 10 → Fin 25 := ![12,8,22,11,13,23,9,10,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{3},{4},{5},{6},{0,1,6},{2,3,6},{4,5,6},{7},{0,2,7},{1,4,7},{3,5,7},{8},{1,3,8},{2,4,8},{0,5,8},{6,7,8},{9},{0,3,4,9},{1,2,5,9},{6,9},{7,9},{8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={4} then 2 else if T={5} then 2 else if T={6} then 1 else if T={0,1,6} then 1 else if T={2,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 1 else if T={0,2,7} then 1 else if T={1,4,7} then 1 else if T={3,5,7} then 1 else if T={8} then 1 else if T={1,3,8} then 1 else if T={2,4,8} then 1 else if T={0,5,8} then 1 else if T={6,7,8} then 1 else if T={9} then 2 else if T={0,3,4,9} then 1 else if T={1,2,5,9} then 1 else if T={6,9} then 1 else if T={7,9} then 1 else if T={8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,23,24,25],[⟨[],2⟩,⟨[13],2⟩,⟨[9],2⟩,⟨[23],2⟩,⟨[12],2⟩,⟨[14],2⟩,⟨[24],2⟩,⟨[10],1⟩,⟨[9,10,13],1⟩,⟨[10,12,23],1⟩,⟨[10,14,24],1⟩,⟨[11],1⟩,⟨[11,13,23],1⟩,⟨[9,11,14],1⟩,⟨[11,12,24],1⟩,⟨[15],1⟩,⟨[9,12,15],1⟩,⟨[14,15,23],1⟩,⟨[13,15,24],1⟩,⟨[10,11,15],1⟩,⟨[25],2⟩,⟨[12,13,14,25],1⟩,⟨[9,23,24,25],1⟩,⟨[10,25],1⟩,⟨[11,25],1⟩,⟨[15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3

namespace Case4
def positionFn : Fin 10 → Fin 25 := ![15,16,17,18,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [{0},{1},{2},{0,1,2},{3},{4},{0,3,4},{5},{1,3,5},{6},{2,4,6},{7},{2,5,7},{3,6,7},{8},{4,5,8},{1,6,8},{0,7,8},{9},{0,5,6,9},{1,4,7,9},{2,3,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={0,1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={0,3,4} then 1 else if T={5} then 2 else if T={1,3,5} then 1 else if T={6} then 2 else if T={2,4,6} then 1 else if T={7} then 2 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else if T={9} then 4 else if T={0,5,6,9} then 1 else if T={1,4,7,9} then 1 else if T={2,3,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[16,17,18,19,20,21,22,23,24,25],[⟨[16],2⟩,⟨[17],2⟩,⟨[18],2⟩,⟨[16,17,18],1⟩,⟨[19],2⟩,⟨[20],2⟩,⟨[16,19,20],1⟩,⟨[21],2⟩,⟨[17,19,21],1⟩,⟨[22],2⟩,⟨[18,20,22],1⟩,⟨[23],2⟩,⟨[18,21,23],1⟩,⟨[19,22,23],1⟩,⟨[24],2⟩,⟨[20,21,24],1⟩,⟨[17,22,24],1⟩,⟨[16,23,24],1⟩,⟨[25],4⟩,⟨[16,21,22,25],1⟩,⟨[17,20,23,25],1⟩,⟨[18,19,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4

namespace Case5
def positionFn : Fin 10 → Fin 25 := ![21,12,13,8,9,22,10,11,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{0,2},{3},{1,3},{4},{5},{4,5},{0,1,6},{2,3,6},{4,6},{5,6},{1,7},{3,7},{0,4,7},{2,5,7},{0,8},{2,8},{3,4,8},{1,5,8},{6,7,8},{9},{1,2,4,9},{0,3,5,9},{6,9},{7,9},{8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={5} then 1 else if T={4,5} then 1 else if T={0,1,6} then 1 else if T={2,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={0,4,7} then 1 else if T={2,5,7} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={1,5,8} then 1 else if T={6,7,8} then 1 else if T={9} then 1 else if T={1,2,4,9} then 1 else if T={0,3,5,9} then 1 else if T={6,9} then 1 else if T={7,9} then 1 else if T={8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,22,23,24,25],[⟨[],6⟩,⟨[22],1⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[14,22],1⟩,⟨[9],1⟩,⟨[9,13],1⟩,⟨[10],1⟩,⟨[23],1⟩,⟨[10,23],1⟩,⟨[11,13,22],1⟩,⟨[9,11,14],1⟩,⟨[10,11],1⟩,⟨[11,23],1⟩,⟨[12,13],1⟩,⟨[9,12],1⟩,⟨[10,12,22],1⟩,⟨[12,14,23],1⟩,⟨[22,24],1⟩,⟨[14,24],1⟩,⟨[9,10,24],1⟩,⟨[13,23,24],1⟩,⟨[11,12,24],1⟩,⟨[25],1⟩,⟨[10,13,14,25],1⟩,⟨[9,22,23,25],1⟩,⟨[11,25],1⟩,⟨[12,25],1⟩,⟨[24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case5

namespace Case6
def positionFn : Fin 10 → Fin 25 := ![8,14,22,9,12,11,13,10,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0,1,2},{3},{2,3},{4},{1,4},{0,3,4},{5},{0,5},{1,3,5},{6},{0,6},{2,4,6},{7},{1,7},{2,5,7},{3,6,7},{8},{2,8},{4,5,8},{1,6,8},{0,7,8},{0,9},{1,9},{2,9},{5,6,9},{4,7,9},{3,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,4,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={2,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else if T={0,9} then 1 else if T={1,9} then 1 else if T={2,9} then 1 else if T={5,6,9} then 1 else if T={4,7,9} then 1 else if T={3,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,23,24,25],[⟨[],7⟩,⟨[9,15,23],1⟩,⟨[10],1⟩,⟨[10,23],1⟩,⟨[13],1⟩,⟨[13,15],1⟩,⟨[9,10,13],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[10,12,15],1⟩,⟨[14],1⟩,⟨[9,14],1⟩,⟨[13,14,23],1⟩,⟨[11],1⟩,⟨[11,15],1⟩,⟨[11,12,23],1⟩,⟨[10,11,14],1⟩,⟨[24],1⟩,⟨[23,24],1⟩,⟨[12,13,24],1⟩,⟨[14,15,24],1⟩,⟨[9,11,24],1⟩,⟨[9,25],1⟩,⟨[15,25],1⟩,⟨[23,25],1⟩,⟨[12,14,25],1⟩,⟨[11,13,25],1⟩,⟨[10,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6

namespace Case7
def positionFn : Fin 10 → Fin 25 := ![8,14,22,9,10,11,13,12,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{3},{0,1,3},{2,3},{4},{1,4},{0,2,4},{5},{0,5},{1,2,5},{6},{0,6},{3,4,6},{7},{1,7},{3,5,7},{2,6,7},{8},{2,8},{4,5,8},{1,6,8},{0,7,8},{0,9},{1,9},{2,9},{5,6,9},{4,7,9},{3,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={3} then 1 else if T={0,1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,2,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={3,4,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 1 else if T={2,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else if T={0,9} then 1 else if T={1,9} then 1 else if T={2,9} then 1 else if T={5,6,9} then 1 else if T={4,7,9} then 1 else if T={3,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,23,24,25],[⟨[],7⟩,⟨[10],1⟩,⟨[9,10,15],1⟩,⟨[10,23],1⟩,⟨[11],1⟩,⟨[11,15],1⟩,⟨[9,11,23],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[12,15,23],1⟩,⟨[14],1⟩,⟨[9,14],1⟩,⟨[10,11,14],1⟩,⟨[13],1⟩,⟨[13,15],1⟩,⟨[10,12,13],1⟩,⟨[13,14,23],1⟩,⟨[24],1⟩,⟨[23,24],1⟩,⟨[11,12,24],1⟩,⟨[14,15,24],1⟩,⟨[9,13,24],1⟩,⟨[9,25],1⟩,⟨[15,25],1⟩,⟨[23,25],1⟩,⟨[12,14,25],1⟩,⟨[11,13,25],1⟩,⟨[10,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7

namespace Case8
def positionFn : Fin 10 → Fin 25 := ![22,7,23,11,8,9,12,10,13,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{2,3},{1,4},{0,3,4},{1,5},{4,5},{2,6},{3,6},{0,5,6},{7},{0,7},{1,3,7},{2,5,7},{4,6,7},{8},{0,8},{2,4,8},{3,5,8},{1,6,8},{0,1,2,9},{3,9},{4,9},{5,9},{6,9},{7,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={2,3} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={1,5} then 1 else if T={4,5} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={0,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={2,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={1,6,8} then 1 else if T={0,1,2,9} then 1 else if T={3,9} then 1 else if T={4,9} then 1 else if T={5,9} then 1 else if T={6,9} then 1 else if T={7,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[8,9,10,11,12,13,14,23,24,25],[⟨[],7⟩,⟨[23],1⟩,⟨[8],1⟩,⟨[24],1⟩,⟨[12,24],1⟩,⟨[8,9],1⟩,⟨[9,12,23],1⟩,⟨[8,10],1⟩,⟨[9,10],1⟩,⟨[13,24],1⟩,⟨[12,13],1⟩,⟨[10,13,23],1⟩,⟨[11],1⟩,⟨[11,23],1⟩,⟨[8,11,12],1⟩,⟨[10,11,24],1⟩,⟨[9,11,13],1⟩,⟨[14],1⟩,⟨[14,23],1⟩,⟨[9,14,24],1⟩,⟨[10,12,14],1⟩,⟨[8,13,14],1⟩,⟨[8,23,24,25],1⟩,⟨[12,25],1⟩,⟨[9,25],1⟩,⟨[10,25],1⟩,⟨[13,25],1⟩,⟨[11,14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8

namespace Case9
def positionFn : Fin 10 → Fin 25 := ![8,21,22,9,23,12,11,10,13,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{2,3},{2,4},{3,4},{5},{1,5},{0,3,5},{6},{0,6},{1,3,6},{4,5,6},{7},{1,7},{0,4,7},{2,6,7},{8},{0,8},{1,4,8},{2,5,8},{3,7,8},{9},{0,1,2,9},{3,9},{4,9},{5,7,9},{6,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={2,3} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={0,3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={0,4,7} then 1 else if T={2,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={2,5,8} then 1 else if T={3,7,8} then 1 else if T={9} then 1 else if T={0,1,2,9} then 1 else if T={3,9} then 1 else if T={4,9} then 1 else if T={5,7,9} then 1 else if T={6,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,22,23,24,25],[⟨[],6⟩,⟨[9],1⟩,⟨[22],1⟩,⟨[23],1⟩,⟨[10,23],1⟩,⟨[23,24],1⟩,⟨[10,24],1⟩,⟨[13],1⟩,⟨[13,22],1⟩,⟨[9,10,13],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[10,12,22],1⟩,⟨[12,13,24],1⟩,⟨[11],1⟩,⟨[11,22],1⟩,⟨[9,11,24],1⟩,⟨[11,12,23],1⟩,⟨[14],1⟩,⟨[9,14],1⟩,⟨[14,22,24],1⟩,⟨[13,14,23],1⟩,⟨[10,11,14],1⟩,⟨[25],1⟩,⟨[9,22,23,25],1⟩,⟨[10,25],1⟩,⟨[24,25],1⟩,⟨[11,13,25],1⟩,⟨[12,14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9

namespace Case10
def positionFn : Fin 10 → Fin 25 := ![12,7,8,22,9,10,13,11,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{0,1,2},{3},{2,3},{4},{1,4},{0,3,4},{5},{0,5},{6},{2,6},{3,6},{1,5,6},{7},{1,7},{4,7},{3,5,7},{8},{0,8},{5,8},{4,6,8},{2,7,8},{9},{2,4,5,9},{0,6,7,9},{1,3,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={1,5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={4,7} then 1 else if T={3,5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else if T={9} then 3 else if T={2,4,5,9} then 1 else if T={0,6,7,9} then 1 else if T={1,3,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[8,9,10,11,12,13,14,23,24,25],[⟨[],4⟩,⟨[13],1⟩,⟨[8],1⟩,⟨[9],1⟩,⟨[8,9,13],1⟩,⟨[23],1⟩,⟨[9,23],1⟩,⟨[10],1⟩,⟨[8,10],1⟩,⟨[10,13,23],1⟩,⟨[11],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[9,14],1⟩,⟨[14,23],1⟩,⟨[8,11,14],1⟩,⟨[12],1⟩,⟨[8,12],1⟩,⟨[10,12],1⟩,⟨[11,12,23],1⟩,⟨[24],1⟩,⟨[13,24],1⟩,⟨[11,24],1⟩,⟨[10,14,24],1⟩,⟨[9,12,24],1⟩,⟨[25],3⟩,⟨[9,10,11,25],1⟩,⟨[12,13,14,25],1⟩,⟨[8,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10

namespace Case11
def positionFn : Fin 10 → Fin 25 := ![8,22,23,9,12,11,13,10,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{3},{2,3},{4},{1,4},{0,3,4},{5},{0,5},{1,3,5},{6},{0,6},{2,4,6},{7},{1,7},{2,5,7},{3,6,7},{8},{2,8},{4,5,8},{1,6,8},{0,7,8},{9},{0,1,2,9},{5,6,9},{4,7,9},{3,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,4,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={2,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else if T={9} then 2 else if T={0,1,2,9} then 1 else if T={5,6,9} then 1 else if T={4,7,9} then 1 else if T={3,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,23,24,25],[⟨[],5⟩,⟨[9],1⟩,⟨[23],1⟩,⟨[24],1⟩,⟨[10],1⟩,⟨[10,24],1⟩,⟨[13],1⟩,⟨[13,23],1⟩,⟨[9,10,13],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[10,12,23],1⟩,⟨[14],1⟩,⟨[9,14],1⟩,⟨[13,14,24],1⟩,⟨[11],1⟩,⟨[11,23],1⟩,⟨[11,12,24],1⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[15,24],1⟩,⟨[12,13,15],1⟩,⟨[14,15,23],1⟩,⟨[9,11,15],1⟩,⟨[25],2⟩,⟨[9,23,24,25],1⟩,⟨[12,14,25],1⟩,⟨[11,13,25],1⟩,⟨[10,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11

namespace Case12
def positionFn : Fin 10 → Fin 25 := ![8,14,9,22,23,10,11,12,13,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0,1,2},{2,3},{2,4},{3,4},{5},{1,5},{0,3,5},{6},{0,6},{1,3,6},{4,5,6},{7},{1,7},{0,4,7},{2,6,7},{8},{0,8},{1,4,8},{2,5,8},{3,7,8},{0,9},{1,9},{2,9},{3,9},{4,9},{5,7,9},{6,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,1,2} then 1 else if T={2,3} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={0,3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={0,4,7} then 1 else if T={2,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={2,5,8} then 1 else if T={3,7,8} then 1 else if T={0,9} then 1 else if T={1,9} then 1 else if T={2,9} then 1 else if T={3,9} then 1 else if T={4,9} then 1 else if T={5,7,9} then 1 else if T={6,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,23,24,25],[⟨[],7⟩,⟨[9,10,15],1⟩,⟨[10,23],1⟩,⟨[10,24],1⟩,⟨[23,24],1⟩,⟨[11],1⟩,⟨[11,15],1⟩,⟨[9,11,23],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[12,15,23],1⟩,⟨[11,12,24],1⟩,⟨[13],1⟩,⟨[13,15],1⟩,⟨[9,13,24],1⟩,⟨[10,12,13],1⟩,⟨[14],1⟩,⟨[9,14],1⟩,⟨[14,15,24],1⟩,⟨[10,11,14],1⟩,⟨[13,14,23],1⟩,⟨[9,25],1⟩,⟨[15,25],1⟩,⟨[10,25],1⟩,⟨[23,25],1⟩,⟨[24,25],1⟩,⟨[11,13,25],1⟩,⟨[12,14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case12

namespace Case13
def positionFn : Fin 10 → Fin 25 := ![8,9,10,22,13,11,12,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{2,3},{1,4},{0,3,4},{0,5},{1,3,5},{0,6},{2,4,6},{5,6},{1,7},{4,7},{2,5,7},{3,6,7},{2,8},{3,8},{4,5,8},{1,6,8},{0,7,8},{0,1,2,9},{3,9},{4,9},{5,9},{6,9},{7,9},{8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={2,3} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={1,3,5} then 1 else if T={0,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={1,7} then 1 else if T={4,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else if T={0,1,2,9} then 1 else if T={3,9} then 1 else if T={4,9} then 1 else if T={5,9} then 1 else if T={6,9} then 1 else if T={7,9} then 1 else if T={8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,23,24,25],[⟨[],7⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[11,23],1⟩,⟨[10,14],1⟩,⟨[9,14,23],1⟩,⟨[9,12],1⟩,⟨[10,12,23],1⟩,⟨[9,13],1⟩,⟨[11,13,14],1⟩,⟨[12,13],1⟩,⟨[10,15],1⟩,⟨[14,15],1⟩,⟨[11,12,15],1⟩,⟨[13,15,23],1⟩,⟨[11,24],1⟩,⟨[23,24],1⟩,⟨[12,14,24],1⟩,⟨[10,13,24],1⟩,⟨[9,15,24],1⟩,⟨[9,10,11,25],1⟩,⟨[23,25],1⟩,⟨[14,25],1⟩,⟨[12,25],1⟩,⟨[13,25],1⟩,⟨[15,25],1⟩,⟨[24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case13

namespace Case14
def positionFn : Fin 10 → Fin 25 := ![21,12,13,8,9,22,10,11,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{0,2},{3},{1,3},{4},{5},{4,5},{0,1,6},{2,3,6},{4,6},{5,6},{1,7},{3,7},{0,4,7},{2,5,7},{0,8},{2,8},{3,4,8},{1,5,8},{6,7,8},{9},{1,2,4,9},{0,3,5,9},{6,9},{7,9},{8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={5} then 1 else if T={4,5} then 1 else if T={0,1,6} then 1 else if T={2,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={0,4,7} then 1 else if T={2,5,7} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={1,5,8} then 1 else if T={6,7,8} then 1 else if T={9} then 2 else if T={1,2,4,9} then 1 else if T={0,3,5,9} then 1 else if T={6,9} then 1 else if T={7,9} then 1 else if T={8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,22,23,24,25],[⟨[],5⟩,⟨[22],1⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[14,22],1⟩,⟨[9],1⟩,⟨[9,13],1⟩,⟨[10],1⟩,⟨[23],1⟩,⟨[10,23],1⟩,⟨[11,13,22],1⟩,⟨[9,11,14],1⟩,⟨[10,11],1⟩,⟨[11,23],1⟩,⟨[12,13],1⟩,⟨[9,12],1⟩,⟨[10,12,22],1⟩,⟨[12,14,23],1⟩,⟨[22,24],1⟩,⟨[14,24],1⟩,⟨[9,10,24],1⟩,⟨[13,23,24],1⟩,⟨[11,12,24],1⟩,⟨[25],2⟩,⟨[10,13,14,25],1⟩,⟨[9,22,23,25],1⟩,⟨[11,25],1⟩,⟨[12,25],1⟩,⟨[24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case14

namespace Case15
def positionFn : Fin 10 → Fin 25 := ![8,14,22,9,12,11,13,10,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0,1,2},{3},{2,3},{4},{1,4},{0,3,4},{5},{0,5},{1,3,5},{6},{0,6},{2,4,6},{7},{1,7},{2,5,7},{3,6,7},{8},{2,8},{4,5,8},{1,6,8},{0,7,8},{9},{0,9},{1,9},{2,9},{5,6,9},{4,7,9},{3,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,4,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={2,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else if T={9} then 1 else if T={0,9} then 1 else if T={1,9} then 1 else if T={2,9} then 1 else if T={5,6,9} then 1 else if T={4,7,9} then 1 else if T={3,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,23,24,25],[⟨[],6⟩,⟨[9,15,23],1⟩,⟨[10],1⟩,⟨[10,23],1⟩,⟨[13],1⟩,⟨[13,15],1⟩,⟨[9,10,13],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[10,12,15],1⟩,⟨[14],1⟩,⟨[9,14],1⟩,⟨[13,14,23],1⟩,⟨[11],1⟩,⟨[11,15],1⟩,⟨[11,12,23],1⟩,⟨[10,11,14],1⟩,⟨[24],1⟩,⟨[23,24],1⟩,⟨[12,13,24],1⟩,⟨[14,15,24],1⟩,⟨[9,11,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[15,25],1⟩,⟨[23,25],1⟩,⟨[12,14,25],1⟩,⟨[11,13,25],1⟩,⟨[10,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case15

namespace Case16
def positionFn : Fin 10 → Fin 25 := ![8,14,22,9,10,11,13,12,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{3},{0,1,3},{2,3},{4},{1,4},{0,2,4},{5},{0,5},{1,2,5},{6},{0,6},{3,4,6},{7},{1,7},{3,5,7},{2,6,7},{8},{2,8},{4,5,8},{1,6,8},{0,7,8},{9},{0,9},{1,9},{2,9},{5,6,9},{4,7,9},{3,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={3} then 1 else if T={0,1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,2,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={3,4,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 1 else if T={2,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else if T={9} then 1 else if T={0,9} then 1 else if T={1,9} then 1 else if T={2,9} then 1 else if T={5,6,9} then 1 else if T={4,7,9} then 1 else if T={3,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,23,24,25],[⟨[],6⟩,⟨[10],1⟩,⟨[9,10,15],1⟩,⟨[10,23],1⟩,⟨[11],1⟩,⟨[11,15],1⟩,⟨[9,11,23],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[12,15,23],1⟩,⟨[14],1⟩,⟨[9,14],1⟩,⟨[10,11,14],1⟩,⟨[13],1⟩,⟨[13,15],1⟩,⟨[10,12,13],1⟩,⟨[13,14,23],1⟩,⟨[24],1⟩,⟨[23,24],1⟩,⟨[11,12,24],1⟩,⟨[14,15,24],1⟩,⟨[9,13,24],1⟩,⟨[25],1⟩,⟨[9,25],1⟩,⟨[15,25],1⟩,⟨[23,25],1⟩,⟨[12,14,25],1⟩,⟨[11,13,25],1⟩,⟨[10,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case16

namespace Case17
def positionFn : Fin 10 → Fin 25 := ![12,8,13,22,11,14,23,9,10,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{2,3},{1,4},{0,3,4},{1,5},{4,5},{2,6},{3,6},{0,5,6},{7},{0,7},{1,3,7},{2,5,7},{4,6,7},{8},{0,8},{2,4,8},{3,5,8},{1,6,8},{9},{0,1,2,9},{3,9},{4,9},{5,9},{6,9},{7,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={2,3} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={1,5} then 1 else if T={4,5} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={0,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={2,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={1,6,8} then 1 else if T={9} then 1 else if T={0,1,2,9} then 1 else if T={3,9} then 1 else if T={4,9} then 1 else if T={5,9} then 1 else if T={6,9} then 1 else if T={7,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,23,24,25],[⟨[],6⟩,⟨[13],1⟩,⟨[9],1⟩,⟨[14],1⟩,⟨[14,23],1⟩,⟨[9,12],1⟩,⟨[12,13,23],1⟩,⟨[9,15],1⟩,⟨[12,15],1⟩,⟨[14,24],1⟩,⟨[23,24],1⟩,⟨[13,15,24],1⟩,⟨[10],1⟩,⟨[10,13],1⟩,⟨[9,10,23],1⟩,⟨[10,14,15],1⟩,⟨[10,12,24],1⟩,⟨[11],1⟩,⟨[11,13],1⟩,⟨[11,12,14],1⟩,⟨[11,15,23],1⟩,⟨[9,11,24],1⟩,⟨[25],1⟩,⟨[9,13,14,25],1⟩,⟨[23,25],1⟩,⟨[12,25],1⟩,⟨[15,25],1⟩,⟨[24,25],1⟩,⟨[10,11,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case17

namespace Case18
def positionFn : Fin 10 → Fin 25 := ![8,21,22,9,23,12,11,10,13,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{2,3},{2,4},{3,4},{5},{1,5},{0,3,5},{6},{0,6},{1,3,6},{4,5,6},{7},{1,7},{0,4,7},{2,6,7},{8},{0,8},{1,4,8},{2,5,8},{3,7,8},{9},{0,1,2,9},{3,9},{4,9},{5,7,9},{6,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={2,3} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={0,3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={0,4,7} then 1 else if T={2,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={2,5,8} then 1 else if T={3,7,8} then 1 else if T={9} then 2 else if T={0,1,2,9} then 1 else if T={3,9} then 1 else if T={4,9} then 1 else if T={5,7,9} then 1 else if T={6,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,22,23,24,25],[⟨[],5⟩,⟨[9],1⟩,⟨[22],1⟩,⟨[23],1⟩,⟨[10,23],1⟩,⟨[23,24],1⟩,⟨[10,24],1⟩,⟨[13],1⟩,⟨[13,22],1⟩,⟨[9,10,13],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[10,12,22],1⟩,⟨[12,13,24],1⟩,⟨[11],1⟩,⟨[11,22],1⟩,⟨[9,11,24],1⟩,⟨[11,12,23],1⟩,⟨[14],1⟩,⟨[9,14],1⟩,⟨[14,22,24],1⟩,⟨[13,14,23],1⟩,⟨[10,11,14],1⟩,⟨[25],2⟩,⟨[9,22,23,25],1⟩,⟨[10,25],1⟩,⟨[24,25],1⟩,⟨[11,13,25],1⟩,⟨[12,14,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case18

namespace Case19
def positionFn : Fin 10 → Fin 25 := ![13,11,8,22,9,10,14,12,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{0,1,2},{3},{2,3},{4},{1,4},{0,3,4},{5},{0,5},{6},{2,6},{3,6},{1,5,6},{7},{1,7},{4,7},{3,5,7},{8},{0,8},{5,8},{4,6,8},{2,7,8},{9},{2,4,5,9},{0,6,7,9},{1,3,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={1,5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={4,7} then 1 else if T={3,5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else if T={9} then 4 else if T={2,4,5,9} then 1 else if T={0,6,7,9} then 1 else if T={1,3,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,23,24,25],[⟨[],3⟩,⟨[14],1⟩,⟨[12],1⟩,⟨[9],1⟩,⟨[9,12,14],1⟩,⟨[23],1⟩,⟨[9,23],1⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[10,14,23],1⟩,⟨[11],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[15,23],1⟩,⟨[11,12,15],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[10,13],1⟩,⟨[11,13,23],1⟩,⟨[24],1⟩,⟨[14,24],1⟩,⟨[11,24],1⟩,⟨[10,15,24],1⟩,⟨[9,13,24],1⟩,⟨[25],4⟩,⟨[9,10,11,25],1⟩,⟨[13,14,15,25],1⟩,⟨[12,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case19

namespace Case20
def positionFn : Fin 10 → Fin 25 := ![8,22,23,9,12,11,13,10,14,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0},{1},{2},{3},{2,3},{4},{1,4},{0,3,4},{5},{0,5},{1,3,5},{6},{0,6},{2,4,6},{7},{1,7},{2,5,7},{3,6,7},{8},{2,8},{4,5,8},{1,6,8},{0,7,8},{9},{0,1,2,9},{5,6,9},{4,7,9},{3,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,4,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={2,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else if T={9} then 3 else if T={0,1,2,9} then 1 else if T={5,6,9} then 1 else if T={4,7,9} then 1 else if T={3,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,23,24,25],[⟨[],4⟩,⟨[9],1⟩,⟨[23],1⟩,⟨[24],1⟩,⟨[10],1⟩,⟨[10,24],1⟩,⟨[13],1⟩,⟨[13,23],1⟩,⟨[9,10,13],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[10,12,23],1⟩,⟨[14],1⟩,⟨[9,14],1⟩,⟨[13,14,24],1⟩,⟨[11],1⟩,⟨[11,23],1⟩,⟨[11,12,24],1⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[15,24],1⟩,⟨[12,13,15],1⟩,⟨[14,15,23],1⟩,⟨[9,11,15],1⟩,⟨[25],3⟩,⟨[9,23,24,25],1⟩,⟨[12,14,25],1⟩,⟨[11,13,25],1⟩,⟨[10,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case20

namespace Case21
def positionFn : Fin 10 → Fin 25 := ![7,22,23,12,11,8,10,13,9,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{1,3},{2,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{0,6},{2,6},{3,6},{1,5,6},{0,7},{1,7},{4,7},{3,5,7},{0,8},{1,8},{5,8},{4,6,8},{2,7,8},{9},{0,1,2,9},{4,5,9},{6,7,9},{3,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 8 else if T={1,3} then 1 else if T={2,3} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={1,5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={4,7} then 1 else if T={3,5,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else if T={9} then 2 else if T={0,1,2,9} then 1 else if T={4,5,9} then 1 else if T={6,7,9} then 1 else if T={3,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[8,9,10,11,12,13,14,23,24,25],[⟨[],8⟩,⟨[13,23],1⟩,⟨[13,24],1⟩,⟨[12,23],1⟩,⟨[12,24],1⟩,⟨[8,12,13],1⟩,⟨[8,9],1⟩,⟨[9,24],1⟩,⟨[8,11],1⟩,⟨[11,24],1⟩,⟨[11,13],1⟩,⟨[9,11,23],1⟩,⟨[8,14],1⟩,⟨[14,23],1⟩,⟨[12,14],1⟩,⟨[9,13,14],1⟩,⟨[8,10],1⟩,⟨[10,23],1⟩,⟨[9,10],1⟩,⟨[10,11,12],1⟩,⟨[10,14,24],1⟩,⟨[25],2⟩,⟨[8,23,24,25],1⟩,⟨[9,12,25],1⟩,⟨[11,14,25],1⟩,⟨[10,13,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case21

namespace Case22
def positionFn : Fin 10 → Fin 25 := ![10,12,7,11,8,22,9,13,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0,1,2},{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{3,4,5},{1,6},{2,6},{4,6},{5,6},{0,7},{2,7},{3,7},{5,7},{0,8},{1,8},{3,8},{4,8},{6,7,8},{9},{0,3,6,9},{1,4,7,9},{2,5,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={0,1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,4,5} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,8} then 1 else if T={4,8} then 1 else if T={6,7,8} then 1 else if T={9} then 3 else if T={0,3,6,9} then 1 else if T={1,4,7,9} then 1 else if T={2,5,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[8,9,10,11,12,13,14,23,24,25],[⟨[],7⟩,⟨[8,11,13],1⟩,⟨[12,13],1⟩,⟨[8,12],1⟩,⟨[9,11],1⟩,⟨[8,9],1⟩,⟨[11,23],1⟩,⟨[13,23],1⟩,⟨[9,12,23],1⟩,⟨[10,13],1⟩,⟨[8,10],1⟩,⟨[9,10],1⟩,⟨[10,23],1⟩,⟨[11,14],1⟩,⟨[8,14],1⟩,⟨[12,14],1⟩,⟨[14,23],1⟩,⟨[11,24],1⟩,⟨[13,24],1⟩,⟨[12,24],1⟩,⟨[9,24],1⟩,⟨[10,14,24],1⟩,⟨[25],3⟩,⟨[10,11,12,25],1⟩,⟨[9,13,14,25],1⟩,⟨[8,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case22

namespace Case23
def positionFn : Fin 10 → Fin 25 := ![9,20,21,22,10,11,12,13,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{1,3},{2,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{0,6},{2,6},{3,6},{1,5,6},{0,7},{1,7},{4,7},{3,5,7},{0,8},{1,8},{5,8},{4,6,8},{2,7,8},{9},{0,1,2,9},{4,5,9},{6,7,9},{3,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 7 else if T={1,3} then 1 else if T={2,3} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={1,5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={4,7} then 1 else if T={3,5,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else if T={9} then 3 else if T={0,1,2,9} then 1 else if T={4,5,9} then 1 else if T={6,7,9} then 1 else if T={3,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,21,22,23,24,25],[⟨[],7⟩,⟨[21,23],1⟩,⟨[22,23],1⟩,⟨[11,21],1⟩,⟨[11,22],1⟩,⟨[10,11,23],1⟩,⟨[10,12],1⟩,⟨[12,22],1⟩,⟨[10,13],1⟩,⟨[13,22],1⟩,⟨[13,23],1⟩,⟨[12,13,21],1⟩,⟨[10,14],1⟩,⟨[14,21],1⟩,⟨[11,14],1⟩,⟨[12,14,23],1⟩,⟨[10,24],1⟩,⟨[21,24],1⟩,⟨[12,24],1⟩,⟨[11,13,24],1⟩,⟨[14,22,24],1⟩,⟨[25],3⟩,⟨[10,21,22,25],1⟩,⟨[11,12,25],1⟩,⟨[13,14,25],1⟩,⟨[23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case23

namespace Case24
def positionFn : Fin 10 → Fin 25 := ![11,8,9,10,13,22,12,14,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 10 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 10)) := [∅,{0,1,2},{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{3,4,5},{1,6},{2,6},{4,6},{5,6},{0,7},{2,7},{3,7},{5,7},{0,8},{1,8},{3,8},{4,8},{6,7,8},{9},{0,3,6,9},{1,4,7,9},{2,5,8,9}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 10)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,4,5} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,8} then 1 else if T={4,8} then 1 else if T={6,7,8} then 1 else if T={9} then 4 else if T={0,3,6,9} then 1 else if T={1,4,7,9} then 1 else if T={2,5,8,9} then 1 else 0) else 0
theorem support (T : Finset (Fin 10)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,23,24,25],[⟨[],6⟩,⟨[9,10,12],1⟩,⟨[9,11],1⟩,⟨[10,11],1⟩,⟨[12,14],1⟩,⟨[10,14],1⟩,⟨[12,23],1⟩,⟨[9,23],1⟩,⟨[11,14,23],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[13,14],1⟩,⟨[13,23],1⟩,⟨[12,15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[15,23],1⟩,⟨[12,24],1⟩,⟨[9,24],1⟩,⟨[11,24],1⟩,⟨[14,24],1⟩,⟨[13,15,24],1⟩,⟨[25],4⟩,⟨[11,12,13,25],1⟩,⟨[9,14,15,25],1⟩,⟨[10,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case24
def μ : Fin 25 → Finset (Fin 10) → ℕ := ![Case0.μ,Case1.μ,Case2.μ,Case3.μ,Case4.μ,Case5.μ,Case6.μ,Case7.μ,Case8.μ,Case9.μ,Case10.μ,Case11.μ,Case12.μ,Case13.μ,Case14.μ,Case15.μ,Case16.μ,Case17.μ,Case18.μ,Case19.μ,Case20.μ,Case21.μ,Case22.μ,Case23.μ,Case24.μ]
end Aris4Math.ThirtyFour.TwentyFiveNineLowTenth

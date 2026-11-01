import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case6216
def positionFn : Fin 9 → Fin 25 := ![16,17,18,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{1,2},{3},{4},{3,4},{5},{0,5},{1,5},{6},{0,1,4,6},{2,3,5,6},{7},{1,7},{0,3,7},{2,4,7},{5,7},{8},{0,8},{2,8},{1,3,8},{4,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,5} then 1 else if T={6} then 4 else if T={0,1,4,6} then 1 else if T={2,3,5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,3,8} then 1 else if T={4,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[17,18,19,20,21,22,23,24,25],[⟨[],1⟩,⟨[17],1⟩,⟨[18],1⟩,⟨[19],1⟩,⟨[17,19],1⟩,⟨[18,19],1⟩,⟨[20],2⟩,⟨[21],2⟩,⟨[20,21],1⟩,⟨[22],2⟩,⟨[17,22],1⟩,⟨[18,22],1⟩,⟨[23],4⟩,⟨[17,18,21,23],1⟩,⟨[19,20,22,23],1⟩,⟨[24],2⟩,⟨[18,24],1⟩,⟨[17,20,24],1⟩,⟨[19,21,24],1⟩,⟨[22,24],1⟩,⟨[25],2⟩,⟨[17,25],1⟩,⟨[19,25],1⟩,⟨[18,20,25],1⟩,⟨[21,22,25],1⟩,⟨[23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6216
namespace Case6216
def big : Finset (Finset (Fin 9)) := {{0,1,4,6},{2,3,5,6},{0,3,7},{2,4,7},{1,3,8},{4,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{3,4},{0,5},{1,5},{0,1,4,6},{2,3,5,6},{1,7},{0,3,7},{2,4,7},{5,7},{0,8},{2,8},{1,3,8},{4,5,8},{6,7,8}]
end Case6216
namespace Case6217
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{0,2},{3},{4},{2,4},{0,3,4},{5},{1,5},{2,5},{4,5},{6},{1,2,3,6},{7},{3,7},{1,4,7},{0,5,6,7},{8},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 4 else if T={1,2,3,6} then 1 else if T={7} then 3 else if T={3,7} then 1 else if T={1,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[10,13,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],4⟩,⟨[11,12,13,16],1⟩,⟨[17],3⟩,⟨[13,17],1⟩,⟨[11,14,17],1⟩,⟨[10,15,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[13,15,18],1⟩,⟨[14,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6217
namespace Case6217
def big : Finset (Finset (Fin 9)) := {{0,3,4},{1,2,3,6},{1,4,7},{0,5,6,7},{3,5,8},{4,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{2,4},{0,3,4},{1,5},{2,5},{4,5},{1,2,3,6},{3,7},{1,4,7},{0,5,6,7},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]
end Case6217
namespace Case6218
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{0,2},{3},{4},{0,4},{2,4},{5},{1,5},{2,5},{3,4,5},{6},{1,2,3,6},{7},{3,7},{1,4,7},{0,5,6,7},{8},{1,8},{0,3,8},{5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 4 else if T={1,2,3,6} then 1 else if T={7} then 3 else if T={3,7} then 1 else if T={1,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={0,3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],4⟩,⟨[11,12,13,16],1⟩,⟨[17],3⟩,⟨[13,17],1⟩,⟨[11,14,17],1⟩,⟨[10,15,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[10,13,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6218
namespace Case6218
def big : Finset (Finset (Fin 9)) := {{3,4,5},{1,2,3,6},{1,4,7},{0,5,6,7},{0,3,8},{4,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{0,4},{2,4},{1,5},{2,5},{3,4,5},{1,2,3,6},{3,7},{1,4,7},{0,5,6,7},{1,8},{0,3,8},{5,8},{4,6,8},{2,7,8}]
end Case6218
namespace Case6219
def positionFn : Fin 9 → Fin 25 := ![16,17,18,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{1,2},{3},{4},{1,4},{0,3,4},{5},{0,5},{1,5},{4,5},{6},{2,3,5,6},{7},{3,7},{2,4,7},{0,1,6,7},{8},{0,8},{2,8},{1,3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 4 else if T={2,3,5,6} then 1 else if T={7} then 3 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[17,18,19,20,21,22,23,24,25],[⟨[],1⟩,⟨[17],1⟩,⟨[18],1⟩,⟨[19],1⟩,⟨[17,19],1⟩,⟨[18,19],1⟩,⟨[20],2⟩,⟨[21],1⟩,⟨[18,21],1⟩,⟨[17,20,21],1⟩,⟨[22],2⟩,⟨[17,22],1⟩,⟨[18,22],1⟩,⟨[21,22],1⟩,⟨[23],4⟩,⟨[19,20,22,23],1⟩,⟨[24],3⟩,⟨[20,24],1⟩,⟨[19,21,24],1⟩,⟨[17,18,23,24],1⟩,⟨[25],2⟩,⟨[17,25],1⟩,⟨[19,25],1⟩,⟨[18,20,25],1⟩,⟨[21,23,25],1⟩,⟨[22,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6219
namespace Case6219
def big : Finset (Finset (Fin 9)) := {{0,3,4},{2,3,5,6},{2,4,7},{0,1,6,7},{1,3,8},{4,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,4},{0,3,4},{0,5},{1,5},{4,5},{2,3,5,6},{3,7},{2,4,7},{0,1,6,7},{0,8},{2,8},{1,3,8},{4,6,8},{5,7,8}]
end Case6219
namespace Case6220
def positionFn : Fin 9 → Fin 25 := ![16,17,18,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{1,2},{3},{4},{1,4},{2,4},{0,3,4},{5},{0,5},{1,5},{6},{2,3,5,6},{7},{3,7},{4,5,7},{0,1,6,7},{8},{0,8},{1,3,8},{5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,5} then 1 else if T={6} then 4 else if T={2,3,5,6} then 1 else if T={7} then 3 else if T={3,7} then 1 else if T={4,5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[17,18,19,20,21,22,23,24,25],[⟨[],1⟩,⟨[17],1⟩,⟨[18],1⟩,⟨[19],1⟩,⟨[17,19],1⟩,⟨[18,19],1⟩,⟨[20],2⟩,⟨[21],1⟩,⟨[18,21],1⟩,⟨[19,21],1⟩,⟨[17,20,21],1⟩,⟨[22],2⟩,⟨[17,22],1⟩,⟨[18,22],1⟩,⟨[23],4⟩,⟨[19,20,22,23],1⟩,⟨[24],3⟩,⟨[20,24],1⟩,⟨[21,22,24],1⟩,⟨[17,18,23,24],1⟩,⟨[25],2⟩,⟨[17,25],1⟩,⟨[18,20,25],1⟩,⟨[22,25],1⟩,⟨[21,23,25],1⟩,⟨[19,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6220
namespace Case6220
def big : Finset (Finset (Fin 9)) := {{0,3,4},{2,3,5,6},{4,5,7},{0,1,6,7},{1,3,8},{4,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,4},{2,4},{0,3,4},{0,5},{1,5},{2,3,5,6},{3,7},{4,5,7},{0,1,6,7},{0,8},{1,3,8},{5,8},{4,6,8},{2,7,8}]
end Case6220
namespace Case6221
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{1,2},{3},{1,3},{4},{0,4},{2,4},{5},{0,5},{1,5},{3,5},{6},{3,4,6},{7},{0,3,7},{1,4,7},{2,5,6,7},{8},{2,3,8},{4,5,8},{0,1,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={6} then 4 else if T={3,4,6} then 1 else if T={7} then 3 else if T={0,3,7} then 1 else if T={1,4,7} then 1 else if T={2,5,6,7} then 1 else if T={8} then 3 else if T={2,3,8} then 1 else if T={4,5,8} then 1 else if T={0,1,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[17],4⟩,⟨[14,15,17],1⟩,⟨[18],3⟩,⟨[11,14,18],1⟩,⟨[12,15,18],1⟩,⟨[13,16,17,18],1⟩,⟨[19],3⟩,⟨[13,14,19],1⟩,⟨[15,16,19],1⟩,⟨[11,12,17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6221
namespace Case6221
def big : Finset (Finset (Fin 9)) := {{3,4,6},{0,3,7},{1,4,7},{2,5,6,7},{2,3,8},{4,5,8},{0,1,6,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{0,4},{2,4},{0,5},{1,5},{3,5},{3,4,6},{0,3,7},{1,4,7},{2,5,6,7},{2,3,8},{4,5,8},{0,1,6,8},{7,8}]
end Case6221
namespace Case6222
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,1,2,4},{3,4},{5},{0,5},{1,5},{6},{0,6},{1,6},{2,3,5,6},{7},{1,7},{0,3,7},{4,5,7},{6,7},{8},{0,8},{1,3,8},{5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={4} then 2 else if T={0,1,2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,3,5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,3,7} then 1 else if T={4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],3⟩,⟨[14],2⟩,⟨[15],2⟩,⟨[11,12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,14,16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[11,14,18],1⟩,⟨[15,16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,14,19],1⟩,⟨[16,19],1⟩,⟨[15,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6222
namespace Case6222
def big : Finset (Finset (Fin 9)) := {{0,1,2,4},{2,3,5,6},{0,3,7},{4,5,7},{1,3,8},{4,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2,4},{3,4},{0,5},{1,5},{0,6},{1,6},{2,3,5,6},{1,7},{0,3,7},{4,5,7},{6,7},{0,8},{1,3,8},{5,8},{4,6,8},{2,7,8}]
end Case6222
namespace Case6223
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,2,3},{4},{1,4},{5},{0,5},{1,5},{3,4,5},{6},{0,6},{1,6},{4,6},{7},{3,7},{0,4,7},{2,5,6,7},{8},{0,8},{2,4,8},{5,8},{3,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={0,1,2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={4,6} then 1 else if T={7} then 3 else if T={3,7} then 1 else if T={0,4,7} then 1 else if T={2,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],3⟩,⟨[14],2⟩,⟨[11,12,13,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[18],3⟩,⟨[14,18],1⟩,⟨[11,15,18],1⟩,⟨[13,16,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,15,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6223
namespace Case6223
def big : Finset (Finset (Fin 9)) := {{0,1,2,3},{3,4,5},{0,4,7},{2,5,6,7},{2,4,8},{3,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2,3},{1,4},{0,5},{1,5},{3,4,5},{0,6},{1,6},{4,6},{3,7},{0,4,7},{2,5,6,7},{0,8},{2,4,8},{5,8},{3,6,8},{1,7,8}]
end Case6223
namespace Case6224
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{1,4},{0,3,4},{5},{0,5},{1,5},{6},{0,6},{1,6},{4,6},{2,3,5,6},{7},{0,1,2,7},{3,7},{4,5,7},{8},{0,8},{1,3,8},{2,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={4,6} then 1 else if T={2,3,5,6} then 1 else if T={7} then 3 else if T={0,1,2,7} then 1 else if T={3,7} then 1 else if T={4,5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],3⟩,⟨[14],2⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[11,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[13,14,16,17],1⟩,⟨[18],3⟩,⟨[11,12,13,18],1⟩,⟨[14,18],1⟩,⟨[15,16,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,14,19],1⟩,⟨[13,15,19],1⟩,⟨[16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6224
namespace Case6224
def big : Finset (Finset (Fin 9)) := {{0,3,4},{2,3,5,6},{0,1,2,7},{4,5,7},{1,3,8},{2,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{1,4},{0,3,4},{0,5},{1,5},{0,6},{1,6},{4,6},{2,3,5,6},{0,1,2,7},{3,7},{4,5,7},{0,8},{1,3,8},{2,4,8},{5,8},{6,7,8}]
end Case6224
namespace Case6225
def positionFn : Fin 9 → Fin 25 := ![8,9,10,11,12,13,14,15,16]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{1,3},{4},{0,4},{2,3,4},{5},{0,5},{1,5},{4,5},{6},{0,6},{1,6},{3,6},{7},{0,3,7},{1,4,7},{2,5,6,7},{8},{0,1,2,8},{3,5,8},{4,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={2} then 3 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={7} then 3 else if T={0,3,7} then 1 else if T={1,4,7} then 1 else if T={2,5,6,7} then 1 else if T={8} then 3 else if T={0,1,2,8} then 1 else if T={3,5,8} then 1 else if T={4,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,16,17],[⟨[],1⟩,⟨[9],1⟩,⟨[10],1⟩,⟨[11],3⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[11,12,13],1⟩,⟨[14],2⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[9,15],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[16],3⟩,⟨[9,12,16],1⟩,⟨[10,13,16],1⟩,⟨[11,14,15,16],1⟩,⟨[17],3⟩,⟨[9,10,11,17],1⟩,⟨[12,14,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6225
namespace Case6225
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,3,7},{1,4,7},{2,5,6,7},{0,1,2,8},{3,5,8},{4,6,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,4},{2,3,4},{0,5},{1,5},{4,5},{0,6},{1,6},{3,6},{0,3,7},{1,4,7},{2,5,6,7},{0,1,2,8},{3,5,8},{4,6,8},{7,8}]
end Case6225
namespace Case6226
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{2,3},{4},{1,4},{0,2,4},{5},{0,5},{1,5},{3,4,5},{6},{0,6},{1,6},{4,6},{7},{0,1,3,7},{2,5,6,7},{8},{0,8},{1,2,8},{5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,2,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={4,6} then 1 else if T={7} then 4 else if T={0,1,3,7} then 1 else if T={2,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[10,12,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[14,16],1⟩,⟨[17],4⟩,⟨[10,11,13,17],1⟩,⟨[12,15,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,12,18],1⟩,⟨[15,18],1⟩,⟨[13,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6226
namespace Case6226
def big : Finset (Finset (Fin 9)) := {{0,2,4},{3,4,5},{0,1,3,7},{2,5,6,7},{1,2,8},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{2,3},{1,4},{0,2,4},{0,5},{1,5},{3,4,5},{0,6},{1,6},{4,6},{0,1,3,7},{2,5,6,7},{0,8},{1,2,8},{5,8},{3,6,8},{4,7,8}]
end Case6226
namespace Case6227
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{1,3},{4},{0,4},{5},{0,5},{1,5},{2,3,5},{4,5},{6},{0,6},{1,6},{3,6},{2,4,6},{7},{0,1,2,7},{3,4,7},{8},{2,8},{0,3,8},{1,4,8},{5,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={7} then 4 else if T={0,1,2,7} then 1 else if T={3,4,7} then 1 else if T={8} then 3 else if T={2,8} then 1 else if T={0,3,8} then 1 else if T={1,4,8} then 1 else if T={5,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[14,17],1⟩,⟨[13,15,17],1⟩,⟨[18],4⟩,⟨[11,12,13,18],1⟩,⟨[14,15,18],1⟩,⟨[19],3⟩,⟨[13,19],1⟩,⟨[11,14,19],1⟩,⟨[12,15,19],1⟩,⟨[16,17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6227
namespace Case6227
def big : Finset (Finset (Fin 9)) := {{2,3,5},{2,4,6},{0,1,2,7},{3,4,7},{0,3,8},{1,4,8},{5,6,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,4},{0,5},{1,5},{2,3,5},{4,5},{0,6},{1,6},{3,6},{2,4,6},{0,1,2,7},{3,4,7},{2,8},{0,3,8},{1,4,8},{5,6,7,8}]
end Case6227
namespace Case6228
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{1,3},{0,2,3},{4},{0,4},{1,2,4},{5},{0,5},{1,5},{4,5},{6},{0,6},{1,6},{3,6},{7},{3,4,7},{2,5,6,7},{8},{2,8},{3,5,8},{4,6,8},{0,1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={3} then 1 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={7} then 4 else if T={3,4,7} then 1 else if T={2,5,6,7} then 1 else if T={8} then 3 else if T={2,8} then 1 else if T={3,5,8} then 1 else if T={4,6,8} then 1 else if T={0,1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,13,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[14,17],1⟩,⟨[18],4⟩,⟨[14,15,18],1⟩,⟨[13,16,17,18],1⟩,⟨[19],3⟩,⟨[13,19],1⟩,⟨[14,16,19],1⟩,⟨[15,17,19],1⟩,⟨[11,12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6228
namespace Case6228
def big : Finset (Finset (Fin 9)) := {{0,2,3},{1,2,4},{3,4,7},{2,5,6,7},{3,5,8},{4,6,8},{0,1,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,2,3},{0,4},{1,2,4},{0,5},{1,5},{4,5},{0,6},{1,6},{3,6},{3,4,7},{2,5,6,7},{2,8},{3,5,8},{4,6,8},{0,1,7,8}]
end Case6228
namespace Case6229
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{3},{4},{3,4},{5},{1,5},{0,2,3,5},{6},{0,6},{1,2,4,6},{5,6},{7},{1,3,7},{0,4,7},{5,7},{6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={4} then 2 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={0,2,3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,3,7} then 1 else if T={0,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[10,12,13,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[11,12,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,13,17],1⟩,⟨[10,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[14,15,18],1⟩,⟨[13,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6229
namespace Case6229
def big : Finset (Finset (Fin 9)) := {{0,2,3,5},{1,2,4,6},{1,3,7},{0,4,7},{4,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{3,4},{1,5},{0,2,3,5},{0,6},{1,2,4,6},{5,6},{1,3,7},{0,4,7},{5,7},{6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
end Case6229
namespace Case6230
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{3},{4},{0,3,4},{5},{1,5},{4,5},{6},{0,6},{1,2,3,6},{4,6},{5,6},{7},{3,7},{1,4,7},{0,2,5,7},{8},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,2,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={3,7} then 1 else if T={1,4,7} then 1 else if T={0,2,5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[10,13,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[11,12,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[13,17],1⟩,⟨[11,14,17],1⟩,⟨[10,12,15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6230
namespace Case6230
def big : Finset (Finset (Fin 9)) := {{0,3,4},{1,2,3,6},{1,4,7},{0,2,5,7},{2,4,8},{3,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,3,4},{1,5},{4,5},{0,6},{1,2,3,6},{4,6},{5,6},{3,7},{1,4,7},{0,2,5,7},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}]
end Case6230
namespace Case6231
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{3},{4},{0,4},{1,4},{5},{1,5},{3,4,5},{6},{0,6},{1,2,3,6},{5,6},{7},{3,7},{0,2,5,7},{4,6,7},{8},{0,3,8},{2,4,8},{5,8},{6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,2,3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={3,7} then 1 else if T={0,2,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,3,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[11,12,13,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[13,17],1⟩,⟨[10,12,15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,13,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6231
namespace Case6231
def big : Finset (Finset (Fin 9)) := {{3,4,5},{1,2,3,6},{0,2,5,7},{4,6,7},{0,3,8},{2,4,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,4},{1,4},{1,5},{3,4,5},{0,6},{1,2,3,6},{5,6},{3,7},{0,2,5,7},{4,6,7},{0,3,8},{2,4,8},{5,8},{6,8},{1,7,8}]
end Case6231
namespace Case6232
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{3},{4},{0,4},{1,4},{2,3,4},{5},{0,5},{3,5},{6},{1,6},{3,6},{5,6},{7},{0,3,7},{1,2,5,7},{4,6,7},{8},{1,3,8},{4,5,8},{0,2,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={0,3,7} then 1 else if T={1,2,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={1,3,8} then 1 else if T={4,5,8} then 1 else if T={0,2,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[14,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[11,14,18],1⟩,⟨[12,13,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],3⟩,⟨[12,14,19],1⟩,⟨[15,16,19],1⟩,⟨[11,13,17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6232
namespace Case6232
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,3,7},{1,2,5,7},{4,6,7},{1,3,8},{4,5,8},{0,2,6,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,4},{1,4},{2,3,4},{0,5},{3,5},{1,6},{3,6},{5,6},{0,3,7},{1,2,5,7},{4,6,7},{1,3,8},{4,5,8},{0,2,6,8},{7,8}]
end Case6232
namespace Case6233
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{3},{2,3},{4},{0,2,4},{1,3,4},{5},{0,5},{4,5},{6},{1,6},{4,6},{5,6},{7},{1,2,5,7},{0,3,6,7},{8},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,2,4} then 1 else if T={1,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 4 else if T={1,2,5,7} then 1 else if T={0,3,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,5,8} then 1 else if T={2,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,13,15],1⟩,⟨[12,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],4⟩,⟨[12,13,16,18],1⟩,⟨[11,14,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[14,16,19],1⟩,⟨[13,17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6233
namespace Case6233
def big : Finset (Finset (Fin 9)) := {{0,2,4},{1,3,4},{1,2,5,7},{0,3,6,7},{3,5,8},{2,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{2,3},{0,2,4},{1,3,4},{0,5},{4,5},{1,6},{4,6},{5,6},{1,2,5,7},{0,3,6,7},{0,8},{1,8},{3,5,8},{2,6,8},{4,7,8}]
end Case6233
namespace Case6234
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{3},{2,3},{4},{0,4},{1,4},{5},{1,5},{2,4,5},{6},{0,6},{3,4,6},{5,6},{7},{0,3,5,7},{1,2,6,7},{8},{0,2,8},{1,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 4 else if T={0,3,5,7} then 1 else if T={1,2,6,7} then 1 else if T={8} then 2 else if T={0,2,8} then 1 else if T={1,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[13,15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],4⟩,⟨[11,14,16,18],1⟩,⟨[12,13,17,18],1⟩,⟨[19],2⟩,⟨[11,13,19],1⟩,⟨[12,14,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6234
namespace Case6234
def big : Finset (Finset (Fin 9)) := {{2,4,5},{3,4,6},{0,3,5,7},{1,2,6,7},{0,2,8},{1,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{2,3},{0,4},{1,4},{1,5},{2,4,5},{0,6},{3,4,6},{5,6},{0,3,5,7},{1,2,6,7},{0,2,8},{1,3,8},{5,8},{6,8},{4,7,8}]
end Case6234
namespace Case6235
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{3},{0,2,3},{4},{0,4},{1,4},{5},{1,5},{3,5},{2,4,5},{6},{0,6},{3,6},{5,6},{7},{3,4,7},{1,2,6,7},{8},{2,8},{1,3,8},{4,6,8},{0,5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 4 else if T={3,4,7} then 1 else if T={1,2,6,7} then 1 else if T={8} then 3 else if T={2,8} then 1 else if T={1,3,8} then 1 else if T={4,6,8} then 1 else if T={0,5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[10,12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[12,14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],4⟩,⟨[13,14,17],1⟩,⟨[11,12,16,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[11,13,18],1⟩,⟨[14,16,18],1⟩,⟨[10,15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6235
namespace Case6235
def big : Finset (Finset (Fin 9)) := {{0,2,3},{2,4,5},{3,4,7},{1,2,6,7},{1,3,8},{4,6,8},{0,5,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2,3},{0,4},{1,4},{1,5},{3,5},{2,4,5},{0,6},{3,6},{5,6},{3,4,7},{1,2,6,7},{2,8},{1,3,8},{4,6,8},{0,5,7,8}]
end Case6235
namespace Case6236
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{3},{4},{3,4},{5},{1,5},{0,2,3,5},{6},{0,6},{1,2,4,6},{5,6},{7},{0,7},{1,3,7},{4,5,7},{6,7},{8},{1,8},{0,4,8},{5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={4} then 2 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={0,2,3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={0,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[10,12,13,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[11,12,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,13,17],1⟩,⟨[14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[10,14,18],1⟩,⟨[15,18],1⟩,⟨[13,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6236
namespace Case6236
def big : Finset (Finset (Fin 9)) := {{0,2,3,5},{1,2,4,6},{1,3,7},{4,5,7},{0,4,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{3,4},{1,5},{0,2,3,5},{0,6},{1,2,4,6},{5,6},{0,7},{1,3,7},{4,5,7},{6,7},{1,8},{0,4,8},{5,8},{3,6,8},{2,7,8}]
end Case6236
namespace Case6237
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{3},{4},{0,4},{5},{1,5},{3,4,5},{6},{0,6},{1,2,3,6},{4,6},{5,6},{7},{3,7},{1,4,7},{0,2,5,7},{8},{1,8},{0,3,8},{2,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,2,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={3,7} then 1 else if T={1,4,7} then 1 else if T={0,2,5,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={0,3,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[14],2⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[14,15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,13,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[14,18],1⟩,⟨[12,15,18],1⟩,⟨[11,13,16,18],1⟩,⟨[19],2⟩,⟨[12,19],1⟩,⟨[11,14,19],1⟩,⟨[13,15,19],1⟩,⟨[16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6237
namespace Case6237
def big : Finset (Finset (Fin 9)) := {{3,4,5},{1,2,3,6},{1,4,7},{0,2,5,7},{0,3,8},{2,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,4},{1,5},{3,4,5},{0,6},{1,2,3,6},{4,6},{5,6},{3,7},{1,4,7},{0,2,5,7},{1,8},{0,3,8},{2,4,8},{5,8},{6,7,8}]
end Case6237
namespace Case6238
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{3},{4},{1,4},{0,3,4},{5},{1,5},{4,5},{6},{0,6},{1,2,3,6},{5,6},{7},{3,7},{0,2,5,7},{4,6,7},{8},{0,8},{2,4,8},{3,5,8},{6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,2,3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={3,7} then 1 else if T={0,2,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[10,13,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[11,12,13,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[13,17],1⟩,⟨[10,12,15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6238
namespace Case6238
def big : Finset (Finset (Fin 9)) := {{0,3,4},{1,2,3,6},{0,2,5,7},{4,6,7},{2,4,8},{3,5,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,4},{0,3,4},{1,5},{4,5},{0,6},{1,2,3,6},{5,6},{3,7},{0,2,5,7},{4,6,7},{0,8},{2,4,8},{3,5,8},{6,8},{1,7,8}]
end Case6238
namespace Case6239
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{3},{1,3},{4},{0,4},{2,3,4},{5},{0,5},{4,5},{6},{1,6},{3,6},{5,6},{7},{0,3,7},{1,2,5,7},{4,6,7},{8},{1,4,8},{3,5,8},{0,2,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={0,3,7} then 1 else if T={1,2,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={1,4,8} then 1 else if T={3,5,8} then 1 else if T={0,2,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[14,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[11,14,18],1⟩,⟨[12,13,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],3⟩,⟨[12,15,19],1⟩,⟨[14,16,19],1⟩,⟨[11,13,17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case6239
namespace Case6239
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,3,7},{1,2,5,7},{4,6,7},{1,4,8},{3,5,8},{0,2,6,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{0,4},{2,3,4},{0,5},{4,5},{1,6},{3,6},{5,6},{0,3,7},{1,2,5,7},{4,6,7},{1,4,8},{3,5,8},{0,2,6,8},{7,8}]
end Case6239
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

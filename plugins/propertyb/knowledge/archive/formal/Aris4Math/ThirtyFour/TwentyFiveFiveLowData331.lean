import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case7944
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{3},{0,3},{0,4},{1,4},{2,4},{5},{1,5},{3,5},{4,5},{6},{1,6},{3,4,6},{7},{1,7},{3,7},{0,2,5,6,7},{8},{0,8},{1,2,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 1 else if T={0,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={3,4,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={3,7} then 1 else if T={0,2,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[13,14,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[10,12,15,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,12,13,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7944
namespace Case7944
def big : Finset (Finset (Fin 9)) := {{3,4,6},{0,2,5,6,7},{1,2,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,3},{0,4},{1,4},{2,4},{1,5},{3,5},{4,5},{1,6},{3,4,6},{1,7},{3,7},{0,2,5,6,7},{0,8},{1,2,3,8},{5,8},{6,8},{4,7,8}]
end Case7944
namespace Case7945
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{1,2},{3},{1,3},{4},{0,4},{3,4},{5},{1,5},{4,5},{6},{0,2,3,5,6},{7},{0,7},{2,7},{5,7},{1,4,6,7},{8},{0,8},{1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 4 else if T={0,2,3,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={1,4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[12],2⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[14,15],1⟩,⟨[16],4⟩,⟨[10,12,13,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[11,14,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7945
namespace Case7945
def big : Finset (Finset (Fin 9)) := {{0,2,3,5,6},{1,4,6,7},{2,4,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{1,3},{0,4},{3,4},{1,5},{4,5},{0,2,3,5,6},{0,7},{2,7},{5,7},{1,4,6,7},{0,8},{1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
end Case7945
namespace Case7946
def positionFn : Fin 9 → Fin 25 := ![8,9,10,11,12,13,14,15,16]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{1,2},{3},{1,3},{0,4},{1,4},{5},{1,5},{4,5},{6},{4,6},{0,2,3,5,6},{7},{0,7},{3,7},{2,4,7},{5,7},{8},{0,8},{2,8},{3,4,8},{5,8},{1,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 4 else if T={4,6} then 1 else if T={0,2,3,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={1,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,16,17],[⟨[],1⟩,⟨[9],1⟩,⟨[9,10],1⟩,⟨[11],2⟩,⟨[10,11],1⟩,⟨[12],2⟩,⟨[10,12],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[14],2⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[15],4⟩,⟨[13,15],1⟩,⟨[9,11,12,14,15],1⟩,⟨[16],2⟩,⟨[9,16],1⟩,⟨[12,16],1⟩,⟨[11,13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[9,17],1⟩,⟨[11,17],1⟩,⟨[12,13,17],1⟩,⟨[14,17],1⟩,⟨[10,15,16,17],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7946
namespace Case7946
def big : Finset (Finset (Fin 9)) := {{0,2,3,5,6},{2,4,7},{3,4,8},{1,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{1,3},{0,4},{1,4},{1,5},{4,5},{4,6},{0,2,3,5,6},{0,7},{3,7},{2,4,7},{5,7},{0,8},{2,8},{3,4,8},{5,8},{1,6,7,8}]
end Case7946
namespace Case7947
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{1,2},{3},{0,3},{4},{0,4},{2,4},{5},{1,5},{3,5},{4,5},{6},{1,3,4,6},{7},{1,7},{3,7},{0,2,5,6,7},{8},{0,8},{1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 4 else if T={1,3,4,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={3,7} then 1 else if T={0,2,5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[12],2⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],4⟩,⟨[11,13,14,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[10,12,15,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,13,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7947
namespace Case7947
def big : Finset (Finset (Fin 9)) := {{1,3,4,6},{0,2,5,6,7},{2,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{0,3},{0,4},{2,4},{1,5},{3,5},{4,5},{1,3,4,6},{1,7},{3,7},{0,2,5,6,7},{0,8},{1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
end Case7947
namespace Case7948
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{1,2},{3},{0,3},{0,4},{1,4},{2,3,4},{5},{1,5},{3,5},{4,5},{6},{4,6},{7},{1,7},{3,7},{0,2,5,6,7},{8},{0,8},{2,8},{5,8},{1,3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 4 else if T={4,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={3,7} then 1 else if T={0,2,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={1,3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],4⟩,⟨[15,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[14,18],1⟩,⟨[11,13,16,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,19],1⟩,⟨[16,19],1⟩,⟨[12,14,17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7948
namespace Case7948
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,2,5,6,7},{1,3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{0,3},{0,4},{1,4},{2,3,4},{1,5},{3,5},{4,5},{4,6},{1,7},{3,7},{0,2,5,6,7},{0,8},{2,8},{5,8},{1,3,6,8},{4,7,8}]
end Case7948
namespace Case7949
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{1,2},{3},{0,3},{2,3},{0,4},{1,4},{5},{1,5},{3,5},{4,5},{6},{4,6},{7},{1,7},{3,4,7},{0,2,5,6,7},{8},{0,8},{2,4,8},{5,8},{1,3,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 4 else if T={4,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={0,2,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={1,3,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[12],2⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],4⟩,⟨[14,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[13,14,17],1⟩,⟨[10,12,15,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[11,13,16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7949
namespace Case7949
def big : Finset (Finset (Fin 9)) := {{3,4,7},{0,2,5,6,7},{2,4,8},{1,3,6,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{0,3},{2,3},{0,4},{1,4},{1,5},{3,5},{4,5},{4,6},{1,7},{3,4,7},{0,2,5,6,7},{0,8},{2,4,8},{5,8},{1,3,6,8},{7,8}]
end Case7949
namespace Case7950
def positionFn : Fin 9 → Fin 25 := ![8,9,10,11,12,13,14,15,16]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{0,2},{3},{0,3},{0,4},{1,4},{5},{1,5},{2,5},{3,5},{4,5},{6},{1,2,3,6},{4,6},{7},{1,7},{3,7},{2,4,7},{8},{1,8},{2,8},{3,4,8},{0,5,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 4 else if T={1,2,3,6} then 1 else if T={4,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={8} then 3 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={0,5,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,16,17],[⟨[],1⟩,⟨[9],1⟩,⟨[9,10],1⟩,⟨[11],1⟩,⟨[9,11],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[14],2⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],4⟩,⟨[10,11,12,15],1⟩,⟨[13,15],1⟩,⟨[16],3⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[11,13,16],1⟩,⟨[17],3⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,13,17],1⟩,⟨[9,14,15,16,17],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7950
namespace Case7950
def big : Finset (Finset (Fin 9)) := {{1,2,3,6},{2,4,7},{3,4,8},{0,5,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{0,3},{0,4},{1,4},{1,5},{2,5},{3,5},{4,5},{1,2,3,6},{4,6},{1,7},{3,7},{2,4,7},{1,8},{2,8},{3,4,8},{0,5,6,7,8}]
end Case7950
namespace Case7951
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,4},{3,4},{5},{0,1,2,3,5},{4,5},{6},{0,6},{2,6},{3,6},{5,6},{7},{0,7},{2,7},{5,7},{1,4,6,7},{8},{0,8},{1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 3 else if T={2} then 2 else if T={3} then 2 else if T={4} then 1 else if T={0,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={0,1,2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={1,4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],3⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[10,11,12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[11,14,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7951
namespace Case7951
def big : Finset (Finset (Fin 9)) := {{0,1,2,3,5},{1,4,6,7},{2,4,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,4},{3,4},{0,1,2,3,5},{4,5},{0,6},{2,6},{3,6},{5,6},{0,7},{2,7},{5,7},{1,4,6,7},{0,8},{1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
end Case7951
namespace Case7952
def positionFn : Fin 9 → Fin 25 := ![8,9,10,11,12,13,14,15,16]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,4},{1,4},{5},{0,1,2,3,5},{4,5},{6},{0,6},{2,6},{3,6},{4,6},{5,6},{7},{0,7},{3,7},{2,4,7},{5,7},{8},{0,8},{2,8},{3,4,8},{5,8},{1,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 3 else if T={2} then 2 else if T={3} then 2 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={0,1,2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={1,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,16,17],[⟨[],1⟩,⟨[9],1⟩,⟨[10],3⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[9,13],1⟩,⟨[10,13],1⟩,⟨[14],2⟩,⟨[9,10,11,12,14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[9,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[9,16],1⟩,⟨[12,16],1⟩,⟨[11,13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[9,17],1⟩,⟨[11,17],1⟩,⟨[12,13,17],1⟩,⟨[14,17],1⟩,⟨[10,15,16,17],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7952
namespace Case7952
def big : Finset (Finset (Fin 9)) := {{0,1,2,3,5},{2,4,7},{3,4,8},{1,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,4},{1,4},{0,1,2,3,5},{4,5},{0,6},{2,6},{3,6},{4,6},{5,6},{0,7},{3,7},{2,4,7},{5,7},{0,8},{2,8},{3,4,8},{5,8},{1,6,7,8}]
end Case7952
namespace Case7953
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,3},{4},{0,4},{2,4},{5},{3,5},{4,5},{6},{0,6},{2,6},{1,3,4,6},{5,6},{7},{3,7},{0,1,2,5,7},{6,7},{8},{0,8},{1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 3 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={3,7} then 1 else if T={0,1,2,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],3⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[11,13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[13,17],1⟩,⟨[10,11,12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,13,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7953
namespace Case7953
def big : Finset (Finset (Fin 9)) := {{1,3,4,6},{0,1,2,5,7},{2,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{2,4},{3,5},{4,5},{0,6},{2,6},{1,3,4,6},{5,6},{3,7},{0,1,2,5,7},{6,7},{0,8},{1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
end Case7953
namespace Case7954
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,3},{0,4},{1,4},{2,3,4},{5},{3,5},{4,5},{6},{0,6},{2,6},{4,6},{5,6},{7},{3,7},{0,1,2,5,7},{6,7},{8},{0,8},{2,8},{5,8},{1,3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 3 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 2 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={3,7} then 1 else if T={0,1,2,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={1,3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[14,18],1⟩,⟨[11,12,13,16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,19],1⟩,⟨[16,19],1⟩,⟨[12,14,17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7954
namespace Case7954
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,1,2,5,7},{1,3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{1,4},{2,3,4},{3,5},{4,5},{0,6},{2,6},{4,6},{5,6},{3,7},{0,1,2,5,7},{6,7},{0,8},{2,8},{5,8},{1,3,6,8},{4,7,8}]
end Case7954
namespace Case7955
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,3},{2,3},{0,4},{1,4},{5},{3,5},{4,5},{6},{0,6},{2,6},{4,6},{5,6},{7},{3,4,7},{0,1,2,5,7},{6,7},{8},{0,8},{2,4,8},{5,8},{1,3,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 3 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={3,4,7} then 1 else if T={0,1,2,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={1,3,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[13,14],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],2⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[14,15,18],1⟩,⟨[11,12,13,16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,15,19],1⟩,⟨[16,19],1⟩,⟨[12,14,17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7955
namespace Case7955
def big : Finset (Finset (Fin 9)) := {{3,4,7},{0,1,2,5,7},{2,4,8},{1,3,6,8}}
def full : List (Finset (Fin 9)) := [{0,3},{2,3},{0,4},{1,4},{3,5},{4,5},{0,6},{2,6},{4,6},{5,6},{3,4,7},{0,1,2,5,7},{6,7},{0,8},{2,4,8},{5,8},{1,3,6,8},{7,8}]
end Case7955
namespace Case7956
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{3},{0,3},{0,4},{1,4},{5},{2,5},{3,5},{4,5},{6},{0,6},{1,2,3,6},{4,6},{5,6},{7},{3,7},{2,4,7},{6,7},{8},{2,8},{3,4,8},{6,8},{0,1,5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 3 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,2,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={6,8} then 1 else if T={0,1,5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],3⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[11,12,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[13,17],1⟩,⟨[12,14,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[13,14,18],1⟩,⟨[16,18],1⟩,⟨[10,11,15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7956
namespace Case7956
def big : Finset (Finset (Fin 9)) := {{1,2,3,6},{2,4,7},{3,4,8},{0,1,5,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{0,4},{1,4},{2,5},{3,5},{4,5},{0,6},{1,2,3,6},{4,6},{5,6},{3,7},{2,4,7},{6,7},{2,8},{3,4,8},{6,8},{0,1,5,7,8}]
end Case7956
namespace Case7957
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,3},{2,3},{4},{0,4},{1,4},{5},{3,5},{4,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{0,1,2,5,7},{3,4,6,7},{8},{0,8},{1,3,8},{2,4,8},{5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 4 else if T={0,1,2,5,7} then 1 else if T={3,4,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],2⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[16,17],1⟩,⟨[18],4⟩,⟨[11,12,13,16,18],1⟩,⟨[14,15,17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[12,14,19],1⟩,⟨[13,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7957
namespace Case7957
def big : Finset (Finset (Fin 9)) := {{0,1,2,5,7},{3,4,6,7},{1,3,8},{2,4,8}}
def full : List (Finset (Fin 9)) := [{0,3},{2,3},{0,4},{1,4},{3,5},{4,5},{0,6},{1,6},{2,6},{5,6},{0,1,2,5,7},{3,4,6,7},{0,8},{1,3,8},{2,4,8},{5,8},{6,8},{7,8}]
end Case7957
namespace Case7958
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,3},{2,3},{0,4},{1,3,4},{5},{3,5},{4,5},{6},{0,6},{1,6},{2,6},{4,6},{5,6},{7},{4,7},{0,1,2,5,7},{8},{0,8},{1,8},{2,4,8},{5,8},{3,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={5} then 2 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 4 else if T={4,7} then 1 else if T={0,1,2,5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={3,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[10,14],1⟩,⟨[11,13,14],1⟩,⟨[15],2⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],4⟩,⟨[14,17],1⟩,⟨[10,11,12,15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[13,16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7958
namespace Case7958
def big : Finset (Finset (Fin 9)) := {{1,3,4},{0,1,2,5,7},{2,4,8},{3,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{2,3},{0,4},{1,3,4},{3,5},{4,5},{0,6},{1,6},{2,6},{4,6},{5,6},{4,7},{0,1,2,5,7},{0,8},{1,8},{2,4,8},{5,8},{3,6,7,8}]
end Case7958
namespace Case7959
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{3},{0,3},{1,3},{0,4},{1,2,4},{5},{2,5},{3,5},{4,5},{6},{0,6},{1,6},{4,6},{5,6},{7},{4,7},{2,3,6,7},{8},{2,8},{3,4,8},{6,8},{0,1,5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 2 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 4 else if T={4,7} then 1 else if T={2,3,6,7} then 1 else if T={8} then 3 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={6,8} then 1 else if T={0,1,5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[11,15],1⟩,⟨[12,13,15],1⟩,⟨[16],2⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],4⟩,⟨[15,18],1⟩,⟨[13,14,17,18],1⟩,⟨[19],3⟩,⟨[13,19],1⟩,⟨[14,15,19],1⟩,⟨[17,19],1⟩,⟨[11,12,16,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7959
namespace Case7959
def big : Finset (Finset (Fin 9)) := {{1,2,4},{2,3,6,7},{3,4,8},{0,1,5,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{1,3},{0,4},{1,2,4},{2,5},{3,5},{4,5},{0,6},{1,6},{4,6},{5,6},{4,7},{2,3,6,7},{2,8},{3,4,8},{6,8},{0,1,5,7,8}]
end Case7959
namespace Case7960
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,3},{4},{3,4},{5},{0,5},{4,5},{6},{0,6},{4,6},{1,2,3,5,6},{7},{2,7},{0,1,4,7},{5,7},{6,7},{8},{0,8},{1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 3 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={4,6} then 1 else if T={1,2,3,5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={0,1,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],3⟩,⟨[12],2⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[14,16],1⟩,⟨[11,12,13,15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[10,11,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7960
namespace Case7960
def big : Finset (Finset (Fin 9)) := {{1,2,3,5,6},{0,1,4,7},{2,4,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{3,4},{0,5},{4,5},{0,6},{4,6},{1,2,3,5,6},{2,7},{0,1,4,7},{5,7},{6,7},{0,8},{1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
end Case7960
namespace Case7961
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,3},{0,4},{1,4},{5},{0,5},{4,5},{6},{0,6},{4,6},{1,2,3,5,6},{7},{3,7},{2,4,7},{5,7},{6,7},{8},{2,8},{3,4,8},{5,8},{6,8},{0,1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 3 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={4,6} then 1 else if T={1,2,3,5,6} then 1 else if T={7} then 2 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={0,1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[15,17],1⟩,⟨[12,13,14,16,17],1⟩,⟨[18],2⟩,⟨[14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[13,19],1⟩,⟨[14,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[11,12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7961
namespace Case7961
def big : Finset (Finset (Fin 9)) := {{1,2,3,5,6},{2,4,7},{3,4,8},{0,1,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{0,4},{1,4},{0,5},{4,5},{0,6},{4,6},{1,2,3,5,6},{3,7},{2,4,7},{5,7},{6,7},{2,8},{3,4,8},{5,8},{6,8},{0,1,7,8}]
end Case7961
namespace Case7962
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{4},{2,4},{0,1,3,4},{5},{0,5},{3,5},{4,5},{6},{0,6},{3,6},{4,6},{7},{0,7},{3,7},{1,2,5,6,7},{8},{0,8},{1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 3 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={0,1,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={3,7} then 1 else if T={1,2,5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[15],1⟩,⟨[13,15],1⟩,⟨[11,12,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[18],3⟩,⟨[11,18],1⟩,⟨[14,18],1⟩,⟨[12,13,16,17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,14,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7962
namespace Case7962
def big : Finset (Finset (Fin 9)) := {{0,1,3,4},{1,2,5,6,7},{2,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{2,4},{0,1,3,4},{0,5},{3,5},{4,5},{0,6},{3,6},{4,6},{0,7},{3,7},{1,2,5,6,7},{0,8},{1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
end Case7962
namespace Case7963
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,4},{1,4},{2,3,4},{5},{0,5},{3,5},{4,5},{6},{0,6},{3,6},{4,6},{7},{0,7},{3,7},{1,2,5,6,7},{8},{2,8},{0,1,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 3 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={3,7} then 1 else if T={1,2,5,6,7} then 1 else if T={8} then 2 else if T={2,8} then 1 else if T={0,1,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[18],3⟩,⟨[11,18],1⟩,⟨[14,18],1⟩,⟨[12,13,16,17,18],1⟩,⟨[19],2⟩,⟨[13,19],1⟩,⟨[11,12,14,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7963
namespace Case7963
def big : Finset (Finset (Fin 9)) := {{2,3,4},{1,2,5,6,7},{0,1,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,4},{1,4},{2,3,4},{0,5},{3,5},{4,5},{0,6},{3,6},{4,6},{0,7},{3,7},{1,2,5,6,7},{2,8},{0,1,3,8},{5,8},{6,8},{4,7,8}]
end Case7963
namespace Case7964
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{2,3},{0,4},{1,4},{5},{0,5},{3,5},{4,5},{6},{0,6},{3,6},{4,6},{7},{0,7},{3,4,7},{1,2,5,6,7},{8},{0,1,3,8},{2,4,8},{5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 3 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={1,2,5,6,7} then 1 else if T={8} then 2 else if T={0,1,3,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],3⟩,⟨[12],2⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],3⟩,⟨[10,17],1⟩,⟨[13,14,17],1⟩,⟨[11,12,15,16,17],1⟩,⟨[18],2⟩,⟨[10,11,13,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7964
namespace Case7964
def big : Finset (Finset (Fin 9)) := {{3,4,7},{1,2,5,6,7},{0,1,3,8},{2,4,8}}
def full : List (Finset (Fin 9)) := [{0,2},{2,3},{0,4},{1,4},{0,5},{3,5},{4,5},{0,6},{3,6},{4,6},{0,7},{3,4,7},{1,2,5,6,7},{0,1,3,8},{2,4,8},{5,8},{6,8},{7,8}]
end Case7964
namespace Case7965
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,1,2,3},{0,4},{1,4},{5},{0,5},{2,5},{3,5},{4,5},{6},{0,6},{2,6},{3,6},{4,6},{7},{0,7},{3,7},{2,4,7},{8},{0,8},{2,8},{3,4,8},{1,5,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 3 else if T={2} then 1 else if T={3} then 1 else if T={0,1,2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={1,5,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],3⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[10,11,12,13],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],3⟩,⟨[10,17],1⟩,⟨[13,17],1⟩,⟨[12,14,17],1⟩,⟨[18],3⟩,⟨[10,18],1⟩,⟨[12,18],1⟩,⟨[13,14,18],1⟩,⟨[11,15,16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7965
namespace Case7965
def big : Finset (Finset (Fin 9)) := {{0,1,2,3},{2,4,7},{3,4,8},{1,5,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2,3},{0,4},{1,4},{0,5},{2,5},{3,5},{4,5},{0,6},{2,6},{3,6},{4,6},{0,7},{3,7},{2,4,7},{0,8},{2,8},{3,4,8},{1,5,6,7,8}]
end Case7965
namespace Case7966
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{3},{2,3},{4},{1,4},{5},{0,5},{3,5},{4,5},{6},{0,6},{3,6},{4,6},{7},{0,3,4,7},{1,2,5,6,7},{8},{0,8},{1,3,8},{2,4,8},{5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={7} then 4 else if T={0,3,4,7} then 1 else if T={1,2,5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],2⟩,⟨[10,11],1⟩,⟨[12],2⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],4⟩,⟨[10,13,14,17],1⟩,⟨[11,12,15,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,13,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7966
namespace Case7966
def big : Finset (Finset (Fin 9)) := {{0,3,4,7},{1,2,5,6,7},{1,3,8},{2,4,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{2,3},{1,4},{0,5},{3,5},{4,5},{0,6},{3,6},{4,6},{0,3,4,7},{1,2,5,6,7},{0,8},{1,3,8},{2,4,8},{5,8},{6,8},{7,8}]
end Case7966
namespace Case7967
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{3},{2,3},{0,4},{1,3,4},{5},{0,5},{3,5},{4,5},{6},{0,6},{3,6},{4,6},{7},{4,7},{1,2,5,6,7},{8},{1,8},{2,4,8},{5,8},{6,8},{0,3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={7} then 4 else if T={4,7} then 1 else if T={1,2,5,6,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={0,3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],2⟩,⟨[10,11],1⟩,⟨[12],2⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[10,14],1⟩,⟨[11,13,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],4⟩,⟨[14,17],1⟩,⟨[11,12,15,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[10,13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7967
namespace Case7967
def big : Finset (Finset (Fin 9)) := {{1,3,4},{1,2,5,6,7},{2,4,8},{0,3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{2,3},{0,4},{1,3,4},{0,5},{3,5},{4,5},{0,6},{3,6},{4,6},{4,7},{1,2,5,6,7},{1,8},{2,4,8},{5,8},{6,8},{0,3,7,8}]
end Case7967
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

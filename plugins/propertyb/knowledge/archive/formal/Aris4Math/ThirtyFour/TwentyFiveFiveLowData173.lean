import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case4152
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{2,5},{3,5},{4,5},{6},{0,1,2,6},{3,6},{5,6},{7},{1,7},{0,3,7},{5,7},{4,6,7},{8},{0,8},{3,4,8},{1,5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={3,4,8} then 1 else if T={1,5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,11,12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[10,13,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[13,14,18],1⟩,⟨[11,15,18],1⟩,⟨[16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4152
namespace Case4152
def big : Finset (Finset (Fin 9)) := {{0,1,2,6},{0,3,7},{4,6,7},{3,4,8},{1,5,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{2,5},{3,5},{4,5},{0,1,2,6},{3,6},{5,6},{1,7},{0,3,7},{5,7},{4,6,7},{0,8},{3,4,8},{1,5,8},{6,8},{2,7,8}]
end Case4152
namespace Case4153
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,3},{2,3},{4},{0,4},{0,5},{2,5},{3,5},{1,4,5},{6},{0,1,2,6},{3,6},{4,6},{5,6},{7},{0,7},{1,7},{2,7},{3,4,7},{5,7},{8},{1,8},{0,3,8},{2,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={1,4,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={0,3,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[11,14,15],1⟩,⟨[16],2⟩,⟨[10,11,12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[10,13,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4153
namespace Case4153
def big : Finset (Finset (Fin 9)) := {{1,4,5},{0,1,2,6},{3,4,7},{0,3,8},{2,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{2,3},{0,4},{0,5},{2,5},{3,5},{1,4,5},{0,1,2,6},{3,6},{4,6},{5,6},{0,7},{1,7},{2,7},{3,4,7},{5,7},{1,8},{0,3,8},{2,4,8},{5,8},{6,7,8}]
end Case4153
namespace Case4154
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,3},{2,3},{4},{2,4},{0,3,4},{0,5},{1,5},{3,5},{4,5},{6},{0,1,2,6},{3,6},{5,6},{7},{0,7},{1,7},{2,7},{5,7},{4,6,7},{8},{0,8},{1,4,8},{2,5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={2,5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[10,13,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,11,12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,14,18],1⟩,⟨[12,15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4154
namespace Case4154
def big : Finset (Finset (Fin 9)) := {{0,3,4},{0,1,2,6},{4,6,7},{1,4,8},{2,5,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{2,3},{2,4},{0,3,4},{0,5},{1,5},{3,5},{4,5},{0,1,2,6},{3,6},{5,6},{0,7},{1,7},{2,7},{5,7},{4,6,7},{0,8},{1,4,8},{2,5,8},{6,8},{3,7,8}]
end Case4154
namespace Case4155
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,3},{1,3},{2,3},{4},{2,4},{1,5},{2,5},{3,5},{0,4,5},{6},{0,1,2,6},{4,6},{5,6},{7},{0,7},{1,7},{3,4,7},{5,7},{6,7},{8},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[10,14,15],1⟩,⟨[16],2⟩,⟨[10,11,12,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[13,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4155
namespace Case4155
def big : Finset (Finset (Fin 9)) := {{0,4,5},{0,1,2,6},{3,4,7},{1,4,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{2,3},{2,4},{1,5},{2,5},{3,5},{0,4,5},{0,1,2,6},{4,6},{5,6},{0,7},{1,7},{3,4,7},{5,7},{6,7},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]
end Case4155
namespace Case4156
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,3},{1,3},{2,3},{4},{2,4},{0,5},{1,5},{3,5},{4,5},{6},{0,1,2,6},{3,4,6},{5,6},{7},{1,7},{2,7},{0,4,7},{5,7},{6,7},{8},{0,8},{1,4,8},{2,5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={0,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={2,5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,11,12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[10,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,14,18],1⟩,⟨[12,15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4156
namespace Case4156
def big : Finset (Finset (Fin 9)) := {{0,1,2,6},{3,4,6},{0,4,7},{1,4,8},{2,5,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{2,3},{2,4},{0,5},{1,5},{3,5},{4,5},{0,1,2,6},{3,4,6},{5,6},{1,7},{2,7},{0,4,7},{5,7},{6,7},{0,8},{1,4,8},{2,5,8},{6,8},{3,7,8}]
end Case4156
namespace Case4157
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{2,3},{4},{1,4},{0,3,4},{0,5},{2,5},{1,3,5},{4,5},{6},{0,1,2,6},{3,6},{5,6},{7},{0,7},{1,7},{2,4,7},{5,7},{6,7},{8},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={1,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[10,13,14],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[11,13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,11,12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4157
namespace Case4157
def big : Finset (Finset (Fin 9)) := {{0,3,4},{1,3,5},{0,1,2,6},{2,4,7},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{2,3},{1,4},{0,3,4},{0,5},{2,5},{1,3,5},{4,5},{0,1,2,6},{3,6},{5,6},{0,7},{1,7},{2,4,7},{5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]
end Case4157
namespace Case4158
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{1,3},{4},{0,4},{2,3,4},{0,5},{2,5},{3,5},{1,4,5},{6},{2,6},{4,6},{5,6},{7},{2,7},{3,7},{5,7},{0,1,6,7},{8},{1,8},{0,2,8},{5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,3,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={1,4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={0,2,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[13,14,15],1⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[12,15,16],1⟩,⟨[17],2⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[13,18],1⟩,⟨[14,18],1⟩,⟨[16,18],1⟩,⟨[11,12,17,18],1⟩,⟨[19],2⟩,⟨[12,19],1⟩,⟨[11,13,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4158
namespace Case4158
def big : Finset (Finset (Fin 9)) := {{2,3,4},{1,4,5},{0,1,6,7},{0,2,8},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{0,4},{2,3,4},{0,5},{2,5},{3,5},{1,4,5},{2,6},{4,6},{5,6},{2,7},{3,7},{5,7},{0,1,6,7},{1,8},{0,2,8},{5,8},{3,6,8},{4,7,8}]
end Case4158
namespace Case4159
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{1,3},{4},{1,4},{0,2,4},{0,5},{2,5},{3,5},{4,5},{6},{2,6},{3,4,6},{5,6},{7},{2,7},{3,7},{5,7},{0,1,6,7},{8},{0,8},{2,3,8},{1,5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,2,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[11,13,15],1⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[13,17],1⟩,⟨[14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[13,18],1⟩,⟨[14,18],1⟩,⟨[16,18],1⟩,⟨[11,12,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,14,19],1⟩,⟨[12,16,19],1⟩,⟨[17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4159
namespace Case4159
def big : Finset (Finset (Fin 9)) := {{0,2,4},{3,4,6},{0,1,6,7},{2,3,8},{1,5,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{1,4},{0,2,4},{0,5},{2,5},{3,5},{4,5},{2,6},{3,4,6},{5,6},{2,7},{3,7},{5,7},{0,1,6,7},{0,8},{2,3,8},{1,5,8},{6,8},{4,7,8}]
end Case4159
namespace Case4160
def positionFn : Fin 9 → Fin 25 := ![20,10,12,13,11,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{1,3},{0,2,3},{4},{0,4},{0,5},{2,5},{3,5},{1,4,5},{6},{2,6},{3,4,6},{5,6},{7},{2,7},{4,7},{5,7},{0,1,6,7},{8},{0,8},{1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={1,4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,21,22,23,24,25],[⟨[],4⟩,⟨[21],1⟩,⟨[11],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[13,14,21],1⟩,⟨[12],1⟩,⟨[12,21],1⟩,⟨[21,22],1⟩,⟨[13,22],1⟩,⟨[14,22],1⟩,⟨[11,12,22],1⟩,⟨[23],2⟩,⟨[13,23],1⟩,⟨[12,14,23],1⟩,⟨[22,23],1⟩,⟨[24],2⟩,⟨[13,24],1⟩,⟨[12,24],1⟩,⟨[22,24],1⟩,⟨[11,21,23,24],1⟩,⟨[25],1⟩,⟨[21,25],1⟩,⟨[11,25],1⟩,⟨[12,13,25],1⟩,⟨[22,25],1⟩,⟨[23,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4160
namespace Case4160
def big : Finset (Finset (Fin 9)) := {{0,2,3},{1,4,5},{3,4,6},{0,1,6,7},{2,4,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{1,3},{0,2,3},{0,4},{0,5},{2,5},{3,5},{1,4,5},{2,6},{3,4,6},{5,6},{2,7},{4,7},{5,7},{0,1,6,7},{0,8},{1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
end Case4160
namespace Case4161
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{3},{1,3},{4},{0,4},{1,5},{2,5},{0,3,5},{4,5},{6},{3,6},{2,4,6},{5,6},{7},{2,7},{3,4,7},{5,7},{0,1,6,7},{8},{0,8},{2,3,8},{1,4,8},{5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={0,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[11,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[14,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[11,12,17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[13,14,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4161
namespace Case4161
def big : Finset (Finset (Fin 9)) := {{0,3,5},{2,4,6},{3,4,7},{0,1,6,7},{2,3,8},{1,4,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{0,4},{1,5},{2,5},{0,3,5},{4,5},{3,6},{2,4,6},{5,6},{2,7},{3,4,7},{5,7},{0,1,6,7},{0,8},{2,3,8},{1,4,8},{5,8},{6,8},{7,8}]
end Case4161
namespace Case4162
def positionFn : Fin 9 → Fin 25 := ![10,21,12,14,11,22,23,24,13]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{0,3},{1,3},{4},{2,3,4},{1,5},{2,5},{3,5},{0,4,5},{6},{3,6},{4,6},{5,6},{7},{2,7},{4,7},{5,7},{0,1,6,7},{8},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={2,3,4} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,22,23,24,25],[⟨[],4⟩,⟨[11],1⟩,⟨[22],1⟩,⟨[11,13],1⟩,⟨[13,22],1⟩,⟨[11,15],1⟩,⟨[15,22],1⟩,⟨[12],1⟩,⟨[12,13,15],1⟩,⟨[22,23],1⟩,⟨[13,23],1⟩,⟨[15,23],1⟩,⟨[11,12,23],1⟩,⟨[24],2⟩,⟨[15,24],1⟩,⟨[12,24],1⟩,⟨[23,24],1⟩,⟨[25],2⟩,⟨[13,25],1⟩,⟨[12,25],1⟩,⟨[23,25],1⟩,⟨[11,22,24,25],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[12,14,22],1⟩,⟨[14,23],1⟩,⟨[13,14,24],1⟩,⟨[14,15,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4162
namespace Case4162
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,4,5},{0,1,6,7},{1,4,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{2,3,4},{1,5},{2,5},{3,5},{0,4,5},{3,6},{4,6},{5,6},{2,7},{4,7},{5,7},{0,1,6,7},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
end Case4162
namespace Case4163
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{0,3},{1,3},{4},{1,4},{0,5},{2,5},{3,5},{4,5},{6},{3,6},{2,4,6},{5,6},{7},{2,7},{3,4,7},{5,7},{0,1,6,7},{8},{2,3,8},{0,4,8},{1,5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={2,3,8} then 1 else if T={0,4,8} then 1 else if T={1,5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[14,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[11,12,17,18],1⟩,⟨[19],2⟩,⟨[13,14,19],1⟩,⟨[11,15,19],1⟩,⟨[12,16,19],1⟩,⟨[17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4163
namespace Case4163
def big : Finset (Finset (Fin 9)) := {{2,4,6},{3,4,7},{0,1,6,7},{2,3,8},{0,4,8},{1,5,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{1,4},{0,5},{2,5},{3,5},{4,5},{3,6},{2,4,6},{5,6},{2,7},{3,4,7},{5,7},{0,1,6,7},{2,3,8},{0,4,8},{1,5,8},{6,8},{7,8}]
end Case4163
namespace Case4164
def positionFn : Fin 9 → Fin 25 := ![20,10,12,11,13,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{3},{4},{1,4},{0,3,4},{0,5},{2,5},{1,3,5},{4,5},{6},{3,6},{2,4,6},{5,6},{7},{2,7},{3,7},{5,7},{0,1,6,7},{8},{0,8},{1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={1,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,21,22,23,24,25],[⟨[],4⟩,⟨[21],1⟩,⟨[11],1⟩,⟨[13,21],1⟩,⟨[11,13],1⟩,⟨[12],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,14,21],1⟩,⟨[21,22],1⟩,⟨[13,22],1⟩,⟨[11,12,22],1⟩,⟨[14,22],1⟩,⟨[23],2⟩,⟨[12,23],1⟩,⟨[13,14,23],1⟩,⟨[22,23],1⟩,⟨[24],2⟩,⟨[13,24],1⟩,⟨[12,24],1⟩,⟨[22,24],1⟩,⟨[11,21,23,24],1⟩,⟨[25],1⟩,⟨[21,25],1⟩,⟨[11,25],1⟩,⟨[12,13,25],1⟩,⟨[22,25],1⟩,⟨[23,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4164
namespace Case4164
def big : Finset (Finset (Fin 9)) := {{0,3,4},{1,3,5},{2,4,6},{0,1,6,7},{2,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,4},{0,3,4},{0,5},{2,5},{1,3,5},{4,5},{3,6},{2,4,6},{5,6},{2,7},{3,7},{5,7},{0,1,6,7},{0,8},{1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
end Case4164
namespace Case4165
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{0,2},{3},{1,2,3},{4},{0,4},{1,5},{2,5},{0,3,5},{4,5},{6},{2,6},{3,6},{1,4,6},{5,6},{7},{1,7},{3,7},{2,4,7},{5,7},{8},{1,8},{2,8},{3,4,8},{5,8},{0,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={0,1} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={0,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={0,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[10,13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[11,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[10,16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4165
namespace Case4165
def big : Finset (Finset (Fin 9)) := {{1,2,3},{0,3,5},{1,4,6},{2,4,7},{3,4,8},{0,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{1,2,3},{0,4},{1,5},{2,5},{0,3,5},{4,5},{2,6},{3,6},{1,4,6},{5,6},{1,7},{3,7},{2,4,7},{5,7},{1,8},{2,8},{3,4,8},{5,8},{0,6,7,8}]
end Case4165
namespace Case4166
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{2,5},{3,5},{4,5},{6},{0,1,2,6},{3,6},{4,6},{7},{0,3,7},{1,4,7},{5,7},{6,7},{8},{0,8},{1,8},{3,4,8},{5,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={7} then 2 else if T={0,3,7} then 1 else if T={1,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,4,8} then 1 else if T={5,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,11,12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[10,13,17],1⟩,⟨[11,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[13,14,18],1⟩,⟨[15,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4166
namespace Case4166
def big : Finset (Finset (Fin 9)) := {{0,1,2,6},{0,3,7},{1,4,7},{3,4,8},{5,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{2,5},{3,5},{4,5},{0,1,2,6},{3,6},{4,6},{0,3,7},{1,4,7},{5,7},{6,7},{0,8},{1,8},{3,4,8},{5,6,8},{2,7,8}]
end Case4166
namespace Case4167
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,3},{2,3},{4},{0,4},{2,4},{0,5},{1,5},{2,5},{3,5},{6},{0,1,2,6},{3,6},{4,5,6},{7},{0,7},{1,7},{3,4,7},{5,7},{6,7},{8},{0,3,8},{1,4,8},{5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[10,11,12,16],1⟩,⟨[13,16],1⟩,⟨[14,15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,13,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4167
namespace Case4167
def big : Finset (Finset (Fin 9)) := {{0,1,2,6},{4,5,6},{3,4,7},{0,3,8},{1,4,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{2,5},{3,5},{0,1,2,6},{3,6},{4,5,6},{0,7},{1,7},{3,4,7},{5,7},{6,7},{0,3,8},{1,4,8},{5,8},{6,8},{2,7,8}]
end Case4167
namespace Case4168
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,3},{2,3},{4},{0,3,4},{0,5},{1,5},{2,5},{3,5},{4,5},{6},{0,1,2,6},{3,6},{4,6},{7},{0,7},{2,7},{1,4,7},{5,7},{6,7},{8},{0,8},{1,8},{2,4,8},{5,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={5,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,13,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,11,12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[11,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[15,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4168
namespace Case4168
def big : Finset (Finset (Fin 9)) := {{0,3,4},{0,1,2,6},{1,4,7},{2,4,8},{5,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{2,3},{0,3,4},{0,5},{1,5},{2,5},{3,5},{4,5},{0,1,2,6},{3,6},{4,6},{0,7},{2,7},{1,4,7},{5,7},{6,7},{0,8},{1,8},{2,4,8},{5,6,8},{3,7,8}]
end Case4168
namespace Case4169
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{1,4},{2,4},{0,3,4},{0,5},{1,5},{2,5},{3,5},{6},{0,1,2,6},{3,6},{4,5,6},{7},{0,7},{2,7},{1,3,7},{5,7},{6,7},{8},{0,8},{1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[11,14,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[11,12,13,17],1⟩,⟨[14,17],1⟩,⟨[15,16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[13,18],1⟩,⟨[12,14,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,14,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4169
namespace Case4169
def big : Finset (Finset (Fin 9)) := {{0,3,4},{0,1,2,6},{4,5,6},{1,3,7},{2,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{1,4},{2,4},{0,3,4},{0,5},{1,5},{2,5},{3,5},{0,1,2,6},{3,6},{4,5,6},{0,7},{2,7},{1,3,7},{5,7},{6,7},{0,8},{1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
end Case4169
namespace Case4170
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{4},{0,4},{1,4},{2,3,4},{0,5},{1,5},{2,5},{3,5},{6},{2,6},{3,6},{4,5,6},{7},{2,7},{3,7},{5,7},{0,1,6,7},{8},{0,2,8},{1,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={0,2,8} then 1 else if T={1,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[15,16,17],1⟩,⟨[18],2⟩,⟨[13,18],1⟩,⟨[14,18],1⟩,⟨[16,18],1⟩,⟨[11,12,17,18],1⟩,⟨[19],2⟩,⟨[11,13,19],1⟩,⟨[12,14,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4170
namespace Case4170
def big : Finset (Finset (Fin 9)) := {{2,3,4},{4,5,6},{0,1,6,7},{0,2,8},{1,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,4},{1,4},{2,3,4},{0,5},{1,5},{2,5},{3,5},{2,6},{3,6},{4,5,6},{2,7},{3,7},{5,7},{0,1,6,7},{0,2,8},{1,3,8},{5,8},{6,8},{4,7,8}]
end Case4170
namespace Case4171
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{4},{0,2,4},{1,3,4},{0,5},{1,5},{2,5},{3,5},{4,5},{6},{2,6},{3,6},{5,6},{7},{2,7},{3,7},{4,7},{0,1,6,7},{8},{0,8},{1,8},{2,3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,2,4} then 1 else if T={1,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={3,7} then 1 else if T={4,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,13,15],1⟩,⟨[12,14,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[13,18],1⟩,⟨[14,18],1⟩,⟨[15,18],1⟩,⟨[11,12,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,14,19],1⟩,⟨[15,17,19],1⟩,⟨[16,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4171
namespace Case4171
def big : Finset (Finset (Fin 9)) := {{0,2,4},{1,3,4},{0,1,6,7},{2,3,8},{4,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,2,4},{1,3,4},{0,5},{1,5},{2,5},{3,5},{4,5},{2,6},{3,6},{5,6},{2,7},{3,7},{4,7},{0,1,6,7},{0,8},{1,8},{2,3,8},{4,6,8},{5,7,8}]
end Case4171
namespace Case4172
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{0,2,3},{4},{0,4},{1,4},{0,5},{1,5},{2,5},{3,5},{6},{2,6},{3,4,6},{5,6},{7},{2,7},{3,7},{4,5,7},{0,1,6,7},{8},{0,8},{1,3,8},{2,4,8},{5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={3,7} then 1 else if T={4,5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[14,15,17],1⟩,⟨[10,11,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,13,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4172
namespace Case4172
def big : Finset (Finset (Fin 9)) := {{0,2,3},{3,4,6},{4,5,7},{0,1,6,7},{1,3,8},{2,4,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,2,3},{0,4},{1,4},{0,5},{1,5},{2,5},{3,5},{2,6},{3,4,6},{5,6},{2,7},{3,7},{4,5,7},{0,1,6,7},{0,8},{1,3,8},{2,4,8},{5,8},{6,8},{7,8}]
end Case4172
namespace Case4173
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{1,3},{4},{0,4},{2,3,4},{0,5},{1,5},{2,5},{3,5},{6},{2,6},{4,6},{5,6},{7},{2,7},{3,7},{4,5,7},{0,1,6,7},{8},{0,2,8},{1,4,8},{5,8},{3,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={3,7} then 1 else if T={4,5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={0,2,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[13,14,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[13,18],1⟩,⟨[14,18],1⟩,⟨[15,16,18],1⟩,⟨[11,12,17,18],1⟩,⟨[19],2⟩,⟨[11,13,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4173
namespace Case4173
def big : Finset (Finset (Fin 9)) := {{2,3,4},{4,5,7},{0,1,6,7},{0,2,8},{1,4,8},{3,6,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{0,4},{2,3,4},{0,5},{1,5},{2,5},{3,5},{2,6},{4,6},{5,6},{2,7},{3,7},{4,5,7},{0,1,6,7},{0,2,8},{1,4,8},{5,8},{3,6,8},{7,8}]
end Case4173
namespace Case4174
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{1,3},{4},{0,2,4},{0,5},{1,5},{2,5},{3,5},{4,5},{6},{2,6},{3,4,6},{5,6},{7},{2,7},{3,7},{4,7},{0,1,6,7},{8},{0,8},{2,3,8},{1,4,8},{6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={3,7} then 1 else if T={4,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,13,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[13,17],1⟩,⟨[14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[13,18],1⟩,⟨[14,18],1⟩,⟨[15,18],1⟩,⟨[11,12,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,14,19],1⟩,⟨[12,15,19],1⟩,⟨[17,19],1⟩,⟨[16,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4174
namespace Case4174
def big : Finset (Finset (Fin 9)) := {{0,2,4},{3,4,6},{0,1,6,7},{2,3,8},{1,4,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{0,2,4},{0,5},{1,5},{2,5},{3,5},{4,5},{2,6},{3,4,6},{5,6},{2,7},{3,7},{4,7},{0,1,6,7},{0,8},{2,3,8},{1,4,8},{6,8},{5,7,8}]
end Case4174
namespace Case4175
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{0,2,3},{4},{0,4},{1,3,4},{0,5},{1,5},{2,5},{3,5},{6},{2,6},{3,6},{4,5,6},{7},{2,7},{4,7},{5,7},{0,1,6,7},{8},{0,8},{1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,14,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[15,16,17],1⟩,⟨[18],2⟩,⟨[13,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[11,12,17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4175
namespace Case4175
def big : Finset (Finset (Fin 9)) := {{0,2,3},{1,3,4},{4,5,6},{0,1,6,7},{2,4,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,2,3},{0,4},{1,3,4},{0,5},{1,5},{2,5},{3,5},{2,6},{3,6},{4,5,6},{2,7},{4,7},{5,7},{0,1,6,7},{0,8},{1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
end Case4175
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

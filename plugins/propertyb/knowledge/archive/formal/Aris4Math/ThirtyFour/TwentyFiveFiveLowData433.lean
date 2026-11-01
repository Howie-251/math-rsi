import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case10392
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{4},{0,2,4},{0,5},{1,5},{2,3,5},{4,5},{6},{2,6},{0,1,3,6},{4,6},{5,6},{7},{0,7},{2,7},{3,7},{1,4,7},{5,7},{8},{0,8},{1,8},{2,8},{3,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={0,2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,1,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={1,4,7} then 1 else if T={5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[10,12,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[10,11,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[11,14,17],1⟩,⟨[15,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10392
namespace Case10392
def big : Finset (Finset (Fin 9)) := {{0,2,4},{2,3,5},{0,1,3,6},{1,4,7},{3,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,2,4},{0,5},{1,5},{2,3,5},{4,5},{2,6},{0,1,3,6},{4,6},{5,6},{0,7},{2,7},{3,7},{1,4,7},{5,7},{0,8},{1,8},{2,8},{3,4,8},{5,8},{6,7,8}]
end Case10392
namespace Case10393
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{1,3},{4},{2,4},{0,5},{1,5},{2,5},{3,5},{6},{2,3,6},{0,1,4,6},{5,6},{7},{0,7},{2,7},{3,7},{4,5,7},{6,7},{8},{0,2,8},{3,4,8},{5,8},{6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={2,3,6} then 1 else if T={0,1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,2,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[12,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[12,13,16],1⟩,⟨[10,11,14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,12,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10393
namespace Case10393
def big : Finset (Finset (Fin 9)) := {{2,3,6},{0,1,4,6},{4,5,7},{0,2,8},{3,4,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{2,4},{0,5},{1,5},{2,5},{3,5},{2,3,6},{0,1,4,6},{5,6},{0,7},{2,7},{3,7},{4,5,7},{6,7},{0,2,8},{3,4,8},{5,8},{6,8},{1,7,8}]
end Case10393
namespace Case10394
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{1,3},{4},{0,2,4},{0,5},{1,5},{2,5},{3,5},{4,5},{6},{2,3,6},{4,6},{5,6},{7},{0,7},{2,7},{3,7},{1,4,7},{6,7},{8},{2,8},{3,4,8},{0,1,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={2,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={1,4,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={0,1,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,13,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[13,18],1⟩,⟨[14,18],1⟩,⟨[12,15,18],1⟩,⟨[17,18],1⟩,⟨[19],3⟩,⟨[13,19],1⟩,⟨[14,15,19],1⟩,⟨[11,12,17,19],1⟩,⟨[16,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10394
namespace Case10394
def big : Finset (Finset (Fin 9)) := {{0,2,4},{2,3,6},{1,4,7},{3,4,8},{0,1,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{0,2,4},{0,5},{1,5},{2,5},{3,5},{4,5},{2,3,6},{4,6},{5,6},{0,7},{2,7},{3,7},{1,4,7},{6,7},{2,8},{3,4,8},{0,1,6,8},{5,7,8}]
end Case10394
namespace Case10395
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{2,3},{4},{0,2,4},{0,5},{1,5},{2,5},{4,5},{6},{0,1,3,6},{4,6},{5,6},{7},{0,7},{2,7},{1,4,7},{3,5,7},{6,7},{8},{0,8},{1,8},{3,4,8},{5,8},{2,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,1,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={3,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,12,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,11,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[11,14,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[12,16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10395
namespace Case10395
def big : Finset (Finset (Fin 9)) := {{0,2,4},{0,1,3,6},{1,4,7},{3,5,7},{3,4,8},{2,6,8}}
def full : List (Finset (Fin 9)) := [{1,2},{2,3},{0,2,4},{0,5},{1,5},{2,5},{4,5},{0,1,3,6},{4,6},{5,6},{0,7},{2,7},{1,4,7},{3,5,7},{6,7},{0,8},{1,8},{3,4,8},{5,8},{2,6,8},{7,8}]
end Case10395
namespace Case10396
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{3},{4},{2,3,4},{0,5},{1,5},{2,5},{4,5},{6},{0,1,3,6},{4,6},{5,6},{7},{1,7},{3,7},{0,4,7},{5,7},{2,6,7},{8},{0,8},{2,8},{1,4,8},{3,5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={2,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,1,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={0,4,7} then 1 else if T={5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,4,8} then 1 else if T={3,5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[12,13,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,11,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[10,14,17],1⟩,⟨[15,17],1⟩,⟨[12,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[12,18],1⟩,⟨[11,14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10396
namespace Case10396
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,1,3,6},{0,4,7},{2,6,7},{1,4,8},{3,5,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{2,3,4},{0,5},{1,5},{2,5},{4,5},{0,1,3,6},{4,6},{5,6},{1,7},{3,7},{0,4,7},{5,7},{2,6,7},{0,8},{2,8},{1,4,8},{3,5,8},{6,8},{7,8}]
end Case10396
namespace Case10397
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{0,3},{1,3},{4},{3,4},{0,5},{2,5},{3,5},{1,4,5},{6},{1,6},{2,3,6},{5,6},{7},{1,7},{2,7},{5,7},{0,4,6,7},{8},{0,1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={3,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={1,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={0,4,6,7} then 1 else if T={8} then 2 else if T={0,1,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[11,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[10,14,16,17],1⟩,⟨[18],2⟩,⟨[10,11,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10397
namespace Case10397
def big : Finset (Finset (Fin 9)) := {{1,4,5},{2,3,6},{0,4,6,7},{0,1,8},{2,4,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{3,4},{0,5},{2,5},{3,5},{1,4,5},{1,6},{2,3,6},{5,6},{1,7},{2,7},{5,7},{0,4,6,7},{0,1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
end Case10397
namespace Case10398
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{0,3},{1,3},{4},{0,1,4},{0,5},{2,5},{3,5},{4,5},{6},{1,6},{2,3,6},{4,6},{5,6},{7},{1,7},{3,7},{2,4,7},{5,7},{8},{2,8},{3,4,8},{1,5,8},{0,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 3 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={1,5,8} then 1 else if T={0,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,11,14],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[13,14,18],1⟩,⟨[11,15,18],1⟩,⟨[10,16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10398
namespace Case10398
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,3,6},{2,4,7},{3,4,8},{1,5,8},{0,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{0,1,4},{0,5},{2,5},{3,5},{4,5},{1,6},{2,3,6},{4,6},{5,6},{1,7},{3,7},{2,4,7},{5,7},{2,8},{3,4,8},{1,5,8},{0,6,7,8}]
end Case10398
namespace Case10399
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{2,3},{4},{0,1,4},{0,5},{2,5},{1,3,5},{4,5},{6},{1,6},{2,4,6},{5,6},{7},{1,7},{4,7},{5,7},{0,3,6,7},{8},{0,8},{1,8},{3,4,8},{5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={1,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={0,3,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,11,14],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[11,13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[10,13,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10399
namespace Case10399
def big : Finset (Finset (Fin 9)) := {{0,1,4},{1,3,5},{2,4,6},{0,3,6,7},{3,4,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{2,3},{0,1,4},{0,5},{2,5},{1,3,5},{4,5},{1,6},{2,4,6},{5,6},{1,7},{4,7},{5,7},{0,3,6,7},{0,8},{1,8},{3,4,8},{5,8},{6,8},{2,7,8}]
end Case10399
namespace Case10400
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{4},{0,1,4},{2,3,4},{0,5},{2,5},{1,3,5},{4,5},{6},{1,6},{4,6},{5,6},{7},{1,7},{2,7},{5,7},{0,3,6,7},{8},{0,8},{1,8},{3,8},{5,8},{2,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={0,1,4} then 1 else if T={2,3,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={1,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={0,3,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[15],1⟩,⟨[11,12,15],1⟩,⟨[13,14,15],1⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[12,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[16,18],1⟩,⟨[11,14,17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[14,19],1⟩,⟨[16,19],1⟩,⟨[13,17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10400
namespace Case10400
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,3,4},{1,3,5},{0,3,6,7},{2,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,1,4},{2,3,4},{0,5},{2,5},{1,3,5},{4,5},{1,6},{4,6},{5,6},{1,7},{2,7},{5,7},{0,3,6,7},{0,8},{1,8},{3,8},{5,8},{2,6,8},{4,7,8}]
end Case10400
namespace Case10401
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{0,2},{3},{2,3},{4},{1,3,4},{0,5},{1,5},{2,5},{4,5},{6},{1,2,6},{4,6},{5,6},{7},{1,7},{2,4,7},{5,7},{0,3,6,7},{8},{1,8},{2,8},{0,4,8},{3,5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={0,1} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={1,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={0,3,6,7} then 1 else if T={8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={0,4,8} then 1 else if T={3,5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,13,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,12,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[10,13,16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[10,14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10401
namespace Case10401
def big : Finset (Finset (Fin 9)) := {{1,3,4},{1,2,6},{2,4,7},{0,3,6,7},{0,4,8},{3,5,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{2,3},{1,3,4},{0,5},{1,5},{2,5},{4,5},{1,2,6},{4,6},{5,6},{1,7},{2,4,7},{5,7},{0,3,6,7},{1,8},{2,8},{0,4,8},{3,5,8},{6,8},{7,8}]
end Case10401
namespace Case10402
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{0,3},{1,3},{2,3},{4},{1,4},{0,5},{1,5},{2,5},{3,4,5},{6},{1,2,6},{3,6},{5,6},{7},{1,7},{2,7},{5,7},{0,4,6,7},{8},{0,1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={0,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={1,2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={0,4,6,7} then 1 else if T={8} then 2 else if T={0,1,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[11,12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[10,14,16,17],1⟩,⟨[18],2⟩,⟨[10,11,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10402
namespace Case10402
def big : Finset (Finset (Fin 9)) := {{3,4,5},{1,2,6},{0,4,6,7},{0,1,8},{2,4,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{1,3},{2,3},{1,4},{0,5},{1,5},{2,5},{3,4,5},{1,2,6},{3,6},{5,6},{1,7},{2,7},{5,7},{0,4,6,7},{0,1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
end Case10402
namespace Case10403
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{0,3},{1,3},{2,3},{4},{0,1,4},{0,5},{1,5},{2,5},{4,5},{6},{1,2,6},{3,6},{4,6},{5,6},{7},{1,7},{2,7},{3,4,7},{5,7},{8},{1,8},{2,4,8},{3,5,8},{0,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={0,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 3 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={0,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,11,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[18],3⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[13,15,18],1⟩,⟨[10,16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10403
namespace Case10403
def big : Finset (Finset (Fin 9)) := {{0,1,4},{1,2,6},{3,4,7},{2,4,8},{3,5,8},{0,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{1,3},{2,3},{0,1,4},{0,5},{1,5},{2,5},{4,5},{1,2,6},{3,6},{4,6},{5,6},{1,7},{2,7},{3,4,7},{5,7},{1,8},{2,4,8},{3,5,8},{0,6,7,8}]
end Case10403
namespace Case10404
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{1,3},{4},{0,1,4},{0,5},{1,5},{2,3,5},{4,5},{6},{1,6},{2,4,6},{5,6},{7},{2,7},{4,7},{5,7},{0,3,6,7},{8},{0,8},{2,8},{3,4,8},{5,8},{6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={0,3,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,11,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[10,13,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[12,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10404
namespace Case10404
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,3,5},{2,4,6},{0,3,6,7},{3,4,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{0,1,4},{0,5},{1,5},{2,3,5},{4,5},{1,6},{2,4,6},{5,6},{2,7},{4,7},{5,7},{0,3,6,7},{0,8},{2,8},{3,4,8},{5,8},{6,8},{1,7,8}]
end Case10404
namespace Case10405
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{0,2},{1,2},{3},{4},{1,3,4},{0,5},{1,5},{2,3,5},{4,5},{6},{1,6},{2,4,6},{5,6},{7},{2,7},{4,7},{5,7},{0,3,6,7},{8},{2,8},{3,8},{0,4,8},{5,8},{6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={1,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={0,3,6,7} then 1 else if T={8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={0,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[15],1⟩,⟨[12,14,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[13,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[11,14,17,18],1⟩,⟨[19],1⟩,⟨[13,19],1⟩,⟨[14,19],1⟩,⟨[11,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10405
namespace Case10405
def big : Finset (Finset (Fin 9)) := {{1,3,4},{2,3,5},{2,4,6},{0,3,6,7},{0,4,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{1,2},{1,3,4},{0,5},{1,5},{2,3,5},{4,5},{1,6},{2,4,6},{5,6},{2,7},{4,7},{5,7},{0,3,6,7},{2,8},{3,8},{0,4,8},{5,8},{6,8},{1,7,8}]
end Case10405
namespace Case10406
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{3},{1,3},{4},{0,1,4},{2,3,4},{0,5},{1,5},{2,5},{4,5},{6},{1,2,6},{4,6},{5,6},{7},{1,7},{2,7},{5,7},{0,3,6,7},{8},{0,8},{1,8},{2,8},{3,5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={2,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={0,3,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11],1⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,12,15],1⟩,⟨[13,14,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[12,13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[16,18],1⟩,⟨[11,14,17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,19],1⟩,⟨[14,16,19],1⟩,⟨[17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10406
namespace Case10406
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,3,4},{1,2,6},{0,3,6,7},{3,5,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,3},{0,1,4},{2,3,4},{0,5},{1,5},{2,5},{4,5},{1,2,6},{4,6},{5,6},{1,7},{2,7},{5,7},{0,3,6,7},{0,8},{1,8},{2,8},{3,5,8},{6,8},{4,7,8}]
end Case10406
namespace Case10407
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{3},{1,3},{4},{0,3,4},{0,5},{1,5},{2,3,5},{4,5},{6},{0,1,6},{2,6},{4,6},{5,6},{7},{0,7},{2,7},{1,4,7},{5,7},{8},{0,8},{1,8},{2,4,8},{5,8},{3,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={3,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,13,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[11,14,17],1⟩,⟨[15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[13,16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10407
namespace Case10407
def big : Finset (Finset (Fin 9)) := {{0,3,4},{2,3,5},{0,1,6},{1,4,7},{2,4,8},{3,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{0,3,4},{0,5},{1,5},{2,3,5},{4,5},{0,1,6},{2,6},{4,6},{5,6},{0,7},{2,7},{1,4,7},{5,7},{0,8},{1,8},{2,4,8},{5,8},{3,6,7,8}]
end Case10407
namespace Case10408
def positionFn : Fin 9 → Fin 25 := ![11,14,10,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{5},{2,5},{6},{2,6},{0,1,5,6},{7},{1,7},{0,2,7},{3,5,7},{4,6,7},{8},{0,8},{1,2,8},{4,5,8},{3,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={6} then 3 else if T={2,6} then 1 else if T={0,1,5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,2,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,15,20,21,22,23,24,25],[⟨[],3⟩,⟨[12],1⟩,⟨[15],1⟩,⟨[12,20],1⟩,⟨[15,20],1⟩,⟨[11,20],1⟩,⟨[12,21],1⟩,⟨[15,21],1⟩,⟨[11,21],1⟩,⟨[20,21],1⟩,⟨[22],3⟩,⟨[11,22],1⟩,⟨[23],3⟩,⟨[11,23],1⟩,⟨[12,15,22,23],1⟩,⟨[24],2⟩,⟨[15,24],1⟩,⟨[11,12,24],1⟩,⟨[20,22,24],1⟩,⟨[21,23,24],1⟩,⟨[25],2⟩,⟨[12,25],1⟩,⟨[11,15,25],1⟩,⟨[21,22,25],1⟩,⟨[20,23,25],1⟩,⟨[24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10408
namespace Case10408
def big : Finset (Finset (Fin 9)) := {{0,1,5,6},{0,2,7},{3,5,7},{4,6,7},{1,2,8},{4,5,8},{3,6,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{2,5},{2,6},{0,1,5,6},{1,7},{0,2,7},{3,5,7},{4,6,7},{0,8},{1,2,8},{4,5,8},{3,6,8},{7,8}]
end Case10408
namespace Case10409
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,3},{1,3},{2,3},{4},{2,4},{5},{0,5},{1,5},{2,5},{3,5},{6},{2,6},{0,1,4,6},{7},{1,7},{0,2,7},{3,4,7},{5,6,7},{8},{0,8},{1,2,8},{4,5,8},{3,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 3 else if T={2,6} then 1 else if T={0,1,4,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,2,7} then 1 else if T={3,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[13,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],3⟩,⟨[13,17],1⟩,⟨[11,12,15,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[11,13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,13,19],1⟩,⟨[15,16,19],1⟩,⟨[14,17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10409
namespace Case10409
def big : Finset (Finset (Fin 9)) := {{0,1,4,6},{0,2,7},{3,4,7},{5,6,7},{1,2,8},{4,5,8},{3,6,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{2,3},{2,4},{0,5},{1,5},{2,5},{3,5},{2,6},{0,1,4,6},{1,7},{0,2,7},{3,4,7},{5,6,7},{0,8},{1,2,8},{4,5,8},{3,6,8},{7,8}]
end Case10409
namespace Case10410
def positionFn : Fin 9 → Fin 25 := ![11,14,10,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,3},{1,3},{2,3},{4},{1,4},{0,2,4},{5},{0,5},{1,5},{2,5},{3,5},{6},{2,6},{3,4,6},{7},{2,7},{4,5,7},{0,1,6,7},{8},{0,8},{1,2,8},{4,8},{5,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 3 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={7} then 3 else if T={2,7} then 1 else if T={4,5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={4,8} then 1 else if T={5,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,15,20,21,22,23,24,25],[⟨[],3⟩,⟨[12],1⟩,⟨[15],1⟩,⟨[12,20],1⟩,⟨[15,20],1⟩,⟨[11,20],1⟩,⟨[21],1⟩,⟨[15,21],1⟩,⟨[11,12,21],1⟩,⟨[22],1⟩,⟨[12,22],1⟩,⟨[15,22],1⟩,⟨[11,22],1⟩,⟨[20,22],1⟩,⟨[23],3⟩,⟨[11,23],1⟩,⟨[20,21,23],1⟩,⟨[24],3⟩,⟨[11,24],1⟩,⟨[21,22,24],1⟩,⟨[12,15,23,24],1⟩,⟨[25],2⟩,⟨[12,25],1⟩,⟨[11,15,25],1⟩,⟨[21,25],1⟩,⟨[22,23,25],1⟩,⟨[20,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10410
namespace Case10410
def big : Finset (Finset (Fin 9)) := {{0,2,4},{3,4,6},{4,5,7},{0,1,6,7},{1,2,8},{5,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{2,3},{1,4},{0,2,4},{0,5},{1,5},{2,5},{3,5},{2,6},{3,4,6},{2,7},{4,5,7},{0,1,6,7},{0,8},{1,2,8},{4,8},{5,6,8},{3,7,8}]
end Case10410
namespace Case10411
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{3},{2,3},{4},{2,4},{0,1,3,4},{5},{0,5},{1,5},{2,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{1,7},{0,2,7},{3,5,7},{4,6,7},{8},{0,8},{1,2,8},{4,5,8},{3,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={0,1,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,2,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[13,15],1⟩,⟨[11,12,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[11,13,18],1⟩,⟨[14,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,13,19],1⟩,⟨[15,16,19],1⟩,⟨[14,17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10411
namespace Case10411
def big : Finset (Finset (Fin 9)) := {{0,1,3,4},{0,2,7},{3,5,7},{4,6,7},{1,2,8},{4,5,8},{3,6,8}}
def full : List (Finset (Fin 9)) := [{2,3},{2,4},{0,1,3,4},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{5,6},{1,7},{0,2,7},{3,5,7},{4,6,7},{0,8},{1,2,8},{4,5,8},{3,6,8},{7,8}]
end Case10411
namespace Case10412
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{3},{2,3},{4},{1,4},{0,2,4},{5},{0,5},{1,5},{2,5},{3,4,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{2,7},{0,1,3,7},{4,6,7},{8},{0,8},{1,2,8},{4,8},{3,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={2,7} then 1 else if T={0,1,3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={4,8} then 1 else if T={3,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[10,12,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[12,17],1⟩,⟨[10,11,13,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,12,18],1⟩,⟨[14,18],1⟩,⟨[13,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10412
namespace Case10412
def big : Finset (Finset (Fin 9)) := {{0,2,4},{3,4,5},{0,1,3,7},{4,6,7},{1,2,8},{3,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{2,3},{1,4},{0,2,4},{0,5},{1,5},{2,5},{3,4,5},{0,6},{1,6},{2,6},{5,6},{2,7},{0,1,3,7},{4,6,7},{0,8},{1,2,8},{4,8},{3,6,8},{5,7,8}]
end Case10412
namespace Case10413
def positionFn : Fin 9 → Fin 25 := ![11,14,10,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{3},{1,3},{0,2,3},{4},{0,4},{1,2,4},{3,4},{5},{0,5},{1,5},{2,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{2,7},{3,5,7},{4,6,7},{8},{2,8},{4,5,8},{3,6,8},{0,1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={2,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={2,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={0,1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,15,20,21,22,23,24,25],[⟨[],3⟩,⟨[12],1⟩,⟨[15],1⟩,⟨[20],1⟩,⟨[15,20],1⟩,⟨[11,12,20],1⟩,⟨[21],1⟩,⟨[12,21],1⟩,⟨[11,15,21],1⟩,⟨[20,21],1⟩,⟨[22],1⟩,⟨[12,22],1⟩,⟨[15,22],1⟩,⟨[11,22],1⟩,⟨[23],1⟩,⟨[12,23],1⟩,⟨[15,23],1⟩,⟨[11,23],1⟩,⟨[22,23],1⟩,⟨[24],3⟩,⟨[11,24],1⟩,⟨[20,22,24],1⟩,⟨[21,23,24],1⟩,⟨[25],3⟩,⟨[11,25],1⟩,⟨[21,22,25],1⟩,⟨[20,23,25],1⟩,⟨[12,15,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10413
namespace Case10413
def big : Finset (Finset (Fin 9)) := {{0,2,3},{1,2,4},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{0,1,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,2,3},{0,4},{1,2,4},{3,4},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{5,6},{2,7},{3,5,7},{4,6,7},{2,8},{4,5,8},{3,6,8},{0,1,7,8}]
end Case10413
namespace Case10414
def positionFn : Fin 9 → Fin 25 := ![19,20,11,12,13,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{0,3},{1,3},{2,3},{4},{5},{2,5},{3,5},{4,5},{6},{0,1,4,6},{5,6},{7},{1,7},{2,4,7},{0,5,7},{3,6,7},{8},{0,8},{3,4,8},{1,5,8},{2,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={0,1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={0,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={3,4,8} then 1 else if T={1,5,8} then 1 else if T={2,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,13,14,20,21,22,23,24,25],[⟨[],3⟩,⟨[20],1⟩,⟨[21],1⟩,⟨[12,20],1⟩,⟨[12,21],1⟩,⟨[13,20],1⟩,⟨[13,21],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[22],1⟩,⟨[12,22],1⟩,⟨[13,22],1⟩,⟨[14,22],1⟩,⟨[23],3⟩,⟨[14,20,21,23],1⟩,⟨[22,23],1⟩,⟨[24],2⟩,⟨[21,24],1⟩,⟨[12,14,24],1⟩,⟨[20,22,24],1⟩,⟨[13,23,24],1⟩,⟨[25],2⟩,⟨[20,25],1⟩,⟨[13,14,25],1⟩,⟨[21,22,25],1⟩,⟨[12,23,25],1⟩,⟨[24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10414
namespace Case10414
def big : Finset (Finset (Fin 9)) := {{0,1,4,6},{2,4,7},{0,5,7},{3,6,7},{3,4,8},{1,5,8},{2,6,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{2,3},{2,5},{3,5},{4,5},{0,1,4,6},{5,6},{1,7},{2,4,7},{0,5,7},{3,6,7},{0,8},{3,4,8},{1,5,8},{2,6,8},{7,8}]
end Case10414
namespace Case10415
def positionFn : Fin 9 → Fin 25 := ![11,20,13,14,12,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{0,3},{1,3},{2,3},{4},{1,4},{5},{2,5},{3,5},{0,4,5},{6},{2,4,6},{5,6},{7},{3,4,7},{5,7},{0,1,6,7},{8},{0,8},{4,8},{1,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 3 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={4,8} then 1 else if T={1,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,13,14,15,21,22,23,24,25],[⟨[],3⟩,⟨[12],1⟩,⟨[21],1⟩,⟨[12,14],1⟩,⟨[14,21],1⟩,⟨[12,15],1⟩,⟨[15,21],1⟩,⟨[14,15],1⟩,⟨[13],1⟩,⟨[13,21],1⟩,⟨[22],1⟩,⟨[14,22],1⟩,⟨[15,22],1⟩,⟨[12,13,22],1⟩,⟨[23],3⟩,⟨[13,14,23],1⟩,⟨[22,23],1⟩,⟨[24],3⟩,⟨[13,15,24],1⟩,⟨[22,24],1⟩,⟨[12,21,23,24],1⟩,⟨[25],2⟩,⟨[12,25],1⟩,⟨[13,25],1⟩,⟨[21,22,25],1⟩,⟨[15,23,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10415
namespace Case10415
def big : Finset (Finset (Fin 9)) := {{0,4,5},{2,4,6},{3,4,7},{0,1,6,7},{1,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{2,3},{1,4},{2,5},{3,5},{0,4,5},{2,4,6},{5,6},{3,4,7},{5,7},{0,1,6,7},{0,8},{4,8},{1,5,8},{3,6,8},{2,7,8}]
end Case10415
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

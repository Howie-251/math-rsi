import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case4320
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{0,3},{4},{0,4},{1,3,4},{5},{3,5},{4,5},{6},{0,1,2,5,6},{7},{0,7},{1,7},{2,3,7},{4,6,7},{8},{0,8},{1,8},{2,4,8},{3,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 2 else if T={2} then 3 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 4 else if T={0,1,2,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={3,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],1⟩,⟨[12],2⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,14,15],1⟩,⟨[16],3⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],4⟩,⟨[11,12,13,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,14,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,15,19],1⟩,⟨[14,17,19],1⟩,⟨[16,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4320
namespace Case4320
def big : Finset (Finset (Fin 9)) := {{1,3,4},{0,1,2,5,6},{2,3,7},{4,6,7},{2,4,8},{3,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{1,3,4},{3,5},{4,5},{0,1,2,5,6},{0,7},{1,7},{2,3,7},{4,6,7},{0,8},{1,8},{2,4,8},{3,6,8},{5,7,8}]
end Case4320
namespace Case4321
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{0,3},{4},{0,4},{1,4},{2,3,4},{5},{3,5},{6},{0,1,2,5,6},{7},{0,7},{1,3,7},{5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 2 else if T={2} then 3 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={6} then 4 else if T={0,1,2,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],1⟩,⟨[12],2⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],3⟩,⟨[14,16],1⟩,⟨[17],4⟩,⟨[11,12,13,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[15,16,19],1⟩,⟨[14,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4321
namespace Case4321
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,1,2,5,6},{1,3,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{1,4},{2,3,4},{3,5},{0,1,2,5,6},{0,7},{1,3,7},{5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
end Case4321
namespace Case4322
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{0,3},{4},{0,4},{1,4},{5},{3,5},{6},{3,4,6},{0,1,2,5,6},{7},{0,7},{1,3,7},{2,4,7},{5,7},{8},{0,8},{1,8},{2,3,8},{4,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 2 else if T={2} then 3 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={6} then 4 else if T={3,4,6} then 1 else if T={0,1,2,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={4,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],1⟩,⟨[11],2⟩,⟨[12],3⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],3⟩,⟨[13,15],1⟩,⟨[16],4⟩,⟨[13,14,16],1⟩,⟨[10,11,12,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4322
namespace Case4322
def big : Finset (Finset (Fin 9)) := {{3,4,6},{0,1,2,5,6},{1,3,7},{2,4,7},{2,3,8},{4,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{1,4},{3,5},{3,4,6},{0,1,2,5,6},{0,7},{1,3,7},{2,4,7},{5,7},{0,8},{1,8},{2,3,8},{4,5,8},{6,7,8}]
end Case4322
namespace Case4323
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{0,3},{1,3},{4},{0,4},{1,4},{5},{3,4,5},{6},{0,1,2,5,6},{7},{0,7},{2,3,7},{5,7},{4,6,7},{8},{0,8},{2,4,8},{5,8},{3,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 2 else if T={2} then 3 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 3 else if T={3,4,5} then 1 else if T={6} then 4 else if T={0,1,2,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],1⟩,⟨[12],2⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],3⟩,⟨[14,15,16],1⟩,⟨[17],4⟩,⟨[11,12,13,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,14,18],1⟩,⟨[16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,15,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4323
namespace Case4323
def big : Finset (Finset (Fin 9)) := {{3,4,5},{0,1,2,5,6},{2,3,7},{4,6,7},{2,4,8},{3,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{0,4},{1,4},{3,4,5},{0,1,2,5,6},{0,7},{2,3,7},{5,7},{4,6,7},{0,8},{2,4,8},{5,8},{3,6,8},{1,7,8}]
end Case4323
namespace Case4324
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{0,2},{3},{0,3},{1,2,3},{4},{0,4},{1,4},{5},{2,5},{3,5},{6},{2,4,6},{7},{3,4,7},{0,1,5,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 2 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 4 else if T={2,4,6} then 1 else if T={7} then 4 else if T={3,4,7} then 1 else if T={0,1,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],1⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],3⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],4⟩,⟨[13,15,17],1⟩,⟨[18],4⟩,⟨[14,15,18],1⟩,⟨[11,12,16,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[15,16,19],1⟩,⟨[14,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4324
namespace Case4324
def big : Finset (Finset (Fin 9)) := {{1,2,3},{2,4,6},{3,4,7},{0,1,5,6,7},{4,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{1,2,3},{0,4},{1,4},{2,5},{3,5},{2,4,6},{3,4,7},{0,1,5,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
end Case4324
namespace Case4325
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{0,2},{3},{0,3},{1,3},{4},{0,4},{1,4},{5},{2,5},{3,4,5},{6},{2,3,6},{7},{2,4,7},{0,1,5,6,7},{8},{0,8},{1,2,8},{5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 2 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 4 else if T={2,3,6} then 1 else if T={7} then 4 else if T={2,4,7} then 1 else if T={0,1,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],1⟩,⟨[11],2⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],4⟩,⟨[12,13,16],1⟩,⟨[17],4⟩,⟨[12,14,17],1⟩,⟨[10,11,15,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,12,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4325
namespace Case4325
def big : Finset (Finset (Fin 9)) := {{3,4,5},{2,3,6},{2,4,7},{0,1,5,6,7},{1,2,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{1,3},{0,4},{1,4},{2,5},{3,4,5},{2,3,6},{2,4,7},{0,1,5,6,7},{0,8},{1,2,8},{5,8},{4,6,8},{3,7,8}]
end Case4325
namespace Case4326
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{0,3},{4},{0,4},{5},{3,4,5},{6},{3,6},{4,6},{0,1,2,5,6},{7},{0,7},{1,3,7},{2,4,7},{5,7},{8},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 3 else if T={2} then 3 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 3 else if T={3,4,5} then 1 else if T={6} then 3 else if T={3,6} then 1 else if T={4,6} then 1 else if T={0,1,2,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],1⟩,⟨[12],3⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],3⟩,⟨[14,15,16],1⟩,⟨[17],3⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[11,12,13,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,14,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4326
namespace Case4326
def big : Finset (Finset (Fin 9)) := {{3,4,5},{0,1,2,5,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{3,4,5},{3,6},{4,6},{0,1,2,5,6},{0,7},{1,3,7},{2,4,7},{5,7},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
end Case4326
namespace Case4327
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{0,3},{4},{0,4},{1,3,4},{5},{3,5},{6},{4,6},{0,1,2,5,6},{7},{0,7},{2,3,7},{4,5,7},{6,7},{8},{0,8},{2,4,8},{5,8},{3,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 3 else if T={2} then 3 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={6} then 3 else if T={4,6} then 1 else if T={0,1,2,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,3,7} then 1 else if T={4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],1⟩,⟨[11],3⟩,⟨[12],3⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,13,14],1⟩,⟨[15],3⟩,⟨[13,15],1⟩,⟨[16],3⟩,⟨[14,16],1⟩,⟨[10,11,12,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,13,17],1⟩,⟨[14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[13,16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4327
namespace Case4327
def big : Finset (Finset (Fin 9)) := {{1,3,4},{0,1,2,5,6},{2,3,7},{4,5,7},{2,4,8},{3,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{1,3,4},{3,5},{4,6},{0,1,2,5,6},{0,7},{2,3,7},{4,5,7},{6,7},{0,8},{2,4,8},{5,8},{3,6,8},{1,7,8}]
end Case4327
namespace Case4328
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{0,2},{3},{0,3},{1,2,3},{4},{0,4},{5},{3,5},{2,4,5},{6},{2,6},{4,6},{7},{3,4,7},{0,1,5,6,7},{8},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 3 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 3 else if T={2,6} then 1 else if T={4,6} then 1 else if T={7} then 4 else if T={3,4,7} then 1 else if T={0,1,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],1⟩,⟨[12],3⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],3⟩,⟨[14,16],1⟩,⟨[13,15,16],1⟩,⟨[17],3⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[18],4⟩,⟨[14,15,18],1⟩,⟨[11,12,16,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4328
namespace Case4328
def big : Finset (Finset (Fin 9)) := {{1,2,3},{2,4,5},{3,4,7},{0,1,5,6,7},{1,4,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{1,2,3},{0,4},{3,5},{2,4,5},{2,6},{4,6},{3,4,7},{0,1,5,6,7},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]
end Case4328
namespace Case4329
def positionFn : Fin 9 → Fin 25 := ![8,9,10,11,12,13,14,15,16]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{0,1},{2},{0,2},{3},{0,3},{4},{0,4},{5},{1,2,5},{3,5},{4,5},{6},{1,6},{2,6},{3,4,6},{7},{1,3,7},{2,4,7},{8},{2,3,8},{1,4,8},{0,5,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 3 else if T={1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={7} then 4 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={8} then 4 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={0,5,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,16,17],[⟨[9],1⟩,⟨[10],1⟩,⟨[9,10],1⟩,⟨[11],1⟩,⟨[9,11],1⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[14],3⟩,⟨[10,11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],3⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,13,15],1⟩,⟨[16],4⟩,⟨[10,12,16],1⟩,⟨[11,13,16],1⟩,⟨[17],4⟩,⟨[11,12,17],1⟩,⟨[10,13,17],1⟩,⟨[9,14,15,16,17],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4329
namespace Case4329
def big : Finset (Finset (Fin 9)) := {{1,2,5},{3,4,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{0,5,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{0,3},{0,4},{1,2,5},{3,5},{4,5},{1,6},{2,6},{3,4,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{0,5,6,7,8}]
end Case4329
namespace Case4330
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{4},{1,4},{5},{0,1,2,3,5},{4,5},{6},{1,6},{0,4,6},{5,6},{7},{0,7},{2,4,7},{5,7},{3,6,7},{8},{0,8},{3,4,8},{5,8},{2,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 3 else if T={3} then 3 else if T={4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={0,1,2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],2⟩,⟨[11],2⟩,⟨[12],3⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[10,11,12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[10,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[13,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[12,16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4330
namespace Case4330
def big : Finset (Finset (Fin 9)) := {{0,1,2,3,5},{0,4,6},{2,4,7},{3,6,7},{3,4,8},{2,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{1,4},{0,1,2,3,5},{4,5},{1,6},{0,4,6},{5,6},{0,7},{2,4,7},{5,7},{3,6,7},{0,8},{3,4,8},{5,8},{2,6,8},{1,7,8}]
end Case4330
namespace Case4331
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{1,3},{4},{1,4},{0,3,4},{5},{3,5},{4,5},{6},{0,1,2,5,6},{7},{0,7},{2,3,7},{5,7},{4,6,7},{8},{0,8},{2,4,8},{5,8},{3,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 3 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 4 else if T={0,1,2,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],2⟩,⟨[12],2⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[11,14,15],1⟩,⟨[16],2⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],4⟩,⟨[11,12,13,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,14,18],1⟩,⟨[16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,15,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4331
namespace Case4331
def big : Finset (Finset (Fin 9)) := {{0,3,4},{0,1,2,5,6},{2,3,7},{4,6,7},{2,4,8},{3,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{1,4},{0,3,4},{3,5},{4,5},{0,1,2,5,6},{0,7},{2,3,7},{5,7},{4,6,7},{0,8},{2,4,8},{5,8},{3,6,8},{1,7,8}]
end Case4331
namespace Case4332
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{1,3},{4},{0,4},{2,3,4},{5},{3,5},{4,5},{6},{0,1,2,5,6},{7},{1,7},{0,3,7},{5,7},{4,6,7},{8},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 3 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,3,4} then 1 else if T={5} then 2 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 4 else if T={0,1,2,5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],2⟩,⟨[12],2⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],4⟩,⟨[11,12,13,16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[11,14,18],1⟩,⟨[16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4332
namespace Case4332
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,1,2,5,6},{0,3,7},{4,6,7},{1,4,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,4},{2,3,4},{3,5},{4,5},{0,1,2,5,6},{1,7},{0,3,7},{5,7},{4,6,7},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]
end Case4332
namespace Case4333
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{1,3},{4},{0,4},{5},{3,5},{4,5},{6},{3,4,6},{0,1,2,5,6},{7},{1,7},{0,3,7},{2,4,7},{5,7},{8},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 3 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 2 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 4 else if T={3,4,6} then 1 else if T={0,1,2,5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],2⟩,⟨[12],2⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],2⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],4⟩,⟨[14,15,17],1⟩,⟨[11,12,13,16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[11,14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,14,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4333
namespace Case4333
def big : Finset (Finset (Fin 9)) := {{3,4,6},{0,1,2,5,6},{0,3,7},{2,4,7},{2,3,8},{1,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,4},{3,5},{4,5},{3,4,6},{0,1,2,5,6},{1,7},{0,3,7},{2,4,7},{5,7},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
end Case4333
namespace Case4334
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{1,2},{3},{1,3},{0,2,3},{4},{0,4},{5},{2,5},{3,5},{4,5},{6},{2,4,6},{7},{3,4,7},{0,1,5,6,7},{8},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 4 else if T={2,4,6} then 1 else if T={7} then 4 else if T={3,4,7} then 1 else if T={0,1,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],2⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],4⟩,⟨[13,15,17],1⟩,⟨[18],4⟩,⟨[14,15,18],1⟩,⟨[11,12,16,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4334
namespace Case4334
def big : Finset (Finset (Fin 9)) := {{0,2,3},{2,4,6},{3,4,7},{0,1,5,6,7},{1,4,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{1,3},{0,2,3},{0,4},{2,5},{3,5},{4,5},{2,4,6},{3,4,7},{0,1,5,6,7},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]
end Case4334
namespace Case4335
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{4},{0,3,4},{5},{3,5},{4,5},{6},{3,6},{4,6},{0,1,2,5,6},{7},{0,7},{1,3,7},{2,4,7},{5,7},{8},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 3 else if T={2} then 3 else if T={3} then 1 else if T={4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={3,6} then 1 else if T={4,6} then 1 else if T={0,1,2,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],2⟩,⟨[12],3⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[15],1⟩,⟨[11,14,15],1⟩,⟨[16],2⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[11,12,13,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,14,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4335
namespace Case4335
def big : Finset (Finset (Fin 9)) := {{0,3,4},{0,1,2,5,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,3,4},{3,5},{4,5},{3,6},{4,6},{0,1,2,5,6},{0,7},{1,3,7},{2,4,7},{5,7},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
end Case4335
namespace Case4336
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{4},{0,4},{1,3,4},{5},{3,5},{4,5},{6},{3,6},{0,1,2,5,6},{7},{0,3,7},{2,4,7},{5,7},{6,7},{8},{0,8},{2,3,8},{5,8},{4,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 3 else if T={2} then 3 else if T={3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={5} then 2 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={3,6} then 1 else if T={0,1,2,5,6} then 1 else if T={7} then 2 else if T={0,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],2⟩,⟨[12],3⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,14,15],1⟩,⟨[16],2⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[14,17],1⟩,⟨[11,12,13,16,17],1⟩,⟨[18],2⟩,⟨[11,14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,14,19],1⟩,⟨[16,19],1⟩,⟨[15,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4336
namespace Case4336
def big : Finset (Finset (Fin 9)) := {{1,3,4},{0,1,2,5,6},{0,3,7},{2,4,7},{2,3,8},{4,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,4},{1,3,4},{3,5},{4,5},{3,6},{0,1,2,5,6},{0,3,7},{2,4,7},{5,7},{6,7},{0,8},{2,3,8},{5,8},{4,6,8},{1,7,8}]
end Case4336
namespace Case4337
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{0,3},{4},{0,4},{5},{3,5},{4,5},{6},{3,4,6},{0,1,2,5,6},{7},{1,3,7},{2,4,7},{5,7},{6,7},{8},{2,3,8},{1,4,8},{5,8},{6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 3 else if T={2} then 3 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 2 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={3,4,6} then 1 else if T={0,1,2,5,6} then 1 else if T={7} then 2 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],2⟩,⟨[12],3⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],2⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[14,15,17],1⟩,⟨[11,12,13,16,17],1⟩,⟨[18],2⟩,⟨[12,14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[13,14,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[11,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4337
namespace Case4337
def big : Finset (Finset (Fin 9)) := {{3,4,6},{0,1,2,5,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{0,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{3,5},{4,5},{3,4,6},{0,1,2,5,6},{1,3,7},{2,4,7},{5,7},{6,7},{2,3,8},{1,4,8},{5,8},{6,8},{0,7,8}]
end Case4337
namespace Case4338
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{0,2,3},{4},{0,4},{1,2,4},{5},{2,5},{3,5},{4,5},{6},{2,6},{3,6},{7},{3,4,7},{0,1,5,6,7},{8},{0,8},{1,3,8},{5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 3 else if T={2} then 1 else if T={3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={2,6} then 1 else if T={3,6} then 1 else if T={7} then 4 else if T={3,4,7} then 1 else if T={0,1,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],2⟩,⟨[12],3⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,13,15],1⟩,⟨[16],2⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[18],4⟩,⟨[14,15,18],1⟩,⟨[11,12,16,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,14,19],1⟩,⟨[16,19],1⟩,⟨[15,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4338
namespace Case4338
def big : Finset (Finset (Fin 9)) := {{0,2,3},{1,2,4},{3,4,7},{0,1,5,6,7},{1,3,8},{4,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2,3},{0,4},{1,2,4},{2,5},{3,5},{4,5},{2,6},{3,6},{3,4,7},{0,1,5,6,7},{0,8},{1,3,8},{5,8},{4,6,8},{2,7,8}]
end Case4338
namespace Case4339
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{0,3},{1,2,3},{4},{0,4},{5},{2,5},{3,5},{4,5},{6},{2,6},{3,4,6},{7},{2,4,7},{0,1,5,6,7},{8},{0,2,8},{1,4,8},{5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 3 else if T={2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={7} then 4 else if T={2,4,7} then 1 else if T={0,1,5,6,7} then 1 else if T={8} then 2 else if T={0,2,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],2⟩,⟨[12],3⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],2⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[13,17],1⟩,⟨[14,15,17],1⟩,⟨[18],4⟩,⟨[13,15,18],1⟩,⟨[11,12,16,17,18],1⟩,⟨[19],2⟩,⟨[11,13,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4339
namespace Case4339
def big : Finset (Finset (Fin 9)) := {{1,2,3},{3,4,6},{2,4,7},{0,1,5,6,7},{0,2,8},{1,4,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,2,3},{0,4},{2,5},{3,5},{4,5},{2,6},{3,4,6},{2,4,7},{0,1,5,6,7},{0,2,8},{1,4,8},{5,8},{6,8},{3,7,8}]
end Case4339
namespace Case4340
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{0,1,2},{3},{0,3},{4},{0,4},{5},{1,5},{2,5},{3,5},{4,5},{6},{1,6},{2,6},{3,4,6},{7},{1,3,7},{2,4,7},{8},{2,3,8},{1,4,8},{0,5,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={7} then 4 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={8} then 4 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={0,5,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[10,11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[17],4⟩,⟨[11,13,17],1⟩,⟨[12,14,17],1⟩,⟨[18],4⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[10,15,16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4340
namespace Case4340
def big : Finset (Finset (Fin 9)) := {{0,1,2},{3,4,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{0,5,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{0,3},{0,4},{1,5},{2,5},{3,5},{4,5},{1,6},{2,6},{3,4,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{0,5,6,7,8}]
end Case4340
namespace Case4341
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{0,2,3},{4},{1,2,4},{5},{2,5},{3,5},{4,5},{6},{2,6},{3,4,6},{7},{3,7},{4,7},{0,1,5,6,7},{8},{1,3,8},{0,4,8},{5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 3 else if T={1} then 3 else if T={2} then 1 else if T={3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={1,2,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={7} then 3 else if T={3,7} then 1 else if T={4,7} then 1 else if T={0,1,5,6,7} then 1 else if T={8} then 2 else if T={1,3,8} then 1 else if T={0,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],3⟩,⟨[12],3⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[12,13,15],1⟩,⟨[16],2⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[13,17],1⟩,⟨[14,15,17],1⟩,⟨[18],3⟩,⟨[14,18],1⟩,⟨[15,18],1⟩,⟨[11,12,16,17,18],1⟩,⟨[19],2⟩,⟨[12,14,19],1⟩,⟨[11,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4341
namespace Case4341
def big : Finset (Finset (Fin 9)) := {{0,2,3},{1,2,4},{3,4,6},{0,1,5,6,7},{1,3,8},{0,4,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2,3},{1,2,4},{2,5},{3,5},{4,5},{2,6},{3,4,6},{3,7},{4,7},{0,1,5,6,7},{1,3,8},{0,4,8},{5,8},{6,8},{2,7,8}]
end Case4341
namespace Case4342
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{0,1,2},{3},{4},{0,3,4},{5},{1,5},{2,5},{3,5},{4,5},{6},{2,6},{1,3,6},{4,6},{7},{1,7},{3,7},{2,4,7},{8},{2,3,8},{1,4,8},{0,5,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 3 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={2,6} then 1 else if T={1,3,6} then 1 else if T={4,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={8} then 4 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={0,5,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[10,11,12],1⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[10,13,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[12,16],1⟩,⟨[11,13,16],1⟩,⟨[14,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[12,14,17],1⟩,⟨[18],4⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[10,15,16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4342
namespace Case4342
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,4},{1,3,6},{2,4,7},{2,3,8},{1,4,8},{0,5,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{0,3,4},{1,5},{2,5},{3,5},{4,5},{2,6},{1,3,6},{4,6},{1,7},{3,7},{2,4,7},{2,3,8},{1,4,8},{0,5,6,7,8}]
end Case4342
namespace Case4343
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{4},{0,1,2,3,4},{5},{0,5},{1,5},{6},{0,6},{1,6},{2,5,6},{7},{0,7},{1,7},{3,5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 1 else if T={2} then 3 else if T={3} then 3 else if T={4} then 3 else if T={0,1,2,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],1⟩,⟨[11],1⟩,⟨[12],3⟩,⟨[13],3⟩,⟨[14],3⟩,⟨[10,11,12,13,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[14,15,18],1⟩,⟨[13,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4343
namespace Case4343
def big : Finset (Finset (Fin 9)) := {{0,1,2,3,4},{2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2,3,4},{0,5},{1,5},{0,6},{1,6},{2,5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
end Case4343
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

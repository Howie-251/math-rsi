import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case9192
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,3},{2,3},{4},{1,2,4},{5},{0,5},{1,5},{3,4,5},{6},{1,6},{0,4,6},{5,6},{7},{0,7},{1,3,7},{5,7},{2,6,7},{8},{0,1,8},{2,5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={1,2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={2,5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[11,12,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[10,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,13,17],1⟩,⟨[15,17],1⟩,⟨[12,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[12,15,18],1⟩,⟨[13,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9192
namespace Case9192
def big : Finset (Finset (Fin 9)) := {{1,2,4},{3,4,5},{0,4,6},{1,3,7},{2,6,7},{0,1,8},{2,5,8},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{2,3},{1,2,4},{0,5},{1,5},{3,4,5},{1,6},{0,4,6},{5,6},{0,7},{1,3,7},{5,7},{2,6,7},{0,1,8},{2,5,8},{3,6,8},{4,7,8}]
end Case9192
namespace Case9193
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{1,2},{3},{0,3},{4},{0,4},{1,3,4},{5},{0,5},{1,5},{2,5},{3,5},{6},{0,6},{2,3,6},{4,6},{7},{0,1,7},{2,4,7},{5,6,7},{8},{0,2,8},{4,5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,3,6} then 1 else if T={4,6} then 1 else if T={7} then 3 else if T={0,1,7} then 1 else if T={2,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 3 else if T={0,2,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,13,16],1⟩,⟨[14,16],1⟩,⟨[17],3⟩,⟨[10,11,17],1⟩,⟨[12,14,17],1⟩,⟨[15,16,17],1⟩,⟨[18],3⟩,⟨[10,12,18],1⟩,⟨[14,15,18],1⟩,⟨[11,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9193
namespace Case9193
def big : Finset (Finset (Fin 9)) := {{1,3,4},{2,3,6},{0,1,7},{2,4,7},{5,6,7},{0,2,8},{4,5,8},{1,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,4},{1,3,4},{0,5},{1,5},{2,5},{3,5},{0,6},{2,3,6},{4,6},{0,1,7},{2,4,7},{5,6,7},{0,2,8},{4,5,8},{1,6,8},{3,7,8}]
end Case9193
namespace Case9194
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{1,2},{3},{0,3},{4},{0,1,4},{2,3,4},{5},{0,5},{1,5},{2,5},{6},{0,6},{1,3,6},{5,6},{7},{0,7},{3,7},{4,5,7},{2,6,7},{8},{0,2,8},{3,5,8},{4,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,7} then 1 else if T={4,5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 3 else if T={0,2,8} then 1 else if T={3,5,8} then 1 else if T={4,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[11,12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,14,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[14,18],1⟩,⟨[15,16,18],1⟩,⟨[13,17,18],1⟩,⟨[19],3⟩,⟨[11,13,19],1⟩,⟨[14,16,19],1⟩,⟨[15,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9194
namespace Case9194
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,3,4},{1,3,6},{4,5,7},{2,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,1,4},{2,3,4},{0,5},{1,5},{2,5},{0,6},{1,3,6},{5,6},{0,7},{3,7},{4,5,7},{2,6,7},{0,2,8},{3,5,8},{4,6,8},{1,7,8}]
end Case9194
namespace Case9195
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{1,2},{3},{0,3},{4},{0,1,4},{5},{0,5},{1,5},{2,5},{3,4,5},{6},{0,6},{2,3,6},{5,6},{7},{0,7},{3,7},{2,4,7},{1,6,7},{8},{0,2,8},{1,3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={1,6,7} then 1 else if T={8} then 3 else if T={0,2,8} then 1 else if T={1,3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[13,17],1⟩,⟨[12,14,17],1⟩,⟨[11,16,17],1⟩,⟨[18],3⟩,⟨[10,12,18],1⟩,⟨[11,13,18],1⟩,⟨[14,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9195
namespace Case9195
def big : Finset (Finset (Fin 9)) := {{0,1,4},{3,4,5},{2,3,6},{2,4,7},{1,6,7},{0,2,8},{1,3,8},{4,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,1,4},{0,5},{1,5},{2,5},{3,4,5},{0,6},{2,3,6},{5,6},{0,7},{3,7},{2,4,7},{1,6,7},{0,2,8},{1,3,8},{4,6,8},{5,7,8}]
end Case9195
namespace Case9196
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,3},{1,2,3},{4},{0,1,4},{5},{0,5},{1,5},{3,5},{6},{1,6},{2,4,6},{5,6},{7},{0,7},{2,7},{4,5,7},{3,6,7},{8},{3,4,8},{2,5,8},{0,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={4,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 3 else if T={3,4,8} then 1 else if T={2,5,8} then 1 else if T={0,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,13,14],1⟩,⟨[15],2⟩,⟨[11,12,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,18],1⟩,⟨[15,16,18],1⟩,⟨[14,17,18],1⟩,⟨[19],3⟩,⟨[14,15,19],1⟩,⟨[13,16,19],1⟩,⟨[11,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9196
namespace Case9196
def big : Finset (Finset (Fin 9)) := {{1,2,3},{0,1,4},{2,4,6},{4,5,7},{3,6,7},{3,4,8},{2,5,8},{0,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{1,2,3},{0,1,4},{0,5},{1,5},{3,5},{1,6},{2,4,6},{5,6},{0,7},{2,7},{4,5,7},{3,6,7},{3,4,8},{2,5,8},{0,6,8},{1,7,8}]
end Case9196
namespace Case9197
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,3},{1,2,3},{4},{5},{0,5},{1,5},{3,5},{2,4,5},{6},{1,6},{0,4,6},{5,6},{7},{0,7},{2,7},{1,4,7},{3,6,7},{8},{0,1,8},{3,4,8},{2,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 2 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={3,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={3,4,8} then 1 else if T={2,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,13,14],1⟩,⟨[15],2⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[13,15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[11,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,18],1⟩,⟨[12,15,18],1⟩,⟨[14,17,18],1⟩,⟨[19],3⟩,⟨[11,12,19],1⟩,⟨[14,15,19],1⟩,⟨[13,17,19],1⟩,⟨[16,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9197
namespace Case9197
def big : Finset (Finset (Fin 9)) := {{1,2,3},{2,4,5},{0,4,6},{1,4,7},{3,6,7},{0,1,8},{3,4,8},{2,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{1,2,3},{0,5},{1,5},{3,5},{2,4,5},{1,6},{0,4,6},{5,6},{0,7},{2,7},{1,4,7},{3,6,7},{0,1,8},{3,4,8},{2,6,8},{5,7,8}]
end Case9197
namespace Case9198
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,1,3},{4},{5},{0,5},{1,5},{2,4,5},{6},{1,6},{2,3,6},{0,4,6},{5,6},{7},{0,7},{1,2,7},{3,4,7},{5,7},{8},{0,8},{2,8},{1,4,8},{3,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={0,1,3} then 1 else if T={4} then 2 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,4,8} then 1 else if T={3,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[11,12,14],1⟩,⟨[15],2⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[11,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,19],1⟩,⟨[12,15,19],1⟩,⟨[14,16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9198
namespace Case9198
def big : Finset (Finset (Fin 9)) := {{0,1,3},{2,4,5},{2,3,6},{0,4,6},{1,2,7},{3,4,7},{1,4,8},{3,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,1,3},{0,5},{1,5},{2,4,5},{1,6},{2,3,6},{0,4,6},{5,6},{0,7},{1,2,7},{3,4,7},{5,7},{0,8},{2,8},{1,4,8},{3,5,8},{6,7,8}]
end Case9198
namespace Case9199
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,3},{4},{0,1,4},{5},{0,5},{1,5},{2,5},{3,4,5},{6},{1,6},{2,3,6},{5,6},{7},{0,7},{1,2,7},{3,7},{4,6,7},{8},{1,3,8},{2,4,8},{0,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={1,3,8} then 1 else if T={2,4,8} then 1 else if T={0,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,12,17],1⟩,⟨[13,17],1⟩,⟨[14,16,17],1⟩,⟨[18],3⟩,⟨[11,13,18],1⟩,⟨[12,14,18],1⟩,⟨[10,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9199
namespace Case9199
def big : Finset (Finset (Fin 9)) := {{0,1,4},{3,4,5},{2,3,6},{1,2,7},{4,6,7},{1,3,8},{2,4,8},{0,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{0,1,4},{0,5},{1,5},{2,5},{3,4,5},{1,6},{2,3,6},{5,6},{0,7},{1,2,7},{3,7},{4,6,7},{1,3,8},{2,4,8},{0,6,8},{5,7,8}]
end Case9199
namespace Case9200
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,3},{4},{1,2,4},{5},{0,5},{1,5},{3,5},{6},{1,6},{2,3,6},{0,4,6},{5,6},{7},{0,7},{2,7},{1,3,7},{4,5,7},{8},{0,1,8},{3,4,8},{2,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 2 else if T={1,2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,3,7} then 1 else if T={4,5,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={3,4,8} then 1 else if T={2,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],2⟩,⟨[11,12,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,13,16],1⟩,⟨[10,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[11,13,17],1⟩,⟨[14,15,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[13,14,18],1⟩,⟨[12,15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9200
namespace Case9200
def big : Finset (Finset (Fin 9)) := {{1,2,4},{2,3,6},{0,4,6},{1,3,7},{4,5,7},{0,1,8},{3,4,8},{2,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{1,2,4},{0,5},{1,5},{3,5},{1,6},{2,3,6},{0,4,6},{5,6},{0,7},{2,7},{1,3,7},{4,5,7},{0,1,8},{3,4,8},{2,5,8},{6,7,8}]
end Case9200
namespace Case9201
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,1,3},{4},{1,2,4},{5},{0,5},{1,5},{2,3,5},{6},{1,6},{0,4,6},{5,6},{7},{0,7},{3,4,7},{5,7},{2,6,7},{8},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={0,1,3} then 1 else if T={4} then 2 else if T={1,2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,3,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[10,11,13],1⟩,⟨[14],2⟩,⟨[11,12,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,13,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[10,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[12,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,18],1⟩,⟨[14,15,18],1⟩,⟨[13,16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9201
namespace Case9201
def big : Finset (Finset (Fin 9)) := {{0,1,3},{1,2,4},{2,3,5},{0,4,6},{3,4,7},{2,6,7},{4,5,8},{3,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,1,3},{1,2,4},{0,5},{1,5},{2,3,5},{1,6},{0,4,6},{5,6},{0,7},{3,4,7},{5,7},{2,6,7},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]
end Case9201
namespace Case9202
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{1,2},{3},{0,3},{4},{0,1,4},{5},{0,5},{1,5},{2,5},{3,5},{6},{0,6},{1,3,6},{2,4,6},{7},{0,7},{2,3,7},{4,5,7},{6,7},{8},{0,2,8},{3,4,8},{5,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,3,6} then 1 else if T={2,4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,3,7} then 1 else if T={4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={0,2,8} then 1 else if T={3,4,8} then 1 else if T={5,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[11,13,16],1⟩,⟨[12,14,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,13,17],1⟩,⟨[14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[10,12,18],1⟩,⟨[13,14,18],1⟩,⟨[15,16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9202
namespace Case9202
def big : Finset (Finset (Fin 9)) := {{0,1,4},{1,3,6},{2,4,6},{2,3,7},{4,5,7},{0,2,8},{3,4,8},{5,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,1,4},{0,5},{1,5},{2,5},{3,5},{0,6},{1,3,6},{2,4,6},{0,7},{2,3,7},{4,5,7},{6,7},{0,2,8},{3,4,8},{5,6,8},{1,7,8}]
end Case9202
namespace Case9203
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{1,2},{3},{0,1,3},{4},{0,2,4},{5},{0,5},{1,5},{2,5},{6},{0,6},{2,3,6},{4,5,6},{7},{0,7},{1,4,7},{3,5,7},{6,7},{8},{0,8},{3,4,8},{5,8},{1,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,1,3} then 1 else if T={4} then 2 else if T={0,2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,4,7} then 1 else if T={3,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={1,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[10,11,13],1⟩,⟨[14],2⟩,⟨[10,12,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,13,16],1⟩,⟨[14,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,14,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[11,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9203
namespace Case9203
def big : Finset (Finset (Fin 9)) := {{0,1,3},{0,2,4},{2,3,6},{4,5,6},{1,4,7},{3,5,7},{3,4,8},{1,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,1,3},{0,2,4},{0,5},{1,5},{2,5},{0,6},{2,3,6},{4,5,6},{0,7},{1,4,7},{3,5,7},{6,7},{0,8},{3,4,8},{5,8},{1,6,8},{2,7,8}]
end Case9203
namespace Case9204
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,1,3},{4},{2,3,4},{5},{0,5},{1,5},{2,5},{6},{1,6},{0,4,6},{5,6},{7},{0,7},{1,2,7},{4,5,7},{3,6,7},{8},{0,8},{1,4,8},{3,5,8},{2,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={0,1,3} then 1 else if T={4} then 2 else if T={2,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={4,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={3,5,8} then 1 else if T={2,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[10,11,13],1⟩,⟨[14],2⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[10,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,12,17],1⟩,⟨[14,15,17],1⟩,⟨[13,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,14,18],1⟩,⟨[13,15,18],1⟩,⟨[12,16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9204
namespace Case9204
def big : Finset (Finset (Fin 9)) := {{0,1,3},{2,3,4},{0,4,6},{1,2,7},{4,5,7},{3,6,7},{1,4,8},{3,5,8},{2,6,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,1,3},{2,3,4},{0,5},{1,5},{2,5},{1,6},{0,4,6},{5,6},{0,7},{1,2,7},{4,5,7},{3,6,7},{0,8},{1,4,8},{3,5,8},{2,6,8},{7,8}]
end Case9204
namespace Case9205
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{3},{0,3},{2,3},{4},{5},{0,5},{1,5},{2,4,5},{6},{1,3,6},{0,4,6},{5,6},{7},{1,2,7},{3,4,7},{5,7},{6,7},{8},{1,4,8},{3,5,8},{2,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,4,5} then 1 else if T={6} then 2 else if T={1,3,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={1,4,8} then 1 else if T={3,5,8} then 1 else if T={2,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,15,16],1⟩,⟨[17],2⟩,⟨[12,14,17],1⟩,⟨[11,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],3⟩,⟨[12,15,19],1⟩,⟨[14,16,19],1⟩,⟨[13,17,19],1⟩,⟨[11,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9205
namespace Case9205
def big : Finset (Finset (Fin 9)) := {{2,4,5},{1,3,6},{0,4,6},{1,2,7},{3,4,7},{1,4,8},{3,5,8},{2,6,8},{0,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{0,3},{2,3},{0,5},{1,5},{2,4,5},{1,3,6},{0,4,6},{5,6},{1,2,7},{3,4,7},{5,7},{6,7},{1,4,8},{3,5,8},{2,6,8},{0,7,8}]
end Case9205
namespace Case9206
def positionFn : Fin 9 → Fin 25 := ![16,17,18,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{1,2},{3},{4},{5},{0,5},{1,3,5},{2,4,5},{6},{0,3,6},{1,4,6},{5,6},{7},{2,3,7},{0,4,7},{5,7},{6,7},{8},{0,8},{3,4,8},{5,8},{2,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={5} then 1 else if T={0,5} then 1 else if T={1,3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 2 else if T={0,3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={2,3,7} then 1 else if T={0,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[17,18,19,20,21,22,23,24,25],[⟨[],3⟩,⟨[18],1⟩,⟨[17,18],1⟩,⟨[19],1⟩,⟨[17,19],1⟩,⟨[18,19],1⟩,⟨[20],2⟩,⟨[21],2⟩,⟨[22],1⟩,⟨[17,22],1⟩,⟨[18,20,22],1⟩,⟨[19,21,22],1⟩,⟨[23],2⟩,⟨[17,20,23],1⟩,⟨[18,21,23],1⟩,⟨[22,23],1⟩,⟨[24],2⟩,⟨[19,20,24],1⟩,⟨[17,21,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[25],2⟩,⟨[17,25],1⟩,⟨[20,21,25],1⟩,⟨[22,25],1⟩,⟨[19,23,25],1⟩,⟨[18,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9206
namespace Case9206
def big : Finset (Finset (Fin 9)) := {{1,3,5},{2,4,5},{0,3,6},{1,4,6},{2,3,7},{0,4,7},{3,4,8},{2,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{1,2},{0,5},{1,3,5},{2,4,5},{0,3,6},{1,4,6},{5,6},{2,3,7},{0,4,7},{5,7},{6,7},{0,8},{3,4,8},{5,8},{2,6,8},{1,7,8}]
end Case9206
namespace Case9207
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{3},{4},{1,3,4},{5},{0,5},{1,5},{2,3,5},{6},{1,2,6},{0,4,6},{5,6},{7},{0,3,7},{2,4,7},{5,7},{6,7},{8},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={1,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,3,5} then 1 else if T={6} then 2 else if T={1,2,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[15],2⟩,⟨[12,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[17],2⟩,⟨[12,13,17],1⟩,⟨[11,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,19],1⟩,⟨[15,16,19],1⟩,⟨[14,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9207
namespace Case9207
def big : Finset (Finset (Fin 9)) := {{1,3,4},{2,3,5},{1,2,6},{0,4,6},{0,3,7},{2,4,7},{4,5,8},{3,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{1,3,4},{0,5},{1,5},{2,3,5},{1,2,6},{0,4,6},{5,6},{0,3,7},{2,4,7},{5,7},{6,7},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]
end Case9207
namespace Case9208
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{2,3},{4},{1,4},{0,3,4},{5},{0,5},{1,5},{4,5},{6},{0,6},{2,6},{3,6},{5,6},{7},{1,3,7},{2,5,7},{4,6,7},{8},{2,4,8},{3,5,8},{1,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,3,7} then 1 else if T={2,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[11,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[12,14,18],1⟩,⟨[13,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],3⟩,⟨[13,15,19],1⟩,⟨[14,16,19],1⟩,⟨[12,17,19],1⟩,⟨[11,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9208
namespace Case9208
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,4},{1,3,7},{2,5,7},{4,6,7},{2,4,8},{3,5,8},{1,6,8},{0,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{2,3},{1,4},{0,3,4},{0,5},{1,5},{4,5},{0,6},{2,6},{3,6},{5,6},{1,3,7},{2,5,7},{4,6,7},{2,4,8},{3,5,8},{1,6,8},{0,7,8}]
end Case9208
namespace Case9209
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{3},{0,3},{4},{0,1,4},{5},{0,5},{3,5},{2,4,5},{6},{1,6},{2,6},{3,4,6},{5,6},{7},{0,2,7},{1,3,7},{5,7},{6,7},{8},{2,3,8},{1,5,8},{0,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,2,7} then 1 else if T={1,3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={2,3,8} then 1 else if T={1,5,8} then 1 else if T={0,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[13,15],1⟩,⟨[12,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,12,17],1⟩,⟨[11,13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[12,13,18],1⟩,⟨[11,15,18],1⟩,⟨[10,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9209
namespace Case9209
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,4,5},{3,4,6},{0,2,7},{1,3,7},{2,3,8},{1,5,8},{0,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,1,4},{0,5},{3,5},{2,4,5},{1,6},{2,6},{3,4,6},{5,6},{0,2,7},{1,3,7},{5,7},{6,7},{2,3,8},{1,5,8},{0,6,8},{4,7,8}]
end Case9209
namespace Case9210
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{2,3},{4},{5},{0,5},{1,5},{3,4,5},{6},{0,6},{2,6},{3,6},{1,4,6},{5,6},{7},{1,7},{0,3,7},{2,4,7},{5,7},{8},{1,3,8},{0,4,8},{2,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 3 else if T={1,3,8} then 1 else if T={0,4,8} then 1 else if T={2,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[11,14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[19],3⟩,⟨[12,14,19],1⟩,⟨[11,15,19],1⟩,⟨[13,16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9210
namespace Case9210
def big : Finset (Finset (Fin 9)) := {{0,1,2},{3,4,5},{1,4,6},{0,3,7},{2,4,7},{1,3,8},{0,4,8},{2,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{2,3},{0,5},{1,5},{3,4,5},{0,6},{2,6},{3,6},{1,4,6},{5,6},{1,7},{0,3,7},{2,4,7},{5,7},{1,3,8},{0,4,8},{2,5,8},{6,7,8}]
end Case9210
namespace Case9211
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{2,3},{4},{0,3,4},{5},{0,5},{1,5},{2,4,5},{6},{1,6},{2,6},{3,6},{5,6},{7},{0,7},{1,3,7},{5,7},{4,6,7},{8},{1,4,8},{3,5,8},{0,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,4,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={1,4,8} then 1 else if T={3,5,8} then 1 else if T={0,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[11,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,15,16],1⟩,⟨[17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],3⟩,⟨[12,15,19],1⟩,⟨[14,16,19],1⟩,⟨[11,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9211
namespace Case9211
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,4},{2,4,5},{1,3,7},{4,6,7},{1,4,8},{3,5,8},{0,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{2,3},{0,3,4},{0,5},{1,5},{2,4,5},{1,6},{2,6},{3,6},{5,6},{0,7},{1,3,7},{5,7},{4,6,7},{1,4,8},{3,5,8},{0,6,8},{2,7,8}]
end Case9211
namespace Case9212
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{3},{0,1,3},{4},{5},{0,5},{2,3,5},{1,4,5},{6},{1,6},{2,6},{0,4,6},{5,6},{7},{0,2,7},{3,4,7},{5,7},{6,7},{8},{0,8},{2,4,8},{5,8},{3,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,1,3} then 1 else if T={4} then 2 else if T={5} then 1 else if T={0,5} then 1 else if T={2,3,5} then 1 else if T={1,4,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[11,12,14],1⟩,⟨[15],2⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[13,14,16],1⟩,⟨[12,15,16],1⟩,⟨[17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[11,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,15,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9212
namespace Case9212
def big : Finset (Finset (Fin 9)) := {{0,1,3},{2,3,5},{1,4,5},{0,4,6},{0,2,7},{3,4,7},{2,4,8},{3,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,1,3},{0,5},{2,3,5},{1,4,5},{1,6},{2,6},{0,4,6},{5,6},{0,2,7},{3,4,7},{5,7},{6,7},{0,8},{2,4,8},{5,8},{3,6,8},{1,7,8}]
end Case9212
namespace Case9213
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{4},{0,3,4},{5},{0,5},{2,5},{1,3,5},{6},{0,6},{1,6},{2,4,6},{5,6},{7},{1,7},{2,3,7},{4,5,7},{6,7},{8},{2,8},{1,4,8},{5,8},{3,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={1,3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,3,7} then 1 else if T={4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={2,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],2⟩,⟨[15],2⟩,⟨[11,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[12,14,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[13,14,18],1⟩,⟨[15,16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[13,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[11,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9213
namespace Case9213
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,4},{1,3,5},{2,4,6},{2,3,7},{4,5,7},{1,4,8},{3,6,8},{0,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{0,3,4},{0,5},{2,5},{1,3,5},{0,6},{1,6},{2,4,6},{5,6},{1,7},{2,3,7},{4,5,7},{6,7},{2,8},{1,4,8},{5,8},{3,6,8},{0,7,8}]
end Case9213
namespace Case9214
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,3},{4},{2,3,4},{5},{1,5},{2,5},{0,4,5},{6},{0,6},{2,6},{1,4,6},{5,6},{7},{1,7},{0,2,7},{5,7},{3,6,7},{8},{0,8},{1,2,8},{3,5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 2 else if T={0,1,3} then 1 else if T={4} then 2 else if T={2,3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={0,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,2,7} then 1 else if T={5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={3,5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],2⟩,⟨[10,11,13],1⟩,⟨[14],2⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[10,14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[11,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[10,12,17],1⟩,⟨[15,17],1⟩,⟨[13,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,12,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9214
namespace Case9214
def big : Finset (Finset (Fin 9)) := {{0,1,3},{2,3,4},{0,4,5},{1,4,6},{0,2,7},{3,6,7},{1,2,8},{3,5,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,3},{2,3,4},{1,5},{2,5},{0,4,5},{0,6},{2,6},{1,4,6},{5,6},{1,7},{0,2,7},{5,7},{3,6,7},{0,8},{1,2,8},{3,5,8},{6,8},{4,7,8}]
end Case9214
namespace Case9215
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{3},{4},{0,3,4},{5},{0,5},{1,3,5},{2,4,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{0,1,7},{2,3,7},{5,7},{4,6,7},{8},{0,2,8},{1,4,8},{5,8},{3,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,1,7} then 1 else if T={2,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,2,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[10,13,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,13,15],1⟩,⟨[12,14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,11,17],1⟩,⟨[12,13,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,12,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[13,16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9215
namespace Case9215
def big : Finset (Finset (Fin 9)) := {{0,3,4},{1,3,5},{2,4,5},{0,1,7},{2,3,7},{4,6,7},{0,2,8},{1,4,8},{3,6,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3,4},{0,5},{1,3,5},{2,4,5},{0,6},{1,6},{2,6},{5,6},{0,1,7},{2,3,7},{5,7},{4,6,7},{0,2,8},{1,4,8},{5,8},{3,6,8},{7,8}]
end Case9215
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

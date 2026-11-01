import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case3264
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{1,3},{4},{0,4},{5},{1,5},{2,5},{4,5},{6},{0,1,2,6},{3,4,6},{5,6},{7},{1,7},{2,4,7},{0,3,5,7},{8},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={0,1,2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={0,3,5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],2⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[10,11,12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[12,14,17],1⟩,⟨[10,13,15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3264
namespace Case3264
def big : Finset (Finset (Fin 9)) := {{0,1,2,6},{3,4,6},{2,4,7},{0,3,5,7},{2,3,8},{1,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,4},{1,5},{2,5},{4,5},{0,1,2,6},{3,4,6},{5,6},{1,7},{2,4,7},{0,3,5,7},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
end Case3264
namespace Case3265
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{3},{0,3},{4},{0,4},{1,3,4},{5},{1,5},{3,5},{4,5},{6},{2,3,6},{5,6},{7},{2,4,7},{5,7},{0,1,6,7},{8},{1,8},{0,2,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={1} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={2,3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 3 else if T={1,8} then 1 else if T={0,2,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],2⟩,⟨[12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,14,15],1⟩,⟨[16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[13,14,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[11,12,17,18],1⟩,⟨[19],3⟩,⟨[12,19],1⟩,⟨[11,13,16,19],1⟩,⟨[15,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3265
namespace Case3265
def big : Finset (Finset (Fin 9)) := {{1,3,4},{2,3,6},{2,4,7},{0,1,6,7},{0,2,5,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,4},{1,3,4},{1,5},{3,5},{4,5},{2,3,6},{5,6},{2,4,7},{5,7},{0,1,6,7},{1,8},{0,2,5,8},{4,6,8},{3,7,8}]
end Case3265
namespace Case3266
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,2,3},{4},{0,4},{5},{1,5},{2,5},{3,5},{4,5},{6},{1,6},{2,4,6},{7},{1,7},{3,4,7},{0,5,6,7},{8},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={0,1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={2,4,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],2⟩,⟨[12],1⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[11,12,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[12,17],1⟩,⟨[13,15,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[14,15,18],1⟩,⟨[11,16,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3266
namespace Case3266
def big : Finset (Finset (Fin 9)) := {{0,1,2,3},{2,4,6},{3,4,7},{0,5,6,7},{1,4,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2,3},{0,4},{1,5},{2,5},{3,5},{4,5},{1,6},{2,4,6},{1,7},{3,4,7},{0,5,6,7},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]
end Case3266
namespace Case3267
def positionFn : Fin 9 → Fin 25 := ![8,9,10,11,12,13,14,15,16]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,3},{4},{0,4},{1,3,4},{5},{1,5},{2,5},{3,5},{4,5},{6},{1,6},{2,3,6},{7},{1,7},{2,4,7},{0,5,6,7},{8},{0,1,2,8},{5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={1} then 1 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 3 else if T={0,1,2,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,16,17],[⟨[],1⟩,⟨[9],2⟩,⟨[10],1⟩,⟨[11],2⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[10,12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],3⟩,⟨[10,15],1⟩,⟨[11,12,15],1⟩,⟨[16],3⟩,⟨[10,16],1⟩,⟨[11,13,16],1⟩,⟨[9,14,15,16],1⟩,⟨[17],3⟩,⟨[9,10,11,17],1⟩,⟨[14,17],1⟩,⟨[13,15,17],1⟩,⟨[12,16,17],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3267
namespace Case3267
def big : Finset (Finset (Fin 9)) := {{1,3,4},{2,3,6},{2,4,7},{0,5,6,7},{0,1,2,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{1,3,4},{1,5},{2,5},{3,5},{4,5},{1,6},{2,3,6},{1,7},{2,4,7},{0,5,6,7},{0,1,2,8},{5,8},{4,6,8},{3,7,8}]
end Case3267
namespace Case3268
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{5},{0,1,2,5},{3,5},{4,5},{6},{1,6},{2,6},{0,3,4,6},{5,6},{7},{0,7},{1,3,7},{2,4,7},{5,7},{8},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={4} then 2 else if T={5} then 1 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,6} then 1 else if T={0,3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[15],1⟩,⟨[10,11,12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[10,13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3268
namespace Case3268
def big : Finset (Finset (Fin 9)) := {{0,1,2,5},{0,3,4,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2,5},{3,5},{4,5},{1,6},{2,6},{0,3,4,6},{5,6},{0,7},{1,3,7},{2,4,7},{5,7},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
end Case3268
namespace Case3269
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,4},{1,2,4},{5},{1,5},{0,2,3,5},{4,5},{6},{2,6},{3,6},{5,6},{7},{3,4,7},{5,7},{0,1,6,7},{8},{0,8},{1,3,8},{5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={0,2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[10,12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[10,11,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,13,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3269
namespace Case3269
def big : Finset (Finset (Fin 9)) := {{1,2,4},{0,2,3,5},{3,4,7},{0,1,6,7},{1,3,8},{4,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,4},{1,2,4},{1,5},{0,2,3,5},{4,5},{2,6},{3,6},{5,6},{3,4,7},{5,7},{0,1,6,7},{0,8},{1,3,8},{5,8},{4,6,8},{2,7,8}]
end Case3269
namespace Case3270
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,3},{4},{0,4},{5},{0,1,2,5},{3,5},{4,5},{6},{1,6},{2,6},{3,4,6},{5,6},{7},{1,3,7},{2,4,7},{5,7},{8},{2,3,8},{1,4,8},{5,8},{0,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 3 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={0,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[15],1⟩,⟨[10,11,12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[11,13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[18],3⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[10,16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3270
namespace Case3270
def big : Finset (Finset (Fin 9)) := {{0,1,2,5},{3,4,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{0,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{0,1,2,5},{3,5},{4,5},{1,6},{2,6},{3,4,6},{5,6},{1,3,7},{2,4,7},{5,7},{2,3,8},{1,4,8},{5,8},{0,6,7,8}]
end Case3270
namespace Case3271
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,4},{1,2,4},{5},{2,5},{3,5},{4,5},{6},{1,6},{0,2,3,6},{5,6},{7},{3,4,7},{0,1,5,7},{6,7},{8},{0,8},{1,3,8},{5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,2,3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={3,4,7} then 1 else if T={0,1,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,12,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[10,12,13,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[13,14,17],1⟩,⟨[10,11,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,13,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3271
namespace Case3271
def big : Finset (Finset (Fin 9)) := {{1,2,4},{0,2,3,6},{3,4,7},{0,1,5,7},{1,3,8},{4,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,4},{1,2,4},{2,5},{3,5},{4,5},{1,6},{0,2,3,6},{5,6},{3,4,7},{0,1,5,7},{6,7},{0,8},{1,3,8},{5,8},{4,6,8},{2,7,8}]
end Case3271
namespace Case3272
def positionFn : Fin 9 → Fin 25 := ![16,17,18,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,3},{1,2,3},{4},{0,4},{5},{2,5},{3,5},{4,5},{6},{1,6},{3,4,6},{5,6},{7},{2,4,7},{0,1,5,7},{6,7},{8},{1,4,8},{5,8},{0,2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={2,4,7} then 1 else if T={0,1,5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={0,2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[17,18,19,20,21,22,23,24,25],[⟨[],1⟩,⟨[17],2⟩,⟨[18],2⟩,⟨[19],2⟩,⟨[20],1⟩,⟨[17,20],1⟩,⟨[18,19,20],1⟩,⟨[21],1⟩,⟨[17,21],1⟩,⟨[22],1⟩,⟨[19,22],1⟩,⟨[20,22],1⟩,⟨[21,22],1⟩,⟨[23],2⟩,⟨[18,23],1⟩,⟨[20,21,23],1⟩,⟨[22,23],1⟩,⟨[24],3⟩,⟨[19,21,24],1⟩,⟨[17,18,22,24],1⟩,⟨[23,24],1⟩,⟨[25],3⟩,⟨[18,21,25],1⟩,⟨[22,25],1⟩,⟨[17,19,23,25],1⟩,⟨[20,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3272
namespace Case3272
def big : Finset (Finset (Fin 9)) := {{1,2,3},{3,4,6},{2,4,7},{0,1,5,7},{1,4,8},{0,2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,2,3},{0,4},{2,5},{3,5},{4,5},{1,6},{3,4,6},{5,6},{2,4,7},{0,1,5,7},{6,7},{1,4,8},{5,8},{0,2,6,8},{3,7,8}]
end Case3272
namespace Case3273
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,3},{4},{0,4},{5},{1,5},{2,5},{3,5},{4,5},{6},{0,1,2,6},{3,4,6},{5,6},{7},{1,3,7},{2,4,7},{6,7},{8},{2,3,8},{1,4,8},{6,8},{0,5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={6,8} then 1 else if T={0,5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,11,12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[11,13,17],1⟩,⟨[12,14,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[16,18],1⟩,⟨[10,15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3273
namespace Case3273
def big : Finset (Finset (Fin 9)) := {{0,1,2,6},{3,4,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{0,5,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{1,5},{2,5},{3,5},{4,5},{0,1,2,6},{3,4,6},{5,6},{1,3,7},{2,4,7},{6,7},{2,3,8},{1,4,8},{6,8},{0,5,7,8}]
end Case3273
namespace Case3274
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,3},{4},{0,4},{5},{0,5},{1,5},{2,5},{6},{0,1,2,6},{3,4,5,6},{7},{1,3,7},{2,4,7},{5,7},{6,7},{8},{2,3,8},{1,4,8},{5,8},{6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 3 else if T={0,1,2,6} then 1 else if T={3,4,5,6} then 1 else if T={7} then 2 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[10,13],1⟩,⟨[14],2⟩,⟨[10,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],3⟩,⟨[10,11,12,16],1⟩,⟨[13,14,15,16],1⟩,⟨[17],2⟩,⟨[11,13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[10,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3274
namespace Case3274
def big : Finset (Finset (Fin 9)) := {{0,1,2,6},{3,4,5,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{0,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{0,5},{1,5},{2,5},{0,1,2,6},{3,4,5,6},{1,3,7},{2,4,7},{5,7},{6,7},{2,3,8},{1,4,8},{5,8},{6,8},{0,7,8}]
end Case3274
namespace Case3275
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{3},{0,3},{4},{1,2,4},{5},{0,5},{1,5},{4,5},{6},{4,6},{2,3,5,6},{7},{3,4,7},{5,7},{0,1,6,7},{8},{1,3,8},{0,4,8},{5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 1 else if T={1,2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={4,6} then 1 else if T={2,3,5,6} then 1 else if T={7} then 3 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={1,3,8} then 1 else if T={0,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[12,13,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[15,17],1⟩,⟨[13,14,16,17],1⟩,⟨[18],3⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[11,12,17,18],1⟩,⟨[19],2⟩,⟨[12,14,19],1⟩,⟨[11,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3275
namespace Case3275
def big : Finset (Finset (Fin 9)) := {{1,2,4},{2,3,5,6},{3,4,7},{0,1,6,7},{1,3,8},{0,4,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{1,2,4},{0,5},{1,5},{4,5},{4,6},{2,3,5,6},{3,4,7},{5,7},{0,1,6,7},{1,3,8},{0,4,8},{5,8},{6,8},{2,7,8}]
end Case3275
namespace Case3276
def positionFn : Fin 9 → Fin 25 := ![16,17,18,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{0,2},{3},{4},{0,3,4},{5},{0,5},{3,5},{4,5},{6},{3,6},{4,6},{1,2,5,6},{7},{1,3,7},{2,4,7},{5,7},{8},{2,3,8},{1,4,8},{5,8},{0,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 1 else if T={4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={3,6} then 1 else if T={4,6} then 1 else if T={1,2,5,6} then 1 else if T={7} then 3 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 3 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={0,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[17,18,19,20,21,22,23,24,25],[⟨[],1⟩,⟨[17],1⟩,⟨[18],2⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[17,19],1⟩,⟨[20],1⟩,⟨[21],1⟩,⟨[17,20,21],1⟩,⟨[22],1⟩,⟨[17,22],1⟩,⟨[20,22],1⟩,⟨[21,22],1⟩,⟨[23],3⟩,⟨[20,23],1⟩,⟨[21,23],1⟩,⟨[18,19,22,23],1⟩,⟨[24],3⟩,⟨[18,20,24],1⟩,⟨[19,21,24],1⟩,⟨[22,24],1⟩,⟨[25],3⟩,⟨[19,20,25],1⟩,⟨[18,21,25],1⟩,⟨[22,25],1⟩,⟨[17,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3276
namespace Case3276
def big : Finset (Finset (Fin 9)) := {{0,3,4},{1,2,5,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{0,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{0,3,4},{0,5},{3,5},{4,5},{3,6},{4,6},{1,2,5,6},{1,3,7},{2,4,7},{5,7},{2,3,8},{1,4,8},{5,8},{0,6,7,8}]
end Case3276
namespace Case3277
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{3},{4},{1,2,4},{5},{0,5},{2,5},{3,5},{4,5},{6},{0,2,3,6},{4,6},{7},{0,7},{3,4,7},{1,5,6,7},{8},{1,3,8},{0,4,8},{5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={4} then 1 else if T={1,2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={0,2,3,6} then 1 else if T={4,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={1,5,6,7} then 1 else if T={8} then 2 else if T={1,3,8} then 1 else if T={0,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],2⟩,⟨[10,11],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[11,12,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[10,12,13,16],1⟩,⟨[14,16],1⟩,⟨[17],3⟩,⟨[10,17],1⟩,⟨[13,14,17],1⟩,⟨[11,15,16,17],1⟩,⟨[18],2⟩,⟨[11,13,18],1⟩,⟨[10,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3277
namespace Case3277
def big : Finset (Finset (Fin 9)) := {{1,2,4},{0,2,3,6},{3,4,7},{1,5,6,7},{1,3,8},{0,4,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2,4},{0,5},{2,5},{3,5},{4,5},{0,2,3,6},{4,6},{0,7},{3,4,7},{1,5,6,7},{1,3,8},{0,4,8},{5,8},{6,8},{2,7,8}]
end Case3277
namespace Case3278
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{3},{1,2,3},{4},{0,3,4},{5},{0,5},{1,5},{3,5},{4,5},{6},{3,6},{4,6},{7},{2,4,7},{5,7},{0,1,6,7},{8},{0,8},{1,4,8},{2,5,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={3,6} then 1 else if T={4,6} then 1 else if T={7} then 3 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={2,5,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[11,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[18],3⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[11,12,17,18],1⟩,⟨[19],3⟩,⟨[11,19],1⟩,⟨[12,15,19],1⟩,⟨[13,16,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3278
namespace Case3278
def big : Finset (Finset (Fin 9)) := {{1,2,3},{0,3,4},{2,4,7},{0,1,6,7},{1,4,8},{2,5,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2,3},{0,3,4},{0,5},{1,5},{3,5},{4,5},{3,6},{4,6},{2,4,7},{5,7},{0,1,6,7},{0,8},{1,4,8},{2,5,6,8},{3,7,8}]
end Case3278
namespace Case3279
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,3,4},{5},{0,5},{1,5},{2,5},{3,5},{4,5},{6},{0,1,2,6},{3,6},{4,6},{7},{0,7},{1,3,7},{2,4,7},{8},{0,8},{2,3,8},{1,4,8},{5,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={0,1,2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[15],1⟩,⟨[11,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[11,12,13,17],1⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[18],3⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[13,15,18],1⟩,⟨[19],3⟩,⟨[11,19],1⟩,⟨[13,14,19],1⟩,⟨[12,15,19],1⟩,⟨[16,17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3279
namespace Case3279
def big : Finset (Finset (Fin 9)) := {{0,3,4},{0,1,2,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{5,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,3,4},{0,5},{1,5},{2,5},{3,5},{4,5},{0,1,2,6},{3,6},{4,6},{0,7},{1,3,7},{2,4,7},{0,8},{2,3,8},{1,4,8},{5,6,7,8}]
end Case3279
namespace Case3280
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,2,4},{1,3,4},{5},{2,5},{3,5},{4,5},{6},{4,6},{0,1,5,6},{7},{0,7},{1,7},{5,7},{2,3,6,7},{8},{1,2,8},{0,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={4} then 1 else if T={0,2,4} then 1 else if T={1,3,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={4,6} then 1 else if T={0,1,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={5,7} then 1 else if T={2,3,6,7} then 1 else if T={8} then 2 else if T={1,2,8} then 1 else if T={0,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[15],1⟩,⟨[11,13,15],1⟩,⟨[12,14,15],1⟩,⟨[16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[15,17],1⟩,⟨[11,12,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[16,18],1⟩,⟨[13,14,17,18],1⟩,⟨[19],2⟩,⟨[12,13,19],1⟩,⟨[11,14,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3280
namespace Case3280
def big : Finset (Finset (Fin 9)) := {{0,2,4},{1,3,4},{0,1,5,6},{2,3,6,7},{1,2,8},{0,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,2,4},{1,3,4},{2,5},{3,5},{4,5},{4,6},{0,1,5,6},{0,7},{1,7},{5,7},{2,3,6,7},{1,2,8},{0,3,8},{5,8},{6,8},{4,7,8}]
end Case3280
namespace Case3281
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,3},{4},{0,2,4},{5},{0,5},{3,5},{4,5},{6},{3,6},{4,6},{1,2,5,6},{7},{1,7},{2,7},{3,4,7},{5,7},{8},{2,3,8},{1,4,8},{5,8},{0,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={0,1,3} then 1 else if T={4} then 1 else if T={0,2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={3,6} then 1 else if T={4,6} then 1 else if T={1,2,5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 3 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={0,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[10,11,13],1⟩,⟨[14],1⟩,⟨[10,12,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[11,12,15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[18],3⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[10,16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3281
namespace Case3281
def big : Finset (Finset (Fin 9)) := {{0,1,3},{0,2,4},{1,2,5,6},{3,4,7},{2,3,8},{1,4,8},{0,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,3},{0,2,4},{0,5},{3,5},{4,5},{3,6},{4,6},{1,2,5,6},{1,7},{2,7},{3,4,7},{5,7},{2,3,8},{1,4,8},{5,8},{0,6,7,8}]
end Case3281
namespace Case3282
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,3},{4},{0,2,4},{5},{1,5},{2,5},{3,5},{4,5},{6},{3,6},{4,6},{7},{0,7},{3,4,7},{5,7},{1,2,6,7},{8},{2,3,8},{1,4,8},{0,5,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={0,1,3} then 1 else if T={4} then 1 else if T={0,2,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={3,6} then 1 else if T={4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={1,2,6,7} then 1 else if T={8} then 3 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={0,5,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[10,11,13],1⟩,⟨[14],1⟩,⟨[10,12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[11,12,16,17],1⟩,⟨[18],3⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[10,15,16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3282
namespace Case3282
def big : Finset (Finset (Fin 9)) := {{0,1,3},{0,2,4},{3,4,7},{1,2,6,7},{2,3,8},{1,4,8},{0,5,6,8}}
def full : List (Finset (Fin 9)) := [{0,1,3},{0,2,4},{1,5},{2,5},{3,5},{4,5},{3,6},{4,6},{0,7},{3,4,7},{5,7},{1,2,6,7},{2,3,8},{1,4,8},{0,5,6,8},{7,8}]
end Case3282
namespace Case3283
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{2,3},{4},{2,4},{0,1,3,4},{5},{0,5},{2,5},{6},{0,6},{1,6},{3,5,6},{7},{0,7},{1,7},{4,5,7},{2,6,7},{8},{0,2,8},{1,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={0,1,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={2,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={4,5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 3 else if T={0,2,8} then 1 else if T={1,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[13,15],1⟩,⟨[11,12,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[15,16,18],1⟩,⟨[13,17,18],1⟩,⟨[19],3⟩,⟨[11,13,19],1⟩,⟨[12,16,19],1⟩,⟨[15,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3283
namespace Case3283
def big : Finset (Finset (Fin 9)) := {{0,1,3,4},{3,5,6},{4,5,7},{2,6,7},{0,2,8},{1,5,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{2,3},{2,4},{0,1,3,4},{0,5},{2,5},{0,6},{1,6},{3,5,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,2,8},{1,5,8},{4,6,8},{3,7,8}]
end Case3283
namespace Case3284
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{2,3},{4},{0,4},{2,4},{5},{2,5},{0,1,3,5},{6},{0,6},{1,6},{3,4,6},{7},{0,7},{1,7},{4,5,7},{2,6,7},{8},{0,2,8},{1,4,8},{5,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={0,1,3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={4,5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 3 else if T={0,2,8} then 1 else if T={1,4,8} then 1 else if T={5,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[10,11,13,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[13,14,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[14,15,17],1⟩,⟨[12,16,17],1⟩,⟨[18],3⟩,⟨[10,12,18],1⟩,⟨[11,14,18],1⟩,⟨[15,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3284
namespace Case3284
def big : Finset (Finset (Fin 9)) := {{0,1,3,5},{3,4,6},{4,5,7},{2,6,7},{0,2,8},{1,4,8},{5,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{2,3},{0,4},{2,4},{2,5},{0,1,3,5},{0,6},{1,6},{3,4,6},{0,7},{1,7},{4,5,7},{2,6,7},{0,2,8},{1,4,8},{5,6,8},{3,7,8}]
end Case3284
namespace Case3285
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{2,3},{4},{0,4},{1,4},{5},{2,5},{0,1,3,5},{6},{0,6},{2,6},{3,4,6},{7},{0,7},{1,7},{2,4,7},{5,6,7},{8},{0,2,8},{4,5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={0,1,3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 3 else if T={0,2,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[10,11,13,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,14,17],1⟩,⟨[15,16,17],1⟩,⟨[18],3⟩,⟨[10,12,18],1⟩,⟨[14,15,18],1⟩,⟨[11,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3285
namespace Case3285
def big : Finset (Finset (Fin 9)) := {{0,1,3,5},{3,4,6},{2,4,7},{5,6,7},{0,2,8},{4,5,8},{1,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{2,3},{0,4},{1,4},{2,5},{0,1,3,5},{0,6},{2,6},{3,4,6},{0,7},{1,7},{2,4,7},{5,6,7},{0,2,8},{4,5,8},{1,6,8},{3,7,8}]
end Case3285
namespace Case3286
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{2,3},{4},{0,4},{1,4},{5},{2,5},{0,1,3,5},{6},{0,6},{2,6},{4,5,6},{7},{0,7},{1,7},{2,4,7},{3,6,7},{8},{0,2,8},{3,4,8},{1,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={0,1,3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={3,6,7} then 1 else if T={8} then 3 else if T={0,2,8} then 1 else if T={3,4,8} then 1 else if T={1,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[10,11,13,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[14,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,14,17],1⟩,⟨[13,16,17],1⟩,⟨[18],3⟩,⟨[10,12,18],1⟩,⟨[13,14,18],1⟩,⟨[11,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3286
namespace Case3286
def big : Finset (Finset (Fin 9)) := {{0,1,3,5},{4,5,6},{2,4,7},{3,6,7},{0,2,8},{3,4,8},{1,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{2,3},{0,4},{1,4},{2,5},{0,1,3,5},{0,6},{2,6},{4,5,6},{0,7},{1,7},{2,4,7},{3,6,7},{0,2,8},{3,4,8},{1,6,8},{5,7,8}]
end Case3286
namespace Case3287
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{2,3},{4},{0,2,4},{5},{2,5},{0,1,3,5},{6},{0,6},{2,6},{1,4,6},{7},{0,7},{1,7},{3,4,7},{5,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 2 else if T={0,2,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={0,1,3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[10,12,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[10,11,13,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[11,14,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,14,17],1⟩,⟨[15,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[14,15,18],1⟩,⟨[13,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3287
namespace Case3287
def big : Finset (Finset (Fin 9)) := {{0,2,4},{0,1,3,5},{1,4,6},{3,4,7},{5,6,7},{4,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{2,3},{0,2,4},{2,5},{0,1,3,5},{0,6},{2,6},{1,4,6},{0,7},{1,7},{3,4,7},{5,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
end Case3287
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

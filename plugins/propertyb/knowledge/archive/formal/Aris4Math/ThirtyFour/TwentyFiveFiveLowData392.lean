import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case9408
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,2},{1,2},{0,3},{1,3},{4},{0,4},{0,5},{1,5},{2,5},{3,5},{4,5},{6},{3,6},{2,4,6},{5,6},{7},{2,7},{3,4,7},{0,1,6,7},{8},{0,8},{2,3,8},{1,4,8},{6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[14,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[13,18],1⟩,⟨[14,15,18],1⟩,⟨[11,12,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,14,19],1⟩,⟨[12,15,19],1⟩,⟨[17,19],1⟩,⟨[16,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9408
namespace Case9408
def big : Finset (Finset (Fin 9)) := {{2,4,6},{3,4,7},{0,1,6,7},{2,3,8},{1,4,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{0,4},{0,5},{1,5},{2,5},{3,5},{4,5},{3,6},{2,4,6},{5,6},{2,7},{3,4,7},{0,1,6,7},{0,8},{2,3,8},{1,4,8},{6,8},{5,7,8}]
end Case9408
namespace Case9409
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,2},{1,2},{3},{2,3},{4},{0,4},{0,5},{1,5},{2,5},{3,4,5},{6},{0,1,3,6},{4,6},{5,6},{7},{0,7},{1,7},{2,4,7},{5,7},{6,7},{8},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={0,1,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,15,16],1⟩,⟨[17],2⟩,⟨[11,12,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[13,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9409
namespace Case9409
def big : Finset (Finset (Fin 9)) := {{3,4,5},{0,1,3,6},{2,4,7},{1,4,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{2,3},{0,4},{0,5},{1,5},{2,5},{3,4,5},{0,1,3,6},{4,6},{5,6},{0,7},{1,7},{2,4,7},{5,7},{6,7},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
end Case9409
namespace Case9410
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,2},{1,2},{3},{2,3},{4},{0,4},{0,5},{1,5},{2,5},{4,5},{6},{0,1,3,6},{2,4,6},{5,6},{7},{0,7},{1,7},{3,4,7},{5,7},{6,7},{8},{0,8},{1,4,8},{3,5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,1,3,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={3,5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,12,14,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,15,19],1⟩,⟨[14,16,19],1⟩,⟨[17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9410
namespace Case9410
def big : Finset (Finset (Fin 9)) := {{0,1,3,6},{2,4,6},{3,4,7},{1,4,8},{3,5,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{2,3},{0,4},{0,5},{1,5},{2,5},{4,5},{0,1,3,6},{2,4,6},{5,6},{0,7},{1,7},{3,4,7},{5,7},{6,7},{0,8},{1,4,8},{3,5,8},{6,8},{2,7,8}]
end Case9410
namespace Case9411
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,2},{1,2},{3},{0,3},{4},{0,4},{1,3,4},{0,5},{1,5},{2,5},{3,5},{6},{2,3,6},{4,6},{5,6},{7},{0,7},{1,7},{2,4,7},{5,7},{6,7},{8},{2,8},{4,5,8},{0,1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={2,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={2,8} then 1 else if T={4,5,8} then 1 else if T={0,1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,14,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],3⟩,⟨[13,19],1⟩,⟨[15,16,19],1⟩,⟨[11,12,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9411
namespace Case9411
def big : Finset (Finset (Fin 9)) := {{1,3,4},{2,3,6},{2,4,7},{4,5,8},{0,1,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{0,4},{1,3,4},{0,5},{1,5},{2,5},{3,5},{2,3,6},{4,6},{5,6},{0,7},{1,7},{2,4,7},{5,7},{6,7},{2,8},{4,5,8},{0,1,6,8},{3,7,8}]
end Case9411
namespace Case9412
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,2},{1,2},{3},{4},{0,4},{0,5},{1,5},{2,5},{3,4,5},{6},{2,6},{0,1,3,6},{4,6},{5,6},{7},{0,7},{1,7},{3,7},{2,4,7},{5,7},{8},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={0,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,1,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[11],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[10,11,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9412
namespace Case9412
def big : Finset (Finset (Fin 9)) := {{3,4,5},{0,1,3,6},{2,4,7},{2,3,8},{1,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,4},{0,5},{1,5},{2,5},{3,4,5},{2,6},{0,1,3,6},{4,6},{5,6},{0,7},{1,7},{3,7},{2,4,7},{5,7},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
end Case9412
namespace Case9413
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,2},{1,2},{3},{4},{0,4},{2,3,4},{0,5},{1,5},{2,5},{4,5},{6},{2,6},{0,1,3,6},{5,6},{7},{0,7},{1,7},{3,7},{5,7},{4,6,7},{8},{0,8},{1,4,8},{3,5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={0,4} then 1 else if T={2,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,1,3,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={3,5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[11],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,13,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[10,11,13,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9413
namespace Case9413
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,1,3,6},{4,6,7},{1,4,8},{3,5,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,4},{2,3,4},{0,5},{1,5},{2,5},{4,5},{2,6},{0,1,3,6},{5,6},{0,7},{1,7},{3,7},{5,7},{4,6,7},{0,8},{1,4,8},{3,5,8},{6,8},{2,7,8}]
end Case9413
namespace Case9414
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,2},{1,2},{3},{0,3},{4},{0,4},{1,3,4},{0,5},{1,5},{2,5},{4,5},{6},{2,6},{3,6},{5,6},{7},{0,7},{1,7},{2,3,7},{5,7},{4,6,7},{8},{2,4,8},{3,5,8},{0,1,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={0,1,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,14,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,14,18],1⟩,⟨[16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],3⟩,⟨[13,15,19],1⟩,⟨[14,16,19],1⟩,⟨[11,12,17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9414
namespace Case9414
def big : Finset (Finset (Fin 9)) := {{1,3,4},{2,3,7},{4,6,7},{2,4,8},{3,5,8},{0,1,6,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{0,4},{1,3,4},{0,5},{1,5},{2,5},{4,5},{2,6},{3,6},{5,6},{0,7},{1,7},{2,3,7},{5,7},{4,6,7},{2,4,8},{3,5,8},{0,1,6,8},{7,8}]
end Case9414
namespace Case9415
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,3},{4},{0,4},{1,3,4},{0,5},{1,5},{2,3,5},{4,5},{6},{0,1,2,6},{3,6},{5,6},{7},{0,7},{1,7},{2,4,7},{5,7},{6,7},{8},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,13,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,11,12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9415
namespace Case9415
def big : Finset (Finset (Fin 9)) := {{1,3,4},{2,3,5},{0,1,2,6},{2,4,7},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{1,3,4},{0,5},{1,5},{2,3,5},{4,5},{0,1,2,6},{3,6},{5,6},{0,7},{1,7},{2,4,7},{5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]
end Case9415
namespace Case9416
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{0,2},{3},{2,3},{4},{0,4},{1,2,4},{0,5},{1,5},{2,5},{3,4,5},{6},{1,6},{4,6},{5,6},{7},{1,7},{2,7},{5,7},{0,3,6,7},{8},{0,8},{1,3,8},{5,8},{2,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,1} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={0,3,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10,11],1⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,12,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[10,13,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,13,18],1⟩,⟨[15,18],1⟩,⟨[12,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9416
namespace Case9416
def big : Finset (Finset (Fin 9)) := {{1,2,4},{3,4,5},{0,3,6,7},{1,3,8},{2,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{2,3},{0,4},{1,2,4},{0,5},{1,5},{2,5},{3,4,5},{1,6},{4,6},{5,6},{1,7},{2,7},{5,7},{0,3,6,7},{0,8},{1,3,8},{5,8},{2,6,8},{4,7,8}]
end Case9416
namespace Case9417
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{0,2},{3},{2,3},{4},{0,4},{1,3,4},{0,5},{1,5},{2,5},{4,5},{6},{1,6},{2,4,6},{5,6},{7},{1,7},{2,7},{5,7},{0,3,6,7},{8},{0,8},{1,2,8},{3,5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,1} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={0,3,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={3,5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10,11],1⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,13,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[10,13,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,12,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9417
namespace Case9417
def big : Finset (Finset (Fin 9)) := {{1,3,4},{2,4,6},{0,3,6,7},{1,2,8},{3,5,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{2,3},{0,4},{1,3,4},{0,5},{1,5},{2,5},{4,5},{1,6},{2,4,6},{5,6},{1,7},{2,7},{5,7},{0,3,6,7},{0,8},{1,2,8},{3,5,8},{6,8},{4,7,8}]
end Case9417
namespace Case9418
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{0,2},{3},{0,3},{1,2,3},{4},{0,4},{0,5},{1,5},{2,5},{4,5},{6},{2,6},{3,6},{1,4,6},{5,6},{7},{1,7},{2,7},{3,4,7},{5,7},{8},{1,8},{2,4,8},{3,5,8},{0,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,1} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 3 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={0,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11,12],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[19],3⟩,⟨[12,19],1⟩,⟨[13,15,19],1⟩,⟨[14,16,19],1⟩,⟨[11,17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9418
namespace Case9418
def big : Finset (Finset (Fin 9)) := {{1,2,3},{1,4,6},{3,4,7},{2,4,8},{3,5,8},{0,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{0,3},{1,2,3},{0,4},{0,5},{1,5},{2,5},{4,5},{2,6},{3,6},{1,4,6},{5,6},{1,7},{2,7},{3,4,7},{5,7},{1,8},{2,4,8},{3,5,8},{0,6,7,8}]
end Case9418
namespace Case9419
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{1,2},{3},{0,3},{4},{0,4},{0,5},{1,5},{3,5},{2,4,5},{6},{1,3,6},{4,6},{5,6},{7},{1,7},{3,4,7},{5,7},{0,2,6,7},{8},{0,8},{2,3,8},{1,4,8},{5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,1} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 2 else if T={1,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[13,15,16],1⟩,⟨[17],2⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[11,13,17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[13,14,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9419
namespace Case9419
def big : Finset (Finset (Fin 9)) := {{2,4,5},{1,3,6},{3,4,7},{0,2,6,7},{2,3,8},{1,4,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{0,3},{0,4},{0,5},{1,5},{3,5},{2,4,5},{1,3,6},{4,6},{5,6},{1,7},{3,4,7},{5,7},{0,2,6,7},{0,8},{2,3,8},{1,4,8},{5,8},{6,8},{7,8}]
end Case9419
namespace Case9420
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{3},{0,3},{1,2,3},{4},{0,4},{0,5},{1,5},{3,5},{2,4,5},{6},{1,6},{3,4,6},{5,6},{7},{1,7},{4,7},{5,7},{0,2,6,7},{8},{0,8},{2,8},{1,4,8},{5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[13,15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[11,13,17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[13,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9420
namespace Case9420
def big : Finset (Finset (Fin 9)) := {{1,2,3},{2,4,5},{3,4,6},{0,2,6,7},{1,4,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,3},{1,2,3},{0,4},{0,5},{1,5},{3,5},{2,4,5},{1,6},{3,4,6},{5,6},{1,7},{4,7},{5,7},{0,2,6,7},{0,8},{2,8},{1,4,8},{5,8},{6,8},{3,7,8}]
end Case9420
namespace Case9421
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{1,3},{4},{2,4},{5},{2,5},{3,5},{0,1,4,5},{0,6},{1,6},{2,6},{3,6},{5,6},{7},{0,2,7},{3,4,7},{5,7},{6,7},{8},{0,8},{2,3,8},{5,8},{4,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,1,4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[10,11,14,15],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,13,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9421
namespace Case9421
def big : Finset (Finset (Fin 9)) := {{0,1,4,5},{0,2,7},{3,4,7},{2,3,8},{4,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{2,4},{2,5},{3,5},{0,1,4,5},{0,6},{1,6},{2,6},{3,6},{5,6},{0,2,7},{3,4,7},{5,7},{6,7},{0,8},{2,3,8},{5,8},{4,6,8},{1,7,8}]
end Case9421
namespace Case9422
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{1,3},{4},{0,4},{2,3,4},{5},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{5,6},{7},{2,7},{0,1,5,7},{4,6,7},{8},{0,2,8},{1,4,8},{5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,3,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={2,7} then 1 else if T={0,1,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,2,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[13,18],1⟩,⟨[11,12,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,13,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9422
namespace Case9422
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,1,5,7},{4,6,7},{0,2,8},{1,4,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{0,4},{2,3,4},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{5,6},{2,7},{0,1,5,7},{4,6,7},{0,2,8},{1,4,8},{5,8},{6,8},{3,7,8}]
end Case9422
namespace Case9423
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{1,3},{4},{0,2,4},{5},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{4,6},{5,6},{7},{2,7},{3,4,7},{0,1,5,7},{8},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,2,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={0,1,5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,13,15],1⟩,⟨[16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[13,18],1⟩,⟨[14,15,18],1⟩,⟨[11,12,16,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,14,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9423
namespace Case9423
def big : Finset (Finset (Fin 9)) := {{0,2,4},{3,4,7},{0,1,5,7},{2,3,8},{1,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{0,2,4},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{4,6},{5,6},{2,7},{3,4,7},{0,1,5,7},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
end Case9423
namespace Case9424
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{2,3},{4},{0,4},{5},{2,5},{0,1,3,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{7},{0,7},{1,7},{2,4,7},{5,7},{6,7},{8},{0,2,8},{1,4,8},{5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={0,1,3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,2,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[10,11,13,15],1⟩,⟨[14,15],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,12,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9424
namespace Case9424
def big : Finset (Finset (Fin 9)) := {{0,1,3,5},{3,4,6},{2,4,7},{0,2,8},{1,4,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{2,3},{0,4},{2,5},{0,1,3,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{0,7},{1,7},{2,4,7},{5,7},{6,7},{0,2,8},{1,4,8},{5,8},{6,8},{3,7,8}]
end Case9424
namespace Case9425
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{2,3},{4},{0,2,4},{5},{2,5},{0,1,3,5},{4,5},{0,6},{1,6},{2,6},{4,6},{5,6},{7},{0,7},{1,7},{3,4,7},{5,7},{6,7},{8},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,2,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={0,1,3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,12,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[10,11,13,15],1⟩,⟨[14,15],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[13,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9425
namespace Case9425
def big : Finset (Finset (Fin 9)) := {{0,2,4},{0,1,3,5},{3,4,7},{1,4,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{2,3},{0,2,4},{2,5},{0,1,3,5},{4,5},{0,6},{1,6},{2,6},{4,6},{5,6},{0,7},{1,7},{3,4,7},{5,7},{6,7},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]
end Case9425
namespace Case9426
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{0,2,3},{4},{0,4},{1,3,4},{5},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{5,6},{7},{0,7},{1,7},{2,4,7},{5,7},{6,7},{8},{2,8},{0,1,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={2,8} then 1 else if T={0,1,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,14,15],1⟩,⟨[16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],3⟩,⟨[13,19],1⟩,⟨[11,12,16,19],1⟩,⟨[15,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9426
namespace Case9426
def big : Finset (Finset (Fin 9)) := {{0,2,3},{1,3,4},{2,4,7},{0,1,5,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,2,3},{0,4},{1,3,4},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{5,6},{0,7},{1,7},{2,4,7},{5,7},{6,7},{2,8},{0,1,5,8},{4,6,8},{3,7,8}]
end Case9426
namespace Case9427
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{3},{4},{1,4},{5},{2,5},{0,1,3,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{7},{0,7},{3,7},{2,4,7},{5,7},{6,7},{8},{2,3,8},{0,4,8},{5,8},{6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={0,1,3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={2,3,8} then 1 else if T={0,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[10,11,13,15],1⟩,⟨[14,15],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,13,18],1⟩,⟨[10,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9427
namespace Case9427
def big : Finset (Finset (Fin 9)) := {{0,1,3,5},{3,4,6},{2,4,7},{2,3,8},{0,4,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,4},{2,5},{0,1,3,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{0,7},{3,7},{2,4,7},{5,7},{6,7},{2,3,8},{0,4,8},{5,8},{6,8},{1,7,8}]
end Case9427
namespace Case9428
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{3},{4},{2,3,4},{5},{2,5},{0,1,3,5},{4,5},{0,6},{1,6},{2,6},{4,6},{5,6},{7},{1,7},{3,7},{0,4,7},{5,7},{6,7},{8},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={2,3,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={0,1,3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={0,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[10,11,13,15],1⟩,⟨[14,15],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[10,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[13,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9428
namespace Case9428
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,1,3,5},{0,4,7},{1,4,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{2,3,4},{2,5},{0,1,3,5},{4,5},{0,6},{1,6},{2,6},{4,6},{5,6},{1,7},{3,7},{0,4,7},{5,7},{6,7},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]
end Case9428
namespace Case9429
def positionFn : Fin 9 → Fin 25 := ![20,10,12,11,13,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{3},{4},{1,4},{0,3,4},{5},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{5,6},{7},{0,7},{1,3,7},{2,4,7},{5,7},{6,7},{8},{2,3,8},{0,1,5,8},{4,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={2,3,8} then 1 else if T={0,1,5,8} then 1 else if T={4,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,21,22,23,24,25],[⟨[],4⟩,⟨[21],1⟩,⟨[11],1⟩,⟨[13,21],1⟩,⟨[11,13],1⟩,⟨[12],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,14,21],1⟩,⟨[22],1⟩,⟨[13,22],1⟩,⟨[12,22],1⟩,⟨[14,22],1⟩,⟨[21,23],1⟩,⟨[11,23],1⟩,⟨[13,23],1⟩,⟨[12,23],1⟩,⟨[22,23],1⟩,⟨[24],1⟩,⟨[21,24],1⟩,⟨[11,12,24],1⟩,⟨[13,14,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[25],3⟩,⟨[12,13,25],1⟩,⟨[11,21,22,25],1⟩,⟨[14,23,25],1⟩,⟨[24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9429
namespace Case9429
def big : Finset (Finset (Fin 9)) := {{0,3,4},{1,3,7},{2,4,7},{2,3,8},{0,1,5,8},{4,6,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,4},{0,3,4},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{5,6},{0,7},{1,3,7},{2,4,7},{5,7},{6,7},{2,3,8},{0,1,5,8},{4,6,8},{7,8}]
end Case9429
namespace Case9430
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{1,4},{0,3,4},{5},{0,1,2,5},{3,5},{4,5},{0,6},{1,6},{3,6},{2,4,6},{5,6},{7},{0,7},{2,7},{1,3,7},{5,7},{6,7},{8},{0,8},{1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[10,13,14],1⟩,⟨[15],1⟩,⟨[10,11,12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[12,14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[11,13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,13,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9430
namespace Case9430
def big : Finset (Finset (Fin 9)) := {{0,3,4},{0,1,2,5},{2,4,6},{1,3,7},{2,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{1,4},{0,3,4},{0,1,2,5},{3,5},{4,5},{0,6},{1,6},{3,6},{2,4,6},{5,6},{0,7},{2,7},{1,3,7},{5,7},{6,7},{0,8},{1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
end Case9430
namespace Case9431
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{3},{1,3},{4},{0,4},{1,2,4},{5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{7},{1,7},{2,7},{0,3,5,7},{6,7},{8},{0,1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={0,3,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,1,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[10,13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,11,18],1⟩,⟨[12,13,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case9431
namespace Case9431
def big : Finset (Finset (Fin 9)) := {{1,2,4},{3,4,6},{0,3,5,7},{0,1,8},{2,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,3},{0,4},{1,2,4},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{1,7},{2,7},{0,3,5,7},{6,7},{0,1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
end Case9431
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case1920
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,3},{4},{0,4},{1,4},{2,3,4},{5},{2,5},{6},{3,6},{0,1,5,6},{7},{0,7},{1,2,7},{3,5,7},{4,6,7},{8},{0,8},{1,3,8},{4,5,8},{2,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={1} then 2 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={6} then 3 else if T={3,6} then 1 else if T={0,1,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={4,5,8} then 1 else if T={2,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],3⟩,⟨[13,16],1⟩,⟨[17],3⟩,⟨[14,17],1⟩,⟨[11,12,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,13,18],1⟩,⟨[14,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,14,19],1⟩,⟨[15,16,19],1⟩,⟨[13,17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1920
namespace Case1920
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,1,5,6},{1,2,7},{3,5,7},{4,6,7},{1,3,8},{4,5,8},{2,6,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{0,4},{1,4},{2,3,4},{2,5},{3,6},{0,1,5,6},{0,7},{1,2,7},{3,5,7},{4,6,7},{0,8},{1,3,8},{4,5,8},{2,6,8},{7,8}]
end Case1920
namespace Case1921
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{3},{0,3},{4},{0,4},{3,4},{5},{1,3,5},{2,4,5},{6},{1,6},{2,3,6},{7},{2,7},{1,4,7},{0,5,6,7},{8},{0,8},{1,2,8},{5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={3,4} then 1 else if T={5} then 3 else if T={1,3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={7} then 3 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[13,14],1⟩,⟨[15],3⟩,⟨[11,13,15],1⟩,⟨[12,14,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[12,13,16],1⟩,⟨[17],3⟩,⟨[12,17],1⟩,⟨[11,14,17],1⟩,⟨[10,15,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,12,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1921
namespace Case1921
def big : Finset (Finset (Fin 9)) := {{1,3,5},{2,4,5},{2,3,6},{1,4,7},{0,5,6,7},{1,2,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{0,3},{0,4},{3,4},{1,3,5},{2,4,5},{1,6},{2,3,6},{2,7},{1,4,7},{0,5,6,7},{0,8},{1,2,8},{5,8},{4,6,8},{3,7,8}]
end Case1921
namespace Case1922
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{3},{0,3},{1,2,3},{4},{0,4},{5},{3,5},{1,4,5},{6},{1,6},{2,4,6},{7},{2,7},{3,4,7},{0,5,6,7},{8},{0,8},{4,8},{2,5,8},{3,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={1,4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={2,4,6} then 1 else if T={7} then 3 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={4,8} then 1 else if T={2,5,8} then 1 else if T={3,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],3⟩,⟨[14,16],1⟩,⟨[12,15,16],1⟩,⟨[17],3⟩,⟨[12,17],1⟩,⟨[13,15,17],1⟩,⟨[18],3⟩,⟨[13,18],1⟩,⟨[14,15,18],1⟩,⟨[11,16,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[15,19],1⟩,⟨[13,16,19],1⟩,⟨[14,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1922
namespace Case1922
def big : Finset (Finset (Fin 9)) := {{1,2,3},{1,4,5},{2,4,6},{3,4,7},{0,5,6,7},{2,5,8},{3,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{0,3},{1,2,3},{0,4},{3,5},{1,4,5},{1,6},{2,4,6},{2,7},{3,4,7},{0,5,6,7},{0,8},{4,8},{2,5,8},{3,6,8},{1,7,8}]
end Case1922
namespace Case1923
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{3,4},{5},{0,1,2,5},{3,5},{4,5},{6},{2,6},{0,3,6},{1,4,6},{5,6},{7},{0,7},{1,3,7},{2,4,7},{5,7},{8},{1,8},{2,3,8},{0,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={0,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[11,12,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[13,17],1⟩,⟨[11,14,17],1⟩,⟨[12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[19],2⟩,⟨[12,19],1⟩,⟨[13,14,19],1⟩,⟨[11,15,19],1⟩,⟨[16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1923
namespace Case1923
def big : Finset (Finset (Fin 9)) := {{0,1,2,5},{0,3,6},{1,4,6},{1,3,7},{2,4,7},{2,3,8},{0,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{3,4},{0,1,2,5},{3,5},{4,5},{2,6},{0,3,6},{1,4,6},{5,6},{0,7},{1,3,7},{2,4,7},{5,7},{1,8},{2,3,8},{0,4,8},{5,8},{6,7,8}]
end Case1923
namespace Case1924
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{2,4},{0,3,4},{5},{0,1,2,5},{3,5},{4,5},{6},{3,6},{1,4,6},{5,6},{7},{1,7},{2,3,7},{5,7},{0,6,7},{8},{0,8},{1,3,8},{5,8},{2,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,3,7} then 1 else if T={5,7} then 1 else if T={0,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[10,13,14],1⟩,⟨[15],1⟩,⟨[10,11,12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[13,16],1⟩,⟨[11,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,13,17],1⟩,⟨[15,17],1⟩,⟨[10,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,13,18],1⟩,⟨[15,18],1⟩,⟨[12,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1924
namespace Case1924
def big : Finset (Finset (Fin 9)) := {{0,3,4},{0,1,2,5},{1,4,6},{2,3,7},{0,6,7},{1,3,8},{2,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{2,4},{0,3,4},{0,1,2,5},{3,5},{4,5},{3,6},{1,4,6},{5,6},{1,7},{2,3,7},{5,7},{0,6,7},{0,8},{1,3,8},{5,8},{2,6,8},{4,7,8}]
end Case1924
namespace Case1925
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{1,3},{4},{2,4},{5},{0,1,2,5},{3,5},{4,5},{6},{0,3,6},{1,4,6},{5,6},{7},{2,3,7},{0,4,7},{5,7},{6,7},{8},{0,8},{3,4,8},{5,8},{2,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={2,3,7} then 1 else if T={0,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[10,11,12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,13,16],1⟩,⟨[11,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[12,13,17],1⟩,⟨[10,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[12,16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1925
namespace Case1925
def big : Finset (Finset (Fin 9)) := {{0,1,2,5},{0,3,6},{1,4,6},{2,3,7},{0,4,7},{3,4,8},{2,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{2,4},{0,1,2,5},{3,5},{4,5},{0,3,6},{1,4,6},{5,6},{2,3,7},{0,4,7},{5,7},{6,7},{0,8},{3,4,8},{5,8},{2,6,8},{1,7,8}]
end Case1925
namespace Case1926
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,2,3},{4},{1,2,4},{3,4},{5},{2,5},{3,5},{4,5},{6},{2,6},{0,1,5,6},{7},{0,7},{1,3,7},{5,7},{4,6,7},{8},{1,8},{0,4,8},{5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 2 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={1,2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={2,6} then 1 else if T={0,1,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={0,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[13,17],1⟩,⟨[11,12,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[12,19],1⟩,⟨[11,15,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1926
namespace Case1926
def big : Finset (Finset (Fin 9)) := {{0,2,3},{1,2,4},{0,1,5,6},{1,3,7},{4,6,7},{0,4,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2,3},{1,2,4},{3,4},{2,5},{3,5},{4,5},{2,6},{0,1,5,6},{0,7},{1,3,7},{5,7},{4,6,7},{1,8},{0,4,8},{5,8},{3,6,8},{2,7,8}]
end Case1926
namespace Case1927
def positionFn : Fin 9 → Fin 25 := ![16,17,18,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{1,3},{0,2,3},{4},{2,4},{5},{2,5},{3,5},{4,5},{6},{3,4,6},{0,1,5,6},{7},{1,2,7},{0,4,7},{5,7},{6,7},{8},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 2 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={3,4,6} then 1 else if T={0,1,5,6} then 1 else if T={7} then 2 else if T={1,2,7} then 1 else if T={0,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[17,18,19,20,21,22,23,24,25],[⟨[],2⟩,⟨[17],2⟩,⟨[18],2⟩,⟨[19],1⟩,⟨[20],1⟩,⟨[18,20],1⟩,⟨[17,19,20],1⟩,⟨[21],1⟩,⟨[19,21],1⟩,⟨[22],1⟩,⟨[19,22],1⟩,⟨[20,22],1⟩,⟨[21,22],1⟩,⟨[23],3⟩,⟨[20,21,23],1⟩,⟨[17,18,22,23],1⟩,⟨[24],2⟩,⟨[18,19,24],1⟩,⟨[17,21,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[25],2⟩,⟨[17,25],1⟩,⟨[18,21,25],1⟩,⟨[22,25],1⟩,⟨[19,23,25],1⟩,⟨[20,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1927
namespace Case1927
def big : Finset (Finset (Fin 9)) := {{0,2,3},{3,4,6},{0,1,5,6},{1,2,7},{0,4,7},{1,4,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,2,3},{2,4},{2,5},{3,5},{4,5},{3,4,6},{0,1,5,6},{1,2,7},{0,4,7},{5,7},{6,7},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
end Case1927
namespace Case1928
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{1,2,3},{4},{1,4},{0,2,4},{5},{2,5},{3,5},{4,5},{6},{3,6},{0,1,5,6},{7},{2,7},{0,3,7},{5,7},{4,6,7},{8},{0,8},{3,4,8},{5,8},{2,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 2 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,2,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={3,6} then 1 else if T={0,1,5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={0,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[11,13,15],1⟩,⟨[16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[14,17],1⟩,⟨[11,12,16,17],1⟩,⟨[18],2⟩,⟨[13,18],1⟩,⟨[11,14,18],1⟩,⟨[16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[14,15,19],1⟩,⟨[16,19],1⟩,⟨[13,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1928
namespace Case1928
def big : Finset (Finset (Fin 9)) := {{1,2,3},{0,2,4},{0,1,5,6},{0,3,7},{4,6,7},{3,4,8},{2,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{1,2,3},{1,4},{0,2,4},{2,5},{3,5},{4,5},{3,6},{0,1,5,6},{2,7},{0,3,7},{5,7},{4,6,7},{0,8},{3,4,8},{5,8},{2,6,8},{1,7,8}]
end Case1928
namespace Case1929
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,2,3},{4},{1,4},{5},{2,5},{3,5},{4,5},{6},{3,6},{2,4,6},{0,1,5,6},{7},{2,7},{1,3,7},{0,4,7},{5,7},{8},{0,8},{1,2,8},{3,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 2 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={0,1,5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={1,3,7} then 1 else if T={0,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[14,17],1⟩,⟨[13,15,17],1⟩,⟨[11,12,16,17],1⟩,⟨[18],2⟩,⟨[13,18],1⟩,⟨[12,14,18],1⟩,⟨[11,15,18],1⟩,⟨[16,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,13,19],1⟩,⟨[14,15,19],1⟩,⟨[16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1929
namespace Case1929
def big : Finset (Finset (Fin 9)) := {{0,2,3},{2,4,6},{0,1,5,6},{1,3,7},{0,4,7},{1,2,8},{3,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,2,3},{1,4},{2,5},{3,5},{4,5},{3,6},{2,4,6},{0,1,5,6},{2,7},{1,3,7},{0,4,7},{5,7},{0,8},{1,2,8},{3,4,8},{5,8},{6,7,8}]
end Case1929
namespace Case1930
def positionFn : Fin 9 → Fin 25 := ![16,17,18,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{1,3},{0,2,3},{4},{0,4},{5},{2,5},{3,5},{4,5},{6},{2,4,6},{0,1,5,6},{7},{1,2,7},{3,4,7},{5,7},{6,7},{8},{2,8},{1,4,8},{5,8},{3,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 2 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={2,4,6} then 1 else if T={0,1,5,6} then 1 else if T={7} then 2 else if T={1,2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={2,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[17,18,19,20,21,22,23,24,25],[⟨[],2⟩,⟨[17],2⟩,⟨[18],2⟩,⟨[19],1⟩,⟨[20],1⟩,⟨[18,20],1⟩,⟨[17,19,20],1⟩,⟨[21],1⟩,⟨[17,21],1⟩,⟨[22],1⟩,⟨[19,22],1⟩,⟨[20,22],1⟩,⟨[21,22],1⟩,⟨[23],3⟩,⟨[19,21,23],1⟩,⟨[17,18,22,23],1⟩,⟨[24],2⟩,⟨[18,19,24],1⟩,⟨[20,21,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[25],2⟩,⟨[19,25],1⟩,⟨[18,21,25],1⟩,⟨[22,25],1⟩,⟨[20,23,25],1⟩,⟨[17,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1930
namespace Case1930
def big : Finset (Finset (Fin 9)) := {{0,2,3},{2,4,6},{0,1,5,6},{1,2,7},{3,4,7},{1,4,8},{3,6,8},{0,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,2,3},{0,4},{2,5},{3,5},{4,5},{2,4,6},{0,1,5,6},{1,2,7},{3,4,7},{5,7},{6,7},{2,8},{1,4,8},{5,8},{3,6,8},{0,7,8}]
end Case1930
namespace Case1931
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,3},{4},{1,4},{2,3,4},{5},{2,5},{3,5},{4,5},{6},{2,6},{0,1,5,6},{7},{0,2,7},{1,3,7},{5,7},{4,6,7},{8},{1,2,8},{0,4,8},{5,8},{3,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 2 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={2,6} then 1 else if T={0,1,5,6} then 1 else if T={7} then 2 else if T={0,2,7} then 1 else if T={1,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={1,2,8} then 1 else if T={0,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[13,17],1⟩,⟨[11,12,16,17],1⟩,⟨[18],2⟩,⟨[11,13,18],1⟩,⟨[12,14,18],1⟩,⟨[16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[12,13,19],1⟩,⟨[11,15,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1931
namespace Case1931
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,1,5,6},{0,2,7},{1,3,7},{4,6,7},{1,2,8},{0,4,8},{3,6,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,4},{2,3,4},{2,5},{3,5},{4,5},{2,6},{0,1,5,6},{0,2,7},{1,3,7},{5,7},{4,6,7},{1,2,8},{0,4,8},{5,8},{3,6,8},{7,8}]
end Case1931
namespace Case1932
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{2,3},{4},{0,4},{5},{1,5},{2,5},{3,5},{4,5},{6},{1,3,6},{2,4,6},{7},{1,7},{3,4,7},{0,5,6,7},{8},{0,3,8},{1,4,8},{5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 2 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={1,3,6} then 1 else if T={2,4,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 2 else if T={0,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[10,11,12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[11,13,16],1⟩,⟨[12,14,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[13,14,17],1⟩,⟨[10,15,16,17],1⟩,⟨[18],2⟩,⟨[10,13,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1932
namespace Case1932
def big : Finset (Finset (Fin 9)) := {{0,1,2},{1,3,6},{2,4,6},{3,4,7},{0,5,6,7},{0,3,8},{1,4,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{2,3},{0,4},{1,5},{2,5},{3,5},{4,5},{1,3,6},{2,4,6},{1,7},{3,4,7},{0,5,6,7},{0,3,8},{1,4,8},{5,8},{6,8},{2,7,8}]
end Case1932
namespace Case1933
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,3},{4},{0,2,4},{3,4},{5},{1,5},{2,5},{3,5},{4,5},{6},{1,6},{2,3,6},{7},{2,7},{1,4,7},{0,5,6,7},{8},{0,8},{1,2,8},{5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 2 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={0,1,3} then 1 else if T={4} then 1 else if T={0,2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={7} then 3 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[10,11,13],1⟩,⟨[14],1⟩,⟨[10,12,14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[12,13,16],1⟩,⟨[17],3⟩,⟨[12,17],1⟩,⟨[11,14,17],1⟩,⟨[10,15,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,12,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1933
namespace Case1933
def big : Finset (Finset (Fin 9)) := {{0,1,3},{0,2,4},{2,3,6},{1,4,7},{0,5,6,7},{1,2,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,3},{0,2,4},{3,4},{1,5},{2,5},{3,5},{4,5},{1,6},{2,3,6},{2,7},{1,4,7},{0,5,6,7},{0,8},{1,2,8},{5,8},{4,6,8},{3,7,8}]
end Case1933
namespace Case1934
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{4},{0,4},{1,3,4},{5},{1,5},{2,5},{3,5},{4,5},{6},{3,6},{2,4,6},{7},{1,7},{2,3,7},{0,5,6,7},{8},{2,8},{0,3,8},{5,8},{1,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 2 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={2,3,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 2 else if T={2,8} then 1 else if T={0,3,8} then 1 else if T={5,8} then 1 else if T={1,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],2⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,14,15],1⟩,⟨[16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[14,17],1⟩,⟨[13,15,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[13,14,18],1⟩,⟨[11,16,17,18],1⟩,⟨[19],2⟩,⟨[13,19],1⟩,⟨[11,14,19],1⟩,⟨[16,19],1⟩,⟨[12,17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1934
namespace Case1934
def big : Finset (Finset (Fin 9)) := {{0,1,2},{1,3,4},{2,4,6},{2,3,7},{0,5,6,7},{0,3,8},{1,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{0,4},{1,3,4},{1,5},{2,5},{3,5},{4,5},{3,6},{2,4,6},{1,7},{2,3,7},{0,5,6,7},{2,8},{0,3,8},{5,8},{1,6,8},{4,7,8}]
end Case1934
namespace Case1935
def positionFn : Fin 9 → Fin 25 := ![16,17,18,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{4},{3,4},{5},{0,5},{1,5},{2,5},{3,5},{4,5},{6},{2,6},{0,3,6},{1,4,6},{7},{0,7},{1,3,7},{2,4,7},{8},{1,8},{2,3,8},{0,4,8},{5,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={2,6} then 1 else if T={0,3,6} then 1 else if T={1,4,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={8} then 3 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={0,4,8} then 1 else if T={5,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[17,18,19,20,21,22,23,24,25],[⟨[],2⟩,⟨[17],1⟩,⟨[18],1⟩,⟨[19],1⟩,⟨[17,18,19],1⟩,⟨[20],1⟩,⟨[21],1⟩,⟨[20,21],1⟩,⟨[22],1⟩,⟨[17,22],1⟩,⟨[18,22],1⟩,⟨[19,22],1⟩,⟨[20,22],1⟩,⟨[21,22],1⟩,⟨[23],3⟩,⟨[19,23],1⟩,⟨[17,20,23],1⟩,⟨[18,21,23],1⟩,⟨[24],3⟩,⟨[17,24],1⟩,⟨[18,20,24],1⟩,⟨[19,21,24],1⟩,⟨[25],3⟩,⟨[18,25],1⟩,⟨[19,20,25],1⟩,⟨[17,21,25],1⟩,⟨[22,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1935
namespace Case1935
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,6},{1,4,6},{1,3,7},{2,4,7},{2,3,8},{0,4,8},{5,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{3,4},{0,5},{1,5},{2,5},{3,5},{4,5},{2,6},{0,3,6},{1,4,6},{0,7},{1,3,7},{2,4,7},{1,8},{2,3,8},{0,4,8},{5,6,7,8}]
end Case1935
namespace Case1936
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,2,3},{0,4},{1,4},{2,4},{3,4},{5},{2,5},{3,5},{6},{1,6},{3,6},{0,5,6},{7},{0,7},{2,7},{1,5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={0,1,2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,6} then 1 else if T={0,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[11,12,13,14],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[14,17],1⟩,⟨[11,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,18],1⟩,⟨[12,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[15,16,19],1⟩,⟨[13,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1936
namespace Case1936
def big : Finset (Finset (Fin 9)) := {{0,1,2,3},{0,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2,3},{0,4},{1,4},{2,4},{3,4},{2,5},{3,5},{1,6},{3,6},{0,5,6},{0,7},{2,7},{1,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]
end Case1936
namespace Case1937
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,2,3},{4},{2,4},{3,4},{5},{0,5},{1,5},{2,5},{3,5},{6},{1,6},{3,6},{0,4,6},{7},{0,7},{2,7},{1,4,7},{5,6,7},{8},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={0,1,2,3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,6} then 1 else if T={0,4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[11,12,13,14],1⟩,⟨[15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[14,17],1⟩,⟨[11,15,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,18],1⟩,⟨[12,15,18],1⟩,⟨[16,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[15,16,19],1⟩,⟨[13,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1937
namespace Case1937
def big : Finset (Finset (Fin 9)) := {{0,1,2,3},{0,4,6},{1,4,7},{5,6,7},{4,5,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2,3},{2,4},{3,4},{0,5},{1,5},{2,5},{3,5},{1,6},{3,6},{0,4,6},{0,7},{2,7},{1,4,7},{5,6,7},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]
end Case1937
namespace Case1938
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,3},{1,3},{2,3},{4},{2,4},{5},{0,1,2,5},{3,5},{4,5},{6},{1,6},{0,4,6},{5,6},{7},{0,7},{2,7},{1,4,7},{3,6,7},{8},{0,8},{1,8},{3,4,8},{2,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,4,8} then 1 else if T={2,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[11,12,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[11,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,18],1⟩,⟨[12,15,18],1⟩,⟨[14,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[14,15,19],1⟩,⟨[13,17,19],1⟩,⟨[16,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1938
namespace Case1938
def big : Finset (Finset (Fin 9)) := {{0,1,2,5},{0,4,6},{1,4,7},{3,6,7},{3,4,8},{2,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{2,3},{2,4},{0,1,2,5},{3,5},{4,5},{1,6},{0,4,6},{5,6},{0,7},{2,7},{1,4,7},{3,6,7},{0,8},{1,8},{3,4,8},{2,6,8},{5,7,8}]
end Case1938
namespace Case1939
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,3},{1,3},{2,3},{4},{1,4},{2,4},{5},{0,1,2,5},{3,5},{6},{2,6},{0,4,6},{5,6},{7},{0,7},{3,4,7},{5,7},{1,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[10,11,12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[10,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[11,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[14,15,18],1⟩,⟨[13,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1939
namespace Case1939
def big : Finset (Finset (Fin 9)) := {{0,1,2,5},{0,4,6},{3,4,7},{1,6,7},{4,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{2,3},{1,4},{2,4},{0,1,2,5},{3,5},{2,6},{0,4,6},{5,6},{0,7},{3,4,7},{5,7},{1,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
end Case1939
namespace Case1940
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{2,3},{4},{1,4},{0,3,4},{5},{0,1,2,5},{3,5},{4,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{0,7},{2,7},{1,3,7},{4,6,7},{8},{0,8},{1,8},{2,4,8},{3,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={3,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[10,13,14],1⟩,⟨[15],2⟩,⟨[10,11,12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[11,13,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[13,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1940
namespace Case1940
def big : Finset (Finset (Fin 9)) := {{0,3,4},{0,1,2,5},{1,3,7},{4,6,7},{2,4,8},{3,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{2,3},{1,4},{0,3,4},{0,1,2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{2,7},{1,3,7},{4,6,7},{0,8},{1,8},{2,4,8},{3,6,8},{5,7,8}]
end Case1940
namespace Case1941
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{2,3},{4},{1,4},{2,4},{0,3,4},{5},{0,1,2,5},{3,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{0,7},{1,3,7},{5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[11,14,15],1⟩,⟨[16],2⟩,⟨[11,12,13,16],1⟩,⟨[14,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[15,16,19],1⟩,⟨[14,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1941
namespace Case1941
def big : Finset (Finset (Fin 9)) := {{0,3,4},{0,1,2,5},{1,3,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{2,3},{1,4},{2,4},{0,3,4},{0,1,2,5},{3,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,3,7},{5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
end Case1941
namespace Case1942
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{2,3},{4},{0,4},{1,4},{5},{0,1,2,5},{3,5},{6},{0,6},{1,6},{2,6},{3,4,6},{5,6},{7},{1,7},{0,3,7},{2,4,7},{5,7},{8},{0,8},{2,8},{1,3,8},{4,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,3,8} then 1 else if T={4,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[10,11,12,15],1⟩,⟨[13,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[10,13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,18],1⟩,⟨[11,13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1942
namespace Case1942
def big : Finset (Finset (Fin 9)) := {{0,1,2,5},{3,4,6},{0,3,7},{2,4,7},{1,3,8},{4,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{2,3},{0,4},{1,4},{0,1,2,5},{3,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{1,7},{0,3,7},{2,4,7},{5,7},{0,8},{2,8},{1,3,8},{4,5,8},{6,7,8}]
end Case1942
namespace Case1943
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{1,3},{2,3},{4},{0,4},{2,4},{5},{0,1,2,5},{3,4,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{1,7},{0,3,7},{5,7},{4,6,7},{8},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={0,1,2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[10,11,12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[10,13,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[13,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1943
namespace Case1943
def big : Finset (Finset (Fin 9)) := {{0,1,2,5},{3,4,5},{0,3,7},{4,6,7},{1,4,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{2,3},{0,4},{2,4},{0,1,2,5},{3,4,5},{0,6},{1,6},{2,6},{5,6},{1,7},{0,3,7},{5,7},{4,6,7},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]
end Case1943
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case8064
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{3},{0,3},{4},{0,1,4},{2,4},{5},{0,5},{2,5},{4,5},{6},{1,6},{3,4,6},{5,6},{7},{1,3,5,7},{0,2,6,7},{8},{0,8},{1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 4 else if T={1,3,5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],4⟩,⟨[11,13,15,17],1⟩,⟨[10,12,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,13,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8064
namespace Case8064
def big : Finset (Finset (Fin 9)) := {{0,1,4},{3,4,6},{1,3,5,7},{0,2,6,7},{2,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,1,4},{2,4},{0,5},{2,5},{4,5},{1,6},{3,4,6},{5,6},{1,3,5,7},{0,2,6,7},{0,8},{1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
end Case8064
namespace Case8065
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{3},{0,4},{1,4},{2,4},{5},{0,5},{2,5},{4,5},{6},{1,6},{0,2,3,6},{5,6},{7},{0,7},{1,3,5,7},{4,6,7},{8},{0,1,8},{3,4,8},{5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,2,3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={1,3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,1,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[10,12,13,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[10,17],1⟩,⟨[11,13,15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,11,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8065
namespace Case8065
def big : Finset (Finset (Fin 9)) := {{0,2,3,6},{1,3,5,7},{4,6,7},{0,1,8},{3,4,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,4},{1,4},{2,4},{0,5},{2,5},{4,5},{1,6},{0,2,3,6},{5,6},{0,7},{1,3,5,7},{4,6,7},{0,1,8},{3,4,8},{5,8},{6,8},{2,7,8}]
end Case8065
namespace Case8066
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{3},{4},{0,4},{5},{0,5},{2,5},{1,3,4,5},{6},{1,6},{0,2,3,6},{5,6},{7},{0,7},{1,7},{2,7},{5,7},{4,6,7},{8},{0,1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={4} then 2 else if T={0,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={1,3,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,2,3,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,1,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[14],2⟩,⟨[10,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[11,13,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[10,12,13,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,11,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8066
namespace Case8066
def big : Finset (Finset (Fin 9)) := {{1,3,4,5},{0,2,3,6},{4,6,7},{0,1,8},{2,4,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,4},{0,5},{2,5},{1,3,4,5},{1,6},{0,2,3,6},{5,6},{0,7},{1,7},{2,7},{5,7},{4,6,7},{0,1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
end Case8066
namespace Case8067
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{3},{4},{0,1,4},{5},{0,5},{2,5},{4,5},{6},{1,6},{0,2,3,6},{4,6},{5,6},{7},{0,7},{1,7},{2,7},{3,4,7},{5,7},{8},{0,8},{2,4,8},{1,3,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={4} then 1 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,2,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={1,3,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[10,12,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[18],3⟩,⟨[10,18],1⟩,⟨[12,14,18],1⟩,⟨[11,13,15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8067
namespace Case8067
def big : Finset (Finset (Fin 9)) := {{0,1,4},{0,2,3,6},{3,4,7},{2,4,8},{1,3,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,1,4},{0,5},{2,5},{4,5},{1,6},{0,2,3,6},{4,6},{5,6},{0,7},{1,7},{2,7},{3,4,7},{5,7},{0,8},{2,4,8},{1,3,5,8},{6,7,8}]
end Case8067
namespace Case8068
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{0,3},{1,3},{2,3},{4},{0,4},{5},{0,5},{2,5},{3,5},{6},{1,6},{3,4,6},{5,6},{7},{1,4,5,7},{0,2,6,7},{8},{0,1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 4 else if T={1,4,5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 2 else if T={0,1,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],4⟩,⟨[12,15,16,18],1⟩,⟨[11,13,17,18],1⟩,⟨[19],2⟩,⟨[11,12,19],1⟩,⟨[13,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8068
namespace Case8068
def big : Finset (Finset (Fin 9)) := {{3,4,6},{1,4,5,7},{0,2,6,7},{0,1,8},{2,4,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{2,3},{0,4},{0,5},{2,5},{3,5},{1,6},{3,4,6},{5,6},{1,4,5,7},{0,2,6,7},{0,1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
end Case8068
namespace Case8069
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{0,3},{1,3},{2,3},{4},{0,1,4},{5},{0,5},{2,5},{3,5},{4,5},{6},{1,6},{4,6},{5,6},{7},{3,4,7},{0,2,6,7},{8},{0,8},{2,4,8},{3,6,8},{1,5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 4 else if T={3,4,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={3,6,8} then 1 else if T={1,5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],4⟩,⟨[13,14,17],1⟩,⟨[10,12,16,17],1⟩,⟨[18],3⟩,⟨[10,18],1⟩,⟨[12,14,18],1⟩,⟨[13,16,18],1⟩,⟨[11,15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8069
namespace Case8069
def big : Finset (Finset (Fin 9)) := {{0,1,4},{3,4,7},{0,2,6,7},{2,4,8},{3,6,8},{1,5,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{2,3},{0,1,4},{0,5},{2,5},{3,5},{4,5},{1,6},{4,6},{5,6},{3,4,7},{0,2,6,7},{0,8},{2,4,8},{3,6,8},{1,5,7,8}]
end Case8069
namespace Case8070
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{3},{0,3},{4},{0,1,4},{2,3,4},{5},{0,5},{2,5},{4,5},{6},{1,6},{4,6},{5,6},{7},{1,3,5,7},{0,2,6,7},{8},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 4 else if T={1,3,5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],4⟩,⟨[12,14,16,18],1⟩,⟨[11,13,17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8070
namespace Case8070
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,3,4},{1,3,5,7},{0,2,6,7},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,1,4},{2,3,4},{0,5},{2,5},{4,5},{1,6},{4,6},{5,6},{1,3,5,7},{0,2,6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
end Case8070
namespace Case8071
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,3},{1,3},{4},{1,4},{5},{1,5},{3,5},{0,2,4,5},{6},{0,6},{3,4,6},{5,6},{7},{0,7},{3,7},{5,7},{1,2,6,7},{8},{0,1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={0,2,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={1,2,6,7} then 1 else if T={8} then 2 else if T={0,1,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],3⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[10,12,14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[11,12,16,17],1⟩,⟨[18],2⟩,⟨[10,11,18],1⟩,⟨[12,13,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8071
namespace Case8071
def big : Finset (Finset (Fin 9)) := {{0,2,4,5},{3,4,6},{1,2,6,7},{0,1,8},{2,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{1,4},{1,5},{3,5},{0,2,4,5},{0,6},{3,4,6},{5,6},{0,7},{3,7},{5,7},{1,2,6,7},{0,1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
end Case8071
namespace Case8072
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,3},{1,3},{4},{0,1,4},{2,3,4},{5},{1,5},{3,5},{4,5},{6},{0,6},{4,6},{5,6},{7},{0,7},{3,7},{5,7},{1,2,6,7},{8},{1,8},{0,2,5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={1,2,6,7} then 1 else if T={8} then 3 else if T={1,8} then 1 else if T={0,2,5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],3⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[14,18],1⟩,⟨[16,18],1⟩,⟨[12,13,17,18],1⟩,⟨[19],3⟩,⟨[12,19],1⟩,⟨[11,13,16,19],1⟩,⟨[14,17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8072
namespace Case8072
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,3,4},{1,2,6,7},{0,2,5,8},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{0,1,4},{2,3,4},{1,5},{3,5},{4,5},{0,6},{4,6},{5,6},{0,7},{3,7},{5,7},{1,2,6,7},{1,8},{0,2,5,8},{3,6,8},{4,7,8}]
end Case8072
namespace Case8073
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{1,3},{4},{0,1,4},{5},{1,5},{0,2,3,5},{4,5},{6},{0,6},{3,4,6},{5,6},{7},{0,7},{4,7},{5,7},{1,2,6,7},{8},{0,8},{1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={0,2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={1,2,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[10,12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[11,12,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8073
namespace Case8073
def big : Finset (Finset (Fin 9)) := {{0,1,4},{0,2,3,5},{3,4,6},{1,2,6,7},{2,4,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,1,4},{1,5},{0,2,3,5},{4,5},{0,6},{3,4,6},{5,6},{0,7},{4,7},{5,7},{1,2,6,7},{0,8},{1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
end Case8073
namespace Case8074
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{3},{1,3},{4},{0,1,4},{5},{1,5},{2,5},{4,5},{6},{0,6},{2,3,6},{4,6},{5,6},{7},{0,7},{2,7},{3,4,7},{5,7},{8},{2,4,8},{0,3,5,8},{1,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 4 else if T={2,4,8} then 1 else if T={0,3,5,8} then 1 else if T={1,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[18],4⟩,⟨[12,14,18],1⟩,⟨[10,13,15,18],1⟩,⟨[11,16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8074
namespace Case8074
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,3,6},{3,4,7},{2,4,8},{0,3,5,8},{1,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{0,1,4},{1,5},{2,5},{4,5},{0,6},{2,3,6},{4,6},{5,6},{0,7},{2,7},{3,4,7},{5,7},{2,4,8},{0,3,5,8},{1,6,7,8}]
end Case8074
namespace Case8075
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{1,2},{3},{1,4},{2,4},{5},{0,5},{2,5},{4,5},{6},{0,2,3,6},{4,6},{5,6},{7},{0,4,7},{1,3,5,7},{6,7},{8},{0,8},{3,4,8},{5,8},{1,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,2,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={0,4,7} then 1 else if T={1,3,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={1,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,12,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[10,14,17],1⟩,⟨[11,13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[11,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8075
namespace Case8075
def big : Finset (Finset (Fin 9)) := {{0,2,3,6},{0,4,7},{1,3,5,7},{3,4,8},{1,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{1,4},{2,4},{0,5},{2,5},{4,5},{0,2,3,6},{4,6},{5,6},{0,4,7},{1,3,5,7},{6,7},{0,8},{3,4,8},{5,8},{1,6,8},{2,7,8}]
end Case8075
namespace Case8076
def positionFn : Fin 9 → Fin 25 := ![11,12,19,20,13,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{1,2},{3},{4},{5},{0,5},{1,5},{2,3,4,5},{6},{0,1,3,6},{4,6},{5,6},{7},{1,7},{2,7},{0,4,7},{5,7},{6,7},{8},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={4} then 2 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,3,4,5} then 1 else if T={6} then 2 else if T={0,1,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={0,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,13,14,20,21,22,23,24,25],[⟨[],2⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[20],1⟩,⟨[12,20],1⟩,⟨[13,20],1⟩,⟨[21],3⟩,⟨[14],2⟩,⟨[22],1⟩,⟨[12,22],1⟩,⟨[13,22],1⟩,⟨[14,20,21,22],1⟩,⟨[23],2⟩,⟨[12,13,21,23],1⟩,⟨[14,23],1⟩,⟨[22,23],1⟩,⟨[24],1⟩,⟨[13,24],1⟩,⟨[20,24],1⟩,⟨[12,14,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[25],2⟩,⟨[12,25],1⟩,⟨[13,14,25],1⟩,⟨[22,25],1⟩,⟨[20,23,25],1⟩,⟨[21,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8076
namespace Case8076
def big : Finset (Finset (Fin 9)) := {{2,3,4,5},{0,1,3,6},{0,4,7},{1,4,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,5},{1,5},{2,3,4,5},{0,1,3,6},{4,6},{5,6},{1,7},{2,7},{0,4,7},{5,7},{6,7},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
end Case8076
namespace Case8077
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{0,2},{3},{4},{2,4},{5},{1,5},{2,5},{4,5},{6},{1,2,3,6},{0,4,6},{5,6},{7},{0,7},{1,7},{3,4,7},{5,7},{6,7},{8},{1,4,8},{0,3,5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 3 else if T={4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,2,3,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={1,4,8} then 1 else if T={0,3,5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],3⟩,⟨[15],1⟩,⟨[13,15],1⟩,⟨[16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[12,13,14,17],1⟩,⟨[11,15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],3⟩,⟨[12,15,19],1⟩,⟨[11,14,16,19],1⟩,⟨[17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8077
namespace Case8077
def big : Finset (Finset (Fin 9)) := {{1,2,3,6},{0,4,6},{3,4,7},{1,4,8},{0,3,5,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{2,4},{1,5},{2,5},{4,5},{1,2,3,6},{0,4,6},{5,6},{0,7},{1,7},{3,4,7},{5,7},{6,7},{1,4,8},{0,3,5,8},{6,8},{2,7,8}]
end Case8077
namespace Case8078
def positionFn : Fin 9 → Fin 25 := ![14,18,19,11,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{1,2},{1,3},{2,3},{4},{0,3,4},{5},{0,5},{1,5},{3,5},{6},{3,6},{4,6},{5,6},{7},{2,4,5,7},{0,1,6,7},{8},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 4 else if T={2,4,5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,15,19,20,21,22,23,24,25],[⟨[],2⟩,⟨[15],1⟩,⟨[19],1⟩,⟨[20],1⟩,⟨[15,20],1⟩,⟨[19,20],1⟩,⟨[12,19],1⟩,⟨[12,20],1⟩,⟨[21],2⟩,⟨[12,15,21],1⟩,⟨[22],1⟩,⟨[15,22],1⟩,⟨[19,22],1⟩,⟨[12,22],1⟩,⟨[23],2⟩,⟨[12,23],1⟩,⟨[21,23],1⟩,⟨[22,23],1⟩,⟨[24],4⟩,⟨[20,21,22,24],1⟩,⟨[15,19,23,24],1⟩,⟨[25],2⟩,⟨[15,25],1⟩,⟨[19,21,25],1⟩,⟨[22,25],1⟩,⟨[20,23,25],1⟩,⟨[12,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8078
namespace Case8078
def big : Finset (Finset (Fin 9)) := {{0,3,4},{2,4,5,7},{0,1,6,7},{1,4,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{2,3},{0,3,4},{0,5},{1,5},{3,5},{3,6},{4,6},{5,6},{2,4,5,7},{0,1,6,7},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
end Case8078
namespace Case8079
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{1,2},{1,3},{2,3},{4},{0,4},{5},{0,5},{2,5},{3,5},{4,5},{6},{3,6},{1,4,6},{5,6},{7},{3,4,7},{0,2,6,7},{8},{0,3,8},{2,4,8},{6,8},{1,5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 4 else if T={3,4,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 3 else if T={0,3,8} then 1 else if T={2,4,8} then 1 else if T={6,8} then 1 else if T={1,5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[13,16],1⟩,⟨[11,14,16],1⟩,⟨[15,16],1⟩,⟨[17],4⟩,⟨[13,14,17],1⟩,⟨[10,12,16,17],1⟩,⟨[18],3⟩,⟨[10,13,18],1⟩,⟨[12,14,18],1⟩,⟨[16,18],1⟩,⟨[11,15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8079
namespace Case8079
def big : Finset (Finset (Fin 9)) := {{1,4,6},{3,4,7},{0,2,6,7},{0,3,8},{2,4,8},{1,5,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{1,3},{2,3},{0,4},{0,5},{2,5},{3,5},{4,5},{3,6},{1,4,6},{5,6},{3,4,7},{0,2,6,7},{0,3,8},{2,4,8},{6,8},{1,5,7,8}]
end Case8079
namespace Case8080
def positionFn : Fin 9 → Fin 25 := ![11,19,13,20,12,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{1,2},{3},{4},{1,4},{0,3,4},{5},{0,5},{1,5},{4,5},{6},{3,6},{2,4,6},{5,6},{7},{2,3,5,7},{0,1,6,7},{8},{0,8},{2,8},{1,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 4 else if T={2,3,5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,13,14,20,21,22,23,24,25],[⟨[],2⟩,⟨[12],1⟩,⟨[20],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[14,20],1⟩,⟨[21],2⟩,⟨[13],1⟩,⟨[13,20],1⟩,⟨[12,13,21],1⟩,⟨[22],1⟩,⟨[12,22],1⟩,⟨[20,22],1⟩,⟨[13,22],1⟩,⟨[23],2⟩,⟨[21,23],1⟩,⟨[13,14,23],1⟩,⟨[22,23],1⟩,⟨[24],4⟩,⟨[14,21,22,24],1⟩,⟨[12,20,23,24],1⟩,⟨[25],1⟩,⟨[12,25],1⟩,⟨[14,25],1⟩,⟨[20,21,25],1⟩,⟨[22,25],1⟩,⟨[23,25],1⟩,⟨[13,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8080
namespace Case8080
def big : Finset (Finset (Fin 9)) := {{0,3,4},{2,4,6},{2,3,5,7},{0,1,6,7},{1,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,4},{0,3,4},{0,5},{1,5},{4,5},{3,6},{2,4,6},{5,6},{2,3,5,7},{0,1,6,7},{0,8},{2,8},{1,3,8},{5,8},{6,8},{4,7,8}]
end Case8080
namespace Case8081
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{1,3},{4},{0,3,4},{5},{0,5},{3,5},{1,2,4,5},{6},{3,6},{4,6},{5,6},{7},{1,7},{3,7},{5,7},{0,2,6,7},{8},{0,8},{2,3,8},{5,8},{1,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={1,3} then 1 else if T={4} then 2 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={3,5} then 1 else if T={1,2,4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={1,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[11,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[14,16],1⟩,⟨[12,13,15,16],1⟩,⟨[17],2⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[14,18],1⟩,⟨[16,18],1⟩,⟨[11,13,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,14,19],1⟩,⟨[16,19],1⟩,⟨[12,17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8081
namespace Case8081
def big : Finset (Finset (Fin 9)) := {{0,3,4},{1,2,4,5},{0,2,6,7},{2,3,8},{1,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{0,3,4},{0,5},{3,5},{1,2,4,5},{3,6},{4,6},{5,6},{1,7},{3,7},{5,7},{0,2,6,7},{0,8},{2,3,8},{5,8},{1,6,8},{4,7,8}]
end Case8081
namespace Case8082
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{1,3},{4},{0,4},{2,3,4},{5},{0,5},{3,5},{4,5},{6},{3,6},{1,4,6},{5,6},{7},{1,7},{3,7},{5,7},{0,2,6,7},{8},{0,3,8},{1,2,5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 3 else if T={0,3,8} then 1 else if T={1,2,5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[14,17],1⟩,⟨[12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[14,18],1⟩,⟨[16,18],1⟩,⟨[11,13,17,18],1⟩,⟨[19],3⟩,⟨[11,14,19],1⟩,⟨[12,13,16,19],1⟩,⟨[17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8082
namespace Case8082
def big : Finset (Finset (Fin 9)) := {{2,3,4},{1,4,6},{0,2,6,7},{0,3,8},{1,2,5,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{0,4},{2,3,4},{0,5},{3,5},{4,5},{3,6},{1,4,6},{5,6},{1,7},{3,7},{5,7},{0,2,6,7},{0,3,8},{1,2,5,8},{6,8},{4,7,8}]
end Case8082
namespace Case8083
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{3},{4},{0,4},{5},{0,5},{1,2,3,5},{4,5},{6},{3,6},{1,4,6},{5,6},{7},{1,7},{3,4,7},{5,7},{0,2,6,7},{8},{1,8},{0,3,8},{2,4,8},{5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 1 else if T={1,8} then 1 else if T={0,3,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[13,16],1⟩,⟨[11,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[10,12,16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[10,13,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8083
namespace Case8083
def big : Finset (Finset (Fin 9)) := {{1,2,3,5},{1,4,6},{3,4,7},{0,2,6,7},{0,3,8},{2,4,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,4},{0,5},{1,2,3,5},{4,5},{3,6},{1,4,6},{5,6},{1,7},{3,4,7},{5,7},{0,2,6,7},{1,8},{0,3,8},{2,4,8},{5,8},{6,8},{7,8}]
end Case8083
namespace Case8084
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{1,2},{3},{0,2,3},{4},{0,4},{5},{0,5},{2,5},{4,5},{6},{2,6},{3,6},{1,4,6},{5,6},{7},{1,7},{2,7},{3,4,7},{5,7},{8},{2,4,8},{1,3,5,8},{0,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 4 else if T={2,4,8} then 1 else if T={1,3,5,8} then 1 else if T={0,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[10,12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[11,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[18],4⟩,⟨[12,14,18],1⟩,⟨[11,13,15,18],1⟩,⟨[10,16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8084
namespace Case8084
def big : Finset (Finset (Fin 9)) := {{0,2,3},{1,4,6},{3,4,7},{2,4,8},{1,3,5,8},{0,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{0,2,3},{0,4},{0,5},{2,5},{4,5},{2,6},{3,6},{1,4,6},{5,6},{1,7},{2,7},{3,4,7},{5,7},{2,4,8},{1,3,5,8},{0,6,7,8}]
end Case8084
namespace Case8085
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{0,3},{1,3},{4},{5},{0,5},{3,5},{1,2,4,5},{6},{3,6},{4,6},{5,6},{7},{1,7},{3,4,7},{5,7},{0,2,6,7},{8},{2,3,8},{0,4,8},{5,8},{1,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={5} then 1 else if T={0,5} then 1 else if T={3,5} then 1 else if T={1,2,4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 2 else if T={2,3,8} then 1 else if T={0,4,8} then 1 else if T={5,8} then 1 else if T={1,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[14,16],1⟩,⟨[12,13,15,16],1⟩,⟨[17],2⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[11,13,17,18],1⟩,⟨[19],2⟩,⟨[13,14,19],1⟩,⟨[11,15,19],1⟩,⟨[16,19],1⟩,⟨[12,17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8085
namespace Case8085
def big : Finset (Finset (Fin 9)) := {{1,2,4,5},{3,4,7},{0,2,6,7},{2,3,8},{0,4,8},{1,6,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,3},{1,3},{0,5},{3,5},{1,2,4,5},{3,6},{4,6},{5,6},{1,7},{3,4,7},{5,7},{0,2,6,7},{2,3,8},{0,4,8},{5,8},{1,6,8},{7,8}]
end Case8085
namespace Case8086
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{0,3},{1,3},{4},{2,3,4},{5},{1,5},{3,5},{4,5},{6},{3,6},{0,4,6},{5,6},{7},{0,7},{4,7},{5,7},{1,2,6,7},{8},{1,4,8},{0,2,5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={2,3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={1,2,6,7} then 1 else if T={8} then 3 else if T={1,4,8} then 1 else if T={0,2,5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[14,17],1⟩,⟨[11,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[12,13,17,18],1⟩,⟨[19],3⟩,⟨[12,15,19],1⟩,⟨[11,13,16,19],1⟩,⟨[17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8086
namespace Case8086
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,4,6},{1,2,6,7},{1,4,8},{0,2,5,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,3},{1,3},{2,3,4},{1,5},{3,5},{4,5},{3,6},{0,4,6},{5,6},{0,7},{4,7},{5,7},{1,2,6,7},{1,4,8},{0,2,5,8},{6,8},{3,7,8}]
end Case8086
namespace Case8087
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{3},{4},{0,3,4},{5},{0,5},{1,2,3,5},{4,5},{6},{3,6},{1,4,6},{5,6},{7},{1,7},{4,7},{5,7},{0,2,6,7},{8},{0,8},{1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[10,13,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[13,16],1⟩,⟨[11,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[10,12,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case8087
namespace Case8087
def big : Finset (Finset (Fin 9)) := {{0,3,4},{1,2,3,5},{1,4,6},{0,2,6,7},{2,4,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,3,4},{0,5},{1,2,3,5},{4,5},{3,6},{1,4,6},{5,6},{1,7},{4,7},{5,7},{0,2,6,7},{0,8},{1,8},{2,4,8},{5,8},{6,8},{3,7,8}]
end Case8087
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

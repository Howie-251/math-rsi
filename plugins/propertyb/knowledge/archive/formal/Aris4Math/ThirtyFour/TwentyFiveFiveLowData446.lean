import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case10704
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{0,2},{1,2},{3},{4},{5},{1,5},{2,5},{6},{1,6},{2,6},{0,3,4,5,6},{7},{1,3,7},{2,4,7},{5,7},{6,7},{8},{2,3,8},{1,4,8},{5,8},{6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={4} then 3 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,6} then 1 else if T={0,3,4,5,6} then 1 else if T={7} then 2 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],2⟩,⟨[10,11],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[14],3⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[10,13,14,15,16],1⟩,⟨[17],2⟩,⟨[11,13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[10,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10704
namespace Case10704
def big : Finset (Finset (Fin 9)) := {{0,3,4,5,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{0,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{1,2},{1,5},{2,5},{1,6},{2,6},{0,3,4,5,6},{1,3,7},{2,4,7},{5,7},{6,7},{2,3,8},{1,4,8},{5,8},{6,8},{0,7,8}]
end Case10704
namespace Case10705
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{0,2},{1,2},{3},{4},{1,3,4},{5},{1,5},{2,5},{4,5},{6},{1,6},{2,6},{4,6},{7},{2,4,7},{0,3,5,6,7},{8},{2,3,8},{0,4,8},{5,8},{6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 3 else if T={4} then 1 else if T={1,3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={7} then 4 else if T={2,4,7} then 1 else if T={0,3,5,6,7} then 1 else if T={8} then 2 else if T={2,3,8} then 1 else if T={0,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],2⟩,⟨[10,11],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[11,13,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[17],4⟩,⟨[12,14,17],1⟩,⟨[10,13,15,16,17],1⟩,⟨[18],2⟩,⟨[12,13,18],1⟩,⟨[10,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10705
namespace Case10705
def big : Finset (Finset (Fin 9)) := {{1,3,4},{2,4,7},{0,3,5,6,7},{2,3,8},{0,4,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{1,2},{1,3,4},{1,5},{2,5},{4,5},{1,6},{2,6},{4,6},{2,4,7},{0,3,5,6,7},{2,3,8},{0,4,8},{5,8},{6,8},{1,7,8}]
end Case10705
namespace Case10706
def positionFn : Fin 9 → Fin 25 := ![8,9,10,11,12,13,14,15,16]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{0,2},{1,2},{3},{4},{0,3,4},{5},{1,5},{2,5},{3,5},{4,5},{6},{1,6},{2,6},{3,6},{4,6},{7},{1,3,7},{2,4,7},{8},{2,3,8},{1,4,8},{0,5,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={7} then 4 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={8} then 4 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={0,5,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,16,17],[⟨[],1⟩,⟨[9],2⟩,⟨[9,10],1⟩,⟨[9,11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[9,12,13],1⟩,⟨[14],2⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],4⟩,⟨[10,12,16],1⟩,⟨[11,13,16],1⟩,⟨[17],4⟩,⟨[11,12,17],1⟩,⟨[10,13,17],1⟩,⟨[9,14,15,16,17],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10706
namespace Case10706
def big : Finset (Finset (Fin 9)) := {{0,3,4},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{0,5,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{1,2},{0,3,4},{1,5},{2,5},{3,5},{4,5},{1,6},{2,6},{3,6},{4,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{0,5,6,7,8}]
end Case10706
namespace Case10707
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{3},{4},{1,2,4},{5},{1,5},{4,5},{6},{1,6},{4,6},{0,2,3,5,6},{7},{0,7},{1,7},{3,4,7},{5,7},{6,7},{8},{1,3,8},{0,4,8},{5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 3 else if T={4} then 1 else if T={1,2,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={4,6} then 1 else if T={0,2,3,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={1,3,8} then 1 else if T={0,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],2⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[11,12,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[14,16],1⟩,⟨[10,12,13,15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,13,18],1⟩,⟨[10,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10707
namespace Case10707
def big : Finset (Finset (Fin 9)) := {{1,2,4},{0,2,3,5,6},{3,4,7},{1,3,8},{0,4,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2,4},{1,5},{4,5},{1,6},{4,6},{0,2,3,5,6},{0,7},{1,7},{3,4,7},{5,7},{6,7},{1,3,8},{0,4,8},{5,8},{6,8},{2,7,8}]
end Case10707
namespace Case10708
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{3},{1,2,3},{4},{0,3,4},{5},{1,5},{3,5},{4,5},{6},{1,6},{3,6},{4,6},{7},{0,7},{1,7},{2,4,7},{5,7},{6,7},{8},{1,4,8},{0,2,5,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 4 else if T={1,4,8} then 1 else if T={0,2,5,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],2⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[10,13,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],4⟩,⟨[11,14,18],1⟩,⟨[10,12,15,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10708
namespace Case10708
def big : Finset (Finset (Fin 9)) := {{1,2,3},{0,3,4},{2,4,7},{1,4,8},{0,2,5,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2,3},{0,3,4},{1,5},{3,5},{4,5},{1,6},{3,6},{4,6},{0,7},{1,7},{2,4,7},{5,7},{6,7},{1,4,8},{0,2,5,6,8},{3,7,8}]
end Case10708
namespace Case10709
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,3,4},{5},{3,5},{4,5},{6},{3,6},{4,6},{0,1,2,5,6},{7},{0,7},{1,3,7},{2,4,7},{5,7},{6,7},{8},{0,8},{2,3,8},{1,4,8},{5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={1} then 3 else if T={2} then 3 else if T={3} then 1 else if T={4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={4,6} then 1 else if T={0,1,2,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],2⟩,⟨[12],3⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[15],1⟩,⟨[11,14,15],1⟩,⟨[16],2⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[11,12,13,16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[13,14,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10709
namespace Case10709
def big : Finset (Finset (Fin 9)) := {{0,3,4},{0,1,2,5,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8}}
def full : List (Finset (Fin 9)) := [{0,3,4},{3,5},{4,5},{3,6},{4,6},{0,1,2,5,6},{0,7},{1,3,7},{2,4,7},{5,7},{6,7},{0,8},{2,3,8},{1,4,8},{5,8},{6,8},{7,8}]
end Case10709
namespace Case10710
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{3},{4},{0,2,4},{1,3,4},{5},{0,5},{1,5},{4,5},{6},{0,6},{1,6},{4,6},{7},{0,7},{1,7},{2,3,5,6,7},{8},{1,2,8},{0,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 3 else if T={4} then 1 else if T={0,2,4} then 1 else if T={1,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={4,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,3,5,6,7} then 1 else if T={8} then 2 else if T={1,2,8} then 1 else if T={0,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[14],3⟩,⟨[15],1⟩,⟨[11,13,15],1⟩,⟨[12,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[18],3⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,14,16,17,18],1⟩,⟨[19],2⟩,⟨[12,13,19],1⟩,⟨[11,14,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10710
namespace Case10710
def big : Finset (Finset (Fin 9)) := {{0,2,4},{1,3,4},{2,3,5,6,7},{1,2,8},{0,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2,4},{1,3,4},{0,5},{1,5},{4,5},{0,6},{1,6},{4,6},{0,7},{1,7},{2,3,5,6,7},{1,2,8},{0,3,8},{5,8},{6,8},{4,7,8}]
end Case10710
namespace Case10711
def positionFn : Fin 9 → Fin 25 := ![8,9,10,11,12,13,14,15,16]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{3},{0,2,3},{4},{1,2,4},{5},{0,5},{1,5},{3,5},{4,5},{6},{0,6},{1,6},{3,6},{4,6},{7},{0,7},{1,7},{3,4,7},{8},{1,3,8},{0,4,8},{2,5,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={1,2,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={8} then 4 else if T={1,3,8} then 1 else if T={0,4,8} then 1 else if T={2,5,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,16,17],[⟨[],1⟩,⟨[9,10],1⟩,⟨[11],3⟩,⟨[12],1⟩,⟨[9,11,12],1⟩,⟨[13],1⟩,⟨[10,11,13],1⟩,⟨[14],2⟩,⟨[9,14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[9,15],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],3⟩,⟨[9,16],1⟩,⟨[10,16],1⟩,⟨[12,13,16],1⟩,⟨[17],4⟩,⟨[10,12,17],1⟩,⟨[9,13,17],1⟩,⟨[11,14,15,16,17],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10711
namespace Case10711
def big : Finset (Finset (Fin 9)) := {{0,2,3},{1,2,4},{3,4,7},{1,3,8},{0,4,8},{2,5,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2,3},{1,2,4},{0,5},{1,5},{3,5},{4,5},{0,6},{1,6},{3,6},{4,6},{0,7},{1,7},{3,4,7},{1,3,8},{0,4,8},{2,5,6,7,8}]
end Case10711
namespace Case10712
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,1,3},{4},{0,2,4},{5},{0,5},{3,5},{4,5},{6},{0,6},{3,6},{4,6},{7},{0,7},{3,4,7},{1,2,5,6,7},{8},{0,8},{2,3,8},{1,4,8},{5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 3 else if T={2} then 3 else if T={3} then 1 else if T={0,1,3} then 1 else if T={4} then 1 else if T={0,2,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={1,2,5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],3⟩,⟨[12],3⟩,⟨[13],1⟩,⟨[10,11,13],1⟩,⟨[14],1⟩,⟨[10,12,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],3⟩,⟨[10,17],1⟩,⟨[13,14,17],1⟩,⟨[11,12,15,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10712
namespace Case10712
def big : Finset (Finset (Fin 9)) := {{0,1,3},{0,2,4},{3,4,7},{1,2,5,6,7},{2,3,8},{1,4,8}}
def full : List (Finset (Fin 9)) := [{0,1,3},{0,2,4},{0,5},{3,5},{4,5},{0,6},{3,6},{4,6},{0,7},{3,4,7},{1,2,5,6,7},{0,8},{2,3,8},{1,4,8},{5,8},{6,8},{7,8}]
end Case10712
namespace Case10713
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{5},{0,5},{1,5},{6},{0,6},{2,6},{3,5,6},{7},{0,1,7},{2,5,7},{4,6,7},{8},{0,2,8},{4,5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,5,6} then 1 else if T={7} then 3 else if T={0,1,7} then 1 else if T={2,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={0,2,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[14,16,17],1⟩,⟨[18],3⟩,⟨[11,12,18],1⟩,⟨[13,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],3⟩,⟨[11,13,19],1⟩,⟨[15,16,19],1⟩,⟨[12,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10713
namespace Case10713
def big : Finset (Finset (Fin 9)) := {{3,5,6},{0,1,7},{2,5,7},{4,6,7},{0,2,8},{4,5,8},{1,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,4},{0,5},{1,5},{0,6},{2,6},{3,5,6},{0,1,7},{2,5,7},{4,6,7},{0,2,8},{4,5,8},{1,6,8},{3,7,8}]
end Case10713
namespace Case10714
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1,2},{0,3},{1,3},{2,3},{4},{0,4},{2,4},{5},{0,5},{1,5},{2,5},{3,5},{6},{0,6},{1,6},{3,4,6},{7},{0,2,7},{1,4,7},{5,6,7},{8},{0,1,8},{4,5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,4,6} then 1 else if T={7} then 3 else if T={0,2,7} then 1 else if T={1,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={4,5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[11,12],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[13,14,16],1⟩,⟨[17],3⟩,⟨[10,12,17],1⟩,⟨[11,14,17],1⟩,⟨[15,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[14,15,18],1⟩,⟨[12,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10714
namespace Case10714
def big : Finset (Finset (Fin 9)) := {{3,4,6},{0,2,7},{1,4,7},{5,6,7},{0,1,8},{4,5,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{2,5},{3,5},{0,6},{1,6},{3,4,6},{0,2,7},{1,4,7},{5,6,7},{0,1,8},{4,5,8},{2,6,8},{3,7,8}]
end Case10714
namespace Case10715
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1,2},{0,3},{1,3},{2,3},{4},{0,1,4},{5},{0,5},{1,5},{2,5},{3,5},{6},{0,6},{1,6},{2,4,6},{7},{0,7},{2,7},{4,5,7},{3,6,7},{8},{0,2,8},{3,4,8},{5,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={4,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 3 else if T={0,2,8} then 1 else if T={3,4,8} then 1 else if T={5,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[11,12,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,15,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,18],1⟩,⟨[15,16,18],1⟩,⟨[14,17,18],1⟩,⟨[19],3⟩,⟨[11,13,19],1⟩,⟨[14,15,19],1⟩,⟨[16,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10715
namespace Case10715
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,4,6},{4,5,7},{3,6,7},{0,2,8},{3,4,8},{5,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{2,3},{0,1,4},{0,5},{1,5},{2,5},{3,5},{0,6},{1,6},{2,4,6},{0,7},{2,7},{4,5,7},{3,6,7},{0,2,8},{3,4,8},{5,6,8},{1,7,8}]
end Case10715
namespace Case10716
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1,2},{0,3},{1,3},{2,3},{4},{0,4},{2,4},{5},{0,5},{1,5},{2,5},{3,5},{6},{0,6},{1,6},{4,5,6},{7},{0,1,7},{3,4,7},{2,6,7},{8},{0,2,8},{1,4,8},{3,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={4,5,6} then 1 else if T={7} then 3 else if T={0,1,7} then 1 else if T={3,4,7} then 1 else if T={2,6,7} then 1 else if T={8} then 3 else if T={0,2,8} then 1 else if T={1,4,8} then 1 else if T={3,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[11,12],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[14,15,16],1⟩,⟨[17],3⟩,⟨[10,11,17],1⟩,⟨[13,14,17],1⟩,⟨[12,16,17],1⟩,⟨[18],3⟩,⟨[10,12,18],1⟩,⟨[11,14,18],1⟩,⟨[13,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10716
namespace Case10716
def big : Finset (Finset (Fin 9)) := {{4,5,6},{0,1,7},{3,4,7},{2,6,7},{0,2,8},{1,4,8},{3,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{2,5},{3,5},{0,6},{1,6},{4,5,6},{0,1,7},{3,4,7},{2,6,7},{0,2,8},{1,4,8},{3,6,8},{5,7,8}]
end Case10716
namespace Case10717
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1,2},{0,3},{1,3},{2,3},{4},{0,1,4},{5},{0,5},{1,5},{2,5},{3,5},{6},{0,6},{2,6},{3,4,6},{7},{0,7},{1,7},{2,4,7},{5,6,7},{8},{0,2,8},{4,5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 3 else if T={0,2,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[11,12,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[14,15,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,15,18],1⟩,⟨[16,17,18],1⟩,⟨[19],3⟩,⟨[11,13,19],1⟩,⟨[15,16,19],1⟩,⟨[12,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10717
namespace Case10717
def big : Finset (Finset (Fin 9)) := {{0,1,4},{3,4,6},{2,4,7},{5,6,7},{0,2,8},{4,5,8},{1,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{2,3},{0,1,4},{0,5},{1,5},{2,5},{3,5},{0,6},{2,6},{3,4,6},{0,7},{1,7},{2,4,7},{5,6,7},{0,2,8},{4,5,8},{1,6,8},{3,7,8}]
end Case10717
namespace Case10718
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1,2},{3},{0,3},{1,3},{4},{0,4},{2,4},{5},{0,5},{1,5},{2,5},{3,4,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{0,1,7},{2,3,7},{4,6,7},{8},{0,2,8},{1,4,8},{3,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={0,1,7} then 1 else if T={2,3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={0,2,8} then 1 else if T={1,4,8} then 1 else if T={3,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[10,11,17],1⟩,⟨[12,13,17],1⟩,⟨[14,16,17],1⟩,⟨[18],3⟩,⟨[10,12,18],1⟩,⟨[11,14,18],1⟩,⟨[13,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10718
namespace Case10718
def big : Finset (Finset (Fin 9)) := {{3,4,5},{0,1,7},{2,3,7},{4,6,7},{0,2,8},{1,4,8},{3,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{0,4},{2,4},{0,5},{1,5},{2,5},{3,4,5},{0,6},{1,6},{2,6},{5,6},{0,1,7},{2,3,7},{4,6,7},{0,2,8},{1,4,8},{3,6,8},{5,7,8}]
end Case10718
namespace Case10719
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1,2},{3},{0,3},{1,3},{4},{0,1,4},{2,3,4},{5},{0,5},{1,5},{2,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{0,7},{2,7},{3,5,7},{4,6,7},{8},{0,2,8},{4,5,8},{3,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={0,2,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[11,12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,18],1⟩,⟨[14,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],3⟩,⟨[11,13,19],1⟩,⟨[15,16,19],1⟩,⟨[14,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10719
namespace Case10719
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,3,4},{3,5,7},{4,6,7},{0,2,8},{4,5,8},{3,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{0,1,4},{2,3,4},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{5,6},{0,7},{2,7},{3,5,7},{4,6,7},{0,2,8},{4,5,8},{3,6,8},{1,7,8}]
end Case10719
namespace Case10720
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1,2},{3},{0,3},{2,3},{4},{0,1,4},{5},{0,5},{1,5},{2,5},{3,4,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{0,7},{1,7},{2,4,7},{3,6,7},{8},{0,2,8},{1,3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={3,6,7} then 1 else if T={8} then 3 else if T={0,2,8} then 1 else if T={1,3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,14,17],1⟩,⟨[13,16,17],1⟩,⟨[18],3⟩,⟨[10,12,18],1⟩,⟨[11,13,18],1⟩,⟨[14,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10720
namespace Case10720
def big : Finset (Finset (Fin 9)) := {{0,1,4},{3,4,5},{2,4,7},{3,6,7},{0,2,8},{1,3,8},{4,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{2,3},{0,1,4},{0,5},{1,5},{2,5},{3,4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,4,7},{3,6,7},{0,2,8},{1,3,8},{4,6,8},{5,7,8}]
end Case10720
namespace Case10721
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1,2},{3},{0,1,3},{4},{0,2,4},{5},{0,5},{1,5},{2,5},{3,4,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{0,7},{1,7},{2,3,7},{4,6,7},{8},{0,8},{2,8},{1,4,8},{3,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1,2} then 1 else if T={3} then 2 else if T={0,1,3} then 1 else if T={4} then 2 else if T={0,2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,4,8} then 1 else if T={3,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[10,11,13],1⟩,⟨[14],2⟩,⟨[10,12,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,13,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,18],1⟩,⟨[11,14,18],1⟩,⟨[13,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10721
namespace Case10721
def big : Finset (Finset (Fin 9)) := {{0,1,3},{0,2,4},{3,4,5},{2,3,7},{4,6,7},{1,4,8},{3,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,1,3},{0,2,4},{0,5},{1,5},{2,5},{3,4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,3,7},{4,6,7},{0,8},{2,8},{1,4,8},{3,6,8},{5,7,8}]
end Case10721
namespace Case10722
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{2,3},{4},{0,4},{1,4},{5},{1,5},{2,5},{3,5},{6},{0,6},{2,4,6},{5,6},{7},{0,1,7},{4,5,7},{3,6,7},{8},{3,4,8},{0,5,8},{1,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={0,1,7} then 1 else if T={4,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 3 else if T={3,4,8} then 1 else if T={0,5,8} then 1 else if T={1,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[11,12,18],1⟩,⟨[15,16,18],1⟩,⟨[14,17,18],1⟩,⟨[19],3⟩,⟨[14,15,19],1⟩,⟨[11,16,19],1⟩,⟨[12,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10722
namespace Case10722
def big : Finset (Finset (Fin 9)) := {{2,4,6},{0,1,7},{4,5,7},{3,6,7},{3,4,8},{0,5,8},{1,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{1,5},{2,5},{3,5},{0,6},{2,4,6},{5,6},{0,1,7},{4,5,7},{3,6,7},{3,4,8},{0,5,8},{1,6,8},{2,7,8}]
end Case10722
namespace Case10723
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{2,3},{4},{1,4},{5},{0,5},{2,5},{3,5},{4,5},{6},{0,6},{1,6},{2,4,6},{7},{0,1,7},{3,4,7},{5,6,7},{8},{0,4,8},{1,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,4,6} then 1 else if T={7} then 3 else if T={0,1,7} then 1 else if T={3,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 3 else if T={0,4,8} then 1 else if T={1,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,15,17],1⟩,⟨[18],3⟩,⟨[11,12,18],1⟩,⟨[14,15,18],1⟩,⟨[16,17,18],1⟩,⟨[19],3⟩,⟨[11,15,19],1⟩,⟨[12,16,19],1⟩,⟨[14,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10723
namespace Case10723
def big : Finset (Finset (Fin 9)) := {{2,4,6},{0,1,7},{3,4,7},{5,6,7},{0,4,8},{1,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{2,3},{1,4},{0,5},{2,5},{3,5},{4,5},{0,6},{1,6},{2,4,6},{0,1,7},{3,4,7},{5,6,7},{0,4,8},{1,5,8},{3,6,8},{2,7,8}]
end Case10723
namespace Case10724
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{2,3},{4},{0,1,4},{5},{1,5},{2,5},{3,5},{6},{0,6},{2,4,6},{5,6},{7},{0,7},{1,7},{4,5,7},{3,6,7},{8},{3,4,8},{0,5,8},{1,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={4,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 3 else if T={3,4,8} then 1 else if T={0,5,8} then 1 else if T={1,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[11,12,15],1⟩,⟨[16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[15,16,18],1⟩,⟨[14,17,18],1⟩,⟨[19],3⟩,⟨[14,15,19],1⟩,⟨[11,16,19],1⟩,⟨[12,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10724
namespace Case10724
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,4,6},{4,5,7},{3,6,7},{3,4,8},{0,5,8},{1,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{2,3},{0,1,4},{1,5},{2,5},{3,5},{0,6},{2,4,6},{5,6},{0,7},{1,7},{4,5,7},{3,6,7},{3,4,8},{0,5,8},{1,6,8},{2,7,8}]
end Case10724
namespace Case10725
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{2,3},{4},{5},{1,5},{2,5},{3,5},{0,4,5},{6},{0,6},{1,4,6},{5,6},{7},{0,7},{1,7},{2,4,7},{3,6,7},{8},{0,1,8},{3,4,8},{2,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={3,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={3,4,8} then 1 else if T={2,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[11,15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,15,18],1⟩,⟨[14,17,18],1⟩,⟨[19],3⟩,⟨[11,12,19],1⟩,⟨[14,15,19],1⟩,⟨[13,17,19],1⟩,⟨[16,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10725
namespace Case10725
def big : Finset (Finset (Fin 9)) := {{0,4,5},{1,4,6},{2,4,7},{3,6,7},{0,1,8},{3,4,8},{2,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{2,3},{1,5},{2,5},{3,5},{0,4,5},{0,6},{1,4,6},{5,6},{0,7},{1,7},{2,4,7},{3,6,7},{0,1,8},{3,4,8},{2,6,8},{5,7,8}]
end Case10725
namespace Case10726
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{3},{1,3},{4},{0,4},{1,4},{2,3,4},{5},{0,5},{2,5},{3,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{0,1,7},{4,5,7},{3,6,7},{8},{0,3,8},{1,5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={0,1,7} then 1 else if T={4,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 3 else if T={0,3,8} then 1 else if T={1,5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[11,12,18],1⟩,⟨[15,16,18],1⟩,⟨[14,17,18],1⟩,⟨[19],3⟩,⟨[11,14,19],1⟩,⟨[12,16,19],1⟩,⟨[15,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10726
namespace Case10726
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,1,7},{4,5,7},{3,6,7},{0,3,8},{1,5,8},{4,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{0,4},{1,4},{2,3,4},{0,5},{2,5},{3,5},{0,6},{1,6},{2,6},{5,6},{0,1,7},{4,5,7},{3,6,7},{0,3,8},{1,5,8},{4,6,8},{2,7,8}]
end Case10726
namespace Case10727
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{3},{0,3},{1,3},{4},{0,1,4},{5},{1,5},{2,5},{3,4,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{0,7},{2,3,7},{5,7},{4,6,7},{8},{2,4,8},{0,5,8},{3,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={2,4,8} then 1 else if T={0,5,8} then 1 else if T={3,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,13,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],3⟩,⟨[12,14,18],1⟩,⟨[10,15,18],1⟩,⟨[13,16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case10727
namespace Case10727
def big : Finset (Finset (Fin 9)) := {{0,1,4},{3,4,5},{2,3,7},{4,6,7},{2,4,8},{0,5,8},{3,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{0,1,4},{1,5},{2,5},{3,4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{2,3,7},{5,7},{4,6,7},{2,4,8},{0,5,8},{3,6,8},{1,7,8}]
end Case10727
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case7632
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{3},{4},{2,4},{5},{1,5},{0,3,4,5},{6},{0,6},{1,2,3,6},{7},{0,7},{2,7},{1,4,7},{5,6,7},{8},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 3 else if T={4} then 2 else if T={2,4} then 1 else if T={5} then 3 else if T={1,5} then 1 else if T={0,3,4,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,2,3,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],3⟩,⟨[14],2⟩,⟨[12,14],1⟩,⟨[15],3⟩,⟨[11,15],1⟩,⟨[10,13,14,15],1⟩,⟨[16],3⟩,⟨[10,16],1⟩,⟨[11,12,13,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[11,14,17],1⟩,⟨[15,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,15,18],1⟩,⟨[14,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7632
namespace Case7632
def big : Finset (Finset (Fin 9)) := {{0,3,4,5},{1,2,3,6},{1,4,7},{5,6,7},{2,5,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{2,4},{1,5},{0,3,4,5},{0,6},{1,2,3,6},{0,7},{2,7},{1,4,7},{5,6,7},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]
end Case7632
namespace Case7633
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{3},{4},{0,4},{1,2,3,4},{5},{2,5},{6},{1,6},{0,3,5,6},{7},{0,7},{2,7},{1,5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 3 else if T={4} then 2 else if T={0,4} then 1 else if T={1,2,3,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],3⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[12,13,14,15],1⟩,⟨[16],3⟩,⟨[13,16],1⟩,⟨[17],3⟩,⟨[12,17],1⟩,⟨[11,14,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,18],1⟩,⟨[12,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[15,16,19],1⟩,⟨[13,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7633
namespace Case7633
def big : Finset (Finset (Fin 9)) := {{1,2,3,4},{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{0,4},{1,2,3,4},{2,5},{1,6},{0,3,5,6},{0,7},{2,7},{1,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]
end Case7633
namespace Case7634
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{3},{4},{0,4},{2,4},{5},{2,5},{1,4,5},{6},{1,6},{0,3,5,6},{7},{0,7},{1,2,3,7},{4,6,7},{8},{0,8},{1,8},{3,4,8},{2,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 3 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={1,4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={1,2,3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,4,8} then 1 else if T={2,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[11,14,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[10,13,15,16],1⟩,⟨[17],3⟩,⟨[10,17],1⟩,⟨[11,12,13,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[13,14,18],1⟩,⟨[12,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7634
namespace Case7634
def big : Finset (Finset (Fin 9)) := {{1,4,5},{0,3,5,6},{1,2,3,7},{4,6,7},{3,4,8},{2,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{0,4},{2,4},{2,5},{1,4,5},{1,6},{0,3,5,6},{0,7},{1,2,3,7},{4,6,7},{0,8},{1,8},{3,4,8},{2,6,8},{5,7,8}]
end Case7634
namespace Case7635
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{3},{2,3},{4},{1,4},{5},{0,3,4,5},{6},{0,6},{1,2,5,6},{7},{0,7},{2,7},{1,3,7},{4,6,7},{8},{0,8},{1,8},{2,4,8},{3,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={5} then 4 else if T={0,3,4,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,2,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={3,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],4⟩,⟨[10,13,14,15],1⟩,⟨[16],3⟩,⟨[10,16],1⟩,⟨[11,12,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[11,13,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[13,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7635
namespace Case7635
def big : Finset (Finset (Fin 9)) := {{0,3,4,5},{1,2,5,6},{1,3,7},{4,6,7},{2,4,8},{3,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{2,3},{1,4},{0,3,4,5},{0,6},{1,2,5,6},{0,7},{2,7},{1,3,7},{4,6,7},{0,8},{1,8},{2,4,8},{3,6,8},{5,7,8}]
end Case7635
namespace Case7636
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{3},{2,3},{4},{0,4},{5},{1,2,4,5},{6},{1,6},{0,3,5,6},{7},{0,7},{2,7},{1,3,7},{4,6,7},{8},{0,8},{1,8},{3,4,8},{2,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={5} then 4 else if T={1,2,4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,4,8} then 1 else if T={2,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[10,14],1⟩,⟨[15],4⟩,⟨[11,12,14,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[10,13,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[11,13,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[13,14,18],1⟩,⟨[12,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7636
namespace Case7636
def big : Finset (Finset (Fin 9)) := {{1,2,4,5},{0,3,5,6},{1,3,7},{4,6,7},{3,4,8},{2,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{2,3},{0,4},{1,2,4,5},{1,6},{0,3,5,6},{0,7},{2,7},{1,3,7},{4,6,7},{0,8},{1,8},{3,4,8},{2,6,8},{5,7,8}]
end Case7636
namespace Case7637
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{3},{2,3},{4},{0,4},{2,4},{1,3,4},{5},{6},{1,6},{0,3,5,6},{7},{0,7},{1,2,5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={1,3,4} then 1 else if T={5} then 4 else if T={6} then 3 else if T={1,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={1,2,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[12,14,15],1⟩,⟨[16],4⟩,⟨[17],3⟩,⟨[12,17],1⟩,⟨[11,14,16,17],1⟩,⟨[18],3⟩,⟨[11,18],1⟩,⟨[12,13,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[15,16,19],1⟩,⟨[13,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7637
namespace Case7637
def big : Finset (Finset (Fin 9)) := {{1,3,4},{0,3,5,6},{1,2,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{2,3},{0,4},{2,4},{1,3,4},{1,6},{0,3,5,6},{0,7},{1,2,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]
end Case7637
namespace Case7638
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{3},{2,3},{4},{0,4},{1,4},{5},{6},{1,6},{2,4,6},{0,3,5,6},{7},{0,7},{3,4,7},{1,2,5,7},{8},{0,8},{2,8},{1,3,8},{4,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 4 else if T={6} then 3 else if T={1,6} then 1 else if T={2,4,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={1,2,5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,3,8} then 1 else if T={4,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],4⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[12,14,16],1⟩,⟨[10,13,15,16],1⟩,⟨[17],3⟩,⟨[10,17],1⟩,⟨[13,14,17],1⟩,⟨[11,12,15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,18],1⟩,⟨[11,13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7638
namespace Case7638
def big : Finset (Finset (Fin 9)) := {{2,4,6},{0,3,5,6},{3,4,7},{1,2,5,7},{1,3,8},{4,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{2,3},{0,4},{1,4},{1,6},{2,4,6},{0,3,5,6},{0,7},{3,4,7},{1,2,5,7},{0,8},{2,8},{1,3,8},{4,5,8},{6,7,8}]
end Case7638
namespace Case7639
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{3},{0,3},{4},{0,4},{2,4},{5},{1,2,3,5},{6},{2,6},{1,4,6},{7},{1,7},{3,4,7},{0,5,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 4 else if T={1,2,3,5} then 1 else if T={6} then 3 else if T={2,6} then 1 else if T={1,4,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],4⟩,⟨[11,12,13,15],1⟩,⟨[16],3⟩,⟨[12,16],1⟩,⟨[11,14,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[13,14,17],1⟩,⟨[10,15,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[14,15,18],1⟩,⟨[13,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7639
namespace Case7639
def big : Finset (Finset (Fin 9)) := {{1,2,3,5},{1,4,6},{3,4,7},{0,5,6,7},{4,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{0,3},{0,4},{2,4},{1,2,3,5},{2,6},{1,4,6},{1,7},{3,4,7},{0,5,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
end Case7639
namespace Case7640
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{3},{0,3},{2,3},{4},{0,4},{1,4},{5},{3,4,5},{6},{2,6},{1,3,6},{7},{1,7},{2,4,7},{0,5,6,7},{8},{0,8},{1,2,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 4 else if T={3,4,5} then 1 else if T={6} then 3 else if T={2,6} then 1 else if T={1,3,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={1,2,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],4⟩,⟨[13,14,15],1⟩,⟨[16],3⟩,⟨[12,16],1⟩,⟨[11,13,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[12,14,17],1⟩,⟨[10,15,16,17],1⟩,⟨[18],3⟩,⟨[10,18],1⟩,⟨[11,12,15,18],1⟩,⟨[14,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7640
namespace Case7640
def big : Finset (Finset (Fin 9)) := {{3,4,5},{1,3,6},{2,4,7},{0,5,6,7},{1,2,5,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{0,3},{2,3},{0,4},{1,4},{3,4,5},{2,6},{1,3,6},{1,7},{2,4,7},{0,5,6,7},{0,8},{1,2,5,8},{4,6,8},{3,7,8}]
end Case7640
namespace Case7641
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{3},{4},{1,4},{0,2,3,4},{5},{0,5},{3,5},{6},{0,6},{1,2,5,6},{7},{0,7},{1,3,7},{5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={4} then 2 else if T={1,4} then 1 else if T={0,2,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={3,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,2,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[14],2⟩,⟨[15],2⟩,⟨[12,15],1⟩,⟨[11,13,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[14,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[12,13,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[15,16,19],1⟩,⟨[14,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7641
namespace Case7641
def big : Finset (Finset (Fin 9)) := {{0,2,3,4},{1,2,5,6},{1,3,7},{4,6,7},{4,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,4},{0,2,3,4},{0,5},{3,5},{0,6},{1,2,5,6},{0,7},{1,3,7},{5,7},{4,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
end Case7641
namespace Case7642
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{3},{4},{0,4},{5},{0,5},{3,5},{1,2,4,5},{6},{1,6},{0,2,3,6},{7},{0,7},{1,3,7},{5,7},{4,6,7},{8},{0,8},{1,8},{3,4,8},{5,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={4} then 2 else if T={0,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={3,5} then 1 else if T={1,2,4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={0,2,3,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,4,8} then 1 else if T={5,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[10,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[13,15],1⟩,⟨[11,12,14,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[10,12,13,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,13,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[13,14,18],1⟩,⟨[15,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7642
namespace Case7642
def big : Finset (Finset (Fin 9)) := {{1,2,4,5},{0,2,3,6},{1,3,7},{4,6,7},{3,4,8},{5,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,4},{0,5},{3,5},{1,2,4,5},{1,6},{0,2,3,6},{0,7},{1,3,7},{5,7},{4,6,7},{0,8},{1,8},{3,4,8},{5,6,8},{2,7,8}]
end Case7642
namespace Case7643
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{3},{4},{0,4},{1,3,4},{5},{0,5},{3,5},{4,5},{6},{0,6},{1,2,5,6},{7},{1,7},{0,2,3,7},{4,6,7},{8},{0,8},{1,8},{2,4,8},{3,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,2,5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={0,2,3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={3,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,13,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[10,16],1⟩,⟨[11,12,15,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[10,12,13,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[13,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7643
namespace Case7643
def big : Finset (Finset (Fin 9)) := {{1,3,4},{1,2,5,6},{0,2,3,7},{4,6,7},{2,4,8},{3,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,4},{1,3,4},{0,5},{3,5},{4,5},{0,6},{1,2,5,6},{1,7},{0,2,3,7},{4,6,7},{0,8},{1,8},{2,4,8},{3,6,8},{5,7,8}]
end Case7643
namespace Case7644
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{3},{4},{0,4},{1,4},{5},{0,5},{3,5},{6},{0,6},{3,4,6},{1,2,5,6},{7},{1,7},{0,2,3,7},{4,5,7},{8},{0,8},{1,3,8},{2,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={3,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={3,4,6} then 1 else if T={1,2,5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={0,2,3,7} then 1 else if T={4,5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[13,15],1⟩,⟨[16],3⟩,⟨[10,16],1⟩,⟨[13,14,16],1⟩,⟨[11,12,15,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[10,12,13,17],1⟩,⟨[14,15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,13,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7644
namespace Case7644
def big : Finset (Finset (Fin 9)) := {{3,4,6},{1,2,5,6},{0,2,3,7},{4,5,7},{1,3,8},{2,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,4},{1,4},{0,5},{3,5},{0,6},{3,4,6},{1,2,5,6},{1,7},{0,2,3,7},{4,5,7},{0,8},{1,3,8},{2,4,8},{5,8},{6,7,8}]
end Case7644
namespace Case7645
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{3},{1,3},{4},{0,4},{5},{0,5},{1,2,4,5},{6},{0,2,3,6},{5,6},{7},{0,7},{3,4,7},{5,7},{1,6,7},{8},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,2,4,5} then 1 else if T={6} then 3 else if T={0,2,3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[10,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[11,12,14,15],1⟩,⟨[16],3⟩,⟨[10,12,13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[11,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[13,15,18],1⟩,⟨[14,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7645
namespace Case7645
def big : Finset (Finset (Fin 9)) := {{1,2,4,5},{0,2,3,6},{3,4,7},{1,6,7},{3,5,8},{4,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{0,4},{0,5},{1,2,4,5},{0,2,3,6},{5,6},{0,7},{3,4,7},{5,7},{1,6,7},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]
end Case7645
namespace Case7646
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{3},{1,3},{4},{0,4},{5},{0,5},{4,5},{6},{0,2,3,6},{1,4,6},{5,6},{7},{0,7},{3,4,7},{1,2,5,7},{8},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={0,2,3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={1,2,5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[14],2⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[11,13,14,17],1⟩,⟨[12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[11,18],1⟩,⟨[14,15,18],1⟩,⟨[12,13,16,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,15,19],1⟩,⟨[14,16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7646
namespace Case7646
def big : Finset (Finset (Fin 9)) := {{0,2,3,6},{1,4,6},{3,4,7},{1,2,5,7},{2,4,8},{3,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{0,4},{0,5},{4,5},{0,2,3,6},{1,4,6},{5,6},{0,7},{3,4,7},{1,2,5,7},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}]
end Case7646
namespace Case7647
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{3},{1,3},{4},{0,4},{1,4},{5},{0,5},{3,4,5},{6},{0,2,3,6},{5,6},{7},{0,7},{1,2,5,7},{4,6,7},{8},{0,8},{2,4,8},{5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={3,4,5} then 1 else if T={6} then 3 else if T={0,2,3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={1,2,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[13,14,15],1⟩,⟨[16],3⟩,⟨[10,12,13,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[10,17],1⟩,⟨[11,12,15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[11,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7647
namespace Case7647
def big : Finset (Finset (Fin 9)) := {{3,4,5},{0,2,3,6},{1,2,5,7},{4,6,7},{2,4,8},{1,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{0,4},{1,4},{0,5},{3,4,5},{0,2,3,6},{5,6},{0,7},{1,2,5,7},{4,6,7},{0,8},{2,4,8},{5,8},{1,6,8},{3,7,8}]
end Case7647
namespace Case7648
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{3},{0,3},{4},{0,4},{5},{0,5},{1,2,3,5},{4,5},{6},{1,4,6},{5,6},{7},{1,7},{3,4,7},{0,2,6,7},{8},{0,8},{1,8},{2,4,8},{3,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={3,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[14,15,18],1⟩,⟨[11,13,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,15,19],1⟩,⟨[14,17,19],1⟩,⟨[16,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7648
namespace Case7648
def big : Finset (Finset (Fin 9)) := {{1,2,3,5},{1,4,6},{3,4,7},{0,2,6,7},{2,4,8},{3,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,3},{0,4},{0,5},{1,2,3,5},{4,5},{1,4,6},{5,6},{1,7},{3,4,7},{0,2,6,7},{0,8},{1,8},{2,4,8},{3,6,8},{5,7,8}]
end Case7648
namespace Case7649
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{3},{0,3},{4},{0,4},{1,4},{5},{0,5},{1,2,3,5},{6},{3,4,6},{5,6},{7},{1,7},{4,5,7},{0,2,6,7},{8},{0,8},{2,4,8},{5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,2,3,5} then 1 else if T={6} then 3 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={4,5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[11,12,13,15],1⟩,⟨[16],3⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[14,15,17],1⟩,⟨[10,12,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[11,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7649
namespace Case7649
def big : Finset (Finset (Fin 9)) := {{1,2,3,5},{3,4,6},{4,5,7},{0,2,6,7},{2,4,8},{1,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,3},{0,4},{1,4},{0,5},{1,2,3,5},{3,4,6},{5,6},{1,7},{4,5,7},{0,2,6,7},{0,8},{2,4,8},{5,8},{1,6,8},{3,7,8}]
end Case7649
namespace Case7650
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{3},{0,3},{4},{0,4},{1,4},{2,3,4},{5},{0,5},{3,5},{6},{1,3,6},{5,6},{7},{1,7},{4,5,7},{0,2,6,7},{8},{0,8},{1,2,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 3 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={3,5} then 1 else if T={6} then 3 else if T={1,3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={4,5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={1,2,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[14,16],1⟩,⟨[17],3⟩,⟨[12,14,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[15,16,18],1⟩,⟨[11,13,17,18],1⟩,⟨[19],3⟩,⟨[11,19],1⟩,⟨[12,13,16,19],1⟩,⟨[15,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7650
namespace Case7650
def big : Finset (Finset (Fin 9)) := {{2,3,4},{1,3,6},{4,5,7},{0,2,6,7},{1,2,5,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,3},{0,4},{1,4},{2,3,4},{0,5},{3,5},{1,3,6},{5,6},{1,7},{4,5,7},{0,2,6,7},{0,8},{1,2,5,8},{4,6,8},{3,7,8}]
end Case7650
namespace Case7651
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{3},{0,3},{4},{1,4},{5},{0,5},{2,5},{6},{0,2,4,6},{1,3,5,6},{7},{0,7},{1,2,7},{3,4,7},{5,7},{8},{0,8},{1,8},{2,3,8},{4,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={2,5} then 1 else if T={6} then 4 else if T={0,2,4,6} then 1 else if T={1,3,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={4,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[10,13],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[16],4⟩,⟨[10,12,14,16],1⟩,⟨[11,13,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7651
namespace Case7651
def big : Finset (Finset (Fin 9)) := {{0,2,4,6},{1,3,5,6},{1,2,7},{3,4,7},{2,3,8},{4,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,3},{1,4},{0,5},{2,5},{0,2,4,6},{1,3,5,6},{0,7},{1,2,7},{3,4,7},{5,7},{0,8},{1,8},{2,3,8},{4,5,8},{6,7,8}]
end Case7651
namespace Case7652
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{3},{1,3},{4},{0,4},{1,2,4},{5},{0,5},{2,5},{4,5},{6},{0,2,3,6},{7},{0,7},{3,4,7},{1,5,6,7},{8},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 4 else if T={0,2,3,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={1,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,12,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],4⟩,⟨[10,12,13,16],1⟩,⟨[17],3⟩,⟨[10,17],1⟩,⟨[13,14,17],1⟩,⟨[11,15,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[13,15,18],1⟩,⟨[14,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7652
namespace Case7652
def big : Finset (Finset (Fin 9)) := {{1,2,4},{0,2,3,6},{3,4,7},{1,5,6,7},{3,5,8},{4,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{0,4},{1,2,4},{0,5},{2,5},{4,5},{0,2,3,6},{0,7},{3,4,7},{1,5,6,7},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]
end Case7652
namespace Case7653
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{3},{1,3},{4},{0,4},{1,4},{5},{0,5},{2,5},{3,4,5},{6},{0,2,3,6},{7},{0,7},{2,4,7},{1,5,6,7},{8},{0,8},{1,2,8},{5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 4 else if T={0,2,3,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={2,4,7} then 1 else if T={1,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],4⟩,⟨[10,12,13,16],1⟩,⟨[17],3⟩,⟨[10,17],1⟩,⟨[12,14,17],1⟩,⟨[11,15,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,12,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7653
namespace Case7653
def big : Finset (Finset (Fin 9)) := {{3,4,5},{0,2,3,6},{2,4,7},{1,5,6,7},{1,2,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{0,4},{1,4},{0,5},{2,5},{3,4,5},{0,2,3,6},{0,7},{2,4,7},{1,5,6,7},{0,8},{1,2,8},{5,8},{4,6,8},{3,7,8}]
end Case7653
namespace Case7654
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{3},{0,3},{4},{0,4},{1,2,4},{5},{0,5},{2,5},{4,5},{6},{1,3,5,6},{7},{1,7},{3,4,7},{0,2,6,7},{8},{0,8},{1,8},{2,3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 4 else if T={1,3,5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,13,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],4⟩,⟨[12,14,16,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[14,15,18],1⟩,⟨[11,13,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,14,19],1⟩,⟨[15,17,19],1⟩,⟨[16,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7654
namespace Case7654
def big : Finset (Finset (Fin 9)) := {{1,2,4},{1,3,5,6},{3,4,7},{0,2,6,7},{2,3,8},{4,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,3},{0,4},{1,2,4},{0,5},{2,5},{4,5},{1,3,5,6},{1,7},{3,4,7},{0,2,6,7},{0,8},{1,8},{2,3,8},{4,6,8},{5,7,8}]
end Case7654
namespace Case7655
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{3},{0,3},{4},{0,4},{1,4},{2,3,4},{5},{0,5},{2,5},{6},{1,3,5,6},{7},{1,7},{4,5,7},{0,2,6,7},{8},{0,8},{1,2,8},{5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={2,5} then 1 else if T={6} then 4 else if T={1,3,5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={4,5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[17],4⟩,⟨[12,14,16,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[15,16,18],1⟩,⟨[11,13,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,13,19],1⟩,⟨[16,19],1⟩,⟨[15,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7655
namespace Case7655
def big : Finset (Finset (Fin 9)) := {{2,3,4},{1,3,5,6},{4,5,7},{0,2,6,7},{1,2,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,3},{0,4},{1,4},{2,3,4},{0,5},{2,5},{1,3,5,6},{1,7},{4,5,7},{0,2,6,7},{0,8},{1,2,8},{5,8},{4,6,8},{3,7,8}]
end Case7655
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

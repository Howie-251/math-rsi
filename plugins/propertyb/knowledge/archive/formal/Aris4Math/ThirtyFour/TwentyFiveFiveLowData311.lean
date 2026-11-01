import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case7464
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,3},{4},{0,4},{1,2,4},{5},{4,5},{6},{1,6},{3,4,6},{0,2,5,6},{7},{0,7},{2,7},{1,3,5,7},{6,7},{8},{0,1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={5} then 3 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,4,6} then 1 else if T={0,2,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,3,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,1,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,12,14],1⟩,⟨[15],3⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[13,14,16],1⟩,⟨[10,12,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[11,13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,11,18],1⟩,⟨[12,13,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7464
namespace Case7464
def big : Finset (Finset (Fin 9)) := {{1,2,4},{3,4,6},{0,2,5,6},{1,3,5,7},{0,1,8},{2,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{1,2,4},{4,5},{1,6},{3,4,6},{0,2,5,6},{0,7},{2,7},{1,3,5,7},{6,7},{0,1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
end Case7464
namespace Case7465
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{3},{0,1,3},{4},{0,4},{5},{3,5},{4,5},{6},{1,6},{3,6},{2,4,6},{7},{0,7},{3,4,7},{1,2,5,7},{6,7},{8},{2,3,8},{1,4,8},{0,5,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 1 else if T={0,1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={1,2,5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={0,5,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[10,11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[15],3⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[12,14,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[13,14,17],1⟩,⟨[11,12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[10,15,16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7465
namespace Case7465
def big : Finset (Finset (Fin 9)) := {{0,1,3},{2,4,6},{3,4,7},{1,2,5,7},{2,3,8},{1,4,8},{0,5,6,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,1,3},{0,4},{3,5},{4,5},{1,6},{3,6},{2,4,6},{0,7},{3,4,7},{1,2,5,7},{6,7},{2,3,8},{1,4,8},{0,5,6,8},{7,8}]
end Case7465
namespace Case7466
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,3},{4},{0,4},{1,2,4},{5},{3,5},{4,5},{6},{0,6},{2,6},{3,4,6},{7},{1,7},{3,7},{0,2,5,7},{6,7},{8},{0,8},{2,3,8},{1,5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={0,1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={3,7} then 1 else if T={0,2,5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[10,11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,12,14],1⟩,⟨[15],3⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[10,12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[10,18],1⟩,⟨[12,13,18],1⟩,⟨[11,15,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7466
namespace Case7466
def big : Finset (Finset (Fin 9)) := {{0,1,3},{1,2,4},{3,4,6},{0,2,5,7},{2,3,8},{1,5,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,3},{0,4},{1,2,4},{3,5},{4,5},{0,6},{2,6},{3,4,6},{1,7},{3,7},{0,2,5,7},{6,7},{0,8},{2,3,8},{1,5,6,8},{4,7,8}]
end Case7466
namespace Case7467
def positionFn : Fin 9 → Fin 25 := ![16,17,18,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{3},{1,2,3},{4},{0,4},{5},{3,5},{4,5},{6},{3,6},{1,4,6},{0,2,5,6},{7},{0,7},{2,7},{3,4,7},{6,7},{8},{0,3,8},{2,4,8},{6,8},{1,5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={0,2,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={0,3,8} then 1 else if T={2,4,8} then 1 else if T={6,8} then 1 else if T={1,5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[17,18,19,20,21,22,23,24,25],[⟨[],1⟩,⟨[17],1⟩,⟨[18],2⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[20],1⟩,⟨[18,19,20],1⟩,⟨[21],1⟩,⟨[17,21],1⟩,⟨[22],3⟩,⟨[20,22],1⟩,⟨[21,22],1⟩,⟨[23],2⟩,⟨[20,23],1⟩,⟨[18,21,23],1⟩,⟨[17,19,22,23],1⟩,⟨[24],2⟩,⟨[17,24],1⟩,⟨[19,24],1⟩,⟨[20,21,24],1⟩,⟨[23,24],1⟩,⟨[25],3⟩,⟨[17,20,25],1⟩,⟨[19,21,25],1⟩,⟨[23,25],1⟩,⟨[18,22,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7467
namespace Case7467
def big : Finset (Finset (Fin 9)) := {{1,2,3},{1,4,6},{0,2,5,6},{3,4,7},{0,3,8},{2,4,8},{1,5,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2,3},{0,4},{3,5},{4,5},{3,6},{1,4,6},{0,2,5,6},{0,7},{2,7},{3,4,7},{6,7},{0,3,8},{2,4,8},{6,8},{1,5,7,8}]
end Case7467
namespace Case7468
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{3},{4},{1,2,4},{5},{0,2,3,5},{4,5},{6},{0,6},{2,6},{3,4,6},{7},{0,7},{3,7},{4,7},{1,5,6,7},{8},{1,3,8},{0,4,8},{5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 2 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={4} then 1 else if T={1,2,4} then 1 else if T={5} then 3 else if T={0,2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,7} then 1 else if T={4,7} then 1 else if T={1,5,6,7} then 1 else if T={8} then 2 else if T={1,3,8} then 1 else if T={0,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],1⟩,⟨[11],2⟩,⟨[10,11],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[11,12,14],1⟩,⟨[15],3⟩,⟨[10,12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[11,15,16,17],1⟩,⟨[18],2⟩,⟨[11,13,18],1⟩,⟨[10,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7468
namespace Case7468
def big : Finset (Finset (Fin 9)) := {{1,2,4},{0,2,3,5},{3,4,6},{1,5,6,7},{1,3,8},{0,4,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2,4},{0,2,3,5},{4,5},{0,6},{2,6},{3,4,6},{0,7},{3,7},{4,7},{1,5,6,7},{1,3,8},{0,4,8},{5,8},{6,8},{2,7,8}]
end Case7468
namespace Case7469
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,3,4},{5},{0,1,2,5},{3,5},{4,5},{6},{0,6},{2,6},{1,3,6},{4,6},{7},{0,7},{1,7},{3,7},{2,4,7},{8},{0,8},{2,3,8},{1,4,8},{5,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={4} then 1 else if T={0,3,4} then 1 else if T={5} then 3 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,3,6} then 1 else if T={4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[15],1⟩,⟨[11,14,15],1⟩,⟨[16],3⟩,⟨[11,12,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[14,18],1⟩,⟨[13,15,18],1⟩,⟨[19],3⟩,⟨[11,19],1⟩,⟨[13,14,19],1⟩,⟨[12,15,19],1⟩,⟨[16,17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7469
namespace Case7469
def big : Finset (Finset (Fin 9)) := {{0,3,4},{0,1,2,5},{1,3,6},{2,4,7},{2,3,8},{1,4,8},{5,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,3,4},{0,1,2,5},{3,5},{4,5},{0,6},{2,6},{1,3,6},{4,6},{0,7},{1,7},{3,7},{2,4,7},{0,8},{2,3,8},{1,4,8},{5,6,7,8}]
end Case7469
namespace Case7470
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{3},{1,2,3},{4},{0,3,4},{5},{3,5},{4,5},{6},{0,6},{3,6},{1,4,6},{7},{0,7},{1,7},{4,7},{2,5,6,7},{8},{2,4,8},{0,1,5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,3,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={4,7} then 1 else if T={2,5,6,7} then 1 else if T={8} then 3 else if T={2,4,8} then 1 else if T={0,1,5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],1⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[11,14,15],1⟩,⟨[16],3⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[14,17],1⟩,⟨[12,15,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[15,18],1⟩,⟨[13,16,17,18],1⟩,⟨[19],3⟩,⟨[13,15,19],1⟩,⟨[11,12,16,19],1⟩,⟨[17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7470
namespace Case7470
def big : Finset (Finset (Fin 9)) := {{1,2,3},{0,3,4},{1,4,6},{2,5,6,7},{2,4,8},{0,1,5,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2,3},{0,3,4},{3,5},{4,5},{0,6},{3,6},{1,4,6},{0,7},{1,7},{4,7},{2,5,6,7},{2,4,8},{0,1,5,8},{6,8},{3,7,8}]
end Case7470
namespace Case7471
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,3},{4},{0,2,4},{5},{3,5},{4,5},{6},{1,6},{2,3,6},{4,6},{7},{2,7},{3,7},{1,4,7},{0,5,6,7},{8},{0,8},{3,4,8},{1,2,5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 1 else if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={0,1,3} then 1 else if T={4} then 1 else if T={0,2,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={4,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={3,7} then 1 else if T={1,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={3,4,8} then 1 else if T={1,2,5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],1⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[10,11,13],1⟩,⟨[14],1⟩,⟨[10,12,14],1⟩,⟨[15],3⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[11,14,17],1⟩,⟨[10,15,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[13,14,18],1⟩,⟨[11,12,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7471
namespace Case7471
def big : Finset (Finset (Fin 9)) := {{0,1,3},{0,2,4},{2,3,6},{1,4,7},{0,5,6,7},{3,4,8},{1,2,5,8}}
def full : List (Finset (Fin 9)) := [{0,1,3},{0,2,4},{3,5},{4,5},{1,6},{2,3,6},{4,6},{2,7},{3,7},{1,4,7},{0,5,6,7},{0,8},{3,4,8},{1,2,5,8},{6,8},{7,8}]
end Case7471
namespace Case7472
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{2,3},{4},{1,4},{5},{1,5},{0,3,4,5},{6},{0,6},{2,6},{1,3,6},{7},{0,7},{1,7},{2,4,7},{5,6,7},{8},{0,1,8},{2,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={5} then 3 else if T={1,5} then 1 else if T={0,3,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,3,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={2,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],3⟩,⟨[11,15],1⟩,⟨[10,13,14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[11,13,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,14,17],1⟩,⟨[15,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[12,15,18],1⟩,⟨[14,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7472
namespace Case7472
def big : Finset (Finset (Fin 9)) := {{0,3,4,5},{1,3,6},{2,4,7},{5,6,7},{0,1,8},{2,5,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{2,3},{1,4},{1,5},{0,3,4,5},{0,6},{2,6},{1,3,6},{0,7},{1,7},{2,4,7},{5,6,7},{0,1,8},{2,5,8},{4,6,8},{3,7,8}]
end Case7472
namespace Case7473
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{2,3},{4},{1,4},{5},{1,5},{0,3,4,5},{6},{0,6},{2,6},{1,3,6},{7},{0,7},{1,7},{2,5,7},{4,6,7},{8},{0,1,8},{2,4,8},{5,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={5} then 3 else if T={1,5} then 1 else if T={0,3,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,3,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={2,4,8} then 1 else if T={5,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],3⟩,⟨[11,15],1⟩,⟨[10,13,14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[11,13,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[12,14,18],1⟩,⟨[15,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7473
namespace Case7473
def big : Finset (Finset (Fin 9)) := {{0,3,4,5},{1,3,6},{2,5,7},{4,6,7},{0,1,8},{2,4,8},{5,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{2,3},{1,4},{1,5},{0,3,4,5},{0,6},{2,6},{1,3,6},{0,7},{1,7},{2,5,7},{4,6,7},{0,1,8},{2,4,8},{5,6,8},{3,7,8}]
end Case7473
namespace Case7474
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{2,3},{4},{0,4},{2,4},{1,3,4},{5},{1,5},{6},{1,6},{0,3,5,6},{7},{0,7},{1,7},{2,5,7},{4,6,7},{8},{0,1,8},{4,5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={1,3,4} then 1 else if T={5} then 3 else if T={1,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={4,5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[12,14,15],1⟩,⟨[16],3⟩,⟨[12,16],1⟩,⟨[17],3⟩,⟨[12,17],1⟩,⟨[11,14,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],3⟩,⟨[11,12,19],1⟩,⟨[15,16,19],1⟩,⟨[13,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7474
namespace Case7474
def big : Finset (Finset (Fin 9)) := {{1,3,4},{0,3,5,6},{2,5,7},{4,6,7},{0,1,8},{4,5,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{2,3},{0,4},{2,4},{1,3,4},{1,5},{1,6},{0,3,5,6},{0,7},{1,7},{2,5,7},{4,6,7},{0,1,8},{4,5,8},{2,6,8},{3,7,8}]
end Case7474
namespace Case7475
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{2,3},{4},{0,4},{1,4},{5},{1,5},{2,4,5},{6},{1,6},{0,3,5,6},{7},{0,7},{2,7},{1,3,7},{4,6,7},{8},{0,1,8},{3,4,8},{2,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 3 else if T={1,5} then 1 else if T={2,4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={3,4,8} then 1 else if T={2,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],3⟩,⟨[11,15],1⟩,⟨[12,14,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[10,13,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[11,13,17],1⟩,⟨[14,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[13,14,18],1⟩,⟨[12,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7475
namespace Case7475
def big : Finset (Finset (Fin 9)) := {{2,4,5},{0,3,5,6},{1,3,7},{4,6,7},{0,1,8},{3,4,8},{2,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{2,3},{0,4},{1,4},{1,5},{2,4,5},{1,6},{0,3,5,6},{0,7},{2,7},{1,3,7},{4,6,7},{0,1,8},{3,4,8},{2,6,8},{5,7,8}]
end Case7475
namespace Case7476
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{2,3},{4},{0,1,4},{5},{1,5},{2,4,5},{6},{1,6},{0,3,5,6},{7},{0,7},{2,7},{1,3,7},{4,6,7},{8},{0,8},{1,8},{3,4,8},{2,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 3 else if T={1,5} then 1 else if T={2,4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,4,8} then 1 else if T={2,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],3⟩,⟨[11,15],1⟩,⟨[12,14,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[10,13,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[11,13,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[13,14,18],1⟩,⟨[12,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7476
namespace Case7476
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,4,5},{0,3,5,6},{1,3,7},{4,6,7},{3,4,8},{2,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{2,3},{0,1,4},{1,5},{2,4,5},{1,6},{0,3,5,6},{0,7},{2,7},{1,3,7},{4,6,7},{0,8},{1,8},{3,4,8},{2,6,8},{5,7,8}]
end Case7476
namespace Case7477
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{1,3},{4},{1,4},{5},{2,5},{0,3,4,5},{6},{0,6},{1,6},{2,3,6},{7},{0,7},{2,7},{1,5,7},{4,6,7},{8},{0,1,8},{2,4,8},{5,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={0,3,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={2,4,8} then 1 else if T={5,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[10,13,14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,13,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[11,15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[12,14,18],1⟩,⟨[15,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7477
namespace Case7477
def big : Finset (Finset (Fin 9)) := {{0,3,4,5},{2,3,6},{1,5,7},{4,6,7},{0,1,8},{2,4,8},{5,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{1,4},{2,5},{0,3,4,5},{0,6},{1,6},{2,3,6},{0,7},{2,7},{1,5,7},{4,6,7},{0,1,8},{2,4,8},{5,6,8},{3,7,8}]
end Case7477
namespace Case7478
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{1,3},{4},{0,4},{2,4},{5},{2,5},{1,4,5},{6},{1,6},{0,3,5,6},{7},{0,7},{1,7},{2,3,7},{4,6,7},{8},{0,1,8},{3,4,8},{2,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={1,4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={3,4,8} then 1 else if T={2,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[11,14,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[10,13,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,13,17],1⟩,⟨[14,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[13,14,18],1⟩,⟨[12,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7478
namespace Case7478
def big : Finset (Finset (Fin 9)) := {{1,4,5},{0,3,5,6},{2,3,7},{4,6,7},{0,1,8},{3,4,8},{2,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{0,4},{2,4},{2,5},{1,4,5},{1,6},{0,3,5,6},{0,7},{1,7},{2,3,7},{4,6,7},{0,1,8},{3,4,8},{2,6,8},{5,7,8}]
end Case7478
namespace Case7479
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{1,3},{4},{0,4},{1,4},{2,3,4},{5},{2,5},{6},{1,6},{0,3,5,6},{7},{0,7},{2,7},{1,5,7},{4,6,7},{8},{0,1,8},{4,5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={4,5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],3⟩,⟨[13,16],1⟩,⟨[17],3⟩,⟨[12,17],1⟩,⟨[11,14,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,18],1⟩,⟨[12,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],3⟩,⟨[11,12,19],1⟩,⟨[15,16,19],1⟩,⟨[13,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7479
namespace Case7479
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,3,5,6},{1,5,7},{4,6,7},{0,1,8},{4,5,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{0,4},{1,4},{2,3,4},{2,5},{1,6},{0,3,5,6},{0,7},{2,7},{1,5,7},{4,6,7},{0,1,8},{4,5,8},{2,6,8},{3,7,8}]
end Case7479
namespace Case7480
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{1,3},{4},{0,1,4},{5},{1,5},{2,4,5},{6},{2,6},{0,3,5,6},{7},{0,7},{1,7},{2,3,7},{4,6,7},{8},{0,8},{2,8},{3,4,8},{1,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 3 else if T={1,5} then 1 else if T={2,4,5} then 1 else if T={6} then 3 else if T={2,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={1,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],3⟩,⟨[11,15],1⟩,⟨[12,14,15],1⟩,⟨[16],3⟩,⟨[12,16],1⟩,⟨[10,13,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,13,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,18],1⟩,⟨[13,14,18],1⟩,⟨[11,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7480
namespace Case7480
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,4,5},{0,3,5,6},{2,3,7},{4,6,7},{3,4,8},{1,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{0,1,4},{1,5},{2,4,5},{2,6},{0,3,5,6},{0,7},{1,7},{2,3,7},{4,6,7},{0,8},{2,8},{3,4,8},{1,6,8},{5,7,8}]
end Case7480
namespace Case7481
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{1,3},{4},{0,4},{2,4},{5},{2,5},{1,4,5},{6},{1,6},{0,3,5,6},{7},{0,7},{1,7},{3,4,7},{2,6,7},{8},{0,1,8},{2,3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={1,4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={2,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={2,3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[11,14,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[10,13,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,14,17],1⟩,⟨[12,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[12,13,18],1⟩,⟨[14,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7481
namespace Case7481
def big : Finset (Finset (Fin 9)) := {{1,4,5},{0,3,5,6},{3,4,7},{2,6,7},{0,1,8},{2,3,8},{4,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{0,4},{2,4},{2,5},{1,4,5},{1,6},{0,3,5,6},{0,7},{1,7},{3,4,7},{2,6,7},{0,1,8},{2,3,8},{4,6,8},{5,7,8}]
end Case7481
namespace Case7482
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{1,3},{4},{0,4},{1,4},{5},{1,5},{2,4,5},{6},{2,6},{0,3,5,6},{7},{0,7},{2,7},{3,4,7},{1,6,7},{8},{0,1,8},{2,3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 3 else if T={1,5} then 1 else if T={2,4,5} then 1 else if T={6} then 3 else if T={2,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={1,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={2,3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],3⟩,⟨[11,15],1⟩,⟨[12,14,15],1⟩,⟨[16],3⟩,⟨[12,16],1⟩,⟨[10,13,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[11,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[12,13,18],1⟩,⟨[14,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7482
namespace Case7482
def big : Finset (Finset (Fin 9)) := {{2,4,5},{0,3,5,6},{3,4,7},{1,6,7},{0,1,8},{2,3,8},{4,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{0,4},{1,4},{1,5},{2,4,5},{2,6},{0,3,5,6},{0,7},{2,7},{3,4,7},{1,6,7},{0,1,8},{2,3,8},{4,6,8},{5,7,8}]
end Case7482
namespace Case7483
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{1,3},{4},{0,1,4},{2,3,4},{5},{2,5},{6},{1,6},{0,3,5,6},{7},{0,7},{2,7},{1,5,7},{4,6,7},{8},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[11,12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],3⟩,⟨[13,16],1⟩,⟨[17],3⟩,⟨[12,17],1⟩,⟨[11,14,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,18],1⟩,⟨[12,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[15,16,19],1⟩,⟨[13,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7483
namespace Case7483
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,3,4},{0,3,5,6},{1,5,7},{4,6,7},{4,5,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{0,1,4},{2,3,4},{2,5},{1,6},{0,3,5,6},{0,7},{2,7},{1,5,7},{4,6,7},{0,8},{1,8},{4,5,8},{2,6,8},{3,7,8}]
end Case7483
namespace Case7484
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{0,3},{2,3},{4},{0,4},{1,4},{5},{2,5},{1,3,5},{6},{1,6},{2,4,6},{7},{1,7},{3,4,7},{0,5,6,7},{8},{0,1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={1,3,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={2,4,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[11,13,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[12,14,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[13,14,17],1⟩,⟨[10,15,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[14,15,18],1⟩,⟨[13,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7484
namespace Case7484
def big : Finset (Finset (Fin 9)) := {{1,3,5},{2,4,6},{3,4,7},{0,5,6,7},{0,1,8},{4,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{2,3},{0,4},{1,4},{2,5},{1,3,5},{1,6},{2,4,6},{1,7},{3,4,7},{0,5,6,7},{0,1,8},{4,5,8},{3,6,8},{2,7,8}]
end Case7484
namespace Case7485
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{0,3},{2,3},{4},{0,1,4},{5},{2,5},{1,3,5},{6},{1,6},{2,4,6},{7},{1,7},{3,4,7},{0,5,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={1,3,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={2,4,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[11,13,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[12,14,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[13,14,17],1⟩,⟨[10,15,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[14,15,18],1⟩,⟨[13,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7485
namespace Case7485
def big : Finset (Finset (Fin 9)) := {{0,1,4},{1,3,5},{2,4,6},{3,4,7},{0,5,6,7},{4,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{2,3},{0,1,4},{2,5},{1,3,5},{1,6},{2,4,6},{1,7},{3,4,7},{0,5,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
end Case7485
namespace Case7486
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{0,3},{1,3},{4},{0,1,4},{5},{1,5},{2,3,5},{6},{1,6},{2,4,6},{7},{2,7},{3,4,7},{0,5,6,7},{8},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 3 else if T={1,5} then 1 else if T={2,3,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={2,4,6} then 1 else if T={7} then 3 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],3⟩,⟨[11,15],1⟩,⟨[12,13,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[12,14,16],1⟩,⟨[17],3⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[10,15,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,18],1⟩,⟨[14,15,18],1⟩,⟨[13,16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7486
namespace Case7486
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,3,5},{2,4,6},{3,4,7},{0,5,6,7},{4,5,8},{3,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{0,1,4},{1,5},{2,3,5},{1,6},{2,4,6},{2,7},{3,4,7},{0,5,6,7},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]
end Case7486
namespace Case7487
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{3},{1,3},{4},{1,4},{0,2,3,4},{5},{0,5},{1,5},{2,5},{6},{0,6},{1,2,6},{5,6},{7},{0,7},{1,7},{3,5,7},{4,6,7},{8},{0,1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={0,2,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,2,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[12,15],1⟩,⟨[11,13,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,13,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[14,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],3⟩,⟨[11,12,19],1⟩,⟨[15,16,19],1⟩,⟨[14,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7487
namespace Case7487
def big : Finset (Finset (Fin 9)) := {{0,2,3,4},{1,2,6},{3,5,7},{4,6,7},{0,1,8},{4,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{1,4},{0,2,3,4},{0,5},{1,5},{2,5},{0,6},{1,2,6},{5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,1,8},{4,5,8},{3,6,8},{2,7,8}]
end Case7487
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

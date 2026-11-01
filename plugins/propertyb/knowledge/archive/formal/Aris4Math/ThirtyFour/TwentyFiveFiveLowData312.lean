import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case7488
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{3},{1,3},{4},{0,4},{1,2,4},{5},{0,5},{1,5},{2,5},{4,5},{6},{1,6},{0,2,3,6},{7},{0,7},{1,7},{3,5,7},{4,6,7},{8},{0,1,8},{3,4,8},{5,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={0,2,3,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={3,4,8} then 1 else if T={5,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,12,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[10,12,13,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[13,14,18],1⟩,⟨[15,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7488
namespace Case7488
def big : Finset (Finset (Fin 9)) := {{1,2,4},{0,2,3,6},{3,5,7},{4,6,7},{0,1,8},{3,4,8},{5,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,4},{1,2,4},{0,5},{1,5},{2,5},{4,5},{1,6},{0,2,3,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,1,8},{3,4,8},{5,6,8},{2,7,8}]
end Case7488
namespace Case7489
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{3},{1,3},{4},{0,4},{1,4},{5},{0,5},{1,5},{2,5},{3,4,5},{6},{1,6},{0,2,3,6},{7},{0,7},{1,2,7},{5,7},{4,6,7},{8},{0,1,8},{2,4,8},{5,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={0,2,3,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={2,4,8} then 1 else if T={5,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[10,12,13,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,12,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[12,14,18],1⟩,⟨[15,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7489
namespace Case7489
def big : Finset (Finset (Fin 9)) := {{3,4,5},{0,2,3,6},{1,2,7},{4,6,7},{0,1,8},{2,4,8},{5,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,4},{1,4},{0,5},{1,5},{2,5},{3,4,5},{1,6},{0,2,3,6},{0,7},{1,2,7},{5,7},{4,6,7},{0,1,8},{2,4,8},{5,6,8},{3,7,8}]
end Case7489
namespace Case7490
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{3},{1,3},{4},{0,1,4},{5},{0,5},{1,5},{2,5},{6},{1,6},{0,2,3,6},{4,5,6},{7},{0,7},{1,2,7},{3,4,7},{5,7},{8},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={0,2,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[10,12,13,16],1⟩,⟨[14,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7490
namespace Case7490
def big : Finset (Finset (Fin 9)) := {{0,1,4},{0,2,3,6},{4,5,6},{1,2,7},{3,4,7},{2,4,8},{3,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,1,4},{0,5},{1,5},{2,5},{1,6},{0,2,3,6},{4,5,6},{0,7},{1,2,7},{3,4,7},{5,7},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}]
end Case7490
namespace Case7491
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{3},{1,3},{4},{0,4},{1,2,4},{5},{0,5},{1,5},{2,5},{4,5},{6},{1,6},{0,2,3,6},{7},{0,7},{1,7},{3,4,7},{5,6,7},{8},{0,1,8},{3,5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={0,2,3,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={3,5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,12,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[10,12,13,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,14,17],1⟩,⟨[15,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[13,15,18],1⟩,⟨[14,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7491
namespace Case7491
def big : Finset (Finset (Fin 9)) := {{1,2,4},{0,2,3,6},{3,4,7},{5,6,7},{0,1,8},{3,5,8},{4,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,4},{1,2,4},{0,5},{1,5},{2,5},{4,5},{1,6},{0,2,3,6},{0,7},{1,7},{3,4,7},{5,6,7},{0,1,8},{3,5,8},{4,6,8},{2,7,8}]
end Case7491
namespace Case7492
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{3},{1,3},{4},{0,4},{1,4},{5},{0,5},{1,5},{2,5},{6},{1,6},{0,2,3,6},{4,5,6},{7},{0,7},{1,2,7},{3,4,7},{5,7},{8},{0,1,8},{2,4,8},{3,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={0,2,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[10,12,13,16],1⟩,⟨[14,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[12,14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7492
namespace Case7492
def big : Finset (Finset (Fin 9)) := {{0,2,3,6},{4,5,6},{1,2,7},{3,4,7},{0,1,8},{2,4,8},{3,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,4},{1,4},{0,5},{1,5},{2,5},{1,6},{0,2,3,6},{4,5,6},{0,7},{1,2,7},{3,4,7},{5,7},{0,1,8},{2,4,8},{3,5,8},{6,7,8}]
end Case7492
namespace Case7493
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{3},{1,3},{4},{0,1,4},{5},{0,5},{1,5},{2,5},{3,4,5},{6},{1,6},{0,2,3,6},{7},{0,7},{1,2,7},{5,7},{4,6,7},{8},{0,8},{1,8},{2,4,8},{5,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={0,2,3,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={5,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[10,12,13,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,12,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[15,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7493
namespace Case7493
def big : Finset (Finset (Fin 9)) := {{0,1,4},{3,4,5},{0,2,3,6},{1,2,7},{4,6,7},{2,4,8},{5,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,1,4},{0,5},{1,5},{2,5},{3,4,5},{1,6},{0,2,3,6},{0,7},{1,2,7},{5,7},{4,6,7},{0,8},{1,8},{2,4,8},{5,6,8},{3,7,8}]
end Case7493
namespace Case7494
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{3},{0,3},{1,2,3},{4},{0,4},{1,4},{5},{0,5},{1,5},{2,5},{3,5},{6},{1,6},{3,4,6},{7},{1,7},{4,5,7},{0,2,6,7},{8},{0,1,8},{2,4,8},{5,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={3,4,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={4,5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={2,4,8} then 1 else if T={5,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],3⟩,⟨[12,17],1⟩,⟨[14,15,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[15,16,18],1⟩,⟨[11,13,17,18],1⟩,⟨[19],3⟩,⟨[11,12,19],1⟩,⟨[13,15,19],1⟩,⟨[16,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7494
namespace Case7494
def big : Finset (Finset (Fin 9)) := {{1,2,3},{3,4,6},{4,5,7},{0,2,6,7},{0,1,8},{2,4,8},{5,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,2,3},{0,4},{1,4},{0,5},{1,5},{2,5},{3,5},{1,6},{3,4,6},{1,7},{4,5,7},{0,2,6,7},{0,1,8},{2,4,8},{5,6,8},{3,7,8}]
end Case7494
namespace Case7495
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{3},{0,3},{1,2,3},{4},{0,1,4},{5},{0,5},{1,5},{2,5},{3,5},{6},{1,6},{3,4,6},{7},{1,7},{4,5,7},{0,2,6,7},{8},{0,8},{1,8},{2,4,8},{5,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={3,4,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={4,5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={5,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,13,14],1⟩,⟨[15],2⟩,⟨[11,12,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],3⟩,⟨[12,17],1⟩,⟨[14,15,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[15,16,18],1⟩,⟨[11,13,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,15,19],1⟩,⟨[16,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7495
namespace Case7495
def big : Finset (Finset (Fin 9)) := {{1,2,3},{0,1,4},{3,4,6},{4,5,7},{0,2,6,7},{2,4,8},{5,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,2,3},{0,1,4},{0,5},{1,5},{2,5},{3,5},{1,6},{3,4,6},{1,7},{4,5,7},{0,2,6,7},{0,8},{1,8},{2,4,8},{5,6,8},{3,7,8}]
end Case7495
namespace Case7496
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{3},{0,3},{1,3},{4},{0,1,4},{2,3,4},{5},{0,5},{1,5},{2,5},{6},{1,6},{3,5,6},{7},{1,7},{4,5,7},{0,2,6,7},{8},{0,8},{1,2,8},{5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={3,5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={4,5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[11,12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[17],3⟩,⟨[12,17],1⟩,⟨[14,16,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[15,16,18],1⟩,⟨[11,13,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,13,19],1⟩,⟨[16,19],1⟩,⟨[15,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7496
namespace Case7496
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,3,4},{3,5,6},{4,5,7},{0,2,6,7},{1,2,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{0,1,4},{2,3,4},{0,5},{1,5},{2,5},{1,6},{3,5,6},{1,7},{4,5,7},{0,2,6,7},{0,8},{1,2,8},{5,8},{4,6,8},{3,7,8}]
end Case7496
namespace Case7497
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{1,2},{3},{1,3},{4},{0,4},{5},{0,5},{1,5},{4,5},{6},{0,2,3,6},{1,4,6},{5,6},{7},{0,7},{1,7},{2,4,7},{3,5,7},{8},{0,1,8},{3,4,8},{2,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={0,2,3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={3,5,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={3,4,8} then 1 else if T={2,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[10,12,13,16],1⟩,⟨[11,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,14,17],1⟩,⟨[13,15,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[13,14,18],1⟩,⟨[12,15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7497
namespace Case7497
def big : Finset (Finset (Fin 9)) := {{0,2,3,6},{1,4,6},{2,4,7},{3,5,7},{0,1,8},{3,4,8},{2,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{1,3},{0,4},{0,5},{1,5},{4,5},{0,2,3,6},{1,4,6},{5,6},{0,7},{1,7},{2,4,7},{3,5,7},{0,1,8},{3,4,8},{2,5,8},{6,7,8}]
end Case7497
namespace Case7498
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{1,2},{3},{1,3},{4},{0,4},{1,4},{5},{0,5},{1,5},{2,4,5},{6},{0,2,3,6},{5,6},{7},{0,7},{3,4,7},{5,7},{1,6,7},{8},{0,1,8},{3,5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,4,5} then 1 else if T={6} then 3 else if T={0,2,3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={1,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={3,5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,14,15],1⟩,⟨[16],3⟩,⟨[10,12,13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[11,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[13,15,18],1⟩,⟨[14,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7498
namespace Case7498
def big : Finset (Finset (Fin 9)) := {{2,4,5},{0,2,3,6},{3,4,7},{1,6,7},{0,1,8},{3,5,8},{4,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{1,3},{0,4},{1,4},{0,5},{1,5},{2,4,5},{0,2,3,6},{5,6},{0,7},{3,4,7},{5,7},{1,6,7},{0,1,8},{3,5,8},{4,6,8},{2,7,8}]
end Case7498
namespace Case7499
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{1,2},{3},{1,3},{4},{0,1,4},{5},{0,5},{1,5},{2,4,5},{6},{0,2,3,6},{5,6},{7},{0,7},{3,4,7},{5,7},{1,6,7},{8},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,4,5} then 1 else if T={6} then 3 else if T={0,2,3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,14,15],1⟩,⟨[16],3⟩,⟨[10,12,13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[11,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[13,15,18],1⟩,⟨[14,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7499
namespace Case7499
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,4,5},{0,2,3,6},{3,4,7},{1,6,7},{3,5,8},{4,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{1,3},{0,1,4},{0,5},{1,5},{2,4,5},{0,2,3,6},{5,6},{0,7},{3,4,7},{5,7},{1,6,7},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]
end Case7499
namespace Case7500
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{1,2},{3},{0,3},{4},{0,4},{1,4},{5},{0,5},{1,5},{3,5},{2,4,5},{6},{1,3,6},{5,6},{7},{1,7},{3,4,7},{0,2,6,7},{8},{0,1,8},{2,3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 3 else if T={1,3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={2,3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[12,14,15],1⟩,⟨[16],3⟩,⟨[11,13,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[13,14,17],1⟩,⟨[10,12,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[12,13,18],1⟩,⟨[14,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7500
namespace Case7500
def big : Finset (Finset (Fin 9)) := {{2,4,5},{1,3,6},{3,4,7},{0,2,6,7},{0,1,8},{2,3,8},{4,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,4},{1,4},{0,5},{1,5},{3,5},{2,4,5},{1,3,6},{5,6},{1,7},{3,4,7},{0,2,6,7},{0,1,8},{2,3,8},{4,6,8},{5,7,8}]
end Case7500
namespace Case7501
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{1,2},{3},{0,3},{4},{0,1,4},{2,3,4},{5},{0,5},{1,5},{3,5},{6},{1,3,6},{5,6},{7},{1,7},{4,5,7},{0,2,6,7},{8},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={6} then 3 else if T={1,3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={4,5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[11,12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[17],3⟩,⟨[12,14,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[15,16,18],1⟩,⟨[11,13,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,16,19],1⟩,⟨[15,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7501
namespace Case7501
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,3,4},{1,3,6},{4,5,7},{0,2,6,7},{2,5,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,1,4},{2,3,4},{0,5},{1,5},{3,5},{1,3,6},{5,6},{1,7},{4,5,7},{0,2,6,7},{0,8},{1,8},{2,5,8},{4,6,8},{3,7,8}]
end Case7501
namespace Case7502
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{1,2},{3},{0,3},{1,3},{4},{0,1,4},{5},{0,5},{1,5},{2,3,5},{6},{3,4,6},{5,6},{7},{1,7},{4,5,7},{0,2,6,7},{8},{0,8},{2,4,8},{5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,3,5} then 1 else if T={6} then 3 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={4,5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,13,15],1⟩,⟨[16],3⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[14,15,17],1⟩,⟨[10,12,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[11,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7502
namespace Case7502
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,3,5},{3,4,6},{4,5,7},{0,2,6,7},{2,4,8},{1,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{0,1,4},{0,5},{1,5},{2,3,5},{3,4,6},{5,6},{1,7},{4,5,7},{0,2,6,7},{0,8},{2,4,8},{5,8},{1,6,8},{3,7,8}]
end Case7502
namespace Case7503
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{1,2},{3},{0,3},{4},{0,4},{1,4},{2,3,4},{5},{0,5},{1,5},{3,5},{6},{1,3,6},{5,6},{7},{1,7},{4,5,7},{0,2,6,7},{8},{0,1,8},{2,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={6} then 3 else if T={1,3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={4,5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={2,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[17],3⟩,⟨[12,14,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[15,16,18],1⟩,⟨[11,13,17,18],1⟩,⟨[19],3⟩,⟨[11,12,19],1⟩,⟨[13,16,19],1⟩,⟨[15,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7503
namespace Case7503
def big : Finset (Finset (Fin 9)) := {{2,3,4},{1,3,6},{4,5,7},{0,2,6,7},{0,1,8},{2,5,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,4},{1,4},{2,3,4},{0,5},{1,5},{3,5},{1,3,6},{5,6},{1,7},{4,5,7},{0,2,6,7},{0,1,8},{2,5,8},{4,6,8},{3,7,8}]
end Case7503
namespace Case7504
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{1,2},{3},{0,3},{4},{0,1,4},{5},{0,5},{1,5},{3,5},{2,4,5},{6},{1,3,6},{5,6},{7},{1,7},{3,4,7},{0,2,6,7},{8},{0,8},{1,8},{2,3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 3 else if T={1,3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[12,14,15],1⟩,⟨[16],3⟩,⟨[11,13,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[13,14,17],1⟩,⟨[10,12,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,13,18],1⟩,⟨[14,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7504
namespace Case7504
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,4,5},{1,3,6},{3,4,7},{0,2,6,7},{2,3,8},{4,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,1,4},{0,5},{1,5},{3,5},{2,4,5},{1,3,6},{5,6},{1,7},{3,4,7},{0,2,6,7},{0,8},{1,8},{2,3,8},{4,6,8},{5,7,8}]
end Case7504
namespace Case7505
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{1,2},{3},{0,3},{1,3},{4},{0,1,4},{5},{0,5},{1,5},{2,4,5},{6},{3,4,6},{5,6},{7},{1,7},{3,5,7},{0,2,6,7},{8},{0,8},{2,3,8},{5,8},{1,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,4,5} then 1 else if T={6} then 3 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={0,2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={1,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,14,15],1⟩,⟨[16],3⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[13,15,17],1⟩,⟨[10,12,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,13,18],1⟩,⟨[15,18],1⟩,⟨[11,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7505
namespace Case7505
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,4,5},{3,4,6},{3,5,7},{0,2,6,7},{2,3,8},{1,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{0,1,4},{0,5},{1,5},{2,4,5},{3,4,6},{5,6},{1,7},{3,5,7},{0,2,6,7},{0,8},{2,3,8},{5,8},{1,6,8},{4,7,8}]
end Case7505
namespace Case7506
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{0,2},{3},{0,3},{1,3},{4},{0,1,4},{5},{0,5},{1,5},{2,5},{6},{1,2,6},{3,4,6},{5,6},{7},{1,7},{2,3,7},{4,5,7},{8},{1,8},{2,4,8},{3,5,8},{0,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 3 else if T={1,2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={2,3,7} then 1 else if T={4,5,7} then 1 else if T={8} then 3 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={0,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],3⟩,⟨[11,12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[12,13,17],1⟩,⟨[14,15,17],1⟩,⟨[18],3⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[13,15,18],1⟩,⟨[10,16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7506
namespace Case7506
def big : Finset (Finset (Fin 9)) := {{0,1,4},{1,2,6},{3,4,6},{2,3,7},{4,5,7},{2,4,8},{3,5,8},{0,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{1,3},{0,1,4},{0,5},{1,5},{2,5},{1,2,6},{3,4,6},{5,6},{1,7},{2,3,7},{4,5,7},{1,8},{2,4,8},{3,5,8},{0,6,7,8}]
end Case7506
namespace Case7507
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{3},{4},{1,4},{0,2,3,4},{5},{1,5},{2,5},{3,5},{6},{0,6},{1,2,6},{5,6},{7},{0,7},{1,7},{4,5,7},{3,6,7},{8},{1,3,8},{0,5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={4} then 2 else if T={1,4} then 1 else if T={0,2,3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,2,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={4,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 3 else if T={1,3,8} then 1 else if T={0,5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[15],2⟩,⟨[12,15],1⟩,⟨[11,13,14,15],1⟩,⟨[16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,13,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[15,16,18],1⟩,⟨[14,17,18],1⟩,⟨[19],3⟩,⟨[12,14,19],1⟩,⟨[11,16,19],1⟩,⟨[15,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7507
namespace Case7507
def big : Finset (Finset (Fin 9)) := {{0,2,3,4},{1,2,6},{4,5,7},{3,6,7},{1,3,8},{0,5,8},{4,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,4},{0,2,3,4},{1,5},{2,5},{3,5},{0,6},{1,2,6},{5,6},{0,7},{1,7},{4,5,7},{3,6,7},{1,3,8},{0,5,8},{4,6,8},{2,7,8}]
end Case7507
namespace Case7508
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{3},{1,3},{4},{0,4},{1,4},{5},{1,5},{2,5},{3,4,5},{6},{0,2,3,6},{5,6},{7},{0,7},{1,2,7},{5,7},{4,6,7},{8},{2,4,8},{0,5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 3 else if T={0,2,3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={2,4,8} then 1 else if T={0,5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],3⟩,⟨[10,12,13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,12,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],3⟩,⟨[12,14,18],1⟩,⟨[10,15,18],1⟩,⟨[11,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7508
namespace Case7508
def big : Finset (Finset (Fin 9)) := {{3,4,5},{0,2,3,6},{1,2,7},{4,6,7},{2,4,8},{0,5,8},{1,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{0,4},{1,4},{1,5},{2,5},{3,4,5},{0,2,3,6},{5,6},{0,7},{1,2,7},{5,7},{4,6,7},{2,4,8},{0,5,8},{1,6,8},{3,7,8}]
end Case7508
namespace Case7509
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{3},{1,3},{4},{0,4},{1,2,4},{5},{1,5},{2,5},{4,5},{6},{0,2,3,6},{5,6},{7},{0,7},{1,7},{3,5,7},{4,6,7},{8},{3,4,8},{0,5,8},{1,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={0,2,3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={3,4,8} then 1 else if T={0,5,8} then 1 else if T={1,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[10,12,13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],3⟩,⟨[13,14,18],1⟩,⟨[10,15,18],1⟩,⟨[11,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7509
namespace Case7509
def big : Finset (Finset (Fin 9)) := {{1,2,4},{0,2,3,6},{3,5,7},{4,6,7},{3,4,8},{0,5,8},{1,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{0,4},{1,2,4},{1,5},{2,5},{4,5},{0,2,3,6},{5,6},{0,7},{1,7},{3,5,7},{4,6,7},{3,4,8},{0,5,8},{1,6,8},{2,7,8}]
end Case7509
namespace Case7510
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{3},{1,3},{4},{5},{1,5},{2,5},{0,4,5},{6},{0,2,3,6},{1,4,6},{5,6},{7},{0,7},{1,2,7},{3,4,7},{5,7},{8},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={0,4,5} then 1 else if T={6} then 3 else if T={0,2,3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[11,15,16],1⟩,⟨[17],3⟩,⟨[11,13,14,17],1⟩,⟨[12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,15,19],1⟩,⟨[14,16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7510
namespace Case7510
def big : Finset (Finset (Fin 9)) := {{0,4,5},{0,2,3,6},{1,4,6},{1,2,7},{3,4,7},{2,4,8},{3,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{1,5},{2,5},{0,4,5},{0,2,3,6},{1,4,6},{5,6},{0,7},{1,2,7},{3,4,7},{5,7},{0,8},{1,8},{2,4,8},{3,5,8},{6,7,8}]
end Case7510
namespace Case7511
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{3},{1,3},{4},{0,4},{1,4},{5},{1,5},{2,5},{3,4,5},{6},{0,2,3,6},{5,6},{7},{0,7},{2,4,7},{5,7},{1,6,7},{8},{1,2,8},{0,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 3 else if T={0,2,3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={1,6,7} then 1 else if T={8} then 3 else if T={1,2,8} then 1 else if T={0,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[10,11],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],3⟩,⟨[10,12,13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[11,16,17],1⟩,⟨[18],3⟩,⟨[11,12,18],1⟩,⟨[10,15,18],1⟩,⟨[14,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case7511
namespace Case7511
def big : Finset (Finset (Fin 9)) := {{3,4,5},{0,2,3,6},{2,4,7},{1,6,7},{1,2,8},{0,5,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{0,4},{1,4},{1,5},{2,5},{3,4,5},{0,2,3,6},{5,6},{0,7},{2,4,7},{5,7},{1,6,7},{1,2,8},{0,5,8},{4,6,8},{3,7,8}]
end Case7511
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case3888
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,3},{4},{0,4},{1,3,4},{0,5},{1,5},{2,5},{4,5},{6},{0,1,2,6},{3,6},{5,6},{7},{0,7},{2,4,7},{3,5,7},{6,7},{8},{0,8},{2,3,8},{5,8},{4,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,4,7} then 1 else if T={3,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,13,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,11,12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,14,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,13,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3888
namespace Case3888
def big : Finset (Finset (Fin 9)) := {{1,3,4},{0,1,2,6},{2,4,7},{3,5,7},{2,3,8},{4,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{1,3,4},{0,5},{1,5},{2,5},{4,5},{0,1,2,6},{3,6},{5,6},{0,7},{2,4,7},{3,5,7},{6,7},{0,8},{2,3,8},{5,8},{4,6,8},{1,7,8}]
end Case3888
namespace Case3889
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,3},{4},{0,4},{0,5},{1,5},{2,5},{3,5},{4,5},{6},{0,1,2,6},{3,4,6},{5,6},{7},{0,7},{1,3,7},{2,4,7},{6,7},{8},{0,8},{2,3,8},{1,4,8},{6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,11,12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,13,17],1⟩,⟨[12,14,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3889
namespace Case3889
def big : Finset (Finset (Fin 9)) := {{0,1,2,6},{3,4,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{0,5},{1,5},{2,5},{3,5},{4,5},{0,1,2,6},{3,4,6},{5,6},{0,7},{1,3,7},{2,4,7},{6,7},{0,8},{2,3,8},{1,4,8},{6,8},{5,7,8}]
end Case3889
namespace Case3890
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,3},{1,2,3},{4},{0,4},{0,5},{1,5},{3,5},{2,4,5},{6},{2,6},{4,6},{5,6},{7},{3,4,7},{5,7},{0,1,6,7},{8},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 2 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[13,15,16],1⟩,⟨[17],2⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[11,12,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3890
namespace Case3890
def big : Finset (Finset (Fin 9)) := {{1,2,3},{2,4,5},{3,4,7},{0,1,6,7},{1,4,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{1,2,3},{0,4},{0,5},{1,5},{3,5},{2,4,5},{2,6},{4,6},{5,6},{3,4,7},{5,7},{0,1,6,7},{0,8},{1,4,8},{5,8},{3,6,8},{2,7,8}]
end Case3890
namespace Case3891
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,3},{1,2,3},{4},{0,4},{0,5},{1,5},{2,5},{4,5},{6},{3,6},{2,4,6},{5,6},{7},{3,4,7},{5,7},{0,1,6,7},{8},{0,8},{1,4,8},{3,5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 2 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={3,5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[14,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[11,12,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,15,19],1⟩,⟨[14,16,19],1⟩,⟨[17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3891
namespace Case3891
def big : Finset (Finset (Fin 9)) := {{1,2,3},{2,4,6},{3,4,7},{0,1,6,7},{1,4,8},{3,5,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{1,2,3},{0,4},{0,5},{1,5},{2,5},{4,5},{3,6},{2,4,6},{5,6},{3,4,7},{5,7},{0,1,6,7},{0,8},{1,4,8},{3,5,8},{6,8},{2,7,8}]
end Case3891
namespace Case3892
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,1},{2},{0,2},{3},{0,3},{4},{0,4},{0,5},{1,2,5},{3,5},{4,5},{6},{1,6},{2,6},{3,4,6},{5,6},{7},{1,3,7},{2,4,7},{5,7},{8},{2,3,8},{1,4,8},{5,8},{0,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={0,5} then 1 else if T={1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 3 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={0,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[10,15],1⟩,⟨[11,12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[11,13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[18],3⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[10,16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3892
namespace Case3892
def big : Finset (Finset (Fin 9)) := {{1,2,5},{3,4,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{0,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{0,3},{0,4},{0,5},{1,2,5},{3,5},{4,5},{1,6},{2,6},{3,4,6},{5,6},{1,3,7},{2,4,7},{5,7},{2,3,8},{1,4,8},{5,8},{0,6,7,8}]
end Case3892
namespace Case3893
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,3},{4},{0,4},{5},{0,1,2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{7},{1,3,7},{2,4,7},{5,7},{6,7},{8},{2,3,8},{1,4,8},{5,8},{6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[15],1⟩,⟨[10,11,12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[10,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3893
namespace Case3893
def big : Finset (Finset (Fin 9)) := {{0,1,2,5},{3,4,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{0,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{0,1,2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{1,3,7},{2,4,7},{5,7},{6,7},{2,3,8},{1,4,8},{5,8},{6,8},{0,7,8}]
end Case3893
namespace Case3894
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,4},{1,3,4},{5},{0,1,2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{5,6},{7},{0,3,7},{2,4,7},{5,7},{6,7},{8},{0,8},{2,3,8},{5,8},{4,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={5} then 1 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[10,11,12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,13,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3894
namespace Case3894
def big : Finset (Finset (Fin 9)) := {{1,3,4},{0,1,2,5},{0,3,7},{2,4,7},{2,3,8},{4,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,4},{1,3,4},{0,1,2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{5,6},{0,3,7},{2,4,7},{5,7},{6,7},{0,8},{2,3,8},{5,8},{4,6,8},{1,7,8}]
end Case3894
namespace Case3895
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{4},{0,3,4},{5},{0,1,2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{4,6},{5,6},{7},{0,7},{1,3,7},{2,4,7},{5,7},{8},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[10,13,14],1⟩,⟨[15],1⟩,⟨[10,11,12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3895
namespace Case3895
def big : Finset (Finset (Fin 9)) := {{0,3,4},{0,1,2,5},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,3,4},{0,1,2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{4,6},{5,6},{0,7},{1,3,7},{2,4,7},{5,7},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
end Case3895
namespace Case3896
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,3},{1,2,3},{4},{0,4},{5},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{7},{2,4,7},{0,1,5,7},{6,7},{8},{0,2,8},{1,4,8},{5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={2,4,7} then 1 else if T={0,1,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,2,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[13,15,18],1⟩,⟨[11,12,16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,13,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3896
namespace Case3896
def big : Finset (Finset (Fin 9)) := {{1,2,3},{3,4,6},{2,4,7},{0,1,5,7},{0,2,8},{1,4,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,2,3},{0,4},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{2,4,7},{0,1,5,7},{6,7},{0,2,8},{1,4,8},{5,8},{6,8},{3,7,8}]
end Case3896
namespace Case3897
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,2,3},{4},{0,4},{1,2,4},{5},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{5,6},{7},{3,4,7},{0,1,5,7},{6,7},{8},{0,8},{1,3,8},{5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={3,4,7} then 1 else if T={0,1,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,13,15],1⟩,⟨[16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[14,15,18],1⟩,⟨[11,12,16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,14,19],1⟩,⟨[16,19],1⟩,⟨[15,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3897
namespace Case3897
def big : Finset (Finset (Fin 9)) := {{0,2,3},{1,2,4},{3,4,7},{0,1,5,7},{1,3,8},{4,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2,3},{0,4},{1,2,4},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{5,6},{3,4,7},{0,1,5,7},{6,7},{0,8},{1,3,8},{5,8},{4,6,8},{2,7,8}]
end Case3897
namespace Case3898
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{0,3},{4},{0,4},{5},{1,5},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{7},{1,3,7},{2,4,7},{6,7},{8},{2,3,8},{1,4,8},{6,8},{0,5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={6,8} then 1 else if T={0,5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[10,11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[11,13,17],1⟩,⟨[12,14,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[16,18],1⟩,⟨[10,15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3898
namespace Case3898
def big : Finset (Finset (Fin 9)) := {{0,1,2},{3,4,6},{1,3,7},{2,4,7},{2,3,8},{1,4,8},{0,5,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{0,3},{0,4},{1,5},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{1,3,7},{2,4,7},{6,7},{2,3,8},{1,4,8},{6,8},{0,5,7,8}]
end Case3898
namespace Case3899
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,2,3},{4},{1,2,4},{5},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{7},{3,7},{4,7},{0,1,5,7},{6,7},{8},{1,3,8},{0,4,8},{5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 2 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={1,2,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={3,7} then 1 else if T={4,7} then 1 else if T={0,1,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={1,3,8} then 1 else if T={0,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[12,13,15],1⟩,⟨[16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[14,18],1⟩,⟨[15,18],1⟩,⟨[11,12,16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[12,14,19],1⟩,⟨[11,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3899
namespace Case3899
def big : Finset (Finset (Fin 9)) := {{0,2,3},{1,2,4},{3,4,6},{0,1,5,7},{1,3,8},{0,4,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2,3},{1,2,4},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{3,7},{4,7},{0,1,5,7},{6,7},{1,3,8},{0,4,8},{5,8},{6,8},{2,7,8}]
end Case3899
namespace Case3900
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,2,3},{4},{1,2,4},{5},{2,5},{3,5},{4,5},{0,6},{1,6},{3,6},{4,6},{5,6},{7},{2,7},{3,4,7},{0,1,5,7},{6,7},{8},{1,3,8},{0,4,8},{5,8},{2,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 2 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={1,2,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={0,1,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={1,3,8} then 1 else if T={0,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[12,13,15],1⟩,⟨[16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[13,18],1⟩,⟨[14,15,18],1⟩,⟨[11,12,16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[12,14,19],1⟩,⟨[11,15,19],1⟩,⟨[16,19],1⟩,⟨[13,17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3900
namespace Case3900
def big : Finset (Finset (Fin 9)) := {{0,2,3},{1,2,4},{3,4,7},{0,1,5,7},{1,3,8},{0,4,8},{2,6,8}}
def full : List (Finset (Fin 9)) := [{0,2,3},{1,2,4},{2,5},{3,5},{4,5},{0,6},{1,6},{3,6},{4,6},{5,6},{2,7},{3,4,7},{0,1,5,7},{6,7},{1,3,8},{0,4,8},{5,8},{2,6,8},{7,8}]
end Case3900
namespace Case3901
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,1,3},{4},{0,2,4},{5},{1,5},{2,5},{3,5},{4,5},{0,6},{1,2,6},{3,6},{4,6},{5,6},{7},{1,7},{2,7},{3,4,7},{6,7},{8},{2,3,8},{1,4,8},{6,8},{0,5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 2 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={0,1,3} then 1 else if T={4} then 1 else if T={0,2,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={6,8} then 1 else if T={0,5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[10,11,13],1⟩,⟨[14],1⟩,⟨[10,12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[10,16],1⟩,⟨[11,12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[16,18],1⟩,⟨[10,15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3901
namespace Case3901
def big : Finset (Finset (Fin 9)) := {{0,1,3},{0,2,4},{1,2,6},{3,4,7},{2,3,8},{1,4,8},{0,5,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,3},{0,2,4},{1,5},{2,5},{3,5},{4,5},{0,6},{1,2,6},{3,6},{4,6},{5,6},{1,7},{2,7},{3,4,7},{6,7},{2,3,8},{1,4,8},{6,8},{0,5,7,8}]
end Case3901
namespace Case3902
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{1,3},{4},{1,4},{0,2,3,4},{5},{0,5},{6},{0,6},{1,2,5,6},{7},{0,7},{1,7},{3,5,7},{4,6,7},{8},{0,1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={0,2,3,4} then 1 else if T={5} then 3 else if T={0,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,2,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],1⟩,⟨[12],1⟩,⟨[13],3⟩,⟨[14],2⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[12,15],1⟩,⟨[11,13,14,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[12,13,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[14,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],3⟩,⟨[11,12,19],1⟩,⟨[15,16,19],1⟩,⟨[14,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3902
namespace Case3902
def big : Finset (Finset (Fin 9)) := {{0,2,3,4},{1,2,5,6},{3,5,7},{4,6,7},{0,1,8},{4,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{1,4},{0,2,3,4},{0,5},{0,6},{1,2,5,6},{0,7},{1,7},{3,5,7},{4,6,7},{0,1,8},{4,5,8},{3,6,8},{2,7,8}]
end Case3902
namespace Case3903
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{1,3},{4},{0,4},{5},{1,5},{0,2,3,5},{6},{0,6},{1,2,4,6},{7},{0,7},{1,7},{3,4,7},{5,6,7},{8},{0,1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={5} then 3 else if T={1,5} then 1 else if T={0,2,3,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,2,4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={5,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],1⟩,⟨[11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[10,14],1⟩,⟨[15],3⟩,⟨[11,15],1⟩,⟨[10,12,13,15],1⟩,⟨[16],3⟩,⟨[10,16],1⟩,⟨[11,12,14,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,14,17],1⟩,⟨[15,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[14,15,18],1⟩,⟨[13,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3903
namespace Case3903
def big : Finset (Finset (Fin 9)) := {{0,2,3,5},{1,2,4,6},{3,4,7},{5,6,7},{0,1,8},{4,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,4},{1,5},{0,2,3,5},{0,6},{1,2,4,6},{0,7},{1,7},{3,4,7},{5,6,7},{0,1,8},{4,5,8},{3,6,8},{2,7,8}]
end Case3903
namespace Case3904
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{1,3},{4},{0,4},{5},{1,5},{0,2,3,5},{6},{0,6},{1,2,4,6},{7},{0,7},{1,7},{4,5,7},{3,6,7},{8},{0,1,8},{3,4,8},{5,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={5} then 3 else if T={1,5} then 1 else if T={0,2,3,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,2,4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={4,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={3,4,8} then 1 else if T={5,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],1⟩,⟨[11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[10,14],1⟩,⟨[15],3⟩,⟨[11,15],1⟩,⟨[10,12,13,15],1⟩,⟨[16],3⟩,⟨[10,16],1⟩,⟨[11,12,14,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[14,15,17],1⟩,⟨[13,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[13,14,18],1⟩,⟨[15,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3904
namespace Case3904
def big : Finset (Finset (Fin 9)) := {{0,2,3,5},{1,2,4,6},{4,5,7},{3,6,7},{0,1,8},{3,4,8},{5,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,4},{1,5},{0,2,3,5},{0,6},{1,2,4,6},{0,7},{1,7},{4,5,7},{3,6,7},{0,1,8},{3,4,8},{5,6,8},{2,7,8}]
end Case3904
namespace Case3905
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{1,3},{4},{0,4},{1,4},{5},{0,5},{3,4,5},{6},{0,6},{1,2,5,6},{7},{1,7},{0,2,3,7},{4,6,7},{8},{0,1,8},{2,4,8},{3,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 3 else if T={0,5} then 1 else if T={3,4,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,2,5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={0,2,3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={2,4,8} then 1 else if T={3,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],1⟩,⟨[11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],3⟩,⟨[10,15],1⟩,⟨[13,14,15],1⟩,⟨[16],3⟩,⟨[10,16],1⟩,⟨[11,12,15,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[10,12,13,17],1⟩,⟨[14,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[12,14,18],1⟩,⟨[13,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3905
namespace Case3905
def big : Finset (Finset (Fin 9)) := {{3,4,5},{1,2,5,6},{0,2,3,7},{4,6,7},{0,1,8},{2,4,8},{3,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,4},{1,4},{0,5},{3,4,5},{0,6},{1,2,5,6},{1,7},{0,2,3,7},{4,6,7},{0,1,8},{2,4,8},{3,6,8},{5,7,8}]
end Case3905
namespace Case3906
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{1,3},{4},{0,1,4},{5},{0,5},{3,4,5},{6},{0,6},{1,2,5,6},{7},{1,7},{0,2,3,7},{4,6,7},{8},{0,8},{1,8},{2,4,8},{3,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 1 else if T={2} then 3 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 3 else if T={0,5} then 1 else if T={3,4,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,2,5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={0,2,3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={3,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],1⟩,⟨[11],1⟩,⟨[12],3⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],3⟩,⟨[10,15],1⟩,⟨[13,14,15],1⟩,⟨[16],3⟩,⟨[10,16],1⟩,⟨[11,12,15,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[10,12,13,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[13,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3906
namespace Case3906
def big : Finset (Finset (Fin 9)) := {{0,1,4},{3,4,5},{1,2,5,6},{0,2,3,7},{4,6,7},{2,4,8},{3,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,1,4},{0,5},{3,4,5},{0,6},{1,2,5,6},{1,7},{0,2,3,7},{4,6,7},{0,8},{1,8},{2,4,8},{3,6,8},{5,7,8}]
end Case3906
namespace Case3907
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{0,3},{1,3},{4},{0,1,4},{2,3,4},{5},{1,5},{6},{1,6},{0,2,5,6},{7},{0,7},{3,5,7},{4,6,7},{8},{0,8},{4,5,8},{3,6,8},{1,2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 1 else if T={2} then 3 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 3 else if T={1,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={0,2,5,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={1,2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],1⟩,⟨[12],1⟩,⟨[13],3⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[11,12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],3⟩,⟨[12,16],1⟩,⟨[17],3⟩,⟨[12,17],1⟩,⟨[11,13,16,17],1⟩,⟨[18],3⟩,⟨[11,18],1⟩,⟨[14,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],3⟩,⟨[11,19],1⟩,⟨[15,16,19],1⟩,⟨[14,17,19],1⟩,⟨[12,13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3907
namespace Case3907
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,3,4},{0,2,5,6},{3,5,7},{4,6,7},{4,5,8},{3,6,8},{1,2,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{0,1,4},{2,3,4},{1,5},{1,6},{0,2,5,6},{0,7},{3,5,7},{4,6,7},{0,8},{4,5,8},{3,6,8},{1,2,7,8}]
end Case3907
namespace Case3908
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{0,2},{3},{1,3},{4},{1,4},{5},{0,3,4,5},{6},{0,6},{1,2,5,6},{7},{0,7},{1,7},{2,3,7},{4,6,7},{8},{0,1,8},{2,4,8},{3,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={5} then 4 else if T={0,3,4,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,2,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,3,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={2,4,8} then 1 else if T={3,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],1⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],4⟩,⟨[10,13,14,15],1⟩,⟨[16],3⟩,⟨[10,16],1⟩,⟨[11,12,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,13,17],1⟩,⟨[14,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[12,14,18],1⟩,⟨[13,16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3908
namespace Case3908
def big : Finset (Finset (Fin 9)) := {{0,3,4,5},{1,2,5,6},{2,3,7},{4,6,7},{0,1,8},{2,4,8},{3,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,3},{1,4},{0,3,4,5},{0,6},{1,2,5,6},{0,7},{1,7},{2,3,7},{4,6,7},{0,1,8},{2,4,8},{3,6,8},{5,7,8}]
end Case3908
namespace Case3909
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{1,2},{3},{1,3},{4},{0,4},{1,4},{5},{0,2,3,5},{6},{0,6},{2,4,6},{7},{0,7},{3,4,7},{1,5,6,7},{8},{0,1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 4 else if T={0,2,3,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={2,4,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={1,5,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],1⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],4⟩,⟨[10,12,13,15],1⟩,⟨[16],3⟩,⟨[10,16],1⟩,⟨[12,14,16],1⟩,⟨[17],3⟩,⟨[10,17],1⟩,⟨[13,14,17],1⟩,⟨[11,15,16,17],1⟩,⟨[18],3⟩,⟨[10,11,18],1⟩,⟨[14,15,18],1⟩,⟨[13,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3909
namespace Case3909
def big : Finset (Finset (Fin 9)) := {{0,2,3,5},{2,4,6},{3,4,7},{1,5,6,7},{0,1,8},{4,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{1,3},{0,4},{1,4},{0,2,3,5},{0,6},{2,4,6},{0,7},{3,4,7},{1,5,6,7},{0,1,8},{4,5,8},{3,6,8},{2,7,8}]
end Case3909
namespace Case3910
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{1,2},{3},{1,3},{4},{0,1,4},{5},{0,2,3,5},{6},{0,6},{2,4,6},{7},{0,7},{3,4,7},{1,5,6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={0,1,4} then 1 else if T={5} then 4 else if T={0,2,3,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={2,4,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={1,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],1⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[10,11,14],1⟩,⟨[15],4⟩,⟨[10,12,13,15],1⟩,⟨[16],3⟩,⟨[10,16],1⟩,⟨[12,14,16],1⟩,⟨[17],3⟩,⟨[10,17],1⟩,⟨[13,14,17],1⟩,⟨[11,15,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[14,15,18],1⟩,⟨[13,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3910
namespace Case3910
def big : Finset (Finset (Fin 9)) := {{0,1,4},{0,2,3,5},{2,4,6},{3,4,7},{1,5,6,7},{4,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{1,3},{0,1,4},{0,2,3,5},{0,6},{2,4,6},{0,7},{3,4,7},{1,5,6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
end Case3910
namespace Case3911
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{1,2},{3},{0,3},{4},{0,4},{1,4},{2,3,4},{5},{6},{1,6},{0,2,5,6},{7},{0,7},{1,3,5,7},{4,6,7},{8},{0,1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 4 else if T={6} then 3 else if T={1,6} then 1 else if T={0,2,5,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={1,3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={0,1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],1⟩,⟨[12],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],4⟩,⟨[17],3⟩,⟨[12,17],1⟩,⟨[11,13,16,17],1⟩,⟨[18],3⟩,⟨[11,18],1⟩,⟨[12,14,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],3⟩,⟨[11,12,19],1⟩,⟨[15,16,19],1⟩,⟨[14,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case3911
namespace Case3911
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,2,5,6},{1,3,5,7},{4,6,7},{0,1,8},{4,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,4},{1,4},{2,3,4},{1,6},{0,2,5,6},{0,7},{1,3,5,7},{4,6,7},{0,1,8},{4,5,8},{3,6,8},{2,7,8}]
end Case3911
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

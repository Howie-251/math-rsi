import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case4944
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{0,3},{4},{0,4},{2,4},{1,3,4},{5},{2,5},{3,5},{6},{0,6},{1,6},{2,3,6},{5,6},{7},{2,7},{0,1,5,7},{4,6,7},{8},{1,8},{0,2,8},{4,5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={1,3,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={2,7} then 1 else if T={0,1,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={0,2,8} then 1 else if T={4,5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[12,14,15],1⟩,⟨[16],2⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[13,18],1⟩,⟨[11,12,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[12,19],1⟩,⟨[11,13,19],1⟩,⟨[15,16,19],1⟩,⟨[17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4944
namespace Case4944
def big : Finset (Finset (Fin 9)) := {{1,3,4},{2,3,6},{0,1,5,7},{4,6,7},{0,2,8},{4,5,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,4},{2,4},{1,3,4},{2,5},{3,5},{0,6},{1,6},{2,3,6},{5,6},{2,7},{0,1,5,7},{4,6,7},{1,8},{0,2,8},{4,5,8},{6,8},{3,7,8}]
end Case4944
namespace Case4945
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{3},{4},{1,4},{2,4},{5},{2,5},{0,1,3,5},{6},{1,6},{3,6},{0,4,6},{5,6},{7},{0,7},{2,3,7},{4,5,7},{6,7},{8},{0,8},{3,4,8},{5,8},{2,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={0,1,3,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,3,7} then 1 else if T={4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[12,15],1⟩,⟨[10,11,13,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[10,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,13,17],1⟩,⟨[14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[12,16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4945
namespace Case4945
def big : Finset (Finset (Fin 9)) := {{0,1,3,5},{0,4,6},{2,3,7},{4,5,7},{3,4,8},{2,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,4},{2,4},{2,5},{0,1,3,5},{1,6},{3,6},{0,4,6},{5,6},{0,7},{2,3,7},{4,5,7},{6,7},{0,8},{3,4,8},{5,8},{2,6,8},{1,7,8}]
end Case4945
namespace Case4946
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{3},{4},{1,4},{2,3,4},{5},{2,5},{0,1,3,5},{6},{0,6},{3,6},{4,6},{5,6},{7},{1,7},{0,4,7},{5,7},{2,6,7},{8},{0,8},{2,8},{4,5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={0,1,3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,4,7} then 1 else if T={5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[13,16],1⟩,⟨[11,12,14,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[11,15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,19],1⟩,⟨[15,16,19],1⟩,⟨[12,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4946
namespace Case4946
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,1,3,5},{0,4,7},{2,6,7},{4,5,8},{1,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,4},{2,3,4},{2,5},{0,1,3,5},{0,6},{3,6},{4,6},{5,6},{1,7},{0,4,7},{5,7},{2,6,7},{0,8},{2,8},{4,5,8},{1,6,8},{3,7,8}]
end Case4946
namespace Case4947
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{3},{4},{1,4},{5},{2,5},{0,1,3,5},{4,5},{6},{0,6},{3,6},{2,4,6},{5,6},{7},{1,7},{2,3,7},{0,4,7},{6,7},{8},{0,8},{2,8},{3,4,8},{1,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={0,1,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,3,7} then 1 else if T={0,4,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={1,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[16],2⟩,⟨[13,16],1⟩,⟨[11,12,14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[14,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[13,14,18],1⟩,⟨[11,15,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,19],1⟩,⟨[14,15,19],1⟩,⟨[12,17,19],1⟩,⟨[16,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4947
namespace Case4947
def big : Finset (Finset (Fin 9)) := {{0,1,3,5},{2,4,6},{2,3,7},{0,4,7},{3,4,8},{1,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,4},{2,5},{0,1,3,5},{4,5},{0,6},{3,6},{2,4,6},{5,6},{1,7},{2,3,7},{0,4,7},{6,7},{0,8},{2,8},{3,4,8},{1,6,8},{5,7,8}]
end Case4947
namespace Case4948
def positionFn : Fin 9 → Fin 25 := ![19,11,13,20,12,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{3},{1,3},{2,3},{4},{0,4},{5},{2,5},{3,4,5},{6},{1,6},{0,3,6},{4,6},{5,6},{7},{2,4,7},{0,1,5,7},{6,7},{8},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={0,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={2,4,7} then 1 else if T={0,1,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,13,14,20,21,22,23,24,25],[⟨[],3⟩,⟨[20],1⟩,⟨[12],1⟩,⟨[14,20],1⟩,⟨[12,14],1⟩,⟨[21],1⟩,⟨[12,21],1⟩,⟨[14,21],1⟩,⟨[13],1⟩,⟨[13,20],1⟩,⟨[22],2⟩,⟨[14,22],1⟩,⟨[13,21,22],1⟩,⟨[23],1⟩,⟨[12,23],1⟩,⟨[20,21,23],1⟩,⟨[13,23],1⟩,⟨[22,23],1⟩,⟨[24],3⟩,⟨[13,14,24],1⟩,⟨[12,20,22,24],1⟩,⟨[23,24],1⟩,⟨[25],2⟩,⟨[20,25],1⟩,⟨[12,13,25],1⟩,⟨[22,25],1⟩,⟨[14,23,25],1⟩,⟨[21,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4948
namespace Case4948
def big : Finset (Finset (Fin 9)) := {{3,4,5},{0,3,6},{2,4,7},{0,1,5,7},{1,4,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{2,3},{0,4},{2,5},{3,4,5},{1,6},{0,3,6},{4,6},{5,6},{2,4,7},{0,1,5,7},{6,7},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
end Case4948
namespace Case4949
def positionFn : Fin 9 → Fin 25 := ![19,11,13,20,12,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{3},{1,3},{2,3},{4},{0,4},{5},{2,5},{4,5},{6},{1,6},{0,3,6},{2,4,6},{5,6},{7},{3,4,7},{0,1,5,7},{6,7},{8},{0,8},{1,4,8},{3,5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={0,3,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={3,4,7} then 1 else if T={0,1,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={3,5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,13,14,20,21,22,23,24,25],[⟨[],3⟩,⟨[20],1⟩,⟨[12],1⟩,⟨[14,20],1⟩,⟨[12,14],1⟩,⟨[21],1⟩,⟨[12,21],1⟩,⟨[14,21],1⟩,⟨[13],1⟩,⟨[13,20],1⟩,⟨[22],2⟩,⟨[14,22],1⟩,⟨[13,22],1⟩,⟨[23],1⟩,⟨[12,23],1⟩,⟨[20,21,23],1⟩,⟨[13,14,23],1⟩,⟨[22,23],1⟩,⟨[24],3⟩,⟨[13,21,24],1⟩,⟨[12,20,22,24],1⟩,⟨[23,24],1⟩,⟨[25],2⟩,⟨[20,25],1⟩,⟨[12,13,25],1⟩,⟨[21,22,25],1⟩,⟨[23,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4949
namespace Case4949
def big : Finset (Finset (Fin 9)) := {{0,3,6},{2,4,6},{3,4,7},{0,1,5,7},{1,4,8},{3,5,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{2,3},{0,4},{2,5},{4,5},{1,6},{0,3,6},{2,4,6},{5,6},{3,4,7},{0,1,5,7},{6,7},{0,8},{1,4,8},{3,5,8},{6,8},{2,7,8}]
end Case4949
namespace Case4950
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{3},{1,3},{4},{1,4},{0,3,4},{5},{2,5},{3,5},{6},{0,6},{2,3,6},{4,6},{5,6},{7},{2,4,7},{0,1,5,7},{6,7},{8},{0,8},{2,8},{4,5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={2,4,7} then 1 else if T={0,1,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[11,14,15],1⟩,⟨[16],2⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[13,15,18],1⟩,⟨[11,12,16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,19],1⟩,⟨[15,16,19],1⟩,⟨[12,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4950
namespace Case4950
def big : Finset (Finset (Fin 9)) := {{0,3,4},{2,3,6},{2,4,7},{0,1,5,7},{4,5,8},{1,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{1,4},{0,3,4},{2,5},{3,5},{0,6},{2,3,6},{4,6},{5,6},{2,4,7},{0,1,5,7},{6,7},{0,8},{2,8},{4,5,8},{1,6,8},{3,7,8}]
end Case4950
namespace Case4951
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{1,3},{4},{0,4},{5},{0,1,2,5},{3,4,5},{6},{1,6},{2,6},{0,3,6},{4,6},{5,6},{7},{0,7},{1,7},{3,7},{2,4,7},{5,7},{8},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 2 else if T={0,1,2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={0,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[15],2⟩,⟨[10,11,12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[10,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4951
namespace Case4951
def big : Finset (Finset (Fin 9)) := {{0,1,2,5},{3,4,5},{0,3,6},{2,4,7},{2,3,8},{1,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,4},{0,1,2,5},{3,4,5},{1,6},{2,6},{0,3,6},{4,6},{5,6},{0,7},{1,7},{3,7},{2,4,7},{5,7},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
end Case4951
namespace Case4952
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{1,3},{4},{0,4},{2,3,4},{5},{0,1,2,5},{4,5},{6},{1,6},{2,6},{0,3,6},{5,6},{7},{0,7},{1,7},{3,7},{5,7},{4,6,7},{8},{0,8},{1,4,8},{3,5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,3,4} then 1 else if T={5} then 2 else if T={0,1,2,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={0,3,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={3,5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,13,14],1⟩,⟨[15],2⟩,⟨[10,11,12,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[10,13,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4952
namespace Case4952
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,1,2,5},{0,3,6},{4,6,7},{1,4,8},{3,5,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,3},{0,4},{2,3,4},{0,1,2,5},{4,5},{1,6},{2,6},{0,3,6},{5,6},{0,7},{1,7},{3,7},{5,7},{4,6,7},{0,8},{1,4,8},{3,5,8},{6,8},{2,7,8}]
end Case4952
namespace Case4953
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{1,3},{4},{1,4},{0,3,4},{5},{0,1,2,5},{4,5},{6},{0,6},{2,6},{3,6},{5,6},{7},{0,7},{1,7},{2,3,7},{5,7},{4,6,7},{8},{0,8},{2,4,8},{3,5,8},{1,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 2 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={0,1,2,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={1,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[10,13,14],1⟩,⟨[15],2⟩,⟨[10,11,12,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,13,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,14,18],1⟩,⟨[13,15,18],1⟩,⟨[11,16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4953
namespace Case4953
def big : Finset (Finset (Fin 9)) := {{0,3,4},{0,1,2,5},{2,3,7},{4,6,7},{2,4,8},{3,5,8},{1,6,8}}
def full : List (Finset (Fin 9)) := [{1,3},{1,4},{0,3,4},{0,1,2,5},{4,5},{0,6},{2,6},{3,6},{5,6},{0,7},{1,7},{2,3,7},{5,7},{4,6,7},{0,8},{2,4,8},{3,5,8},{1,6,8},{7,8}]
end Case4953
namespace Case4954
def positionFn : Fin 9 → Fin 25 := ![20,11,13,14,12,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{3},{1,3},{0,2,3},{4},{0,4},{5},{3,5},{2,4,5},{6},{0,6},{2,6},{1,4,6},{5,6},{7},{0,7},{1,7},{4,7},{5,7},{3,6,7},{8},{3,4,8},{0,1,5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 2 else if T={3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 3 else if T={3,4,8} then 1 else if T={0,1,5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,13,14,15,21,22,23,24,25],[⟨[],3⟩,⟨[21],1⟩,⟨[12],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[14,15,21],1⟩,⟨[13],1⟩,⟨[13,21],1⟩,⟨[22],2⟩,⟨[15,22],1⟩,⟨[13,14,22],1⟩,⟨[23],1⟩,⟨[21,23],1⟩,⟨[14,23],1⟩,⟨[12,13,23],1⟩,⟨[22,23],1⟩,⟨[24],1⟩,⟨[21,24],1⟩,⟨[12,24],1⟩,⟨[13,24],1⟩,⟨[22,24],1⟩,⟨[15,23,24],1⟩,⟨[25],3⟩,⟨[13,15,25],1⟩,⟨[12,21,22,25],1⟩,⟨[23,25],1⟩,⟨[14,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4954
namespace Case4954
def big : Finset (Finset (Fin 9)) := {{0,2,3},{2,4,5},{1,4,6},{3,6,7},{3,4,8},{0,1,5,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{1,3},{0,2,3},{0,4},{3,5},{2,4,5},{0,6},{2,6},{1,4,6},{5,6},{0,7},{1,7},{4,7},{5,7},{3,6,7},{3,4,8},{0,1,5,8},{6,8},{2,7,8}]
end Case4954
namespace Case4955
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{3},{1,3},{4},{0,1,4},{2,4},{5},{1,5},{2,5},{6},{1,6},{2,6},{4,6},{0,3,5,6},{7},{0,7},{1,2,7},{3,4,7},{5,7},{8},{0,8},{1,8},{2,3,8},{4,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={4,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,11,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[10,13,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4955
namespace Case4955
def big : Finset (Finset (Fin 9)) := {{0,1,4},{0,3,5,6},{1,2,7},{3,4,7},{2,3,8},{4,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,3},{0,1,4},{2,4},{1,5},{2,5},{1,6},{2,6},{4,6},{0,3,5,6},{0,7},{1,2,7},{3,4,7},{5,7},{0,8},{1,8},{2,3,8},{4,5,8},{6,7,8}]
end Case4955
namespace Case4956
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{3},{1,3},{4},{0,4},{1,4},{2,3,4},{5},{1,5},{2,5},{6},{1,6},{2,6},{0,3,5,6},{7},{0,1,7},{2,7},{4,5,7},{6,7},{8},{0,8},{1,2,8},{5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 2 else if T={0,1,7} then 1 else if T={2,7} then 1 else if T={4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[11,14,16,17],1⟩,⟨[18],2⟩,⟨[11,12,18],1⟩,⟨[13,18],1⟩,⟨[15,16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,13,19],1⟩,⟨[16,19],1⟩,⟨[15,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4956
namespace Case4956
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,3,5,6},{0,1,7},{4,5,7},{1,2,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,3},{0,4},{1,4},{2,3,4},{1,5},{2,5},{1,6},{2,6},{0,3,5,6},{0,1,7},{2,7},{4,5,7},{6,7},{0,8},{1,2,8},{5,8},{4,6,8},{3,7,8}]
end Case4956
namespace Case4957
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{3},{1,3},{4},{0,4},{1,2,4},{5},{1,5},{2,5},{6},{1,6},{2,6},{4,6},{0,3,5,6},{7},{0,1,7},{2,7},{3,4,7},{5,7},{8},{0,8},{1,8},{2,3,8},{4,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 2 else if T={0,1,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={4,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,12,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[10,13,15,16],1⟩,⟨[17],2⟩,⟨[10,11,17],1⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4957
namespace Case4957
def big : Finset (Finset (Fin 9)) := {{1,2,4},{0,3,5,6},{0,1,7},{3,4,7},{2,3,8},{4,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,3},{0,4},{1,2,4},{1,5},{2,5},{1,6},{2,6},{4,6},{0,3,5,6},{0,1,7},{2,7},{3,4,7},{5,7},{0,8},{1,8},{2,3,8},{4,5,8},{6,7,8}]
end Case4957
namespace Case4958
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{3},{0,1,3},{2,3},{4},{0,4},{1,4},{5},{1,5},{2,5},{3,4,5},{6},{1,6},{2,6},{3,6},{7},{1,7},{2,4,7},{0,5,6,7},{8},{0,8},{1,2,8},{5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[10,11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[12,14,17],1⟩,⟨[10,15,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,12,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4958
namespace Case4958
def big : Finset (Finset (Fin 9)) := {{0,1,3},{3,4,5},{2,4,7},{0,5,6,7},{1,2,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,1,3},{2,3},{0,4},{1,4},{1,5},{2,5},{3,4,5},{1,6},{2,6},{3,6},{1,7},{2,4,7},{0,5,6,7},{0,8},{1,2,8},{5,8},{4,6,8},{3,7,8}]
end Case4958
namespace Case4959
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{3},{0,1,3},{2,3},{4},{0,4},{1,2,4},{5},{1,5},{2,5},{4,5},{6},{1,6},{2,6},{3,6},{7},{1,7},{3,4,7},{0,5,6,7},{8},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[10,11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,12,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[13,14,17],1⟩,⟨[10,15,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[13,15,18],1⟩,⟨[14,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4959
namespace Case4959
def big : Finset (Finset (Fin 9)) := {{0,1,3},{1,2,4},{3,4,7},{0,5,6,7},{3,5,8},{4,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,1,3},{2,3},{0,4},{1,2,4},{1,5},{2,5},{4,5},{1,6},{2,6},{3,6},{1,7},{3,4,7},{0,5,6,7},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]
end Case4959
namespace Case4960
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{3},{0,3},{1,2,3},{4},{0,4},{1,4},{5},{1,5},{2,5},{3,4,5},{6},{1,6},{2,6},{3,6},{7},{1,7},{2,4,7},{0,5,6,7},{8},{0,1,8},{2,8},{5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 2 else if T={0,1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[12,14,17],1⟩,⟨[10,15,16,17],1⟩,⟨[18],2⟩,⟨[10,11,18],1⟩,⟨[12,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4960
namespace Case4960
def big : Finset (Finset (Fin 9)) := {{1,2,3},{3,4,5},{2,4,7},{0,5,6,7},{0,1,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{1,2,3},{0,4},{1,4},{1,5},{2,5},{3,4,5},{1,6},{2,6},{3,6},{1,7},{2,4,7},{0,5,6,7},{0,1,8},{2,8},{5,8},{4,6,8},{3,7,8}]
end Case4960
namespace Case4961
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{1,2},{3},{0,1,3},{4},{0,4},{1,4},{5},{1,5},{3,4,5},{6},{1,6},{3,6},{0,2,5,6},{7},{0,7},{3,7},{2,4,7},{5,7},{6,7},{8},{0,8},{2,3,8},{5,8},{4,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 1 else if T={0,1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,6} then 1 else if T={0,2,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[10,12,15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,13,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4961
namespace Case4961
def big : Finset (Finset (Fin 9)) := {{0,1,3},{3,4,5},{0,2,5,6},{2,4,7},{2,3,8},{4,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,1,3},{0,4},{1,4},{1,5},{3,4,5},{1,6},{3,6},{0,2,5,6},{0,7},{3,7},{2,4,7},{5,7},{6,7},{0,8},{2,3,8},{5,8},{4,6,8},{1,7,8}]
end Case4961
namespace Case4962
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{1,2},{3},{0,1,3},{4},{0,4},{2,3,4},{5},{1,5},{4,5},{6},{1,6},{3,6},{0,2,5,6},{7},{0,7},{3,7},{1,4,7},{5,7},{6,7},{8},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 1 else if T={0,1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,6} then 1 else if T={0,2,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={3,7} then 1 else if T={1,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[14,17],1⟩,⟨[11,13,16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[14,18],1⟩,⟨[12,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[14,16,19],1⟩,⟨[15,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4962
namespace Case4962
def big : Finset (Finset (Fin 9)) := {{0,1,3},{2,3,4},{0,2,5,6},{1,4,7},{3,5,8},{4,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,1,3},{0,4},{2,3,4},{1,5},{4,5},{1,6},{3,6},{0,2,5,6},{0,7},{3,7},{1,4,7},{5,7},{6,7},{0,8},{1,8},{3,5,8},{4,6,8},{2,7,8}]
end Case4962
namespace Case4963
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{1,2},{3},{0,3},{4},{0,4},{1,4},{5},{1,5},{3,4,5},{6},{1,6},{3,6},{0,2,5,6},{7},{0,7},{1,3,7},{2,4,7},{5,7},{6,7},{8},{0,1,8},{2,3,8},{5,8},{4,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,6} then 1 else if T={0,2,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,1,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[12],2⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[10,12,15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,11,18],1⟩,⟨[12,13,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4963
namespace Case4963
def big : Finset (Finset (Fin 9)) := {{3,4,5},{0,2,5,6},{1,3,7},{2,4,7},{0,1,8},{2,3,8},{4,6,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,4},{1,4},{1,5},{3,4,5},{1,6},{3,6},{0,2,5,6},{0,7},{1,3,7},{2,4,7},{5,7},{6,7},{0,1,8},{2,3,8},{5,8},{4,6,8},{7,8}]
end Case4963
namespace Case4964
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{2},{0,1,2},{3},{0,3},{4},{0,4},{1,4},{5},{1,5},{3,5},{2,4,5},{6},{1,6},{2,6},{3,4,6},{7},{0,7},{2,7},{1,3,7},{5,7},{6,7},{8},{1,8},{2,3,8},{0,5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={0,5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[12],1⟩,⟨[10,11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[12,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[11,13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[11,18],1⟩,⟨[12,13,18],1⟩,⟨[10,15,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4964
namespace Case4964
def big : Finset (Finset (Fin 9)) := {{0,1,2},{2,4,5},{3,4,6},{1,3,7},{2,3,8},{0,5,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{0,3},{0,4},{1,4},{1,5},{3,5},{2,4,5},{1,6},{2,6},{3,4,6},{0,7},{2,7},{1,3,7},{5,7},{6,7},{1,8},{2,3,8},{0,5,6,8},{4,7,8}]
end Case4964
namespace Case4965
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{3},{1,3},{4},{0,4},{1,2,4},{5},{1,5},{3,4,5},{6},{1,6},{3,6},{0,2,5,6},{7},{2,7},{0,3,7},{4,7},{5,7},{6,7},{8},{0,8},{2,3,8},{5,8},{4,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,6} then 1 else if T={0,2,5,6} then 1 else if T={7} then 1 else if T={2,7} then 1 else if T={0,3,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,13,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[14,15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[14,17],1⟩,⟨[11,13,16,17],1⟩,⟨[18],1⟩,⟨[13,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,14,19],1⟩,⟨[16,19],1⟩,⟨[15,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4965
namespace Case4965
def big : Finset (Finset (Fin 9)) := {{1,2,4},{3,4,5},{0,2,5,6},{0,3,7},{2,3,8},{4,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{0,4},{1,2,4},{1,5},{3,4,5},{1,6},{3,6},{0,2,5,6},{2,7},{0,3,7},{4,7},{5,7},{6,7},{0,8},{2,3,8},{5,8},{4,6,8},{1,7,8}]
end Case4965
namespace Case4966
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{3},{1,3},{4},{0,4},{2,3,4},{5},{1,5},{4,5},{6},{1,6},{3,6},{0,2,5,6},{7},{2,7},{0,3,7},{1,4,7},{5,7},{6,7},{8},{0,8},{1,2,8},{3,5,8},{4,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,6} then 1 else if T={0,2,5,6} then 1 else if T={7} then 1 else if T={2,7} then 1 else if T={0,3,7} then 1 else if T={1,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={3,5,8} then 1 else if T={4,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[14,17],1⟩,⟨[11,13,16,17],1⟩,⟨[18],1⟩,⟨[13,18],1⟩,⟨[11,14,18],1⟩,⟨[12,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,13,19],1⟩,⟨[14,16,19],1⟩,⟨[15,17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4966
namespace Case4966
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,2,5,6},{0,3,7},{1,4,7},{1,2,8},{3,5,8},{4,6,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{0,4},{2,3,4},{1,5},{4,5},{1,6},{3,6},{0,2,5,6},{2,7},{0,3,7},{1,4,7},{5,7},{6,7},{0,8},{1,2,8},{3,5,8},{4,6,8},{7,8}]
end Case4966
namespace Case4967
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{2},{3},{0,3},{1,2,3},{4},{0,4},{5},{1,5},{3,4,5},{6},{1,6},{4,6},{0,2,5,6},{7},{2,7},{3,7},{1,4,7},{5,7},{6,7},{8},{1,8},{2,4,8},{5,8},{3,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={4,6} then 1 else if T={0,2,5,6} then 1 else if T={7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={1,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[14,15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[11,13,16,17],1⟩,⟨[18],1⟩,⟨[13,18],1⟩,⟨[14,18],1⟩,⟨[12,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[12,19],1⟩,⟨[13,15,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[11,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4967
namespace Case4967
def big : Finset (Finset (Fin 9)) := {{1,2,3},{3,4,5},{0,2,5,6},{1,4,7},{2,4,8},{3,6,8},{0,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,3},{1,2,3},{0,4},{1,5},{3,4,5},{1,6},{4,6},{0,2,5,6},{2,7},{3,7},{1,4,7},{5,7},{6,7},{1,8},{2,4,8},{5,8},{3,6,8},{0,7,8}]
end Case4967
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case4872
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{0,1,3},{2,3},{4},{1,4},{5},{3,5},{0,2,4,5},{6},{0,6},{2,6},{3,6},{7},{0,7},{1,7},{3,7},{5,7},{4,6,7},{8},{0,8},{3,4,8},{1,5,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={0,1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={0,2,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={3,4,8} then 1 else if T={1,5,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[10,11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],3⟩,⟨[13,15],1⟩,⟨[10,12,14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],3⟩,⟨[10,18],1⟩,⟨[13,14,18],1⟩,⟨[11,15,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4872
namespace Case4872
def big : Finset (Finset (Fin 9)) := {{0,1,3},{0,2,4,5},{4,6,7},{3,4,8},{1,5,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,1,3},{2,3},{1,4},{3,5},{0,2,4,5},{0,6},{2,6},{3,6},{0,7},{1,7},{3,7},{5,7},{4,6,7},{0,8},{3,4,8},{1,5,6,8},{2,7,8}]
end Case4872
namespace Case4873
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{0,1,3},{2,3},{4},{0,4},{5},{3,5},{6},{0,6},{2,6},{3,6},{1,4,5,6},{7},{0,7},{1,7},{3,7},{2,4,7},{5,7},{8},{1,8},{3,4,8},{0,2,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={0,1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={1,4,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 3 else if T={1,8} then 1 else if T={3,4,8} then 1 else if T={0,2,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[11,12,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[16],3⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[12,15,16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[19],3⟩,⟨[12,19],1⟩,⟨[14,15,19],1⟩,⟨[11,13,16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4873
namespace Case4873
def big : Finset (Finset (Fin 9)) := {{0,1,3},{1,4,5,6},{2,4,7},{3,4,8},{0,2,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,1,3},{2,3},{0,4},{3,5},{0,6},{2,6},{3,6},{1,4,5,6},{0,7},{1,7},{3,7},{2,4,7},{5,7},{1,8},{3,4,8},{0,2,5,8},{6,7,8}]
end Case4873
namespace Case4874
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{0,3},{1,3},{4},{1,4},{5},{3,5},{0,2,4,5},{6},{0,6},{2,6},{3,4,6},{7},{0,1,7},{2,7},{3,7},{5,7},{6,7},{8},{0,8},{2,3,8},{1,5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={0,2,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={7} then 1 else if T={0,1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],3⟩,⟨[13,15],1⟩,⟨[10,12,14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[17],1⟩,⟨[10,11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[10,18],1⟩,⟨[12,13,18],1⟩,⟨[11,15,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4874
namespace Case4874
def big : Finset (Finset (Fin 9)) := {{0,2,4,5},{3,4,6},{0,1,7},{2,3,8},{1,5,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{1,4},{3,5},{0,2,4,5},{0,6},{2,6},{3,4,6},{0,1,7},{2,7},{3,7},{5,7},{6,7},{0,8},{2,3,8},{1,5,6,8},{4,7,8}]
end Case4874
namespace Case4875
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{0,3},{1,3},{4},{0,4},{2,3,4},{5},{3,5},{6},{0,6},{2,6},{1,4,5,6},{7},{0,1,7},{2,7},{3,7},{5,7},{6,7},{8},{1,8},{0,2,5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={2,3,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,4,5,6} then 1 else if T={7} then 1 else if T={0,1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={1,8} then 1 else if T={0,2,5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[10,14],1⟩,⟨[12,13,14],1⟩,⟨[15],3⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[11,14,15,16],1⟩,⟨[17],1⟩,⟨[10,11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[11,18],1⟩,⟨[10,12,15,18],1⟩,⟨[13,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4875
namespace Case4875
def big : Finset (Finset (Fin 9)) := {{2,3,4},{1,4,5,6},{0,1,7},{0,2,5,8},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{0,4},{2,3,4},{3,5},{0,6},{2,6},{1,4,5,6},{0,1,7},{2,7},{3,7},{5,7},{6,7},{1,8},{0,2,5,8},{3,6,8},{4,7,8}]
end Case4875
namespace Case4876
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{1,2},{3},{0,3},{4},{1,4},{5},{0,2,4,5},{6},{0,6},{2,6},{1,3,5,6},{7},{0,1,7},{2,7},{3,4,7},{5,7},{6,7},{8},{0,8},{1,8},{2,3,8},{5,8},{4,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={5} then 3 else if T={0,2,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,3,5,6} then 1 else if T={7} then 1 else if T={0,1,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[10,13],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],3⟩,⟨[10,12,14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[11,13,15,16],1⟩,⟨[17],1⟩,⟨[10,11,17],1⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,13,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4876
namespace Case4876
def big : Finset (Finset (Fin 9)) := {{0,2,4,5},{1,3,5,6},{0,1,7},{3,4,7},{2,3,8},{4,6,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,4},{0,2,4,5},{0,6},{2,6},{1,3,5,6},{0,1,7},{2,7},{3,4,7},{5,7},{6,7},{0,8},{1,8},{2,3,8},{5,8},{4,6,8},{7,8}]
end Case4876
namespace Case4877
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1,2},{0,3},{1,3},{2,3},{4},{1,4},{5},{2,5},{3,5},{6},{0,6},{2,6},{3,4,6},{7},{1,7},{2,7},{0,4,5,7},{6,7},{8},{0,8},{2,4,8},{1,5,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={0,4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={1,5,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11,12],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[10,14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[10,18],1⟩,⟨[12,14,18],1⟩,⟨[11,15,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4877
namespace Case4877
def big : Finset (Finset (Fin 9)) := {{0,1,2},{3,4,6},{0,4,5,7},{2,4,8},{1,5,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{0,3},{1,3},{2,3},{1,4},{2,5},{3,5},{0,6},{2,6},{3,4,6},{1,7},{2,7},{0,4,5,7},{6,7},{0,8},{2,4,8},{1,5,6,8},{3,7,8}]
end Case4877
namespace Case4878
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1,2},{3},{1,3},{4},{0,4},{2,3,4},{5},{2,5},{6},{1,6},{2,6},{0,3,5,6},{7},{0,7},{2,7},{1,4,5,7},{6,7},{8},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={2,3,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[10,14],1⟩,⟨[12,13,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[10,13,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[11,14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4878
namespace Case4878
def big : Finset (Finset (Fin 9)) := {{0,1,2},{2,3,4},{0,3,5,6},{1,4,5,7},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{1,3},{0,4},{2,3,4},{2,5},{1,6},{2,6},{0,3,5,6},{0,7},{2,7},{1,4,5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]
end Case4878
namespace Case4879
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{3},{0,3},{4},{1,4},{5},{2,5},{6},{1,6},{2,3,6},{0,4,5,6},{7},{0,7},{2,4,7},{1,3,5,7},{6,7},{8},{0,1,8},{2,8},{3,4,8},{5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={0,4,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,4,7} then 1 else if T={1,3,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,1,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[10,13],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,13,16],1⟩,⟨[10,14,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,14,17],1⟩,⟨[11,13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,11,18],1⟩,⟨[12,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4879
namespace Case4879
def big : Finset (Finset (Fin 9)) := {{2,3,6},{0,4,5,6},{2,4,7},{1,3,5,7},{0,1,8},{3,4,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,4},{2,5},{1,6},{2,3,6},{0,4,5,6},{0,7},{2,4,7},{1,3,5,7},{6,7},{0,1,8},{2,8},{3,4,8},{5,8},{6,8},{7,8}]
end Case4879
namespace Case4880
def positionFn : Fin 9 → Fin 25 := ![19,12,13,20,11,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{1,2},{1,3},{2,3},{0,4},{3,4},{5},{3,5},{4,5},{6},{1,6},{0,3,6},{4,6},{7},{2,4,7},{0,1,5,7},{6,7},{8},{0,8},{1,4,8},{2,5,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={3,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,3,6} then 1 else if T={4,6} then 1 else if T={7} then 3 else if T={2,4,7} then 1 else if T={0,1,5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={2,5,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,13,14,20,21,22,23,24,25],[⟨[],2⟩,⟨[20],1⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[14,20],1⟩,⟨[13,14],1⟩,⟨[13,21],1⟩,⟨[14,21],1⟩,⟨[12,20],1⟩,⟨[12,21],1⟩,⟨[22],3⟩,⟨[21,22],1⟩,⟨[12,22],1⟩,⟨[23],2⟩,⟨[13,23],1⟩,⟨[20,21,23],1⟩,⟨[12,23],1⟩,⟨[24],3⟩,⟨[12,14,24],1⟩,⟨[13,20,22,24],1⟩,⟨[23,24],1⟩,⟨[25],3⟩,⟨[20,25],1⟩,⟨[12,13,25],1⟩,⟨[14,22,23,25],1⟩,⟨[21,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4880
namespace Case4880
def big : Finset (Finset (Fin 9)) := {{0,3,6},{2,4,7},{0,1,5,7},{1,4,8},{2,5,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{2,3},{0,4},{3,4},{3,5},{4,5},{1,6},{0,3,6},{4,6},{2,4,7},{0,1,5,7},{6,7},{0,8},{1,4,8},{2,5,6,8},{3,7,8}]
end Case4880
namespace Case4881
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{1,2},{1,3},{2,3},{4},{5},{3,5},{0,2,4,5},{6},{2,6},{0,3,6},{4,6},{7},{0,7},{3,7},{1,4,7},{5,7},{6,7},{8},{0,8},{3,4,8},{1,5,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={5} then 3 else if T={3,5} then 1 else if T={0,2,4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,3,6} then 1 else if T={4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={3,7} then 1 else if T={1,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={3,4,8} then 1 else if T={1,5,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[15],3⟩,⟨[13,15],1⟩,⟨[10,12,14,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[10,13,16],1⟩,⟨[14,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[13,17],1⟩,⟨[11,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[10,18],1⟩,⟨[13,14,18],1⟩,⟨[11,15,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4881
namespace Case4881
def big : Finset (Finset (Fin 9)) := {{0,2,4,5},{0,3,6},{1,4,7},{3,4,8},{1,5,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{1,3},{2,3},{3,5},{0,2,4,5},{2,6},{0,3,6},{4,6},{0,7},{3,7},{1,4,7},{5,7},{6,7},{0,8},{3,4,8},{1,5,6,8},{2,7,8}]
end Case4881
namespace Case4882
def positionFn : Fin 9 → Fin 25 := ![14,18,19,11,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{1,2},{1,3},{2,3},{4},{0,4},{5},{3,5},{6},{1,6},{0,3,6},{2,4,5,6},{7},{0,7},{3,7},{1,4,7},{5,7},{6,7},{8},{3,4,8},{0,1,5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,3,6} then 1 else if T={2,4,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={3,7} then 1 else if T={1,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={3,4,8} then 1 else if T={0,1,5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,15,19,20,21,22,23,24,25],[⟨[],2⟩,⟨[15],1⟩,⟨[19],1⟩,⟨[20],1⟩,⟨[15,20],1⟩,⟨[19,20],1⟩,⟨[12,19],1⟩,⟨[12,20],1⟩,⟨[21],2⟩,⟨[15,21],1⟩,⟨[22],3⟩,⟨[12,22],1⟩,⟨[23],2⟩,⟨[19,23],1⟩,⟨[12,15,23],1⟩,⟨[20,21,22,23],1⟩,⟨[24],1⟩,⟨[15,24],1⟩,⟨[12,24],1⟩,⟨[19,21,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[25],3⟩,⟨[12,21,25],1⟩,⟨[15,19,22,25],1⟩,⟨[23,25],1⟩,⟨[20,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4882
namespace Case4882
def big : Finset (Finset (Fin 9)) := {{0,3,6},{2,4,5,6},{1,4,7},{3,4,8},{0,1,5,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{2,3},{0,4},{3,5},{1,6},{0,3,6},{2,4,5,6},{0,7},{3,7},{1,4,7},{5,7},{6,7},{3,4,8},{0,1,5,8},{6,8},{2,7,8}]
end Case4882
namespace Case4883
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{0,2},{2,3},{4},{0,3,4},{5},{3,5},{1,2,4,5},{6},{1,6},{3,6},{4,6},{7},{0,7},{1,7},{3,7},{5,7},{2,6,7},{8},{2,8},{1,3,8},{0,5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,3,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={1,2,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 3 else if T={2,8} then 1 else if T={1,3,8} then 1 else if T={0,5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[10,13,14],1⟩,⟨[15],3⟩,⟨[13,15],1⟩,⟨[11,12,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[12,16,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[11,13,18],1⟩,⟨[10,15,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4883
namespace Case4883
def big : Finset (Finset (Fin 9)) := {{0,3,4},{1,2,4,5},{2,6,7},{1,3,8},{0,5,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{2,3},{0,3,4},{3,5},{1,2,4,5},{1,6},{3,6},{4,6},{0,7},{1,7},{3,7},{5,7},{2,6,7},{2,8},{1,3,8},{0,5,6,8},{4,7,8}]
end Case4883
namespace Case4884
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{1,2},{2,3},{4},{2,4},{0,3,4},{5},{3,5},{6},{0,6},{3,6},{1,4,5,6},{7},{0,7},{1,7},{3,7},{5,7},{2,6,7},{8},{1,3,8},{0,2,5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={3,6} then 1 else if T={1,4,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 3 else if T={1,3,8} then 1 else if T={0,2,5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[13,15],1⟩,⟨[11,14,15],1⟩,⟨[16],3⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[14,17],1⟩,⟨[12,15,16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[14,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩,⟨[19],3⟩,⟨[12,14,19],1⟩,⟨[11,13,16,19],1⟩,⟨[17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4884
namespace Case4884
def big : Finset (Finset (Fin 9)) := {{0,3,4},{1,4,5,6},{2,6,7},{1,3,8},{0,2,5,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{2,3},{2,4},{0,3,4},{3,5},{0,6},{3,6},{1,4,5,6},{0,7},{1,7},{3,7},{5,7},{2,6,7},{1,3,8},{0,2,5,8},{6,8},{4,7,8}]
end Case4884
namespace Case4885
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{1,2},{3},{4},{2,4},{5},{0,2,3,5},{6},{0,6},{3,6},{1,4,5,6},{7},{2,7},{1,3,7},{0,4,7},{5,7},{6,7},{8},{0,8},{1,8},{3,4,8},{5,8},{2,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={2,4} then 1 else if T={5} then 3 else if T={0,2,3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={3,6} then 1 else if T={1,4,5,6} then 1 else if T={7} then 1 else if T={2,7} then 1 else if T={1,3,7} then 1 else if T={0,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[12,14],1⟩,⟨[15],3⟩,⟨[10,12,13,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[13,16],1⟩,⟨[11,14,15,16],1⟩,⟨[17],1⟩,⟨[12,17],1⟩,⟨[11,13,17],1⟩,⟨[10,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[12,16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4885
namespace Case4885
def big : Finset (Finset (Fin 9)) := {{0,2,3,5},{1,4,5,6},{1,3,7},{0,4,7},{3,4,8},{2,6,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{2,4},{0,2,3,5},{0,6},{3,6},{1,4,5,6},{2,7},{1,3,7},{0,4,7},{5,7},{6,7},{0,8},{1,8},{3,4,8},{5,8},{2,6,8},{7,8}]
end Case4885
namespace Case4886
def positionFn : Fin 9 → Fin 25 := ![14,18,11,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{2,3},{4},{5},{2,5},{3,5},{0,1,4,5},{6},{1,6},{0,2,6},{3,6},{4,6},{7},{0,7},{1,7},{2,7},{3,4,7},{8},{0,8},{1,3,8},{2,4,8},{5,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={5} then 3 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,1,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={1,3,8} then 1 else if T={2,4,8} then 1 else if T={5,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,15,19,20,21,22,23,24,25],[⟨[],2⟩,⟨[15],1⟩,⟨[19],1⟩,⟨[12,19],1⟩,⟨[15,20],1⟩,⟨[12,20],1⟩,⟨[21],2⟩,⟨[22],3⟩,⟨[12,22],1⟩,⟨[20,22],1⟩,⟨[15,19,21,22],1⟩,⟨[23],2⟩,⟨[19,23],1⟩,⟨[12,15,23],1⟩,⟨[20,23],1⟩,⟨[21,23],1⟩,⟨[24],2⟩,⟨[15,24],1⟩,⟨[19,24],1⟩,⟨[12,24],1⟩,⟨[20,21,24],1⟩,⟨[25],3⟩,⟨[15,25],1⟩,⟨[19,20,25],1⟩,⟨[12,21,25],1⟩,⟨[22,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4886
namespace Case4886
def big : Finset (Finset (Fin 9)) := {{0,1,4,5},{0,2,6},{3,4,7},{1,3,8},{2,4,8},{5,6,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{2,3},{2,5},{3,5},{0,1,4,5},{1,6},{0,2,6},{3,6},{4,6},{0,7},{1,7},{2,7},{3,4,7},{0,8},{1,3,8},{2,4,8},{5,6,7,8}]
end Case4886
namespace Case4887
def positionFn : Fin 9 → Fin 25 := ![14,18,11,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{2,3},{4},{1,4},{0,2,4},{5},{2,5},{3,5},{6},{0,6},{2,6},{1,3,6},{7},{0,7},{1,7},{3,7},{4,5,6,7},{8},{3,4,8},{0,1,5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={0,2,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,3,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={4,5,6,7} then 1 else if T={8} then 3 else if T={3,4,8} then 1 else if T={0,1,5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,15,19,20,21,22,23,24,25],[⟨[],2⟩,⟨[15],1⟩,⟨[19],1⟩,⟨[12,19],1⟩,⟨[15,20],1⟩,⟨[12,20],1⟩,⟨[21],2⟩,⟨[19,21],1⟩,⟨[12,15,21],1⟩,⟨[22],3⟩,⟨[12,22],1⟩,⟨[20,22],1⟩,⟨[23],2⟩,⟨[15,23],1⟩,⟨[12,23],1⟩,⟨[19,20,23],1⟩,⟨[24],2⟩,⟨[15,24],1⟩,⟨[19,24],1⟩,⟨[20,24],1⟩,⟨[21,22,23,24],1⟩,⟨[25],3⟩,⟨[20,21,25],1⟩,⟨[15,19,22,25],1⟩,⟨[23,25],1⟩,⟨[12,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4887
namespace Case4887
def big : Finset (Finset (Fin 9)) := {{0,2,4},{1,3,6},{4,5,6,7},{3,4,8},{0,1,5,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{2,3},{1,4},{0,2,4},{2,5},{3,5},{0,6},{2,6},{1,3,6},{0,7},{1,7},{3,7},{4,5,6,7},{3,4,8},{0,1,5,8},{6,8},{2,7,8}]
end Case4887
namespace Case4888
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{0,3},{4},{2,3,4},{5},{2,5},{0,1,4,5},{6},{1,6},{0,2,6},{4,6},{7},{0,7},{1,7},{2,7},{3,5,6,7},{8},{0,8},{2,8},{1,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 2 else if T={2,3,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={0,1,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,2,6} then 1 else if T={4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[10,13],1⟩,⟨[14],2⟩,⟨[12,13,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[10,11,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[10,12,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,15,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[12,18],1⟩,⟨[11,13,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4888
namespace Case4888
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,1,4,5},{0,2,6},{3,5,6,7},{1,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{2,3,4},{2,5},{0,1,4,5},{1,6},{0,2,6},{4,6},{0,7},{1,7},{2,7},{3,5,6,7},{0,8},{2,8},{1,3,8},{5,8},{6,8},{4,7,8}]
end Case4888
namespace Case4889
def positionFn : Fin 9 → Fin 25 := ![14,18,11,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{1,3},{0,2,3},{4},{5},{2,5},{0,1,4,5},{6},{0,6},{2,6},{4,6},{7},{0,7},{1,7},{2,4,7},{3,5,6,7},{8},{0,8},{2,8},{3,4,8},{5,8},{1,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={4} then 2 else if T={5} then 3 else if T={2,5} then 1 else if T={0,1,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={3,5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={1,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,15,19,20,21,22,23,24,25],[⟨[],2⟩,⟨[15],1⟩,⟨[19],1⟩,⟨[12,19],1⟩,⟨[20],2⟩,⟨[19,20],1⟩,⟨[12,15,20],1⟩,⟨[21],2⟩,⟨[22],3⟩,⟨[12,22],1⟩,⟨[15,19,21,22],1⟩,⟨[23],2⟩,⟨[15,23],1⟩,⟨[12,23],1⟩,⟨[21,23],1⟩,⟨[24],2⟩,⟨[15,24],1⟩,⟨[19,24],1⟩,⟨[12,21,24],1⟩,⟨[20,22,23,24],1⟩,⟨[25],1⟩,⟨[15,25],1⟩,⟨[12,25],1⟩,⟨[20,21,25],1⟩,⟨[22,25],1⟩,⟨[19,23,25],1⟩,⟨[24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4889
namespace Case4889
def big : Finset (Finset (Fin 9)) := {{0,2,3},{0,1,4,5},{2,4,7},{3,5,6,7},{3,4,8},{1,6,8}}
def full : List (Finset (Fin 9)) := [{1,2},{1,3},{0,2,3},{2,5},{0,1,4,5},{0,6},{2,6},{4,6},{0,7},{1,7},{2,4,7},{3,5,6,7},{0,8},{2,8},{3,4,8},{5,8},{1,6,8},{7,8}]
end Case4889
namespace Case4890
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{1,2},{0,3},{2,3},{4},{0,2,4},{5},{2,5},{3,5},{6},{2,6},{1,3,6},{4,6},{7},{0,7},{3,7},{1,4,5,7},{6,7},{8},{1,8},{3,4,8},{0,5,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,2,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={1,3,6} then 1 else if T={4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,7} then 1 else if T={1,4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={1,8} then 1 else if T={3,4,8} then 1 else if T={0,5,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[10,12,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[11,13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[13,17],1⟩,⟨[11,14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[11,18],1⟩,⟨[13,14,18],1⟩,⟨[10,15,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4890
namespace Case4890
def big : Finset (Finset (Fin 9)) := {{0,2,4},{1,3,6},{1,4,5,7},{3,4,8},{0,5,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{0,3},{2,3},{0,2,4},{2,5},{3,5},{2,6},{1,3,6},{4,6},{0,7},{3,7},{1,4,5,7},{6,7},{1,8},{3,4,8},{0,5,6,8},{2,7,8}]
end Case4890
namespace Case4891
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{1,2},{0,3},{2,3},{4},{0,4},{5},{2,5},{3,5},{6},{0,2,6},{3,6},{1,4,5,6},{7},{1,7},{2,7},{3,4,7},{6,7},{8},{1,3,8},{2,4,8},{6,8},{0,5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,2,6} then 1 else if T={3,6} then 1 else if T={1,4,5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={1,3,8} then 1 else if T={2,4,8} then 1 else if T={6,8} then 1 else if T={0,5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[10,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[10,12,16],1⟩,⟨[13,16],1⟩,⟨[11,14,15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[11,13,18],1⟩,⟨[12,14,18],1⟩,⟨[16,18],1⟩,⟨[10,15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4891
namespace Case4891
def big : Finset (Finset (Fin 9)) := {{0,2,6},{1,4,5,6},{3,4,7},{1,3,8},{2,4,8},{0,5,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{0,3},{2,3},{0,4},{2,5},{3,5},{0,2,6},{3,6},{1,4,5,6},{1,7},{2,7},{3,4,7},{6,7},{1,3,8},{2,4,8},{6,8},{0,5,7,8}]
end Case4891
namespace Case4892
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{1,2},{3},{4},{0,4},{2,3,4},{5},{2,5},{6},{0,2,6},{3,6},{1,4,5,6},{7},{1,7},{2,7},{0,3,5,7},{6,7},{8},{0,8},{2,8},{1,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={0,4} then 1 else if T={2,3,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={6} then 2 else if T={0,2,6} then 1 else if T={3,6} then 1 else if T={1,4,5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={0,3,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[13,14,15],1⟩,⟨[16],3⟩,⟨[13,16],1⟩,⟨[17],2⟩,⟨[11,13,17],1⟩,⟨[14,17],1⟩,⟨[12,15,16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[11,14,16,18],1⟩,⟨[17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[13,19],1⟩,⟨[12,14,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4892
namespace Case4892
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,2,6},{1,4,5,6},{0,3,5,7},{1,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{0,4},{2,3,4},{2,5},{0,2,6},{3,6},{1,4,5,6},{1,7},{2,7},{0,3,5,7},{6,7},{0,8},{2,8},{1,3,8},{5,8},{6,8},{4,7,8}]
end Case4892
namespace Case4893
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{1,2},{3},{0,2,3},{4},{1,4},{5},{2,5},{6},{2,6},{3,6},{0,4,5,6},{7},{0,7},{2,4,7},{1,3,5,7},{6,7},{8},{0,8},{2,8},{3,4,8},{5,8},{1,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={3,6} then 1 else if T={0,4,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,4,7} then 1 else if T={1,3,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={1,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[10,12,13],1⟩,⟨[14],2⟩,⟨[11,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[10,14,15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,14,17],1⟩,⟨[11,13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[12,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[11,16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4893
namespace Case4893
def big : Finset (Finset (Fin 9)) := {{0,2,3},{0,4,5,6},{2,4,7},{1,3,5,7},{3,4,8},{1,6,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{0,2,3},{1,4},{2,5},{2,6},{3,6},{0,4,5,6},{0,7},{2,4,7},{1,3,5,7},{6,7},{0,8},{2,8},{3,4,8},{5,8},{1,6,8},{7,8}]
end Case4893
namespace Case4894
def positionFn : Fin 9 → Fin 25 := ![14,11,18,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{4},{0,4},{1,3,4},{5},{1,5},{2,5},{6},{0,1,6},{2,6},{3,6},{7},{1,7},{2,4,7},{0,3,5,7},{6,7},{8},{0,8},{1,8},{2,3,8},{4,5,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={5} then 3 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 2 else if T={0,1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={0,3,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={4,5,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,15,19,20,21,22,23,24,25],[⟨[],2⟩,⟨[15],1⟩,⟨[15,19],1⟩,⟨[12,19],1⟩,⟨[20],2⟩,⟨[21],2⟩,⟨[15,21],1⟩,⟨[12,20,21],1⟩,⟨[22],3⟩,⟨[12,22],1⟩,⟨[19,22],1⟩,⟨[23],2⟩,⟨[12,15,23],1⟩,⟨[19,23],1⟩,⟨[20,23],1⟩,⟨[24],2⟩,⟨[12,24],1⟩,⟨[19,21,24],1⟩,⟨[15,20,22,24],1⟩,⟨[23,24],1⟩,⟨[25],2⟩,⟨[15,25],1⟩,⟨[12,25],1⟩,⟨[19,20,25],1⟩,⟨[21,22,23,25],1⟩,⟨[24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4894
namespace Case4894
def big : Finset (Finset (Fin 9)) := {{1,3,4},{0,1,6},{2,4,7},{0,3,5,7},{2,3,8},{4,5,6,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,4},{1,3,4},{1,5},{2,5},{0,1,6},{2,6},{3,6},{1,7},{2,4,7},{0,3,5,7},{6,7},{0,8},{1,8},{2,3,8},{4,5,6,8},{7,8}]
end Case4894
namespace Case4895
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{0,3},{1,3},{2,3},{4},{0,2,4},{5},{2,5},{3,5},{6},{0,6},{2,6},{1,4,5,6},{7},{1,7},{2,7},{4,7},{3,6,7},{8},{1,2,8},{3,4,8},{6,8},{0,5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,2,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,4,5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={4,7} then 1 else if T={3,6,7} then 1 else if T={8} then 3 else if T={1,2,8} then 1 else if T={3,4,8} then 1 else if T={6,8} then 1 else if T={0,5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[10,12,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[11,14,15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[14,17],1⟩,⟨[13,16,17],1⟩,⟨[18],3⟩,⟨[11,12,18],1⟩,⟨[13,14,18],1⟩,⟨[16,18],1⟩,⟨[10,15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case4895
namespace Case4895
def big : Finset (Finset (Fin 9)) := {{0,2,4},{1,4,5,6},{3,6,7},{1,2,8},{3,4,8},{0,5,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,3},{1,3},{2,3},{0,2,4},{2,5},{3,5},{0,6},{2,6},{1,4,5,6},{1,7},{2,7},{4,7},{3,6,7},{1,2,8},{3,4,8},{6,8},{0,5,7,8}]
end Case4895
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case24
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{1,3},{4},{2,4},{5},{2,5},{0,3,5},{1,4,5},{6},{3,6},{0,4,6},{5,6},{7},{0,7},{2,3,7},{4,7},{1,6,7},{8},{0,8},{1,8},{3,4,8},{2,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={0,3,5} then 1 else if T={1,4,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,3,7} then 1 else if T={4,7} then 1 else if T={1,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,4,8} then 1 else if T={2,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[13,16],1⟩,⟨[11,14,16],1⟩,⟨[12,15,16],1⟩,⟨[17],2⟩,⟨[14,17],1⟩,⟨[11,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[12,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[14,15,19],1⟩,⟨[13,17,19],1⟩,⟨[16,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case24
namespace Case24
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,5},{1,4,5},{0,4,6},{2,3,7},{1,6,7},{3,4,8},{2,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{1,3},{2,4},{2,5},{0,3,5},{1,4,5},{3,6},{0,4,6},{5,6},{0,7},{2,3,7},{4,7},{1,6,7},{0,8},{1,8},{3,4,8},{2,6,8},{5,7,8}]
end Case24
namespace Case25
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{2,3},{4},{1,4},{2,4},{5},{1,3,5},{0,4,5},{6},{1,6},{0,3,6},{5,6},{7},{0,7},{3,4,7},{5,7},{2,6,7},{8},{0,8},{3,8},{2,5,8},{4,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={1,3,5} then 1 else if T={0,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={3,8} then 1 else if T={2,5,8} then 1 else if T={4,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[12,14,16],1⟩,⟨[11,15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[11,14,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[14,19],1⟩,⟨[13,16,19],1⟩,⟨[15,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case25
namespace Case25
def big : Finset (Finset (Fin 9)) := {{0,1,2},{1,3,5},{0,4,5},{0,3,6},{3,4,7},{2,6,7},{2,5,8},{4,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{2,3},{1,4},{2,4},{1,3,5},{0,4,5},{1,6},{0,3,6},{5,6},{0,7},{3,4,7},{5,7},{2,6,7},{0,8},{3,8},{2,5,8},{4,6,8},{1,7,8}]
end Case25
namespace Case26
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{2,3},{4},{1,4},{5},{0,5},{1,3,5},{2,4,5},{6},{0,3,6},{4,6},{5,6},{7},{1,7},{3,7},{0,4,7},{2,6,7},{8},{0,8},{2,8},{3,4,8},{1,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 2 else if T={0,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={3,7} then 1 else if T={0,4,7} then 1 else if T={2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={1,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,14,16],1⟩,⟨[13,15,16],1⟩,⟨[17],2⟩,⟨[11,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[14,18],1⟩,⟨[11,15,18],1⟩,⟨[13,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,19],1⟩,⟨[14,15,19],1⟩,⟨[12,17,19],1⟩,⟨[16,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case26
namespace Case26
def big : Finset (Finset (Fin 9)) := {{0,1,2},{1,3,5},{2,4,5},{0,3,6},{0,4,7},{2,6,7},{3,4,8},{1,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{2,3},{1,4},{0,5},{1,3,5},{2,4,5},{0,3,6},{4,6},{5,6},{1,7},{3,7},{0,4,7},{2,6,7},{0,8},{2,8},{3,4,8},{1,6,8},{5,7,8}]
end Case26
namespace Case27
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{2,3},{4},{1,4},{0,3,4},{5},{1,3,5},{4,5},{6},{0,6},{2,4,6},{5,6},{7},{1,7},{2,7},{0,5,7},{3,6,7},{8},{0,8},{3,8},{2,5,8},{1,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={1,3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={0,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={3,8} then 1 else if T={2,5,8} then 1 else if T={1,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[11,14,15],1⟩,⟨[16],2⟩,⟨[12,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[11,16,18],1⟩,⟨[14,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[14,19],1⟩,⟨[13,16,19],1⟩,⟨[12,17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case27
namespace Case27
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,4},{1,3,5},{2,4,6},{0,5,7},{3,6,7},{2,5,8},{1,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{2,3},{1,4},{0,3,4},{1,3,5},{4,5},{0,6},{2,4,6},{5,6},{1,7},{2,7},{0,5,7},{3,6,7},{0,8},{3,8},{2,5,8},{1,6,8},{4,7,8}]
end Case27
namespace Case28
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{2,3},{4},{0,4},{1,4},{5},{2,5},{1,3,5},{6},{1,6},{0,3,6},{4,5,6},{7},{3,7},{2,4,7},{0,5,7},{6,7},{8},{0,8},{3,4,8},{5,8},{2,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={1,3,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={0,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],2⟩,⟨[13,16],1⟩,⟨[12,14,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[11,14,17],1⟩,⟨[15,16,17],1⟩,⟨[18],2⟩,⟨[14,18],1⟩,⟨[13,15,18],1⟩,⟨[11,16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[14,15,19],1⟩,⟨[16,19],1⟩,⟨[13,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case28
namespace Case28
def big : Finset (Finset (Fin 9)) := {{0,1,2},{1,3,5},{0,3,6},{4,5,6},{2,4,7},{0,5,7},{3,4,8},{2,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{2,3},{0,4},{1,4},{2,5},{1,3,5},{1,6},{0,3,6},{4,5,6},{3,7},{2,4,7},{0,5,7},{6,7},{0,8},{3,4,8},{5,8},{2,6,8},{1,7,8}]
end Case28
namespace Case29
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{2,3},{4},{1,4},{2,4},{5},{1,5},{0,3,5},{6},{3,6},{0,4,6},{2,5,6},{7},{0,7},{1,3,7},{4,5,7},{6,7},{8},{0,8},{3,4,8},{5,8},{1,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={0,3,5} then 1 else if T={6} then 2 else if T={3,6} then 1 else if T={0,4,6} then 1 else if T={2,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={1,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[11,14,16],1⟩,⟨[17],2⟩,⟨[14,17],1⟩,⟨[11,15,17],1⟩,⟨[13,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,14,18],1⟩,⟨[15,16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[14,15,19],1⟩,⟨[16,19],1⟩,⟨[12,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case29
namespace Case29
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,5},{0,4,6},{2,5,6},{1,3,7},{4,5,7},{3,4,8},{1,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{2,3},{1,4},{2,4},{1,5},{0,3,5},{3,6},{0,4,6},{2,5,6},{0,7},{1,3,7},{4,5,7},{6,7},{0,8},{3,4,8},{5,8},{1,6,8},{2,7,8}]
end Case29
namespace Case30
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{2,3},{4},{0,4},{1,4},{5},{1,2,5},{0,3,5},{6},{0,1,6},{3,6},{2,4,6},{5,6},{7},{1,7},{0,2,7},{3,4,7},{5,7},{8},{0,8},{2,8},{1,3,8},{4,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={1,2,5} then 1 else if T={0,3,5} then 1 else if T={6} then 2 else if T={0,1,6} then 1 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,3,8} then 1 else if T={4,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],2⟩,⟨[11,12,15],1⟩,⟨[10,13,15],1⟩,⟨[16],2⟩,⟨[10,11,16],1⟩,⟨[13,16],1⟩,⟨[12,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[10,12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,18],1⟩,⟨[11,13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case30
namespace Case30
def big : Finset (Finset (Fin 9)) := {{1,2,5},{0,3,5},{0,1,6},{2,4,6},{0,2,7},{3,4,7},{1,3,8},{4,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{2,3},{0,4},{1,4},{1,2,5},{0,3,5},{0,1,6},{3,6},{2,4,6},{5,6},{1,7},{0,2,7},{3,4,7},{5,7},{0,8},{2,8},{1,3,8},{4,5,8},{6,7,8}]
end Case30
namespace Case31
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{3},{0,3},{2,3},{4},{1,4},{2,4},{5},{0,1,5},{3,4,5},{6},{0,2,6},{1,3,6},{5,6},{7},{0,7},{1,2,7},{5,7},{4,6,7},{8},{1,8},{0,4,8},{2,5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={0,1,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={0,2,6} then 1 else if T={1,3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={0,4,8} then 1 else if T={2,5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[10,11,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[10,12,16],1⟩,⟨[11,13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,12,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[10,14,18],1⟩,⟨[12,15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case31
namespace Case31
def big : Finset (Finset (Fin 9)) := {{0,1,5},{3,4,5},{0,2,6},{1,3,6},{1,2,7},{4,6,7},{0,4,8},{2,5,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{2,3},{1,4},{2,4},{0,1,5},{3,4,5},{0,2,6},{1,3,6},{5,6},{0,7},{1,2,7},{5,7},{4,6,7},{1,8},{0,4,8},{2,5,8},{6,8},{3,7,8}]
end Case31
namespace Case32
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{2,3},{4},{1,4},{0,3,4},{5},{0,5},{1,3,5},{6},{0,6},{2,4,6},{5,6},{7},{1,7},{4,7},{2,5,7},{3,6,7},{8},{2,8},{3,8},{4,5,8},{1,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={0,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={4,7} then 1 else if T={2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[11,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,14,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[15,18],1⟩,⟨[13,16,18],1⟩,⟨[14,17,18],1⟩,⟨[19],2⟩,⟨[13,19],1⟩,⟨[14,19],1⟩,⟨[15,16,19],1⟩,⟨[12,17,19],1⟩,⟨[11,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case32
namespace Case32
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{2,3},{1,4},{0,3,4},{0,5},{1,3,5},{0,6},{2,4,6},{5,6},{1,7},{4,7},{2,5,7},{3,6,7},{2,8},{3,8},{4,5,8},{1,6,8},{0,7,8}]
end Case32
namespace Case33
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{2,3},{4},{1,4},{5},{0,5},{1,3,5},{2,4,5},{6},{0,6},{3,4,6},{5,6},{7},{1,7},{0,3,7},{4,7},{2,6,7},{8},{2,8},{3,8},{0,4,8},{1,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,3,7} then 1 else if T={4,7} then 1 else if T={2,6,7} then 1 else if T={8} then 2 else if T={2,8} then 1 else if T={3,8} then 1 else if T={0,4,8} then 1 else if T={1,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,14,16],1⟩,⟨[13,15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[13,17,18],1⟩,⟨[19],2⟩,⟨[13,19],1⟩,⟨[14,19],1⟩,⟨[11,15,19],1⟩,⟨[12,17,19],1⟩,⟨[16,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case33
namespace Case33
def big : Finset (Finset (Fin 9)) := {{0,1,2},{1,3,5},{2,4,5},{3,4,6},{0,3,7},{2,6,7},{0,4,8},{1,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{2,3},{1,4},{0,5},{1,3,5},{2,4,5},{0,6},{3,4,6},{5,6},{1,7},{0,3,7},{4,7},{2,6,7},{2,8},{3,8},{0,4,8},{1,6,8},{5,7,8}]
end Case33
namespace Case34
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,1,2},{3},{2,3},{4},{2,4},{3,4},{5},{1,5},{0,3,5},{6},{0,6},{1,3,6},{4,5,6},{7},{1,7},{0,4,7},{5,7},{2,6,7},{8},{0,8},{1,4,8},{2,5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={0,3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,4,7} then 1 else if T={5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={2,5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[11,14,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,14,17],1⟩,⟨[15,16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[11,15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,15,19],1⟩,⟨[13,16,19],1⟩,⟨[17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case34
namespace Case34
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,5},{1,3,6},{4,5,6},{0,4,7},{2,6,7},{1,4,8},{2,5,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{2,3},{2,4},{3,4},{1,5},{0,3,5},{0,6},{1,3,6},{4,5,6},{1,7},{0,4,7},{5,7},{2,6,7},{0,8},{1,4,8},{2,5,8},{6,8},{3,7,8}]
end Case34
namespace Case35
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{3},{2,3},{4},{2,4},{3,4},{5},{0,2,5},{1,3,5},{6},{1,2,6},{0,4,6},{5,6},{7},{0,3,7},{1,4,7},{5,7},{6,7},{8},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={0,2,5} then 1 else if T={1,3,5} then 1 else if T={6} then 2 else if T={1,2,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,3,7} then 1 else if T={1,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[10,12,15],1⟩,⟨[11,13,15],1⟩,⟨[16],2⟩,⟨[11,12,16],1⟩,⟨[10,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,13,17],1⟩,⟨[11,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[14,15,18],1⟩,⟨[13,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case35
namespace Case35
def big : Finset (Finset (Fin 9)) := {{0,2,5},{1,3,5},{1,2,6},{0,4,6},{0,3,7},{1,4,7},{4,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{2,3},{2,4},{3,4},{0,2,5},{1,3,5},{1,2,6},{0,4,6},{5,6},{0,3,7},{1,4,7},{5,7},{6,7},{0,8},{1,8},{4,5,8},{3,6,8},{2,7,8}]
end Case35
namespace Case36
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1,3},{2,3},{1,4},{0,2,4},{3,4},{5},{0,5},{1,2,5},{3,5},{4,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{0,7},{1,7},{2,7},{4,7},{3,6,7},{8},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,1,3} then 1 else if T={2,3} then 1 else if T={1,4} then 1 else if T={0,2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={4,7} then 1 else if T={3,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],6⟩,⟨[11,12,14],1⟩,⟨[13,14],1⟩,⟨[12,15],1⟩,⟨[11,13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[15,18],1⟩,⟨[14,17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,19],1⟩,⟨[14,19],1⟩,⟨[15,17,19],1⟩,⟨[16,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case36
namespace Case36
def big : Finset (Finset (Fin 9)) := {{0,1,3},{0,2,4},{1,2,5},{3,6,7},{4,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,3},{2,3},{1,4},{0,2,4},{3,4},{0,5},{1,2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,7},{4,7},{3,6,7},{0,8},{1,8},{2,8},{3,8},{4,6,8},{5,7,8}]
end Case36
namespace Case37
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1,2},{2,3},{0,4},{1,4},{3,4},{5},{1,5},{2,5},{0,3,5},{6},{0,6},{2,6},{1,3,6},{4,6},{5,6},{7},{0,7},{1,7},{3,7},{2,4,7},{5,7},{8},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,1,2} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={0,3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],6⟩,⟨[10,11,12],1⟩,⟨[12,13],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[10,13,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[11,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case37
namespace Case37
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,5},{1,3,6},{2,4,7},{4,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{2,3},{0,4},{1,4},{3,4},{1,5},{2,5},{0,3,5},{0,6},{2,6},{1,3,6},{4,6},{5,6},{0,7},{1,7},{3,7},{2,4,7},{5,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}]
end Case37
namespace Case38
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1,2},{2,3},{0,4},{1,4},{2,4},{3,4},{5},{1,5},{2,5},{0,3,5},{6},{0,6},{2,6},{1,3,6},{5,6},{7},{0,7},{1,7},{3,7},{4,5,7},{6,7},{8},{0,8},{1,8},{3,8},{5,8},{4,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,1,2} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={0,3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,3,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],6⟩,⟨[11,12,13],1⟩,⟨[13,14],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[11,14,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[12,14,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[14,18],1⟩,⟨[15,16,18],1⟩,⟨[17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[14,19],1⟩,⟨[16,19],1⟩,⟨[15,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case38
namespace Case38
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,5},{1,3,6},{4,5,7},{4,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{2,3},{0,4},{1,4},{2,4},{3,4},{1,5},{2,5},{0,3,5},{0,6},{2,6},{1,3,6},{5,6},{0,7},{1,7},{3,7},{4,5,7},{6,7},{0,8},{1,8},{3,8},{5,8},{4,6,8},{2,7,8}]
end Case38
namespace Case39
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1,2},{1,3},{2,3},{0,4},{2,4},{3,4},{5},{2,5},{0,3,5},{1,4,5},{6},{0,6},{1,6},{4,6},{5,6},{7},{0,7},{1,7},{3,7},{5,7},{2,6,7},{8},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={0,3,5} then 1 else if T={1,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],6⟩,⟨[10,11,12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[10,13,15],1⟩,⟨[11,14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[12,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[15,18],1⟩,⟨[13,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case39
namespace Case39
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,5},{1,4,5},{2,6,7},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{1,3},{2,3},{0,4},{2,4},{3,4},{2,5},{0,3,5},{1,4,5},{0,6},{1,6},{4,6},{5,6},{0,7},{1,7},{3,7},{5,7},{2,6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
end Case39
namespace Case40
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1,2},{1,3},{2,3},{0,4},{2,4},{5},{1,5},{0,3,5},{4,5},{6},{0,6},{2,6},{3,6},{1,4,6},{5,6},{7},{0,7},{1,7},{2,7},{3,4,7},{5,7},{8},{0,8},{1,8},{3,8},{4,8},{2,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={0,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,8} then 1 else if T={4,8} then 1 else if T={2,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],6⟩,⟨[10,11,12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[10,13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[11,14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[13,18],1⟩,⟨[14,18],1⟩,⟨[12,15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case40
namespace Case40
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,5},{1,4,6},{3,4,7},{2,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{1,3},{2,3},{0,4},{2,4},{1,5},{0,3,5},{4,5},{0,6},{2,6},{3,6},{1,4,6},{5,6},{0,7},{1,7},{2,7},{3,4,7},{5,7},{0,8},{1,8},{3,8},{4,8},{2,5,8},{6,7,8}]
end Case40
namespace Case41
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1,2},{1,3},{2,3},{0,4},{2,4},{3,4},{5},{1,5},{0,3,5},{4,5},{6},{0,6},{2,6},{1,4,6},{5,6},{7},{0,7},{1,7},{3,7},{2,5,7},{6,7},{8},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={0,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],6⟩,⟨[10,11,12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[10,13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[11,14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[15,18],1⟩,⟨[13,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case41
namespace Case41
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,5},{1,4,6},{2,5,7},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{1,3},{2,3},{0,4},{2,4},{3,4},{1,5},{0,3,5},{4,5},{0,6},{2,6},{1,4,6},{5,6},{0,7},{1,7},{3,7},{2,5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
end Case41
namespace Case42
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1,2},{1,3},{2,3},{0,4},{1,4},{2,4},{5},{2,5},{0,3,5},{4,5},{6},{0,6},{1,6},{3,4,6},{5,6},{7},{0,7},{2,7},{3,7},{1,5,7},{6,7},{8},{0,8},{1,8},{3,8},{5,8},{2,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={0,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={1,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],6⟩,⟨[10,11,12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[10,13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[11,15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[13,18],1⟩,⟨[15,18],1⟩,⟨[12,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case42
namespace Case42
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,5},{3,4,6},{1,5,7},{2,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{1,3},{2,3},{0,4},{1,4},{2,4},{2,5},{0,3,5},{4,5},{0,6},{1,6},{3,4,6},{5,6},{0,7},{2,7},{3,7},{1,5,7},{6,7},{0,8},{1,8},{3,8},{5,8},{2,6,8},{4,7,8}]
end Case42
namespace Case43
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1,2},{1,3},{2,3},{1,4},{2,4},{0,3,4},{5},{0,5},{3,5},{4,5},{6},{0,6},{2,6},{4,6},{1,5,6},{7},{0,7},{1,7},{3,7},{2,5,7},{6,7},{8},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={1,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],6⟩,⟨[11,12,13],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[11,14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[12,16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[14,18],1⟩,⟨[13,16,18],1⟩,⟨[17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case43
namespace Case43
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,4},{1,5,6},{2,5,7},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{1,3},{2,3},{1,4},{2,4},{0,3,4},{0,5},{3,5},{4,5},{0,6},{2,6},{4,6},{1,5,6},{0,7},{1,7},{3,7},{2,5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
end Case43
namespace Case44
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1,2},{1,3},{2,3},{0,4},{1,4},{2,4},{5},{1,5},{2,5},{0,3,5},{6},{0,6},{2,6},{3,4,6},{5,6},{7},{0,7},{3,7},{4,7},{5,7},{1,6,7},{8},{0,8},{1,8},{3,8},{4,5,8},{6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={0,3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={3,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={1,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={3,8} then 1 else if T={4,5,8} then 1 else if T={6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],6⟩,⟨[10,11,12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[10,13,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[11,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case44
namespace Case44
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,5},{3,4,6},{1,6,7},{4,5,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{1,3},{2,3},{0,4},{1,4},{2,4},{1,5},{2,5},{0,3,5},{0,6},{2,6},{3,4,6},{5,6},{0,7},{3,7},{4,7},{5,7},{1,6,7},{0,8},{1,8},{3,8},{4,5,8},{6,8},{2,7,8}]
end Case44
namespace Case45
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{5},{0,1,5},{2,5},{3,4,5},{6},{1,6},{0,2,6},{4,6},{5,6},{7},{0,7},{1,2,7},{3,7},{5,7},{6,7},{8},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={0,1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={0,2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],6⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],1⟩,⟨[11,12,16],1⟩,⟨[13,16],1⟩,⟨[14,15,16],1⟩,⟨[17],1⟩,⟨[12,17],1⟩,⟨[11,13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,13,18],1⟩,⟨[14,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case45
namespace Case45
def big : Finset (Finset (Fin 9)) := {{0,1,5},{3,4,5},{0,2,6},{1,2,7},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,1,5},{2,5},{3,4,5},{1,6},{0,2,6},{4,6},{5,6},{0,7},{1,2,7},{3,7},{5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
end Case45
namespace Case46
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1,2},{0,3},{1,3},{0,4},{2,4},{3,4},{5},{0,1,5},{2,3,5},{4,5},{6},{1,6},{0,2,6},{3,6},{5,6},{7},{0,7},{2,7},{1,4,7},{5,7},{6,7},{8},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,1,5} then 1 else if T={2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={0,2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],6⟩,⟨[11,12],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[10,11,15],1⟩,⟨[12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[10,12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[11,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[15,18],1⟩,⟨[14,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case46
namespace Case46
def big : Finset (Finset (Fin 9)) := {{0,1,5},{2,3,5},{0,2,6},{1,4,7},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{1,3},{0,4},{2,4},{3,4},{0,1,5},{2,3,5},{4,5},{1,6},{0,2,6},{3,6},{5,6},{0,7},{2,7},{1,4,7},{5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]
end Case46
namespace Case47
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1,2},{0,3},{2,3},{0,4},{1,4},{5},{0,2,5},{1,3,5},{4,5},{6},{0,1,6},{2,6},{3,6},{4,6},{5,6},{7},{0,7},{1,7},{3,7},{2,4,7},{5,7},{8},{0,8},{1,8},{2,8},{3,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={1,2} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,2,5} then 1 else if T={1,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],6⟩,⟨[11,12],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[10,12,15],1⟩,⟨[11,13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[10,11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case47
namespace Case47
def big : Finset (Finset (Fin 9)) := {{0,2,5},{1,3,5},{0,1,6},{2,4,7},{3,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{2,3},{0,4},{1,4},{0,2,5},{1,3,5},{4,5},{0,1,6},{2,6},{3,6},{4,6},{5,6},{0,7},{1,7},{3,7},{2,4,7},{5,7},{0,8},{1,8},{2,8},{3,4,8},{5,8},{6,7,8}]
end Case47
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

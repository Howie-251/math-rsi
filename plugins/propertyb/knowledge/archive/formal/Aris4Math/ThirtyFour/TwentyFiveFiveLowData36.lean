import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case864
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{3},{1,3},{0,2,3},{4},{1,4},{5},{0,5},{2,5},{3,5},{4,5},{6},{2,6},{0,4,6},{1,5,6},{7},{0,7},{1,2,7},{3,4,7},{6,7},{8},{0,8},{1,8},{2,4,8},{3,6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,4,6} then 1 else if T={1,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={3,4,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={3,6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[13,17],1⟩,⟨[11,15,17],1⟩,⟨[12,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,13,18],1⟩,⟨[14,15,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,15,19],1⟩,⟨[14,17,19],1⟩,⟨[16,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case864
namespace Case864
def big : Finset (Finset (Fin 9)) := {{0,2,3},{0,4,6},{1,5,6},{1,2,7},{3,4,7},{2,4,8},{3,6,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{0,2,3},{1,4},{0,5},{2,5},{3,5},{4,5},{2,6},{0,4,6},{1,5,6},{0,7},{1,2,7},{3,4,7},{6,7},{0,8},{1,8},{2,4,8},{3,6,8},{5,7,8}]
end Case864
namespace Case865
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{1,2},{3},{1,3},{4},{0,4},{1,4},{5},{0,5},{2,5},{3,5},{6},{0,2,6},{3,4,6},{1,5,6},{7},{0,3,7},{2,4,7},{5,7},{6,7},{8},{0,8},{2,3,8},{4,5,8},{6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,2,6} then 1 else if T={3,4,6} then 1 else if T={1,5,6} then 1 else if T={7} then 2 else if T={0,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={4,5,8} then 1 else if T={6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[10,12,16],1⟩,⟨[13,14,16],1⟩,⟨[11,15,16],1⟩,⟨[17],2⟩,⟨[10,13,17],1⟩,⟨[12,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[11,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case865
namespace Case865
def big : Finset (Finset (Fin 9)) := {{0,2,6},{3,4,6},{1,5,6},{0,3,7},{2,4,7},{2,3,8},{4,5,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{1,3},{0,4},{1,4},{0,5},{2,5},{3,5},{0,2,6},{3,4,6},{1,5,6},{0,3,7},{2,4,7},{5,7},{6,7},{0,8},{2,3,8},{4,5,8},{6,8},{1,7,8}]
end Case865
namespace Case866
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,1,2},{3},{1,3},{2,3},{4},{0,4},{5},{2,5},{0,3,5},{1,4,5},{6},{0,6},{1,6},{4,6},{5,6},{7},{0,7},{2,4,7},{5,7},{3,6,7},{8},{0,8},{3,4,8},{5,8},{2,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={0,3,5} then 1 else if T={1,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],1⟩,⟨[13,16],1⟩,⟨[11,14,16],1⟩,⟨[12,15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[14,15,19],1⟩,⟨[16,19],1⟩,⟨[13,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case866
namespace Case866
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,5},{1,4,5},{2,4,7},{3,6,7},{3,4,8},{2,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{1,3},{2,3},{0,4},{2,5},{0,3,5},{1,4,5},{0,6},{1,6},{4,6},{5,6},{0,7},{2,4,7},{5,7},{3,6,7},{0,8},{3,4,8},{5,8},{2,6,8},{1,7,8}]
end Case866
namespace Case867
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,1,2},{3},{1,3},{2,3},{4},{0,4},{5},{2,5},{0,3,5},{4,5},{6},{0,6},{1,6},{3,4,6},{5,6},{7},{0,7},{2,4,7},{1,5,7},{6,7},{8},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={0,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,4,7} then 1 else if T={1,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],1⟩,⟨[13,16],1⟩,⟨[11,14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,15,18],1⟩,⟨[12,16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[13,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case867
namespace Case867
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,5},{3,4,6},{2,4,7},{1,5,7},{1,4,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{1,3},{2,3},{0,4},{2,5},{0,3,5},{4,5},{0,6},{1,6},{3,4,6},{5,6},{0,7},{2,4,7},{1,5,7},{6,7},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
end Case867
namespace Case868
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,1,2},{3},{1,3},{2,3},{4},{0,4},{5},{1,5},{0,3,5},{4,5},{6},{0,6},{2,6},{1,4,6},{5,6},{7},{0,7},{2,4,7},{5,7},{3,6,7},{8},{0,8},{3,4,8},{2,5,8},{6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={0,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={3,4,8} then 1 else if T={2,5,8} then 1 else if T={6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],1⟩,⟨[12,16],1⟩,⟨[11,14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[14,15,19],1⟩,⟨[13,16,19],1⟩,⟨[17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case868
namespace Case868
def big : Finset (Finset (Fin 9)) := {{0,1,2},{0,3,5},{1,4,6},{2,4,7},{3,6,7},{3,4,8},{2,5,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{1,3},{2,3},{0,4},{1,5},{0,3,5},{4,5},{0,6},{2,6},{1,4,6},{5,6},{0,7},{2,4,7},{5,7},{3,6,7},{0,8},{3,4,8},{2,5,8},{6,8},{1,7,8}]
end Case868
namespace Case869
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{1,2},{3},{0,3},{4},{0,4},{5},{0,1,5},{3,5},{2,4,5},{6},{0,6},{2,6},{1,3,6},{4,6},{5,6},{7},{1,7},{0,2,7},{3,4,7},{5,7},{8},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={0,1,5} then 1 else if T={3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[15],1⟩,⟨[10,11,15],1⟩,⟨[13,15],1⟩,⟨[12,14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[11,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[10,12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case869
namespace Case869
def big : Finset (Finset (Fin 9)) := {{0,1,5},{2,4,5},{1,3,6},{0,2,7},{3,4,7},{2,3,8},{1,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,4},{0,1,5},{3,5},{2,4,5},{0,6},{2,6},{1,3,6},{4,6},{5,6},{1,7},{0,2,7},{3,4,7},{5,7},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
end Case869
namespace Case870
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{1,2},{3},{0,3},{4},{0,4},{1,3,4},{5},{0,1,5},{2,3,5},{4,5},{6},{0,6},{2,6},{3,6},{5,6},{7},{1,7},{0,2,7},{5,7},{4,6,7},{8},{0,8},{2,4,8},{5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={5} then 1 else if T={0,1,5} then 1 else if T={2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,2,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[10,11,15],1⟩,⟨[12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[10,12,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[11,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case870
namespace Case870
def big : Finset (Finset (Fin 9)) := {{1,3,4},{0,1,5},{2,3,5},{0,2,7},{4,6,7},{2,4,8},{1,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,4},{1,3,4},{0,1,5},{2,3,5},{4,5},{0,6},{2,6},{3,6},{5,6},{1,7},{0,2,7},{5,7},{4,6,7},{0,8},{2,4,8},{5,8},{1,6,8},{3,7,8}]
end Case870
namespace Case871
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{1,2},{3},{0,3},{4},{0,4},{2,3,4},{5},{0,1,5},{3,5},{4,5},{6},{0,6},{2,6},{1,3,6},{5,6},{7},{1,7},{0,2,7},{5,7},{4,6,7},{8},{0,8},{1,4,8},{2,5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,3,4} then 1 else if T={5} then 1 else if T={0,1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,2,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={2,5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[10,11,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[11,13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[10,12,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,14,18],1⟩,⟨[12,15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case871
namespace Case871
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,1,5},{1,3,6},{0,2,7},{4,6,7},{1,4,8},{2,5,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,4},{2,3,4},{0,1,5},{3,5},{4,5},{0,6},{2,6},{1,3,6},{5,6},{1,7},{0,2,7},{5,7},{4,6,7},{0,8},{1,4,8},{2,5,8},{6,8},{3,7,8}]
end Case871
namespace Case872
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{1,2},{3},{0,3},{4},{0,4},{2,3,4},{5},{0,1,5},{2,5},{3,5},{6},{0,6},{1,3,6},{4,6},{5,6},{7},{1,7},{0,2,7},{4,5,7},{6,7},{8},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,3,4} then 1 else if T={5} then 1 else if T={0,1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,2,7} then 1 else if T={4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[10,11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[11,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[10,12,17],1⟩,⟨[14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[12,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case872
namespace Case872
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,1,5},{1,3,6},{0,2,7},{4,5,7},{1,4,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,4},{2,3,4},{0,1,5},{2,5},{3,5},{0,6},{1,3,6},{4,6},{5,6},{1,7},{0,2,7},{4,5,7},{6,7},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
end Case872
namespace Case873
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{1,2},{3},{0,3},{4},{0,4},{1,3,4},{5},{0,1,5},{2,5},{3,5},{6},{0,6},{2,3,6},{4,6},{5,6},{7},{1,7},{0,2,7},{4,5,7},{6,7},{8},{0,8},{2,4,8},{5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={5} then 1 else if T={0,1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,2,7} then 1 else if T={4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[10,11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[12,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[10,12,17],1⟩,⟨[14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[11,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case873
namespace Case873
def big : Finset (Finset (Fin 9)) := {{1,3,4},{0,1,5},{2,3,6},{0,2,7},{4,5,7},{2,4,8},{1,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,4},{1,3,4},{0,1,5},{2,5},{3,5},{0,6},{2,3,6},{4,6},{5,6},{1,7},{0,2,7},{4,5,7},{6,7},{0,8},{2,4,8},{5,8},{1,6,8},{3,7,8}]
end Case873
namespace Case874
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{1,2},{3},{0,3},{4},{0,4},{5},{0,1,5},{2,5},{3,5},{4,5},{6},{0,6},{1,3,6},{2,4,6},{5,6},{7},{1,7},{0,2,7},{3,4,7},{6,7},{8},{0,8},{2,3,8},{1,4,8},{6,8},{5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={0,1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,3,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={0,2,7} then 1 else if T={3,4,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={6,8} then 1 else if T={5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[15],1⟩,⟨[10,11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[11,13,16],1⟩,⟨[12,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[10,12,17],1⟩,⟨[13,14,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,13,18],1⟩,⟨[11,14,18],1⟩,⟨[16,18],1⟩,⟨[15,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case874
namespace Case874
def big : Finset (Finset (Fin 9)) := {{0,1,5},{1,3,6},{2,4,6},{0,2,7},{3,4,7},{2,3,8},{1,4,8},{5,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,4},{0,1,5},{2,5},{3,5},{4,5},{0,6},{1,3,6},{2,4,6},{5,6},{1,7},{0,2,7},{3,4,7},{6,7},{0,8},{2,3,8},{1,4,8},{6,8},{5,7,8}]
end Case874
namespace Case875
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,3},{1,2,3},{4},{0,4},{5},{0,1,5},{3,5},{4,5},{6},{0,6},{2,6},{1,4,6},{5,6},{7},{1,7},{3,4,7},{2,5,7},{6,7},{8},{1,8},{2,4,8},{5,8},{3,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={0,1,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={2,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],1⟩,⟨[11,12,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[14,15,18],1⟩,⟨[13,16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[12,19],1⟩,⟨[13,15,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[11,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case875
namespace Case875
def big : Finset (Finset (Fin 9)) := {{1,2,3},{0,1,5},{1,4,6},{3,4,7},{2,5,7},{2,4,8},{3,6,8},{0,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{1,2,3},{0,4},{0,1,5},{3,5},{4,5},{0,6},{2,6},{1,4,6},{5,6},{1,7},{3,4,7},{2,5,7},{6,7},{1,8},{2,4,8},{5,8},{3,6,8},{0,7,8}]
end Case875
namespace Case876
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,1,2},{3},{0,3},{4},{0,4},{1,3,4},{5},{1,5},{2,3,5},{4,5},{6},{0,6},{2,6},{3,6},{5,6},{7},{1,7},{2,7},{0,5,7},{4,6,7},{8},{0,8},{2,4,8},{5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={0,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,14,15],1⟩,⟨[16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[11,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,15,19],1⟩,⟨[16,19],1⟩,⟨[12,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case876
namespace Case876
def big : Finset (Finset (Fin 9)) := {{0,1,2},{1,3,4},{2,3,5},{0,5,7},{4,6,7},{2,4,8},{1,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{0,3},{0,4},{1,3,4},{1,5},{2,3,5},{4,5},{0,6},{2,6},{3,6},{5,6},{1,7},{2,7},{0,5,7},{4,6,7},{0,8},{2,4,8},{5,8},{1,6,8},{3,7,8}]
end Case876
namespace Case877
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,1,2},{3},{0,3},{4},{0,4},{5},{2,5},{1,3,5},{4,5},{6},{0,6},{1,6},{3,6},{2,4,6},{5,6},{7},{1,7},{2,7},{3,4,7},{0,5,7},{8},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={1,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={0,5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],1⟩,⟨[13,16],1⟩,⟨[12,14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[14,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[14,15,18],1⟩,⟨[11,16,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,14,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case877
namespace Case877
def big : Finset (Finset (Fin 9)) := {{0,1,2},{1,3,5},{2,4,6},{3,4,7},{0,5,7},{2,3,8},{1,4,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{0,3},{0,4},{2,5},{1,3,5},{4,5},{0,6},{1,6},{3,6},{2,4,6},{5,6},{1,7},{2,7},{3,4,7},{0,5,7},{0,8},{2,3,8},{1,4,8},{5,8},{6,7,8}]
end Case877
namespace Case878
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,1,2},{3},{0,3},{4},{0,4},{1,3,4},{5},{2,5},{3,5},{4,5},{6},{0,6},{1,6},{2,3,6},{5,6},{7},{1,7},{2,7},{0,5,7},{4,6,7},{8},{0,8},{2,4,8},{1,5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={2} then 1 else if T={0,1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,3,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={0,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={1,5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,14,15],1⟩,⟨[16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[11,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,15,19],1⟩,⟨[12,16,19],1⟩,⟨[17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case878
namespace Case878
def big : Finset (Finset (Fin 9)) := {{0,1,2},{1,3,4},{2,3,6},{0,5,7},{4,6,7},{2,4,8},{1,5,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2},{0,3},{0,4},{1,3,4},{2,5},{3,5},{4,5},{0,6},{1,6},{2,3,6},{5,6},{1,7},{2,7},{0,5,7},{4,6,7},{0,8},{2,4,8},{1,5,8},{6,8},{3,7,8}]
end Case878
namespace Case879
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,3},{1,2,3},{4},{0,4},{5},{2,5},{3,5},{1,4,5},{6},{0,6},{1,6},{4,6},{5,6},{7},{0,1,7},{2,4,7},{5,7},{3,6,7},{8},{1,8},{3,4,8},{0,5,8},{2,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={1,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,1,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={3,4,8} then 1 else if T={0,5,8} then 1 else if T={2,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[12,15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,12,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩,⟨[19],2⟩,⟨[12,19],1⟩,⟨[14,15,19],1⟩,⟨[11,16,19],1⟩,⟨[13,17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case879
namespace Case879
def big : Finset (Finset (Fin 9)) := {{1,2,3},{1,4,5},{0,1,7},{2,4,7},{3,6,7},{3,4,8},{0,5,8},{2,6,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{1,2,3},{0,4},{2,5},{3,5},{1,4,5},{0,6},{1,6},{4,6},{5,6},{0,1,7},{2,4,7},{5,7},{3,6,7},{1,8},{3,4,8},{0,5,8},{2,6,8},{7,8}]
end Case879
namespace Case880
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{0,3},{1,2,3},{4},{0,4},{5},{1,5},{2,5},{4,5},{6},{0,6},{3,6},{1,4,6},{5,6},{7},{0,1,7},{2,4,7},{3,5,7},{6,7},{8},{1,8},{3,4,8},{0,5,8},{2,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,1,7} then 1 else if T={2,4,7} then 1 else if T={3,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={3,4,8} then 1 else if T={0,5,8} then 1 else if T={2,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[14,17],1⟩,⟨[12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,12,18],1⟩,⟨[13,15,18],1⟩,⟨[14,16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[12,19],1⟩,⟨[14,15,19],1⟩,⟨[11,16,19],1⟩,⟨[13,17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case880
namespace Case880
def big : Finset (Finset (Fin 9)) := {{1,2,3},{1,4,6},{0,1,7},{2,4,7},{3,5,7},{3,4,8},{0,5,8},{2,6,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{1,2,3},{0,4},{1,5},{2,5},{4,5},{0,6},{3,6},{1,4,6},{5,6},{0,1,7},{2,4,7},{3,5,7},{6,7},{1,8},{3,4,8},{0,5,8},{2,6,8},{7,8}]
end Case880
namespace Case881
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{3},{1,3},{2,3},{4},{0,4},{2,4},{5},{1,5},{0,2,5},{3,4,5},{6},{1,6},{0,3,6},{5,6},{7},{0,7},{1,2,7},{5,7},{4,6,7},{8},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={0,2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[10,12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[10,13,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,12,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[12,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case881
namespace Case881
def big : Finset (Finset (Fin 9)) := {{0,2,5},{3,4,5},{0,3,6},{1,2,7},{4,6,7},{1,4,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{2,3},{0,4},{2,4},{1,5},{0,2,5},{3,4,5},{1,6},{0,3,6},{5,6},{0,7},{1,2,7},{5,7},{4,6,7},{0,8},{1,4,8},{5,8},{2,6,8},{3,7,8}]
end Case881
namespace Case882
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{1,2},{3},{1,3},{0,2,3},{4},{3,4},{5},{1,5},{2,5},{0,4,5},{6},{0,6},{1,4,6},{5,6},{7},{0,7},{2,4,7},{5,7},{3,6,7},{8},{0,8},{4,8},{3,5,8},{2,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={0,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={4,8} then 1 else if T={3,5,8} then 1 else if T={2,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[11,15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[15,19],1⟩,⟨[14,16,19],1⟩,⟨[13,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case882
namespace Case882
def big : Finset (Finset (Fin 9)) := {{0,2,3},{0,4,5},{1,4,6},{2,4,7},{3,6,7},{3,5,8},{2,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{1,3},{0,2,3},{3,4},{1,5},{2,5},{0,4,5},{0,6},{1,4,6},{5,6},{0,7},{2,4,7},{5,7},{3,6,7},{0,8},{4,8},{3,5,8},{2,6,8},{1,7,8}]
end Case882
namespace Case883
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{3},{1,3},{0,2,3},{4},{0,4},{2,4},{5},{0,5},{1,2,5},{3,5},{6},{0,6},{1,4,6},{5,6},{7},{1,7},{3,4,7},{5,7},{2,6,7},{8},{1,8},{2,8},{4,5,8},{3,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={2,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩,⟨[19],2⟩,⟨[12,19],1⟩,⟨[13,19],1⟩,⟨[15,16,19],1⟩,⟨[14,17,19],1⟩,⟨[11,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case883
namespace Case883
def big : Finset (Finset (Fin 9)) := {{0,2,3},{1,2,5},{1,4,6},{3,4,7},{2,6,7},{4,5,8},{3,6,8},{0,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{0,2,3},{0,4},{2,4},{0,5},{1,2,5},{3,5},{0,6},{1,4,6},{5,6},{1,7},{3,4,7},{5,7},{2,6,7},{1,8},{2,8},{4,5,8},{3,6,8},{0,7,8}]
end Case883
namespace Case884
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{3},{0,3},{4},{1,4},{2,4},{5},{1,5},{0,2,5},{3,5},{6},{1,6},{2,3,6},{0,4,6},{5,6},{7},{0,7},{1,2,7},{3,4,7},{5,7},{8},{0,8},{2,8},{1,3,8},{4,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={0,2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,3,8} then 1 else if T={4,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[10,12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,13,16],1⟩,⟨[10,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[18],2⟩,⟨[10,18],1⟩,⟨[12,18],1⟩,⟨[11,13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case884
namespace Case884
def big : Finset (Finset (Fin 9)) := {{0,2,5},{2,3,6},{0,4,6},{1,2,7},{3,4,7},{1,3,8},{4,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,3},{1,4},{2,4},{1,5},{0,2,5},{3,5},{1,6},{2,3,6},{0,4,6},{5,6},{0,7},{1,2,7},{3,4,7},{5,7},{0,8},{2,8},{1,3,8},{4,5,8},{6,7,8}]
end Case884
namespace Case885
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{3},{1,3},{4},{0,4},{2,4},{5},{1,5},{0,2,5},{3,5},{6},{0,6},{1,2,6},{3,4,6},{5,6},{7},{0,7},{2,3,7},{1,4,7},{5,7},{8},{1,8},{2,8},{0,3,8},{4,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={0,2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,3,7} then 1 else if T={1,4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={2,8} then 1 else if T={0,3,8} then 1 else if T={4,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[10,12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[11,12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,13,17],1⟩,⟨[11,14,17],1⟩,⟨[15,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[10,13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case885
namespace Case885
def big : Finset (Finset (Fin 9)) := {{0,2,5},{1,2,6},{3,4,6},{2,3,7},{1,4,7},{0,3,8},{4,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{0,4},{2,4},{1,5},{0,2,5},{3,5},{0,6},{1,2,6},{3,4,6},{5,6},{0,7},{2,3,7},{1,4,7},{5,7},{1,8},{2,8},{0,3,8},{4,5,8},{6,7,8}]
end Case885
namespace Case886
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{3},{1,3},{0,2,3},{4},{1,4},{2,4},{5},{0,5},{1,2,5},{3,5},{6},{1,6},{0,4,6},{5,6},{7},{0,7},{3,4,7},{5,7},{2,6,7},{8},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,8} then 1 else if T={4,5,8} then 1 else if T={3,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[11,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[14,15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[13,19],1⟩,⟨[15,16,19],1⟩,⟨[14,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case886
namespace Case886
def big : Finset (Finset (Fin 9)) := {{0,2,3},{1,2,5},{0,4,6},{3,4,7},{2,6,7},{4,5,8},{3,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{0,2,3},{1,4},{2,4},{0,5},{1,2,5},{3,5},{1,6},{0,4,6},{5,6},{0,7},{3,4,7},{5,7},{2,6,7},{0,8},{2,8},{4,5,8},{3,6,8},{1,7,8}]
end Case886
namespace Case887
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{1,2},{3},{1,3},{0,2,3},{4},{3,4},{5},{0,5},{2,5},{1,4,5},{6},{1,6},{0,4,6},{5,6},{7},{0,7},{2,4,7},{5,7},{3,6,7},{8},{0,8},{4,8},{3,5,8},{2,6,8},{1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={0,2,3} then 1 else if T={4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={1,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={4,8} then 1 else if T={3,5,8} then 1 else if T={2,6,8} then 1 else if T={1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[12,14],1⟩,⟨[11,13,14],1⟩,⟨[15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[12,15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[11,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[15,19],1⟩,⟨[14,16,19],1⟩,⟨[13,17,19],1⟩,⟨[12,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case887
namespace Case887
def big : Finset (Finset (Fin 9)) := {{0,2,3},{1,4,5},{0,4,6},{2,4,7},{3,6,7},{3,5,8},{2,6,8},{1,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{1,3},{0,2,3},{3,4},{0,5},{2,5},{1,4,5},{1,6},{0,4,6},{5,6},{0,7},{2,4,7},{5,7},{3,6,7},{0,8},{4,8},{3,5,8},{2,6,8},{1,7,8}]
end Case887
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

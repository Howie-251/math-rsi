import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case1992
def positionFn : Fin 9 → Fin 25 := ![8,9,10,11,12,13,14,15,16]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{2,3},{4},{1,4},{5},{0,1,2,5},{6},{0,3,4,6},{5,6},{7},{0,7},{1,3,7},{4,5,7},{2,6,7},{8},{0,8},{2,4,8},{3,5,8},{1,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={5} then 3 else if T={0,1,2,5} then 1 else if T={6} then 3 else if T={0,3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={4,5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={3,5,8} then 1 else if T={1,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,16,17],[⟨[9],2⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[10,13],1⟩,⟨[14],3⟩,⟨[9,10,11,14],1⟩,⟨[15],3⟩,⟨[9,12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[9,16],1⟩,⟨[10,12,16],1⟩,⟨[13,14,16],1⟩,⟨[11,15,16],1⟩,⟨[17],2⟩,⟨[9,17],1⟩,⟨[11,13,17],1⟩,⟨[12,14,17],1⟩,⟨[10,15,17],1⟩,⟨[16,17],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1992
namespace Case1992
def big : Finset (Finset (Fin 9)) := {{0,1,2,5},{0,3,4,6},{1,3,7},{4,5,7},{2,6,7},{2,4,8},{3,5,8},{1,6,8}}
def full : List (Finset (Fin 9)) := [{2,3},{1,4},{0,1,2,5},{0,3,4,6},{5,6},{0,7},{1,3,7},{4,5,7},{2,6,7},{0,8},{2,4,8},{3,5,8},{1,6,8},{7,8}]
end Case1992
namespace Case1993
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{2,3},{4},{0,4},{1,2,4},{5},{3,4,5},{6},{0,1,3,6},{5,6},{7},{1,7},{0,2,5,7},{4,6,7},{8},{0,8},{4,8},{1,5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={5} then 3 else if T={3,4,5} then 1 else if T={6} then 3 else if T={0,1,3,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={0,2,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={4,8} then 1 else if T={1,5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],2⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,13,15],1⟩,⟨[16],3⟩,⟨[14,15,16],1⟩,⟨[17],3⟩,⟨[11,12,14,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[11,13,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[15,19],1⟩,⟨[12,16,19],1⟩,⟨[13,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1993
namespace Case1993
def big : Finset (Finset (Fin 9)) := {{1,2,4},{3,4,5},{0,1,3,6},{0,2,5,7},{4,6,7},{1,5,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{2,3},{0,4},{1,2,4},{3,4,5},{0,1,3,6},{5,6},{1,7},{0,2,5,7},{4,6,7},{0,8},{4,8},{1,5,8},{2,6,8},{3,7,8}]
end Case1993
namespace Case1994
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{2,3},{4},{0,4},{5},{1,4,5},{6},{0,1,3,6},{2,4,6},{5,6},{7},{1,7},{3,4,7},{0,2,5,7},{8},{0,8},{1,2,8},{4,8},{3,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={5} then 3 else if T={1,4,5} then 1 else if T={6} then 3 else if T={0,1,3,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={3,4,7} then 1 else if T={0,2,5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,2,8} then 1 else if T={4,8} then 1 else if T={3,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],2⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[16],3⟩,⟨[12,15,16],1⟩,⟨[17],3⟩,⟨[11,12,14,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[14,15,18],1⟩,⟨[11,13,16,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,13,19],1⟩,⟨[15,19],1⟩,⟨[14,16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1994
namespace Case1994
def big : Finset (Finset (Fin 9)) := {{1,4,5},{0,1,3,6},{2,4,6},{3,4,7},{0,2,5,7},{1,2,8},{3,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{2,3},{0,4},{1,4,5},{0,1,3,6},{2,4,6},{5,6},{1,7},{3,4,7},{0,2,5,7},{0,8},{1,2,8},{4,8},{3,5,8},{6,7,8}]
end Case1994
namespace Case1995
def positionFn : Fin 9 → Fin 25 := ![8,9,10,11,12,13,14,15,16]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{0,3},{4},{0,4},{3,4},{5},{1,3,5},{2,4,5},{6},{1,6},{2,3,6},{7},{2,7},{1,4,7},{0,5,6,7},{8},{0,1,2,8},{5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={3,4} then 1 else if T={5} then 3 else if T={1,3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={7} then 3 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 3 else if T={0,1,2,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[9,10,11,12,13,14,15,16,17],[⟨[9],2⟩,⟨[10],2⟩,⟨[11],2⟩,⟨[12],1⟩,⟨[9,12],1⟩,⟨[13],1⟩,⟨[9,13],1⟩,⟨[12,13],1⟩,⟨[14],3⟩,⟨[10,12,14],1⟩,⟨[11,13,14],1⟩,⟨[15],3⟩,⟨[10,15],1⟩,⟨[11,12,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[10,13,16],1⟩,⟨[9,14,15,16],1⟩,⟨[17],3⟩,⟨[9,10,11,17],1⟩,⟨[14,17],1⟩,⟨[13,15,17],1⟩,⟨[12,16,17],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1995
namespace Case1995
def big : Finset (Finset (Fin 9)) := {{1,3,5},{2,4,5},{2,3,6},{1,4,7},{0,5,6,7},{0,1,2,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{3,4},{1,3,5},{2,4,5},{1,6},{2,3,6},{2,7},{1,4,7},{0,5,6,7},{0,1,2,8},{5,8},{4,6,8},{3,7,8}]
end Case1995
namespace Case1996
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{0,3},{1,2,3},{4},{0,4},{3,4},{5},{1,4,5},{6},{2,4,6},{5,6},{7},{1,7},{0,2,5,7},{3,6,7},{8},{2,8},{3,5,8},{0,1,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={3,4} then 1 else if T={5} then 3 else if T={1,4,5} then 1 else if T={6} then 3 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={0,2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 3 else if T={2,8} then 1 else if T={3,5,8} then 1 else if T={0,1,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],2⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[12,15,16],1⟩,⟨[17],3⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[11,13,16,18],1⟩,⟨[14,17,18],1⟩,⟨[19],3⟩,⟨[13,19],1⟩,⟨[14,16,19],1⟩,⟨[11,12,17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1996
namespace Case1996
def big : Finset (Finset (Fin 9)) := {{1,2,3},{1,4,5},{2,4,6},{0,2,5,7},{3,6,7},{3,5,8},{0,1,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,2,3},{0,4},{3,4},{1,4,5},{2,4,6},{5,6},{1,7},{0,2,5,7},{3,6,7},{2,8},{3,5,8},{0,1,6,8},{4,7,8}]
end Case1996
namespace Case1997
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{1,2},{3},{0,3},{4},{0,4},{3,4},{5},{1,3,5},{6},{2,3,6},{4,5,6},{7},{1,4,7},{0,2,5,7},{6,7},{8},{2,4,8},{5,8},{0,1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={3,4} then 1 else if T={5} then 3 else if T={1,3,5} then 1 else if T={6} then 3 else if T={2,3,6} then 1 else if T={4,5,6} then 1 else if T={7} then 3 else if T={1,4,7} then 1 else if T={0,2,5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={0,1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],2⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[12,14,16],1⟩,⟨[17],3⟩,⟨[13,14,17],1⟩,⟨[15,16,17],1⟩,⟨[18],3⟩,⟨[12,15,18],1⟩,⟨[11,13,16,18],1⟩,⟨[17,18],1⟩,⟨[19],3⟩,⟨[13,15,19],1⟩,⟨[16,19],1⟩,⟨[11,12,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1997
namespace Case1997
def big : Finset (Finset (Fin 9)) := {{1,3,5},{2,3,6},{4,5,6},{1,4,7},{0,2,5,7},{2,4,8},{0,1,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{0,4},{3,4},{1,3,5},{2,3,6},{4,5,6},{1,4,7},{0,2,5,7},{6,7},{2,4,8},{5,8},{0,1,6,8},{3,7,8}]
end Case1997
namespace Case1998
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{1,3},{4},{2,4},{5},{0,3,4,5},{6},{0,6},{1,2,5,6},{7},{0,1,7},{2,3,7},{5,7},{4,6,7},{8},{0,2,8},{1,4,8},{5,8},{3,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={5} then 3 else if T={0,3,4,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,2,5,6} then 1 else if T={7} then 2 else if T={0,1,7} then 1 else if T={2,3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,2,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[12,14],1⟩,⟨[15],3⟩,⟨[10,13,14,15],1⟩,⟨[16],3⟩,⟨[10,16],1⟩,⟨[11,12,15,16],1⟩,⟨[17],2⟩,⟨[10,11,17],1⟩,⟨[12,13,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],2⟩,⟨[10,12,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[13,16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1998
namespace Case1998
def big : Finset (Finset (Fin 9)) := {{0,3,4,5},{1,2,5,6},{0,1,7},{2,3,7},{4,6,7},{0,2,8},{1,4,8},{3,6,8}}
def full : List (Finset (Fin 9)) := [{1,3},{2,4},{0,3,4,5},{0,6},{1,2,5,6},{0,1,7},{2,3,7},{5,7},{4,6,7},{0,2,8},{1,4,8},{5,8},{3,6,8},{7,8}]
end Case1998
namespace Case1999
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{0,3},{4},{0,1,4},{5},{1,2,3,5},{4,5},{6},{2,6},{3,4,6},{7},{1,7},{2,4,7},{0,5,6,7},{8},{0,2,8},{4,8},{5,8},{1,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={0,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={5} then 3 else if T={1,2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={2,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 2 else if T={0,2,8} then 1 else if T={4,8} then 1 else if T={5,8} then 1 else if T={1,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,11,14],1⟩,⟨[15],3⟩,⟨[11,12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[12,14,17],1⟩,⟨[10,15,16,17],1⟩,⟨[18],2⟩,⟨[10,12,18],1⟩,⟨[14,18],1⟩,⟨[15,18],1⟩,⟨[11,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case1999
namespace Case1999
def big : Finset (Finset (Fin 9)) := {{0,1,4},{1,2,3,5},{3,4,6},{2,4,7},{0,5,6,7},{0,2,8},{1,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,1,4},{1,2,3,5},{4,5},{2,6},{3,4,6},{1,7},{2,4,7},{0,5,6,7},{0,2,8},{4,8},{5,8},{1,6,8},{3,7,8}]
end Case1999
namespace Case2000
def positionFn : Fin 9 → Fin 25 := ![16,17,18,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{4},{3,4},{5},{0,1,2,5},{3,5},{4,5},{6},{2,6},{0,3,6},{1,4,6},{7},{0,7},{1,3,7},{2,4,7},{8},{1,8},{2,3,8},{0,4,8},{5,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={4} then 1 else if T={3,4} then 1 else if T={5} then 3 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={2,6} then 1 else if T={0,3,6} then 1 else if T={1,4,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={1,3,7} then 1 else if T={2,4,7} then 1 else if T={8} then 3 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={0,4,8} then 1 else if T={5,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[17,18,19,20,21,22,23,24,25],[⟨[17],2⟩,⟨[18],2⟩,⟨[19],2⟩,⟨[20],1⟩,⟨[21],1⟩,⟨[20,21],1⟩,⟨[22],3⟩,⟨[17,18,19,22],1⟩,⟨[20,22],1⟩,⟨[21,22],1⟩,⟨[23],3⟩,⟨[19,23],1⟩,⟨[17,20,23],1⟩,⟨[18,21,23],1⟩,⟨[24],3⟩,⟨[17,24],1⟩,⟨[18,20,24],1⟩,⟨[19,21,24],1⟩,⟨[25],3⟩,⟨[18,25],1⟩,⟨[19,20,25],1⟩,⟨[17,21,25],1⟩,⟨[22,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2000
namespace Case2000
def big : Finset (Finset (Fin 9)) := {{0,1,2,5},{0,3,6},{1,4,6},{1,3,7},{2,4,7},{2,3,8},{0,4,8},{5,6,7,8}}
def full : List (Finset (Fin 9)) := [{3,4},{0,1,2,5},{3,5},{4,5},{2,6},{0,3,6},{1,4,6},{0,7},{1,3,7},{2,4,7},{1,8},{2,3,8},{0,4,8},{5,6,7,8}]
end Case2000
namespace Case2001
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{2,3},{4},{0,2,4},{1,3,4},{5},{4,5},{6},{0,6},{1,2,5,6},{7},{1,7},{0,3,5,7},{4,6,7},{8},{0,1,8},{4,8},{5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,2,4} then 1 else if T={1,3,4} then 1 else if T={5} then 3 else if T={4,5} then 1 else if T={6} then 3 else if T={0,6} then 1 else if T={1,2,5,6} then 1 else if T={7} then 3 else if T={1,7} then 1 else if T={0,3,5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 2 else if T={0,1,8} then 1 else if T={4,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[11],2⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,13,15],1⟩,⟨[12,14,15],1⟩,⟨[16],3⟩,⟨[15,16],1⟩,⟨[17],3⟩,⟨[11,17],1⟩,⟨[12,13,16,17],1⟩,⟨[18],3⟩,⟨[12,18],1⟩,⟨[11,14,16,18],1⟩,⟨[15,17,18],1⟩,⟨[19],2⟩,⟨[11,12,19],1⟩,⟨[15,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[13,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2001
namespace Case2001
def big : Finset (Finset (Fin 9)) := {{0,2,4},{1,3,4},{1,2,5,6},{0,3,5,7},{4,6,7},{0,1,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{2,3},{0,2,4},{1,3,4},{4,5},{0,6},{1,2,5,6},{1,7},{0,3,5,7},{4,6,7},{0,1,8},{4,8},{5,8},{3,6,8},{2,7,8}]
end Case2001
namespace Case2002
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{2,3},{4},{0,1,4},{5},{4,5},{6},{1,6},{2,4,6},{0,3,5,6},{7},{0,7},{3,4,7},{1,2,5,7},{8},{0,2,8},{1,3,8},{4,8},{5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={5} then 3 else if T={4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={2,4,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 3 else if T={0,7} then 1 else if T={3,4,7} then 1 else if T={1,2,5,7} then 1 else if T={8} then 2 else if T={0,2,8} then 1 else if T={1,3,8} then 1 else if T={4,8} then 1 else if T={5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,11,14],1⟩,⟨[15],3⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[12,14,16],1⟩,⟨[10,13,15,16],1⟩,⟨[17],3⟩,⟨[10,17],1⟩,⟨[13,14,17],1⟩,⟨[11,12,15,17],1⟩,⟨[18],2⟩,⟨[10,12,18],1⟩,⟨[11,13,18],1⟩,⟨[14,18],1⟩,⟨[15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2002
namespace Case2002
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,4,6},{0,3,5,6},{3,4,7},{1,2,5,7},{0,2,8},{1,3,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{2,3},{0,1,4},{4,5},{1,6},{2,4,6},{0,3,5,6},{0,7},{3,4,7},{1,2,5,7},{0,2,8},{1,3,8},{4,8},{5,8},{6,7,8}]
end Case2002
namespace Case2003
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{0,1,3},{4},{0,2,4},{3,4},{5},{3,5},{4,5},{6},{1,6},{2,3,6},{7},{2,7},{1,4,7},{0,5,6,7},{8},{0,8},{1,2,5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={3} then 1 else if T={0,1,3} then 1 else if T={4} then 1 else if T={0,2,4} then 1 else if T={3,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={7} then 3 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={0,5,6,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={1,2,5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[10,11,13],1⟩,⟨[14],1⟩,⟨[10,12,14],1⟩,⟨[13,14],1⟩,⟨[15],3⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[11,16],1⟩,⟨[12,13,16],1⟩,⟨[17],3⟩,⟨[12,17],1⟩,⟨[11,14,17],1⟩,⟨[10,15,16,17],1⟩,⟨[18],3⟩,⟨[10,18],1⟩,⟨[11,12,15,18],1⟩,⟨[14,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2003
namespace Case2003
def big : Finset (Finset (Fin 9)) := {{0,1,3},{0,2,4},{2,3,6},{1,4,7},{0,5,6,7},{1,2,5,8},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,3},{0,2,4},{3,4},{3,5},{4,5},{1,6},{2,3,6},{2,7},{1,4,7},{0,5,6,7},{0,8},{1,2,5,8},{4,6,8},{3,7,8}]
end Case2003
namespace Case2004
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{0,2},{3},{1,3},{4},{0,1,4},{5},{4,5},{6},{2,4,6},{0,3,5,6},{7},{3,4,7},{1,2,5,7},{6,7},{8},{2,3,8},{4,8},{5,8},{1,6,8},{0,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={0,2} then 1 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 1 else if T={0,1,4} then 1 else if T={5} then 3 else if T={4,5} then 1 else if T={6} then 3 else if T={2,4,6} then 1 else if T={0,3,5,6} then 1 else if T={7} then 3 else if T={3,4,7} then 1 else if T={1,2,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={2,3,8} then 1 else if T={4,8} then 1 else if T={5,8} then 1 else if T={1,6,8} then 1 else if T={0,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,11,14],1⟩,⟨[15],3⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[12,14,16],1⟩,⟨[10,13,15,16],1⟩,⟨[17],3⟩,⟨[13,14,17],1⟩,⟨[11,12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,13,18],1⟩,⟨[14,18],1⟩,⟨[15,18],1⟩,⟨[11,16,18],1⟩,⟨[10,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2004
namespace Case2004
def big : Finset (Finset (Fin 9)) := {{0,1,4},{2,4,6},{0,3,5,6},{3,4,7},{1,2,5,7},{2,3,8},{1,6,8},{0,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,3},{0,1,4},{4,5},{2,4,6},{0,3,5,6},{3,4,7},{1,2,5,7},{6,7},{2,3,8},{4,8},{5,8},{1,6,8},{0,7,8}]
end Case2004
namespace Case2005
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{1,2},{3},{0,1,3},{4},{3,4},{5},{3,5},{4,5},{6},{2,3,6},{0,4,6},{7},{1,4,7},{0,2,5,7},{6,7},{8},{0,8},{2,4,8},{1,5,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 2 else if T={1} then 2 else if T={2} then 2 else if T={1,2} then 1 else if T={3} then 1 else if T={0,1,3} then 1 else if T={4} then 1 else if T={3,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 3 else if T={2,3,6} then 1 else if T={0,4,6} then 1 else if T={7} then 3 else if T={1,4,7} then 1 else if T={0,2,5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={2,4,8} then 1 else if T={1,5,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[10],2⟩,⟨[11],2⟩,⟨[12],2⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[10,11,13],1⟩,⟨[14],1⟩,⟨[13,14],1⟩,⟨[15],3⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[12,13,16],1⟩,⟨[10,14,16],1⟩,⟨[17],3⟩,⟨[11,14,17],1⟩,⟨[10,12,15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[10,18],1⟩,⟨[12,14,18],1⟩,⟨[11,15,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2005
namespace Case2005
def big : Finset (Finset (Fin 9)) := {{0,1,3},{2,3,6},{0,4,6},{1,4,7},{0,2,5,7},{2,4,8},{1,5,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,1,3},{3,4},{3,5},{4,5},{2,3,6},{0,4,6},{1,4,7},{0,2,5,7},{6,7},{0,8},{2,4,8},{1,5,6,8},{3,7,8}]
end Case2005
namespace Case2006
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,3},{4},{0,1,2,4},{3,4},{5},{0,5},{2,5},{6},{0,6},{2,6},{4,6},{1,3,5,6},{7},{0,7},{1,7},{2,3,7},{4,7},{5,7},{8},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,1,2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={2,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={1,3,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,3,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[11,12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[12,14,16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,19],1⟩,⟨[14,19],1⟩,⟨[15,16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2006
namespace Case2006
def big : Finset (Finset (Fin 9)) := {{0,1,2,4},{1,3,5,6},{2,3,7},{4,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,1,2,4},{3,4},{0,5},{2,5},{0,6},{2,6},{4,6},{1,3,5,6},{0,7},{1,7},{2,3,7},{4,7},{5,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}]
end Case2006
namespace Case2007
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,1,2,3},{4},{0,4},{2,4},{3,4},{5},{0,5},{3,5},{6},{0,6},{2,6},{1,4,5,6},{7},{0,7},{1,7},{3,7},{2,5,7},{6,7},{8},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={0,1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,4,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[11,12,13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[12,15,16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[14,18],1⟩,⟨[13,16,18],1⟩,⟨[17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2007
namespace Case2007
def big : Finset (Finset (Fin 9)) := {{0,1,2,3},{1,4,5,6},{2,5,7},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2,3},{0,4},{2,4},{3,4},{0,5},{3,5},{0,6},{2,6},{1,4,5,6},{0,7},{1,7},{3,7},{2,5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
end Case2007
namespace Case2008
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,1,2,3},{0,4},{1,4},{3,4},{5},{0,5},{3,5},{2,4,5},{6},{0,6},{2,6},{4,6},{7},{0,7},{2,7},{3,7},{1,5,6,7},{8},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={0,1,2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={1,5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[11],2⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[10,11,12,13],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[13,15],1⟩,⟨[12,14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[11,15,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[15,18],1⟩,⟨[13,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2008
namespace Case2008
def big : Finset (Finset (Fin 9)) := {{0,1,2,3},{2,4,5},{1,5,6,7},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2,3},{0,4},{1,4},{3,4},{0,5},{3,5},{2,4,5},{0,6},{2,6},{4,6},{0,7},{2,7},{3,7},{1,5,6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
end Case2008
namespace Case2009
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,3},{4},{0,4},{2,4},{5},{0,1,2,5},{3,5},{6},{0,6},{2,6},{1,3,4,6},{5,6},{7},{0,7},{1,7},{2,3,7},{4,7},{5,7},{8},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,3,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[11],2⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[10,11,12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[11,13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,13,17],1⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[14,15,18],1⟩,⟨[16,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2009
namespace Case2009
def big : Finset (Finset (Fin 9)) := {{0,1,2,5},{1,3,4,6},{2,3,7},{4,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{2,4},{0,1,2,5},{3,5},{0,6},{2,6},{1,3,4,6},{5,6},{0,7},{1,7},{2,3,7},{4,7},{5,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}]
end Case2009
namespace Case2010
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,3},{4},{0,4},{2,4},{5},{0,1,2,5},{3,5},{4,5},{6},{0,6},{2,6},{1,3,4,6},{7},{0,7},{1,7},{2,3,7},{5,7},{6,7},{8},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,3,4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[11],2⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[10,11,12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[11,13,14,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[15,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2010
namespace Case2010
def big : Finset (Finset (Fin 9)) := {{0,1,2,5},{1,3,4,6},{2,3,7},{5,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{2,4},{0,1,2,5},{3,5},{4,5},{0,6},{2,6},{1,3,4,6},{0,7},{1,7},{2,3,7},{5,7},{6,7},{0,8},{1,8},{2,8},{3,8},{5,6,8},{4,7,8}]
end Case2010
namespace Case2011
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,3},{0,4},{1,4},{2,3,4},{5},{0,5},{2,5},{6},{0,1,2,6},{3,6},{4,6},{5,6},{7},{0,7},{2,7},{4,7},{1,3,5,7},{8},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={2,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={4,7} then 1 else if T={1,3,5,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[13,16],1⟩,⟨[17],2⟩,⟨[11,12,13,17],1⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,18],1⟩,⟨[15,18],1⟩,⟨[12,14,16,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,19],1⟩,⟨[14,19],1⟩,⟨[15,16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2011
namespace Case2011
def big : Finset (Finset (Fin 9)) := {{2,3,4},{0,1,2,6},{1,3,5,7},{4,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{1,4},{2,3,4},{0,5},{2,5},{0,1,2,6},{3,6},{4,6},{5,6},{0,7},{2,7},{4,7},{1,3,5,7},{0,8},{1,8},{2,8},{3,8},{4,5,8},{6,7,8}]
end Case2011
namespace Case2012
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,3},{0,4},{1,4},{2,4},{3,4},{5},{0,1,2,5},{3,5},{6},{0,6},{2,6},{4,5,6},{7},{0,7},{2,7},{5,7},{1,3,6,7},{8},{0,8},{1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={0,1,2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={4,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={1,3,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[11,12,13,16],1⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[15,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,18],1⟩,⟨[16,18],1⟩,⟨[12,14,17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,14,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2012
namespace Case2012
def big : Finset (Finset (Fin 9)) := {{0,1,2,5},{4,5,6},{1,3,6,7},{2,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{0,4},{1,4},{2,4},{3,4},{0,1,2,5},{3,5},{0,6},{2,6},{4,5,6},{0,7},{2,7},{5,7},{1,3,6,7},{0,8},{1,8},{2,3,8},{5,8},{6,8},{4,7,8}]
end Case2012
namespace Case2013
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,3},{2,3},{4},{0,4},{2,4},{5},{0,1,2,5},{4,5},{6},{0,6},{1,3,4,6},{5,6},{7},{0,7},{1,7},{3,7},{5,7},{2,6,7},{8},{0,8},{1,8},{2,8},{3,5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={0,1,2,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,3,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={2,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[11],2⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[10,11,12,15],1⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[11,13,14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[12,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2013
namespace Case2013
def big : Finset (Finset (Fin 9)) := {{0,1,2,5},{1,3,4,6},{2,6,7},{3,5,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{2,3},{0,4},{2,4},{0,1,2,5},{4,5},{0,6},{1,3,4,6},{5,6},{0,7},{1,7},{3,7},{5,7},{2,6,7},{0,8},{1,8},{2,8},{3,5,8},{6,8},{4,7,8}]
end Case2013
namespace Case2014
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{3},{0,3},{2,3},{0,4},{1,4},{3,4},{5},{0,5},{2,4,5},{6},{0,1,2,6},{4,6},{5,6},{7},{0,7},{2,7},{1,3,5,7},{6,7},{8},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 2 else if T={2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={2,4,5} then 1 else if T={6} then 2 else if T={0,1,2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,3,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[11],2⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[10,15],1⟩,⟨[12,14,15],1⟩,⟨[16],2⟩,⟨[10,11,12,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[11,13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[15,18],1⟩,⟨[13,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2014
namespace Case2014
def big : Finset (Finset (Fin 9)) := {{2,4,5},{0,1,2,6},{1,3,5,7},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{2,3},{0,4},{1,4},{3,4},{0,5},{2,4,5},{0,1,2,6},{4,6},{5,6},{0,7},{2,7},{1,3,5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
end Case2014
namespace Case2015
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{2},{0,2},{3},{2,3},{0,4},{1,4},{3,4},{5},{0,1,3,5},{2,4,5},{6},{0,6},{4,6},{5,6},{7},{0,7},{3,7},{5,7},{1,2,6,7},{8},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={1} then 2 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={3,4} then 1 else if T={5} then 2 else if T={0,1,3,5} then 1 else if T={2,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={1,2,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[11],2⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[10,11,13,15],1⟩,⟨[12,14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[11,12,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[15,18],1⟩,⟨[13,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case2015
namespace Case2015
def big : Finset (Finset (Fin 9)) := {{0,1,3,5},{2,4,5},{1,2,6,7},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{2,3},{0,4},{1,4},{3,4},{0,1,3,5},{2,4,5},{0,6},{4,6},{5,6},{0,7},{3,7},{5,7},{1,2,6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
end Case2015
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

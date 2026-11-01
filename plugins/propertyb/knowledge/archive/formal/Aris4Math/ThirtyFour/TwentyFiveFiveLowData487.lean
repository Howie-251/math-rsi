import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case11688
def positionFn : Fin 9 → Fin 25 := ![10,11,12,20,9,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{4},{0,1,2,3,4},{5},{0,5},{1,5},{2,5},{3,5},{6},{0,6},{1,6},{2,6},{3,6},{7},{0,7},{1,7},{2,7},{3,7},{8},{0,8},{1,8},{2,8},{3,8},{4,5,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={4} then 4 else if T={0,1,2,3,4} then 1 else if T={5} then 2 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={4,5,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,21,22,23,24,25],[⟨[11],1⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[21],1⟩,⟨[10],4⟩,⟨[10,11,12,13,21],1⟩,⟨[22],2⟩,⟨[11,22],1⟩,⟨[12,22],1⟩,⟨[13,22],1⟩,⟨[21,22],1⟩,⟨[23],2⟩,⟨[11,23],1⟩,⟨[12,23],1⟩,⟨[13,23],1⟩,⟨[21,23],1⟩,⟨[24],2⟩,⟨[11,24],1⟩,⟨[12,24],1⟩,⟨[13,24],1⟩,⟨[21,24],1⟩,⟨[25],2⟩,⟨[11,25],1⟩,⟨[12,25],1⟩,⟨[13,25],1⟩,⟨[21,25],1⟩,⟨[10,22,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11688
namespace Case11688
def big : Finset (Finset (Fin 9)) := {{0,1,2,3,4},{4,5,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2,3,4},{0,5},{1,5},{2,5},{3,5},{0,6},{1,6},{2,6},{3,6},{0,7},{1,7},{2,7},{3,7},{0,8},{1,8},{2,8},{3,8},{4,5,6,7,8}]
end Case11688
namespace Case11689
def positionFn : Fin 9 → Fin 25 := ![9,18,19,10,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{0,3},{1,3},{2,3},{4},{0,4},{1,4},{2,4},{5},{3,5},{4,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{0,7},{1,7},{2,7},{5,7},{8},{0,1,2,5,8},{3,4,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 2 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={8} then 5 else if T={0,1,2,5,8} then 1 else if T={3,4,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,19,20,21,22,23,24,25],[⟨[10],1⟩,⟨[19],1⟩,⟨[20],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[11,19],1⟩,⟨[11,20],1⟩,⟨[21],1⟩,⟨[10,21],1⟩,⟨[19,21],1⟩,⟨[20,21],1⟩,⟨[22],2⟩,⟨[11,22],1⟩,⟨[21,22],1⟩,⟨[23],2⟩,⟨[10,23],1⟩,⟨[19,23],1⟩,⟨[20,23],1⟩,⟨[22,23],1⟩,⟨[24],2⟩,⟨[10,24],1⟩,⟨[19,24],1⟩,⟨[20,24],1⟩,⟨[22,24],1⟩,⟨[25],5⟩,⟨[10,19,20,22,25],1⟩,⟨[11,21,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11689
namespace Case11689
def big : Finset (Finset (Fin 9)) := {{0,1,2,5,8},{3,4,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{3,5},{4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,7},{5,7},{0,1,2,5,8},{3,4,6,7,8}]
end Case11689
namespace Case11690
def positionFn : Fin 9 → Fin 25 := ![9,18,19,10,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{3},{0,3},{1,3},{2,3},{4},{5},{3,5},{0,1,2,4,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{0,7},{1,7},{2,7},{5,7},{8},{0,8},{1,8},{2,8},{5,8},{3,4,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 4 else if T={5} then 2 else if T={3,5} then 1 else if T={0,1,2,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={3,4,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,19,20,21,22,23,24,25],[⟨[10],1⟩,⟨[19],1⟩,⟨[20],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[11,19],1⟩,⟨[11,20],1⟩,⟨[21],4⟩,⟨[22],2⟩,⟨[11,22],1⟩,⟨[10,19,20,21,22],1⟩,⟨[23],2⟩,⟨[10,23],1⟩,⟨[19,23],1⟩,⟨[20,23],1⟩,⟨[22,23],1⟩,⟨[24],2⟩,⟨[10,24],1⟩,⟨[19,24],1⟩,⟨[20,24],1⟩,⟨[22,24],1⟩,⟨[25],2⟩,⟨[10,25],1⟩,⟨[19,25],1⟩,⟨[20,25],1⟩,⟨[22,25],1⟩,⟨[11,21,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11690
namespace Case11690
def big : Finset (Finset (Fin 9)) := {{0,1,2,4,5},{3,4,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{2,3},{3,5},{0,1,2,4,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,7},{5,7},{0,8},{1,8},{2,8},{5,8},{3,4,6,7,8}]
end Case11690
namespace Case11691
def positionFn : Fin 9 → Fin 25 := ![9,18,10,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [{0},{1},{2},{0,2},{1,2},{3},{0,3},{1,3},{4},{5},{2,5},{3,5},{6},{2,6},{3,6},{0,1,4,5,6},{7},{0,7},{1,7},{5,7},{6,7},{8},{0,8},{1,8},{5,8},{6,8},{2,3,4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 4 else if T={5} then 2 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={3,6} then 1 else if T={0,1,4,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={2,3,4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,19,20,21,22,23,24,25],[⟨[10],1⟩,⟨[19],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[11,19],1⟩,⟨[20],1⟩,⟨[10,20],1⟩,⟨[19,20],1⟩,⟨[21],4⟩,⟨[22],2⟩,⟨[11,22],1⟩,⟨[20,22],1⟩,⟨[23],2⟩,⟨[11,23],1⟩,⟨[20,23],1⟩,⟨[10,19,21,22,23],1⟩,⟨[24],2⟩,⟨[10,24],1⟩,⟨[19,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[25],2⟩,⟨[10,25],1⟩,⟨[19,25],1⟩,⟨[22,25],1⟩,⟨[23,25],1⟩,⟨[11,20,21,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11691
namespace Case11691
def big : Finset (Finset (Fin 9)) := {{0,1,4,5,6},{2,3,4,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{2,5},{3,5},{2,6},{3,6},{0,1,4,5,6},{0,7},{1,7},{5,7},{6,7},{0,8},{1,8},{5,8},{6,8},{2,3,4,7,8}]
end Case11691
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

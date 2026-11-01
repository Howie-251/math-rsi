import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case11640
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,2},{1,2},{3},{4},{0,4},{0,5},{2,5},{3,5},{1,4,5},{0,6},{1,6},{2,3,6},{4,6},{5,6},{0,7},{1,7},{2,7},{3,4,7},{5,7},{6,7},{8},{0,1,3,8},{2,4,8},{5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={0,4} then 1 else if T={0,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={1,4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,1,3,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],5⟩,⟨[11],1⟩,⟨[10,12],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[10,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[11,14,15],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,13,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[10,11,13,18],1⟩,⟨[12,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11640
namespace Case11640
def big : Finset (Finset (Fin 9)) := {{1,4,5},{2,3,6},{3,4,7},{0,1,3,8},{2,4,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,4},{0,5},{2,5},{3,5},{1,4,5},{0,6},{1,6},{2,3,6},{4,6},{5,6},{0,7},{1,7},{2,7},{3,4,7},{5,7},{6,7},{0,1,3,8},{2,4,8},{5,8},{6,8},{7,8}]
end Case11640
namespace Case11641
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{1},{0,2},{3},{4},{0,4},{1,2,4},{0,5},{1,5},{2,3,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{8},{2,8},{0,1,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={1} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={0,4} then 1 else if T={1,2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={2,8} then 1 else if T={0,1,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],5⟩,⟨[11],1⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,12,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,13,15],1⟩,⟨[14,15],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[10,11,13,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11641
namespace Case11641
def big : Finset (Finset (Fin 9)) := {{1,2,4},{2,3,5},{3,4,6},{0,1,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,4},{1,2,4},{0,5},{1,5},{2,3,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{2,8},{0,1,3,8},{5,8},{6,8},{4,7,8}]
end Case11641
namespace Case11642
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{4},{0,2,4},{5},{2,5},{0,1,3,5},{4,5},{0,6},{2,6},{3,6},{1,4,6},{5,6},{0,7},{1,7},{2,3,7},{4,7},{5,7},{6,7},{0,8},{1,8},{2,8},{3,4,8},{5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={0,2,4} then 1 else if T={5} then 1 else if T={2,5} then 1 else if T={0,1,3,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={1,4,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,3,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],5⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[10,12,14],1⟩,⟨[15],1⟩,⟨[12,15],1⟩,⟨[10,11,13,15],1⟩,⟨[14,15],1⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[11,14,16],1⟩,⟨[15,16],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,13,17],1⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11642
namespace Case11642
def big : Finset (Finset (Fin 9)) := {{0,2,4},{0,1,3,5},{1,4,6},{2,3,7},{3,4,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,2,4},{2,5},{0,1,3,5},{4,5},{0,6},{2,6},{3,6},{1,4,6},{5,6},{0,7},{1,7},{2,3,7},{4,7},{5,7},{6,7},{0,8},{1,8},{2,8},{3,4,8},{5,8},{6,8},{7,8}]
end Case11642
namespace Case11643
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{2},{3},{0,1,2,3},{4},{0,4},{1,4},{0,5},{1,5},{3,5},{2,4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{0,8},{1,8},{2,8},{3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={2} then 1 else if T={3} then 1 else if T={0,1,2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={2,4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],6⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[10,11,12,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[13,15],1⟩,⟨[12,14,15],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[15,16],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11643
namespace Case11643
def big : Finset (Finset (Fin 9)) := {{0,1,2,3},{2,4,5},{3,4,6},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2,3},{0,4},{1,4},{0,5},{1,5},{3,5},{2,4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{0,8},{1,8},{2,8},{3,8},{5,8},{6,8},{4,7,8}]
end Case11643
namespace Case11644
def positionFn : Fin 9 → Fin 25 := ![11,19,12,20,13,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{5},{0,5},{1,5},{2,5},{3,5},{6},{4,6},{5,6},{7},{2,7},{3,7},{0,1,6,7},{8},{0,8},{1,8},{2,3,6,8},{4,5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 3 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={2,7} then 1 else if T={3,7} then 1 else if T={0,1,6,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,6,8} then 1 else if T={4,5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,13,14,20,21,22,23,24,25],[⟨[],3⟩,⟨[12,13],1⟩,⟨[13,20],1⟩,⟨[12,21],1⟩,⟨[20,21],1⟩,⟨[12,14],1⟩,⟨[14,20],1⟩,⟨[13,14],1⟩,⟨[14,21],1⟩,⟨[22],1⟩,⟨[12,22],1⟩,⟨[20,22],1⟩,⟨[13,22],1⟩,⟨[21,22],1⟩,⟨[23],3⟩,⟨[14,23],1⟩,⟨[22,23],1⟩,⟨[24],3⟩,⟨[13,24],1⟩,⟨[21,24],1⟩,⟨[12,20,23,24],1⟩,⟨[25],3⟩,⟨[12,25],1⟩,⟨[20,25],1⟩,⟨[13,21,23,25],1⟩,⟨[14,22,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11644
namespace Case11644
def big : Finset (Finset (Fin 9)) := {{0,1,6,7},{2,3,6,8},{4,5,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{2,4},{3,4},{0,5},{1,5},{2,5},{3,5},{4,6},{5,6},{2,7},{3,7},{0,1,6,7},{0,8},{1,8},{2,3,6,8},{4,5,7,8}]
end Case11644
namespace Case11645
def positionFn : Fin 9 → Fin 25 := ![10,13,20,21,11,22,23,12,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{4},{5},{0,5},{1,5},{2,5},{3,5},{4,5},{6},{0,6},{1,6},{2,6},{3,6},{4,6},{7},{2,7},{3,7},{0,1,4,7},{8},{0,8},{1,8},{2,3,4,8},{5,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={7} then 3 else if T={2,7} then 1 else if T={3,7} then 1 else if T={0,1,4,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,4,8} then 1 else if T={5,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,21,22,23,24,25],[⟨[],3⟩,⟨[11,21],1⟩,⟨[14,21],1⟩,⟨[11,22],1⟩,⟨[14,22],1⟩,⟨[12],2⟩,⟨[23],1⟩,⟨[11,23],1⟩,⟨[14,23],1⟩,⟨[21,23],1⟩,⟨[22,23],1⟩,⟨[12,23],1⟩,⟨[24],1⟩,⟨[11,24],1⟩,⟨[14,24],1⟩,⟨[21,24],1⟩,⟨[22,24],1⟩,⟨[12,24],1⟩,⟨[13],3⟩,⟨[13,21],1⟩,⟨[13,22],1⟩,⟨[11,12,13,14],1⟩,⟨[25],3⟩,⟨[11,25],1⟩,⟨[14,25],1⟩,⟨[12,21,22,25],1⟩,⟨[13,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11645
namespace Case11645
def big : Finset (Finset (Fin 9)) := {{0,1,4,7},{2,3,4,8},{5,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{0,5},{1,5},{2,5},{3,5},{4,5},{0,6},{1,6},{2,6},{3,6},{4,6},{2,7},{3,7},{0,1,4,7},{0,8},{1,8},{2,3,4,8},{5,6,7,8}]
end Case11645
namespace Case11646
def positionFn : Fin 9 → Fin 25 := ![10,12,11,20,13,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{4},{2,4},{3,4},{5},{0,5},{1,5},{2,5},{3,5},{6},{0,6},{1,6},{2,6},{3,6},{7},{0,1,4,7},{5,7},{6,7},{8},{0,8},{1,8},{4,5,6,8},{2,3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={7} then 3 else if T={0,1,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={1,8} then 1 else if T={4,5,6,8} then 1 else if T={2,3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,21,22,23,24,25],[⟨[],3⟩,⟨[11,12],1⟩,⟨[12,13],1⟩,⟨[11,21],1⟩,⟨[13,21],1⟩,⟨[14],2⟩,⟨[12,14],1⟩,⟨[14,21],1⟩,⟨[22],1⟩,⟨[11,22],1⟩,⟨[13,22],1⟩,⟨[12,22],1⟩,⟨[21,22],1⟩,⟨[23],1⟩,⟨[11,23],1⟩,⟨[13,23],1⟩,⟨[12,23],1⟩,⟨[21,23],1⟩,⟨[24],3⟩,⟨[11,13,14,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[25],3⟩,⟨[11,25],1⟩,⟨[13,25],1⟩,⟨[14,22,23,25],1⟩,⟨[12,21,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11646
namespace Case11646
def big : Finset (Finset (Fin 9)) := {{0,1,4,7},{4,5,6,8},{2,3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{2,4},{3,4},{0,5},{1,5},{2,5},{3,5},{0,6},{1,6},{2,6},{3,6},{0,1,4,7},{5,7},{6,7},{0,8},{1,8},{4,5,6,8},{2,3,7,8}]
end Case11646
namespace Case11647
def positionFn : Fin 9 → Fin 25 := ![10,12,20,11,13,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{2,3},{4},{3,4},{5},{0,5},{1,5},{3,5},{6},{0,6},{1,6},{2,6},{4,6},{5,6},{7},{2,7},{0,1,4,7},{5,7},{8},{0,8},{1,8},{2,4,5,8},{3,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={2,7} then 1 else if T={0,1,4,7} then 1 else if T={5,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,5,8} then 1 else if T={3,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,21,22,23,24,25],[⟨[],3⟩,⟨[11,21],1⟩,⟨[13,21],1⟩,⟨[11,12],1⟩,⟨[12,13],1⟩,⟨[12,21],1⟩,⟨[14],2⟩,⟨[12,14],1⟩,⟨[22],1⟩,⟨[11,22],1⟩,⟨[13,22],1⟩,⟨[12,22],1⟩,⟨[23],1⟩,⟨[11,23],1⟩,⟨[13,23],1⟩,⟨[21,23],1⟩,⟨[14,23],1⟩,⟨[22,23],1⟩,⟨[24],3⟩,⟨[21,24],1⟩,⟨[11,13,14,24],1⟩,⟨[22,24],1⟩,⟨[25],3⟩,⟨[11,25],1⟩,⟨[13,25],1⟩,⟨[14,21,22,25],1⟩,⟨[12,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11647
namespace Case11647
def big : Finset (Finset (Fin 9)) := {{0,1,4,7},{2,4,5,8},{3,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{2,3},{3,4},{0,5},{1,5},{3,5},{0,6},{1,6},{2,6},{4,6},{5,6},{2,7},{0,1,4,7},{5,7},{0,8},{1,8},{2,4,5,8},{3,6,7,8}]
end Case11647
namespace Case11648
def positionFn : Fin 9 → Fin 25 := ![11,19,12,13,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{2,3},{4},{0,4},{1,4},{5},{0,5},{1,5},{3,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{3,7},{2,4,5,7},{6,7},{8},{2,8},{5,8},{3,4,6,8},{0,1,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={3,7} then 1 else if T={2,4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={2,8} then 1 else if T={5,8} then 1 else if T={3,4,6,8} then 1 else if T={0,1,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,13,14,20,21,22,23,24,25],[⟨[],3⟩,⟨[12,13],1⟩,⟨[13,20],1⟩,⟨[12,14],1⟩,⟨[14,20],1⟩,⟨[13,14],1⟩,⟨[21],2⟩,⟨[12,21],1⟩,⟨[20,21],1⟩,⟨[22],1⟩,⟨[12,22],1⟩,⟨[20,22],1⟩,⟨[14,22],1⟩,⟨[23],1⟩,⟨[12,23],1⟩,⟨[20,23],1⟩,⟨[13,23],1⟩,⟨[22,23],1⟩,⟨[24],3⟩,⟨[14,24],1⟩,⟨[13,21,22,24],1⟩,⟨[23,24],1⟩,⟨[25],3⟩,⟨[13,25],1⟩,⟨[22,25],1⟩,⟨[14,21,23,25],1⟩,⟨[12,20,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11648
namespace Case11648
def big : Finset (Finset (Fin 9)) := {{2,4,5,7},{3,4,6,8},{0,1,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{2,3},{0,4},{1,4},{0,5},{1,5},{3,5},{0,6},{1,6},{2,6},{5,6},{3,7},{2,4,5,7},{6,7},{2,8},{5,8},{3,4,6,8},{0,1,7,8}]
end Case11648
namespace Case11649
def positionFn : Fin 9 → Fin 25 := ![10,14,20,11,12,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{3},{4},{2,4},{0,1,3,4},{5},{0,5},{1,5},{4,5},{6},{0,6},{1,6},{2,6},{3,6},{5,6},{7},{0,7},{1,7},{2,7},{3,7},{5,7},{8},{0,8},{1,8},{2,3,5,8},{4,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={2,4} then 1 else if T={0,1,3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,5,8} then 1 else if T={4,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,15,21,22,23,24,25],[⟨[],3⟩,⟨[11,21],1⟩,⟨[15,21],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[13,21],1⟩,⟨[11,12,13,15],1⟩,⟨[22],1⟩,⟨[11,22],1⟩,⟨[15,22],1⟩,⟨[13,22],1⟩,⟨[23],1⟩,⟨[11,23],1⟩,⟨[15,23],1⟩,⟨[21,23],1⟩,⟨[12,23],1⟩,⟨[22,23],1⟩,⟨[24],1⟩,⟨[11,24],1⟩,⟨[15,24],1⟩,⟨[21,24],1⟩,⟨[12,24],1⟩,⟨[22,24],1⟩,⟨[25],3⟩,⟨[11,25],1⟩,⟨[15,25],1⟩,⟨[12,21,22,25],1⟩,⟨[13,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11649
namespace Case11649
def big : Finset (Finset (Fin 9)) := {{0,1,3,4},{2,3,5,8},{4,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{2,4},{0,1,3,4},{0,5},{1,5},{4,5},{0,6},{1,6},{2,6},{3,6},{5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{0,8},{1,8},{2,3,5,8},{4,6,7,8}]
end Case11649
namespace Case11650
def positionFn : Fin 9 → Fin 25 := ![13,14,10,11,12,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{3},{4},{0,4},{1,4},{5},{0,5},{1,5},{2,3,4,5},{6},{0,6},{1,6},{2,6},{3,6},{5,6},{7},{0,7},{1,7},{2,7},{3,7},{5,7},{8},{2,8},{0,1,3,8},{5,8},{4,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,3,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={8} then 3 else if T={2,8} then 1 else if T={0,1,3,8} then 1 else if T={5,8} then 1 else if T={4,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,22,23,24,25],[⟨[],3⟩,⟨[11,14],1⟩,⟨[11,15],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[13,14],1⟩,⟨[13,15],1⟩,⟨[22],1⟩,⟨[14,22],1⟩,⟨[15,22],1⟩,⟨[11,12,13,22],1⟩,⟨[23],1⟩,⟨[14,23],1⟩,⟨[15,23],1⟩,⟨[11,23],1⟩,⟨[12,23],1⟩,⟨[22,23],1⟩,⟨[24],1⟩,⟨[14,24],1⟩,⟨[15,24],1⟩,⟨[11,24],1⟩,⟨[12,24],1⟩,⟨[22,24],1⟩,⟨[25],3⟩,⟨[11,25],1⟩,⟨[12,14,15,25],1⟩,⟨[22,25],1⟩,⟨[13,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11650
namespace Case11650
def big : Finset (Finset (Fin 9)) := {{2,3,4,5},{0,1,3,8},{4,6,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,4},{1,4},{0,5},{1,5},{2,3,4,5},{0,6},{1,6},{2,6},{3,6},{5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{2,8},{0,1,3,8},{5,8},{4,6,7,8}]
end Case11650
namespace Case11651
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{3},{2,3},{4},{0,4},{1,4},{5},{0,5},{1,5},{3,5},{6},{0,6},{1,6},{2,6},{5,6},{7},{0,7},{1,7},{2,7},{5,7},{3,4,6,7},{8},{0,1,3,8},{2,4,5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={3,4,6,7} then 1 else if T={8} then 3 else if T={0,1,3,8} then 1 else if T={2,4,5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[16,18],1⟩,⟨[14,15,17,18],1⟩,⟨[19],3⟩,⟨[11,12,14,19],1⟩,⟨[13,15,16,19],1⟩,⟨[17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11651
namespace Case11651
def big : Finset (Finset (Fin 9)) := {{3,4,6,7},{0,1,3,8},{2,4,5,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{2,3},{0,4},{1,4},{0,5},{1,5},{3,5},{0,6},{1,6},{2,6},{5,6},{0,7},{1,7},{2,7},{5,7},{3,4,6,7},{0,1,3,8},{2,4,5,8},{6,8},{7,8}]
end Case11651
namespace Case11652
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{2},{3},{0,1,2,3},{4},{0,4},{1,4},{5},{0,5},{1,5},{3,5},{6},{0,6},{1,6},{3,6},{2,4,5,6},{7},{0,7},{1,7},{2,7},{5,7},{6,7},{8},{0,8},{1,8},{2,8},{5,8},{6,8},{3,4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={2} then 2 else if T={3} then 2 else if T={0,1,2,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={3,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={2,4,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[13],2⟩,⟨[14],2⟩,⟨[11,12,13,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[14,17],1⟩,⟨[13,15,16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[14,15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11652
namespace Case11652
def big : Finset (Finset (Fin 9)) := {{0,1,2,3},{2,4,5,6},{3,4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1,2,3},{0,4},{1,4},{0,5},{1,5},{3,5},{0,6},{1,6},{3,6},{2,4,5,6},{0,7},{1,7},{2,7},{5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{6,8},{3,4,7,8}]
end Case11652
namespace Case11653
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{0,2},{1,2},{3},{2,3},{4},{1,4},{5},{1,5},{2,5},{0,3,4,5},{6},{0,6},{2,6},{4,6},{5,6},{7},{0,7},{1,7},{3,7},{5,7},{6,7},{8},{0,8},{5,8},{1,3,6,8},{2,4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={2,3} then 1 else if T={4} then 2 else if T={1,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={0,3,4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={0,8} then 1 else if T={5,8} then 1 else if T={1,3,6,8} then 1 else if T={2,4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],3⟩,⟨[11,12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[12,15],1⟩,⟨[16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[11,14,15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[14,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],3⟩,⟨[11,19],1⟩,⟨[16,19],1⟩,⟨[12,14,17,19],1⟩,⟨[13,15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11653
namespace Case11653
def big : Finset (Finset (Fin 9)) := {{0,3,4,5},{1,3,6,8},{2,4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{1,2},{2,3},{1,4},{1,5},{2,5},{0,3,4,5},{0,6},{2,6},{4,6},{5,6},{0,7},{1,7},{3,7},{5,7},{6,7},{0,8},{5,8},{1,3,6,8},{2,4,7,8}]
end Case11653
namespace Case11654
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,1},{2},{3},{1,3},{4},{0,4},{5},{1,5},{0,2,3,5},{4,5},{6},{0,6},{3,6},{1,2,4,6},{5,6},{7},{0,7},{1,7},{2,7},{5,7},{6,7},{8},{0,8},{1,8},{2,8},{5,8},{6,8},{3,4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 3 else if T={0,1} then 1 else if T={2} then 2 else if T={3} then 2 else if T={1,3} then 1 else if T={4} then 2 else if T={0,4} then 1 else if T={5} then 1 else if T={1,5} then 1 else if T={0,2,3,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={3,6} then 1 else if T={1,2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],3⟩,⟨[10,11],1⟩,⟨[12],2⟩,⟨[13],2⟩,⟨[11,13],1⟩,⟨[14],2⟩,⟨[10,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[10,12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[10,16],1⟩,⟨[13,16],1⟩,⟨[11,12,14,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[13,14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11654
namespace Case11654
def big : Finset (Finset (Fin 9)) := {{0,2,3,5},{1,2,4,6},{3,4,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,3},{0,4},{1,5},{0,2,3,5},{4,5},{0,6},{3,6},{1,2,4,6},{5,6},{0,7},{1,7},{2,7},{5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{6,8},{3,4,7,8}]
end Case11654
namespace Case11655
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,4,5},{0,6},{1,6},{2,6},{4,6},{5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{8},{0,1,2,8},{5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={0,1,2,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],6⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,14,15],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[10,11,12,18],1⟩,⟨[15,18],1⟩,⟨[13,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11655
namespace Case11655
def big : Finset (Finset (Fin 9)) := {{3,4,5},{0,1,2,8},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{3,4,5},{0,6},{1,6},{2,6},{4,6},{5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{0,1,2,8},{5,8},{3,6,8},{4,7,8}]
end Case11655
namespace Case11656
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,3},{1,3},{2,3},{4},{0,1,2,4},{0,5},{1,5},{2,5},{3,4,5},{0,6},{1,6},{2,6},{4,6},{5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{8},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,1,2,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],6⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[11,12,13,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,15,16],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[14,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,19],1⟩,⟨[16,19],1⟩,⟨[14,17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11656
namespace Case11656
def big : Finset (Finset (Fin 9)) := {{0,1,2,4},{3,4,5},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{2,3},{0,1,2,4},{0,5},{1,5},{2,5},{3,4,5},{0,6},{1,6},{2,6},{4,6},{5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
end Case11656
namespace Case11657
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{0,3},{1,3},{4},{5},{2,5},{3,5},{0,1,4,5},{0,6},{1,6},{2,3,6},{4,6},{5,6},{0,7},{1,7},{3,7},{2,4,7},{5,7},{6,7},{0,8},{1,8},{2,8},{3,4,8},{5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 6 else if T={0,2} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,1,4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],6⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[11,12,15,16],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,19],1⟩,⟨[14,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11657
namespace Case11657
def big : Finset (Finset (Fin 9)) := {{0,1,4,5},{2,3,6},{2,4,7},{3,4,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{2,5},{3,5},{0,1,4,5},{0,6},{1,6},{2,3,6},{4,6},{5,6},{0,7},{1,7},{3,7},{2,4,7},{5,7},{6,7},{0,8},{1,8},{2,8},{3,4,8},{5,8},{6,8},{7,8}]
end Case11657
namespace Case11658
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{3},{4},{0,4},{1,4},{0,5},{1,5},{2,5},{3,5},{0,6},{1,6},{2,6},{3,6},{4,6},{5,6},{7},{0,7},{1,7},{2,3,4,7},{5,7},{8},{2,8},{0,1,3,8},{4,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,3,4,7} then 1 else if T={5,7} then 1 else if T={8} then 3 else if T={2,8} then 1 else if T={0,1,3,8} then 1 else if T={4,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,14,15,18],1⟩,⟨[16,18],1⟩,⟨[19],3⟩,⟨[13,19],1⟩,⟨[11,12,14,19],1⟩,⟨[15,16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11658
namespace Case11658
def big : Finset (Finset (Fin 9)) := {{2,3,4,7},{0,1,3,8},{4,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,4},{1,4},{0,5},{1,5},{2,5},{3,5},{0,6},{1,6},{2,6},{3,6},{4,6},{5,6},{0,7},{1,7},{2,3,4,7},{5,7},{2,8},{0,1,3,8},{4,5,8},{6,7,8}]
end Case11658
namespace Case11659
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{3},{4},{2,4},{0,1,3,4},{0,5},{1,5},{2,5},{3,5},{0,6},{1,6},{2,6},{3,6},{5,6},{7},{0,7},{1,7},{4,5,7},{6,7},{8},{0,8},{1,8},{5,8},{4,6,8},{2,3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={2,4} then 1 else if T={0,1,3,4} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={2,3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[15],2⟩,⟨[13,15],1⟩,⟨[11,12,14,15],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[14,16],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[15,16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[16,19],1⟩,⟨[15,17,19],1⟩,⟨[13,14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11659
namespace Case11659
def big : Finset (Finset (Fin 9)) := {{0,1,3,4},{4,5,7},{4,6,8},{2,3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{2,4},{0,1,3,4},{0,5},{1,5},{2,5},{3,5},{0,6},{1,6},{2,6},{3,6},{5,6},{0,7},{1,7},{4,5,7},{6,7},{0,8},{1,8},{5,8},{4,6,8},{2,3,7,8}]
end Case11659
namespace Case11660
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{3},{0,3},{1,3},{4},{0,4},{1,4},{5},{2,3,4,5},{0,6},{1,6},{2,6},{4,6},{5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{8},{2,8},{0,1,5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 3 else if T={2,3,4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={2,8} then 1 else if T={0,1,5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[16],3⟩,⟨[13,14,15,16],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[14,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],3⟩,⟨[13,19],1⟩,⟨[11,12,16,19],1⟩,⟨[14,17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11660
namespace Case11660
def big : Finset (Finset (Fin 9)) := {{2,3,4,5},{0,1,5,8},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{0,4},{1,4},{2,3,4,5},{0,6},{1,6},{2,6},{4,6},{5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{2,8},{0,1,5,8},{3,6,8},{4,7,8}]
end Case11660
namespace Case11661
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,2},{1,2},{3},{0,3},{1,3},{4},{2,4},{5},{0,1,4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{8},{0,8},{1,8},{2,3,5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={2,4} then 1 else if T={5} then 3 else if T={0,1,4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[13,15],1⟩,⟨[16],3⟩,⟨[11,12,15,16],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[14,15,17],1⟩,⟨[16,17],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[14,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,14,16,19],1⟩,⟨[17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11661
namespace Case11661
def big : Finset (Finset (Fin 9)) := {{0,1,4,5},{3,4,6},{2,3,5,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{2,4},{0,1,4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{0,8},{1,8},{2,3,5,8},{6,8},{4,7,8}]
end Case11661
namespace Case11662
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{2},{3},{0,3},{1,3},{4},{0,4},{1,4},{5},{0,5},{1,5},{2,3,4,5},{0,6},{1,6},{2,6},{4,6},{5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{8},{0,1,2,8},{5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,3,4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={0,1,2,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],4⟩,⟨[12],2⟩,⟨[13],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[14],1⟩,⟨[10,14],1⟩,⟨[11,14],1⟩,⟨[15],1⟩,⟨[10,15],1⟩,⟨[11,15],1⟩,⟨[12,13,14,15],1⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[14,16],1⟩,⟨[15,16],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[10,11,12,18],1⟩,⟨[15,18],1⟩,⟨[13,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11662
namespace Case11662
def big : Finset (Finset (Fin 9)) := {{2,3,4,5},{0,1,2,8},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{0,4},{1,4},{0,5},{1,5},{2,3,4,5},{0,6},{1,6},{2,6},{4,6},{5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{0,1,2,8},{5,8},{3,6,8},{4,7,8}]
end Case11662
namespace Case11663
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{2},{3},{0,3},{1,3},{4},{0,1,2,4},{5},{0,5},{1,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{8},{0,8},{1,8},{2,3,5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 4 else if T={2} then 2 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={0,1,2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={4,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,3,5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],4⟩,⟨[13],2⟩,⟨[14],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[15],2⟩,⟨[11,12,13,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[15,16],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[14,15,17],1⟩,⟨[16,17],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[14,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,14,16,19],1⟩,⟨[17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11663
namespace Case11663
def big : Finset (Finset (Fin 9)) := {{0,1,2,4},{3,4,6},{2,3,5,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{0,1,2,4},{0,5},{1,5},{4,5},{0,6},{1,6},{2,6},{3,4,6},{5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{0,8},{1,8},{2,3,5,8},{6,8},{4,7,8}]
end Case11663
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

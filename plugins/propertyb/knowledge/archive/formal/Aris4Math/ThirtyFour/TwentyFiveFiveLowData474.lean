import Aris4Math.ThirtyFour.CachedSparseApplication
import Aris4Math.ThirtyFour.TwentyFiveColoredColoring
namespace Aris4Math.ThirtyFour.TwentyFiveFiveLow
open Aris4Math.ThirtyThree.MultiLockRecovery Aris4Math.K6Classification
open LocalProfiles CachedRows TwentyFiveUnitCounts TwentyFiveColoredActual
open TwentyFiveColoredColoring
open scoped BigOperators
set_option maxRecDepth 100000
set_option maxHeartbeats 0
namespace Case11376
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{0,3},{1,3},{2,3},{4},{1,2,4},{5},{2,5},{3,4,5},{6},{1,6},{3,6},{5,6},{7},{1,7},{2,7},{5,7},{0,4,6,7},{8},{4,8},{0,1,5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 2 else if T={1} then 1 else if T={0,2} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={1,2,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={3,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={3,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={0,4,6,7} then 1 else if T={8} then 3 else if T={4,8} then 1 else if T={0,1,5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],2⟩,⟨[12],1⟩,⟨[11,13],1⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[12,13,15],1⟩,⟨[16],2⟩,⟨[13,16],1⟩,⟨[14,15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[14,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[16,18],1⟩,⟨[11,15,17,18],1⟩,⟨[19],3⟩,⟨[15,19],1⟩,⟨[11,12,16,19],1⟩,⟨[13,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11376
namespace Case11376
def big : Finset (Finset (Fin 9)) := {{1,2,4},{3,4,5},{0,4,6,7},{0,1,5,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{0,3},{1,3},{2,3},{1,2,4},{2,5},{3,4,5},{1,6},{3,6},{5,6},{1,7},{2,7},{5,7},{0,4,6,7},{4,8},{0,1,5,8},{2,6,8},{3,7,8}]
end Case11376
namespace Case11377
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{3},{1,2,3},{4},{3,4},{5},{1,5},{2,4,5},{6},{2,6},{0,1,4,6},{5,6},{7},{1,7},{2,7},{0,3,5,7},{6,7},{8},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 2 else if T={1} then 1 else if T={0,2} then 1 else if T={3} then 2 else if T={1,2,3} then 1 else if T={4} then 2 else if T={3,4} then 1 else if T={5} then 2 else if T={1,5} then 1 else if T={2,4,5} then 1 else if T={6} then 2 else if T={2,6} then 1 else if T={0,1,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={0,3,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={3,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],2⟩,⟨[11],1⟩,⟨[10,12],1⟩,⟨[13],2⟩,⟨[11,12,13],1⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[11,15],1⟩,⟨[12,14,15],1⟩,⟨[16],2⟩,⟨[12,16],1⟩,⟨[10,11,14,16],1⟩,⟨[15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[10,13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[15,18],1⟩,⟨[13,16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11377
namespace Case11377
def big : Finset (Finset (Fin 9)) := {{1,2,3},{2,4,5},{0,1,4,6},{0,3,5,7},{3,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2,3},{3,4},{1,5},{2,4,5},{2,6},{0,1,4,6},{5,6},{1,7},{2,7},{0,3,5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{3,6,8},{4,7,8}]
end Case11377
namespace Case11378
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,2},{1,2},{3},{4},{3,4},{5},{2,3,5},{0,1,4,5},{6},{1,6},{2,4,6},{5,6},{7},{1,7},{2,7},{5,7},{0,3,6,7},{8},{0,8},{2,8},{1,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 2 else if T={1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={3,4} then 1 else if T={5} then 2 else if T={2,3,5} then 1 else if T={0,1,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={5,7} then 1 else if T={0,3,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],2⟩,⟨[12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[15],2⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[13,14,16],1⟩,⟨[11,12,15,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[13,15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[16,18],1⟩,⟨[11,14,17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[13,19],1⟩,⟨[12,14,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11378
namespace Case11378
def big : Finset (Finset (Fin 9)) := {{2,3,5},{0,1,4,5},{2,4,6},{0,3,6,7},{1,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{3,4},{2,3,5},{0,1,4,5},{1,6},{2,4,6},{5,6},{1,7},{2,7},{5,7},{0,3,6,7},{0,8},{2,8},{1,3,8},{5,8},{6,8},{4,7,8}]
end Case11378
namespace Case11379
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,1},{0,2},{1,2},{3},{4},{3,4},{5},{2,5},{1,3,5},{6},{1,6},{2,3,6},{0,4,5,6},{7},{2,7},{1,4,7},{5,7},{6,7},{8},{1,8},{2,4,8},{5,8},{6,8},{0,3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 2 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={3,4} then 1 else if T={5} then 2 else if T={2,5} then 1 else if T={1,3,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={0,4,5,6} then 1 else if T={7} then 2 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={0,3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],2⟩,⟨[11,12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[15],2⟩,⟨[14,15],1⟩,⟨[16],2⟩,⟨[13,16],1⟩,⟨[12,14,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[11,15,16,17],1⟩,⟨[18],2⟩,⟨[13,18],1⟩,⟨[12,15,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[12,19],1⟩,⟨[13,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[11,14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11379
namespace Case11379
def big : Finset (Finset (Fin 9)) := {{1,3,5},{2,3,6},{0,4,5,6},{1,4,7},{2,4,8},{0,3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{1,2},{3,4},{2,5},{1,3,5},{1,6},{2,3,6},{0,4,5,6},{2,7},{1,4,7},{5,7},{6,7},{1,8},{2,4,8},{5,8},{6,8},{0,3,7,8}]
end Case11379
namespace Case11380
def positionFn : Fin 9 → Fin 25 := ![12,13,19,20,11,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{0,2},{3},{1,3},{2,3},{2,4},{3,4},{5},{4,5},{6},{0,6},{1,6},{4,6},{5,6},{7},{0,4,7},{1,2,5,7},{3,6,7},{8},{1,4,8},{0,3,5,8},{2,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 3 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 3 else if T={0,4,7} then 1 else if T={1,2,5,7} then 1 else if T={3,6,7} then 1 else if T={8} then 3 else if T={1,4,8} then 1 else if T={0,3,5,8} then 1 else if T={2,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,13,14,20,21,22,23,24,25],[⟨[],2⟩,⟨[13],1⟩,⟨[14],1⟩,⟨[13,14],1⟩,⟨[20],1⟩,⟨[13,20],1⟩,⟨[21],1⟩,⟨[14,21],1⟩,⟨[20,21],1⟩,⟨[12,20],1⟩,⟨[12,21],1⟩,⟨[22],3⟩,⟨[12,22],1⟩,⟨[23],1⟩,⟨[13,23],1⟩,⟨[14,23],1⟩,⟨[12,23],1⟩,⟨[22,23],1⟩,⟨[24],3⟩,⟨[12,13,24],1⟩,⟨[14,20,22,24],1⟩,⟨[21,23,24],1⟩,⟨[25],3⟩,⟨[12,14,25],1⟩,⟨[13,21,22,25],1⟩,⟨[20,23,25],1⟩,⟨[24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11380
namespace Case11380
def big : Finset (Finset (Fin 9)) := {{0,4,7},{1,2,5,7},{3,6,7},{1,4,8},{0,3,5,8},{2,6,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{1,3},{2,3},{2,4},{3,4},{4,5},{0,6},{1,6},{4,6},{5,6},{0,4,7},{1,2,5,7},{3,6,7},{1,4,8},{0,3,5,8},{2,6,8},{7,8}]
end Case11380
namespace Case11381
def positionFn : Fin 9 → Fin 25 := ![11,12,19,20,13,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{1,2},{3},{0,3},{1,3},{4},{5},{2,3,4,5},{6},{1,6},{3,6},{0,4,6},{5,6},{7},{0,7},{2,7},{1,4,7},{5,7},{6,7},{8},{4,8},{0,1,5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={4} then 2 else if T={5} then 3 else if T={2,3,4,5} then 1 else if T={6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={0,4,6} then 1 else if T={5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={4,8} then 1 else if T={0,1,5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,13,14,20,21,22,23,24,25],[⟨[],2⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[20],1⟩,⟨[12,20],1⟩,⟨[13,20],1⟩,⟨[21],1⟩,⟨[12,21],1⟩,⟨[13,21],1⟩,⟨[14],2⟩,⟨[22],3⟩,⟨[14,20,21,22],1⟩,⟨[23],1⟩,⟨[13,23],1⟩,⟨[21,23],1⟩,⟨[12,14,23],1⟩,⟨[22,23],1⟩,⟨[24],1⟩,⟨[12,24],1⟩,⟨[20,24],1⟩,⟨[13,14,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[25],3⟩,⟨[14,25],1⟩,⟨[12,13,22,25],1⟩,⟨[20,23,25],1⟩,⟨[21,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11381
namespace Case11381
def big : Finset (Finset (Fin 9)) := {{2,3,4,5},{0,4,6},{1,4,7},{0,1,5,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,3},{1,3},{2,3,4,5},{1,6},{3,6},{0,4,6},{5,6},{0,7},{2,7},{1,4,7},{5,7},{6,7},{4,8},{0,1,5,8},{2,6,8},{3,7,8}]
end Case11381
namespace Case11382
def positionFn : Fin 9 → Fin 25 := ![12,19,13,11,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{1,2},{1,3},{0,4},{2,4},{3,4},{5},{3,5},{4,5},{6},{0,6},{1,6},{3,6},{7},{0,3,7},{1,4,7},{2,5,6,7},{8},{2,3,8},{0,1,5,8},{4,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={1,3} then 1 else if T={0,4} then 1 else if T={2,4} then 1 else if T={3,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={7} then 3 else if T={0,3,7} then 1 else if T={1,4,7} then 1 else if T={2,5,6,7} then 1 else if T={8} then 3 else if T={2,3,8} then 1 else if T={0,1,5,8} then 1 else if T={4,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,13,14,20,21,22,23,24,25],[⟨[],2⟩,⟨[13],1⟩,⟨[20],1⟩,⟨[14],1⟩,⟨[13,14],1⟩,⟨[14,20],1⟩,⟨[12,20],1⟩,⟨[13,21],1⟩,⟨[14,21],1⟩,⟨[12,21],1⟩,⟨[22],3⟩,⟨[12,22],1⟩,⟨[21,22],1⟩,⟨[23],2⟩,⟨[13,23],1⟩,⟨[20,23],1⟩,⟨[12,23],1⟩,⟨[24],3⟩,⟨[12,13,24],1⟩,⟨[20,21,24],1⟩,⟨[14,22,23,24],1⟩,⟨[25],3⟩,⟨[12,14,25],1⟩,⟨[13,20,22,25],1⟩,⟨[21,23,25],1⟩,⟨[24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11382
namespace Case11382
def big : Finset (Finset (Fin 9)) := {{0,3,7},{1,4,7},{2,5,6,7},{2,3,8},{0,1,5,8},{4,6,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{0,4},{2,4},{3,4},{3,5},{4,5},{0,6},{1,6},{3,6},{0,3,7},{1,4,7},{2,5,6,7},{2,3,8},{0,1,5,8},{4,6,8},{7,8}]
end Case11382
namespace Case11383
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{0,2},{2,3},{4},{0,3,4},{5},{3,5},{1,2,4,5},{6},{1,6},{2,6},{3,6},{7},{0,7},{1,7},{3,7},{5,7},{4,6,7},{8},{1,3,8},{4,8},{0,5,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,3,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={1,2,4,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={4,6,7} then 1 else if T={8} then 3 else if T={1,3,8} then 1 else if T={4,8} then 1 else if T={0,5,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[10,12],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[10,13,14],1⟩,⟨[15],3⟩,⟨[13,15],1⟩,⟨[11,12,14,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[14,16,17],1⟩,⟨[18],3⟩,⟨[11,13,18],1⟩,⟨[14,18],1⟩,⟨[10,15,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11383
namespace Case11383
def big : Finset (Finset (Fin 9)) := {{0,3,4},{1,2,4,5},{4,6,7},{1,3,8},{0,5,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{2,3},{0,3,4},{3,5},{1,2,4,5},{1,6},{2,6},{3,6},{0,7},{1,7},{3,7},{5,7},{4,6,7},{1,3,8},{4,8},{0,5,6,8},{2,7,8}]
end Case11383
namespace Case11384
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{1,2},{2,3},{4},{0,3,4},{5},{3,5},{6},{0,6},{2,6},{3,6},{1,4,5,6},{7},{0,7},{1,7},{3,7},{2,4,7},{5,7},{8},{1,3,8},{4,8},{0,2,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,3,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={1,4,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={8} then 3 else if T={1,3,8} then 1 else if T={4,8} then 1 else if T={0,2,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[13],1⟩,⟨[12,13],1⟩,⟨[13,14],1⟩,⟨[15],2⟩,⟨[11,14,15],1⟩,⟨[16],3⟩,⟨[14,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[12,15,16,17],1⟩,⟨[18],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[14,18],1⟩,⟨[13,15,18],1⟩,⟨[16,18],1⟩,⟨[19],3⟩,⟨[12,14,19],1⟩,⟨[15,19],1⟩,⟨[11,13,16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11384
namespace Case11384
def big : Finset (Finset (Fin 9)) := {{0,3,4},{1,4,5,6},{2,4,7},{1,3,8},{0,2,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{2,3},{0,3,4},{3,5},{0,6},{2,6},{3,6},{1,4,5,6},{0,7},{1,7},{3,7},{2,4,7},{5,7},{1,3,8},{4,8},{0,2,5,8},{6,7,8}]
end Case11384
namespace Case11385
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{2},{1,2},{1,3},{2,3},{4},{5},{3,5},{0,2,4,5},{6},{0,6},{2,6},{3,4,6},{7},{0,7},{3,7},{1,4,7},{5,7},{6,7},{8},{0,3,8},{4,8},{1,5,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={2} then 1 else if T={1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={5} then 3 else if T={3,5} then 1 else if T={0,2,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={3,7} then 1 else if T={1,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={0,3,8} then 1 else if T={4,8} then 1 else if T={1,5,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[15],3⟩,⟨[13,15],1⟩,⟨[10,12,14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[17],1⟩,⟨[10,17],1⟩,⟨[13,17],1⟩,⟨[11,14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[10,13,18],1⟩,⟨[14,18],1⟩,⟨[11,15,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11385
namespace Case11385
def big : Finset (Finset (Fin 9)) := {{0,2,4,5},{3,4,6},{1,4,7},{0,3,8},{1,5,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{1,3},{2,3},{3,5},{0,2,4,5},{0,6},{2,6},{3,4,6},{0,7},{3,7},{1,4,7},{5,7},{6,7},{0,3,8},{4,8},{1,5,6,8},{2,7,8}]
end Case11385
namespace Case11386
def positionFn : Fin 9 → Fin 25 := ![14,18,19,11,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{1,2},{1,3},{2,3},{4},{0,3,4},{5},{3,5},{6},{0,6},{1,6},{2,4,5,6},{7},{0,7},{3,7},{1,4,7},{5,7},{6,7},{8},{4,8},{0,1,5,8},{3,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,3,4} then 1 else if T={5} then 3 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,4,5,6} then 1 else if T={7} then 1 else if T={0,7} then 1 else if T={3,7} then 1 else if T={1,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={4,8} then 1 else if T={0,1,5,8} then 1 else if T={3,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,15,19,20,21,22,23,24,25],[⟨[],2⟩,⟨[15],1⟩,⟨[19],1⟩,⟨[20],1⟩,⟨[15,20],1⟩,⟨[19,20],1⟩,⟨[12,19],1⟩,⟨[12,20],1⟩,⟨[21],2⟩,⟨[12,15,21],1⟩,⟨[22],3⟩,⟨[12,22],1⟩,⟨[23],2⟩,⟨[15,23],1⟩,⟨[19,23],1⟩,⟨[20,21,22,23],1⟩,⟨[24],1⟩,⟨[15,24],1⟩,⟨[12,24],1⟩,⟨[19,21,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[25],3⟩,⟨[21,25],1⟩,⟨[15,19,22,25],1⟩,⟨[12,23,25],1⟩,⟨[20,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11386
namespace Case11386
def big : Finset (Finset (Fin 9)) := {{0,3,4},{2,4,5,6},{1,4,7},{0,1,5,8},{3,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{1,3},{2,3},{0,3,4},{3,5},{0,6},{1,6},{2,4,5,6},{0,7},{3,7},{1,4,7},{5,7},{6,7},{4,8},{0,1,5,8},{3,6,8},{2,7,8}]
end Case11386
namespace Case11387
def positionFn : Fin 9 → Fin 25 := ![11,12,19,13,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{2},{0,2},{1,2},{3},{4},{3,4},{5},{0,1,4,5},{6},{0,6},{1,6},{2,3,5,6},{7},{1,7},{0,3,7},{2,4,7},{5,7},{6,7},{8},{0,8},{2,8},{1,3,8},{5,8},{4,6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={2} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={3,4} then 1 else if T={5} then 3 else if T={0,1,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,3,5,6} then 1 else if T={7} then 1 else if T={1,7} then 1 else if T={0,3,7} then 1 else if T={2,4,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,3,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,13,14,20,21,22,23,24,25],[⟨[],2⟩,⟨[12],1⟩,⟨[13],1⟩,⟨[20],1⟩,⟨[12,20],1⟩,⟨[13,20],1⟩,⟨[14],2⟩,⟨[21],2⟩,⟨[14,21],1⟩,⟨[22],3⟩,⟨[12,13,21,22],1⟩,⟨[23],2⟩,⟨[12,23],1⟩,⟨[13,23],1⟩,⟨[14,20,22,23],1⟩,⟨[24],1⟩,⟨[13,24],1⟩,⟨[12,14,24],1⟩,⟨[20,21,24],1⟩,⟨[22,24],1⟩,⟨[23,24],1⟩,⟨[25],1⟩,⟨[12,25],1⟩,⟨[20,25],1⟩,⟨[13,14,25],1⟩,⟨[22,25],1⟩,⟨[21,23,25],1⟩,⟨[24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11387
namespace Case11387
def big : Finset (Finset (Fin 9)) := {{0,1,4,5},{2,3,5,6},{0,3,7},{2,4,7},{1,3,8},{4,6,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{3,4},{0,1,4,5},{0,6},{1,6},{2,3,5,6},{1,7},{0,3,7},{2,4,7},{5,7},{6,7},{0,8},{2,8},{1,3,8},{5,8},{4,6,8},{7,8}]
end Case11387
namespace Case11388
def positionFn : Fin 9 → Fin 25 := ![14,18,11,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{2,3},{4},{5},{2,5},{3,5},{0,1,4,5},{6},{0,6},{1,6},{3,6},{2,4,6},{7},{0,7},{1,7},{2,7},{3,4,7},{8},{0,2,8},{1,3,8},{4,8},{5,6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={5} then 3 else if T={2,5} then 1 else if T={3,5} then 1 else if T={0,1,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={2,4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,4,7} then 1 else if T={8} then 3 else if T={0,2,8} then 1 else if T={1,3,8} then 1 else if T={4,8} then 1 else if T={5,6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,15,19,20,21,22,23,24,25],[⟨[],2⟩,⟨[15],1⟩,⟨[19],1⟩,⟨[12,19],1⟩,⟨[15,20],1⟩,⟨[12,20],1⟩,⟨[21],2⟩,⟨[22],3⟩,⟨[12,22],1⟩,⟨[20,22],1⟩,⟨[15,19,21,22],1⟩,⟨[23],2⟩,⟨[15,23],1⟩,⟨[19,23],1⟩,⟨[20,23],1⟩,⟨[12,21,23],1⟩,⟨[24],2⟩,⟨[15,24],1⟩,⟨[19,24],1⟩,⟨[12,24],1⟩,⟨[20,21,24],1⟩,⟨[25],3⟩,⟨[12,15,25],1⟩,⟨[19,20,25],1⟩,⟨[21,25],1⟩,⟨[22,23,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11388
namespace Case11388
def big : Finset (Finset (Fin 9)) := {{0,1,4,5},{2,4,6},{3,4,7},{0,2,8},{1,3,8},{5,6,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{2,3},{2,5},{3,5},{0,1,4,5},{0,6},{1,6},{3,6},{2,4,6},{0,7},{1,7},{2,7},{3,4,7},{0,2,8},{1,3,8},{4,8},{5,6,7,8}]
end Case11388
namespace Case11389
def positionFn : Fin 9 → Fin 25 := ![14,18,11,19,20,21,22,23,24]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{0,3},{2,3},{4},{0,2,4},{1,3,4},{5},{2,5},{3,5},{6},{0,6},{1,6},{3,6},{7},{0,7},{1,7},{2,7},{4,5,6,7},{8},{4,8},{0,1,5,8},{2,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,2,4} then 1 else if T={1,3,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={3,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={4,5,6,7} then 1 else if T={8} then 3 else if T={4,8} then 1 else if T={0,1,5,8} then 1 else if T={2,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[12,15,19,20,21,22,23,24,25],[⟨[],2⟩,⟨[15],1⟩,⟨[19],1⟩,⟨[12,19],1⟩,⟨[15,20],1⟩,⟨[12,20],1⟩,⟨[21],2⟩,⟨[12,15,21],1⟩,⟨[19,20,21],1⟩,⟨[22],3⟩,⟨[12,22],1⟩,⟨[20,22],1⟩,⟨[23],2⟩,⟨[15,23],1⟩,⟨[19,23],1⟩,⟨[20,23],1⟩,⟨[24],2⟩,⟨[15,24],1⟩,⟨[19,24],1⟩,⟨[12,24],1⟩,⟨[21,22,23,24],1⟩,⟨[25],3⟩,⟨[21,25],1⟩,⟨[15,19,22,25],1⟩,⟨[12,23,25],1⟩,⟨[20,24,25],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11389
namespace Case11389
def big : Finset (Finset (Fin 9)) := {{0,2,4},{1,3,4},{4,5,6,7},{0,1,5,8},{2,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,3},{2,3},{0,2,4},{1,3,4},{2,5},{3,5},{0,6},{1,6},{3,6},{0,7},{1,7},{2,7},{4,5,6,7},{4,8},{0,1,5,8},{2,6,8},{3,7,8}]
end Case11389
namespace Case11390
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{1,2},{3},{0,2,3},{4},{3,4},{5},{2,5},{0,1,4,5},{6},{0,6},{1,6},{2,4,6},{7},{0,7},{1,7},{2,7},{3,5,6,7},{8},{0,8},{2,8},{1,3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,2,3} then 1 else if T={4} then 2 else if T={3,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={0,1,4,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,5,6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[10,12,13],1⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[10,11,14,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[11,16],1⟩,⟨[12,14,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,15,16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[12,18],1⟩,⟨[11,13,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[14,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11390
namespace Case11390
def big : Finset (Finset (Fin 9)) := {{0,2,3},{0,1,4,5},{2,4,6},{3,5,6,7},{1,3,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{1,2},{0,2,3},{3,4},{2,5},{0,1,4,5},{0,6},{1,6},{2,4,6},{0,7},{1,7},{2,7},{3,5,6,7},{0,8},{2,8},{1,3,8},{5,8},{6,8},{4,7,8}]
end Case11390
namespace Case11391
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{0,3},{1,3},{2,3},{4},{0,2,4},{5},{2,5},{3,5},{6},{1,6},{2,6},{3,4,6},{7},{0,7},{2,7},{1,4,5,7},{6,7},{8},{1,2,8},{4,8},{0,5,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,2,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={1,2,8} then 1 else if T={4,8} then 1 else if T={0,5,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[10,13],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[10,12,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[12,17],1⟩,⟨[11,14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[11,12,18],1⟩,⟨[14,18],1⟩,⟨[10,15,16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11391
namespace Case11391
def big : Finset (Finset (Fin 9)) := {{0,2,4},{3,4,6},{1,4,5,7},{1,2,8},{0,5,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,3},{1,3},{2,3},{0,2,4},{2,5},{3,5},{1,6},{2,6},{3,4,6},{0,7},{2,7},{1,4,5,7},{6,7},{1,2,8},{4,8},{0,5,6,8},{3,7,8}]
end Case11391
namespace Case11392
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{3},{0,2,3},{4},{1,2,4},{3,4},{5},{2,5},{6},{0,6},{2,6},{1,3,5,6},{7},{1,7},{2,7},{0,4,5,7},{6,7},{8},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={3} then 2 else if T={0,2,3} then 1 else if T={4} then 2 else if T={1,2,4} then 1 else if T={3,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,6} then 1 else if T={1,3,5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={0,4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={5,8} then 1 else if T={4,6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[14],2⟩,⟨[11,13,14],1⟩,⟨[15],2⟩,⟨[12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[13,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[13,17],1⟩,⟨[12,14,16,17],1⟩,⟨[18],2⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[11,15,16,18],1⟩,⟨[17,18],1⟩,⟨[19],1⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,19],1⟩,⟨[16,19],1⟩,⟨[15,17,19],1⟩,⟨[14,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11392
namespace Case11392
def big : Finset (Finset (Fin 9)) := {{0,2,3},{1,2,4},{1,3,5,6},{0,4,5,7},{4,6,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2,3},{1,2,4},{3,4},{2,5},{0,6},{2,6},{1,3,5,6},{1,7},{2,7},{0,4,5,7},{6,7},{0,8},{1,8},{2,8},{5,8},{4,6,8},{3,7,8}]
end Case11392
namespace Case11393
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{0,2},{1,2},{3},{4},{3,4},{5},{2,5},{6},{1,6},{2,3,6},{0,4,5,6},{7},{0,7},{2,4,7},{1,3,5,7},{6,7},{8},{2,8},{0,3,8},{1,4,8},{5,8},{6,8},{7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={4} then 2 else if T={3,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={0,4,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,4,7} then 1 else if T={1,3,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={2,8} then 1 else if T={0,3,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[12],1⟩,⟨[11,12],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[15],2⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[13,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[11,15,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,15,18],1⟩,⟨[12,14,16,18],1⟩,⟨[17,18],1⟩,⟨[19],1⟩,⟨[13,19],1⟩,⟨[11,14,19],1⟩,⟨[12,15,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11393
namespace Case11393
def big : Finset (Finset (Fin 9)) := {{2,3,6},{0,4,5,6},{2,4,7},{1,3,5,7},{0,3,8},{1,4,8}}
def full : List (Finset (Fin 9)) := [{0,1},{0,2},{1,2},{3,4},{2,5},{1,6},{2,3,6},{0,4,5,6},{0,7},{2,4,7},{1,3,5,7},{6,7},{2,8},{0,3,8},{1,4,8},{5,8},{6,8},{7,8}]
end Case11393
namespace Case11394
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{1,2},{0,3},{2,3},{4},{0,2,4},{5},{2,5},{3,5},{6},{1,6},{2,6},{3,4,6},{7},{0,7},{3,7},{1,4,5,7},{6,7},{8},{1,3,8},{4,8},{0,5,6,8},{2,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={1,2} then 1 else if T={0,3} then 1 else if T={2,3} then 1 else if T={4} then 2 else if T={0,2,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={3,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={3,7} then 1 else if T={1,4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 3 else if T={1,3,8} then 1 else if T={4,8} then 1 else if T={0,5,6,8} then 1 else if T={2,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[10,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[10,12,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],2⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,14,16],1⟩,⟨[17],2⟩,⟨[10,17],1⟩,⟨[13,17],1⟩,⟨[11,14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],3⟩,⟨[11,13,18],1⟩,⟨[14,18],1⟩,⟨[10,15,16,18],1⟩,⟨[12,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11394
namespace Case11394
def big : Finset (Finset (Fin 9)) := {{0,2,4},{3,4,6},{1,4,5,7},{1,3,8},{0,5,6,8},{2,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{0,3},{2,3},{0,2,4},{2,5},{3,5},{1,6},{2,6},{3,4,6},{0,7},{3,7},{1,4,5,7},{6,7},{1,3,8},{4,8},{0,5,6,8},{2,7,8}]
end Case11394
namespace Case11395
def positionFn : Fin 9 → Fin 25 := ![9,10,11,12,13,14,15,16,17]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{1},{0,1},{1,2},{3},{0,2,3},{4},{3,4},{5},{2,5},{6},{0,6},{2,4,6},{1,3,5,6},{7},{1,7},{2,7},{0,4,5,7},{6,7},{8},{0,8},{2,8},{1,4,8},{5,8},{6,8},{3,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={1} then 1 else if T={0,1} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,2,3} then 1 else if T={4} then 2 else if T={3,4} then 1 else if T={5} then 3 else if T={2,5} then 1 else if T={6} then 2 else if T={0,6} then 1 else if T={2,4,6} then 1 else if T={1,3,5,6} then 1 else if T={7} then 2 else if T={1,7} then 1 else if T={2,7} then 1 else if T={0,4,5,7} then 1 else if T={6,7} then 1 else if T={8} then 1 else if T={0,8} then 1 else if T={2,8} then 1 else if T={1,4,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={3,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[10,11,12,13,14,15,16,17,18],[⟨[],2⟩,⟨[10],1⟩,⟨[11],1⟩,⟨[10,11],1⟩,⟨[11,12],1⟩,⟨[13],2⟩,⟨[10,12,13],1⟩,⟨[14],2⟩,⟨[13,14],1⟩,⟨[15],3⟩,⟨[12,15],1⟩,⟨[16],2⟩,⟨[10,16],1⟩,⟨[12,14,16],1⟩,⟨[11,13,15,16],1⟩,⟨[17],2⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[10,14,15,17],1⟩,⟨[16,17],1⟩,⟨[18],1⟩,⟨[10,18],1⟩,⟨[12,18],1⟩,⟨[11,14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[13,17,18],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11395
namespace Case11395
def big : Finset (Finset (Fin 9)) := {{0,2,3},{2,4,6},{1,3,5,6},{0,4,5,7},{1,4,8},{3,7,8}}
def full : List (Finset (Fin 9)) := [{0,1},{1,2},{0,2,3},{3,4},{2,5},{0,6},{2,4,6},{1,3,5,6},{1,7},{2,7},{0,4,5,7},{6,7},{0,8},{2,8},{1,4,8},{5,8},{6,8},{3,7,8}]
end Case11395
namespace Case11396
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0},{0,2},{1,2},{3},{0,1,3},{4},{3,4},{5},{1,5},{2,5},{6},{1,6},{2,3,6},{0,4,5,6},{7},{0,7},{2,7},{1,4,7},{6,7},{8},{0,8},{1,8},{2,4,8},{6,8},{3,5,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 2 else if T={0} then 1 else if T={0,2} then 1 else if T={1,2} then 1 else if T={3} then 2 else if T={0,1,3} then 1 else if T={4} then 2 else if T={3,4} then 1 else if T={5} then 3 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 2 else if T={1,6} then 1 else if T={2,3,6} then 1 else if T={0,4,5,6} then 1 else if T={7} then 2 else if T={0,7} then 1 else if T={2,7} then 1 else if T={1,4,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,4,8} then 1 else if T={6,8} then 1 else if T={3,5,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],2⟩,⟨[11],1⟩,⟨[11,13],1⟩,⟨[12,13],1⟩,⟨[14],2⟩,⟨[11,12,14],1⟩,⟨[15],2⟩,⟨[14,15],1⟩,⟨[16],3⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[17],2⟩,⟨[12,17],1⟩,⟨[13,14,17],1⟩,⟨[11,15,16,17],1⟩,⟨[18],2⟩,⟨[11,18],1⟩,⟨[13,18],1⟩,⟨[12,15,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,15,19],1⟩,⟨[17,19],1⟩,⟨[14,16,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11396
namespace Case11396
def big : Finset (Finset (Fin 9)) := {{0,1,3},{2,3,6},{0,4,5,6},{1,4,7},{2,4,8},{3,5,7,8}}
def full : List (Finset (Fin 9)) := [{0,2},{1,2},{0,1,3},{3,4},{1,5},{2,5},{1,6},{2,3,6},{0,4,5,6},{0,7},{2,7},{1,4,7},{6,7},{0,8},{1,8},{2,4,8},{6,8},{3,5,7,8}]
end Case11396
namespace Case11397
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{5},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{3,6},{4,6},{5,6},{7},{0,1,2,7},{3,7},{4,7},{5,7},{8},{0,8},{1,8},{2,8},{3,4,5,8},{6,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,6} then 1 else if T={4,6} then 1 else if T={5,6} then 1 else if T={7} then 2 else if T={0,1,2,7} then 1 else if T={3,7} then 1 else if T={4,7} then 1 else if T={5,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,4,5,8} then 1 else if T={6,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],5⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[14,17],1⟩,⟨[15,17],1⟩,⟨[16,17],1⟩,⟨[18],2⟩,⟨[11,12,13,18],1⟩,⟨[14,18],1⟩,⟨[15,18],1⟩,⟨[16,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,19],1⟩,⟨[14,15,16,19],1⟩,⟨[17,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11397
namespace Case11397
def big : Finset (Finset (Fin 9)) := {{0,1,2,7},{3,4,5,8},{6,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{3,6},{4,6},{5,6},{0,1,2,7},{3,7},{4,7},{5,7},{0,8},{1,8},{2,8},{3,4,5,8},{6,7,8}]
end Case11397
namespace Case11398
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,3},{1,3},{2,3},{4},{0,1,2,4},{3,4},{5},{0,5},{1,5},{2,5},{4,5},{6},{0,6},{1,6},{2,6},{4,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{8},{0,8},{1,8},{2,8},{3,5,6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,1,2,4} then 1 else if T={3,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={4,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={4,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,8} then 1 else if T={1,8} then 1 else if T={2,8} then 1 else if T={3,5,6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],5⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,12,13,15],1⟩,⟨[14,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[15,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[15,17],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[14,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,19],1⟩,⟨[12,19],1⟩,⟨[13,19],1⟩,⟨[14,16,17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11398
namespace Case11398
def big : Finset (Finset (Fin 9)) := {{0,1,2,4},{3,5,6,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{2,3},{0,1,2,4},{3,4},{0,5},{1,5},{2,5},{4,5},{0,6},{1,6},{2,6},{4,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{0,8},{1,8},{2,8},{3,5,6,8},{4,7,8}]
end Case11398
namespace Case11399
def positionFn : Fin 9 → Fin 25 := ![10,11,12,13,14,15,16,17,18]
theorem positionFn_injective : Function.Injective positionFn := by decide +kernel
def positions : Fin 9 ↪ Fin 25 := ⟨positionFn,positionFn_injective⟩
def labels : List (Finset (Fin 9)) := [∅,{0,3},{1,3},{2,3},{4},{0,4},{1,4},{2,4},{5},{0,5},{1,5},{2,5},{6},{0,6},{1,6},{2,6},{3,4,5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{8},{0,1,2,8},{3,8},{5,8},{6,8},{4,7,8}]
theorem labels_nodup : labels.Nodup := by decide +kernel
def μ (T : Finset (Fin 9)) : ℕ := if T ∈ labels then (if T=∅ then 5 else if T={0,3} then 1 else if T={1,3} then 1 else if T={2,3} then 1 else if T={4} then 1 else if T={0,4} then 1 else if T={1,4} then 1 else if T={2,4} then 1 else if T={5} then 1 else if T={0,5} then 1 else if T={1,5} then 1 else if T={2,5} then 1 else if T={6} then 1 else if T={0,6} then 1 else if T={1,6} then 1 else if T={2,6} then 1 else if T={3,4,5,6} then 1 else if T={0,7} then 1 else if T={1,7} then 1 else if T={2,7} then 1 else if T={3,7} then 1 else if T={5,7} then 1 else if T={6,7} then 1 else if T={8} then 2 else if T={0,1,2,8} then 1 else if T={3,8} then 1 else if T={5,8} then 1 else if T={6,8} then 1 else if T={4,7,8} then 1 else 0) else 0
theorem support (T : Finset (Fin 9)) (h : μ T ≠ 0) : T ∈ labels := by
  by_contra hn; simp [μ,hn] at h
def p : Numeric.Profile := ⟨25,executableType positions Finset.univ,
  labels.map (fun T => ⟨executableType positions T,μ T⟩),none,[]⟩
theorem p_eq_profile : p=rawProfile labels positions μ [] := by
  simp only [p,executableType_eq,rawProfile]
def computed : Numeric.Profile := ⟨25,[11,12,13,14,15,16,17,18,19],[⟨[],5⟩,⟨[11,14],1⟩,⟨[12,14],1⟩,⟨[13,14],1⟩,⟨[15],1⟩,⟨[11,15],1⟩,⟨[12,15],1⟩,⟨[13,15],1⟩,⟨[16],1⟩,⟨[11,16],1⟩,⟨[12,16],1⟩,⟨[13,16],1⟩,⟨[17],1⟩,⟨[11,17],1⟩,⟨[12,17],1⟩,⟨[13,17],1⟩,⟨[14,15,16,17],1⟩,⟨[11,18],1⟩,⟨[12,18],1⟩,⟨[13,18],1⟩,⟨[14,18],1⟩,⟨[16,18],1⟩,⟨[17,18],1⟩,⟨[19],2⟩,⟨[11,12,13,19],1⟩,⟨[14,19],1⟩,⟨[16,19],1⟩,⟨[17,19],1⟩,⟨[15,18,19],1⟩],none,[]⟩
theorem p_eq_computed : p=computed := by rfl
theorem valid : Numeric.validProfile p 34 := by
  rw [p_eq_computed]; unfold Numeric.validProfile; decide +kernel
end Case11399
namespace Case11399
def big : Finset (Finset (Fin 9)) := {{3,4,5,6},{0,1,2,8},{4,7,8}}
def full : List (Finset (Fin 9)) := [{0,3},{1,3},{2,3},{0,4},{1,4},{2,4},{0,5},{1,5},{2,5},{0,6},{1,6},{2,6},{3,4,5,6},{0,7},{1,7},{2,7},{3,7},{5,7},{6,7},{0,1,2,8},{3,8},{5,8},{6,8},{4,7,8}]
end Case11399
end Aris4Math.ThirtyFour.TwentyFiveFiveLow

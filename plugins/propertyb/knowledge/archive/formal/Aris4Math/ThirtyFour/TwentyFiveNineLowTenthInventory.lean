import Aris4Math.ThirtyFour.TwentyFiveSparseCompletion
import Aris4Math.ThirtyFour.TwentyFiveInventorySupport
import Aris4Math.ThirtyFour.TwentyFiveUnitConditional
import Aris4Math.ThirtyFour.TwentyFiveNineLowInventory
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthData
namespace Aris4Math.ThirtyFour.TwentyFiveNineLowTenthInventory
open TwentyFiveUnitCounts Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
def big : Fin 25 → Finset (Finset (Fin 10)) := ![{{6,7,8},{0,1,6},{0,2,7},{0,5,8},{1,4,7},{2,4,8},{4,5,6},{1,3,8},{2,3,6},{3,5,7},{0,3,4,9},{1,2,5,9}},
{{0,1,2},{1,3,5},{1,6,8},{2,5,7},{3,6,7},{0,7,8},{2,4,6},{0,3,4},{4,5,8},{0,5,6,9},{1,4,7,9},{2,3,8,9}},
{{3,7,8},{0,3,4},{1,4,7},{2,4,8},{0,6,7},{1,6,8},{2,3,6},{0,5,8},{1,3,5},{2,5,7},{4,5,6},{0,1,2,9}},
{{6,7,8},{0,1,6},{0,2,7},{0,5,8},{1,4,7},{2,4,8},{4,5,6},{1,3,8},{2,3,6},{3,5,7},{0,3,4,9},{1,2,5,9}},
{{0,1,2},{1,3,5},{1,6,8},{2,5,7},{3,6,7},{0,7,8},{2,4,6},{0,3,4},{4,5,8},{0,5,6,9},{1,4,7,9},{2,3,8,9}},
{{6,7,8},{0,1,6},{0,4,7},{1,5,8},{3,4,8},{2,5,7},{2,3,6},{0,3,5,9},{1,2,4,9}},
{{0,1,2},{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{3,8,9},{4,7,9},{5,6,9}},
{{0,1,3},{0,7,8},{1,6,8},{3,5,7},{3,4,6},{4,5,8},{2,6,7},{1,2,5},{0,2,4},{3,8,9},{4,7,9},{5,6,9}},
{{3,5,8},{1,3,7},{2,5,7},{1,6,8},{2,4,8},{4,6,7},{0,5,6},{0,3,4},{7,8,9},{0,1,2,9}},
{{0,3,5},{3,7,8},{2,5,8},{0,4,7},{1,4,8},{2,6,7},{4,5,6},{1,3,6},{5,7,9},{0,1,2,9},{6,8,9}},
{{0,1,2},{1,5,6},{2,7,8},{3,5,7},{4,6,8},{0,3,4},{0,6,7,9},{1,3,8,9},{2,4,5,9}},
{{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{0,1,2,9},{3,8,9},{4,7,9},{5,6,9}},
{{0,1,2},{0,3,5},{1,3,6},{2,5,8},{2,6,7},{3,7,8},{4,5,6},{1,4,8},{0,4,7},{5,7,9},{6,8,9}},
{{3,6,7},{0,7,8},{1,6,8},{0,3,4},{1,3,5},{4,5,8},{2,4,6},{2,5,7},{0,1,2,9}},
{{6,7,8},{0,1,6},{0,4,7},{1,5,8},{3,4,8},{2,5,7},{2,3,6},{0,3,5,9},{1,2,4,9}},
{{0,1,2},{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{3,8,9},{4,7,9},{5,6,9}},
{{0,1,3},{0,7,8},{1,6,8},{3,5,7},{3,4,6},{4,5,8},{2,6,7},{1,2,5},{0,2,4},{3,8,9},{4,7,9},{5,6,9}},
{{3,5,8},{1,3,7},{2,5,7},{1,6,8},{2,4,8},{4,6,7},{0,5,6},{0,3,4},{7,8,9},{0,1,2,9}},
{{0,3,5},{3,7,8},{2,5,8},{0,4,7},{1,4,8},{2,6,7},{4,5,6},{1,3,6},{5,7,9},{0,1,2,9},{6,8,9}},
{{0,1,2},{1,5,6},{2,7,8},{3,5,7},{4,6,8},{0,3,4},{0,6,7,9},{1,3,8,9},{2,4,5,9}},
{{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{0,1,2,9},{3,8,9},{4,7,9},{5,6,9}},
{{0,3,4},{1,5,6},{4,6,8},{3,5,7},{2,7,8},{0,1,2,9},{4,5,9},{3,8,9},{6,7,9}},
{{0,1,2},{3,4,5},{6,7,8},{0,3,6,9},{1,4,7,9},{2,5,8,9}},
{{0,3,4},{1,5,6},{4,6,8},{3,5,7},{2,7,8},{0,1,2,9},{4,5,9},{3,8,9},{6,7,9}},
{{0,1,2},{3,4,5},{6,7,8},{0,3,6,9},{1,4,7,9},{2,5,8,9}}]
def blockLabels : Fin 25 → List (Finset (Fin 10)) := ![[{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{1,3,8},{2,4,8},{0,5,8},{6,7,8},{0,3,4,9},{1,2,5,9},{6,9},{7,9},{8,9}],
[{0,1,2},{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{0,5,6,9},{1,4,7,9},{2,3,8,9}],
[{0,3,4},{1,3,5},{2,3,6},{4,5,6},{1,4,7},{2,5,7},{0,6,7},{2,4,8},{0,5,8},{1,6,8},{3,7,8},{0,1,2,9},{3,9},{4,9},{5,9},{6,9},{7,9},{8,9}],
[{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{1,3,8},{2,4,8},{0,5,8},{6,7,8},{0,3,4,9},{1,2,5,9},{6,9},{7,9},{8,9}],
[{0,1,2},{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{0,5,6,9},{1,4,7,9},{2,3,8,9}],
[{0,2},{1,3},{4,5},{0,1,6},{2,3,6},{4,6},{5,6},{1,7},{3,7},{0,4,7},{2,5,7},{0,8},{2,8},{3,4,8},{1,5,8},{6,7,8},{1,2,4,9},{0,3,5,9},{6,9},{7,9},{8,9}],
[{0,1,2},{2,3},{1,4},{0,3,4},{0,5},{1,3,5},{0,6},{2,4,6},{1,7},{2,5,7},{3,6,7},{2,8},{4,5,8},{1,6,8},{0,7,8},{0,9},{1,9},{2,9},{5,6,9},{4,7,9},{3,8,9}],
[{0,1,3},{2,3},{1,4},{0,2,4},{0,5},{1,2,5},{0,6},{3,4,6},{1,7},{3,5,7},{2,6,7},{2,8},{4,5,8},{1,6,8},{0,7,8},{0,9},{1,9},{2,9},{5,6,9},{4,7,9},{3,8,9}],
[{2,3},{1,4},{0,3,4},{1,5},{4,5},{2,6},{3,6},{0,5,6},{0,7},{1,3,7},{2,5,7},{4,6,7},{0,8},{2,4,8},{3,5,8},{1,6,8},{0,1,2,9},{3,9},{4,9},{5,9},{6,9},{7,8,9}],
[{2,3},{2,4},{3,4},{1,5},{0,3,5},{0,6},{1,3,6},{4,5,6},{1,7},{0,4,7},{2,6,7},{0,8},{1,4,8},{2,5,8},{3,7,8},{0,1,2,9},{3,9},{4,9},{5,7,9},{6,8,9}],
[{0,1,2},{2,3},{1,4},{0,3,4},{0,5},{2,6},{3,6},{1,5,6},{1,7},{4,7},{3,5,7},{0,8},{5,8},{4,6,8},{2,7,8},{2,4,5,9},{0,6,7,9},{1,3,8,9}],
[{2,3},{1,4},{0,3,4},{0,5},{1,3,5},{0,6},{2,4,6},{1,7},{2,5,7},{3,6,7},{2,8},{4,5,8},{1,6,8},{0,7,8},{0,1,2,9},{5,6,9},{4,7,9},{3,8,9}],
[{0,1,2},{2,3},{2,4},{3,4},{1,5},{0,3,5},{0,6},{1,3,6},{4,5,6},{1,7},{0,4,7},{2,6,7},{0,8},{1,4,8},{2,5,8},{3,7,8},{0,9},{1,9},{2,9},{3,9},{4,9},{5,7,9},{6,8,9}],
[{2,3},{1,4},{0,3,4},{0,5},{1,3,5},{0,6},{2,4,6},{5,6},{1,7},{4,7},{2,5,7},{3,6,7},{2,8},{3,8},{4,5,8},{1,6,8},{0,7,8},{0,1,2,9},{3,9},{4,9},{5,9},{6,9},{7,9},{8,9}],
[{0,2},{1,3},{4,5},{0,1,6},{2,3,6},{4,6},{5,6},{1,7},{3,7},{0,4,7},{2,5,7},{0,8},{2,8},{3,4,8},{1,5,8},{6,7,8},{1,2,4,9},{0,3,5,9},{6,9},{7,9},{8,9}],
[{0,1,2},{2,3},{1,4},{0,3,4},{0,5},{1,3,5},{0,6},{2,4,6},{1,7},{2,5,7},{3,6,7},{2,8},{4,5,8},{1,6,8},{0,7,8},{0,9},{1,9},{2,9},{5,6,9},{4,7,9},{3,8,9}],
[{0,1,3},{2,3},{1,4},{0,2,4},{0,5},{1,2,5},{0,6},{3,4,6},{1,7},{3,5,7},{2,6,7},{2,8},{4,5,8},{1,6,8},{0,7,8},{0,9},{1,9},{2,9},{5,6,9},{4,7,9},{3,8,9}],
[{2,3},{1,4},{0,3,4},{1,5},{4,5},{2,6},{3,6},{0,5,6},{0,7},{1,3,7},{2,5,7},{4,6,7},{0,8},{2,4,8},{3,5,8},{1,6,8},{0,1,2,9},{3,9},{4,9},{5,9},{6,9},{7,8,9}],
[{2,3},{2,4},{3,4},{1,5},{0,3,5},{0,6},{1,3,6},{4,5,6},{1,7},{0,4,7},{2,6,7},{0,8},{1,4,8},{2,5,8},{3,7,8},{0,1,2,9},{3,9},{4,9},{5,7,9},{6,8,9}],
[{0,1,2},{2,3},{1,4},{0,3,4},{0,5},{2,6},{3,6},{1,5,6},{1,7},{4,7},{3,5,7},{0,8},{5,8},{4,6,8},{2,7,8},{2,4,5,9},{0,6,7,9},{1,3,8,9}],
[{2,3},{1,4},{0,3,4},{0,5},{1,3,5},{0,6},{2,4,6},{1,7},{2,5,7},{3,6,7},{2,8},{4,5,8},{1,6,8},{0,7,8},{0,1,2,9},{5,6,9},{4,7,9},{3,8,9}],
[{1,3},{2,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{0,6},{2,6},{3,6},{1,5,6},{0,7},{1,7},{4,7},{3,5,7},{0,8},{1,8},{5,8},{4,6,8},{2,7,8},{0,1,2,9},{4,5,9},{6,7,9},{3,8,9}],
[{0,1,2},{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{3,4,5},{1,6},{2,6},{4,6},{5,6},{0,7},{2,7},{3,7},{5,7},{0,8},{1,8},{3,8},{4,8},{6,7,8},{0,3,6,9},{1,4,7,9},{2,5,8,9}],
[{1,3},{2,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{0,6},{2,6},{3,6},{1,5,6},{0,7},{1,7},{4,7},{3,5,7},{0,8},{1,8},{5,8},{4,6,8},{2,7,8},{0,1,2,9},{4,5,9},{6,7,9},{3,8,9}],
[{0,1,2},{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{3,4,5},{1,6},{2,6},{4,6},{5,6},{0,7},{2,7},{3,7},{5,7},{0,8},{1,8},{3,8},{4,8},{6,7,8},{0,3,6,9},{1,4,7,9},{2,5,8,9}]]
def full (c : Fin 25) : Finset (Finset (Fin 10)) := (blockLabels c).toFinset
def lastDegree : Fin 25 → ℕ := ![6,6,7,7,7,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,6,6,7,7]
def degrees (c : Fin 25) (i : Fin 10) : ℕ := if i.val<9 then 6 else lastDegree c
theorem completion0 : pairCompletion (big 0)=full 0 := by
  have same : big 0=([{6,7,8},{0,1,6},{0,2,7},{0,5,8},{1,4,7},{2,4,8},{4,5,6},{1,3,8},{2,3,6},{3,5,7},{0,3,4,9},{1,2,5,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{6,7,8},{0,1,6},{0,2,7},{0,5,8},{1,4,7},{2,4,8},{4,5,6},{1,3,8},{2,3,6},{3,5,7},{0,3,4,9},{1,2,5,9}] [{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{1,3,8},{2,4,8},{0,5,8},{6,7,8},{0,3,4,9},{1,2,5,9},{6,9},{7,9},{8,9}]=true
  decide +kernel
theorem completion1 : pairCompletion (big 1)=full 1 := by
  have same : big 1=([{0,1,2},{1,3,5},{1,6,8},{2,5,7},{3,6,7},{0,7,8},{2,4,6},{0,3,4},{4,5,8},{0,5,6,9},{1,4,7,9},{2,3,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{1,3,5},{1,6,8},{2,5,7},{3,6,7},{0,7,8},{2,4,6},{0,3,4},{4,5,8},{0,5,6,9},{1,4,7,9},{2,3,8,9}] [{0,1,2},{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{0,5,6,9},{1,4,7,9},{2,3,8,9}]=true
  decide +kernel
theorem completion2 : pairCompletion (big 2)=full 2 := by
  have same : big 2=([{3,7,8},{0,3,4},{1,4,7},{2,4,8},{0,6,7},{1,6,8},{2,3,6},{0,5,8},{1,3,5},{2,5,7},{4,5,6},{0,1,2,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,7,8},{0,3,4},{1,4,7},{2,4,8},{0,6,7},{1,6,8},{2,3,6},{0,5,8},{1,3,5},{2,5,7},{4,5,6},{0,1,2,9}] [{0,3,4},{1,3,5},{2,3,6},{4,5,6},{1,4,7},{2,5,7},{0,6,7},{2,4,8},{0,5,8},{1,6,8},{3,7,8},{0,1,2,9},{3,9},{4,9},{5,9},{6,9},{7,9},{8,9}]=true
  decide +kernel
theorem completion3 : pairCompletion (big 3)=full 3 := by
  have same : big 3=([{6,7,8},{0,1,6},{0,2,7},{0,5,8},{1,4,7},{2,4,8},{4,5,6},{1,3,8},{2,3,6},{3,5,7},{0,3,4,9},{1,2,5,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{6,7,8},{0,1,6},{0,2,7},{0,5,8},{1,4,7},{2,4,8},{4,5,6},{1,3,8},{2,3,6},{3,5,7},{0,3,4,9},{1,2,5,9}] [{0,1,6},{2,3,6},{4,5,6},{0,2,7},{1,4,7},{3,5,7},{1,3,8},{2,4,8},{0,5,8},{6,7,8},{0,3,4,9},{1,2,5,9},{6,9},{7,9},{8,9}]=true
  decide +kernel
theorem completion4 : pairCompletion (big 4)=full 4 := by
  have same : big 4=([{0,1,2},{1,3,5},{1,6,8},{2,5,7},{3,6,7},{0,7,8},{2,4,6},{0,3,4},{4,5,8},{0,5,6,9},{1,4,7,9},{2,3,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{1,3,5},{1,6,8},{2,5,7},{3,6,7},{0,7,8},{2,4,6},{0,3,4},{4,5,8},{0,5,6,9},{1,4,7,9},{2,3,8,9}] [{0,1,2},{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{0,5,6,9},{1,4,7,9},{2,3,8,9}]=true
  decide +kernel
theorem completion5 : pairCompletion (big 5)=full 5 := by
  have same : big 5=([{6,7,8},{0,1,6},{0,4,7},{1,5,8},{3,4,8},{2,5,7},{2,3,6},{0,3,5,9},{1,2,4,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{6,7,8},{0,1,6},{0,4,7},{1,5,8},{3,4,8},{2,5,7},{2,3,6},{0,3,5,9},{1,2,4,9}] [{0,2},{1,3},{4,5},{0,1,6},{2,3,6},{4,6},{5,6},{1,7},{3,7},{0,4,7},{2,5,7},{0,8},{2,8},{3,4,8},{1,5,8},{6,7,8},{1,2,4,9},{0,3,5,9},{6,9},{7,9},{8,9}]=true
  decide +kernel
theorem completion6 : pairCompletion (big 6)=full 6 := by
  have same : big 6=([{0,1,2},{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{3,8,9},{4,7,9},{5,6,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{3,8,9},{4,7,9},{5,6,9}] [{0,1,2},{2,3},{1,4},{0,3,4},{0,5},{1,3,5},{0,6},{2,4,6},{1,7},{2,5,7},{3,6,7},{2,8},{4,5,8},{1,6,8},{0,7,8},{0,9},{1,9},{2,9},{5,6,9},{4,7,9},{3,8,9}]=true
  decide +kernel
theorem completion7 : pairCompletion (big 7)=full 7 := by
  have same : big 7=([{0,1,3},{0,7,8},{1,6,8},{3,5,7},{3,4,6},{4,5,8},{2,6,7},{1,2,5},{0,2,4},{3,8,9},{4,7,9},{5,6,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{0,7,8},{1,6,8},{3,5,7},{3,4,6},{4,5,8},{2,6,7},{1,2,5},{0,2,4},{3,8,9},{4,7,9},{5,6,9}] [{0,1,3},{2,3},{1,4},{0,2,4},{0,5},{1,2,5},{0,6},{3,4,6},{1,7},{3,5,7},{2,6,7},{2,8},{4,5,8},{1,6,8},{0,7,8},{0,9},{1,9},{2,9},{5,6,9},{4,7,9},{3,8,9}]=true
  decide +kernel
theorem completion8 : pairCompletion (big 8)=full 8 := by
  have same : big 8=([{3,5,8},{1,3,7},{2,5,7},{1,6,8},{2,4,8},{4,6,7},{0,5,6},{0,3,4},{7,8,9},{0,1,2,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,5,8},{1,3,7},{2,5,7},{1,6,8},{2,4,8},{4,6,7},{0,5,6},{0,3,4},{7,8,9},{0,1,2,9}] [{2,3},{1,4},{0,3,4},{1,5},{4,5},{2,6},{3,6},{0,5,6},{0,7},{1,3,7},{2,5,7},{4,6,7},{0,8},{2,4,8},{3,5,8},{1,6,8},{0,1,2,9},{3,9},{4,9},{5,9},{6,9},{7,8,9}]=true
  decide +kernel
theorem completion9 : pairCompletion (big 9)=full 9 := by
  have same : big 9=([{0,3,5},{3,7,8},{2,5,8},{0,4,7},{1,4,8},{2,6,7},{4,5,6},{1,3,6},{5,7,9},{0,1,2,9},{6,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,5},{3,7,8},{2,5,8},{0,4,7},{1,4,8},{2,6,7},{4,5,6},{1,3,6},{5,7,9},{0,1,2,9},{6,8,9}] [{2,3},{2,4},{3,4},{1,5},{0,3,5},{0,6},{1,3,6},{4,5,6},{1,7},{0,4,7},{2,6,7},{0,8},{1,4,8},{2,5,8},{3,7,8},{0,1,2,9},{3,9},{4,9},{5,7,9},{6,8,9}]=true
  decide +kernel
theorem completion10 : pairCompletion (big 10)=full 10 := by
  have same : big 10=([{0,1,2},{1,5,6},{2,7,8},{3,5,7},{4,6,8},{0,3,4},{0,6,7,9},{1,3,8,9},{2,4,5,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{1,5,6},{2,7,8},{3,5,7},{4,6,8},{0,3,4},{0,6,7,9},{1,3,8,9},{2,4,5,9}] [{0,1,2},{2,3},{1,4},{0,3,4},{0,5},{2,6},{3,6},{1,5,6},{1,7},{4,7},{3,5,7},{0,8},{5,8},{4,6,8},{2,7,8},{2,4,5,9},{0,6,7,9},{1,3,8,9}]=true
  decide +kernel
theorem completion11 : pairCompletion (big 11)=full 11 := by
  have same : big 11=([{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{0,1,2,9},{3,8,9},{4,7,9},{5,6,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{0,1,2,9},{3,8,9},{4,7,9},{5,6,9}] [{2,3},{1,4},{0,3,4},{0,5},{1,3,5},{0,6},{2,4,6},{1,7},{2,5,7},{3,6,7},{2,8},{4,5,8},{1,6,8},{0,7,8},{0,1,2,9},{5,6,9},{4,7,9},{3,8,9}]=true
  decide +kernel
theorem completion12 : pairCompletion (big 12)=full 12 := by
  have same : big 12=([{0,1,2},{0,3,5},{1,3,6},{2,5,8},{2,6,7},{3,7,8},{4,5,6},{1,4,8},{0,4,7},{5,7,9},{6,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,5},{1,3,6},{2,5,8},{2,6,7},{3,7,8},{4,5,6},{1,4,8},{0,4,7},{5,7,9},{6,8,9}] [{0,1,2},{2,3},{2,4},{3,4},{1,5},{0,3,5},{0,6},{1,3,6},{4,5,6},{1,7},{0,4,7},{2,6,7},{0,8},{1,4,8},{2,5,8},{3,7,8},{0,9},{1,9},{2,9},{3,9},{4,9},{5,7,9},{6,8,9}]=true
  decide +kernel
theorem completion13 : pairCompletion (big 13)=full 13 := by
  have same : big 13=([{3,6,7},{0,7,8},{1,6,8},{0,3,4},{1,3,5},{4,5,8},{2,4,6},{2,5,7},{0,1,2,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,6,7},{0,7,8},{1,6,8},{0,3,4},{1,3,5},{4,5,8},{2,4,6},{2,5,7},{0,1,2,9}] [{2,3},{1,4},{0,3,4},{0,5},{1,3,5},{0,6},{2,4,6},{5,6},{1,7},{4,7},{2,5,7},{3,6,7},{2,8},{3,8},{4,5,8},{1,6,8},{0,7,8},{0,1,2,9},{3,9},{4,9},{5,9},{6,9},{7,9},{8,9}]=true
  decide +kernel
theorem completion14 : pairCompletion (big 14)=full 14 := by
  have same : big 14=([{6,7,8},{0,1,6},{0,4,7},{1,5,8},{3,4,8},{2,5,7},{2,3,6},{0,3,5,9},{1,2,4,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{6,7,8},{0,1,6},{0,4,7},{1,5,8},{3,4,8},{2,5,7},{2,3,6},{0,3,5,9},{1,2,4,9}] [{0,2},{1,3},{4,5},{0,1,6},{2,3,6},{4,6},{5,6},{1,7},{3,7},{0,4,7},{2,5,7},{0,8},{2,8},{3,4,8},{1,5,8},{6,7,8},{1,2,4,9},{0,3,5,9},{6,9},{7,9},{8,9}]=true
  decide +kernel
theorem completion15 : pairCompletion (big 15)=full 15 := by
  have same : big 15=([{0,1,2},{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{3,8,9},{4,7,9},{5,6,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{3,8,9},{4,7,9},{5,6,9}] [{0,1,2},{2,3},{1,4},{0,3,4},{0,5},{1,3,5},{0,6},{2,4,6},{1,7},{2,5,7},{3,6,7},{2,8},{4,5,8},{1,6,8},{0,7,8},{0,9},{1,9},{2,9},{5,6,9},{4,7,9},{3,8,9}]=true
  decide +kernel
theorem completion16 : pairCompletion (big 16)=full 16 := by
  have same : big 16=([{0,1,3},{0,7,8},{1,6,8},{3,5,7},{3,4,6},{4,5,8},{2,6,7},{1,2,5},{0,2,4},{3,8,9},{4,7,9},{5,6,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,3},{0,7,8},{1,6,8},{3,5,7},{3,4,6},{4,5,8},{2,6,7},{1,2,5},{0,2,4},{3,8,9},{4,7,9},{5,6,9}] [{0,1,3},{2,3},{1,4},{0,2,4},{0,5},{1,2,5},{0,6},{3,4,6},{1,7},{3,5,7},{2,6,7},{2,8},{4,5,8},{1,6,8},{0,7,8},{0,9},{1,9},{2,9},{5,6,9},{4,7,9},{3,8,9}]=true
  decide +kernel
theorem completion17 : pairCompletion (big 17)=full 17 := by
  have same : big 17=([{3,5,8},{1,3,7},{2,5,7},{1,6,8},{2,4,8},{4,6,7},{0,5,6},{0,3,4},{7,8,9},{0,1,2,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{3,5,8},{1,3,7},{2,5,7},{1,6,8},{2,4,8},{4,6,7},{0,5,6},{0,3,4},{7,8,9},{0,1,2,9}] [{2,3},{1,4},{0,3,4},{1,5},{4,5},{2,6},{3,6},{0,5,6},{0,7},{1,3,7},{2,5,7},{4,6,7},{0,8},{2,4,8},{3,5,8},{1,6,8},{0,1,2,9},{3,9},{4,9},{5,9},{6,9},{7,8,9}]=true
  decide +kernel
theorem completion18 : pairCompletion (big 18)=full 18 := by
  have same : big 18=([{0,3,5},{3,7,8},{2,5,8},{0,4,7},{1,4,8},{2,6,7},{4,5,6},{1,3,6},{5,7,9},{0,1,2,9},{6,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,5},{3,7,8},{2,5,8},{0,4,7},{1,4,8},{2,6,7},{4,5,6},{1,3,6},{5,7,9},{0,1,2,9},{6,8,9}] [{2,3},{2,4},{3,4},{1,5},{0,3,5},{0,6},{1,3,6},{4,5,6},{1,7},{0,4,7},{2,6,7},{0,8},{1,4,8},{2,5,8},{3,7,8},{0,1,2,9},{3,9},{4,9},{5,7,9},{6,8,9}]=true
  decide +kernel
theorem completion19 : pairCompletion (big 19)=full 19 := by
  have same : big 19=([{0,1,2},{1,5,6},{2,7,8},{3,5,7},{4,6,8},{0,3,4},{0,6,7,9},{1,3,8,9},{2,4,5,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{1,5,6},{2,7,8},{3,5,7},{4,6,8},{0,3,4},{0,6,7,9},{1,3,8,9},{2,4,5,9}] [{0,1,2},{2,3},{1,4},{0,3,4},{0,5},{2,6},{3,6},{1,5,6},{1,7},{4,7},{3,5,7},{0,8},{5,8},{4,6,8},{2,7,8},{2,4,5,9},{0,6,7,9},{1,3,8,9}]=true
  decide +kernel
theorem completion20 : pairCompletion (big 20)=full 20 := by
  have same : big 20=([{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{0,1,2,9},{3,8,9},{4,7,9},{5,6,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,3,5},{2,4,6},{2,5,7},{3,6,7},{4,5,8},{1,6,8},{0,7,8},{0,1,2,9},{3,8,9},{4,7,9},{5,6,9}] [{2,3},{1,4},{0,3,4},{0,5},{1,3,5},{0,6},{2,4,6},{1,7},{2,5,7},{3,6,7},{2,8},{4,5,8},{1,6,8},{0,7,8},{0,1,2,9},{5,6,9},{4,7,9},{3,8,9}]=true
  decide +kernel
theorem completion21 : pairCompletion (big 21)=full 21 := by
  have same : big 21=([{0,3,4},{1,5,6},{4,6,8},{3,5,7},{2,7,8},{0,1,2,9},{4,5,9},{3,8,9},{6,7,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,5,6},{4,6,8},{3,5,7},{2,7,8},{0,1,2,9},{4,5,9},{3,8,9},{6,7,9}] [{1,3},{2,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{0,6},{2,6},{3,6},{1,5,6},{0,7},{1,7},{4,7},{3,5,7},{0,8},{1,8},{5,8},{4,6,8},{2,7,8},{0,1,2,9},{4,5,9},{6,7,9},{3,8,9}]=true
  decide +kernel
theorem completion22 : pairCompletion (big 22)=full 22 := by
  have same : big 22=([{0,1,2},{3,4,5},{6,7,8},{0,3,6,9},{1,4,7,9},{2,5,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{3,4,5},{6,7,8},{0,3,6,9},{1,4,7,9},{2,5,8,9}] [{0,1,2},{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{3,4,5},{1,6},{2,6},{4,6},{5,6},{0,7},{2,7},{3,7},{5,7},{0,8},{1,8},{3,8},{4,8},{6,7,8},{0,3,6,9},{1,4,7,9},{2,5,8,9}]=true
  decide +kernel
theorem completion23 : pairCompletion (big 23)=full 23 := by
  have same : big 23=([{0,3,4},{1,5,6},{4,6,8},{3,5,7},{2,7,8},{0,1,2,9},{4,5,9},{3,8,9},{6,7,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,3,4},{1,5,6},{4,6,8},{3,5,7},{2,7,8},{0,1,2,9},{4,5,9},{3,8,9},{6,7,9}] [{1,3},{2,3},{1,4},{2,4},{0,3,4},{0,5},{2,5},{0,6},{2,6},{3,6},{1,5,6},{0,7},{1,7},{4,7},{3,5,7},{0,8},{1,8},{5,8},{4,6,8},{2,7,8},{0,1,2,9},{4,5,9},{6,7,9},{3,8,9}]=true
  decide +kernel
theorem completion24 : pairCompletion (big 24)=full 24 := by
  have same : big 24=([{0,1,2},{3,4,5},{6,7,8},{0,3,6,9},{1,4,7,9},{2,5,8,9}] : List (Finset (Fin 10))).toFinset := by decide +kernel
  rw [same]
  apply TwentyFiveSparseCompletion.complete
  change TwentyFiveSparseCompletion.Check [{0,1,2},{3,4,5},{6,7,8},{0,3,6,9},{1,4,7,9},{2,5,8,9}] [{0,1,2},{1,3},{2,3},{0,4},{2,4},{0,5},{1,5},{3,4,5},{1,6},{2,6},{4,6},{5,6},{0,7},{2,7},{3,7},{5,7},{0,8},{1,8},{3,8},{4,8},{6,7,8},{0,3,6,9},{1,4,7,9},{2,5,8,9}]=true
  decide +kernel
theorem completion : ∀ c,pairCompletion (big c)=full c := by
  intro c
  fin_cases c
  · exact completion0
  · exact completion1
  · exact completion2
  · exact completion3
  · exact completion4
  · exact completion5
  · exact completion6
  · exact completion7
  · exact completion8
  · exact completion9
  · exact completion10
  · exact completion11
  · exact completion12
  · exact completion13
  · exact completion14
  · exact completion15
  · exact completion16
  · exact completion17
  · exact completion18
  · exact completion19
  · exact completion20
  · exact completion21
  · exact completion22
  · exact completion23
  · exact completion24
theorem recovered0 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 0) (full 0) T=TwentyFiveNineLowTenth.Case0.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case0.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 0)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case0.support T pos))
  · decide +kernel
theorem recovered1 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 1) (full 1) T=TwentyFiveNineLowTenth.Case1.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case1.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 1)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case1.support T pos))
  · decide +kernel
theorem recovered2 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 2) (full 2) T=TwentyFiveNineLowTenth.Case2.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case2.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 2)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case2.support T pos))
  · decide +kernel
theorem recovered3 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 3) (full 3) T=TwentyFiveNineLowTenth.Case3.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case3.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 3)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case3.support T pos))
  · decide +kernel
theorem recovered4 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 4) (full 4) T=TwentyFiveNineLowTenth.Case4.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case4.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 4)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case4.support T pos))
  · decide +kernel
theorem recovered5 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 5) (full 5) T=TwentyFiveNineLowTenth.Case5.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case5.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 5)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case5.support T pos))
  · decide +kernel
theorem recovered6 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 6) (full 6) T=TwentyFiveNineLowTenth.Case6.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case6.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 6)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case6.support T pos))
  · decide +kernel
theorem recovered7 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 7) (full 7) T=TwentyFiveNineLowTenth.Case7.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case7.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 7)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case7.support T pos))
  · decide +kernel
theorem recovered8 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 8) (full 8) T=TwentyFiveNineLowTenth.Case8.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case8.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 8)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case8.support T pos))
  · decide +kernel
theorem recovered9 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 9) (full 9) T=TwentyFiveNineLowTenth.Case9.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case9.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 9)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case9.support T pos))
  · decide +kernel
theorem recovered10 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 10) (full 10) T=TwentyFiveNineLowTenth.Case10.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case10.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 10)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case10.support T pos))
  · decide +kernel
theorem recovered11 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 11) (full 11) T=TwentyFiveNineLowTenth.Case11.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case11.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 11)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case11.support T pos))
  · decide +kernel
theorem recovered12 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 12) (full 12) T=TwentyFiveNineLowTenth.Case12.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case12.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 12)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case12.support T pos))
  · decide +kernel
theorem recovered13 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 13) (full 13) T=TwentyFiveNineLowTenth.Case13.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case13.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 13)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case13.support T pos))
  · decide +kernel
theorem recovered14 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 14) (full 14) T=TwentyFiveNineLowTenth.Case14.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case14.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 14)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case14.support T pos))
  · decide +kernel
theorem recovered15 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 15) (full 15) T=TwentyFiveNineLowTenth.Case15.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case15.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 15)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case15.support T pos))
  · decide +kernel
theorem recovered16 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 16) (full 16) T=TwentyFiveNineLowTenth.Case16.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case16.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 16)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case16.support T pos))
  · decide +kernel
theorem recovered17 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 17) (full 17) T=TwentyFiveNineLowTenth.Case17.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case17.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 17)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case17.support T pos))
  · decide +kernel
theorem recovered18 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 18) (full 18) T=TwentyFiveNineLowTenth.Case18.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case18.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 18)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case18.support T pos))
  · decide +kernel
theorem recovered19 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 19) (full 19) T=TwentyFiveNineLowTenth.Case19.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case19.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 19)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case19.support T pos))
  · decide +kernel
theorem recovered20 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 20) (full 20) T=TwentyFiveNineLowTenth.Case20.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case20.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 20)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case20.support T pos))
  · decide +kernel
theorem recovered21 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 21) (full 21) T=TwentyFiveNineLowTenth.Case21.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case21.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 21)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case21.support T pos))
  · decide +kernel
theorem recovered22 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 22) (full 22) T=TwentyFiveNineLowTenth.Case22.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case22.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 22)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case22.support T pos))
  · decide +kernel
theorem recovered23 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 23) (full 23) T=TwentyFiveNineLowTenth.Case23.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case23.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 23)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case23.support T pos))
  · decide +kernel
theorem recovered24 : ∀ T : Finset (Fin 10),
  inventory 34 (degrees 24) (full 24) T=TwentyFiveNineLowTenth.Case24.μ T := by
  apply TwentyFiveInventorySupport.eq_of_support
  · have included : (TwentyFiveNineLowTenth.Case24.labels).all
        (fun T => decide (T∈TwentyFiveInventorySupport.labels (blockLabels 24)))=true := by decide +kernel
    intro T pos
    exact of_decide_eq_true (List.all_eq_true.mp included T (TwentyFiveNineLowTenth.Case24.support T pos))
  · decide +kernel
theorem recovered (c : Fin 25) (T : Finset (Fin 10)) :
  inventory 34 (degrees c) (pairCompletion (big c)) T=TwentyFiveNineLowTenth.μ c T := by
  rw [completion]
  fin_cases c
  · exact recovered0 T
  · exact recovered1 T
  · exact recovered2 T
  · exact recovered3 T
  · exact recovered4 T
  · exact recovered5 T
  · exact recovered6 T
  · exact recovered7 T
  · exact recovered8 T
  · exact recovered9 T
  · exact recovered10 T
  · exact recovered11 T
  · exact recovered12 T
  · exact recovered13 T
  · exact recovered14 T
  · exact recovered15 T
  · exact recovered16 T
  · exact recovered17 T
  · exact recovered18 T
  · exact recovered19 T
  · exact recovered20 T
  · exact recovered21 T
  · exact recovered22 T
  · exact recovered23 T
  · exact recovered24 T
end Aris4Math.ThirtyFour.TwentyFiveNineLowTenthInventory

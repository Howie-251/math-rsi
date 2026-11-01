import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows0Batch0
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows1Batch0
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows2Batch0
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows2Batch1
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows2Batch2
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows3Batch0
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows3Batch1
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows3Batch2
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows4Batch0
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows4Batch1
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows4Batch2
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows4Batch3
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows4Batch4
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows4Batch5
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows4Batch6
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows4Batch7
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows5Batch0
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows5Batch1
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows5Batch2
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows5Batch3
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows5Batch4
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows5Batch5
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows5Batch6
import Aris4Math.ThirtyFour.TwentyFiveNineLowTenthRows5Batch7
namespace Aris4Math.ThirtyFour.TwentyFiveNineLowTenthCoverage
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveUnitConditional TwentyFiveConditionalRows Aris4Math.K6Classification
set_option maxRecDepth 100000
set_option maxHeartbeats 0
export TwentyFiveNineLowTenthRowsData (base lastDegree degrees oldBig candidates)
theorem candidates_eq : ∀ g,(candidates g).toFinset=
  (pairCompletion (oldBig g)).filter (fun T => T.card≤4) := by decide +kernel
theorem candidates_complete (g : Fin 6) (T : Finset (Fin 9))
    (mem : T∈pairCompletion (oldBig g)) (small : T.card≤4) : T∈candidates g := by
  apply List.mem_toFinset.mp
  rw [candidates_eq]
  exact Finset.mem_filter.mpr ⟨mem,small⟩
theorem selected0 : TwentyFiveNineLowTenthRowsData.rows0.map Row.selected=choices (candidates 0) ∅ := by decide +kernel

def witnesses0 : List (Witness 10 25) := TwentyFiveNineLowTenthRowsData.rows0.map Row.witness

theorem checked0 : List.Forall₂
  (TwentyFiveUnitConditional.Checks (degrees 0) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees (oldBig 0))
  (choices (candidates 0) ∅) witnesses0 := by
  rw [← selected0]
  apply checked_rows
  simp only [TwentyFiveNineLowTenthRowsData.rows0,List.all_append,TwentyFiveNineLowTenthRows0Batch0.checked,Bool.true_and]
theorem selected1 : TwentyFiveNineLowTenthRowsData.rows1.map Row.selected=choices (candidates 1) ∅ := by decide +kernel

def witnesses1 : List (Witness 10 25) := TwentyFiveNineLowTenthRowsData.rows1.map Row.witness

theorem checked1 : List.Forall₂
  (TwentyFiveUnitConditional.Checks (degrees 1) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees (oldBig 1))
  (choices (candidates 1) ∅) witnesses1 := by
  rw [← selected1]
  apply checked_rows
  simp only [TwentyFiveNineLowTenthRowsData.rows1,List.all_append,TwentyFiveNineLowTenthRows1Batch0.checked,Bool.true_and]
theorem selected2 : TwentyFiveNineLowTenthRowsData.rows2.map Row.selected=choices (candidates 2) ∅ := by decide +kernel

def witnesses2 : List (Witness 10 25) := TwentyFiveNineLowTenthRowsData.rows2.map Row.witness

theorem checked2 : List.Forall₂
  (TwentyFiveUnitConditional.Checks (degrees 2) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees (oldBig 2))
  (choices (candidates 2) ∅) witnesses2 := by
  rw [← selected2]
  apply checked_rows
  simp only [TwentyFiveNineLowTenthRowsData.rows2,List.all_append,TwentyFiveNineLowTenthRows2Batch0.checked,TwentyFiveNineLowTenthRows2Batch1.checked,TwentyFiveNineLowTenthRows2Batch2.checked,Bool.true_and]
theorem selected3 : TwentyFiveNineLowTenthRowsData.rows3.map Row.selected=choices (candidates 3) ∅ := by decide +kernel

def witnesses3 : List (Witness 10 25) := TwentyFiveNineLowTenthRowsData.rows3.map Row.witness

theorem checked3 : List.Forall₂
  (TwentyFiveUnitConditional.Checks (degrees 3) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees (oldBig 3))
  (choices (candidates 3) ∅) witnesses3 := by
  rw [← selected3]
  apply checked_rows
  simp only [TwentyFiveNineLowTenthRowsData.rows3,List.all_append,TwentyFiveNineLowTenthRows3Batch0.checked,TwentyFiveNineLowTenthRows3Batch1.checked,TwentyFiveNineLowTenthRows3Batch2.checked,Bool.true_and]
theorem selected4 : TwentyFiveNineLowTenthRowsData.rows4.map Row.selected=choices (candidates 4) ∅ := by decide +kernel

def witnesses4 : List (Witness 10 25) := TwentyFiveNineLowTenthRowsData.rows4.map Row.witness

theorem checked4 : List.Forall₂
  (TwentyFiveUnitConditional.Checks (degrees 4) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees (oldBig 4))
  (choices (candidates 4) ∅) witnesses4 := by
  rw [← selected4]
  apply checked_rows
  simp only [TwentyFiveNineLowTenthRowsData.rows4,List.all_append,TwentyFiveNineLowTenthRows4Batch0.checked,TwentyFiveNineLowTenthRows4Batch1.checked,TwentyFiveNineLowTenthRows4Batch2.checked,TwentyFiveNineLowTenthRows4Batch3.checked,TwentyFiveNineLowTenthRows4Batch4.checked,TwentyFiveNineLowTenthRows4Batch5.checked,TwentyFiveNineLowTenthRows4Batch6.checked,TwentyFiveNineLowTenthRows4Batch7.checked,Bool.true_and]
theorem selected5 : TwentyFiveNineLowTenthRowsData.rows5.map Row.selected=choices (candidates 5) ∅ := by decide +kernel

def witnesses5 : List (Witness 10 25) := TwentyFiveNineLowTenthRowsData.rows5.map Row.witness

theorem checked5 : List.Forall₂
  (TwentyFiveUnitConditional.Checks (degrees 5) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees (oldBig 5))
  (choices (candidates 5) ∅) witnesses5 := by
  rw [← selected5]
  apply checked_rows
  simp only [TwentyFiveNineLowTenthRowsData.rows5,List.all_append,TwentyFiveNineLowTenthRows5Batch0.checked,TwentyFiveNineLowTenthRows5Batch1.checked,TwentyFiveNineLowTenthRows5Batch2.checked,TwentyFiveNineLowTenthRows5Batch3.checked,TwentyFiveNineLowTenthRows5Batch4.checked,TwentyFiveNineLowTenthRows5Batch5.checked,TwentyFiveNineLowTenthRows5Batch6.checked,TwentyFiveNineLowTenthRows5Batch7.checked,Bool.true_and]
def witnesses : Fin 6 → List (Witness 10 25) := ![witnesses0,witnesses1,witnesses2,witnesses3,witnesses4,witnesses5]
theorem checked (g : Fin 6) : List.Forall₂
  (TwentyFiveUnitConditional.Checks (degrees g) TwentyFiveNineLowTenthInventory.big TwentyFiveNineLowTenthInventory.degrees (oldBig g))
  (choices (candidates g) ∅) (witnesses g) := by
  fin_cases g
  · exact checked0
  · exact checked1
  · exact checked2
  · exact checked3
  · exact checked4
  · exact checked5
end Aris4Math.ThirtyFour.TwentyFiveNineLowTenthCoverage

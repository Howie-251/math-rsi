import Aris4Math.ThirtyFour.TwentyFiveEightLowTenthRows0Batch0
import Aris4Math.ThirtyFour.TwentyFiveEightLowTenthRows1Batch0
import Aris4Math.ThirtyFour.TwentyFiveEightLowTenthRows1Batch1
import Aris4Math.ThirtyFour.TwentyFiveEightLowTenthRows1Batch2
import Aris4Math.ThirtyFour.TwentyFiveEightLowTenthRows1Batch3
namespace Aris4Math.ThirtyFour.TwentyFiveEightLowTenthCoverage
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveConditionalBudgetRows TwentyFiveColoredActual
open Aris4Math.K6Classification
export TwentyFiveEightLowTenthRowsData (base oldBig candidates)
set_option maxRecDepth 100000
set_option maxHeartbeats 0
theorem candidates_eq : ∀ g,(candidates g).toFinset=
    (pairCompletion (oldBig g)).filter (fun T => T.card≤4) := by
  intro g
  rw [oldBig,TwentyFiveEightLowInventory.completion]
  fin_cases g <;> decide +kernel

theorem candidates_complete (g : Fin 2) (T : Finset (Fin 9))
    (mem : T∈pairCompletion (oldBig g)) (small : T.card≤4) : T∈candidates g := by
  apply List.mem_toFinset.mp
  rw [candidates_eq]
  exact Finset.mem_filter.mpr ⟨mem,small⟩
theorem selected0 : TwentyFiveEightLowTenthRowsData.rows0.map Row.selected=choices (candidates 0) ∅ := by decide +kernel
def witnesses0 : List (Witness 10 20) := TwentyFiveEightLowTenthRowsData.rows0.map (fun r => r.colored.witness)
theorem checked0 : List.Forall₂
    (TwentyFiveUnitConditional.Checks (standard 8) TwentyFiveEightLowTenthInventoryData.big (fun _ => standard 8) (oldBig 0))
    (choices (candidates 0) ∅) witnesses0 := by
  rw [← selected0]
  apply checked_rows
  simp only [TwentyFiveEightLowTenthRowsData.rows0,List.all_append,TwentyFiveEightLowTenthRows0Batch0.checked,Bool.true_and]
theorem selected1 : TwentyFiveEightLowTenthRowsData.rows1.map Row.selected=choices (candidates 1) ∅ := by decide +kernel
def witnesses1 : List (Witness 10 20) := TwentyFiveEightLowTenthRowsData.rows1.map (fun r => r.colored.witness)
theorem checked1 : List.Forall₂
    (TwentyFiveUnitConditional.Checks (standard 8) TwentyFiveEightLowTenthInventoryData.big (fun _ => standard 8) (oldBig 1))
    (choices (candidates 1) ∅) witnesses1 := by
  rw [← selected1]
  apply checked_rows
  simp only [TwentyFiveEightLowTenthRowsData.rows1,List.all_append,TwentyFiveEightLowTenthRows1Batch0.checked,TwentyFiveEightLowTenthRows1Batch1.checked,TwentyFiveEightLowTenthRows1Batch2.checked,TwentyFiveEightLowTenthRows1Batch3.checked,Bool.true_and]
def witnesses : Fin 2 → List (Witness 10 20) := ![witnesses0,witnesses1]
theorem checked (g : Fin 2) : List.Forall₂
    (TwentyFiveUnitConditional.Checks (standard 8) TwentyFiveEightLowTenthInventoryData.big (fun _ => standard 8) (oldBig g))
    (choices (candidates g) ∅) (witnesses g) := by
  fin_cases g
  · exact checked0
  · exact checked1
end Aris4Math.ThirtyFour.TwentyFiveEightLowTenthCoverage

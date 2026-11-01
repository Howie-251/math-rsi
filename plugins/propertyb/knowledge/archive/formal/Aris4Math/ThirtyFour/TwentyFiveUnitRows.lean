import Aris4Math.ThirtyFour.TwentyFiveUnitCatalogue
namespace Aris4Math.ThirtyFour.TwentyFiveUnitRows
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue
variable {n m : ℕ}

structure Row (n m : ℕ) where
  selected : Finset (Finset (Fin n))
  witness : Witness (n+1) m

theorem checked_rows (catalogue : Fin m → Finset (Finset (Fin (n+1))))
    (big : Finset (Finset (Fin n))) (rows : List (Row n m))
    (checked : rows.all (fun r => decide (Checks catalogue big r.selected r.witness))=true) :
    List.Forall₂ (Checks catalogue big) (rows.map Row.selected) (rows.map Row.witness) := by
  induction rows with
  | nil => exact .nil
  | cons r rest ih =>
    simp only [List.all_cons,Bool.and_eq_true,decide_eq_true_eq] at checked
    exact .cons checked.1 (ih checked.2)

end Aris4Math.ThirtyFour.TwentyFiveUnitRows

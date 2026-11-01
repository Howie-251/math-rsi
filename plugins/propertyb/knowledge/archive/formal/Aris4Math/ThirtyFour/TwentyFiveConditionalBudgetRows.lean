import Aris4Math.ThirtyFour.TwentyFiveColoredRows
import Aris4Math.ThirtyFour.TwentyFiveUnitConditional

/-! Some degree-feasible tenth-lock extensions exceed the total edge budget.
These rows use the same exact inventory rejection as the colored catalogue. -/
namespace Aris4Math.ThirtyFour.TwentyFiveConditionalBudgetRows
open TwentyFiveUnitExtension TwentyFiveUnitCatalogue TwentyFiveColoredActual
variable {n m : ℕ}
structure Row (n m : ℕ) where
  selected : Finset (Finset (Fin n))
  colored : TwentyFiveColoredRows.Row (n+1) m

def Check (q : ℕ) (target : Fin m → Finset (Finset (Fin (n+1))))
    (big : Finset (Finset (Fin n))) (r : Row n m) : Prop :=
  extend big r.selected=r.colored.listed.toFinset ∧
    (∀ i,colors r.colored.low i=standard q i) ∧ TwentyFiveColoredRows.Check q target r.colored

instance (q : ℕ) (target : Fin m → Finset (Finset (Fin (n+1))))
    (big : Finset (Finset (Fin n))) (r : Row n m) : Decidable (Check q target big r) := by
  unfold Check
  infer_instance

theorem sound (q : ℕ) (target : Fin m → Finset (Finset (Fin (n+1))))
    (big : Finset (Finset (Fin n))) (r : Row n m) (checked : Check q target big r) :
    TwentyFiveUnitConditional.Checks (standard q) target (fun _ => standard q)
      big r.selected r.colored.witness := by
  intro feasible
  obtain ⟨same,degrees,valid⟩ := checked
  have degreeEq : colors r.colored.low=standard q := funext degrees
  rw [same,← degreeEq] at feasible
  obtain ⟨inj,moves,family⟩ := TwentyFiveColoredRows.direct_sound q target r.colored valid feasible
  refine ⟨inj,?_,?_⟩
  · simpa only [degreeEq] using moves
  · simpa only [same] using family

theorem checked_rows (q : ℕ) (target : Fin m → Finset (Finset (Fin (n+1))))
    (big : Finset (Finset (Fin n))) (rows : List (Row n m))
    (checked : rows.all (fun r => decide (Check q target big r))=true) :
    List.Forall₂ (TwentyFiveUnitConditional.Checks (standard q) target (fun _ => standard q) big)
      (rows.map Row.selected) (rows.map (fun r => r.colored.witness)) := by
  induction rows with
  | nil => exact .nil
  | cons r rest ih =>
    simp only [List.all_cons,Bool.and_eq_true,decide_eq_true_eq] at checked
    exact .cons (sound q target big r checked.1) (ih checked.2)
end Aris4Math.ThirtyFour.TwentyFiveConditionalBudgetRows

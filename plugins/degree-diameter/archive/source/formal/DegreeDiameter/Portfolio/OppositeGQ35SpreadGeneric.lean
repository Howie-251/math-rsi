import DegreeDiameter.Portfolio.SingleExtension
import Mathlib.Data.Fintype.Sum
namespace DegreeDiameter.Portfolio.OppositeGQSpread
open SimpleGraph
variable {P L V J : Type*}

/-- Exact opposite-incidence graph with a separate vertex for each spread line.
The old equivalence fixes the original old-vertex numbering. -/
def graph (e : V ≃ P × L) (Inc : P → L → Prop) (spread : J → L) : SimpleGraph (V ⊕ J) where
  Adj
    | .inl u, .inl v => u ≠ v ∧ Inc (e u).1 (e v).2 ∧ Inc (e v).1 (e u).2
    | .inl u, .inr j => Inc (e u).1 (e u).2 ∧ Inc (e u).1 (spread j)
    | .inr j, .inl u => Inc (e u).1 (e u).2 ∧ Inc (e u).1 (spread j)
    | .inr _, .inr _ => False
  symm := by
    intro u v h
    cases u <;> cases v
    · exact ⟨Ne.symm h.1,h.2.2,h.2.1⟩
    · exact h
    · exact h
    · exact h
  loopless := by intro u h; cases u; exact h.1 rfl; exact h

instance (e : V ≃ P × L) (Inc : P → L → Prop) (spread : J → L)
    [DecidableEq V] [DecidableRel Inc] : DecidableRel (graph e Inc spread).Adj := by
  intro u v
  cases u <;> cases v <;> simp only [graph] <;> infer_instance
end DegreeDiameter.Portfolio.OppositeGQSpread

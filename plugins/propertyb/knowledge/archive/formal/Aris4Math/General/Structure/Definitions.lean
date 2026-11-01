import Aris4Math.General.RS.Definitions
import Mathlib.Combinatorics.SimpleGraph.Clique

/-! Structural objects for the same original edge families as the RS core. -/
namespace Aris4Math.General.RS

universe u

def PairCovering {V : Type u} (E : Finset (Finset V)) : Prop :=
  ∀ x y : V, x ≠ y → ∃ e ∈ E, x ∈ e ∧ y ∈ e

def SingleIntersecting {V : Type u} [DecidableEq V]
    (E : Finset (Finset V)) : Prop :=
  ∀ e ∈ E, ∀ f ∈ E, e ≠ f → (e ∩ f).card = 1

/-- The public-point dichotomy bound, with no optional Gram-rank improvement. -/
def cliqueBudget (k v : ℕ) : ℕ := max (k * k - k + 1) ((v - 1) / (k - 1))

/-- Vertices are actual distinct original edges, not abstract edge profiles. -/
noncomputable def singleGraph {V : Type u} (E : Finset (Finset V)) :
    SimpleGraph {e : Finset V // e ∈ E} := by
  classical
  exact { Adj := fun e f => e ≠ f ∧ (e.val ∩ f.val).card = 1
          symm := by intro e f h; exact ⟨Ne.symm h.1, by simpa [Finset.inter_comm] using h.2⟩
          loopless := by intro e h; exact h.1 rfl }

end Aris4Math.General.RS

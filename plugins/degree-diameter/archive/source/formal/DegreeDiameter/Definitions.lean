import Mathlib.Combinatorics.SimpleGraph.Finite

/-!
Original specification for the degree/diameter (8,2) problem.
No regularity, connectivity, nonemptiness, or structural hypothesis is added.
The distance condition explicitly requires genuine edges or a two-edge path.
-/
namespace DegreeDiameter

/-- Every vertex has degree at most eight. -/
noncomputable def degreeAtMostEight {V : Type*} [Fintype V]
    (G : SimpleGraph V) : Prop := by
  classical
  exact ∀ v, G.degree v ≤ 8

/-- Distinct vertices are joined by a genuine path of length one or two. -/
def diameterAtMostTwo {V : Type*} (G : SimpleGraph V) : Prop :=
  ∀ u v, u ≠ v → G.Adj u v ∨ ∃ w, G.Adj u w ∧ G.Adj w v

/-- There exists a finite simple graph of order `n` satisfying the original bounds. -/
def Exists82 (n : ℕ) : Prop :=
  ∃ (V : Type) (_ : Fintype V) (G : SimpleGraph V),
    Fintype.card V = n ∧ degreeAtMostEight G ∧ diameterAtMostTwo G

/-- The exact extremal-order assertion: a realized lower bound and a universal upper bound. -/
def IsExact82 (n : ℕ) : Prop :=
  Exists82 n ∧ ∀ m, Exists82 m → m ≤ n

end DegreeDiameter

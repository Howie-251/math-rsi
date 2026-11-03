import DegreeDiameter.Portfolio.FullNeighborhoodClones
import DegreeDiameter.Portfolio.OppositeGQ35SpreadGeneric
import Mathlib.Data.Fintype.EquivFin
namespace DegreeDiameter.Portfolio.OvoidSpreadCloneCapacity
variable {P L V J I : Type*}

/-- Product centers live in the fixed original opposite-incidence source.
No evolving neighborhood, center-independence or injectivity condition is used. -/
def center (e : V ≃ P × L) (ovoid : I → P) (spread : J → L) (ij : I × J) : V ⊕ J :=
  .inl (e.symm (ovoid ij.1,spread ij.2))

theorem adjacent_centers_unique (e : V ≃ P × L) (Inc : P → L → Prop)
    (ovoid : I → P) (spread : J → L)
    (hO : ∀ l i i', Inc (ovoid i) l → Inc (ovoid i') l → i = i')
    (hS : ∀ p j j', Inc p (spread j) → Inc p (spread j') → j = j')
    (w : V ⊕ J) (x y : I × J)
    (hx : (OppositeGQSpread.graph e Inc spread).Adj w (center e ovoid spread x))
    (hy : (OppositeGQSpread.graph e Inc spread).Adj w (center e ovoid spread y)) : x = y := by
  cases w with
  | inl v =>
    simp only [center,OppositeGQSpread.graph,Equiv.apply_symm_apply] at hx hy
    exact Prod.ext (hO (e v).2 x.1 y.1 hx.2.2 hy.2.2)
      (hS (e v).1 x.2 y.2 hx.2.1 hy.2.1)
  | inr k =>
    simp only [center,OppositeGQSpread.graph,Equiv.apply_symm_apply] at hx hy
    have hix := hS (ovoid x.1) x.2 k hx.1 hx.2
    have hiy := hS (ovoid y.1) y.2 k hy.1 hy.2
    exact Prod.ext (hO (spread k) x.1 y.1 hx.2 hy.2) (hix.trans hiy.symm)

theorem load_le_one [Fintype V] [Fintype J] [Fintype I]
    [DecidableEq V] (e : V ≃ P × L) (Inc : P → L → Prop) [DecidableRel Inc]
    (ovoid : I → P) (spread : J → L)
    (hO : ∀ l i i', Inc (ovoid i) l → Inc (ovoid i') l → i = i')
    (hS : ∀ p j j', Inc p (spread j) → Inc p (spread j') → j = j') (w : V ⊕ J) :
    FullNeighborhoodClones.load (OppositeGQSpread.graph e Inc spread) (center e ovoid spread) w ≤ 1 := by
  unfold FullNeighborhoodClones.load
  apply Fintype.card_le_one_iff.mpr
  intro x y
  apply Subtype.ext
  exact adjacent_centers_unique e Inc ovoid spread hO hS w x.val y.val x.property y.property
#print axioms adjacent_centers_unique
#print axioms load_le_one
end DegreeDiameter.Portfolio.OvoidSpreadCloneCapacity

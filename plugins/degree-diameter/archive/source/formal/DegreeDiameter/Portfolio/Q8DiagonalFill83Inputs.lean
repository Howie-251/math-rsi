import DegreeDiameter.Portfolio.Q8DiagonalFill83Definitions
import DegreeDiameter.Portfolio.Q8DiagonalFillInputs
namespace DegreeDiameter.Portfolio.Q8DiagonalFill83
theorem adjacent_roles_unique (v : Source.Vertex) (x y : Role)
    (hx : Source.graph.Adj v (center x)) (hy : Source.graph.Adj v (center y)) : x=y := by
  cases v with
  | inl v => cases v with
    | inl v => cases v with
      | inl v =>
        have base : ∀a b : {c:CloneIndex // Q8DiagonalFill.raw.Adj v (Q8DiagonalFill.center c)},a=b :=
          Fintype.card_le_one_iff.mp (Q8DiagonalFill.load_le_one v)
        cases x with
        | inl c => cases y with
          | inl d => exact congrArg Sum.inl (congrArg Subtype.val (base ⟨c,hx⟩ ⟨d,hy⟩))
          | inr u => exact False.elim hy
        | inr u => exact False.elim hx
      | inr j => cases x with
        | inl c => exact False.elim hx
        | inr u => cases y with
          | inl d => exact False.elim hy
          | inr w => cases u;cases w;rfl
    | inr c => cases x <;> exact False.elim hx
  | inr u => cases x <;> exact False.elim hx
theorem load_le_one (v : Source.Vertex) : FullNeighborhoodClones.load Source.graph center v≤1 := by
  unfold FullNeighborhoodClones.load
  apply Fintype.card_le_one_iff.mpr
  intro x y
  apply Subtype.ext
  exact adjacent_roles_unique v x.val y.val x.property y.property
#print axioms adjacent_roles_unique
#print axioms load_le_one
end DegreeDiameter.Portfolio.Q8DiagonalFill83

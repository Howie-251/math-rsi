import DegreeDiameter.N62RepeatComponentBounds

#check @DegreeDiameter.n62_repeat_component_defect_row
#check @DegreeDiameter.n62_repeat_component_size_even
#check @DegreeDiameter.n62_repeat_component_size_ge_four
#check @DegreeDiameter.n62_repeat_quotient_reverse_positive
#check @DegreeDiameter.n62_repeat_quotient_budget_term_nonnegative
#check @DegreeDiameter.n62_repeat_quotient_budget
#check @DegreeDiameter.n62_repeat_component_size_ge_internal_square_sub_two
#print axioms DegreeDiameter.n62_repeat_component_defect_row
#print axioms DegreeDiameter.n62_repeat_component_size_even
#print axioms DegreeDiameter.n62_repeat_component_size_ge_four
#print axioms DegreeDiameter.n62_repeat_quotient_reverse_positive
#print axioms DegreeDiameter.n62_repeat_quotient_budget_term_nonnegative
#print axioms DegreeDiameter.n62_repeat_quotient_budget
#print axioms DegreeDiameter.n62_repeat_component_size_ge_internal_square_sub_two

open DegreeDiameter
open scoped BigOperators
attribute [local instance] Classical.propDecidable

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (C : (repeatSupport G).ConnectedComponent) :
    Even (repeatComponentVertices G C).card :=
  n62_repeat_component_size_even G hdeg hdiam hcard C

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62)
    (hbound : ∀ x y, defectMatrix G x y ≤ 2)
    (C : (repeatSupport G).ConnectedComponent) :
    4 ≤ (repeatComponentVertices G C).card :=
  n62_repeat_component_size_ge_four G hdeg hdiam hcard hbound C

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (C : (repeatSupport G).ConnectedComponent) :
    (∀ D, 0 ≤ repeatQuotientMatrix G C D * (repeatQuotientMatrix G D C - 1)) ∧
    (∑ D, repeatQuotientMatrix G C D * (repeatQuotientMatrix G D C - 1) =
      (repeatComponentSize G C : ℤ) + 2 - repeatQuotientMatrix G C C) ∧
    repeatQuotientMatrix G C C ^ 2 - 2 ≤ (repeatComponentSize G C : ℤ) :=
  ⟨n62_repeat_quotient_budget_term_nonnegative G hdeg hdiam hcard C,
    n62_repeat_quotient_budget G hdeg hdiam hcard C,
    n62_repeat_component_size_ge_internal_square_sub_two G hdeg hdiam hcard C⟩

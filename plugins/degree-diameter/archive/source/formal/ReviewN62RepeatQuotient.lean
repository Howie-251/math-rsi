import DegreeDiameter.N62RepeatQuotient

#print DegreeDiameter.repeatComponentSize
#print DegreeDiameter.repeatMembershipMatrix
#print DegreeDiameter.repeatSizeMatrix
#print DegreeDiameter.repeatQuotientMatrix
#check @DegreeDiameter.repeat_membership_mul
#check @DegreeDiameter.repeat_component_indicator_sum
#check @DegreeDiameter.repeat_component_indicator_card
#check @DegreeDiameter.n62_adjacency_repeat_membership
#check @DegreeDiameter.n62_defect_repeat_membership
#check @DegreeDiameter.n62_repeat_quotient_quadratic
#check @DegreeDiameter.n62_repeat_quotient_row_sum
#check @DegreeDiameter.n62_repeat_component_sizes_sum
#check @DegreeDiameter.n62_repeat_quotient_balance
#check @DegreeDiameter.repeat_quotient_nonnegative
#check @DegreeDiameter.repeat_component_size_pos
#print axioms DegreeDiameter.repeat_membership_mul
#print axioms DegreeDiameter.repeat_component_indicator_sum
#print axioms DegreeDiameter.repeat_component_indicator_card
#print axioms DegreeDiameter.n62_adjacency_repeat_membership
#print axioms DegreeDiameter.n62_defect_repeat_membership
#print axioms DegreeDiameter.n62_repeat_quotient_quadratic
#print axioms DegreeDiameter.n62_repeat_quotient_row_sum
#print axioms DegreeDiameter.n62_repeat_component_sizes_sum
#print axioms DegreeDiameter.n62_repeat_quotient_balance
#print axioms DegreeDiameter.repeat_quotient_nonnegative
#print axioms DegreeDiameter.repeat_component_size_pos

open DegreeDiameter Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) :
    repeatQuotientMatrix G * repeatQuotientMatrix G + repeatQuotientMatrix G =
      (10 : ℤ) • (1 : Matrix (repeatSupport G).ConnectedComponent
        (repeatSupport G).ConnectedComponent ℤ) + repeatSizeMatrix G :=
  n62_repeat_quotient_quadratic G hdeg hdiam hcard

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (C D : (repeatSupport G).ConnectedComponent) :
    (∑ E, repeatQuotientMatrix G C E = 8) ∧
    ((repeatComponentSize G C : ℤ) * repeatQuotientMatrix G C D =
      (repeatComponentSize G D : ℤ) * repeatQuotientMatrix G D C) :=
  ⟨n62_repeat_quotient_row_sum G hdeg hdiam hcard C,
    n62_repeat_quotient_balance G hdeg hdiam hcard C D⟩

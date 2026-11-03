import DegreeDiameter.N62RepeatQuotientTrace

#print DegreeDiameter.centeredRepeatQuotient
#check @DegreeDiameter.cubic_157604_trace_mod_1063
#check @DegreeDiameter.n62_repeat_size_matrix_square
#check @DegreeDiameter.n62_repeat_quotient_size_actions
#check @DegreeDiameter.n62_centered_repeat_quotient_cubic
#check @DegreeDiameter.n62_repeat_quotient_trace_bounds
#check @DegreeDiameter.n62_repeat_component_count_le
#check @DegreeDiameter.n62_repeat_quotient_trace_identity
#check @DegreeDiameter.n62_repeat_component_count_odd
#print axioms DegreeDiameter.cubic_157604_trace_mod_1063
#print axioms DegreeDiameter.n62_repeat_size_matrix_square
#print axioms DegreeDiameter.n62_repeat_quotient_size_actions
#print axioms DegreeDiameter.n62_centered_repeat_quotient_cubic
#print axioms DegreeDiameter.n62_repeat_quotient_trace_bounds
#print axioms DegreeDiameter.n62_repeat_component_count_le
#print axioms DegreeDiameter.n62_repeat_quotient_trace_identity
#print axioms DegreeDiameter.n62_repeat_component_count_odd

open DegreeDiameter Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) :
    (Fintype.card (repeatSupport G).ConnectedComponent : ℤ) +
      2 * trace (repeatQuotientMatrix G) = 17 :=
  n62_repeat_quotient_trace_identity G hdeg hdiam hcard

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) :
    Odd (Fintype.card (repeatSupport G).ConnectedComponent) :=
  n62_repeat_component_count_odd G hdeg hdiam hcard

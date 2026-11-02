import DegreeDiameter.N62RepeatComponentBudget

#check @DegreeDiameter.n62_repeat_component_weight_sum
#check @DegreeDiameter.n62_repeat_component_subset_budget
#check @DegreeDiameter.n62_no_six_components_three_internal_two
#print axioms DegreeDiameter.n62_repeat_component_weight_sum
#print axioms DegreeDiameter.n62_repeat_component_subset_budget
#print axioms DegreeDiameter.n62_no_six_components_three_internal_two

open DegreeDiameter
open scoped BigOperators
attribute [local instance] Classical.propDecidable

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62)
    (S : Finset (repeatSupport G).ConnectedComponent) :
    (S.card : ℤ) + 2 * ∑ C ∈ S, repeatQuotientMatrix G C C ≤ 17 :=
  n62_repeat_component_subset_budget G hdeg hdiam hcard S

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62)
    (hc : 6 ≤ Fintype.card (repeatSupport G).ConnectedComponent)
    (S : Finset (repeatSupport G).ConnectedComponent) (hs : S.card = 3)
    (hd : ∀ C ∈ S, repeatQuotientMatrix G C C = 2) : False := by
  apply n62_no_six_components_three_internal_two G hdeg hdiam hcard hc S hs
  intro C hC
  exact le_of_eq (hd C hC).symm


import DegreeDiameter.N62DoubleParity

#print DegreeDiameter.doubleNonedgePairs
#print DegreeDiameter.doubleRepeatPairs
#print DegreeDiameter.nonedgePairs
#print DegreeDiameter.fourCycleFlags
#check @DegreeDiameter.n62_four_cycle_flags_even
#check @DegreeDiameter.n62_four_cycle_flag_incidence
#check @DegreeDiameter.n62_double_repeat_incidence
#check @DegreeDiameter.n62_double_nonedge_pair_count_odd
#check @DegreeDiameter.n62_double_repeat_pairs_eq_nonedge_pairs
#check @DegreeDiameter.n62_double_repeat_pair_count_odd
#print axioms DegreeDiameter.n62_four_cycle_flags_even
#print axioms DegreeDiameter.n62_four_cycle_flag_incidence
#print axioms DegreeDiameter.n62_double_repeat_incidence
#print axioms DegreeDiameter.n62_double_nonedge_pair_count_odd
#print axioms DegreeDiameter.n62_double_repeat_pairs_eq_nonedge_pairs
#print axioms DegreeDiameter.n62_double_repeat_pair_count_odd

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : DegreeDiameter.degreeAtMostEight G)
    (hdiam : DegreeDiameter.diameterAtMostTwo G)
    (hcard : Fintype.card V = 62)
    (hbound : ∀ x y, DegreeDiameter.defectMatrix G x y ≤ 2) :
    Odd (DegreeDiameter.doubleRepeatPairs G).card :=
  DegreeDiameter.n62_double_repeat_pair_count_odd G hdeg hdiam hcard hbound

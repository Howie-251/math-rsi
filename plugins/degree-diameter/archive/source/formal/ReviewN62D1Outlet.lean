import DegreeDiameter.N62D1Outlet

#print DegreeDiameter.doublePairMate
#print DegreeDiameter.D1MatchParentTemplate
#print DegreeDiameter.DoubleRootParentData
#check @DegreeDiameter.closedDoubleFour_pair_mates
#check @DegreeDiameter.n62_double_pair_mate_properties
#check @DegreeDiameter.n62_double_repeat_pairs_even_of_no_d1
#check @DegreeDiameter.n62_exists_d1_match_parent
#print axioms DegreeDiameter.closedDoubleFour_pair_mates
#print axioms DegreeDiameter.n62_double_pair_mate_properties
#print axioms DegreeDiameter.n62_double_repeat_pairs_even_of_no_d1
#print axioms DegreeDiameter.n62_exists_d1_match_parent

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : DegreeDiameter.degreeAtMostEight G)
    (hdiam : DegreeDiameter.diameterAtMostTwo G)
    (hcard : Fintype.card V = 62)
    (hbound : ∀ x y, DegreeDiameter.defectMatrix G x y ≤ 2) :
    ∃ r w a, DegreeDiameter.D1MatchParentTemplate G r w a :=
  DegreeDiameter.n62_exists_d1_match_parent G hdeg hdiam hcard hbound

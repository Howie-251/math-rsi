import DegreeDiameter.N62D2

#print DegreeDiameter.D2MatchTemplate
#print DegreeDiameter.twoOneRow
#print DegreeDiameter.d2Class
#check @DegreeDiameter.n62_d2_four_rows
#check @DegreeDiameter.n62_two_nonadj_repeats_zero_triangle
#check @DegreeDiameter.n62_d2_named_zero_triangles
#check @DegreeDiameter.two_one_row_mul_adjacency
#check @DegreeDiameter.defect_neighbor_le_commuted
#check @DegreeDiameter.n62_d2_third_repeat_in_class
#check @DegreeDiameter.n62_d2_k_repeat_zero_on_two_neighborhoods
#check @DegreeDiameter.d2_neighborhoods
#check @DegreeDiameter.n62_d2_class_sizes
#check @DegreeDiameter.d2_classes_disjoint
#check @DegreeDiameter.n62_d2_class_commutation
#check @DegreeDiameter.d2_class_parent
#check @DegreeDiameter.n62_d2_class_repeat_weights
#check @DegreeDiameter.n62_d2_class_support
#check @DegreeDiameter.n62_d2_class_neighbor_counts
#check @DegreeDiameter.no_n62_d2_match_template
#print axioms DegreeDiameter.n62_d2_four_rows
#print axioms DegreeDiameter.n62_two_nonadj_repeats_zero_triangle
#print axioms DegreeDiameter.n62_d2_named_zero_triangles
#print axioms DegreeDiameter.two_one_row_mul_adjacency
#print axioms DegreeDiameter.defect_neighbor_le_commuted
#print axioms DegreeDiameter.n62_d2_third_repeat_in_class
#print axioms DegreeDiameter.n62_d2_k_repeat_zero_on_two_neighborhoods
#print axioms DegreeDiameter.d2_neighborhoods
#print axioms DegreeDiameter.n62_d2_class_sizes
#print axioms DegreeDiameter.d2_classes_disjoint
#print axioms DegreeDiameter.n62_d2_class_commutation
#print axioms DegreeDiameter.d2_class_parent
#print axioms DegreeDiameter.n62_d2_class_repeat_weights
#print axioms DegreeDiameter.n62_d2_class_support
#print axioms DegreeDiameter.n62_d2_class_neighbor_counts
#print axioms DegreeDiameter.no_n62_d2_match_template

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : DegreeDiameter.degreeAtMostEight G)
    (hdiam : DegreeDiameter.diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r i j k w a : V}
    (h : DegreeDiameter.D2MatchTemplate G r i j k w a) : False :=
  DegreeDiameter.no_n62_d2_match_template G hdeg hdiam hcard h

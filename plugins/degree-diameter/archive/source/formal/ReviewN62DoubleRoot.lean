import DegreeDiameter.N62DoubleRoot

#print DegreeDiameter.rootParents
#print DegreeDiameter.DoubleRootParentData
#print DegreeDiameter.D1MatchParentTemplate
#check @DegreeDiameter.n62_double_endpoint_zero_triangle
#check @DegreeDiameter.n62_double_root_normal_form
#check @DegreeDiameter.double_root_edge_parents_disjoint
#check @DegreeDiameter.n62_double_root_overlap_classification
#check @DegreeDiameter.double_root_overlap_two_template
#check @DegreeDiameter.n62_double_root_overlap_two_impossible
#check @DegreeDiameter.n62_double_root_d0_or_d1
#check @DegreeDiameter.double_root_disjoint_parent_template
#check @DegreeDiameter.n62_double_root_template_coverage
#check @DegreeDiameter.n62_double_root_d0_match_closed
#check @DegreeDiameter.n62_d0_edge_closed_from_parents
#check @DegreeDiameter.n62_double_root_d1_or_closed_component
#print axioms DegreeDiameter.n62_double_endpoint_zero_triangle
#print axioms DegreeDiameter.n62_double_root_normal_form
#print axioms DegreeDiameter.double_root_edge_parents_disjoint
#print axioms DegreeDiameter.n62_double_root_overlap_classification
#print axioms DegreeDiameter.double_root_overlap_two_template
#print axioms DegreeDiameter.n62_double_root_overlap_two_impossible
#print axioms DegreeDiameter.n62_double_root_d0_or_d1
#print axioms DegreeDiameter.double_root_disjoint_parent_template
#print axioms DegreeDiameter.n62_double_root_template_coverage
#print axioms DegreeDiameter.n62_double_root_d0_match_closed
#print axioms DegreeDiameter.n62_d0_edge_closed_from_parents
#print axioms DegreeDiameter.n62_double_root_d1_or_closed_component

open DegreeDiameter
example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r w : V} (hb : defectMatrix G r w = 2) :
    ∃ a, DoubleRootParentData G r w a ∧ twoOneRow G r w a ∧
      zeroTriangleVertex G r ∧ zeroTriangleVertex G w :=
  n62_double_root_normal_form G hdeg hdiam hcard hb

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {r w : V} (hb : defectMatrix G r w = 2) :
    (∃ a, D1MatchParentTemplate G r w a) ∨ (∃ a b, ClosedDoubleFour G r w b a) :=
  n62_double_root_d1_or_closed_component G hdeg hdiam hcard hb

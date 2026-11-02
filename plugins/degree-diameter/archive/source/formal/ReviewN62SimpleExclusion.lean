import DegreeDiameter.N62SimpleExclusion

#print DegreeDiameter.defectMatrix
#print DegreeDiameter.unitNonedgePairs
#print SimpleGraph.cliqueFinset
#check @DegreeDiameter.n62_simple_repeat_incidence
#check @DegreeDiameter.no_n62_simple_defect_graph
#print axioms DegreeDiameter.n62_simple_repeat_incidence
#print axioms DegreeDiameter.no_n62_simple_defect_graph

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : DegreeDiameter.degreeAtMostEight G)
    (hdiam : DegreeDiameter.diameterAtMostTwo G)
    (hcard : Fintype.card V = 62)
    (hsimple : ∀ x y, DegreeDiameter.defectMatrix G x y ≤ 1) : False :=
  DegreeDiameter.no_n62_simple_defect_graph G hdeg hdiam hcard hsimple

import DegreeDiameter.N62RepeatComponents

#print DegreeDiameter.repeatSupport
#print DegreeDiameter.repeatComponentVertices
#print DegreeDiameter.repeatComponentIndicator
#print DegreeDiameter.repeatComponentNeighborCount
#print DegreeDiameter.repeatComponentDegree
#print DegreeDiameter.repeatQuotientMatrix
#check @DegreeDiameter.n62_repeat_support_adj_iff
#check @DegreeDiameter.integer_weighted_harmonic_edge_eq
#check @DegreeDiameter.n62_repeat_harmonic_constant
#check @DegreeDiameter.mem_repeatComponentVertices
#check @DegreeDiameter.n62_repeat_component_indicator_harmonic
#check @DegreeDiameter.adjacency_mul_repeat_indicator
#check @DegreeDiameter.n62_repeat_component_neighbor_count_harmonic
#check @DegreeDiameter.n62_repeat_components_equitable
#check @DegreeDiameter.n62_repeat_component_degree_spec
#check @DegreeDiameter.n62_repeat_component_internal_degree
#print axioms DegreeDiameter.n62_repeat_support_adj_iff
#print axioms DegreeDiameter.integer_weighted_harmonic_edge_eq
#print axioms DegreeDiameter.n62_repeat_harmonic_constant
#print axioms DegreeDiameter.mem_repeatComponentVertices
#print axioms DegreeDiameter.n62_repeat_component_indicator_harmonic
#print axioms DegreeDiameter.adjacency_mul_repeat_indicator
#print axioms DegreeDiameter.n62_repeat_component_neighbor_count_harmonic
#print axioms DegreeDiameter.n62_repeat_components_equitable
#print axioms DegreeDiameter.n62_repeat_component_degree_spec
#print axioms DegreeDiameter.n62_repeat_component_internal_degree

open DegreeDiameter
attribute [local instance] Classical.propDecidable
example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (C D : (repeatSupport G).ConnectedComponent)
    {x y : V} (hx : x ∈ D.supp) (hy : y ∈ D.supp) :
    ((G.neighborFinset x).filter (fun z => z ∈ C.supp)).card =
      ((G.neighborFinset y).filter (fun z => z ∈ C.supp)).card :=
  n62_repeat_components_equitable G hdeg hdiam hcard C D hx hy

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (D C : (repeatSupport G).ConnectedComponent)
    {x : V} (hx : x ∈ D.supp) :
    (((G.neighborFinset x).filter (fun z => z ∈ C.supp)).card : ℤ) =
      repeatQuotientMatrix G D C := by
  have hh := n62_repeat_component_degree_spec G hdeg hdiam hcard D C hx
  exact congrArg (fun n : ℕ => (n : ℤ)) hh

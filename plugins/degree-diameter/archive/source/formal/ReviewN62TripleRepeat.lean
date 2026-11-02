import DegreeDiameter.N62TripleRepeat

#print DegreeDiameter.commonNeighborVertices
#check @DegreeDiameter.mem_commonNeighborVertices
#check @DegreeDiameter.n62_triple_repeat_rows
#check @DegreeDiameter.n62_triple_repeat_nonadj
#check @DegreeDiameter.n62_triple_endpoint_zero_triangle
#check @DegreeDiameter.n62_triple_common_card
#check @DegreeDiameter.n62_triple_common_nonadj
#check @DegreeDiameter.n62_triple_common_rows
#check @DegreeDiameter.n62_triple_common_pair_neighbors
#check @DegreeDiameter.n62_triple_outside_common_neighbors_unique
#check @DegreeDiameter.n62_triple_pair_component
#check @DegreeDiameter.n62_triple_common_component
#check @DegreeDiameter.n62_triple_component_sizes
#print axioms DegreeDiameter.mem_commonNeighborVertices
#print axioms DegreeDiameter.n62_triple_repeat_rows
#print axioms DegreeDiameter.n62_triple_repeat_nonadj
#print axioms DegreeDiameter.n62_triple_endpoint_zero_triangle
#print axioms DegreeDiameter.n62_triple_common_card
#print axioms DegreeDiameter.n62_triple_common_nonadj
#print axioms DegreeDiameter.n62_triple_common_rows
#print axioms DegreeDiameter.n62_triple_common_pair_neighbors
#print axioms DegreeDiameter.n62_triple_outside_common_neighbors_unique
#print axioms DegreeDiameter.n62_triple_pair_component
#print axioms DegreeDiameter.n62_triple_common_component
#print axioms DegreeDiameter.n62_triple_component_sizes

open DegreeDiameter
attribute [local instance] Classical.propDecidable

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (u v : V) (hb : defectMatrix G u v = 3) :
    zeroTriangleVertex G u ∧ zeroTriangleVertex G v ∧
    ((G.neighborFinset u).filter (fun x => G.Adj x v)).card = 4 := by
  have hvu : defectMatrix G v u = 3 := by rw [(defect_symmetric G).apply u v,hb]
  exact ⟨n62_triple_endpoint_zero_triangle G hdeg hdiam hcard hb,
    n62_triple_endpoint_zero_triangle G hdeg hdiam hcard hvu,
    n62_triple_common_card G hdeg hdiam hcard hb⟩

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (u v : V) (hb : defectMatrix G u v = 3) :
    ∀ x ∈ commonNeighborVertices G u v, ∀ y,
      defectMatrix G x y = if y ∈ commonNeighborVertices G u v ∧ y ≠ x then 1 else 0 := by
  intro x hx
  exact n62_triple_common_rows G hdeg hdiam hcard hb hx

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (u v : V) (hb : defectMatrix G u v = 3) :
    repeatComponentSize G ((repeatSupport G).connectedComponentMk u) = 2 ∧
    ∃ C : (repeatSupport G).ConnectedComponent,
      repeatComponentVertices G C = commonNeighborVertices G u v ∧ repeatComponentSize G C = 4 :=
  n62_triple_component_sizes G hdeg hdiam hcard hb

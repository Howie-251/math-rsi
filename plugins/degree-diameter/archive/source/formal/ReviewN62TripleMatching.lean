import DegreeDiameter.N62TripleMatching

#print DegreeDiameter.tripleExclusiveNeighbors
#check @DegreeDiameter.mem_tripleExclusiveNeighbors
#check @DegreeDiameter.commonNeighborVertices_comm
#check @DegreeDiameter.triple_exclusive_disjoint
#check @DegreeDiameter.triple_exclusive_common_disjoint
#check @DegreeDiameter.n62_triple_exclusive_endpoints
#check @DegreeDiameter.n62_triple_exclusive_card
#check @DegreeDiameter.n62_triple_exclusive_independent
#check @DegreeDiameter.n62_triple_exclusive_common_nonadj
#check @DegreeDiameter.n62_triple_exclusive_opposite_common_card
#check @DegreeDiameter.n62_triple_cross_neighbors_eq
#check @DegreeDiameter.n62_triple_cross_degree_one
#check @DegreeDiameter.n62_triple_exclusive_unique_neighbor
#check @DegreeDiameter.tripleExclusiveMate
#check @DegreeDiameter.tripleExclusiveMate_adj
#check @DegreeDiameter.tripleMatchingEquiv
#check @DegreeDiameter.tripleMatchingEquiv_adj_iff
#check @DegreeDiameter.n62_triple_exclusive_six_remaining
#print axioms DegreeDiameter.mem_tripleExclusiveNeighbors
#print axioms DegreeDiameter.commonNeighborVertices_comm
#print axioms DegreeDiameter.triple_exclusive_disjoint
#print axioms DegreeDiameter.triple_exclusive_common_disjoint
#print axioms DegreeDiameter.n62_triple_exclusive_endpoints
#print axioms DegreeDiameter.n62_triple_exclusive_card
#print axioms DegreeDiameter.n62_triple_exclusive_independent
#print axioms DegreeDiameter.n62_triple_exclusive_common_nonadj
#print axioms DegreeDiameter.n62_triple_exclusive_opposite_common_card
#print axioms DegreeDiameter.n62_triple_cross_neighbors_eq
#print axioms DegreeDiameter.n62_triple_cross_degree_one
#print axioms DegreeDiameter.n62_triple_exclusive_unique_neighbor
#print axioms DegreeDiameter.tripleExclusiveMate
#print axioms DegreeDiameter.tripleExclusiveMate_adj
#print axioms DegreeDiameter.tripleMatchingEquiv
#print axioms DegreeDiameter.tripleMatchingEquiv_adj_iff
#print axioms DegreeDiameter.n62_triple_exclusive_six_remaining

open DegreeDiameter
attribute [local instance] Classical.propDecidable

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (u v : V) (hb : defectMatrix G u v = 3) :
    (tripleExclusiveNeighbors G u v).card = 4 ∧ (tripleExclusiveNeighbors G v u).card = 4 ∧
    Disjoint (tripleExclusiveNeighbors G u v) (tripleExclusiveNeighbors G v u) ∧
    Disjoint (tripleExclusiveNeighbors G u v) (commonNeighborVertices G u v) ∧
    Disjoint (tripleExclusiveNeighbors G v u) (commonNeighborVertices G u v) := by
  have hvu : defectMatrix G v u = 3 := by rw [(defect_symmetric G).apply u v,hb]
  refine ⟨n62_triple_exclusive_card G hdeg hdiam hcard hb,
    n62_triple_exclusive_card G hdeg hdiam hcard hvu,
    triple_exclusive_disjoint G u v,triple_exclusive_common_disjoint G u v,?_⟩
  rw [commonNeighborVertices_comm G u v]
  exact triple_exclusive_common_disjoint G v u

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (u v : V) (hb : defectMatrix G u v = 3) :
    (u ∉ tripleExclusiveNeighbors G u v ∧ v ∉ tripleExclusiveNeighbors G u v) ∧
    (v ∉ tripleExclusiveNeighbors G v u ∧ u ∉ tripleExclusiveNeighbors G v u) ∧
    (∀ x ∈ tripleExclusiveNeighbors G u v, ∃! y, y ∈ tripleExclusiveNeighbors G v u ∧ G.Adj x y) ∧
    (∀ y ∈ tripleExclusiveNeighbors G v u, ∃! x, x ∈ tripleExclusiveNeighbors G u v ∧ G.Adj y x) := by
  have hvu : defectMatrix G v u = 3 := by rw [(defect_symmetric G).apply u v,hb]
  exact ⟨n62_triple_exclusive_endpoints G hdeg hdiam hcard hb,
    n62_triple_exclusive_endpoints G hdeg hdiam hcard hvu,
    fun _ hx => n62_triple_exclusive_unique_neighbor G hdeg hdiam hcard hb hx,
    fun _ hy => n62_triple_exclusive_unique_neighbor G hdeg hdiam hcard hvu hy⟩

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (u v : V) (hb : defectMatrix G u v = 3) :
    ∃ e : {x // x ∈ tripleExclusiveNeighbors G u v} ≃ {y // y ∈ tripleExclusiveNeighbors G v u},
      ∀ (x : {x // x ∈ tripleExclusiveNeighbors G u v})
        (y : {y // y ∈ tripleExclusiveNeighbors G v u}), G.Adj (x : V) (y : V) ↔ e x = y :=
  ⟨tripleMatchingEquiv G hdeg hdiam hcard hb,tripleMatchingEquiv_adj_iff G hdeg hdiam hcard hb⟩

#check @DegreeDiameter.n62_triple_exclusive_remaining_outside
#check @DegreeDiameter.n62_triple_exclusive_exterior_card
#print axioms DegreeDiameter.n62_triple_exclusive_remaining_outside
#print axioms DegreeDiameter.n62_triple_exclusive_exterior_card

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (u v : V) (hb : defectMatrix G u v = 3)
    (x : {x // x ∈ tripleExclusiveNeighbors G u v}) :
    ((G.neighborFinset x).filter (fun z => z ≠ u ∧ z ≠ v ∧
      z ∉ commonNeighborVertices G u v ∧ z ∉ tripleExclusiveNeighbors G u v ∧
      z ∉ tripleExclusiveNeighbors G v u)).card = 6 :=
  n62_triple_exclusive_exterior_card G hdeg hdiam hcard hb x

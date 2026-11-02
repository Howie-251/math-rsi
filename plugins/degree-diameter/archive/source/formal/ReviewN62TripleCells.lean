import DegreeDiameter.N62TripleCells

#check @DegreeDiameter.n62_triple_exclusive_repeat_sum
#print axioms DegreeDiameter.n62_triple_exclusive_repeat_sum
#check @DegreeDiameter.n62_triple_exclusive_repeat_zero_outside
#print axioms DegreeDiameter.n62_triple_exclusive_repeat_zero_outside
#check @DegreeDiameter.n62_triple_exclusive_repeat_crosses
#print axioms DegreeDiameter.n62_triple_exclusive_repeat_crosses
#check @DegreeDiameter.mem_tripleOuterFiber
#print axioms DegreeDiameter.mem_tripleOuterFiber
#check @DegreeDiameter.mem_tripleOuterVertices
#print axioms DegreeDiameter.mem_tripleOuterVertices
#check @DegreeDiameter.n62_triple_outer_fiber_card
#print axioms DegreeDiameter.n62_triple_outer_fiber_card
#check @DegreeDiameter.n62_triple_outer_fibers_disjoint
#print axioms DegreeDiameter.n62_triple_outer_fibers_disjoint
#check @DegreeDiameter.n62_triple_outer_card
#print axioms DegreeDiameter.n62_triple_outer_card
#check @DegreeDiameter.n62_triple_outer_outside
#print axioms DegreeDiameter.n62_triple_outer_outside
#check @DegreeDiameter.n62_triple_common_degree_endpoints
#print axioms DegreeDiameter.n62_triple_common_degree_endpoints
#check @DegreeDiameter.n62_triple_outer_common_degree
#print axioms DegreeDiameter.n62_triple_outer_common_degree
#check @DegreeDiameter.n62_triple_outer_iff_common_degree_one
#print axioms DegreeDiameter.n62_triple_outer_iff_common_degree_one
#check @DegreeDiameter.n62_triple_common_degree_repeat_eq
#print axioms DegreeDiameter.n62_triple_common_degree_repeat_eq
#check @DegreeDiameter.n62_triple_outer_repeat_closed
#print axioms DegreeDiameter.n62_triple_outer_repeat_closed
#check @DegreeDiameter.n62_triple_exclusive_union_card
#print axioms DegreeDiameter.n62_triple_exclusive_union_card
#check @DegreeDiameter.n62_triple_exclusive_union_repeat_closed
#print axioms DegreeDiameter.n62_triple_exclusive_union_repeat_closed
#check @DegreeDiameter.mem_tripleInnerVertices
#print axioms DegreeDiameter.mem_tripleInnerVertices
#check @DegreeDiameter.n62_triple_inner_card
#print axioms DegreeDiameter.n62_triple_inner_card
#check @DegreeDiameter.n62_triple_inner_repeat_closed
#print axioms DegreeDiameter.n62_triple_inner_repeat_closed
#check @DegreeDiameter.n62_triple_inner_outer_disjoint
#print axioms DegreeDiameter.n62_triple_inner_outer_disjoint
#check @DegreeDiameter.mem_tripleRemainingVertices
#print axioms DegreeDiameter.mem_tripleRemainingVertices
#check @DegreeDiameter.n62_triple_remaining_card
#print axioms DegreeDiameter.n62_triple_remaining_card
#check @DegreeDiameter.n62_triple_remaining_repeat_closed
#print axioms DegreeDiameter.n62_triple_remaining_repeat_closed

open DegreeDiameter
open scoped BigOperators
attribute [local instance] Classical.propDecidable

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (u v : V) (hb : defectMatrix G u v = 3) :
    (∀ x ∈ tripleExclusiveNeighbors G u v,
      ∑ y ∈ tripleExclusiveNeighbors G v u, defectMatrix G x y = 3) ∧
    (∀ x ∈ tripleExclusiveNeighbors G u v, ∀ y, 0 < defectMatrix G x y →
      y ∈ tripleExclusiveNeighbors G v u) ∧
    (∀ y ∈ tripleExclusiveNeighbors G v u, ∀ x, 0 < defectMatrix G y x →
      x ∈ tripleExclusiveNeighbors G u v) := by
  have hvu : defectMatrix G v u = 3 := by rw [(defect_symmetric G).apply u v,hb]
  exact ⟨fun _ hx => n62_triple_exclusive_repeat_sum G hdeg hdiam hcard hb hx,
    fun _ hx _ hxy => n62_triple_exclusive_repeat_crosses G hdeg hdiam hcard hb hx hxy,
    fun _ hy _ hyx => n62_triple_exclusive_repeat_crosses G hdeg hdiam hcard hvu hy hyx⟩

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (u v : V) (hb : defectMatrix G u v = 3) :
    (commonNeighborVertices G u v).card = 4 ∧
    (tripleExclusiveVertices G u v).card = 8 ∧
    (tripleOuterVertices G u v).card = 24 ∧
    (tripleRemainingVertices G u v).card = 24 ∧
    Disjoint (tripleInnerVertices G u v) (tripleOuterVertices G u v) :=
  ⟨n62_triple_common_card G hdeg hdiam hcard hb,
    n62_triple_exclusive_union_card G hdeg hdiam hcard hb,
    n62_triple_outer_card G hdeg hdiam hcard hb,
    n62_triple_remaining_card G hdeg hdiam hcard hb,
    n62_triple_inner_outer_disjoint G hdeg hdiam hcard hb⟩

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (u v : V) (hb : defectMatrix G u v = 3) :
    (∀ x ∈ tripleExclusiveVertices G u v, ∀ y, 0 < defectMatrix G x y →
      y ∈ tripleExclusiveVertices G u v) ∧
    (∀ x ∈ tripleOuterVertices G u v, ∀ y, 0 < defectMatrix G x y →
      y ∈ tripleOuterVertices G u v) ∧
    (∀ x ∈ tripleRemainingVertices G u v, ∀ y, 0 < defectMatrix G x y →
      y ∈ tripleRemainingVertices G u v) :=
  ⟨fun _ hx _ hxy => n62_triple_exclusive_union_repeat_closed G hdeg hdiam hcard hb hx hxy,
    fun _ hx _ hxy => n62_triple_outer_repeat_closed G hdeg hdiam hcard hb hx hxy,
    fun _ hx _ hxy => n62_triple_remaining_repeat_closed G hdeg hdiam hcard hb hx hxy⟩

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (u v : V) (hb : defectMatrix G u v = 3) :
    ∀ x, x ∈ tripleOuterVertices G u v ↔
      ((G.neighborFinset x).filter (fun s => s ∈ commonNeighborVertices G u v)).card = 1 :=
  fun _ => n62_triple_outer_iff_common_degree_one G hdeg hdiam hcard hb

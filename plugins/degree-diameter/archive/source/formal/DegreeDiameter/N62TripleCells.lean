import DegreeDiameter.N62TripleMatching

namespace DegreeDiameter
open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- Commutation and an actual saturated endpoint row force repeat row sum three into the opposite exclusive side. -/
theorem n62_triple_exclusive_repeat_sum (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ tripleExclusiveNeighbors G u v) :
    ∑ y ∈ tripleExclusiveNeighbors G v u, defectMatrix G x y = 3 := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hux := ((mem_tripleExclusiveNeighbors G u v x).mp hx).1
  have hr := (n62_triple_repeat_rows G hdeg hdiam hcard hb).2
  have hBA : (defectMatrix G * adjacencyMatrix G) v x = 3 := by
    simp [adjacencyMatrix,SimpleGraph.mul_adjMatrix_apply,hr,hux.symm]
  have hAB := congrArg (fun M => M v x) (adjacency_defect_commute G hreg)
  dsimp only at hAB
  rw [hBA] at hAB
  change (G.adjMatrix ℤ * defectMatrix G) v x = 3 at hAB
  rw [SimpleGraph.adjMatrix_mul_apply] at hAB
  have hxn : x ∉ commonNeighborVertices G u v := by
    intro hxs
    exact (Finset.disjoint_left.mp (triple_exclusive_common_disjoint G u v)) hx hxs
  have hzero {y : V} (hy : y ∈ commonNeighborVertices G u v) : defectMatrix G x y = 0 := by
    rw [← (defect_symmetric G).apply x y,n62_triple_common_rows G hdeg hdiam hcard hb hy]
    simp [hxn]
  calc
    _ = ∑ y ∈ G.neighborFinset v, defectMatrix G x y := by
      apply Finset.sum_subset (Finset.sdiff_subset (s := G.neighborFinset v))
      intro y hy hny
      apply hzero
      have hvy : G.Adj v y := by simpa using hy
      apply (mem_commonNeighborVertices G u v y).mpr
      refine ⟨?_,hvy⟩
      by_contra huy
      exact hny ((mem_tripleExclusiveNeighbors G v u y).mpr ⟨hvy,huy⟩)
    _ = ∑ y ∈ G.neighborFinset v, defectMatrix G y x := by
      apply Finset.sum_congr rfl
      intro y _
      exact ((defect_symmetric G).apply x y).symm
    _ = 3 := hAB

/-- The entire actual repeat row of an exclusive vertex is supported on the opposite side. -/
theorem n62_triple_exclusive_repeat_zero_outside (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x y : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ tripleExclusiveNeighbors G u v) (hy : y ∉ tripleExclusiveNeighbors G v u) :
    defectMatrix G x y = 0 := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have he := Finset.sum_sdiff (f := defectMatrix G x)
    (Finset.subset_univ (tripleExclusiveNeighbors G v u))
  have hs := n62_triple_exclusive_repeat_sum G hdeg hdiam hcard hb hx
  have hr : ∑ z, defectMatrix G x z = 3 := by simpa [hcard] using defect_row_sum G hreg x
  have hz : ∑ z ∈ Finset.univ \ tripleExclusiveNeighbors G v u, defectMatrix G x z = 0 := by omega
  exact (Finset.sum_eq_zero_iff_of_nonneg
    (fun z _ => defect_nonnegative G hreg hdiam x z)).mp hz y (by simp [hy])

/-- Every positive actual repeat from an exclusive vertex crosses to the opposite exclusive side. -/
theorem n62_triple_exclusive_repeat_crosses (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x y : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ tripleExclusiveNeighbors G u v) (hxy : 0 < defectMatrix G x y) :
    y ∈ tripleExclusiveNeighbors G v u := by
  by_contra hy
  rw [n62_triple_exclusive_repeat_zero_outside G hdeg hdiam hcard hb hx hy] at hxy
  omega

/-- Six original neighbors belonging to one common-neighbor vertex, with the triple endpoints removed. -/
def tripleOuterFiber (G : SimpleGraph V) (u v s : V) : Finset V :=
  G.neighborFinset s \ {u,v}

@[simp] theorem mem_tripleOuterFiber (G : SimpleGraph V) (u v s z : V) :
    z ∈ tripleOuterFiber G u v s ↔ G.Adj s z ∧ z ≠ u ∧ z ≠ v := by
  simp [tripleOuterFiber,not_or]

/-- The actual union of the six-neighbor fibers over the common-neighbor four-set. -/
def tripleOuterVertices (G : SimpleGraph V) (u v : V) : Finset V :=
  (commonNeighborVertices G u v).biUnion (tripleOuterFiber G u v)

@[simp] theorem mem_tripleOuterVertices (G : SimpleGraph V) (u v z : V) :
    z ∈ tripleOuterVertices G u v ↔
      ∃ s ∈ commonNeighborVertices G u v, G.Adj s z ∧ z ≠ u ∧ z ≠ v := by
  simp [tripleOuterVertices]

/-- Each actual outer fiber has six vertices. -/
theorem n62_triple_outer_fiber_card (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v s : V} (hb : defectMatrix G u v = 3)
    (hs : s ∈ commonNeighborVertices G u v) : (tripleOuterFiber G u v s).card = 6 := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have huv := (n62_triple_repeat_nonadj G hdeg hdiam hcard hb).1
  have hs' := (mem_commonNeighborVertices G u v s).mp hs
  have hsub : ({u,v} : Finset V) ⊆ G.neighborFinset s := by
    intro z hz
    rcases Finset.mem_insert.mp hz with hzu | hzv
    · subst z; simpa using hs'.1.symm
    · have he := Finset.mem_singleton.mp hzv
      subst z; simpa using hs'.2.symm
  rw [tripleOuterFiber,Finset.card_sdiff_of_subset hsub,SimpleGraph.card_neighborFinset_eq_degree,hreg s]
  simp [huv]

/-- Distinct common-neighbor vertices have disjoint actual outer fibers. -/
theorem n62_triple_outer_fibers_disjoint (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    (commonNeighborVertices G u v : Set V).PairwiseDisjoint (tripleOuterFiber G u v) := by
  intro s hs t ht hst
  apply Finset.disjoint_left.mpr
  intro z hzs hzt
  have hz1 := (mem_tripleOuterFiber G u v s z).mp hzs
  have hz2 := (mem_tripleOuterFiber G u v t z).mp hzt
  exact hst (n62_triple_outside_common_neighbors_unique G hdeg hdiam hcard hb
    hz1.2.1 hz1.2.2 hs ht hz1.1.symm hz2.1.symm)

/-- The actual outer union U has 24 vertices. -/
theorem n62_triple_outer_card (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    (tripleOuterVertices G u v).card = 24 := by
  rw [tripleOuterVertices,Finset.card_biUnion (n62_triple_outer_fibers_disjoint G hdeg hdiam hcard hb)]
  calc
    _ = ∑ _s ∈ commonNeighborVertices G u v, 6 := by
      apply Finset.sum_congr rfl
      intro s hs
      exact n62_triple_outer_fiber_card G hdeg hdiam hcard hb hs
    _ = 24 := by simp [n62_triple_common_card G hdeg hdiam hcard hb]

/-- U is disjoint from both endpoints, the common four-set, and both exclusive sides. -/
theorem n62_triple_outer_outside (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z : V} (hb : defectMatrix G u v = 3)
    (hz : z ∈ tripleOuterVertices G u v) :
    z ≠ u ∧ z ≠ v ∧ z ∉ commonNeighborVertices G u v ∧
      z ∉ tripleExclusiveNeighbors G u v ∧ z ∉ tripleExclusiveNeighbors G v u := by
  obtain ⟨s,hs,hsz,hzu,hzv⟩ := (mem_tripleOuterVertices G u v z).mp hz
  refine ⟨hzu,hzv,?_,?_,?_⟩
  · intro hzS
    exact n62_triple_common_nonadj G hdeg hdiam hcard hb hs hzS hsz
  · intro hzE
    exact n62_triple_exclusive_common_nonadj G hdeg hdiam hcard hb hzE hs hsz.symm
  · intro hzE
    have hvu : defectMatrix G v u = 3 := by rw [(defect_symmetric G).apply u v,hb]
    have hs' : s ∈ commonNeighborVertices G v u := by rw [commonNeighborVertices_comm]; exact hs
    exact n62_triple_exclusive_common_nonadj G hdeg hdiam hcard hvu hzE hs' hsz.symm

/-- The actual number of original neighbors in the common-neighbor four-set. -/
def tripleCommonDegree (G : SimpleGraph V) (u v z : V) : ℕ :=
  ((G.neighborFinset z).filter (fun s => s ∈ commonNeighborVertices G u v)).card

/-- Actual endpoint neighbor counts into S are four. -/
theorem n62_triple_common_degree_endpoints (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    tripleCommonDegree G u v u = 4 ∧ tripleCommonDegree G u v v = 4 := by
  have hu : (G.neighborFinset u).filter (fun s => s ∈ commonNeighborVertices G u v) = commonNeighborVertices G u v := by
    ext s
    simp only [Finset.mem_filter,SimpleGraph.mem_neighborFinset]
    exact ⟨And.right,fun hs => ⟨((mem_commonNeighborVertices G u v s).mp hs).1,hs⟩⟩
  have hv : (G.neighborFinset v).filter (fun s => s ∈ commonNeighborVertices G u v) = commonNeighborVertices G u v := by
    ext s
    simp only [Finset.mem_filter,SimpleGraph.mem_neighborFinset]
    exact ⟨And.right,fun hs => ⟨((mem_commonNeighborVertices G u v s).mp hs).2,hs⟩⟩
  simp only [tripleCommonDegree,hu,hv,n62_triple_common_card G hdeg hdiam hcard hb,and_self]

/-- Every U vertex has exactly one actual original neighbor in S. -/
theorem n62_triple_outer_common_degree (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z : V} (hb : defectMatrix G u v = 3)
    (hz : z ∈ tripleOuterVertices G u v) : tripleCommonDegree G u v z = 1 := by
  obtain ⟨s,hs,hsz,hzu,hzv⟩ := (mem_tripleOuterVertices G u v z).mp hz
  have he : (G.neighborFinset z).filter (fun t => t ∈ commonNeighborVertices G u v) = {s} := by
    ext t
    simp only [Finset.mem_filter,SimpleGraph.mem_neighborFinset,Finset.mem_singleton]
    constructor
    · rintro ⟨hzt,ht⟩
      exact n62_triple_outside_common_neighbors_unique G hdeg hdiam hcard hb hzu hzv ht hs hzt hsz.symm
    · intro ht
      subst t
      exact ⟨hsz.symm,hs⟩
  unfold tripleCommonDegree
  rw [he,Finset.card_singleton]

/-- The actual set U is exactly the level-one set of original neighbor count into S. -/
theorem n62_triple_outer_iff_common_degree_one (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z : V} (hb : defectMatrix G u v = 3) :
    z ∈ tripleOuterVertices G u v ↔ tripleCommonDegree G u v z = 1 := by
  constructor
  · exact n62_triple_outer_common_degree G hdeg hdiam hcard hb
  · intro hc
    have he := n62_triple_common_degree_endpoints G hdeg hdiam hcard hb
    have hzu : z ≠ u := by intro hz; subst z; omega
    have hzv : z ≠ v := by intro hz; subst z; omega
    obtain ⟨s,hs⟩ := Finset.card_pos.mp (show 0 <
      ((G.neighborFinset z).filter (fun s => s ∈ commonNeighborVertices G u v)).card by
        change 0 < tripleCommonDegree G u v z; omega)
    have hs' := Finset.mem_filter.mp hs
    have hzs : G.Adj z s := by simpa using hs'.1
    exact (mem_tripleOuterVertices G u v z).mpr ⟨s,hs'.2,hzs.symm,hzu,hzv⟩

/-- Actual repeat adjacency preserves actual original neighbor counts into S, via the proved component equitability. -/
theorem n62_triple_common_degree_repeat_eq (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x y : V} (hb : defectMatrix G u v = 3)
    (hxy : 0 < defectMatrix G x y) :
    tripleCommonDegree G u v x = tripleCommonDegree G u v y := by
  obtain ⟨s,hs⟩ := Finset.card_pos.mp (show 0 < (commonNeighborVertices G u v).card by
    rw [n62_triple_common_card G hdeg hdiam hcard hb]; decide)
  let C := (repeatSupport G).connectedComponentMk s
  have hC : repeatComponentVertices G C = commonNeighborVertices G u v :=
    n62_triple_common_component G hdeg hdiam hcard hb hs
  have hc (z : V) : repeatComponentNeighborCount G C z = tripleCommonDegree G u v z := by
    unfold repeatComponentNeighborCount tripleCommonDegree
    congr 1
    ext t
    simp only [Finset.mem_filter]
    rw [← mem_repeatComponentVertices G C t,hC]
  have ha := (n62_repeat_support_adj_iff G hdeg hdiam hcard x y).mpr hxy
  have hh := n62_repeat_components_equitable G hdeg hdiam hcard C
    ((repeatSupport G).connectedComponentMk x) (x := x) (y := y) (by rfl)
    (((repeatSupport G).connectedComponentMk x).mem_supp_of_adj_mem_supp (by rfl) ha)
  rw [hc,hc] at hh
  exact hh

/-- U is closed under every actual positive repeat entry. -/
theorem n62_triple_outer_repeat_closed (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x y : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ tripleOuterVertices G u v) (hxy : 0 < defectMatrix G x y) :
    y ∈ tripleOuterVertices G u v := by
  apply (n62_triple_outer_iff_common_degree_one G hdeg hdiam hcard hb).mpr
  rw [← n62_triple_common_degree_repeat_eq G hdeg hdiam hcard hb hxy]
  exact n62_triple_outer_common_degree G hdeg hdiam hcard hb hx

/-- The two actual exclusive sides together. -/
def tripleExclusiveVertices (G : SimpleGraph V) (u v : V) : Finset V :=
  tripleExclusiveNeighbors G u v ∪ tripleExclusiveNeighbors G v u

theorem n62_triple_exclusive_union_card (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    (tripleExclusiveVertices G u v).card = 8 := by
  have hvu : defectMatrix G v u = 3 := by rw [(defect_symmetric G).apply u v,hb]
  rw [tripleExclusiveVertices,Finset.card_union_of_disjoint (triple_exclusive_disjoint G u v),
    n62_triple_exclusive_card G hdeg hdiam hcard hb,
    n62_triple_exclusive_card G hdeg hdiam hcard hvu]

theorem n62_triple_exclusive_union_repeat_closed (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x y : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ tripleExclusiveVertices G u v) (hxy : 0 < defectMatrix G x y) :
    y ∈ tripleExclusiveVertices G u v := by
  rcases Finset.mem_union.mp hx with hx | hx
  · exact Finset.mem_union_right _ (n62_triple_exclusive_repeat_crosses G hdeg hdiam hcard hb hx hxy)
  · have hvu : defectMatrix G v u = 3 := by rw [(defect_symmetric G).apply u v,hb]
    exact Finset.mem_union_left _ (n62_triple_exclusive_repeat_crosses G hdeg hdiam hcard hvu hx hxy)

/-- The actual 14 vertices consisting of the endpoints and their original neighbors. -/
def tripleInnerVertices (G : SimpleGraph V) (u v : V) : Finset V :=
  {u,v} ∪ (G.neighborFinset u ∪ G.neighborFinset v)

theorem mem_tripleInnerVertices (G : SimpleGraph V) (u v z : V) :
    z ∈ tripleInnerVertices G u v ↔ z = u ∨ z = v ∨
      z ∈ commonNeighborVertices G u v ∨ z ∈ tripleExclusiveNeighbors G u v ∨
        z ∈ tripleExclusiveNeighbors G v u := by
  simp only [tripleInnerVertices,Finset.mem_union,Finset.mem_insert,Finset.mem_singleton,
    SimpleGraph.mem_neighborFinset,mem_commonNeighborVertices,mem_tripleExclusiveNeighbors]
  tauto

theorem n62_triple_inner_card (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    (tripleInnerVertices G u v).card = 14 := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  obtain ⟨huv,hn⟩ := n62_triple_repeat_nonadj G hdeg hdiam hcard hb
  have hI : G.neighborFinset u ∩ G.neighborFinset v = commonNeighborVertices G u v := by
    ext z
    simp only [Finset.mem_inter,SimpleGraph.mem_neighborFinset,mem_commonNeighborVertices]
  have hUnion : (G.neighborFinset u ∪ G.neighborFinset v).card = 12 := by
    rw [Finset.card_union,hI,SimpleGraph.card_neighborFinset_eq_degree,
      SimpleGraph.card_neighborFinset_eq_degree,hreg u,hreg v,
      n62_triple_common_card G hdeg hdiam hcard hb]
  have hd : Disjoint ({u,v} : Finset V) (G.neighborFinset u ∪ G.neighborFinset v) := by
    apply Finset.disjoint_left.mpr
    intro z hz hzn
    rcases Finset.mem_insert.mp hz with hzu | hzv
    · subst z
      simpa [hn,SimpleGraph.adj_comm] using hzn
    · have he := Finset.mem_singleton.mp hzv
      subst z
      simpa [hn,SimpleGraph.adj_comm] using hzn
  rw [tripleInnerVertices,Finset.card_union_of_disjoint hd,hUnion]
  simp [huv]

theorem n62_triple_inner_repeat_closed (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x y : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ tripleInnerVertices G u v) (hxy : 0 < defectMatrix G x y) :
    y ∈ tripleInnerVertices G u v := by
  apply (mem_tripleInnerVertices G u v y).mpr
  rcases (mem_tripleInnerVertices G u v x).mp hx with hxu | hxv | hxS | hxE | hxE
  · subst x
    rw [(n62_triple_repeat_rows G hdeg hdiam hcard hb).1 y] at hxy
    split_ifs at hxy with hy
    · exact Or.inr (Or.inl hy)
    · omega
  · subst x
    rw [(n62_triple_repeat_rows G hdeg hdiam hcard hb).2 y] at hxy
    split_ifs at hxy with hy
    · exact Or.inl hy
    · omega
  · rw [n62_triple_common_rows G hdeg hdiam hcard hb hxS y] at hxy
    split_ifs at hxy with hy
    · exact Or.inr (Or.inr (Or.inl hy.1))
    · omega
  · exact Or.inr (Or.inr (Or.inr (Or.inr
      (n62_triple_exclusive_repeat_crosses G hdeg hdiam hcard hb hxE hxy))))
  · have hvu : defectMatrix G v u = 3 := by rw [(defect_symmetric G).apply u v,hb]
    exact Or.inr (Or.inr (Or.inr (Or.inl
      (n62_triple_exclusive_repeat_crosses G hdeg hdiam hcard hvu hxE hxy))))

theorem n62_triple_inner_outer_disjoint (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    Disjoint (tripleInnerVertices G u v) (tripleOuterVertices G u v) := by
  apply Finset.disjoint_left.mpr
  intro z hzI hzU
  have hz := n62_triple_outer_outside G hdeg hdiam hcard hb hzU
  rcases (mem_tripleInnerVertices G u v z).mp hzI with h | h | h | h | h
  · exact hz.1 h
  · exact hz.2.1 h
  · exact hz.2.2.1 h
  · exact hz.2.2.2.1 h
  · exact hz.2.2.2.2 h

/-- The actual remaining vertices after the 14 inner and 24 outer vertices. -/
def tripleRemainingVertices (G : SimpleGraph V) (u v : V) : Finset V :=
  Finset.univ \ (tripleInnerVertices G u v ∪ tripleOuterVertices G u v)

@[simp] theorem mem_tripleRemainingVertices (G : SimpleGraph V) (u v z : V) :
    z ∈ tripleRemainingVertices G u v ↔
      z ∉ tripleInnerVertices G u v ∧ z ∉ tripleOuterVertices G u v := by
  simp [tripleRemainingVertices,not_or]

theorem n62_triple_remaining_card (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    (tripleRemainingVertices G u v).card = 24 := by
  rw [tripleRemainingVertices,Finset.card_sdiff_of_subset (Finset.subset_univ _),
    Finset.card_univ,hcard,
    Finset.card_union_of_disjoint (n62_triple_inner_outer_disjoint G hdeg hdiam hcard hb),
    n62_triple_inner_card G hdeg hdiam hcard hb,n62_triple_outer_card G hdeg hdiam hcard hb]

theorem n62_triple_remaining_repeat_closed (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x y : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ tripleRemainingVertices G u v) (hxy : 0 < defectMatrix G x y) :
    y ∈ tripleRemainingVertices G u v := by
  obtain ⟨hxI,hxU⟩ := (mem_tripleRemainingVertices G u v x).mp hx
  have hyx : 0 < defectMatrix G y x := by rw [(defect_symmetric G).apply x y]; exact hxy
  apply (mem_tripleRemainingVertices G u v y).mpr
  exact ⟨fun hy => hxI (n62_triple_inner_repeat_closed G hdeg hdiam hcard hb hy hyx),
    fun hy => hxU (n62_triple_outer_repeat_closed G hdeg hdiam hcard hb hy hyx)⟩

end
end DegreeDiameter

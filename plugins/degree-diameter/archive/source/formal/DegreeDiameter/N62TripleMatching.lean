import DegreeDiameter.N62TripleRepeat

namespace DegreeDiameter
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- Actual neighbors of u which are not common neighbors of u and v. -/
def tripleExclusiveNeighbors (G : SimpleGraph V) (u v : V) : Finset V :=
  G.neighborFinset u \ commonNeighborVertices G u v

@[simp] theorem mem_tripleExclusiveNeighbors (G : SimpleGraph V) (u v x : V) :
    x ∈ tripleExclusiveNeighbors G u v ↔ G.Adj u x ∧ ¬ G.Adj v x := by
  simp only [tripleExclusiveNeighbors,Finset.mem_sdiff,SimpleGraph.mem_neighborFinset,
    mem_commonNeighborVertices]
  constructor
  · rintro ⟨hu,hn⟩
    exact ⟨hu,fun hv => hn ⟨hu,hv⟩⟩
  · rintro ⟨hu,hn⟩
    exact ⟨hu,fun hv => hn hv.2⟩

/-- Actual common-neighbor sets are symmetric in the two endpoints. -/
theorem commonNeighborVertices_comm (G : SimpleGraph V) (u v : V) :
    commonNeighborVertices G u v = commonNeighborVertices G v u := by
  ext x
  simp only [mem_commonNeighborVertices,and_comm]

/-- The two actual exclusive-neighbor sets are disjoint. -/
theorem triple_exclusive_disjoint (G : SimpleGraph V) (u v : V) :
    Disjoint (tripleExclusiveNeighbors G u v) (tripleExclusiveNeighbors G v u) := by
  apply Finset.disjoint_left.mpr
  intro x hx hy
  exact ((mem_tripleExclusiveNeighbors G u v x).mp hx).2
    ((mem_tripleExclusiveNeighbors G v u x).mp hy).1

/-- Each actual exclusive-neighbor set is disjoint from the actual common-neighbor set. -/
theorem triple_exclusive_common_disjoint (G : SimpleGraph V) (u v : V) :
    Disjoint (tripleExclusiveNeighbors G u v) (commonNeighborVertices G u v) := by
  apply Finset.disjoint_left.mpr
  intro x hx hy
  exact ((mem_tripleExclusiveNeighbors G u v x).mp hx).2
    ((mem_commonNeighborVertices G u v x).mp hy).2

/-- Under an actual triple entry, neither endpoint is an exclusive neighbor. -/
theorem n62_triple_exclusive_endpoints (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    u ∉ tripleExclusiveNeighbors G u v ∧ v ∉ tripleExclusiveNeighbors G u v := by
  have hn := (n62_triple_repeat_nonadj G hdeg hdiam hcard hb).2
  constructor
  · intro hu
    exact G.irrefl ((mem_tripleExclusiveNeighbors G u v u).mp hu).1
  · intro hv
    exact hn ((mem_tripleExclusiveNeighbors G u v v).mp hv).1

/-- Each side of an actual triple pair has exactly four exclusive original neighbors. -/
theorem n62_triple_exclusive_card (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    (tripleExclusiveNeighbors G u v).card = 4 := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hs : commonNeighborVertices G u v ⊆ G.neighborFinset u := by
    intro x hx
    simpa only [SimpleGraph.mem_neighborFinset] using ((mem_commonNeighborVertices G u v x).mp hx).1
  rw [tripleExclusiveNeighbors,Finset.card_sdiff_of_subset hs,
    SimpleGraph.card_neighborFinset_eq_degree,hreg u,n62_triple_common_card G hdeg hdiam hcard hb]

/-- Each exclusive side is independent in the original graph. -/
theorem n62_triple_exclusive_independent (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x y : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ tripleExclusiveNeighbors G u v) (hy : y ∈ tripleExclusiveNeighbors G u v) :
    ¬ G.Adj x y :=
  n62_triple_endpoint_zero_triangle G hdeg hdiam hcard hb x y
    ((mem_tripleExclusiveNeighbors G u v x).mp hx).1
    ((mem_tripleExclusiveNeighbors G u v y).mp hy).1

/-- There are no original edges from either exclusive side to the common-neighbor four-set. -/
theorem n62_triple_exclusive_common_nonadj (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x y : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ tripleExclusiveNeighbors G u v) (hy : y ∈ commonNeighborVertices G u v) :
    ¬ G.Adj x y :=
  n62_triple_endpoint_zero_triangle G hdeg hdiam hcard hb x y
    ((mem_tripleExclusiveNeighbors G u v x).mp hx).1
    ((mem_commonNeighborVertices G u v y).mp hy).1

/-- An exclusive neighbor and the opposite triple endpoint have exactly one actual common neighbor. -/
theorem n62_triple_exclusive_opposite_common_card (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ tripleExclusiveNeighbors G u v) :
    (commonNeighborVertices G x v).card = 1 := by
  have hx' := (mem_tripleExclusiveNeighbors G u v x).mp hx
  have hxv : x ≠ v := by
    intro he
    subst x
    exact (n62_triple_exclusive_endpoints G hdeg hdiam hcard hb).2 hx
  have hxu : x ≠ u := hx'.1.ne'
  have hbx : defectMatrix G x v = 0 := by
    rw [← (defect_symmetric G).apply x v,
      (n62_triple_repeat_rows G hdeg hdiam hcard hb).2 x,if_neg hxu]
  have hnxv : ¬ G.Adj x v := fun ha => hx'.2 ha.symm
  have he := defect_off_diagonal G hxv
  simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply,if_neg hnxv] at he
  change commonNeighborCount G x v = 1
  omega

/-- Actual opposite-endpoint common neighbors are exactly original neighbors in the opposite exclusive side. -/
theorem n62_triple_cross_neighbors_eq (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ tripleExclusiveNeighbors G u v) :
    (G.neighborFinset x).filter (fun y => y ∈ tripleExclusiveNeighbors G v u) =
      commonNeighborVertices G x v := by
  have hux := ((mem_tripleExclusiveNeighbors G u v x).mp hx).1
  ext y
  simp only [Finset.mem_filter,SimpleGraph.mem_neighborFinset,mem_tripleExclusiveNeighbors,
    mem_commonNeighborVertices]
  constructor
  · exact fun h => ⟨h.1,h.2.1⟩
  · rintro ⟨hxy,hvy⟩
    refine ⟨hxy,hvy,?_⟩
    intro huy
    exact n62_triple_endpoint_zero_triangle G hdeg hdiam hcard hb x y hux huy hxy

/-- Actual cross degree is one at every vertex on either side of the triple pair. -/
theorem n62_triple_cross_degree_one (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ tripleExclusiveNeighbors G u v) :
    ((G.neighborFinset x).filter (fun y => y ∈ tripleExclusiveNeighbors G v u)).card = 1 := by
  rw [n62_triple_cross_neighbors_eq G hdeg hdiam hcard hb hx,
    n62_triple_exclusive_opposite_common_card G hdeg hdiam hcard hb hx]

/-- An exclusive vertex has a unique actual original-graph neighbor on the opposite exclusive side. -/
theorem n62_triple_exclusive_unique_neighbor (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ tripleExclusiveNeighbors G u v) :
    ∃! y, y ∈ tripleExclusiveNeighbors G v u ∧ G.Adj x y := by
  obtain ⟨y,hy⟩ := Finset.card_eq_one.mp (n62_triple_cross_degree_one G hdeg hdiam hcard hb hx)
  have hym : y ∈ (G.neighborFinset x).filter (fun z => z ∈ tripleExclusiveNeighbors G v u) := by
    rw [hy]
    simp
  refine ⟨y,?_,?_⟩
  · simpa only [Finset.mem_filter,SimpleGraph.mem_neighborFinset,and_comm] using hym
  · intro z hz
    have hzm : z ∈ (G.neighborFinset x).filter (fun z => z ∈ tripleExclusiveNeighbors G v u) := by
      exact Finset.mem_filter.mpr ⟨by simpa using hz.2,hz.1⟩
    rw [hy] at hzm
    exact Finset.mem_singleton.mp hzm

/-- The actual matching mate, selected from the proved unique original neighbor. -/
def tripleExclusiveMate (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3)
    (x : {x // x ∈ tripleExclusiveNeighbors G u v}) : {y // y ∈ tripleExclusiveNeighbors G v u} :=
  ⟨Classical.choose (n62_triple_exclusive_unique_neighbor G hdeg hdiam hcard hb x.property).exists,
    (Classical.choose_spec (n62_triple_exclusive_unique_neighbor G hdeg hdiam hcard hb x.property).exists).1⟩

theorem tripleExclusiveMate_adj (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3)
    (x : {x // x ∈ tripleExclusiveNeighbors G u v}) :
    G.Adj x (tripleExclusiveMate G hdeg hdiam hcard hb x) :=
  (Classical.choose_spec (n62_triple_exclusive_unique_neighbor G hdeg hdiam hcard hb x.property).exists).2

/-- The original edges between the two actual four-sets construct a perfect matching equivalence. -/
def tripleMatchingEquiv (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    {x // x ∈ tripleExclusiveNeighbors G u v} ≃ {y // y ∈ tripleExclusiveNeighbors G v u} := by
  have hvu : defectMatrix G v u = 3 := by rw [(defect_symmetric G).apply u v,hb]
  refine { toFun := tripleExclusiveMate G hdeg hdiam hcard hb
           invFun := tripleExclusiveMate G hdeg hdiam hcard hvu
           left_inv := ?_
           right_inv := ?_ }
  · intro x
    apply Subtype.ext
    apply (n62_triple_exclusive_unique_neighbor G hdeg hdiam hcard hvu
      (tripleExclusiveMate G hdeg hdiam hcard hb x).property).unique
    · exact ⟨Subtype.property _,tripleExclusiveMate_adj G hdeg hdiam hcard hvu _⟩
    · exact ⟨x.property,(tripleExclusiveMate_adj G hdeg hdiam hcard hb x).symm⟩
  · intro y
    apply Subtype.ext
    apply (n62_triple_exclusive_unique_neighbor G hdeg hdiam hcard hb
      (tripleExclusiveMate G hdeg hdiam hcard hvu y).property).unique
    · exact ⟨Subtype.property _,tripleExclusiveMate_adj G hdeg hdiam hcard hb _⟩
    · exact ⟨y.property,(tripleExclusiveMate_adj G hdeg hdiam hcard hvu y).symm⟩

/-- The constructed equivalence describes exactly the actual cross-side original edges. -/
theorem tripleMatchingEquiv_adj_iff (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3)
    (x : {x // x ∈ tripleExclusiveNeighbors G u v})
    (y : {y // y ∈ tripleExclusiveNeighbors G v u}) :
    G.Adj x y ↔ tripleMatchingEquiv G hdeg hdiam hcard hb x = y := by
  change G.Adj x y ↔ tripleExclusiveMate G hdeg hdiam hcard hb x = y
  constructor
  · intro hxy
    apply Subtype.ext
    exact (n62_triple_exclusive_unique_neighbor G hdeg hdiam hcard hb x.property).unique
      ⟨Subtype.property _,tripleExclusiveMate_adj G hdeg hdiam hcard hb x⟩ ⟨y.property,hxy⟩
  · intro he
    rw [← he]
    exact tripleExclusiveMate_adj G hdeg hdiam hcard hb x

/-- After its endpoint and actual matching mate, an exclusive vertex has six remaining original neighbors. -/
theorem n62_triple_exclusive_six_remaining (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3)
    (x : {x // x ∈ tripleExclusiveNeighbors G u v}) :
    (G.neighborFinset x \ {u,(tripleExclusiveMate G hdeg hdiam hcard hb x : V)}).card = 6 := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hux := ((mem_tripleExclusiveNeighbors G u v x).mp x.property).1
  have hxy := tripleExclusiveMate_adj G hdeg hdiam hcard hb x
  have hne : u ≠ (tripleExclusiveMate G hdeg hdiam hcard hb x : V) := by
    intro he
    have hm := (tripleExclusiveMate G hdeg hdiam hcard hb x).property
    rw [← he] at hm
    have hvu : defectMatrix G v u = 3 := by rw [(defect_symmetric G).apply u v,hb]
    exact (n62_triple_exclusive_endpoints G hdeg hdiam hcard hvu).2 hm
  have hs : ({u,(tripleExclusiveMate G hdeg hdiam hcard hb x : V)} : Finset V) ⊆ G.neighborFinset x := by
    intro z hz
    rcases Finset.mem_insert.mp hz with hzu | hz
    · subst z; simpa using hux.symm
    · have hz' := Finset.mem_singleton.mp hz
      subst z
      simpa using hxy
  rw [Finset.card_sdiff_of_subset hs,SimpleGraph.card_neighborFinset_eq_degree,hreg x]
  simp [hne]

/-- The six remaining neighbors lie outside both endpoints, the common four-set, and both exclusive sides. -/
theorem n62_triple_exclusive_remaining_outside (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z : V} (hb : defectMatrix G u v = 3)
    (x : {x // x ∈ tripleExclusiveNeighbors G u v})
    (hz : z ∈ G.neighborFinset x \ {u,(tripleExclusiveMate G hdeg hdiam hcard hb x : V)}) :
    z ≠ u ∧ z ≠ v ∧ z ∉ commonNeighborVertices G u v ∧
      z ∉ tripleExclusiveNeighbors G u v ∧ z ∉ tripleExclusiveNeighbors G v u := by
  have hh := Finset.mem_sdiff.mp hz
  have haz : G.Adj x z := by simpa using hh.1
  refine ⟨?_,?_,?_,?_,?_⟩
  · intro he; exact hh.2 (by simp [he])
  · intro he
    subst z
    exact ((mem_tripleExclusiveNeighbors G u v x).mp x.property).2 haz.symm
  · intro hs
    exact n62_triple_exclusive_common_nonadj G hdeg hdiam hcard hb x.property hs haz
  · intro hs
    exact n62_triple_exclusive_independent G hdeg hdiam hcard hb x.property hs haz
  · intro hs
    have he := (n62_triple_exclusive_unique_neighbor G hdeg hdiam hcard hb x.property).unique
      ⟨hs,haz⟩ ⟨(tripleExclusiveMate G hdeg hdiam hcard hb x).property,
        tripleExclusiveMate_adj G hdeg hdiam hcard hb x⟩
    exact hh.2 (by simp [he])

/-- Exactly six original neighbors of an exclusive vertex lie outside the three already constructed cells. -/
theorem n62_triple_exclusive_exterior_card (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3)
    (x : {x // x ∈ tripleExclusiveNeighbors G u v}) :
    ((G.neighborFinset x).filter (fun z => z ≠ u ∧ z ≠ v ∧
      z ∉ commonNeighborVertices G u v ∧ z ∉ tripleExclusiveNeighbors G u v ∧
      z ∉ tripleExclusiveNeighbors G v u)).card = 6 := by
  have heq : (G.neighborFinset x).filter (fun z => z ≠ u ∧ z ≠ v ∧
      z ∉ commonNeighborVertices G u v ∧ z ∉ tripleExclusiveNeighbors G u v ∧
      z ∉ tripleExclusiveNeighbors G v u) =
      G.neighborFinset x \ {u,(tripleExclusiveMate G hdeg hdiam hcard hb x : V)} := by
    ext z
    simp only [Finset.mem_filter,Finset.mem_sdiff,SimpleGraph.mem_neighborFinset]
    constructor
    · rintro ⟨haz,hzu,hzv,hzS,hzp,hzm⟩
      refine ⟨haz,?_⟩
      simp only [Finset.mem_insert,Finset.mem_singleton]
      rintro (he | he)
      · exact hzu he
      · subst z
        exact hzm (tripleExclusiveMate G hdeg hdiam hcard hb x).property
    · rintro ⟨haz,hn⟩
      refine ⟨haz,n62_triple_exclusive_remaining_outside G hdeg hdiam hcard hb x ?_⟩
      exact Finset.mem_sdiff.mpr ⟨by simpa using haz,hn⟩
  rw [heq,n62_triple_exclusive_six_remaining G hdeg hdiam hcard hb x]

end
end DegreeDiameter

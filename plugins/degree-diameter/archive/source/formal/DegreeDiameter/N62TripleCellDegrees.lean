import DegreeDiameter.N62TripleCells

namespace DegreeDiameter
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- Actual original-neighbor count into an actual finite vertex set. -/
def tripleCellDegree (G : SimpleGraph V) (C : Finset V) (z : V) : ℕ :=
  (C.filter (G.Adj z)).card

theorem tripleCellDegree_eq_neighbor_filter (G : SimpleGraph V) (C : Finset V) (z : V) :
    tripleCellDegree G C z = ((G.neighborFinset z).filter (fun y => y ∈ C)).card := by
  unfold tripleCellDegree
  congr 1
  ext y
  simp [and_comm]

private theorem outside_inner (G : SimpleGraph V) {u v z : V}
    (hz : z ∉ tripleInnerVertices G u v) :
    z ≠ u ∧ z ≠ v ∧ ¬ G.Adj u z ∧ ¬ G.Adj v z ∧ z ∉ commonNeighborVertices G u v := by
  have hh : ¬ (z = u ∨ z = v ∨ G.Adj u z ∨ G.Adj v z) := by
    simpa [tripleInnerVertices,or_assoc] using hz
  exact ⟨fun h => hh (Or.inl h),fun h => hh (Or.inr (Or.inl h)),
    fun h => hh (Or.inr (Or.inr (Or.inl h))),fun h => hh (Or.inr (Or.inr (Or.inr h))),
    fun h => hh (Or.inr (Or.inr (Or.inl ((mem_commonNeighborVertices G u v z).mp h).1)))⟩

private theorem outer_not_inner (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z : V} (hb : defectMatrix G u v = 3)
    (hz : z ∈ tripleOuterVertices G u v) : z ∉ tripleInnerVertices G u v :=
  fun hi => (Finset.disjoint_left.mp (n62_triple_inner_outer_disjoint G hdeg hdiam hcard hb)) hi hz

private theorem inner_comm (G : SimpleGraph V) (u v : V) :
    tripleInnerVertices G u v = tripleInnerVertices G v u := by
  ext z
  simp only [tripleInnerVertices,Finset.mem_union,Finset.mem_insert,Finset.mem_singleton]
  tauto

private theorem common_degree_eq (G : SimpleGraph V) (u v z : V) :
    tripleCellDegree G (commonNeighborVertices G u v) z = tripleCommonDegree G u v z :=
  tripleCellDegree_eq_neighbor_filter G _ z

/-- Outside the two root neighborhoods, the S and E+ neighbor counts sum to one. -/
theorem n62_triple_outside_neighbor_split (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z : V} (hb : defectMatrix G u v = 3)
    (hz : z ∉ tripleInnerVertices G u v) :
    tripleCommonDegree G u v z + tripleCellDegree G (tripleExclusiveNeighbors G u v) z = 1 := by
  obtain ⟨hzu,hzv,huz,hvz,hzS⟩ := outside_inner G hz
  have hB : defectMatrix G u z = 0 := by
    rw [(n62_triple_repeat_rows G hdeg hdiam hcard hb).1 z,if_neg hzv]
  have he := defect_off_diagonal G hzu.symm
  simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply,if_neg huz] at he
  have hc : (commonNeighborVertices G u z).card = 1 := by
    change commonNeighborCount G u z = 1
    omega
  have hs : commonNeighborVertices G u z =
      (commonNeighborVertices G u v).filter (G.Adj z) ∪
      (tripleExclusiveNeighbors G u v).filter (G.Adj z) := by
    ext y
    simp only [mem_commonNeighborVertices,Finset.mem_union,Finset.mem_filter,
      mem_tripleExclusiveNeighbors]
    tauto
  have hd : Disjoint ((commonNeighborVertices G u v).filter (G.Adj z))
      ((tripleExclusiveNeighbors G u v).filter (G.Adj z)) := by
    apply Finset.disjoint_left.mpr
    intro y hyS hyE
    exact (Finset.disjoint_left.mp (triple_exclusive_common_disjoint G u v))
      (Finset.mem_filter.mp hyE).1 (Finset.mem_filter.mp hyS).1
  rw [hs,Finset.card_union_of_disjoint hd] at hc
  simpa only [← common_degree_eq, tripleCellDegree] using hc

/-- There are no original edges from U to either exclusive side. -/
theorem n62_triple_outer_exclusive_nonadj (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z x : V} (hb : defectMatrix G u v = 3)
    (hz : z ∈ tripleOuterVertices G u v) (hx : x ∈ tripleExclusiveVertices G u v) :
    ¬ G.Adj z x := by
  have hi := outer_not_inner G hdeg hdiam hcard hb hz
  have h1 := n62_triple_outer_common_degree G hdeg hdiam hcard hb hz
  have hp := n62_triple_outside_neighbor_split G hdeg hdiam hcard hb hi
  have hvu : defectMatrix G v u = 3 := by rw [(defect_symmetric G).apply u v,hb]
  have him : z ∉ tripleInnerVertices G v u := by rw [← inner_comm G u v]; exact hi
  have hm := n62_triple_outside_neighbor_split G hdeg hdiam hcard hvu him
  have h1m : tripleCommonDegree G v u z = 1 := by
    unfold tripleCommonDegree
    rw [commonNeighborVertices_comm G v u]
    exact h1
  have hcp : tripleCellDegree G (tripleExclusiveNeighbors G u v) z = 0 := by omega
  have hcm : tripleCellDegree G (tripleExclusiveNeighbors G v u) z = 0 := by omega
  intro hzx
  rcases Finset.mem_union.mp hx with hx | hx
  · have he := Finset.card_eq_zero.mp hcp
    have hm : x ∈ (tripleExclusiveNeighbors G u v).filter (G.Adj z) := Finset.mem_filter.mpr ⟨hx,hzx⟩
    rw [he] at hm
    exact Finset.notMem_empty x hm
  · have he := Finset.card_eq_zero.mp hcm
    have hm : x ∈ (tripleExclusiveNeighbors G v u).filter (G.Adj z) := Finset.mem_filter.mpr ⟨hx,hzx⟩
    rw [he] at hm
    exact Finset.notMem_empty x hm

/-- The remaining 24-set has no original neighbors in S. -/
theorem n62_triple_remaining_common_degree_zero (G : SimpleGraph V)
    {u v z : V} (hz : z ∈ tripleRemainingVertices G u v) : tripleCommonDegree G u v z = 0 := by
  obtain ⟨hi,hU⟩ := (mem_tripleRemainingVertices G u v z).mp hz
  have ho := outside_inner G hi
  apply Finset.card_eq_zero.mpr
  apply Finset.eq_empty_iff_forall_notMem.mpr
  intro s hs
  obtain ⟨hzs,hsS⟩ := Finset.mem_filter.mp hs
  have ha : G.Adj z s := by simpa using hzs
  exact hU ((mem_tripleOuterVertices G u v z).mpr ⟨s,hsS,ha.symm,ho.1,ho.2.1⟩)

/-- Every remaining vertex has exactly one actual original neighbor in each exclusive side. -/
theorem n62_triple_remaining_exclusive_degrees (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z : V} (hb : defectMatrix G u v = 3)
    (hz : z ∈ tripleRemainingVertices G u v) :
    tripleCellDegree G (tripleExclusiveNeighbors G u v) z = 1 ∧
    tripleCellDegree G (tripleExclusiveNeighbors G v u) z = 1 := by
  have hi := ((mem_tripleRemainingVertices G u v z).mp hz).1
  have h0 := n62_triple_remaining_common_degree_zero G hz
  have hp := n62_triple_outside_neighbor_split G hdeg hdiam hcard hb hi
  have hvu : defectMatrix G v u = 3 := by rw [(defect_symmetric G).apply u v,hb]
  have him : z ∉ tripleInnerVertices G v u := by rw [← inner_comm G u v]; exact hi
  have hm := n62_triple_outside_neighbor_split G hdeg hdiam hcard hvu him
  have h0m : tripleCommonDegree G v u z = 0 := by
    unfold tripleCommonDegree
    rw [commonNeighborVertices_comm G v u]
    exact h0
  omega

/-- Each exterior vertex has zero neighbors in its own S fiber and one in every other fiber. -/
theorem n62_triple_outside_fiber_degree (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z s : V} (hb : defectMatrix G u v = 3)
    (hz : z ∉ tripleInnerVertices G u v) (hs : s ∈ commonNeighborVertices G u v) :
    tripleCellDegree G (tripleOuterFiber G u v s) z = if G.Adj z s then 0 else 1 := by
  obtain ⟨hzu,hzv,huz,hvz,hzS⟩ := outside_inner G hz
  have hsz : s ≠ z := by intro he; subst s; exact hzS hs
  have hB : defectMatrix G s z = 0 := by
    rw [n62_triple_common_rows G hdeg hdiam hcard hb hs z]
    simp [hzS]
  have he := defect_off_diagonal G hsz
  have hf : (tripleOuterFiber G u v s).filter (G.Adj z) = commonNeighborVertices G s z := by
    ext y
    simp only [Finset.mem_filter,mem_tripleOuterFiber,mem_commonNeighborVertices]
    constructor
    · exact fun h => ⟨h.1.1,h.2⟩
    · rintro ⟨hsy,hzy⟩
      refine ⟨⟨hsy,?_,?_⟩,hzy⟩
      · intro hy; subst y; exact huz hzy.symm
      · intro hy; subst y; exact hvz hzy.symm
  unfold tripleCellDegree
  rw [hf]
  change commonNeighborCount G s z = _
  by_cases ha : G.Adj z s
  · have has := ha.symm
    simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply,if_pos has] at he
    simp only [if_pos ha]
    omega
  · have has : ¬ G.Adj s z := fun h => ha h.symm
    simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply,if_neg has] at he
    simp only [if_neg ha]
    omega

/-- The exterior neighbor counts into U and S always sum to four. -/
theorem n62_triple_outside_outer_degree_sum (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z : V} (hb : defectMatrix G u v = 3)
    (hz : z ∉ tripleInnerVertices G u v) :
    tripleCellDegree G (tripleOuterVertices G u v) z + tripleCommonDegree G u v z = 4 := by
  have hd : (commonNeighborVertices G u v : Set V).PairwiseDisjoint
      (fun s => (tripleOuterFiber G u v s).filter (G.Adj z)) := by
    intro s hs t ht hst
    exact (n62_triple_outer_fibers_disjoint G hdeg hdiam hcard hb hs ht hst).mono
      (Finset.filter_subset _ _) (Finset.filter_subset _ _)
  have hU : tripleCellDegree G (tripleOuterVertices G u v) z =
      ∑ s ∈ commonNeighborVertices G u v, tripleCellDegree G (tripleOuterFiber G u v s) z := by
    unfold tripleCellDegree tripleOuterVertices
    rw [Finset.filter_biUnion,Finset.card_biUnion hd]
  have hS : tripleCommonDegree G u v z =
      ∑ s ∈ commonNeighborVertices G u v, if G.Adj z s then 1 else 0 := by
    rw [← common_degree_eq]
    simp only [tripleCellDegree,Finset.card_eq_sum_ones,Finset.sum_filter]
  rw [hU,hS,← Finset.sum_add_distrib]
  calc
    _ = ∑ _s ∈ commonNeighborVertices G u v, 1 := by
      apply Finset.sum_congr rfl
      intro s hs
      rw [n62_triple_outside_fiber_degree G hdeg hdiam hcard hb hz hs]
      split_ifs <;> omega
    _ = 4 := by simp [n62_triple_common_card G hdeg hdiam hcard hb]

/-- Every actual U vertex has original internal degree three. -/
theorem n62_triple_outer_internal_degree (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z : V} (hb : defectMatrix G u v = 3)
    (hz : z ∈ tripleOuterVertices G u v) :
    tripleCellDegree G (tripleOuterVertices G u v) z = 3 := by
  have h := n62_triple_outside_outer_degree_sum G hdeg hdiam hcard hb
    (outer_not_inner G hdeg hdiam hcard hb hz)
  have h1 := n62_triple_outer_common_degree G hdeg hdiam hcard hb hz
  omega

/-- Every actual remaining vertex has four original neighbors in U. -/
theorem n62_triple_remaining_outer_degree (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z : V} (hb : defectMatrix G u v = 3)
    (hz : z ∈ tripleRemainingVertices G u v) :
    tripleCellDegree G (tripleOuterVertices G u v) z = 4 := by
  have h := n62_triple_outside_outer_degree_sum G hdeg hdiam hcard hb
    ((mem_tripleRemainingVertices G u v z).mp hz).1
  have h0 := n62_triple_remaining_common_degree_zero G hz
  omega

private theorem cell_degree_union (G : SimpleGraph V) (C D : Finset V) (z : V)
    (hd : Disjoint C D) :
    tripleCellDegree G (C ∪ D) z = tripleCellDegree G C z + tripleCellDegree G D z := by
  unfold tripleCellDegree
  rw [Finset.filter_union,Finset.card_union_of_disjoint
    (hd.mono (Finset.filter_subset _ _) (Finset.filter_subset _ _))]

private theorem cell_degree_zero (G : SimpleGraph V) (C : Finset V) (z : V)
    (h : ∀ y ∈ C, ¬ G.Adj z y) : tripleCellDegree G C z = 0 := by
  apply Finset.card_eq_zero.mpr
  apply Finset.eq_empty_iff_forall_notMem.mpr
  intro y hy
  exact h y (Finset.mem_filter.mp hy).1 (Finset.mem_filter.mp hy).2

private theorem common_exclusive_disjoint (G : SimpleGraph V) (u v : V) :
    Disjoint (commonNeighborVertices G u v) (tripleExclusiveVertices G u v) := by
  apply Finset.disjoint_left.mpr
  intro y hs he
  rcases Finset.mem_union.mp he with hp | hm
  · exact (Finset.disjoint_left.mp (triple_exclusive_common_disjoint G u v)) hp hs
  · have hs' : y ∈ commonNeighborVertices G v u := by rw [commonNeighborVertices_comm]; exact hs
    exact (Finset.disjoint_left.mp (triple_exclusive_common_disjoint G v u)) hm hs'

private theorem outside_inner_degree (G : SimpleGraph V) {u v z : V}
    (hz : z ∉ tripleInnerVertices G u v) :
    tripleCellDegree G (tripleInnerVertices G u v) z =
      tripleCommonDegree G u v z + tripleCellDegree G (tripleExclusiveVertices G u v) z := by
  obtain ⟨_,_,huz,hvz,_⟩ := outside_inner G hz
  have he : (tripleInnerVertices G u v).filter (G.Adj z) =
      (commonNeighborVertices G u v ∪ tripleExclusiveVertices G u v).filter (G.Adj z) := by
    ext y
    simp only [Finset.mem_filter,Finset.mem_union,tripleExclusiveVertices,mem_tripleInnerVertices]
    constructor
    · rintro ⟨hy,hzy⟩
      rcases hy with hu | hv | hs | hp | hm
      · subst y; exact (huz hzy.symm).elim
      · subst y; exact (hvz hzy.symm).elim
      · exact ⟨Or.inl hs,hzy⟩
      · exact ⟨Or.inr (Or.inl hp),hzy⟩
      · exact ⟨Or.inr (Or.inr hm),hzy⟩
    · rintro ⟨hs | hp | hm,hzy⟩
      · exact ⟨Or.inr (Or.inr (Or.inl hs)),hzy⟩
      · exact ⟨Or.inr (Or.inr (Or.inr (Or.inl hp))),hzy⟩
      · exact ⟨Or.inr (Or.inr (Or.inr (Or.inr hm))),hzy⟩
  change ((tripleInnerVertices G u v).filter (G.Adj z)).card = _
  rw [he]
  change tripleCellDegree G (commonNeighborVertices G u v ∪ tripleExclusiveVertices G u v) z = _
  rw [cell_degree_union G _ _ z (common_exclusive_disjoint G u v),common_degree_eq]

private theorem remaining_degree (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) (z : V) :
    tripleCellDegree G (tripleRemainingVertices G u v) z =
      8 - (tripleCellDegree G (tripleInnerVertices G u v) z +
        tripleCellDegree G (tripleOuterVertices G u v) z) := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hu : (Finset.univ.filter (G.Adj z)) = G.neighborFinset z := by ext y; simp
  have hsub : ((tripleInnerVertices G u v ∪ tripleOuterVertices G u v).filter (G.Adj z)) ⊆
      Finset.univ.filter (G.Adj z) := by
    intro y hy
    exact Finset.mem_filter.mpr ⟨Finset.mem_univ _,(Finset.mem_filter.mp hy).2⟩
  have hf : (Finset.univ \ (tripleInnerVertices G u v ∪ tripleOuterVertices G u v)).filter (G.Adj z) =
      Finset.univ.filter (G.Adj z) \ (tripleInnerVertices G u v ∪ tripleOuterVertices G u v).filter (G.Adj z) := by
    ext y
    simp only [Finset.mem_filter,Finset.mem_sdiff,Finset.mem_univ,true_and]
    tauto
  unfold tripleCellDegree tripleRemainingVertices
  rw [hf,Finset.card_sdiff_of_subset hsub,hu,
    SimpleGraph.card_neighborFinset_eq_degree,hreg z]
  change 8 - tripleCellDegree G (tripleInnerVertices G u v ∪ tripleOuterVertices G u v) z = _
  rw [cell_degree_union G _ _ z (n62_triple_inner_outer_disjoint G hdeg hdiam hcard hb)]

/-- The complete E-neighbor count of a remaining vertex is two. -/
theorem n62_triple_remaining_exclusive_union_degree (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z : V} (hb : defectMatrix G u v = 3)
    (hz : z ∈ tripleRemainingVertices G u v) :
    tripleCellDegree G (tripleExclusiveVertices G u v) z = 2 := by
  have h := n62_triple_remaining_exclusive_degrees G hdeg hdiam hcard hb hz
  rw [tripleExclusiveVertices,cell_degree_union G _ _ z (triple_exclusive_disjoint G u v),h.1,h.2]

/-- Every actual remaining vertex has original internal degree two. -/
theorem n62_triple_remaining_internal_degree (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z : V} (hb : defectMatrix G u v = 3)
    (hz : z ∈ tripleRemainingVertices G u v) :
    tripleCellDegree G (tripleRemainingVertices G u v) z = 2 := by
  rw [remaining_degree G hdeg hdiam hcard hb z,
    outside_inner_degree G ((mem_tripleRemainingVertices G u v z).mp hz).1,
    n62_triple_remaining_common_degree_zero G hz,
    n62_triple_remaining_exclusive_union_degree G hdeg hdiam hcard hb hz,
    n62_triple_remaining_outer_degree G hdeg hdiam hcard hb hz]

/-- Every actual U vertex has four original neighbors in the remaining cell. -/
theorem n62_triple_outer_remaining_degree (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z : V} (hb : defectMatrix G u v = 3)
    (hz : z ∈ tripleOuterVertices G u v) :
    tripleCellDegree G (tripleRemainingVertices G u v) z = 4 := by
  have hE : tripleCellDegree G (tripleExclusiveVertices G u v) z = 0 :=
    cell_degree_zero G _ z (fun _ hx => n62_triple_outer_exclusive_nonadj G hdeg hdiam hcard hb hz hx)
  rw [remaining_degree G hdeg hdiam hcard hb z,
    outside_inner_degree G (outer_not_inner G hdeg hdiam hcard hb hz),
    n62_triple_outer_common_degree G hdeg hdiam hcard hb hz,hE,
    n62_triple_outer_internal_degree G hdeg hdiam hcard hb hz]

/-- Counts into the five actual cells, in endpoint-pair, S, E, U, remaining order. -/
def tripleCellRow (G : SimpleGraph V) (u v z : V) : Fin 5 → ℕ :=
  ![tripleCellDegree G {u,v} z,
    tripleCellDegree G (commonNeighborVertices G u v) z,
    tripleCellDegree G (tripleExclusiveVertices G u v) z,
    tripleCellDegree G (tripleOuterVertices G u v) z,
    tripleCellDegree G (tripleRemainingVertices G u v) z]

private theorem outside_pair_degree (G : SimpleGraph V) {u v z : V}
    (hz : z ∉ tripleInnerVertices G u v) : tripleCellDegree G {u,v} z = 0 := by
  have ho := outside_inner G hz
  apply cell_degree_zero
  intro y hy hzy
  rcases Finset.mem_insert.mp hy with hy | hy
  · subst y; exact ho.2.2.1 hzy.symm
  · have he := Finset.mem_singleton.mp hy
    subst y; exact ho.2.2.2.1 hzy.symm

/-- Exact original-neighbor row for every actual U vertex. -/
theorem n62_triple_outer_cell_row (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z : V} (hb : defectMatrix G u v = 3)
    (hz : z ∈ tripleOuterVertices G u v) : tripleCellRow G u v z = ![0,1,0,3,4] := by
  have hp := outside_pair_degree G (outer_not_inner G hdeg hdiam hcard hb hz)
  have hs : tripleCellDegree G (commonNeighborVertices G u v) z = 1 := by
    rw [common_degree_eq,n62_triple_outer_common_degree G hdeg hdiam hcard hb hz]
  have he : tripleCellDegree G (tripleExclusiveVertices G u v) z = 0 :=
    cell_degree_zero G _ z (fun _ hx => n62_triple_outer_exclusive_nonadj G hdeg hdiam hcard hb hz hx)
  simp only [tripleCellRow,hp,hs,he,n62_triple_outer_internal_degree G hdeg hdiam hcard hb hz,
    n62_triple_outer_remaining_degree G hdeg hdiam hcard hb hz]

/-- Exact original-neighbor row for every actual remaining vertex. -/
theorem n62_triple_remaining_cell_row (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z : V} (hb : defectMatrix G u v = 3)
    (hz : z ∈ tripleRemainingVertices G u v) : tripleCellRow G u v z = ![0,0,2,4,2] := by
  have hp := outside_pair_degree G ((mem_tripleRemainingVertices G u v z).mp hz).1
  have hs : tripleCellDegree G (commonNeighborVertices G u v) z = 0 := by
    rw [common_degree_eq,n62_triple_remaining_common_degree_zero G hz]
  simp only [tripleCellRow,hp,hs,n62_triple_remaining_exclusive_union_degree G hdeg hdiam hcard hb hz,
    n62_triple_remaining_outer_degree G hdeg hdiam hcard hb hz,
    n62_triple_remaining_internal_degree G hdeg hdiam hcard hb hz]

/-- Exact original-neighbor row at the first endpoint of any actual triple pair. -/
theorem n62_triple_endpoint_cell_row (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    tripleCellRow G u v u = ![0,4,4,0,0] := by
  have hn := (n62_triple_repeat_nonadj G hdeg hdiam hcard hb).2
  have hp : tripleCellDegree G {u,v} u = 0 := by simp [tripleCellDegree,hn]
  have hs : tripleCellDegree G (commonNeighborVertices G u v) u = 4 := by
    rw [common_degree_eq]
    exact (n62_triple_common_degree_endpoints G hdeg hdiam hcard hb).1
  have he : tripleCellDegree G (tripleExclusiveVertices G u v) u = 4 := by
    have hf : (tripleExclusiveVertices G u v).filter (G.Adj u) = tripleExclusiveNeighbors G u v := by
      ext y
      simp only [tripleExclusiveVertices,Finset.mem_union,Finset.mem_filter,mem_tripleExclusiveNeighbors]
      tauto
    unfold tripleCellDegree
    rw [hf,n62_triple_exclusive_card G hdeg hdiam hcard hb]
  have hU : tripleCellDegree G (tripleOuterVertices G u v) u = 0 := by
    apply cell_degree_zero
    intro y hy
    exact (outside_inner G (outer_not_inner G hdeg hdiam hcard hb hy)).2.2.1
  have hV : tripleCellDegree G (tripleRemainingVertices G u v) u = 0 := by
    apply cell_degree_zero
    intro y hy
    exact (outside_inner G ((mem_tripleRemainingVertices G u v y).mp hy).1).2.2.1
  simp only [tripleCellRow,hp,hs,he,hU,hV]

/-- Exact original-neighbor row on the actual common-neighbor four-set. -/
theorem n62_triple_common_cell_row (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v s : V} (hb : defectMatrix G u v = 3)
    (hs : s ∈ commonNeighborVertices G u v) : tripleCellRow G u v s = ![2,0,0,6,0] := by
  have hs' := (mem_commonNeighborVertices G u v s).mp hs
  have huv := (n62_triple_repeat_nonadj G hdeg hdiam hcard hb).1
  have hp : tripleCellDegree G {u,v} s = 2 := by
    simp [tripleCellDegree,hs'.1.symm,hs'.2.symm,huv]
  have hS : tripleCellDegree G (commonNeighborVertices G u v) s = 0 :=
    cell_degree_zero G _ s (fun _ ht => n62_triple_common_nonadj G hdeg hdiam hcard hb hs ht)
  have hE : tripleCellDegree G (tripleExclusiveVertices G u v) s = 0 := by
    apply cell_degree_zero
    intro x hx ha
    rcases Finset.mem_union.mp hx with hx | hx
    · exact n62_triple_exclusive_common_nonadj G hdeg hdiam hcard hb hx hs ha.symm
    · have hvu : defectMatrix G v u = 3 := by rw [(defect_symmetric G).apply u v,hb]
      have hsR : s ∈ commonNeighborVertices G v u := by rw [commonNeighborVertices_comm]; exact hs
      exact n62_triple_exclusive_common_nonadj G hdeg hdiam hcard hvu hx hsR ha.symm
  have hU : tripleCellDegree G (tripleOuterVertices G u v) s = 6 := by
    have hf : (tripleOuterVertices G u v).filter (G.Adj s) = tripleOuterFiber G u v s := by
      ext y
      simp only [Finset.mem_filter,mem_tripleOuterFiber]
      constructor
      · rintro ⟨hy,ha⟩
        have ho := n62_triple_outer_outside G hdeg hdiam hcard hb hy
        exact ⟨ha,ho.1,ho.2.1⟩
      · rintro ⟨ha,hyu,hyv⟩
        exact ⟨(mem_tripleOuterVertices G u v y).mpr ⟨s,hs,ha,hyu,hyv⟩,ha⟩
    unfold tripleCellDegree
    rw [hf,n62_triple_outer_fiber_card G hdeg hdiam hcard hb hs]
  have hV : tripleCellDegree G (tripleRemainingVertices G u v) s = 0 := by
    apply cell_degree_zero
    intro y hy ha
    obtain ⟨hi,hU⟩ := (mem_tripleRemainingVertices G u v y).mp hy
    have ho := outside_inner G hi
    exact hU ((mem_tripleOuterVertices G u v y).mpr ⟨s,hs,ha,ho.1,ho.2.1⟩)
  simp only [tripleCellRow,hp,hS,hE,hU,hV]

/-- Exact original-neighbor row on the first exclusive side of any actual triple pair. -/
theorem n62_triple_exclusive_cell_row (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v z : V} (hb : defectMatrix G u v = 3)
    (hz : z ∈ tripleExclusiveNeighbors G u v) : tripleCellRow G u v z = ![1,0,1,0,6] := by
  have hz' := (mem_tripleExclusiveNeighbors G u v z).mp hz
  have hzv : ¬ G.Adj z v := fun h => hz'.2 h.symm
  have hzE : z ∈ tripleExclusiveVertices G u v := Finset.mem_union_left _ hz
  have hp : tripleCellDegree G {u,v} z = 1 := by simp [tripleCellDegree,hz'.1.symm,hzv]
  have hS : tripleCellDegree G (commonNeighborVertices G u v) z = 0 :=
    cell_degree_zero G _ z (fun _ hs => n62_triple_exclusive_common_nonadj G hdeg hdiam hcard hb hz hs)
  have hE : tripleCellDegree G (tripleExclusiveVertices G u v) z = 1 := by
    have hplus : tripleCellDegree G (tripleExclusiveNeighbors G u v) z = 0 :=
      cell_degree_zero G _ z (fun _ hx => n62_triple_exclusive_independent G hdeg hdiam hcard hb hz hx)
    have hminus : tripleCellDegree G (tripleExclusiveNeighbors G v u) z = 1 := by
      rw [tripleCellDegree_eq_neighbor_filter]
      exact n62_triple_cross_degree_one G hdeg hdiam hcard hb hz
    rw [tripleExclusiveVertices,cell_degree_union G _ _ z (triple_exclusive_disjoint G u v),hplus,hminus]
  have hU : tripleCellDegree G (tripleOuterVertices G u v) z = 0 :=
    cell_degree_zero G _ z (fun _ hx ha => n62_triple_outer_exclusive_nonadj G hdeg hdiam hcard hb hx hzE ha.symm)
  have hV : tripleCellDegree G (tripleRemainingVertices G u v) z = 6 := by
    rw [tripleCellDegree_eq_neighbor_filter]
    have hf : (G.neighborFinset z).filter (fun y => y ∈ tripleRemainingVertices G u v) =
        (G.neighborFinset z).filter (fun y => y ≠ u ∧ y ≠ v ∧
          y ∉ commonNeighborVertices G u v ∧ y ∉ tripleExclusiveNeighbors G u v ∧
          y ∉ tripleExclusiveNeighbors G v u) := by
      ext y
      have hn : G.Adj z y → y ∉ tripleOuterVertices G u v :=
        fun ha hy => n62_triple_outer_exclusive_nonadj G hdeg hdiam hcard hb hy hzE ha.symm
      simp only [Finset.mem_filter,SimpleGraph.mem_neighborFinset,mem_tripleRemainingVertices,
        mem_tripleInnerVertices,not_or]
      tauto
    rw [hf]
    exact n62_triple_exclusive_exterior_card G hdeg hdiam hcard hb ⟨z,hz⟩
  simp only [tripleCellRow,hp,hS,hE,hU,hV]

end
end DegreeDiameter

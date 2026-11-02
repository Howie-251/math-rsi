import DegreeDiameter.N62OppositeParity

namespace DegreeDiameter
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

private theorem third_of_triangle (G : SimpleGraph V) {T : Finset V}
    (hT : G.IsNClique 3 T) {x y : V} :
    ∃ z ∈ T, z ≠ x ∧ z ≠ y := by
  have hc : ({x,y} : Finset V).card < T.card := by
    rw [hT.card_eq]
    by_cases h : x = y <;> simp [h]
  obtain ⟨z,hz,hzn⟩ := Finset.exists_mem_notMem_of_card_lt_card hc
  exact ⟨z,hz,by simpa using hzn⟩

private theorem triangle_shared_edge_eq (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {T S : Finset V}
    (hT : G.IsNClique 3 T) (hS : G.IsNClique 3 S) {p : V × V}
    (hpT : p ∈ T.offDiag) (hpS : p ∈ S.offDiag) : T = S := by
  obtain ⟨hxT,hyT,hxy⟩ := Finset.mem_offDiag.mp hpT
  obtain ⟨hxS,hyS,_⟩ := Finset.mem_offDiag.mp hpS
  obtain ⟨z,hzT,hzx,hzy⟩ := third_of_triangle G hT (x := p.1) (y := p.2)
  have hxyA := hT.isClique hxT hyT hxy
  have hxzA := hT.isClique hxT hzT hzx.symm
  have hyzA := hT.isClique hyT hzT hzy.symm
  have hw := n62_triangle_within_root G hdeg hdiam hcard hxyA hxzA hyzA
  have hsub : S ⊆ T := by
    intro t ht
    by_cases htx : t = p.1
    · simpa [htx] using hxT
    by_cases hty : t = p.2
    · simpa [hty] using hyT
    have hxt := hS.isClique hxS ht (Ne.symm htx)
    have hyt := hS.isClique hyS ht (Ne.symm hty)
    have hh := (hw p.2 t hxyA hxt).mp hyt
    have htz : t = z := by
      rcases hh with hh | hh
      · exact hh.2
      · exact False.elim (hzy hh.1.symm)
    simpa [htz] using hzT
  exact (Finset.eq_of_subset_of_card_le hsub (by rw [hT.card_eq,hS.card_eq])).symm

private theorem triangle_edge_unit (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {T : Finset V} (hT : G.IsNClique 3 T)
    {p : V × V} (hp : p ∈ T.offDiag) : G.Adj p.1 p.2 ∧ defectMatrix G p.1 p.2 = 1 := by
  obtain ⟨hx,hy,hxy⟩ := Finset.mem_offDiag.mp hp
  obtain ⟨z,hz,hzx,hzy⟩ := third_of_triangle G hT (x := p.1) (y := p.2)
  have ha := hT.isClique hx hy hxy
  have hl := defect_incident_triangle_ge_one G ha
    (hT.isClique hx hz hzx.symm) (hT.isClique hz hy hzy)
  have hu := n62_edge_defect_le_one G hdeg hdiam hcard ha
  exact ⟨ha,by omega⟩

private theorem pair_eq_of_offDiag {P : Finset V} (hc : P.card = 2)
    {p : V × V} (hp : p ∈ P.offDiag) : P = {p.1,p.2} := by
  obtain ⟨hx,hy,hxy⟩ := Finset.mem_offDiag.mp hp
  have hs : ({p.1,p.2} : Finset V) ⊆ P := by simp [Finset.insert_subset_iff,hx,hy]
  exact (Finset.eq_of_subset_of_card_le hs (by simp [hc,hxy])).symm

private theorem unit_nonedge_pair_card (G : SimpleGraph V) {P : Finset V}
    (hP : P ∈ unitNonedgePairs G) : P.card = 2 := by
  obtain ⟨x,y,hxy,_,_,rfl⟩ := (Finset.mem_filter.mp hP).2
  simp [hxy]

private theorem mem_unit_nonedge_offDiag (G : SimpleGraph V) (p : V × V) :
    p ∈ (unitNonedgePairs G).biUnion Finset.offDiag ↔
      p.1 ≠ p.2 ∧ ¬ G.Adj p.1 p.2 ∧ defectMatrix G p.1 p.2 = 1 := by
  constructor
  · intro hp
    obtain ⟨P,hP,hp⟩ := Finset.mem_biUnion.mp hp
    obtain ⟨x,y,hxy,hn,hb,rfl⟩ := (Finset.mem_filter.mp hP).2
    obtain ⟨hx,hy,hne⟩ := Finset.mem_offDiag.mp hp
    simp only [Finset.mem_insert,Finset.mem_singleton] at hx hy
    rcases hx with hx | hx <;> rcases hy with hy | hy
    · exact False.elim (hne (hx.trans hy.symm))
    · simpa [hx,hy] using And.intro hxy (And.intro hn hb)
    · have hbn : defectMatrix G y x = 1 := by rw [(defect_symmetric G).apply x y]; exact hb
      have hnn : ¬ G.Adj y x := fun ha => hn ha.symm
      simpa [hx,hy] using And.intro hxy.symm (And.intro hnn hbn)
    · exact False.elim (hne (hx.trans hy.symm))
  · rintro ⟨hne,hn,hb⟩
    apply Finset.mem_biUnion.mpr
    refine ⟨{p.1,p.2}, ?_, ?_⟩
    · exact Finset.mem_filter.mpr ⟨Finset.mem_univ _,p.1,p.2,hne,hn,hb,rfl⟩
    · simp [Finset.mem_offDiag,hne]

private theorem unit_nonedge_offDiag_card (G : SimpleGraph V) :
    ((unitNonedgePairs G).biUnion Finset.offDiag).card = 2 * (unitNonedgePairs G).card := by
  have hd : (unitNonedgePairs G : Set (Finset V)).PairwiseDisjoint Finset.offDiag := by
    intro P hP Q hQ hne
    apply Finset.disjoint_left.mpr
    intro p hp hq
    exact hne ((pair_eq_of_offDiag (unit_nonedge_pair_card G hP) hp).trans
      (pair_eq_of_offDiag (unit_nonedge_pair_card G hQ) hq).symm)
  rw [Finset.card_biUnion hd]
  have hh : ∑ P ∈ unitNonedgePairs G, P.offDiag.card = ∑ _P ∈ unitNonedgePairs G, 2 := by
    apply Finset.sum_congr rfl
    intro P hP
    rw [Finset.offDiag_card,unit_nonedge_pair_card G hP]
  rw [hh]
  simp [Nat.mul_comm]

private theorem triangle_offDiag_card (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) :
    ((G.cliqueFinset 3).biUnion Finset.offDiag).card = 6 * (G.cliqueFinset 3).card := by
  have hd : (G.cliqueFinset 3 : Set (Finset V)).PairwiseDisjoint Finset.offDiag := by
    intro T hT S hS hne
    apply Finset.disjoint_left.mpr
    intro p hpT hpS
    exact hne (triangle_shared_edge_eq G hdeg hdiam hcard
      (SimpleGraph.mem_cliqueFinset_iff.mp hT) (SimpleGraph.mem_cliqueFinset_iff.mp hS) hpT hpS)
  rw [Finset.card_biUnion hd]
  have hh : ∑ T ∈ G.cliqueFinset 3, T.offDiag.card = ∑ _T ∈ G.cliqueFinset 3, 6 := by
    apply Finset.sum_congr rfl
    intro T hT
    rw [Finset.offDiag_card,(SimpleGraph.mem_cliqueFinset_iff.mp hT).card_eq]
  rw [hh]
  simp [Nat.mul_comm]


private theorem unit_pair_coverage (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) :
    (unitNonedgePairs G).biUnion Finset.offDiag ∪ (G.cliqueFinset 3).biUnion Finset.offDiag =
      Finset.univ.filter (fun p : V × V => defectMatrix G p.1 p.2 = 1) := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  ext p
  constructor
  · intro hp
    apply Finset.mem_filter.mpr
    refine ⟨Finset.mem_univ _, ?_⟩
    rcases Finset.mem_union.mp hp with hn | ht
    · exact ((mem_unit_nonedge_offDiag G p).mp hn).2.2
    · obtain ⟨T,hT,hpT⟩ := Finset.mem_biUnion.mp ht
      exact (triangle_edge_unit G hdeg hdiam hcard
        (SimpleGraph.mem_cliqueFinset_iff.mp hT) hpT).2
  · intro hp
    have hb := (Finset.mem_filter.mp hp).2
    by_cases ha : G.Adj p.1 p.2
    · apply Finset.mem_union_right
      have hc : 0 < commonNeighborCount G p.1 p.2 := by
        have hh := defect_off_diagonal G ha.ne
        simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply,if_pos ha] at hh
        omega
      obtain ⟨z,hz⟩ := Finset.card_pos.mp hc
      have hz' : G.Adj p.1 z ∧ G.Adj z p.2 := by simpa using hz
      apply Finset.mem_biUnion.mpr
      refine ⟨{p.1,p.2,z}, ?_, ?_⟩
      · exact SimpleGraph.mem_cliqueFinset_iff.mpr
          (SimpleGraph.is3Clique_triple_iff.mpr ⟨ha,hz'.1,hz'.2.symm⟩)
      · simp [Finset.mem_offDiag,ha.ne]
    · apply Finset.mem_union_left
      apply (mem_unit_nonedge_offDiag G p).mpr
      have hne : p.1 ≠ p.2 := by
        intro h
        rw [← h,defect_diagonal G hreg] at hb
        omega
      exact ⟨hne,ha,hb⟩

/-- Actual incidence count: unit-repeat nonedges contribute two ordered
pairs, actual triangles contribute six, and the 62 defect rows contribute
three each. No supplied count or cycle certificate is assumed. -/
theorem n62_simple_repeat_incidence (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (hsimple : ∀ x y, defectMatrix G x y ≤ 1) :
    2 * (unitNonedgePairs G).card + 6 * (G.cliqueFinset 3).card = 186 := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hsum (x : V) : ∑ y, defectMatrix G x y = 3 := by
    simpa [hcard] using defect_row_sum G hreg x
  have hvalue (x y : V) : defectMatrix G x y = if defectMatrix G x y = 1 then 1 else 0 := by
    have h0 := defect_nonnegative G hreg hdiam x y
    have h1 := hsimple x y
    split_ifs <;> omega
  have hcInt : ((Finset.univ.filter (fun p : V × V => defectMatrix G p.1 p.2 = 1)).card : ℤ) = 186 := by
    calc
      _ = ∑ p : V × V, defectMatrix G p.1 p.2 := by
        have hind : (∑ p : V × V, defectMatrix G p.1 p.2) =
            ∑ p : V × V, (if defectMatrix G p.1 p.2 = 1 then (1 : ℤ) else 0) := by
          apply Finset.sum_congr rfl
          intro p _
          exact hvalue p.1 p.2
        rw [hind]
        simp
      _ = ∑ x : V, ∑ y : V, defectMatrix G x y := by
        rw [← Finset.univ_product_univ,Finset.sum_product]
      _ = 186 := by simp [hsum,hcard]
  have hc : (Finset.univ.filter (fun p : V × V => defectMatrix G p.1 p.2 = 1)).card = 186 := by
    exact_mod_cast hcInt
  have hd : Disjoint ((unitNonedgePairs G).biUnion Finset.offDiag)
      ((G.cliqueFinset 3).biUnion Finset.offDiag) := by
    apply Finset.disjoint_left.mpr
    intro p hp hq
    have hn := ((mem_unit_nonedge_offDiag G p).mp hp).2.1
    obtain ⟨T,hT,hpT⟩ := Finset.mem_biUnion.mp hq
    exact hn (triangle_edge_unit G hdeg hdiam hcard
      (SimpleGraph.mem_cliqueFinset_iff.mp hT) hpT).1
  have hu := Finset.card_union_of_disjoint hd
  rw [unit_pair_coverage G hdeg hdiam hcard,hc,
    unit_nonedge_offDiag_card G,triangle_offDiag_card G hdeg hdiam hcard] at hu
  exact hu.symm

/-- New original-graph order-62 exclusion of the entire simple-defect case.
Both parity statements and their actual incidence connection are derived. -/
theorem no_n62_simple_defect_graph (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (hsimple : ∀ x y, defectMatrix G x y ≤ 1) : False := by
  obtain ⟨k,hk⟩ := n62_triangle_count_even G hdeg hdiam hcard
  obtain ⟨j,hj⟩ := n62_unit_nonedge_pair_count_even G hdeg hdiam hcard hsimple
  have hc := n62_simple_repeat_incidence G hdeg hdiam hcard hsimple
  omega

end
end DegreeDiameter

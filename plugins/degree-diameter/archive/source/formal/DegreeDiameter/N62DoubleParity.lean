import DegreeDiameter.N62SimpleExclusion

namespace DegreeDiameter
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- Actual unordered double-repeat nonedges. -/
def doubleNonedgePairs (G : SimpleGraph V) : Finset (Finset V) :=
  Finset.univ.filter (fun P => ∃ x y, x ≠ y ∧ ¬ G.Adj x y ∧
    defectMatrix G x y = 2 ∧ P = {x,y})

/-- All actual unordered nonedges. -/
def nonedgePairs (G : SimpleGraph V) : Finset (Finset V) :=
  Finset.univ.filter (fun P => ∃ x y, x ≠ y ∧ ¬ G.Adj x y ∧ P = {x,y})

/-- An actual choice of a nonedge and an unordered two-subset of its
common neighbors; swapping the two opposite pairs pairs these flags. -/
def fourCycleFlags (G : SimpleGraph V) : Finset (Finset V × Finset V) :=
  (nonedgePairs G).biUnion (fun P =>
    ((oppositePair G P).powersetCard 2).image (fun Q => (P,Q)))


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

private theorem double_nonedge_pair_card (G : SimpleGraph V) {P : Finset V}
    (hP : P ∈ doubleNonedgePairs G) : P.card = 2 := by
  obtain ⟨x,y,hxy,_,_,rfl⟩ := (Finset.mem_filter.mp hP).2
  simp [hxy]

private theorem mem_double_nonedge_offDiag (G : SimpleGraph V) (p : V × V) :
    p ∈ (doubleNonedgePairs G).biUnion Finset.offDiag ↔
      p.1 ≠ p.2 ∧ ¬ G.Adj p.1 p.2 ∧ defectMatrix G p.1 p.2 = 2 := by
  constructor
  · intro hp
    obtain ⟨P,hP,hp⟩ := Finset.mem_biUnion.mp hp
    obtain ⟨x,y,hxy,hn,hb,rfl⟩ := (Finset.mem_filter.mp hP).2
    obtain ⟨hx,hy,hne⟩ := Finset.mem_offDiag.mp hp
    simp only [Finset.mem_insert,Finset.mem_singleton] at hx hy
    rcases hx with hx | hx <;> rcases hy with hy | hy
    · exact False.elim (hne (hx.trans hy.symm))
    · simpa [hx,hy] using And.intro hxy (And.intro hn hb)
    · have hbn : defectMatrix G y x = 2 := by rw [(defect_symmetric G).apply x y]; exact hb
      have hnn : ¬ G.Adj y x := fun ha => hn ha.symm
      simpa [hx,hy] using And.intro hxy.symm (And.intro hnn hbn)
    · exact False.elim (hne (hx.trans hy.symm))
  · rintro ⟨hne,hn,hb⟩
    apply Finset.mem_biUnion.mpr
    refine ⟨{p.1,p.2}, ?_, ?_⟩
    · exact Finset.mem_filter.mpr ⟨Finset.mem_univ _,p.1,p.2,hne,hn,hb,rfl⟩
    · simp [Finset.mem_offDiag,hne]

private theorem double_nonedge_offDiag_card (G : SimpleGraph V) :
    ((doubleNonedgePairs G).biUnion Finset.offDiag).card = 2 * (doubleNonedgePairs G).card := by
  have hd : (doubleNonedgePairs G : Set (Finset V)).PairwiseDisjoint Finset.offDiag := by
    intro P hP Q hQ hne
    apply Finset.disjoint_left.mpr
    intro p hp hq
    exact hne ((pair_eq_of_offDiag (double_nonedge_pair_card G hP) hp).trans
      (pair_eq_of_offDiag (double_nonedge_pair_card G hQ) hq).symm)
  rw [Finset.card_biUnion hd]
  have hh : ∑ P ∈ doubleNonedgePairs G, P.offDiag.card = ∑ _P ∈ doubleNonedgePairs G, 2 := by
    apply Finset.sum_congr rfl
    intro P hP
    rw [Finset.offDiag_card,double_nonedge_pair_card G hP]
  rw [hh]
  simp [Nat.mul_comm]

private theorem opposite_pair_card (G : SimpleGraph V) (x y : V) :
    (oppositePair G {x,y}).card = commonNeighborCount G x y := by
  unfold commonNeighborCount
  congr 1
  ext z
  simp [oppositePair,SimpleGraph.adj_comm]

private theorem mem_fourCycleFlags (G : SimpleGraph V) (P Q : Finset V) :
    (P,Q) ∈ fourCycleFlags G ↔ P ∈ nonedgePairs G ∧ Q ⊆ oppositePair G P ∧ Q.card = 2 := by
  simp [fourCycleFlags,Finset.mem_powersetCard]

private theorem opposite_flags_swap (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {P Q : Finset V}
    (hPQ : (P,Q) ∈ fourCycleFlags G) :
    (Q,P) ∈ fourCycleFlags G ∧ (Q,P) ≠ (P,Q) := by
  obtain ⟨hP,hsub,hQc⟩ := (mem_fourCycleFlags G P Q).mp hPQ
  obtain ⟨x,y,hxy,hn,rfl⟩ := (Finset.mem_filter.mp hP).2
  obtain ⟨r,s,hrs,rfl⟩ := Finset.card_eq_two.mp hQc
  have hr : G.Adj x r ∧ G.Adj y r := by simpa using hsub (by simp : r ∈ ({r,s} : Finset V))
  have hs : G.Adj x s ∧ G.Adj y s := by simpa using hsub (by simp : s ∈ ({r,s} : Finset V))
  have hback : ({x,y} : Finset V) ⊆ oppositePair G {r,s} := by
    intro z hz
    simp only [Finset.mem_insert,Finset.mem_singleton] at hz
    rcases hz with rfl | rfl <;> simp [hr.1.symm,hr.2.symm,hs.1.symm,hs.2.symm]
  have hc : 2 ≤ commonNeighborCount G r s := by
    simpa [hxy,opposite_pair_card] using Finset.card_le_card hback
  have hnrs : ¬ G.Adj r s := by
    intro ha
    have hh := defect_off_diagonal G hrs
    have hl := n62_edge_defect_le_one G hdeg hdiam hcard ha
    simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply,if_pos ha] at hh
    omega
  refine ⟨(mem_fourCycleFlags G _ _).mpr ⟨?_,hback,by simp [hxy]⟩,?_⟩
  · exact Finset.mem_filter.mpr ⟨Finset.mem_univ _,r,s,hrs,hnrs,rfl⟩
  · intro heq
    have hsets : ({r,s} : Finset V) = {x,y} := congrArg Prod.fst heq
    have hx : x ∈ ({r,s} : Finset V) := by rw [hsets]; simp
    have hlo := (mem_oppositePair G {x,y} x).mp (hsub hx) x (by simp)
    exact G.irrefl hlo

/-- Actual opposite-pair flags occur in pairs, without any defect bound. -/
theorem n62_four_cycle_flags_even (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) : Even (fourCycleFlags G).card := by
  have hz : (∑ P ∈ fourCycleFlags G, (1 : ZMod 2)) = 0 := by
    apply Finset.sum_involution (fun P _ => P.swap)
    · intro P hP; decide
    · intro P hP _; exact (opposite_flags_swap G hdeg hdiam hcard hP).2
    · intro P hP; exact Prod.swap_swap P
    · intro P hP; exact (opposite_flags_swap G hdeg hdiam hcard hP).1
  apply ZMod.natCast_eq_zero_iff_even.mp
  simpa using hz

private theorem four_cycle_flags_card (G : SimpleGraph V) :
    (fourCycleFlags G).card = ∑ P ∈ nonedgePairs G, (oppositePair G P).card.choose 2 := by
  have hd : (nonedgePairs G : Set (Finset V)).PairwiseDisjoint
      (fun P => ((oppositePair G P).powersetCard 2).image (fun Q => (P,Q))) := by
    intro P hP Q hQ hne
    apply Finset.disjoint_left.mpr
    intro t htP htQ
    obtain ⟨u,_,hu⟩ := Finset.mem_image.mp htP
    obtain ⟨v,_,hv⟩ := Finset.mem_image.mp htQ
    exact hne (congrArg Prod.fst (hu.trans hv.symm))
  unfold fourCycleFlags
  rw [Finset.card_biUnion hd]
  apply Finset.sum_congr rfl
  intro P hP
  rw [Finset.card_image_of_injective _ (by intro Q R hh; exact congrArg Prod.snd hh),
    Finset.card_powersetCard]

/-- Each actual unit nonedge supplies one flag; each actual double nonedge
supplies three choices of two among its three common neighbors. -/
theorem n62_four_cycle_flag_incidence (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (hbound : ∀ x y, defectMatrix G x y ≤ 2) :
    (fourCycleFlags G).card = (unitNonedgePairs G).card + 3 * (doubleNonedgePairs G).card := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hterm (P : Finset V) (hP : P ∈ nonedgePairs G) :
      (oppositePair G P).card.choose 2 =
        (if P ∈ unitNonedgePairs G then 1 else 0) +
        3 * (if P ∈ doubleNonedgePairs G then 1 else 0) := by
    obtain ⟨x,y,hxy,hn,rfl⟩ := (Finset.mem_filter.mp hP).2
    have hu : ({x,y} : Finset V) ∈ unitNonedgePairs G ↔ defectMatrix G x y = 1 := by
      constructor
      · intro hh
        apply ((mem_unit_nonedge_offDiag G (x,y)).mp ?_).2.2
        exact Finset.mem_biUnion.mpr ⟨{x,y},hh,by simp [Finset.mem_offDiag,hxy]⟩
      · intro hh; exact Finset.mem_filter.mpr ⟨Finset.mem_univ _,x,y,hxy,hn,hh,rfl⟩
    have hd : ({x,y} : Finset V) ∈ doubleNonedgePairs G ↔ defectMatrix G x y = 2 := by
      constructor
      · intro hh
        apply ((mem_double_nonedge_offDiag G (x,y)).mp ?_).2.2
        exact Finset.mem_biUnion.mpr ⟨{x,y},hh,by simp [Finset.mem_offDiag,hxy]⟩
      · intro hh; exact Finset.mem_filter.mpr ⟨Finset.mem_univ _,x,y,hxy,hn,hh,rfl⟩
    simp only [opposite_pair_card,hu,hd]
    have ho := defect_off_diagonal G hxy
    simp only [adjacencyMatrix,SimpleGraph.adjMatrix_apply,if_neg hn] at ho
    have h0 := defect_nonnegative G hreg hdiam x y
    have h2 := hbound x y
    have cases : defectMatrix G x y = 0 ∨ defectMatrix G x y = 1 ∨ defectMatrix G x y = 2 := by omega
    rcases cases with hc | hc | hc
    · have hcn : commonNeighborCount G x y = 1 := by omega
      norm_num [hc,hcn]
    · have hcn : commonNeighborCount G x y = 2 := by omega
      norm_num [hc,hcn]
    · have hcn : commonNeighborCount G x y = 3 := by omega
      norm_num [hc,hcn]
  have huf : (nonedgePairs G).filter (fun P => P ∈ unitNonedgePairs G) = unitNonedgePairs G := by
    ext P
    simp only [Finset.mem_filter]
    constructor
    · exact And.right
    · intro hP
      obtain ⟨x,y,hxy,hn,_,heq⟩ := (Finset.mem_filter.mp hP).2
      exact ⟨Finset.mem_filter.mpr ⟨Finset.mem_univ _,x,y,hxy,hn,heq⟩,hP⟩
  have hdf : (nonedgePairs G).filter (fun P => P ∈ doubleNonedgePairs G) = doubleNonedgePairs G := by
    ext P
    simp only [Finset.mem_filter]
    constructor
    · exact And.right
    · intro hP
      obtain ⟨x,y,hxy,hn,_,heq⟩ := (Finset.mem_filter.mp hP).2
      exact ⟨Finset.mem_filter.mpr ⟨Finset.mem_univ _,x,y,hxy,hn,heq⟩,hP⟩
  have hui : nonedgePairs G ∩ unitNonedgePairs G = unitNonedgePairs G := by
    calc
      _ = (nonedgePairs G).filter (fun P => P ∈ unitNonedgePairs G) := by ext P; simp
      _ = _ := huf
  have hdi : nonedgePairs G ∩ doubleNonedgePairs G = doubleNonedgePairs G := by
    calc
      _ = (nonedgePairs G).filter (fun P => P ∈ doubleNonedgePairs G) := by ext P; simp
      _ = _ := hdf
  rw [four_cycle_flags_card]
  calc
    _ = ∑ P ∈ nonedgePairs G, ((if P ∈ unitNonedgePairs G then 1 else 0) +
        3 * (if P ∈ doubleNonedgePairs G then 1 else 0)) := Finset.sum_congr rfl hterm
    _ = _ := by simp [Finset.sum_add_distrib,hui,hdi,Nat.mul_comm]

/-- Exact actual incidence for defect entries at most two. -/
theorem n62_double_repeat_incidence (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (hbound : ∀ x y, defectMatrix G x y ≤ 2) :
    2 * (unitNonedgePairs G).card + 4 * (doubleNonedgePairs G).card +
      6 * (G.cliqueFinset 3).card = 186 := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hsum (x : V) : ∑ y, defectMatrix G x y = 3 := by
    simpa [hcard] using defect_row_sum G hreg x
  have hvalue (x y : V) : defectMatrix G x y =
      (if defectMatrix G x y = 1 then 1 else 0) +
      2 * (if defectMatrix G x y = 2 then 1 else 0) := by
    have h0 := defect_nonnegative G hreg hdiam x y
    have h2 := hbound x y
    split_ifs <;> omega
  let U := Finset.univ.filter (fun p : V × V => defectMatrix G p.1 p.2 = 1)
  let D := Finset.univ.filter (fun p : V × V => defectMatrix G p.1 p.2 = 2)
  have hcInt : (U.card : ℤ) + 2 * D.card = 186 := by
    calc
      _ = ∑ p : V × V, defectMatrix G p.1 p.2 := by
        have hind : (∑ p : V × V, defectMatrix G p.1 p.2) =
            ∑ p : V × V, ((if defectMatrix G p.1 p.2 = 1 then (1 : ℤ) else 0) +
              2 * (if defectMatrix G p.1 p.2 = 2 then (1 : ℤ) else 0)) := by
          apply Finset.sum_congr rfl
          intro p _
          exact hvalue p.1 p.2
        rw [hind,Finset.sum_add_distrib,← Finset.mul_sum]
        simp [U,D]
      _ = ∑ x : V, ∑ y : V, defectMatrix G x y := by
        rw [← Finset.univ_product_univ,Finset.sum_product]
      _ = 186 := by simp [hsum,hcard]
  have hc : U.card + 2 * D.card = 186 := by exact_mod_cast hcInt
  have hd : Disjoint ((unitNonedgePairs G).biUnion Finset.offDiag)
      ((G.cliqueFinset 3).biUnion Finset.offDiag) := by
    apply Finset.disjoint_left.mpr
    intro p hp hq
    have hn := ((mem_unit_nonedge_offDiag G p).mp hp).2.1
    obtain ⟨T,hT,hpT⟩ := Finset.mem_biUnion.mp hq
    exact hn (triangle_edge_unit G hdeg hdiam hcard
      (SimpleGraph.mem_cliqueFinset_iff.mp hT) hpT).1
  have hu := Finset.card_union_of_disjoint hd
  rw [unit_pair_coverage G hdeg hdiam hcard,
    unit_nonedge_offDiag_card G,triangle_offDiag_card G hdeg hdiam hcard] at hu
  change U.card = _ at hu
  have hD : (doubleNonedgePairs G).biUnion Finset.offDiag = D := by
    ext p
    rw [mem_double_nonedge_offDiag]
    simp only [D,Finset.mem_filter,Finset.mem_univ,true_and]
    constructor
    · exact fun h => h.2.2
    · intro hp
      have hn : ¬ G.Adj p.1 p.2 := by
        intro ha
        have := n62_edge_defect_le_one G hdeg hdiam hcard ha
        omega
      have hne : p.1 ≠ p.2 := by
        intro hh
        rw [← hh,defect_diagonal G hreg] at hp
        omega
      exact ⟨hne,hn,hp⟩
  have hdc := double_nonedge_offDiag_card G
  rw [hD] at hdc
  omega

/-- In every legal order-62 graph with actual defect at most two, the
number of actual unordered double-repeat nonedges is odd. -/
theorem n62_double_nonedge_pair_count_odd (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (hbound : ∀ x y, defectMatrix G x y ≤ 2) :
    Odd (doubleNonedgePairs G).card := by
  obtain ⟨f,hf⟩ := n62_four_cycle_flags_even G hdeg hdiam hcard
  obtain ⟨t,ht⟩ := n62_triangle_count_even G hdeg hdiam hcard
  have hflags := n62_four_cycle_flag_incidence G hdeg hdiam hcard hbound
  have hrows := n62_double_repeat_incidence G hdeg hdiam hcard hbound
  refine ⟨(doubleNonedgePairs G).card / 2,?_⟩
  omega


/-- All actual unordered pairs whose defect entry is two, with no
nonadjacency condition built into the set being counted. -/
def doubleRepeatPairs (G : SimpleGraph V) : Finset (Finset V) :=
  Finset.univ.filter (fun P => ∃ x y, x ≠ y ∧ defectMatrix G x y = 2 ∧ P = {x,y})

/-- Every actual double repeat is a nonedge in a legal order-62 graph. -/
theorem n62_double_repeat_pairs_eq_nonedge_pairs (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) : doubleRepeatPairs G = doubleNonedgePairs G := by
  ext P
  constructor
  · intro hP
    obtain ⟨x,y,hxy,hb,heq⟩ := (Finset.mem_filter.mp hP).2
    have hn : ¬ G.Adj x y := by
      intro ha
      have := n62_edge_defect_le_one G hdeg hdiam hcard ha
      omega
    exact Finset.mem_filter.mpr ⟨Finset.mem_univ _,x,y,hxy,hn,hb,heq⟩
  · intro hP
    obtain ⟨x,y,hxy,_,hb,heq⟩ := (Finset.mem_filter.mp hP).2
    exact Finset.mem_filter.mpr ⟨Finset.mem_univ _,x,y,hxy,hb,heq⟩

/-- The number of all actual unordered double repeats is odd, from only
the original graph assumptions and the explicit bound on actual defect. -/
theorem n62_double_repeat_pair_count_odd (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (hbound : ∀ x y, defectMatrix G x y ≤ 2) :
    Odd (doubleRepeatPairs G).card := by
  rw [n62_double_repeat_pairs_eq_nonedge_pairs G hdeg hdiam hcard]
  exact n62_double_nonedge_pair_count_odd G hdeg hdiam hcard hbound

end
end DegreeDiameter

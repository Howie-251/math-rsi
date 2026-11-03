import DegreeDiameter.N62TriangleParity

namespace DegreeDiameter
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- Actual unordered nonadjacent vertex pairs with a unit defect entry. -/
def unitNonedgePairs (G : SimpleGraph V) : Finset (Finset V) :=
  Finset.univ.filter (fun P => ∃ x y, x ≠ y ∧ ¬ G.Adj x y ∧
    defectMatrix G x y = 1 ∧ P = {x,y})

/-- All actual common neighbors of every vertex of an unordered pair. -/
def oppositePair (G : SimpleGraph V) (P : Finset V) : Finset V :=
  Finset.univ.filter (fun z => ∀ x ∈ P, G.Adj x z)

@[simp] theorem mem_oppositePair (G : SimpleGraph V) (P : Finset V) (z : V) :
    z ∈ oppositePair G P ↔ ∀ x ∈ P, G.Adj x z := by simp [oppositePair]

private theorem opposite_pair_card (G : SimpleGraph V) (x y : V) :
    (oppositePair G {x,y}).card = commonNeighborCount G x y := by
  unfold commonNeighborCount
  congr 1
  ext z
  simp [oppositePair, SimpleGraph.adj_comm]

private theorem opposite_pair_card_two (G : SimpleGraph V) {x y : V}
    (hxy : x ≠ y) (hn : ¬ G.Adj x y) (hb : defectMatrix G x y = 1) :
    (oppositePair G {x,y}).card = 2 := by
  rw [opposite_pair_card]
  have hh := defect_off_diagonal G hxy
  simp only [adjacencyMatrix, SimpleGraph.adjMatrix_apply, if_neg hn] at hh
  omega

/-- Under actual simple defect, opposite common-neighbor pairs give a
fixed-point-free involution on genuine unit-repeat nonedges. -/
theorem n62_opposite_pair_properties (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (hsimple : ∀ x y, defectMatrix G x y ≤ 1)
    {P : Finset V} (hP : P ∈ unitNonedgePairs G) :
    oppositePair G P ∈ unitNonedgePairs G ∧
      oppositePair G (oppositePair G P) = P ∧ oppositePair G P ≠ P := by
  obtain ⟨x,y,hxy,hn,hb,rfl⟩ := (Finset.mem_filter.mp hP).2
  have hc := opposite_pair_card_two G hxy hn hb
  obtain ⟨r,s,hrs,heq⟩ := Finset.card_eq_two.mp hc
  have hr : G.Adj x r ∧ G.Adj y r := by
    have : r ∈ oppositePair G {x,y} := by rw [heq]; simp
    simpa using this
  have hs : G.Adj x s ∧ G.Adj y s := by
    have : s ∈ oppositePair G {x,y} := by rw [heq]; simp
    simpa using this
  have hsub : ({x,y} : Finset V) ⊆ oppositePair G {r,s} := by
    intro z hz
    simp only [Finset.mem_insert, Finset.mem_singleton] at hz
    rcases hz with rfl | rfl <;> simp [hr.1.symm, hr.2.symm, hs.1.symm, hs.2.symm]
  have hcge : 2 ≤ commonNeighborCount G r s := by
    have hh := Finset.card_le_card hsub
    simpa [hxy, opposite_pair_card] using hh
  have hnrs : ¬ G.Adj r s := by
    intro hadj
    have hh := defect_off_diagonal G hrs
    have hl := n62_edge_defect_le_one G hdeg hdiam hcard hadj
    simp only [adjacencyMatrix, SimpleGraph.adjMatrix_apply, if_pos hadj] at hh
    omega
  have hbrs : defectMatrix G r s = 1 := by
    have hh := defect_off_diagonal G hrs
    have hl := hsimple r s
    simp only [adjacencyMatrix, SimpleGraph.adjMatrix_apply, if_neg hnrs] at hh
    omega
  have hback : oppositePair G {r,s} = {x,y} := by
    apply (Finset.eq_of_subset_of_card_le hsub ?_).symm
    simp [opposite_pair_card_two G hrs hnrs hbrs, hxy]
  have hne : oppositePair G {x,y} ≠ {x,y} := by
    intro h
    have hx : x ∈ oppositePair G {x,y} := by rw [h]; simp
    have ha := (mem_oppositePair G {x,y} x).mp hx x (by simp)
    exact G.irrefl ha
  refine ⟨?_, ?_, hne⟩
  · apply Finset.mem_filter.mpr
    exact ⟨Finset.mem_univ _, r,s,hrs,hnrs,hbrs,heq⟩
  · rw [heq]
    exact hback

/-- The number of actual unordered unit-repeat nonedges is even when the
actual defect matrix is simple. This is the opposite-pair four-cycle parity
count without introducing any abstract cycle certificate. -/
theorem n62_unit_nonedge_pair_count_even (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) (hsimple : ∀ x y, defectMatrix G x y ≤ 1) :
    Even (unitNonedgePairs G).card := by
  have hzero : (∑ P ∈ unitNonedgePairs G, (1 : ZMod 2)) = 0 := by
    apply Finset.sum_involution (fun P _ => oppositePair G P)
    · intro P hP
      decide
    · intro P hP _
      exact (n62_opposite_pair_properties G hdeg hdiam hcard hsimple hP).2.2
    · intro P hP
      exact (n62_opposite_pair_properties G hdeg hdiam hcard hsimple hP).1
    · intro P hP
      exact (n62_opposite_pair_properties G hdeg hdiam hcard hsimple hP).2.1
  apply ZMod.natCast_eq_zero_iff_even.mp
  simpa using hzero

end
end DegreeDiameter

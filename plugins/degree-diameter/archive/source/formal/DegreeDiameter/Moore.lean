import DegreeDiameter.Definitions
import Mathlib.Algebra.Order.BigOperators.Group.Finset

namespace DegreeDiameter

attribute [local instance] Classical.propDecidable

/-- Counting genuine paths from an arbitrary root, retaining its actual degree. -/
theorem card_le_one_add_eight_mul_degree {V : Type*} [Fintype V]
    (G : SimpleGraph V) (hdeg : degreeAtMostEight G)
    (hdiam : diameterAtMostTwo G) (r : V) :
    Fintype.card V ≤ 1 + 8 * G.degree r := by
  classical
  let N := G.neighborFinset r
  let S := N.biUnion (fun u => (G.neighborFinset u).erase r)
  have hcover : (Finset.univ : Finset V) ⊆ insert r (N ∪ S) := by
    intro v _
    by_cases hvr : v = r
    · simp [hvr]
    apply Finset.mem_insert_of_mem
    rcases hdiam r v (Ne.symm hvr) with hrv | ⟨u, hru, huv⟩
    · apply Finset.mem_union_left
      simpa [N] using hrv
    · apply Finset.mem_union_right
      apply Finset.mem_biUnion.mpr
      refine ⟨u, ?_, ?_⟩
      · simpa [N] using hru
      · simpa using And.intro hvr huv
  have hbranch : S.card ≤ N.card * 7 := by
    apply Finset.card_biUnion_le_card_mul
    intro u hu
    have hru : G.Adj r u := by simpa [N] using hu
    have hrmem : r ∈ G.neighborFinset u := by simpa using hru.symm
    rw [Finset.card_erase_of_mem hrmem]
    exact Nat.sub_le_sub_right (hdeg u) 1
  have hcount := Finset.card_le_card hcover
  have hinsert := Finset.card_insert_le r (N ∪ S)
  have hunion := Finset.card_union_le N S
  have hN : N.card = G.degree r := rfl
  simp only [Finset.card_univ] at hcount
  omega

/-- The Moore bound, covering every finite simple graph in the original domain. -/
theorem moore_bound {V : Type*} [Fintype V]
    (G : SimpleGraph V) (hdeg : degreeAtMostEight G)
    (hdiam : diameterAtMostTwo G) : Fintype.card V ≤ 65 := by
  classical
  cases isEmpty_or_nonempty V with
  | inl hempty => simp
  | inr hnonempty =>
    obtain ⟨r⟩ := hnonempty
    have hroot := card_le_one_add_eight_mul_degree G hdeg hdiam r
    have hdegree := hdeg r
    omega

/-- Above order 57, regularity follows from the original bounds. -/
theorem regular_of_card_gt_57 {V : Type*} [Fintype V]
    (G : SimpleGraph V) (hdeg : degreeAtMostEight G)
    (hdiam : diameterAtMostTwo G) (hcard : 57 < Fintype.card V) :
    G.IsRegularOfDegree 8 := by
  classical
  intro r
  have hroot := card_le_one_add_eight_mul_degree G hdeg hdiam r
  have hdegree := hdeg r
  omega

/-- The order predicate connects to the graph-level Moore bound. -/
theorem exists82_le_65 {n : ℕ} (h : Exists82 n) : n ≤ 65 := by
  obtain ⟨V, fV, G, hcard, hdeg, hdiam⟩ := h
  letI := fV
  simpa [hcard] using moore_bound G hdeg hdiam

end DegreeDiameter

import DegreeDiameter.Moore65
import DegreeDiameter.MatchingZero

namespace DegreeDiameter

open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section

variable {V : Type*} [Fintype V]

theorem defect_zero_or_one_of_card_64 (G : SimpleGraph V)
    (hreg : G.IsRegularOfDegree 8) (hdiam : diameterAtMostTwo G)
    (hn : Fintype.card V = 64) (u v : V) :
    defectMatrix G u v = 0 ∨ defectMatrix G u v = 1 := by
  have hnon := defect_nonnegative G hreg hdiam u v
  have hle : defectMatrix G u v ≤ ∑ w, defectMatrix G u w :=
    Finset.single_le_sum (fun w _ => defect_nonnegative G hreg hdiam u w)
      (Finset.mem_univ v)
  rw [defect_row_sum G hreg, hn] at hle
  omega

theorem defect_pair_le_one_of_card_64 (G : SimpleGraph V)
    (hreg : G.IsRegularOfDegree 8) (hdiam : diameterAtMostTwo G)
    (hn : Fintype.card V = 64) (r : V) {u v : V} (huv : u ≠ v) :
    defectMatrix G r u + defectMatrix G r v ≤ 1 := by
  have hle : ∑ w ∈ ({u, v} : Finset V), defectMatrix G r w ≤
      ∑ w, defectMatrix G r w :=
    Finset.sum_le_sum_of_subset_of_nonneg (Finset.subset_univ _)
      (fun w _ _ => defect_nonnegative G hreg hdiam r w)
  simpa [huv, defect_row_sum G hreg, hn] using hle

/-- The actual defect matrix is an involutory permutation matrix at order 64. -/
theorem defect_square_identity_of_card_64 (G : SimpleGraph V)
    (hreg : G.IsRegularOfDegree 8) (hdiam : diameterAtMostTwo G)
    (hn : Fintype.card V = 64) :
    defectMatrix G * defectMatrix G = (1 : Matrix V V ℤ) := by
  ext u v
  by_cases huv : u = v
  · subst v
    rw [Matrix.one_apply_eq, Matrix.mul_apply]
    calc
      ∑ w, defectMatrix G u w * defectMatrix G w u = ∑ w, defectMatrix G u w := by
        apply Finset.sum_congr rfl
        intro w _
        rw [(defect_symmetric G).apply u w]
        rcases defect_zero_or_one_of_card_64 G hreg hdiam hn u w with h | h <;> simp [h]
      _ = 1 := by rw [defect_row_sum G hreg, hn]; norm_num
  · rw [Matrix.one_apply_ne huv, Matrix.mul_apply]
    apply Finset.sum_eq_zero
    intro w _
    rcases defect_zero_or_one_of_card_64 G hreg hdiam hn u w with hu | hu
    · simp [hu]
    rcases defect_zero_or_one_of_card_64 G hreg hdiam hn w v with hv | hv
    · simp [hv]
    have hwu : defectMatrix G w u = 1 := by
      rw [(defect_symmetric G).apply u w]
      exact hu
    have hpair := defect_pair_le_one_of_card_64 G hreg hdiam hn w huv
    rw [hwu, hv] at hpair
    norm_num at hpair

/-- A triangle would force two positive entries in one actual defect row. -/
theorem triangle_free_of_card_64 (G : SimpleGraph V)
    (hreg : G.IsRegularOfDegree 8) (hdiam : diameterAtMostTwo G)
    (hn : Fintype.card V = 64) : triangleFree G := by
  intro u v w huv hvw hwu
  have hcuv : 0 < commonNeighborCount G u v := by
    apply Finset.card_pos.mpr
    exact ⟨w, by simp [hwu.symm, hvw.symm]⟩
  have hcuw : 0 < commonNeighborCount G u w := by
    apply Finset.card_pos.mpr
    exact ⟨v, by simp [huv, hvw]⟩
  have hbuv : 1 ≤ defectMatrix G u v := by
    rw [defect_off_diagonal G huv.ne]
    simp only [adjacencyMatrix, SimpleGraph.adjMatrix_apply, if_pos huv]
    omega
  have hbuw : 1 ≤ defectMatrix G u w := by
    rw [defect_off_diagonal G hwu.ne']
    simp only [adjacencyMatrix, SimpleGraph.adjMatrix_apply, if_pos hwu.symm]
    omega
  have hp := defect_pair_le_one_of_card_64 G hreg hdiam hn u hvw.ne
  omega

theorem adjacency_defect_trace_zero_of_triangle_free (G : SimpleGraph V)
    (ht : triangleFree G) : trace (adjacencyMatrix G * defectMatrix G) = 0 := by
  apply Finset.sum_eq_zero
  intro v _
  simp only [Matrix.diag_apply, Matrix.mul_apply]
  apply Finset.sum_eq_zero
  intro u _
  by_cases ha : G.Adj v u
  · have hc : commonNeighborCount G u v = 0 := by
      apply Finset.card_eq_zero.mpr
      apply Finset.eq_empty_iff_forall_notMem.mpr
      intro w hw
      have hw' : G.Adj u w ∧ G.Adj w v := by simpa using hw
      exact ht u w v hw'.1 hw'.2 ha
    have hb : defectMatrix G u v = 0 := by
      rw [defect_off_diagonal G ha.ne', hc]
      simp [adjacencyMatrix, ha.symm]
    simp [hb]
  · simp [adjacencyMatrix, ha]

end
end DegreeDiameter

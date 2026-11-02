import DegreeDiameter.TraceFive

namespace DegreeDiameter

open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section

variable {V : Type*} [Fintype V]

/-- Absence of a triangle stated solely in terms of actual graph edges. -/
def triangleFree (G : SimpleGraph V) : Prop :=
  ∀ u v w, G.Adj u v → G.Adj v w → ¬ G.Adj w u

/-- A real 2211 defect row, supported on four distinct vertices inducing two
same-weight edges. No trace or moment equality is part of this definition. -/
def matchingRow (G : SimpleGraph V) (v : V) : Prop :=
  ∃ a b c d : V,
    a ≠ b ∧ a ≠ c ∧ a ≠ d ∧ b ≠ c ∧ b ≠ d ∧ c ≠ d ∧
    (∀ u, defectMatrix G v u = (if u = a then 2 else 0) +
      (if u = b then 2 else 0) + (if u = c then 1 else 0) +
      (if u = d then 1 else 0)) ∧
    G.Adj a b ∧ G.Adj c d ∧ ¬ G.Adj a c ∧ ¬ G.Adj a d ∧
    ¬ G.Adj b c ∧ ¬ G.Adj b d

private theorem row_sum_four (r x : V → ℤ) (a b c d : V)
    (hr : ∀ u, r u = (if u = a then 2 else 0) +
      (if u = b then 2 else 0) + (if u = c then 1 else 0) +
      (if u = d then 1 else 0)) :
    ∑ u, r u * x u = 2 * x a + 2 * x b + x c + x d := by
  simp_rw [hr, add_mul, ite_mul]
  simp [Finset.sum_add_distrib]

theorem matching_row_square (G : SimpleGraph V) (v : V) (h : matchingRow G v) :
    (defectMatrix G ^ 2) v v = 10 := by
  obtain ⟨a, b, c, d, hab, hac, had, hbc, hbd, hcd, hr, _⟩ := h
  simp only [pow_two, Matrix.mul_apply]
  simp_rw [(defect_symmetric G).apply v]
  rw [row_sum_four (defectMatrix G v) (defectMatrix G v) a b c d hr]
  simp [hr, hab, hac, had, hbc, hbd, hcd, Ne.symm hab, Ne.symm hac,
    Ne.symm had, Ne.symm hbc, Ne.symm hbd, Ne.symm hcd]

theorem matching_row_quadratic (G : SimpleGraph V) (v : V) (h : matchingRow G v) :
    (defectMatrix G * adjacencyMatrix G * defectMatrix G) v v = 10 := by
  obtain ⟨a, b, c, d, hab, hac, had, hbc, hbd, hcd, hr,
    eab, ecd, nac, nad, nbc, nbd⟩ := h
  have hm (u : V) : (defectMatrix G * adjacencyMatrix G) v u =
      2 * adjacencyMatrix G a u + 2 * adjacencyMatrix G b u +
      adjacencyMatrix G c u + adjacencyMatrix G d u := by
    exact row_sum_four (defectMatrix G v) (fun w => adjacencyMatrix G w u) a b c d hr
  rw [Matrix.mul_apply]
  simp_rw [hm, (defect_symmetric G).apply v]
  simp_rw [mul_comm _ (defectMatrix G v _)]
  rw [row_sum_four (defectMatrix G v) _ a b c d hr]
  have nba : G.Adj b a := eab.symm
  have ndc : G.Adj d c := ecd.symm
  have nca : ¬ G.Adj c a := fun h => nac h.symm
  have nda : ¬ G.Adj d a := fun h => nad h.symm
  have ncb : ¬ G.Adj c b := fun h => nbc h.symm
  have ndb : ¬ G.Adj d b := fun h => nbd h.symm
  simp [adjacencyMatrix, eab, ecd, nac, nad, nbc, nbd, nba, ndc, nca, nda, ncb, ndb]

theorem matching_rows_square_trace (G : SimpleGraph V) (h : ∀ v, matchingRow G v) :
    trace (defectMatrix G ^ 2) = 10 * (Fintype.card V : ℤ) := by
  simp [trace, diag_apply, matching_row_square G _ (h _), mul_comm]

theorem matching_rows_mixed_trace (G : SimpleGraph V) (h : ∀ v, matchingRow G v) :
    trace (adjacencyMatrix G * defectMatrix G ^ 2) = 10 * (Fintype.card V : ℤ) := by
  rw [pow_two, ← Matrix.mul_assoc, Matrix.trace_mul_cycle]
  simp [trace, diag_apply, matching_row_quadratic G _ (h _), mul_comm]

theorem triangle_free_cube_trace (G : SimpleGraph V) (h : triangleFree G) :
    trace (adjacencyMatrix G ^ 3) = 0 := by
  apply Finset.sum_eq_zero
  intro v _
  simp only [Matrix.diag_apply]
  rw [show (3 : ℕ) = 2 + 1 from rfl, pow_succ, pow_two]
  simp only [Matrix.mul_apply]
  apply Finset.sum_eq_zero
  intro u _
  by_cases huv : G.Adj u v
  · have hcount : commonNeighborCount G v u = 0 := by
      apply Finset.card_eq_zero.mpr
      apply Finset.eq_empty_iff_forall_notMem.mpr
      intro w hw
      have hw' : G.Adj v w ∧ G.Adj w u := by simpa using hw
      exact h v w u hw'.1 hw'.2 huv
    have hprod := adjacency_sq_common_count G v u
    simp only [Matrix.mul_apply] at hprod
    rw [hcount] at hprod
    rw [hprod]
    simp
  · simp [adjacencyMatrix, huv]

/-- Genuine graph-level conditional exclusion: matching-row semantics and
triangle absence imply the trace hypotheses, rather than assuming the moments. -/
theorem no_n59_triangle_free_matching_rows (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hn : Fintype.card V = 59) (ht : triangleFree G)
    (hm : ∀ v, matchingRow G v) : False := by
  apply no_n59_with_matching_zero_traces G hdeg hdiam hn
  · exact triangle_free_cube_trace G ht
  · simpa [hn] using matching_rows_square_trace G hm
  · simpa [hn] using matching_rows_mixed_trace G hm

end
end DegreeDiameter

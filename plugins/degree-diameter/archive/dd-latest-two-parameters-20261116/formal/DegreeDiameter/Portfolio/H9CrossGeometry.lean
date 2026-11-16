import DegreeDiameter.Portfolio.H9CrossRouting

namespace DegreeDiameter.Portfolio.H9CrossGeometry
open H9CrossRouting
variable {K : Type*} [Field K]

theorem cross_right_scalar (p q : Vec7 K) (a : K) :
    cross p (fun i => a * q i) = fun i => a * cross p q i := by
  funext i
  fin_cases i <;> simp [cross] <;> ring

theorem nonzero_cross_not_left_multiple (h3 : (3 : K) = 0)
    (p q : Vec7 K) (hy : cross p q ≠ 0)
    (hqy : cross q (cross p q) = 0) (a : K) :
    cross p q ≠ (fun i => a * p i) := by
  intro heq
  have ha : a ≠ 0 := by
    intro ha
    apply hy
    rw [heq]
    funext i
    simp [ha]
  have hz : (fun i => a * cross q p i) = 0 := by
    rw [← cross_right_scalar, ← heq]
    exact hqy
  have hqp : cross q p = 0 := by
    funext i
    have hi := congrFun hz i
    exact (mul_eq_zero.mp hi).resolve_left ha
  apply hy
  have hs := skew h3 p q
  rw [hqp] at hs
  exact neg_eq_zero.mp hs.symm

theorem nonzero_cross_not_right_multiple
    (p q : Vec7 K) (hy : cross p q ≠ 0)
    (hpy : cross p (cross p q) = 0) (a : K) :
    cross p q ≠ (fun i => a * q i) := by
  intro heq
  have ha : a ≠ 0 := by
    intro ha
    apply hy
    rw [heq]
    funext i
    simp [ha]
  have hz : (fun i => a * cross p q i) = 0 := by
    rw [← cross_right_scalar, ← heq]
    exact hpy
  apply hy
  funext i
  have hi := congrFun hz i
  exact (mul_eq_zero.mp hi).resolve_left ha

/-- A nonzero cross witness is a genuinely different projective point. -/
theorem null_polar_projective_common_neighbor (h3 : (3 : K) = 0)
    (p q : Vec7 K) (hp : norm p = 0) (hq : norm q = 0)
    (hb : polar p q = 0) (hy : cross p q ≠ 0) :
    norm (cross p q) = 0 ∧
    cross p (cross p q) = 0 ∧ cross q (cross p q) = 0 ∧
    (∀ a : K, cross p q ≠ (fun i => a * p i)) ∧
    (∀ a : K, cross p q ≠ (fun i => a * q i)) := by
  obtain ⟨hn, hpy, hqy⟩ := null_polar_common_neighbor h3 p q hp hq hb
  exact ⟨hn, hpy, hqy,
    nonzero_cross_not_left_multiple h3 p q hy hqy,
    nonzero_cross_not_right_multiple p q hy hpy⟩


theorem polar_linear_combination (p r w : Vec7 K) (a b : K) :
    polar p (fun i => a * r i + b * w i) = a * polar p r + b * polar p w := by
  simp [polar]
  ring

theorem norm_linear_combination (r w : Vec7 K) (a b : K) :
    norm (fun i => a * r i + b * w i) =
      a ^ 2 * norm r + a * b * polar r w + b ^ 2 * norm w := by
  simp [norm, polar]
  ring

/-- On a null cross-zero projective line, every point has an orthogonal
nonzero point, with an explicit two-coefficient construction. -/
theorem line_orthogonal_projection (h3 : (3 : K) = 0)
    (p r w : Vec7 K) (hr : norm r = 0) (hw : norm w = 0)
    (hc : cross r w = 0)
    (hi : ∀ a b : K, (fun i => a * r i + b * w i) = 0 → a = 0 ∧ b = 0) :
    ∃ a b : K, (fun i => a * r i + b * w i) ≠ 0 ∧
      polar p (fun i => a * r i + b * w i) = 0 ∧
      norm (fun i => a * r i + b * w i) = 0 := by
  have hrw : polar r w = 0 := by
    have hn := norm_cross h3 r w
    rw [hc, hr, hw] at hn
    have hn0 : norm (0 : Vec7 K) = 0 := by simp [norm]
    rw [hn0, zero_mul, zero_sub] at hn
    have hs : (polar r w) ^ 2 = 0 := neg_eq_zero.mp hn.symm
    rcases mul_eq_zero.mp (show polar r w * polar r w = 0 by
      simpa [pow_two] using hs) with h | h
    · exact h
    · exact h
  by_cases hpr : polar p r = 0
  · refine ⟨1, 0, ?_, ?_, ?_⟩
    · intro hz
      exact one_ne_zero (hi 1 0 hz).1
    · simpa using hpr
    · simpa using hr
  · refine ⟨polar p w, -(polar p r), ?_, ?_, ?_⟩
    · intro hz
      have h := (hi (polar p w) (-(polar p r)) hz).2
      exact hpr (neg_eq_zero.mp h)
    · rw [polar_linear_combination]
      ring
    · rw [norm_linear_combination, hr, hw, hrw]
      ring

end DegreeDiameter.Portfolio.H9CrossGeometry

#print axioms DegreeDiameter.Portfolio.H9CrossGeometry.cross_right_scalar
#print axioms DegreeDiameter.Portfolio.H9CrossGeometry.nonzero_cross_not_left_multiple
#print axioms DegreeDiameter.Portfolio.H9CrossGeometry.nonzero_cross_not_right_multiple
#print axioms DegreeDiameter.Portfolio.H9CrossGeometry.null_polar_projective_common_neighbor

#print axioms DegreeDiameter.Portfolio.H9CrossGeometry.line_orthogonal_projection

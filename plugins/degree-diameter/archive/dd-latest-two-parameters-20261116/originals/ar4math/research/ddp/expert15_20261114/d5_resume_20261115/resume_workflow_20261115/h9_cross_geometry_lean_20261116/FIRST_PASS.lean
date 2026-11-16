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

end DegreeDiameter.Portfolio.H9CrossGeometry

#print axioms DegreeDiameter.Portfolio.H9CrossGeometry.cross_right_scalar
#print axioms DegreeDiameter.Portfolio.H9CrossGeometry.nonzero_cross_not_left_multiple
#print axioms DegreeDiameter.Portfolio.H9CrossGeometry.nonzero_cross_not_right_multiple
#print axioms DegreeDiameter.Portfolio.H9CrossGeometry.null_polar_projective_common_neighbor

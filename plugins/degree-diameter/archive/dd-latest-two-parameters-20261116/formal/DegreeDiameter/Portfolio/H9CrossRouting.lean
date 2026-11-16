import Mathlib.Tactic.Ring
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic.FinCases

/-! Exact universal characteristic-three cross identities. No graph diameter premise. -/
namespace DegreeDiameter.Portfolio.H9CrossRouting
variable {K : Type*} [CommRing K]
abbrev Vec7 (K : Type*) := Fin 7 → K
def norm (p : Vec7 K) : K := (p 0) * (p 4) + (p 1) * (p 5) + (p 2) * (p 6) - (p 3) ^ 2
def polar (p q : Vec7 K) : K := (p 0) * (q 4) + (p 1) * (q 5) + (p 2) * (q 6) - 2 * (p 3) * (q 3) + (p 4) * (q 0) + (p 5) * (q 1) + (p 6) * (q 2)
def cross (p q : Vec7 K) : Vec7 K := ![-(p 0) * (q 3) + (p 3) * (q 0) + (p 5) * (q 6) - (p 6) * (q 5), -(p 1) * (q 3) + (p 3) * (q 1) - (p 4) * (q 6) + (p 6) * (q 4), -(p 2) * (q 3) + (p 3) * (q 2) + (p 4) * (q 5) - (p 5) * (q 4), (p 0) * (q 4) + (p 1) * (q 5) + (p 2) * (q 6) - (p 4) * (q 0) - (p 5) * (q 1) - (p 6) * (q 2), (p 1) * (q 2) - (p 2) * (q 1) - (p 3) * (q 4) + (p 4) * (q 3), -(p 0) * (q 2) + (p 2) * (q 0) - (p 3) * (q 5) + (p 5) * (q 3), (p 0) * (q 1) - (p 1) * (q 0) - (p 3) * (q 6) + (p 6) * (q 3)]

theorem square_0 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross p (cross p q) 0 = -(polar p q) * p 0 - norm p * q 0 := by
  have h : cross p (cross p q) 0 - (-(polar p q) * p 0 - norm p * q 0) = (3 : K) * (-(p 0) * (p 3) * (q 3) + (p 0) * (p 4) * (q 0) + (p 0) * (p 5) * (q 1) + (p 0) * (p 6) * (q 2)) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem square_1 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross p (cross p q) 1 = -(polar p q) * p 1 - norm p * q 1 := by
  have h : cross p (cross p q) 1 - (-(polar p q) * p 1 - norm p * q 1) = (3 : K) * (-(p 1) * (p 3) * (q 3) + (p 1) * (p 4) * (q 0) + (p 1) * (p 5) * (q 1) + (p 1) * (p 6) * (q 2)) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem square_2 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross p (cross p q) 2 = -(polar p q) * p 2 - norm p * q 2 := by
  have h : cross p (cross p q) 2 - (-(polar p q) * p 2 - norm p * q 2) = (3 : K) * (-(p 2) * (p 3) * (q 3) + (p 2) * (p 4) * (q 0) + (p 2) * (p 5) * (q 1) + (p 2) * (p 6) * (q 2)) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem square_3 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross p (cross p q) 3 = -(polar p q) * p 3 - norm p * q 3 := by
  have h : cross p (cross p q) 3 - (-(polar p q) * p 3 - norm p * q 3) = (3 : K) * ((p 0) * (p 4) * (q 3) + (p 1) * (p 5) * (q 3) + (p 2) * (p 6) * (q 3) - (p 3) ^ 2 * (q 3)) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem square_4 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross p (cross p q) 4 = -(polar p q) * p 4 - norm p * q 4 := by
  have h : cross p (cross p q) 4 - (-(polar p q) * p 4 - norm p * q 4) = (3 : K) * ((p 0) * (p 4) * (q 4) + (p 1) * (p 4) * (q 5) + (p 2) * (p 4) * (q 6) - (p 3) * (p 4) * (q 3)) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem square_5 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross p (cross p q) 5 = -(polar p q) * p 5 - norm p * q 5 := by
  have h : cross p (cross p q) 5 - (-(polar p q) * p 5 - norm p * q 5) = (3 : K) * ((p 0) * (p 5) * (q 4) + (p 1) * (p 5) * (q 5) + (p 2) * (p 5) * (q 6) - (p 3) * (p 5) * (q 3)) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem square_6 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross p (cross p q) 6 = -(polar p q) * p 6 - norm p * q 6 := by
  have h : cross p (cross p q) 6 - (-(polar p q) * p 6 - norm p * q 6) = (3 : K) * ((p 0) * (p 6) * (q 4) + (p 1) * (p 6) * (q 5) + (p 2) * (p 6) * (q 6) - (p 3) * (p 6) * (q 3)) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem norm_cross (h3 : (3 : K) = 0) (p q : Vec7 K) :
    norm (cross p q) = norm p * norm q - (polar p q) ^ 2 := by
  have h : norm (cross p q) - (norm p * norm q - (polar p q) ^ 2) = (3 : K) * (-(p 0) * (p 3) * (q 3) * (q 4) + (p 0) * (p 4) * (q 0) * (q 4) + (p 0) * (p 5) * (q 1) * (q 4) + (p 0) * (p 6) * (q 2) * (q 4) - (p 1) * (p 3) * (q 3) * (q 5) + (p 1) * (p 4) * (q 0) * (q 5) + (p 1) * (p 5) * (q 1) * (q 5) + (p 1) * (p 6) * (q 2) * (q 5) - (p 2) * (p 3) * (q 3) * (q 6) + (p 2) * (p 4) * (q 0) * (q 6) + (p 2) * (p 5) * (q 1) * (q 6) + (p 2) * (p 6) * (q 2) * (q 6) + (p 3) ^ 2 * (q 3) ^ 2 - (p 3) * (p 4) * (q 0) * (q 3) - (p 3) * (p 5) * (q 1) * (q 3) - (p 3) * (p 6) * (q 2) * (q 3)) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem skew_0 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross q p 0 = -(cross p q 0) := by
  have h : cross q p 0 - (-(cross p q 0)) = (3 : K) * (0) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem skew_1 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross q p 1 = -(cross p q 1) := by
  have h : cross q p 1 - (-(cross p q 1)) = (3 : K) * (0) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem skew_2 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross q p 2 = -(cross p q 2) := by
  have h : cross q p 2 - (-(cross p q 2)) = (3 : K) * (0) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem skew_3 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross q p 3 = -(cross p q 3) := by
  have h : cross q p 3 - (-(cross p q 3)) = (3 : K) * (0) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem skew_4 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross q p 4 = -(cross p q 4) := by
  have h : cross q p 4 - (-(cross p q 4)) = (3 : K) * (0) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem skew_5 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross q p 5 = -(cross p q 5) := by
  have h : cross q p 5 - (-(cross p q 5)) = (3 : K) * (0) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem skew_6 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross q p 6 = -(cross p q 6) := by
  have h : cross q p 6 - (-(cross p q 6)) = (3 : K) * (0) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem polar_left_cross (h3 : (3 : K) = 0) (p q : Vec7 K) :
    polar p (cross p q) = 0 := by
  have h : polar p (cross p q) - (0) = (3 : K) * (-(p 0) * (p 3) * (q 4) - (p 1) * (p 3) * (q 5) - (p 2) * (p 3) * (q 6) + (p 3) * (p 4) * (q 0) + (p 3) * (p 5) * (q 1) + (p 3) * (p 6) * (q 2)) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem polar_right_cross (h3 : (3 : K) = 0) (p q : Vec7 K) :
    polar q (cross p q) = 0 := by
  have h : polar q (cross p q) - (0) = (3 : K) * (-(p 0) * (q 3) * (q 4) - (p 1) * (q 3) * (q 5) - (p 2) * (q 3) * (q 6) + (p 4) * (q 0) * (q 3) + (p 5) * (q 1) * (q 3) + (p 6) * (q 2) * (q 3)) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem tits_0 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross p q 0 = -(p 0) * (q 3) + (p 3) * (q 0) + (p 5) * (q 6) - (p 6) * (q 5) := by
  have h : cross p q 0 - (-(p 0) * (q 3) + (p 3) * (q 0) + (p 5) * (q 6) - (p 6) * (q 5)) = (3 : K) * (0) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem tits_1 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross p q 1 = -(p 1) * (q 3) + (p 3) * (q 1) - (p 4) * (q 6) + (p 6) * (q 4) := by
  have h : cross p q 1 - (-(p 1) * (q 3) + (p 3) * (q 1) - (p 4) * (q 6) + (p 6) * (q 4)) = (3 : K) * (0) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem tits_2 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross p q 2 = -(p 2) * (q 3) + (p 3) * (q 2) + (p 4) * (q 5) - (p 5) * (q 4) := by
  have h : cross p q 2 - (-(p 2) * (q 3) + (p 3) * (q 2) + (p 4) * (q 5) - (p 5) * (q 4)) = (3 : K) * (0) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem tits_3 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross p q 4 = (p 1) * (q 2) - (p 2) * (q 1) - (p 3) * (q 4) + (p 4) * (q 3) := by
  have h : cross p q 4 - ((p 1) * (q 2) - (p 2) * (q 1) - (p 3) * (q 4) + (p 4) * (q 3)) = (3 : K) * (0) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem tits_4 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross p q 5 = -(p 0) * (q 2) + (p 2) * (q 0) - (p 3) * (q 5) + (p 5) * (q 3) := by
  have h : cross p q 5 - (-(p 0) * (q 2) + (p 2) * (q 0) - (p 3) * (q 5) + (p 5) * (q 3)) = (3 : K) * (0) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem tits_5 (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross p q 6 = (p 0) * (q 1) - (p 1) * (q 0) - (p 3) * (q 6) + (p 6) * (q 3) := by
  have h : cross p q 6 - ((p 0) * (q 1) - (p 1) * (q 0) - (p 3) * (q 6) + (p 6) * (q 3)) = (3 : K) * (0) := by
    simp [cross, norm, polar] <;> ring
  apply sub_eq_zero.mp
  rw [h, h3, zero_mul]

theorem square (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross p (cross p q) = fun i => -(polar p q) * p i - norm p * q i := by
  funext i
  fin_cases i
  · exact square_0 h3 p q
  · exact square_1 h3 p q
  · exact square_2 h3 p q
  · exact square_3 h3 p q
  · exact square_4 h3 p q
  · exact square_5 h3 p q
  · exact square_6 h3 p q

theorem skew (h3 : (3 : K) = 0) (p q : Vec7 K) :
    cross q p = -(cross p q) := by
  funext i
  fin_cases i
  · exact skew_0 h3 p q
  · exact skew_1 h3 p q
  · exact skew_2 h3 p q
  · exact skew_3 h3 p q
  · exact skew_4 h3 p q
  · exact skew_5 h3 p q
  · exact skew_6 h3 p q

theorem null_polar_cross_witness (h3 : (3 : K) = 0) (p q : Vec7 K)
    (hp : norm p = 0) (hq : norm q = 0) (hb : polar p q = 0) :
    norm (cross p q) = 0 ∧ cross p (cross p q) = 0 := by
  constructor
  · rw [norm_cross h3, hp, hq, hb]; ring
  · rw [square h3]; funext i; simp [hp, hb]

/- This final common-neighbor packaging was added after the bounded compile
timed out; neither it nor the earlier identities are claimed kernel-checked. -/
theorem cross_inner_skew (p q : Vec7 K) :
    cross q (cross p q) = -(cross q (cross q p)) := by
  funext i
  fin_cases i <;> simp [cross] <;> ring

theorem null_polar_common_neighbor (h3 : (3 : K) = 0) (p q : Vec7 K)
    (hp : norm p = 0) (hq : norm q = 0) (hb : polar p q = 0) :
    norm (cross p q) = 0 ∧ cross p (cross p q) = 0 ∧ cross q (cross p q) = 0 := by
  obtain ⟨hc, hpc⟩ := null_polar_cross_witness h3 p q hp hq hb
  refine ⟨hc, hpc, ?_⟩
  have hbq : polar q p = 0 := by
    calc
      polar q p = polar p q := by simp [polar] <;> ring
      _ = 0 := hb
  have hqc : cross q (cross q p) = 0 :=
    (null_polar_cross_witness h3 q p hq hp hbq).2
  rw [cross_inner_skew, hqc, neg_zero]

end DegreeDiameter.Portfolio.H9CrossRouting

#print axioms DegreeDiameter.Portfolio.H9CrossRouting.square
#print axioms DegreeDiameter.Portfolio.H9CrossRouting.norm_cross
#print axioms DegreeDiameter.Portfolio.H9CrossRouting.skew
#print axioms DegreeDiameter.Portfolio.H9CrossRouting.null_polar_cross_witness
#print axioms DegreeDiameter.Portfolio.H9CrossRouting.null_polar_common_neighbor

import DegreeDiameter.N62RepeatQuotient
import Mathlib.LinearAlgebra.Matrix.Charpoly.FiniteField
import Mathlib.Tactic.NoncommRing

namespace DegreeDiameter
open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
set_option maxRecDepth 10000
noncomputable section
variable {V : Type*} [Fintype V]

/-- A kernel-checked finite-field trace consequence of the indicated cubic identity. -/
theorem cubic_157604_trace_mod_1063 (P : Matrix V V ℤ)
    (hcube : P ^ 3 = (157604 : ℤ) • P) : (1063 : ℤ) ∣ trace P := by
  letI : Fact (Nat.Prime 1063) := ⟨by decide⟩
  let f : ℤ →+* ZMod 1063 := Int.castRingHom (ZMod 1063)
  let M := f.mapMatrix P
  have hM : M ^ 3 = (157604 : ZMod 1063) • M := by
    have hh := congrArg f.mapMatrix hcube
    simp only [map_pow,map_zsmul] at hh
    calc
      _ = (157604 : ℤ) • M := hh
      _ = _ := by ext x y; simp [Matrix.smul_apply,zsmul_eq_mul]
  have hp (k : ℕ) : M ^ (2 * k + 1) = (157604 : ZMod 1063) ^ k • M := by
    induction k with
    | zero => simp
    | succ k ih =>
      calc
        _ = M ^ (2*k+1) * M ^ 2 := by rw [← pow_add]; congr 1
        _ = (157604 : ZMod 1063) ^ k • (M * M ^ 2) := by rw [ih,Matrix.smul_mul]
        _ = _ := by rw [← pow_succ',hM,smul_smul,pow_succ]
  have hcoef : (157604 : ZMod 1063) ^ 531 = -1 := by decide
  have hf := ZMod.trace_pow_card (p := 1063) M
  rw [hp 531,hcoef,trace_smul,ZMod.pow_card] at hf
  simp only [smul_eq_mul] at hf
  have ht : trace M = 0 := by
    have htwo : (2 : ZMod 1063) * trace M = 0 := by
      calc
        _ = trace M - (-1 * trace M) := by ring
        _ = 0 := by rw [hf,sub_self]
    exact (mul_eq_zero.mp htwo).resolve_left (by decide)
  apply (ZMod.intCast_zmod_eq_zero_iff_dvd (trace P) 1063).mp
  change f (trace P) = 0
  rw [AddMonoidHom.map_trace f P]
  exact ht

/-- Actual component sizes make the quotient's rank-one size matrix square to 62 times itself. -/
theorem n62_repeat_size_matrix_square (G : SimpleGraph V)
    (hcard : Fintype.card V = 62) :
    repeatSizeMatrix G * repeatSizeMatrix G = (62 : ℤ) • repeatSizeMatrix G := by
  ext C D
  simp only [Matrix.mul_apply,repeatSizeMatrix,Matrix.smul_apply,smul_eq_mul,← Finset.sum_mul]
  have hh : (∑ E : (repeatSupport G).ConnectedComponent, (repeatComponentSize G E : ℤ)) = 62 := by
    exact_mod_cast n62_repeat_component_sizes_sum G hcard
  rw [hh]

/-- Actual quotient row sums and edge balance give both actions on the size matrix. -/
theorem n62_repeat_quotient_size_actions (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) :
    repeatQuotientMatrix G * repeatSizeMatrix G = (8 : ℤ) • repeatSizeMatrix G ∧
    repeatSizeMatrix G * repeatQuotientMatrix G = (8 : ℤ) • repeatSizeMatrix G := by
  constructor
  · ext C D
    simp only [Matrix.mul_apply,repeatSizeMatrix,Matrix.smul_apply,smul_eq_mul,← Finset.sum_mul]
    rw [n62_repeat_quotient_row_sum G hdeg hdiam hcard C]
  · ext C D
    simp only [Matrix.mul_apply,repeatSizeMatrix,Matrix.smul_apply,smul_eq_mul]
    simp_rw [n62_repeat_quotient_balance G hdeg hdiam hcard]
    rw [← Finset.mul_sum,n62_repeat_quotient_row_sum G hdeg hdiam hcard D,mul_comm]

/-- The integral centered transform of the actual quotient. -/
def centeredRepeatQuotient (G : SimpleGraph V) :
    Matrix (repeatSupport G).ConnectedComponent (repeatSupport G).ConnectedComponent ℤ :=
  (62 : ℤ) • ((2 : ℤ) • repeatQuotientMatrix G + 1) - (17 : ℤ) • repeatSizeMatrix G

/-- Centering removes the eigenvalue 17 from 2R+I, using only actual quotient identities. -/
theorem n62_centered_repeat_quotient_cubic (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) :
    centeredRepeatQuotient G ^ 3 = (157604 : ℤ) • centeredRepeatQuotient G := by
  let R := repeatQuotientMatrix G
  let N := repeatSizeMatrix G
  let S : Matrix (repeatSupport G).ConnectedComponent (repeatSupport G).ConnectedComponent ℤ :=
    (2 : ℤ) • R + 1
  have hR : R*R+R = (10 : ℤ) • 1 + N := n62_repeat_quotient_quadratic G hdeg hdiam hcard
  obtain ⟨hRN,hNR⟩ := n62_repeat_quotient_size_actions G hdeg hdiam hcard
  change R*N = (8 : ℤ) • N at hRN
  change N*R = (8 : ℤ) • N at hNR
  have hNN : N*N = (62 : ℤ) • N := n62_repeat_size_matrix_square G hcard
  have hS2 : S*S = (41 : ℤ) • 1 + (4 : ℤ) • N := by
    calc
      _ = (4 : ℤ) • (R*R+R) + 1 := by dsimp [S]; noncomm_ring
      _ = _ := by rw [hR]; abel
  have hSN : S*N = (17 : ℤ) • N := by dsimp [S]; noncomm_ring [hRN]
  have hNS : N*S = (17 : ℤ) • N := by dsimp [S]; noncomm_ring [hNR]
  have hP : centeredRepeatQuotient G = (62 : ℤ) • S - (17 : ℤ) • N := rfl
  have hP2 : centeredRepeatQuotient G ^ 2 = (157604 : ℤ) • 1 - (2542 : ℤ) • N := by
    rw [hP]
    noncomm_ring [hS2,hSN,hNS,hNN]
  have hPN : centeredRepeatQuotient G * N = 0 := by rw [hP]; noncomm_ring [hSN,hNN]
  rw [show (3 : ℕ) = 2+1 from rfl,pow_succ',hP2,mul_sub,Matrix.mul_smul,Matrix.mul_smul,
    mul_one,hPN,smul_zero,sub_zero]

/-- The actual quotient has between zero and eight times its dimension on its trace. -/
theorem n62_repeat_quotient_trace_bounds (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) :
    0 ≤ trace (repeatQuotientMatrix G) ∧
    trace (repeatQuotientMatrix G) ≤ 8 * (Fintype.card (repeatSupport G).ConnectedComponent : ℤ) := by
  constructor
  · exact Finset.sum_nonneg (fun C _ => repeat_quotient_nonnegative G C C)
  · have hb (C : (repeatSupport G).ConnectedComponent) : repeatQuotientMatrix G C C ≤ 8 := by
      have hh := Finset.single_le_sum
        (fun D (_ : D ∈ (Finset.univ : Finset (repeatSupport G).ConnectedComponent)) =>
          repeat_quotient_nonnegative G C D) (Finset.mem_univ C)
      rwa [n62_repeat_quotient_row_sum G hdeg hdiam hcard C] at hh
    calc
      _ ≤ ∑ _C : (repeatSupport G).ConnectedComponent, (8 : ℤ) :=
        Finset.sum_le_sum (fun C _ => hb C)
      _ = _ := by simp; ring

/-- Actual nonempty components bound the number of quotient indices by the original order. -/
theorem n62_repeat_component_count_le (G : SimpleGraph V) (hcard : Fintype.card V = 62) :
    Fintype.card (repeatSupport G).ConnectedComponent ≤ 62 := by
  calc
    _ = ∑ _C : (repeatSupport G).ConnectedComponent, 1 := by simp
    _ ≤ ∑ C : (repeatSupport G).ConnectedComponent, repeatComponentSize G C :=
      Finset.sum_le_sum (fun C _ => repeat_component_size_pos G C)
    _ = 62 := n62_repeat_component_sizes_sum G hcard

/-- The actual quotient satisfies c+2 trace(R)=17, derived from original graph hypotheses. -/
theorem n62_repeat_quotient_trace_identity (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) :
    (Fintype.card (repeatSupport G).ConnectedComponent : ℤ) +
      2 * trace (repeatQuotientMatrix G) = 17 := by
  letI : Fact (Nat.Prime 1063) := ⟨by decide⟩
  have htN : trace (repeatSizeMatrix G) = 62 := by
    simp only [Matrix.trace,Matrix.diag_apply,repeatSizeMatrix]
    exact_mod_cast n62_repeat_component_sizes_sum G hcard
  have htP : trace (centeredRepeatQuotient G) = 62 *
      ((Fintype.card (repeatSupport G).ConnectedComponent : ℤ) +
        2 * trace (repeatQuotientMatrix G) - 17) := by
    simp only [centeredRepeatQuotient,trace_sub,trace_smul,trace_add,trace_one,htN,smul_eq_mul]
    ring
  have hd := cubic_157604_trace_mod_1063 (centeredRepeatQuotient G)
    (n62_centered_repeat_quotient_cubic G hdeg hdiam hcard)
  rw [htP] at hd
  have hz := (ZMod.intCast_zmod_eq_zero_iff_dvd _ 1063).mpr hd
  simp only [Int.cast_mul] at hz
  have h62 : ((62 : ℤ) : ZMod 1063) ≠ 0 := by decide
  have hz' := (mul_eq_zero.mp hz).resolve_left h62
  have hd' := (ZMod.intCast_zmod_eq_zero_iff_dvd _ 1063).mp hz'
  obtain ⟨k,hk⟩ := hd'
  have hc : (Fintype.card (repeatSupport G).ConnectedComponent : ℤ) ≤ 62 := by
    exact_mod_cast n62_repeat_component_count_le G hcard
  have hc0 := Int.natCast_nonneg (Fintype.card (repeatSupport G).ConnectedComponent)
  obtain ⟨ht0,ht8⟩ := n62_repeat_quotient_trace_bounds G hdeg hdiam hcard
  omega

/-- The number of actual repeat-support components is odd. -/
theorem n62_repeat_component_count_odd (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) :
    Odd (Fintype.card (repeatSupport G).ConnectedComponent) := by
  have ht := n62_repeat_quotient_trace_identity G hdeg hdiam hcard
  have hi : Odd (Fintype.card (repeatSupport G).ConnectedComponent : ℤ) := by
    refine ⟨8 - trace (repeatQuotientMatrix G),?_⟩
    omega
  exact_mod_cast hi

end
end DegreeDiameter

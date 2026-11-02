import DegreeDiameter.TraceFive
import Mathlib.RingTheory.Norm.Defs
import Mathlib.LinearAlgebra.Matrix.Charpoly.Minpoly

namespace DegreeDiameter

open Matrix Polynomial
noncomputable section

/-- The exact norm formula needed by the n63 finite table. The power basis and
minimal polynomial are actual field data; no determinant value is assumed. -/
theorem norm_twenty_nine_add_four_gen {K : Type*} [Field K] [Algebra ℚ K]
    (pb : PowerBasis ℚ K) :
    Algebra.norm ℚ ((29 : K) + 4 * pb.gen) =
      (-4 : ℚ) ^ pb.dim * (minpoly ℚ pb.gen).eval (-29 / 4) := by
  rw [Algebra.norm_eq_matrix_det pb.basis]
  have hm : Algebra.leftMulMatrix pb.basis ((29 : K) + 4 * pb.gen) =
      (-4 : ℚ) • (Matrix.scalar (Fin pb.dim) (-29 / 4) -
        Algebra.leftMulMatrix pb.basis pb.gen) := by
    simp only [map_add, map_mul, map_ofNat]
    rw [← Matrix.diagonal_ofNat 4, ← Matrix.smul_eq_diagonal_mul]
    ext i j
    by_cases hij : i = j
    · subst j
      simp [Matrix.scalar_apply, Matrix.smul_apply, Matrix.ofNat_apply]
      ring
    · simp [Matrix.scalar_apply, Matrix.smul_apply, Matrix.ofNat_apply, hij]
  rw [hm, Matrix.det_smul, ← Matrix.eval_charpoly, charpoly_leftMulMatrix,
    Fintype.card_fin]

/-- A nonsquare value of the proved norm excludes a square discriminant in the
actual extension field. The finite table must supply the explicit premise. -/
theorem not_isSquare_discriminant_of_norm {K : Type*} [Field K] [Algebra ℚ K]
    (pb : PowerBasis ℚ K)
    (hn : ¬ IsSquare ((-4 : ℚ) ^ pb.dim * (minpoly ℚ pb.gen).eval (-29 / 4))) :
    ¬ IsSquare ((29 : K) + 4 * pb.gen) := by
  intro h
  apply hn
  rw [← norm_twenty_nine_add_four_gen pb]
  exact h.map (Algebra.norm ℚ)

end
end DegreeDiameter

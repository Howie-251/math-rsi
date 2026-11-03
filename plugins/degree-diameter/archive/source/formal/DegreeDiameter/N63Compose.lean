import DegreeDiameter.N63Lift
import Mathlib.Tactic.ComputeDegree
import Mathlib.FieldTheory.IntermediateField.Adjoin.Basic

namespace DegreeDiameter
open Polynomial
noncomputable section

/-- The quadratic relation linking the actual adjacency and defect operators. -/
def n63Quadratic : ℚ[X] := X ^ 2 + X - 7

/-- A nonsquare discriminant excludes a factorization of the needed quadratic. -/
theorem n63_quadratic_irreducible {K : Type*} [Field K] (r : K)
    (h : ¬ IsSquare ((29 : K) + 4 * r)) :
    Irreducible ((X : K[X]) ^ 2 + X - C (7 + r)) := by
  let p : K[X] := X ^ 2 + X - C (7 + r)
  have hm : p.Monic := by dsimp [p]; monicity!
  have hd : p.natDegree = 2 := by dsimp [p]; compute_degree!
  by_contra hi
  obtain ⟨a, b, hab, hs⟩ := hm.not_irreducible_iff_exists_add_mul_eq_coeff hd |>.mp hi
  have hab' : -(7 + r) = a * b := by simpa [p] using hab
  have hs' : (1 : K) = a + b := by simpa [p] using hs
  apply h
  refine ⟨a - b, ?_⟩
  calc
    (29 : K) + 4 * r = (a + b) ^ 2 - 4 * (a * b) := by rw [← hs', ← hab']; ring
    _ = (a - b) * (a - b) := by ring

/-- The proved rational norm test, applied to actual simple-extension data,
forces irreducibility after composing with X²+X−7. -/
theorem n63_composition_irreducible {p : ℚ[X]} (hm : p.Monic)
    (hi : Irreducible p)
    (hn : ¬ IsSquare ((-4 : ℚ) ^ p.natDegree * p.eval (-29 / 4))) :
    Irreducible (p.comp n63Quadratic) := by
  apply Polynomial.irreducible_comp hm (show n63Quadratic.Monic by
    unfold n63Quadratic; monicity!) hi
  intro E _ _ x hx
  have hxint : IsIntegral ℚ x := minpoly.ne_zero_iff.mp (hx ▸ hm.ne_zero)
  letI : Algebra ℚ ↥(IntermediateField.adjoin ℚ ({x} : Set E)) := (IntermediateField.adjoin ℚ {x}).algebra'
  let pb := IntermediateField.adjoin.powerBasis hxint
  have hnorm : ¬ IsSquare ((-4 : ℚ) ^ pb.dim * (minpoly ℚ pb.gen).eval (-29 / 4)) := by
    simpa [pb, IntermediateField.adjoin.powerBasis_dim,
      IntermediateField.adjoin.powerBasis_gen, IntermediateField.minpoly_gen, hx] using hn
  have hdisc := not_isSquare_discriminant_of_norm pb hnorm
  have hquad := n63_quadratic_irreducible pb.gen hdisc
  convert hquad using 1 <;> norm_num [n63Quadratic, pb,
    IntermediateField.adjoin.powerBasis_gen, C_add, map_ofNat] <;> ring

end
end DegreeDiameter

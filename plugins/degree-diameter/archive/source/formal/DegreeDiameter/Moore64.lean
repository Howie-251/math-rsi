import DegreeDiameter.Moore64Structure

namespace DegreeDiameter

open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
set_option maxRecDepth 10000
noncomputable section

variable {V : Type*} [Fintype V]

/-- The original order-64 graph is excluded by a finite-field trace identity. -/
theorem no_original_graph_card_64 (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hn : Fintype.card V = 64) : False := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hBB := defect_square_identity_of_card_64 G hreg hdiam hn
  have ht := triangle_free_of_card_64 G hreg hdiam hn
  have hAB0 := adjacency_defect_trace_zero_of_triangle_free G ht
  have hBA := (adjacency_defect_commute G hreg).symm
  have hBJ : defectMatrix G * onesMatrix = onesMatrix := by
    simpa [hn] using defect_mul_ones G hreg
  have hBT : (defectMatrix G)ᵀ = defectMatrix G := defect_symmetric G
  have hJT : (onesMatrix : Matrix V V ℤ)ᵀ = onesMatrix := rfl
  have hJB : (onesMatrix : Matrix V V ℤ) * defectMatrix G = onesMatrix := by
    have hh := congrArg Matrix.transpose hBJ
    simpa only [Matrix.transpose_mul, hJT, hBT] using hh
  have hAJ := adjacency_mul_ones G hreg
  have hrel : adjacencyMatrix G * adjacencyMatrix G + adjacencyMatrix G =
      (7 : ℤ) • (1 : Matrix V V ℤ) + onesMatrix + defectMatrix G := by
    unfold defectMatrix
    abel
  have hBAB : defectMatrix G * (adjacencyMatrix G * defectMatrix G) = adjacencyMatrix G := by
    rw [← Matrix.mul_assoc, hBA, Matrix.mul_assoc, hBB, mul_one]
  let D₀ : Matrix V V ℤ := adjacencyMatrix G * (1 + defectMatrix G) + 1
  let E₀ : Matrix V V ℤ := (6 : ℤ) • (1 - defectMatrix G)
  have hsq : D₀ ^ 2 = (17 : ℤ) • (1 : Matrix V V ℤ) +
      (16 : ℤ) • defectMatrix G + (4 : ℤ) • onesMatrix := by
    calc
      D₀ ^ 2 = (2 : ℤ) • ((adjacencyMatrix G * adjacencyMatrix G + adjacencyMatrix G) *
          (1 + defectMatrix G)) + 1 := by
        dsimp [D₀]
        noncomm_ring [hBA, hBB, hBAB]
      _ = _ := by rw [hrel]; noncomm_ring [hBB, hJB]
  have hsq' : D₀ ^ 2 = E₀ + (4 : ℤ) • onesMatrix +
      (11 : ℤ) • ((1 : Matrix V V ℤ) + (2 : ℤ) • defectMatrix G) := by
    rw [hsq]
    dsimp [E₀]
    abel
  have hminus : (1 + defectMatrix G) * (1 - defectMatrix G) = 0 := by
    noncomm_ring [hBB]
  have hDE₀ : D₀ * E₀ = E₀ := by
    dsimp [D₀, E₀]
    rw [Matrix.mul_smul, add_mul, Matrix.mul_assoc, hminus, mul_zero, one_mul, zero_add]
  have hDJ₀ : D₀ * onesMatrix = (17 : ℤ) • onesMatrix := by
    dsimp [D₀]
    rw [add_mul, Matrix.mul_assoc, add_mul, one_mul, hBJ, mul_add, hAJ]
    abel
  have htB : trace (defectMatrix G) = 0 := by
    simp [trace, diag_apply, defect_diagonal G hreg]
  have htE₀ : trace E₀ = (384 : ℤ) := by
    dsimp [E₀]
    rw [trace_smul, trace_sub, trace_one, htB, hn]
    norm_num
  have htD₀ : trace D₀ = (64 : ℤ) := by
    dsimp [D₀]
    rw [mul_add, mul_one, trace_add, trace_add, hAB0]
    simp [adjacencyMatrix, hn]
  letI : Fact (Nat.Prime 11) := ⟨by decide⟩
  let f : ℤ →+* ZMod 11 := Int.castRingHom (ZMod 11)
  let D : Matrix V V (ZMod 11) := f.mapMatrix D₀
  let E : Matrix V V (ZMod 11) := f.mapMatrix E₀
  let J : Matrix V V (ZMod 11) := f.mapMatrix onesMatrix
  have h11 (X : Matrix V V (ZMod 11)) : (11 : ℤ) • X = 0 := by
    ext u v
    have hz : (11 : ZMod 11) = 0 := by decide
    simp [Matrix.smul_apply, zsmul_eq_mul, hz]
  have hD2 : D ^ 2 = E + (4 : ℤ) • J := by
    have hh := congrArg f.mapMatrix hsq'
    simpa only [map_pow, map_add, map_zsmul, h11, add_zero] using hh
  have hDE : D * E = E := by
    have hh := congrArg f.mapMatrix hDE₀
    simpa only [map_mul] using hh
  have hDJ : D * J = (17 : ℤ) • J := by
    have hh := congrArg f.mapMatrix hDJ₀
    simpa only [map_mul, map_zsmul] using hh
  have hp (k : ℕ) : D ^ (k + 2) = E + (4 * 17 ^ k : ℤ) • J := by
    induction k with
    | zero => simpa using hD2
    | succ k ih =>
      rw [show k + 1 + 2 = (k + 2) + 1 by omega, pow_succ', ih, mul_add, hDE,
        Matrix.mul_smul, hDJ, smul_smul]
      congr 2
      ring
  have hmap (X : Matrix V V ℤ) : f (trace X) = trace (f.mapMatrix X) :=
    AddMonoidHom.map_trace f X
  have htJ : trace J = (64 : ZMod 11) := by
    change trace (f.mapMatrix (onesMatrix : Matrix V V ℤ)) = _
    rw [← hmap]
    simp [trace, diag_apply, onesMatrix, hn]
  have htE : trace E = (384 : ZMod 11) := by
    change trace (f.mapMatrix E₀) = _
    rw [← hmap, htE₀]
    simp
  have htD : trace D = (64 : ZMod 11) := by
    change trace (f.mapMatrix D₀) = _
    rw [← hmap, htD₀]
    simp
  have hf := ZMod.trace_pow_card (p := 11) D
  rw [hp 9, trace_add, trace_smul, htJ, htE, htD] at hf
  have hfalse : ¬ ((384 : ZMod 11) + ((4 * 17 ^ 9 : ℤ) : ZMod 11) *
      (64 : ZMod 11) = (64 : ZMod 11) ^ 11) := by decide
  exact hfalse (by simpa only [zsmul_eq_mul] using hf)

theorem original_graph_card_le_63 (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G) :
    Fintype.card V ≤ 63 := by
  have hb := original_graph_card_le_64 G hdeg hdiam
  by_contra h
  exact no_original_graph_card_64 G hdeg hdiam (by omega)

theorem exists82_le_63 {n : ℕ} (h : Exists82 n) : n ≤ 63 := by
  obtain ⟨V, inst, G, hn, hdeg, hdiam⟩ := h
  letI := inst
  rw [← hn]
  exact original_graph_card_le_63 G hdeg hdiam

end
end DegreeDiameter

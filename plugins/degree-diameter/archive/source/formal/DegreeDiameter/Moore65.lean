import DegreeDiameter.TraceFive

namespace DegreeDiameter

open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
set_option maxRecDepth 10000
noncomputable section

variable {V : Type*} [Fintype V]

/-- At the Moore order, the actual nonnegative defect has zero row sums. -/
theorem defect_zero_of_card_65 (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hn : Fintype.card V = 65) : defectMatrix G = 0 := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  ext u v
  change defectMatrix G u v = 0
  have hnon := defect_nonnegative G hreg hdiam u v
  have hle : defectMatrix G u v ≤ ∑ w, defectMatrix G u w :=
    Finset.single_le_sum (fun w _ => defect_nonnegative G hreg hdiam u w)
      (Finset.mem_univ v)
  rw [defect_row_sum G hreg, hn] at hle
  omega

/-- Finite-field trace obstruction for a genuine 65-vertex Moore graph. -/
theorem no_original_graph_card_65 (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hn : Fintype.card V = 65) : False := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hzero := defect_zero_of_card_65 G hdeg hdiam hn
  have hrel : adjacencyMatrix G * adjacencyMatrix G + adjacencyMatrix G =
      (7 : ℤ) • (1 : Matrix V V ℤ) + onesMatrix := by
    unfold defectMatrix at hzero
    exact (sub_eq_iff_eq_add.mp (sub_eq_zero.mp hzero)).trans (add_comm _ _)
  let M₀ : Matrix V V ℤ := (2 : ℤ) • adjacencyMatrix G + 1
  have hsq : M₀ ^ 2 = (29 : ℤ) • (1 : Matrix V V ℤ) + (4 : ℤ) • onesMatrix := by
    calc
      M₀ ^ 2 = (4 : ℤ) • (adjacencyMatrix G * adjacencyMatrix G + adjacencyMatrix G) + 1 := by
        dsimp [M₀]
        noncomm_ring
      _ = _ := by rw [hrel]; abel
  have hMJ₀ : M₀ * onesMatrix = (17 : ℤ) • onesMatrix := by
    dsimp [M₀]
    rw [add_mul, Matrix.smul_mul, adjacency_mul_ones G hreg, one_mul, smul_smul]
    noncomm_ring
  letI : Fact (Nat.Prime 29) := ⟨by decide⟩
  let f : ℤ →+* ZMod 29 := Int.castRingHom (ZMod 29)
  let M : Matrix V V (ZMod 29) := f.mapMatrix M₀
  let J : Matrix V V (ZMod 29) := f.mapMatrix onesMatrix
  have h29 : (29 : ℤ) • (1 : Matrix V V (ZMod 29)) = 0 := by
    ext u v
    have hz : (29 : ZMod 29) = 0 := by decide
    simp [Matrix.smul_apply, zsmul_eq_mul, hz]
  have hM2 : M ^ 2 = (4 : ℤ) • J := by
    have hh := congrArg f.mapMatrix hsq
    simpa only [map_pow, map_add, map_zsmul, map_one, h29, zero_add] using hh
  have hMJ : M * J = (17 : ℤ) • J := by
    have hh := congrArg f.mapMatrix hMJ₀
    simpa only [map_mul, map_zsmul] using hh
  have hp (k : ℕ) : M ^ (k + 2) = (4 * 17 ^ k : ℤ) • J := by
    induction k with
    | zero => simpa using hM2
    | succ k ih =>
      rw [show k + 1 + 2 = (k + 2) + 1 by omega, pow_succ', ih,
        Matrix.mul_smul, hMJ, smul_smul]
      congr 1
      ring
  have hmap (X : Matrix V V ℤ) : f (trace X) = trace (f.mapMatrix X) :=
    AddMonoidHom.map_trace f X
  have htJ : trace J = (65 : ZMod 29) := by
    change trace (f.mapMatrix (onesMatrix : Matrix V V ℤ)) = _
    rw [← hmap]
    simp [trace, diag_apply, onesMatrix, hn]
  have htM : trace M = (65 : ZMod 29) := by
    change trace (f.mapMatrix M₀) = _
    rw [← hmap]
    dsimp only [M₀]
    rw [trace_add, trace_smul]
    simp [adjacencyMatrix, hn]
  have hf := ZMod.trace_pow_card (p := 29) M
  rw [hp 27, trace_smul, htJ, htM] at hf
  have hfalse : ¬ (((4 * 17 ^ 27 : ℤ) : ZMod 29) * (65 : ZMod 29) =
      (65 : ZMod 29) ^ 29) := by decide
  exact hfalse (by simpa only [zsmul_eq_mul] using hf)

theorem original_graph_card_le_64 (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G) :
    Fintype.card V ≤ 64 := by
  have hb := moore_bound G hdeg hdiam
  by_contra h
  exact no_original_graph_card_65 G hdeg hdiam (by omega)

theorem exists82_le_64 {n : ℕ} (h : Exists82 n) : n ≤ 64 := by
  obtain ⟨V, inst, G, hn, hdeg, hdiam⟩ := h
  letI := inst
  rw [← hn]
  exact original_graph_card_le_64 G hdeg hdiam

end
end DegreeDiameter

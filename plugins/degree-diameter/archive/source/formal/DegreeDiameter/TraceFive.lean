import DegreeDiameter.Defect
import Mathlib.LinearAlgebra.Matrix.Charpoly.FiniteField
import Mathlib.Tactic.NoncommRing

namespace DegreeDiameter

open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
set_option maxRecDepth 10000

variable {V : Type*} [Fintype V]

/-- Pure matrix congruence: zero integer trace forces the fifth trace to be divisible by five. -/
theorem five_dvd_trace_fifth_of_trace_zero (A : Matrix V V ℤ) (htrace : trace A = 0) :
    (5 : ℤ) ∣ trace (A ^ 5) := by
  letI : Fact (Nat.Prime 5) := ⟨by decide⟩
  let f : ℤ →+* ZMod 5 := Int.castRingHom (ZMod 5)
  have hmap (M : Matrix V V ℤ) : f (trace M) = trace (f.mapMatrix M) :=
    AddMonoidHom.map_trace f M
  have hz : trace (f.mapMatrix A) = 0 := by rw [← hmap, htrace, map_zero]
  have hp := ZMod.trace_pow_card (p := 5) (f.mapMatrix A)
  rw [hz] at hp
  simp only [zero_pow (by decide : (5 : ℕ) ≠ 0)] at hp
  apply (ZMod.intCast_zmod_eq_zero_iff_dvd (trace (A ^ 5)) 5).mp
  change f (trace (A ^ 5)) = 0
  rw [hmap, map_pow]
  exact hp

/-- Applies to the genuine adjacency matrix of every finite simple graph. -/
theorem five_dvd_adjacency_fifth (G : SimpleGraph V) :
    (5 : ℤ) ∣ trace (adjacencyMatrix G ^ 5) := by
  apply five_dvd_trace_fifth_of_trace_zero
  simp [adjacencyMatrix]

/-- A matrix identity for the actual n=59 graph, before taking traces. -/
theorem fifth_matrix_identity_59 (G : SimpleGraph V) (hreg : G.IsRegularOfDegree 8)
    (hn : Fintype.card V = 59) :
    adjacencyMatrix G ^ 5 =
      adjacencyMatrix G * defectMatrix G ^ 2 - (2 : ℤ) • defectMatrix G ^ 2 +
      (17 : ℤ) • adjacencyMatrix G ^ 3 - (12 : ℤ) • adjacencyMatrix G ^ 2 -
      (77 : ℤ) • adjacencyMatrix G + (98 : ℤ) • (1 : Matrix V V ℤ) +
      (426 : ℤ) • (onesMatrix : Matrix V V ℤ) := by
  have hAJ := adjacency_mul_ones G hreg
  have hJA := ones_mul_adjacency G hreg
  have hJJ : (onesMatrix : Matrix V V ℤ) * onesMatrix = (59 : ℤ) • onesMatrix := by
    simpa [hn] using (ones_mul_ones (V := V))
  have hJAA : (onesMatrix : Matrix V V ℤ) * (adjacencyMatrix G * adjacencyMatrix G) =
      (64 : ℤ) • onesMatrix := by
    rw [← Matrix.mul_assoc, hJA, Matrix.smul_mul, hJA, smul_smul]
    norm_num
  unfold defectMatrix
  noncomm_ring [hAJ, hJA, hJJ, hJAA]

/-- The fifth-trace identity uses only the actual graph, its regularity and its order. -/
theorem fifth_trace_identity_59 (G : SimpleGraph V) (hreg : G.IsRegularOfDegree 8)
    (hn : Fintype.card V = 59) :
    trace (adjacencyMatrix G ^ 5) = 25252 +
      trace (adjacencyMatrix G * defectMatrix G ^ 2) - 2 * trace (defectMatrix G ^ 2) +
      17 * trace (adjacencyMatrix G ^ 3) := by
  have hA : trace (adjacencyMatrix G) = 0 := by simp [adjacencyMatrix]
  have hA2 : trace (adjacencyMatrix G ^ 2) = (472 : ℤ) := by
    calc
      trace (adjacencyMatrix G ^ 2) = ∑ _v : V, (8 : ℤ) := by
        apply Finset.sum_congr rfl
        intro v _
        simp only [Matrix.diag_apply, pow_two, adjacencyMatrix]
        rw [SimpleGraph.adjMatrix_mul_self_apply_self, hreg v]
        norm_num
      _ = 472 := by simp [hn]
  have hJ : trace (onesMatrix : Matrix V V ℤ) = 59 := by
    simp [trace, diag_apply, onesMatrix, hn]
  have h := congrArg trace (fifth_matrix_identity_59 G hreg hn)
  simp only [trace_add, trace_sub, trace_smul, trace_one, hA, hA2, hJ, hn,
    smul_eq_mul] at h
  omega

/-- Conditional exclusion only: the three additional trace hypotheses remain explicit. -/
theorem no_n59_with_matching_zero_traces (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hn : Fintype.card V = 59)
    (hthree : trace (adjacencyMatrix G ^ 3) = 0)
    (hs : trace (defectMatrix G ^ 2) = 590)
    (hw : trace (adjacencyMatrix G * defectMatrix G ^ 2) = 590) : False := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have h := fifth_trace_identity_59 G hreg hn
  have hvalue : trace (adjacencyMatrix G ^ 5) = 24662 := by
    rw [hthree, hs, hw] at h
    omega
  have hd := five_dvd_adjacency_fifth G
  rw [hvalue] at hd
  norm_num at hd

end DegreeDiameter

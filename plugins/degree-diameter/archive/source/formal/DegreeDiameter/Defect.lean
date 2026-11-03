import DegreeDiameter.Moore
import Mathlib.Combinatorics.SimpleGraph.AdjMatrix

namespace DegreeDiameter

open scoped BigOperators
open Matrix
attribute [local instance] Classical.propDecidable
noncomputable section

variable {V : Type*} [Fintype V]

/-- The integer adjacency matrix of the original graph. -/
def adjacencyMatrix (G : SimpleGraph V) : Matrix V V ℤ := G.adjMatrix ℤ

/-- The all-ones matrix; this is not the identity matrix. -/
def onesMatrix : Matrix V V ℤ := fun _ _ => 1

/-- The actual defect matrix, with subtraction in the integers. -/
def defectMatrix (G : SimpleGraph V) : Matrix V V ℤ :=
  adjacencyMatrix G * adjacencyMatrix G + adjacencyMatrix G -
    (7 : ℤ) • (1 : Matrix V V ℤ) - onesMatrix

/-- A direct enumeration of genuine common neighbors. -/
def commonNeighborCount (G : SimpleGraph V) (u v : V) : ℕ :=
  ((G.neighborFinset u).filter (fun w => G.Adj w v)).card

theorem adjacency_sq_common_count (G : SimpleGraph V) (u v : V) :
    (adjacencyMatrix G * adjacencyMatrix G) u v = (commonNeighborCount G u v : ℤ) := by
  simp [adjacencyMatrix, commonNeighborCount]
  apply congrArg Finset.card
  ext w
  simp [SimpleGraph.adj_comm, and_comm]

theorem defect_diagonal (G : SimpleGraph V) (hreg : G.IsRegularOfDegree 8) (v : V) :
    defectMatrix G v v = 0 := by
  simp only [defectMatrix, adjacencyMatrix, Matrix.sub_apply, Matrix.add_apply,
    Matrix.smul_apply, SimpleGraph.adjMatrix_mul_self_apply_self, hreg v,
    SimpleGraph.adjMatrix_apply, SimpleGraph.irrefl, ite_false,
    Matrix.one_apply_eq, onesMatrix, smul_eq_mul]
  decide

theorem defect_symmetric (G : SimpleGraph V) : (defectMatrix G).IsSymm := by
  have hJ : (onesMatrix : Matrix V V ℤ)ᵀ = onesMatrix := rfl
  unfold Matrix.IsSymm
  simp only [defectMatrix, adjacencyMatrix, Matrix.transpose_mul,
    Matrix.transpose_add, Matrix.transpose_sub, Matrix.transpose_smul,
    SimpleGraph.transpose_adjMatrix, Matrix.transpose_one, hJ]

theorem defect_off_diagonal (G : SimpleGraph V) {u v : V} (huv : u ≠ v) :
    defectMatrix G u v = (commonNeighborCount G u v : ℤ) + adjacencyMatrix G u v - 1 := by
  simp only [defectMatrix, Matrix.sub_apply, Matrix.add_apply, Matrix.smul_apply,
    Matrix.one_apply, if_neg huv, adjacency_sq_common_count, onesMatrix, smul_eq_mul,
    mul_zero, sub_zero]

theorem defect_nonnegative (G : SimpleGraph V) (hreg : G.IsRegularOfDegree 8)
    (hdiam : diameterAtMostTwo G) (u v : V) : 0 ≤ defectMatrix G u v := by
  by_cases huv : u = v
  · subst v
    rw [defect_diagonal G hreg]
  · rw [defect_off_diagonal G huv]
    by_cases ha : G.Adj u v
    · simp [adjacencyMatrix, ha]
    · obtain ⟨w, huw, hwv⟩ := (hdiam u v huv).resolve_left ha
      have hc : 0 < commonNeighborCount G u v := by
        apply Finset.card_pos.mpr
        exact ⟨w, by simp [huw, hwv]⟩
      simp only [adjacencyMatrix, SimpleGraph.adjMatrix_apply, if_neg ha]
      omega

theorem adjacency_mul_ones (G : SimpleGraph V) (hreg : G.IsRegularOfDegree 8) :
    adjacencyMatrix G * (onesMatrix : Matrix V V ℤ) = (8 : ℤ) • onesMatrix := by
  ext u v
  simp [adjacencyMatrix, onesMatrix, SimpleGraph.adjMatrix_mul_apply, hreg u]

theorem ones_mul_adjacency (G : SimpleGraph V) (hreg : G.IsRegularOfDegree 8) :
    (onesMatrix : Matrix V V ℤ) * adjacencyMatrix G = (8 : ℤ) • onesMatrix := by
  ext u v
  simp [adjacencyMatrix, onesMatrix, SimpleGraph.mul_adjMatrix_apply, hreg v]

theorem ones_mul_ones : (onesMatrix : Matrix V V ℤ) * onesMatrix =
    (Fintype.card V : ℤ) • onesMatrix := by
  ext u v
  simp [onesMatrix, Matrix.mul_apply]

theorem adjacency_defect_commute (G : SimpleGraph V) (hreg : G.IsRegularOfDegree 8) :
    adjacencyMatrix G * defectMatrix G = defectMatrix G * adjacencyMatrix G := by
  unfold defectMatrix
  rw [mul_sub, mul_sub, mul_add, sub_mul, sub_mul, add_mul]
  simp only [Matrix.mul_assoc, Matrix.mul_smul, Matrix.smul_mul, Matrix.mul_one,
    Matrix.one_mul, adjacency_mul_ones G hreg, ones_mul_adjacency G hreg]

theorem defect_mul_ones (G : SimpleGraph V) (hreg : G.IsRegularOfDegree 8) :
    defectMatrix G * onesMatrix = (65 - (Fintype.card V : ℤ)) • onesMatrix := by
  unfold defectMatrix
  rw [sub_mul, sub_mul, add_mul, Matrix.mul_assoc, adjacency_mul_ones G hreg,
    Matrix.mul_smul, adjacency_mul_ones G hreg, Matrix.smul_mul, Matrix.one_mul,
    ones_mul_ones]
  ext u v
  simp only [Matrix.sub_apply, Matrix.add_apply, Matrix.smul_apply, onesMatrix,
    smul_eq_mul]
  omega

theorem defect_row_sum (G : SimpleGraph V) (hreg : G.IsRegularOfDegree 8) (u : V) :
    ∑ v, defectMatrix G u v = 65 - (Fintype.card V : ℤ) := by
  have h := congrArg (fun M : Matrix V V ℤ => M u u) (defect_mul_ones G hreg)
  simpa [Matrix.mul_apply, onesMatrix] using h

/-- All defect properties arise from one arbitrary original graph above order 57. -/
theorem original_graph_defect_properties (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : 57 < Fintype.card V) :
    (∀ v, defectMatrix G v v = 0) ∧ (defectMatrix G).IsSymm ∧
    (∀ u v, 0 ≤ defectMatrix G u v) ∧
    (∀ u, ∑ v, defectMatrix G u v = 65 - (Fintype.card V : ℤ)) ∧
    adjacencyMatrix G * defectMatrix G = defectMatrix G * adjacencyMatrix G := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam hcard
  exact ⟨defect_diagonal G hreg, defect_symmetric G,
    defect_nonnegative G hreg hdiam, defect_row_sum G hreg,
    adjacency_defect_commute G hreg⟩

end
end DegreeDiameter

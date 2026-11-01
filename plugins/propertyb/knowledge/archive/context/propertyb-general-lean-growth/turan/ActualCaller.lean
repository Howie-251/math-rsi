import Aris4Math.General.Structure.Turan

open Aris4Math.General.RS

/-- Three distinct real edges; each two intersect in exactly one point. -/
def triangleEdges : Finset (Finset ℕ) := {{0, 1}, {1, 2}, {0, 2}}

theorem triangleEdges_card : triangleEdges.card = 3 := by decide

/-- Actual use of the generic theorem, with its finite-clique premise discharged
from the original finite edge family rather than supplied as a certificate. -/
theorem actualTriangleCaller :
    (gamma triangleEdges : ℝ) ≤ (1 - 1 / (3 : ℝ)) * (triangleEdges.card : ℝ) ^ 2 := by
  apply singleGraph_gamma_bound triangleEdges (r := 3) (by omega)
  apply singleGraph_cliqueFree_of_card_le
  intro s _
  calc
    s.card ≤ Fintype.card ↥triangleEdges := Finset.card_le_univ s
    _ = 3 := by simpa using triangleEdges_card

def finiteTriangleEdges : Finset (Finset (Fin 3)) := {{0, 1}, {1, 2}, {0, 2}}

theorem finiteTriangleEdges_uniform : Uniform finiteTriangleEdges 2 := by
  intro e he
  simp only [finiteTriangleEdges, Finset.mem_insert, Finset.mem_singleton] at he
  rcases he with rfl | rfl | rfl <;> decide

/-- Nonempty actual caller of the completely assembled uniform-family bound. -/
theorem actualUniformTriangleCaller :
    (gamma finiteTriangleEdges : ℝ) ≤
      (1 - 1 / (cliqueBudget 2 3 : ℝ)) * (finiteTriangleEdges.card : ℝ) ^ 2 := by
  exact gamma_le_cliqueBudget finiteTriangleEdges finiteTriangleEdges_uniform (by omega)

#print axioms actualUniformTriangleCaller
#print axioms singlePairsDartEquiv
#print axioms gamma_eq_twice_singleGraph_edges
#print axioms singleGraph_cliqueFree_of_card_le
#print axioms gamma_le_cliqueBudget
#print axioms singleGraph_gamma_bound
#print axioms actualTriangleCaller
#check @singleGraph_gamma_bound

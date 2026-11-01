import Aris4Math.General.Structure.Main

namespace GeneralStructureAudit
open Aris4Math.General.RS
universe u

theorem original_structural_criterion (V : Type u) [Finite V]
    (E : Finset (Finset V)) (k N : ℕ) (large : 2 ≤ k)
    (uniform : ∀ e ∈ E, e.card = k) (edges : E.card ≤ N)
    (p : ℝ) (positive : 0 < p) (atMostOne : p ≤ 1)
    (numeric : ∀ n : ℕ, k ≤ n → n * (n - 1) ≤ k * (k - 1) * N →
      ((1 - 1 / (max (k * k - k + 1) ((n - 1) / (k - 1)) : ℕ)) *
        (N : ℝ) ^ 2) / ((2 : ℝ) ^ (k - 1)) ^ 2 *
        (∫ y in (0 : ℝ)..p, (1 - y ^ 2) ^ (k - 1)) <
        (1 - (1 - p) ^ k) ^ ((N : ℝ) / (2 : ℝ) ^ (k - 1))) :
    ∃ coloring : V → Bool, ∀ e ∈ E,
      (∃ red ∈ e, coloring red = true) ∧
      (∃ blue ∈ e, coloring blue = false) := by
  exact propertyB_of_structural_rs_bound E k N large uniform edges positive atMostOne numeric

end GeneralStructureAudit

#print Aris4Math.General.RS.PairCovering
#print Aris4Math.General.RS.singleGraph
#print Aris4Math.General.RS.cliqueBudget
#print axioms Aris4Math.General.RS.exists_pair_covering_counterexample
#print axioms Aris4Math.General.RS.pairCovering_count
#print axioms Aris4Math.General.RS.gamma_eq_twice_singleGraph_edges
#print axioms Aris4Math.General.RS.gamma_le_cliqueBudget
#print axioms Aris4Math.General.RS.propertyB_of_structural_rs_bound
#print axioms GeneralStructureAudit.original_structural_criterion

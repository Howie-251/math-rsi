import Aris4Math.General.Structure.Reduction

open Aris4Math.General.RS

example {V : Type*} [Finite V] (E : Finset (Finset V)) (k N : ℕ)
    (hU : Uniform E k) (hM : E.card ≤ N) (hB : ¬ PropertyB E) :
    ∃ n : ℕ, ∃ K : Finset (Finset (Fin n)),
      Uniform K k ∧ K.card ≤ N ∧ ¬ PropertyB K ∧ PairCovering K ∧
      0 < K.card ∧ k ≤ n ∧ n * (n - 1) ≤ k * (k - 1) * N := by
  obtain ⟨n, K, hKU, hKM, hKB, hP⟩ := exists_pair_covering_counterexample E hU hM hB
  obtain ⟨hpos, hkn, hcount⟩ := pairCovering_vertex_bound K hKU hKM hKB hP
  exact ⟨n, K, hKU, hKM, hKB, hP, hpos, hkn, hcount⟩

#print Aris4Math.General.RS.exists_pair_covering_counterexample
#print axioms Aris4Math.General.RS.uniform_le_vertices_of_not_propertyB
#print axioms Aris4Math.General.RS.not_propertyB_card_pos

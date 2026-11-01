import Aris4Math.ThirtyThree.TwentyThreeClusterSelection

open Aris4Math Aris4Math.ThirtyThree
open TwentyThreeClusterSelection

/-- A direct caller uses an actual hypergraph on Fin 23. Only the graph
exclusions supplied by the earlier probability branches are assumed. -/
theorem actual_cluster_caller (H : Simple5Hypergraph (Fin 23))
    (cover : H.PairCovering) (edges : H.edges.card = 33) (count : H.sixVertices.card = 0)
    (upper : ∀ x, H.degree x = 7 → ∀ y, H.degree y = 7 → x ≠ y → H.codegree x y ≤ 2)
    (noPath : ∀ x, H.degree x = 7 → ∀ y, H.degree y = 7 → ∀ z, H.degree z = 7 →
      x ≠ y → x ≠ z → y ≠ z → H.codegree x y = 2 → H.codegree x z = 2 →
      H.codegree y z ≠ 1) :
    (∃ f : Fin 5 → Fin 23, Function.Injective f ∧ (∀ i, H.degree (f i) = 7) ∧
      H.codegree (f 0) (f 1) ≤ 2 ∧
      ∀ i j, i < j → ¬ (i = 0 ∧ j = 1) → H.codegree (f i) (f j) = 1) ∨
    (∃ f : Fin 6 → Fin 23, Function.Injective f ∧ (∀ i, H.degree (f i) = 7) ∧
      (∀ i j, i < j → H.codegree (f i) (f j) = if i.val / 2 = j.val / 2 then 2 else 1) ∧
      ∃ e ∈ H.edges, 4 ≤ (Finset.univ.filter fun i => f i ∈ e).card) := by
  rcases cluster_selection_of_no_sixes H cover (by decide) edges count upper noPath with h | h
  · exact Or.inl h
  · obtain ⟨f,inj,degrees,pairs,e,he,large⟩ := h
    exact Or.inr ⟨f,inj,degrees,pairs,e,he,by rw [indexed_trace_card f inj]; exact large⟩

#check cluster_selection_of_no_sixes
#print FiveCase
#print SixCase
#print axioms TwentyThreeClusterMoments.sum_inter_product
#print axioms TwentyThreeClusterMoments.clique_square_moment
#print axioms TwentyThreeClusterMoments.exists_large_clipped_trace
#print axioms clusters_disjoint
#print axioms six_of_three_cliques
#print axioms cluster_selection_of_no_sixes
#print axioms actual_cluster_caller

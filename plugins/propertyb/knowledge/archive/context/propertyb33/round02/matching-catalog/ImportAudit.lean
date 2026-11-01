import Aris4Math.ThirtyThree.TwentyFourMatchingHighCatalog
open Aris4Math.ThirtyThree
open TwentyFourMatchingHighCatalog
open scoped BigOperators
example (h : Fin 16 → Bool)
    (budgets : ∀ i j : Fin 5, i ≠ j →
      (∑ a : Fin 16, if i ∈ largeTypes a ∧ j ∈ largeTypes a then
        if h a then 1 else 0 else 0) ≤ TwentyFourFiveMatching.pairDegree i j) :
    ∃ k : Fin 18, ∃ σ : Fin 5 ≃ Fin 5,
      (∀ i j, TwentyFourFiveMatching.pairDegree (σ i) (σ j) =
        TwentyFourFiveMatching.pairDegree i j) ∧
      (∀ T : Finset (Fin 5), 3 ≤ T.card →
        highValue h (T.image σ) = TwentyFourFiveMatchingData.counts k T) := by
  exact classify h budgets
#print axioms TwentyFourMatchingHighCatalog.covers
#print axioms TwentyFourMatchingHighCatalog.representatives
#print axioms TwentyFourMatchingHighCatalog.classify

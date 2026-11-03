import DegreeDiameter.N62TripleFourBlock

#print DegreeDiameter.tripleFourPattern
#check @DegreeDiameter.n62_four_block_opposite_entries
#check @DegreeDiameter.n62_four_block_weight_cases
#check @DegreeDiameter.n62_four_block_classification
#print axioms DegreeDiameter.n62_four_block_opposite_entries
#print axioms DegreeDiameter.n62_four_block_weight_cases
#print axioms DegreeDiameter.n62_four_block_classification

open DegreeDiameter
open scoped BigOperators

/-- A caller with exactly the requested matrix hypotheses. -/
example (N : Matrix (Fin 4) (Fin 4) ℤ)
    (hsym : ∀ i j, N i j = N j i)
    (hdiag : ∀ i, N i i = 0)
    (hnonneg : ∀ i j, 0 ≤ N i j)
    (hrow : ∀ i, ∑ j : Fin 4, N i j = 3) :
    ∃ σ : Equiv.Perm (Fin 4), σ 0 = 0 ∧
      (tripleFourPattern (fun i j => N (σ i) (σ j)) 3 0 0 ∨
       tripleFourPattern (fun i j => N (σ i) (σ j)) 2 1 0 ∨
       tripleFourPattern (fun i j => N (σ i) (σ j)) 1 1 1) :=
  n62_four_block_classification N hsym hdiag hnonneg hrow

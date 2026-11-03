import DegreeDiameter.N62TripleActualBlock

#print DegreeDiameter.triplePositiveLabel
#print DegreeDiameter.tripleNegativeLabel
#print DegreeDiameter.tripleActualCrossBlock
#check @DegreeDiameter.n62_triple_exclusive_zero_triangle
#check @DegreeDiameter.n62_triple_matching_repeat_neighbor_sum
#check @DegreeDiameter.n62_triple_matching_repeat_symmetric
#check @DegreeDiameter.n62_triple_labels_adj_iff
#check @DegreeDiameter.n62_triple_actual_block_symmetric
#check @DegreeDiameter.n62_triple_actual_block_diagonal
#check @DegreeDiameter.n62_triple_actual_block_nonnegative
#check @DegreeDiameter.n62_triple_actual_block_row_sum
#check @DegreeDiameter.n62_triple_actual_block_classification
#print axioms DegreeDiameter.triplePositiveLabel
#print axioms DegreeDiameter.tripleNegativeLabel
#print axioms DegreeDiameter.tripleActualCrossBlock
#print axioms DegreeDiameter.n62_triple_exclusive_zero_triangle
#print axioms DegreeDiameter.n62_triple_matching_repeat_neighbor_sum
#print axioms DegreeDiameter.n62_triple_matching_repeat_symmetric
#print axioms DegreeDiameter.n62_triple_labels_adj_iff
#print axioms DegreeDiameter.n62_triple_actual_block_symmetric
#print axioms DegreeDiameter.n62_triple_actual_block_diagonal
#print axioms DegreeDiameter.n62_triple_actual_block_nonnegative
#print axioms DegreeDiameter.n62_triple_actual_block_row_sum
#print axioms DegreeDiameter.n62_triple_actual_block_classification

open DegreeDiameter
open scoped BigOperators
attribute [local instance] Classical.propDecidable

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    ∃ σ : Equiv.Perm (Fin 4), σ 0 = 0 ∧
      (tripleFourPattern (fun i j => tripleActualCrossBlock G hdeg hdiam hcard hb (σ i) (σ j)) 3 0 0 ∨
       tripleFourPattern (fun i j => tripleActualCrossBlock G hdeg hdiam hcard hb (σ i) (σ j)) 2 1 0 ∨
       tripleFourPattern (fun i j => tripleActualCrossBlock G hdeg hdiam hcard hb (σ i) (σ j)) 1 1 1) :=
  n62_triple_actual_block_classification G hdeg hdiam hcard hb

example {V : Type*} [Fintype V] (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    (∀ i, tripleActualCrossBlock G hdeg hdiam hcard hb i i = 0) ∧
      (∀ i, ∑ j : Fin 4, tripleActualCrossBlock G hdeg hdiam hcard hb i j = 3) :=
  ⟨n62_triple_actual_block_diagonal G hdeg hdiam hcard hb,
    n62_triple_actual_block_row_sum G hdeg hdiam hcard hb⟩

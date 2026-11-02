import DegreeDiameter.N62TripleCells
import DegreeDiameter.N62TripleFourBlock
import Mathlib.Data.Fintype.EquivFin

namespace DegreeDiameter
open Matrix
open scoped BigOperators
attribute [local instance] Classical.propDecidable
noncomputable section
variable {V : Type*} [Fintype V]

/-- An exclusive vertex is triangle-free: every incident triangle repeat would
lie across the exclusive sides, where its original neighbor is unique. -/
theorem n62_triple_exclusive_zero_triangle (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v x : V} (hb : defectMatrix G u v = 3)
    (hx : x ∈ tripleExclusiveNeighbors G u v) : zeroTriangleVertex G x := by
  intro y z hxy hxz hyz
  have hypos := defect_incident_triangle_ge_one G hxy hxz hyz.symm
  have hzpos := defect_incident_triangle_ge_one G hxz hxy hyz
  have hy := n62_triple_exclusive_repeat_crosses G hdeg hdiam hcard hb hx (by omega : 0 < defectMatrix G x y)
  have hz := n62_triple_exclusive_repeat_crosses G hdeg hdiam hcard hb hx (by omega : 0 < defectMatrix G x z)
  have he := (n62_triple_exclusive_unique_neighbor G hdeg hdiam hcard hb hx).unique
    ⟨hy,hxy⟩ ⟨hz,hxz⟩
  exact hyz.ne he

/-- The actual repeat row against the original neighbors of another same-side
vertex collapses to that vertex's unique matching neighbor. -/
theorem n62_triple_matching_repeat_neighbor_sum (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3)
    (x z : {x // x ∈ tripleExclusiveNeighbors G u v}) :
    ∑ y ∈ G.neighborFinset z, defectMatrix G x y =
      defectMatrix G x (tripleMatchingEquiv G hdeg hdiam hcard hb z) := by
  let m := tripleMatchingEquiv G hdeg hdiam hcard hb z
  have hzm : G.Adj (z : V) (m : V) :=
    (tripleMatchingEquiv_adj_iff G hdeg hdiam hcard hb z m).mpr rfl
  change (∑ y ∈ G.neighborFinset z, defectMatrix G x y) = defectMatrix G x (m : V)
  apply Finset.sum_eq_single (m : V)
  · intro y hy hne
    by_cases hyp : y ∈ tripleExclusiveNeighbors G v u
    · have hzy : G.Adj (z : V) y := by simpa using hy
      have he := (n62_triple_exclusive_unique_neighbor G hdeg hdiam hcard hb z.property).unique
        ⟨hyp,hzy⟩ ⟨m.property,hzm⟩
      exact (hne he).elim
    · exact n62_triple_exclusive_repeat_zero_outside G hdeg hdiam hcard hb x.property hyp
  · intro hm
    exact (hm (by simpa using hzm)).elim

/-- Actual commutation and the actual matching force symmetry of the cross block. -/
theorem n62_triple_matching_repeat_symmetric (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3)
    (x z : {x // x ∈ tripleExclusiveNeighbors G u v}) :
    defectMatrix G x (tripleMatchingEquiv G hdeg hdiam hcard hb z) =
      defectMatrix G z (tripleMatchingEquiv G hdeg hdiam hcard hb x) := by
  have hreg := regular_of_card_gt_57 G hdeg hdiam (by omega)
  have hh := congrArg (fun M => M (x : V) (z : V)) (adjacency_defect_commute G hreg)
  change (G.adjMatrix ℤ * defectMatrix G) (x : V) (z : V) =
    (defectMatrix G * G.adjMatrix ℤ) (x : V) (z : V) at hh
  rw [SimpleGraph.adjMatrix_mul_apply,SimpleGraph.mul_adjMatrix_apply] at hh
  have hs : (∑ y ∈ G.neighborFinset x, defectMatrix G y z) =
      ∑ y ∈ G.neighborFinset x, defectMatrix G z y := by
    apply Finset.sum_congr rfl
    intro y _
    exact (defect_symmetric G).apply z y
  rw [hs,n62_triple_matching_repeat_neighbor_sum G hdeg hdiam hcard hb z x,
    n62_triple_matching_repeat_neighbor_sum G hdeg hdiam hcard hb x z] at hh
  exact hh.symm

/-- A labeling of the actual four-point positive exclusive side, using its proved cardinality. -/
def triplePositiveLabel (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    Fin 4 ≃ {x // x ∈ tripleExclusiveNeighbors G u v} :=
  (Finset.equivFinOfCardEq (n62_triple_exclusive_card G hdeg hdiam hcard hb)).symm

/-- Label the actual opposite side by the actual original matching. -/
def tripleNegativeLabel (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    Fin 4 ≃ {y // y ∈ tripleExclusiveNeighbors G v u} :=
  (triplePositiveLabel G hdeg hdiam hcard hb).trans
    (tripleMatchingEquiv G hdeg hdiam hcard hb)

/-- Equal labels encode exactly the actual original matching edges. -/
theorem n62_triple_labels_adj_iff (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3)
    (i j : Fin 4) :
    G.Adj (triplePositiveLabel G hdeg hdiam hcard hb i)
      (tripleNegativeLabel G hdeg hdiam hcard hb j) ↔ i = j := by
  change G.Adj (triplePositiveLabel G hdeg hdiam hcard hb i)
    (tripleMatchingEquiv G hdeg hdiam hcard hb
      (triplePositiveLabel G hdeg hdiam hcard hb j)) ↔ i = j
  rw [tripleMatchingEquiv_adj_iff]
  constructor
  · intro he
    exact (triplePositiveLabel G hdeg hdiam hcard hb).injective
      ((tripleMatchingEquiv G hdeg hdiam hcard hb).injective he)
  · rintro rfl
    rfl

/-- The actual cross-repeat matrix on the two labeled exclusive sides. -/
def tripleActualCrossBlock (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    Matrix (Fin 4) (Fin 4) ℤ :=
  fun i j => defectMatrix G (triplePositiveLabel G hdeg hdiam hcard hb i)
    (tripleNegativeLabel G hdeg hdiam hcard hb j)

/-- No cross-block symmetry premise is supplied: it follows from actual commutation. -/
theorem n62_triple_actual_block_symmetric (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    ∀ i j, tripleActualCrossBlock G hdeg hdiam hcard hb i j =
      tripleActualCrossBlock G hdeg hdiam hcard hb j i := by
  intro i j
  exact n62_triple_matching_repeat_symmetric G hdeg hdiam hcard hb
    (triplePositiveLabel G hdeg hdiam hcard hb i)
    (triplePositiveLabel G hdeg hdiam hcard hb j)

/-- Matching original edges incident with the exclusive triangle-free vertices have zero repeat. -/
theorem n62_triple_actual_block_diagonal (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    ∀ i, tripleActualCrossBlock G hdeg hdiam hcard hb i i = 0 := by
  intro i
  let x := triplePositiveLabel G hdeg hdiam hcard hb i
  exact zero_vertex_edge_defect_zero G
    (n62_triple_exclusive_zero_triangle G hdeg hdiam hcard hb x.property)
    ((tripleMatchingEquiv_adj_iff G hdeg hdiam hcard hb x
      (tripleMatchingEquiv G hdeg hdiam hcard hb x)).mpr rfl)

/-- Actual nonnegativity supplies every cross-block entry bound. -/
theorem n62_triple_actual_block_nonnegative (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    ∀ i j, 0 ≤ tripleActualCrossBlock G hdeg hdiam hcard hb i j := by
  intro i j
  exact defect_nonnegative G (regular_of_card_gt_57 G hdeg hdiam (by omega)) hdiam _ _

/-- The actual opposite-side repeat sum transfers through the constructed labeling. -/
theorem n62_triple_actual_block_row_sum (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    ∀ i, ∑ j : Fin 4, tripleActualCrossBlock G hdeg hdiam hcard hb i j = 3 := by
  intro i
  let x := triplePositiveLabel G hdeg hdiam hcard hb i
  change (∑ j : Fin 4, defectMatrix G (x : V)
    (tripleNegativeLabel G hdeg hdiam hcard hb j)) = 3
  rw [(tripleNegativeLabel G hdeg hdiam hcard hb).sum_comp
    (fun y => defectMatrix G (x : V) (y : V))]
  rw [Finset.sum_coe_sort]
  exact n62_triple_exclusive_repeat_sum G hdeg hdiam hcard hb x.property

/-- From the original graph and a triple entry alone, the constructed actual
four-by-four cross-repeat block has one of the three canonical patterns. -/
theorem n62_triple_actual_block_classification (G : SimpleGraph V)
    (hdeg : degreeAtMostEight G) (hdiam : diameterAtMostTwo G)
    (hcard : Fintype.card V = 62) {u v : V} (hb : defectMatrix G u v = 3) :
    ∃ σ : Equiv.Perm (Fin 4), σ 0 = 0 ∧
      (tripleFourPattern (fun i j => tripleActualCrossBlock G hdeg hdiam hcard hb (σ i) (σ j)) 3 0 0 ∨
       tripleFourPattern (fun i j => tripleActualCrossBlock G hdeg hdiam hcard hb (σ i) (σ j)) 2 1 0 ∨
       tripleFourPattern (fun i j => tripleActualCrossBlock G hdeg hdiam hcard hb (σ i) (σ j)) 1 1 1) :=
  n62_four_block_classification _
    (n62_triple_actual_block_symmetric G hdeg hdiam hcard hb)
    (n62_triple_actual_block_diagonal G hdeg hdiam hcard hb)
    (n62_triple_actual_block_nonnegative G hdeg hdiam hcard hb)
    (n62_triple_actual_block_row_sum G hdeg hdiam hcard hb)

end
end DegreeDiameter

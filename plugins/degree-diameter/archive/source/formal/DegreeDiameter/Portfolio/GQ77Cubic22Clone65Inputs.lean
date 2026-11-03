import DegreeDiameter.Portfolio.OppositeGQ77SpreadIncidence
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk00
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk01
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk02
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk03
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk04
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk05
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk06
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk07
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk08
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk09
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk10
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk11
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk12
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk13
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk14
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk15
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk16
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk17
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk18
import DegreeDiameter.Portfolio.GQ77Cubic22Clone65InputChunk19
namespace DegreeDiameter.Portfolio.GQ77Cubic22Clone65
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
theorem owner_of_ovoid : ∀ i, ovoidOwner (ovoid i) = some i := by decide
theorem line_index_certificate : ∀ l k,
    ovoidOwner (OppositeGQ77Spread.linePoint l k) = none ∨
      ovoidOwner (OppositeGQ77Spread.linePoint l k) = some (lineOvoidIndex l) := by
  intro l
  let e := (finProdFinEquiv (m:=20) (n:=20))
  obtain ⟨⟨b,j⟩,rfl⟩ := e.surjective l
  fin_cases b
  · exact line_index_chunk_00 j
  · exact line_index_chunk_01 j
  · exact line_index_chunk_02 j
  · exact line_index_chunk_03 j
  · exact line_index_chunk_04 j
  · exact line_index_chunk_05 j
  · exact line_index_chunk_06 j
  · exact line_index_chunk_07 j
  · exact line_index_chunk_08 j
  · exact line_index_chunk_09 j
  · exact line_index_chunk_10 j
  · exact line_index_chunk_11 j
  · exact line_index_chunk_12 j
  · exact line_index_chunk_13 j
  · exact line_index_chunk_14 j
  · exact line_index_chunk_15 j
  · exact line_index_chunk_16 j
  · exact line_index_chunk_17 j
  · exact line_index_chunk_18 j
  · exact line_index_chunk_19 j

theorem ovoid_index_of_incidence (l : OppositeGQ77Spread.Line) (i : Fin 22)
    (h : OppositeGQ77Spread.Inc (ovoid i) l) : i = lineOvoidIndex l := by
  obtain ⟨k,hk⟩ := h
  have hi : ovoidOwner (OppositeGQ77Spread.linePoint l k) = some i := by
    rw [hk]
    exact owner_of_ovoid i
  rcases line_index_certificate l k with hnone | hsome
  · rw [hnone] at hi
    cases hi
  · exact Option.some.inj (hi.symm.trans hsome)
theorem ovoid_unique : ∀ l i i', OppositeGQ77Spread.Inc (ovoid i) l →
    OppositeGQ77Spread.Inc (ovoid i') l → i = i' := by
  intro l i i' hi hi'
  exact (ovoid_index_of_incidence l i hi).trans (ovoid_index_of_incidence l i' hi').symm
theorem spread_unique : ∀ p j j', OppositeGQ77Spread.Inc p (OppositeGQ77Spread.spread j) →
    OppositeGQ77Spread.Inc p (OppositeGQ77Spread.spread j') → j = j' := by
  intro p j j' hj hj'
  exact (OppositeGQ77Spread.spread_unique p j hj).trans (OppositeGQ77Spread.spread_unique p j' hj').symm
theorem load_le_one (w : Source.Vertex) : FullNeighborhoodClones.load OppositeGQ77Spread.graph center w ≤ 1 := by
  unfold FullNeighborhoodClones.load
  apply Fintype.card_le_one_iff.mpr
  intro x y
  apply Subtype.ext
  apply clonePair.injective
  exact OvoidSpreadCloneCapacity.adjacent_centers_unique OppositeGQ77Spread.oldEquiv
    OppositeGQ77Spread.Inc ovoid OppositeGQ77Spread.spread ovoid_unique spread_unique
    w (clonePair x.val) (clonePair y.val) x.property y.property
#print axioms ovoid_unique
#print axioms load_le_one
end DegreeDiameter.Portfolio.GQ77Cubic22Clone65

import DegreeDiameter.Portfolio.OvoidProduct26Definitions
namespace DegreeDiameter.Portfolio.OvoidProduct26
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000

/--17 literal ovoid values have their stated certificate indices. -/
theorem owner_of_ovoid : ∀ i, ovoidOwner (ovoid i) = some i := by decide

/--425 positive line positions, without enumerating7242×289 source adjacencies. -/
theorem line_index_certificate : ∀ l k,
    ovoidOwner (OppositeGQ44Spread.linePoint l k) = none ∨
      ovoidOwner (OppositeGQ44Spread.linePoint l k) = some (lineOvoidIndex l) := by decide

theorem ovoid_index_of_incidence (l : OppositeGQ44Spread.Line) (i : Fin 17)
    (h : OppositeGQ44Spread.Inc (ovoid i) l) : i = lineOvoidIndex l := by
  obtain ⟨k,hk⟩ := h
  have hi : ovoidOwner (OppositeGQ44Spread.linePoint l k) = some i := by
    rw [hk]
    exact owner_of_ovoid i
  rcases line_index_certificate l k with hnone | hsome
  · rw [hnone] at hi
    cases hi
  · exact Option.some.inj (hi.symm.trans hsome)

theorem ovoid_unique : ∀ l i i', OppositeGQ44Spread.Inc (ovoid i) l →
    OppositeGQ44Spread.Inc (ovoid i') l → i = i' := by
  intro l i i' hi hi'
  exact (ovoid_index_of_incidence l i hi).trans (ovoid_index_of_incidence l i' hi').symm

theorem spread_unique : ∀ p j j', OppositeGQ44Spread.Inc p (OppositeGQ44Spread.spread j) →
    OppositeGQ44Spread.Inc p (OppositeGQ44Spread.spread j') → j = j' := by
  intro p j j' hj hj'
  exact (OppositeGQ44Spread.spread_unique p j hj).trans (OppositeGQ44Spread.spread_unique p j' hj').symm

theorem load_le_one (w : Source.Vertex) : FullNeighborhoodClones.load OppositeGQ44Spread.graph center w ≤ 1 := by
  exact OvoidSpreadCloneCapacity.load_le_one OppositeGQ44Spread.oldEquiv OppositeGQ44Spread.Inc
    ovoid OppositeGQ44Spread.spread ovoid_unique spread_unique w
#print axioms ovoid_unique
#print axioms load_le_one
end DegreeDiameter.Portfolio.OvoidProduct26

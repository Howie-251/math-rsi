import DegreeDiameter.Portfolio.EvenQ8BalancedFullOvoidCopy82Definitions
import DegreeDiameter.Portfolio.EvenQ8SourceFullBalancedHowner
namespace DegreeDiameter.Portfolio.EvenQ8BalancedFullOvoidCopy82
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem owner_of_ovoid : ∀ i,ovoidOwner (ovoid i) = i.val := by decide
theorem line_index_certificate : ∀ l k,
    ovoidOwner (Source.linePoint l k) = 65 ∨
      ovoidOwner (Source.linePoint l k) = (lineOvoidIndex l).val := by decide
theorem ovoid_index_of_incidence (l : Source.Line) (i : Fin 65)
    (h : Source.Inc (ovoid i) l) : i = lineOvoidIndex l := by
  obtain ⟨k,hk⟩ := h
  have hi : ovoidOwner (Source.linePoint l k) = i.val :=
    (congrArg ovoidOwner hk).trans (owner_of_ovoid i)
  rcases line_index_certificate l k with hnone | hsome
  · have := i.isLt
    omega
  · apply Fin.ext
    exact hi.symm.trans hsome
theorem ovoid_unique : ∀ l i i', Source.Inc (ovoid i) l → Source.Inc (ovoid i') l → i = i' := by
  intro l i i' hi hi'
  exact (ovoid_index_of_incidence l i hi).trans (ovoid_index_of_incidence l i' hi').symm
theorem spread_unique : ∀ p j j',Source.Inc p (Source.spread j) →
    Source.Inc p (Source.spread j') → j = j' := by
  intro p j j' hj hj'
  exact (EvenQ8SourceFull.Balanced.howner p j hj).trans
    (EvenQ8SourceFull.Balanced.howner p j' hj').symm
theorem load_le_one (w : Source.Vertex) : FullNeighborhoodClones.load Source.graph center w ≤ 1 := by
  unfold FullNeighborhoodClones.load
  apply Fintype.card_le_one_iff.mpr
  intro x y
  apply Subtype.ext
  apply pair.injective
  exact OvoidSpreadCloneCapacity.adjacent_centers_unique Source.oldEquiv Source.Inc
    ovoid Source.spread ovoid_unique spread_unique
    w (pair x.val) (pair y.val) x.property y.property
#print axioms ovoid_unique
#print axioms load_le_one
end DegreeDiameter.Portfolio.EvenQ8BalancedFullOvoidCopy82

import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputs
import DegreeDiameter.Portfolio.OppositeGQ35SpreadSlots
namespace DegreeDiameter.Portfolio.OppositeGQ35Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
/-- Exactly24 slots, reindexing4 line-points times6 through-point lines. -/
def forward (u : Vertex) (i : Fin 24) : Vertex :=
  OppositeGQSpread.slot oldEquiv spread spreadOwner linePoint pointLine u
    ((finProdFinEquiv (m:=4) (n:=6)).symm i)

theorem forward_covers : ∀ u v, graph.Adj u v → ∃ i, forward u i = v := by
  intro u v h
  obtain ⟨ij,hij⟩ := OppositeGQSpread.slot_covers oldEquiv Inc spread spreadOwner linePoint pointLine
    linePoint_covers pointLine_covers spread_unique u v h
  exact ⟨finProdFinEquiv ij,by simpa only [forward,Equiv.symm_apply_apply] using hij⟩

theorem degree_le_twentyfour : ∀ v, graph.degree v ≤ 24 := by
  simpa only [Fintype.card_fin] using OppositeGQSpread.degree_le_of_cover graph forward forward_covers

#print axioms forward_covers
#print axioms degree_le_twentyfour
end DegreeDiameter.Portfolio.OppositeGQ35Spread

import DegreeDiameter.Portfolio.F4PlaneBlockClonesLoad
namespace DegreeDiameter.Portfolio.F4PlaneBlockClonesFamily
open F4Graph3840 F4PlaneBlockClones
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000

abbrev Carrier (K : Nat) := Fin 3840 ⊕ Fin (K*16)
def graph {K : Nat} (layers : Fin K → Fin 60) : SimpleGraph (Carrier K) :=
  FullNeighborhoodClones.graph F4Graph3840.graph (center layers)
instance {K : Nat} (layers : Fin K → Fin 60) : DecidableRel (graph layers).Adj :=
  inferInstanceAs (DecidableRel (FullNeighborhoodClones.graph F4Graph3840.graph (center layers)).Adj)
def label {K : Nat} : Carrier K ≃ Fin (3840+K*16) := finSumFinEquiv

theorem card (K : Nat) : Fintype.card (Carrier K) = 3840+K*16 := by simp only [Fintype.card_sum,Fintype.card_fin]

theorem label_old {K : Nat} (v : Fin 3840) : (label (.inl v) : Fin (3840+K*16)).val=v.val := rfl

theorem label_new {K : Nat} (j : Fin (K*16)) : (label (.inr j)).val=3840+j.val := rfl

/-- Development interface for any fixed ordered block list; actual callers must
supply their proved60-row capacity, rather than export it as a user premise. -/
theorem recipe_graph_result {K : Nat} (layers : Fin K → Fin 60) (k : Nat)
  (hcap : ∀ a, Fintype.card (Allowed layers a) ≤ k) :
  Fintype.card (Carrier K) = 3840+K*16 ∧ (∀ v, (graph layers).degree v ≤ 20+k) ∧
    DiameterAtMost (graph layers) 3 ∧ ¬DiameterAtMost (graph layers) 2 := by
  refine ⟨card K, ?_, ?_, ?_⟩
  · exact FullNeighborhoodClones.degree_le F4Graph3840.graph (center layers) 20 k degree_le_twenty (load_le_capacity layers k hcap)
  · exact FullNeighborhoodClones.diameterAtMost F4Graph3840.graph (center layers) 3 (by decide) diameterAtMost_three source_no_isolated
  · exact FullNeighborhoodClones.not_diameterAtMost F4Graph3840.graph (center layers) 2 not_diameterAtMost_two
#print axioms recipe_graph_result
end DegreeDiameter.Portfolio.F4PlaneBlockClonesFamily

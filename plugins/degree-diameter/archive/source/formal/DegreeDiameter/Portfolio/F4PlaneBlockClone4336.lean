import DegreeDiameter.Portfolio.F4PlaneBlockLoadSum23
namespace DegreeDiameter.Portfolio.F4PlaneBlockClone4336
open F4PlaneBlockLoadSum23
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000

abbrev Vertex := F4PlaneBlockClonesFamily.Carrier 31
def graph : SimpleGraph Vertex := F4PlaneBlockClonesFamily.graph layers23
instance : DecidableRel graph.Adj :=
  inferInstanceAs (DecidableRel (F4PlaneBlockClonesFamily.graph layers23).Adj)
def label : Vertex ≃ Fin 4336 := F4PlaneBlockClonesFamily.label

theorem label_old (v : Fin 3840) : (label (.inl v)).val=v.val := rfl
theorem label_new (j : Fin (31*16)) : (label (.inr j)).val=3840+j.val := rfl

/-- The single frozen r21+r22 recipe. All actual capacity obligations are supplied
by capacity23; no certificate premise remains for the user. -/
theorem concrete_order_degree_and_exact_D3 :
    Fintype.card Vertex = 4336 ∧ (∀ v, graph.degree v ≤ 23) ∧
      DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2 :=
  F4PlaneBlockClonesFamily.recipe_graph_result layers23 3 capacity23

#print axioms concrete_order_degree_and_exact_D3
end DegreeDiameter.Portfolio.F4PlaneBlockClone4336

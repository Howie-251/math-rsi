import DegreeDiameter.Portfolio.F9U10PlaneCloneFamilyInputs
import DegreeDiameter.Portfolio.F9Graph56862Exact
namespace DegreeDiameter.Portfolio.F9U10PlaneCloneFamily
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem source_no_isolated (v : Fin 56862) : ∃ w, F9Graph56862.graph.Adj v w :=
  ⟨F9Graph56862.forward v 0 F9Graph56862.F.c0,F9Graph56862.forward_adj v 0 F9Graph56862.F.c0⟩
theorem old_walk_bound_iff (k : Nat) (u v : Fin 56862) (n : Nat) :
    (∃ p : (graph k).Walk (.inl u) (.inl v), p.length ≤ n) ↔
      ∃ p : F9Graph56862.graph.Walk u v, p.length ≤ n :=
  FullNeighborhoodClones.old_walk_bound_iff F9Graph56862.graph (center k) u v n
theorem degree_le (k : Nat) : ∀ v, (graph k).degree v ≤ 54+k :=
  FullNeighborhoodClones.degree_le F9Graph56862.graph (center k) 54 k
    F9Graph56862.degree_le_fifty_four (copy_load_le k)
theorem diameterAtMost_three (k : Nat) : DiameterAtMost (graph k) 3 :=
  FullNeighborhoodClones.diameterAtMost F9Graph56862.graph (center k) 3 (by decide)
    F9Graph56862.concrete_order_degree_and_exact_D3.2.2.1 source_no_isolated
theorem not_diameterAtMost_two (k : Nat) : ¬DiameterAtMost (graph k) 2 :=
  FullNeighborhoodClones.not_diameterAtMost F9Graph56862.graph (center k) 2
    F9Graph56862.concrete_order_degree_and_exact_D3.2.2.2
/-- An unconditional fixed-source family theorem; only the five explicit qualified cases below are concrete endpoints. -/
theorem fixed_family_target (k : Nat) : Fintype.card (Vertex k) = 56862+810*k ∧
    (∀ v, (graph k).degree v ≤ 54+k) ∧ DiameterAtMost (graph k) 3 ∧ ¬DiameterAtMost (graph k) 2 :=
  ⟨card_vertex k,degree_le k,diameterAtMost_three k,not_diameterAtMost_two k⟩
theorem fixed_family_claim (k : Nat) : FinalClaim k := fixed_family_target k
theorem concrete_55_57672 : Fintype.card (Vertex 1) = 57672 ∧ (∀ v, (graph 1).degree v ≤ 55) ∧
  DiameterAtMost (graph 1) 3 ∧ ¬DiameterAtMost (graph 1) 2 := fixed_family_target 1
def FinalClaim55 : Prop := Fintype.card (Vertex 1) = 57672 ∧ (∀ v, (graph 1).degree v ≤ 55) ∧
  DiameterAtMost (graph 1) 3 ∧ ¬DiameterAtMost (graph 1) 2
theorem final_claim55 : FinalClaim55 := concrete_55_57672
#print axioms concrete_55_57672
#print axioms final_claim55
theorem concrete_56_58482 : Fintype.card (Vertex 2) = 58482 ∧ (∀ v, (graph 2).degree v ≤ 56) ∧
  DiameterAtMost (graph 2) 3 ∧ ¬DiameterAtMost (graph 2) 2 := fixed_family_target 2
def FinalClaim56 : Prop := Fintype.card (Vertex 2) = 58482 ∧ (∀ v, (graph 2).degree v ≤ 56) ∧
  DiameterAtMost (graph 2) 3 ∧ ¬DiameterAtMost (graph 2) 2
theorem final_claim56 : FinalClaim56 := concrete_56_58482
#print axioms concrete_56_58482
#print axioms final_claim56
theorem concrete_57_59292 : Fintype.card (Vertex 3) = 59292 ∧ (∀ v, (graph 3).degree v ≤ 57) ∧
  DiameterAtMost (graph 3) 3 ∧ ¬DiameterAtMost (graph 3) 2 := fixed_family_target 3
def FinalClaim57 : Prop := Fintype.card (Vertex 3) = 59292 ∧ (∀ v, (graph 3).degree v ≤ 57) ∧
  DiameterAtMost (graph 3) 3 ∧ ¬DiameterAtMost (graph 3) 2
theorem final_claim57 : FinalClaim57 := concrete_57_59292
#print axioms concrete_57_59292
#print axioms final_claim57
theorem concrete_58_60102 : Fintype.card (Vertex 4) = 60102 ∧ (∀ v, (graph 4).degree v ≤ 58) ∧
  DiameterAtMost (graph 4) 3 ∧ ¬DiameterAtMost (graph 4) 2 := fixed_family_target 4
def FinalClaim58 : Prop := Fintype.card (Vertex 4) = 60102 ∧ (∀ v, (graph 4).degree v ≤ 58) ∧
  DiameterAtMost (graph 4) 3 ∧ ¬DiameterAtMost (graph 4) 2
theorem final_claim58 : FinalClaim58 := concrete_58_60102
#print axioms concrete_58_60102
#print axioms final_claim58
theorem concrete_59_60912 : Fintype.card (Vertex 5) = 60912 ∧ (∀ v, (graph 5).degree v ≤ 59) ∧
  DiameterAtMost (graph 5) 3 ∧ ¬DiameterAtMost (graph 5) 2 := fixed_family_target 5
def FinalClaim59 : Prop := Fintype.card (Vertex 5) = 60912 ∧ (∀ v, (graph 5).degree v ≤ 59) ∧
  DiameterAtMost (graph 5) 3 ∧ ¬DiameterAtMost (graph 5) 2
theorem final_claim59 : FinalClaim59 := concrete_59_60912
#print axioms concrete_59_60912
#print axioms final_claim59
#print axioms fixed_family_target
end DegreeDiameter.Portfolio.F9U10PlaneCloneFamily

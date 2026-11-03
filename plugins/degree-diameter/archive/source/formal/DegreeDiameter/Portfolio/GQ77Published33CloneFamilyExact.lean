import DegreeDiameter.Portfolio.GQ77Published33CloneFamilyInputs
import DegreeDiameter.Portfolio.OppositeGQ77SpreadExact
namespace DegreeDiameter.Portfolio.GQ77Published33CloneFamily
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
theorem source_no_isolated (v : Source.Vertex) : ∃ w, OppositeGQ77Spread.graph.Adj v w := by
  have ht : ∃ t : Source.Vertex, v ≠ t := by
    by_cases h0 : v = .inl (0 : OppositeGQ77Spread.Old)
    · refine ⟨.inl (1 : OppositeGQ77Spread.Old),?_⟩
      rw [h0]
      decide
    · exact ⟨.inl (0 : OppositeGQ77Spread.Old),h0⟩
  obtain ⟨t,ht⟩ := ht
  obtain ⟨p,_⟩ := OppositeGQ77Spread.concrete_order_degree_and_exact_D3.2.2.1 v t
  obtain ⟨w,hw,tail,heq⟩ := SimpleGraph.Walk.exists_eq_cons_of_ne ht p
  exact ⟨w,hw⟩


theorem old_walk_bound_iff (k : Nat) (u v : Source.Vertex) (n : Nat) :
    (∃ p : (graph k).Walk (.inl u) (.inl v), p.length ≤ n) ↔
      ∃ p : OppositeGQ77Spread.graph.Walk u v, p.length ≤ n :=
  FullNeighborhoodClones.old_walk_bound_iff OppositeGQ77Spread.graph (center k) u v n
theorem degree_le (k : Nat) : ∀ v, (graph k).degree v ≤ 64+k :=
  FullNeighborhoodClones.degree_le OppositeGQ77Spread.graph (center k) 64 k
    OppositeGQ77Spread.concrete_order_degree_and_exact_D3.2.1 (copy_load_le k)
theorem diameterAtMost_three (k : Nat) : DiameterAtMost (graph k) 3 :=
  FullNeighborhoodClones.diameterAtMost OppositeGQ77Spread.graph (center k) 3 (by decide)
    OppositeGQ77Spread.concrete_order_degree_and_exact_D3.2.2.1 source_no_isolated
theorem not_diameterAtMost_two (k : Nat) : ¬DiameterAtMost (graph k) 2 :=
  FullNeighborhoodClones.not_diameterAtMost OppositeGQ77Spread.graph (center k) 2
    OppositeGQ77Spread.concrete_order_degree_and_exact_D3.2.2.2
theorem fixed_family_target (k : Nat) : Fintype.card (Vertex k) = 160050+1650*k ∧
    (∀ v, (graph k).degree v ≤ 64+k) ∧ DiameterAtMost (graph k) 3 ∧ ¬DiameterAtMost (graph k) 2 :=
  ⟨card_vertex k,degree_le k,diameterAtMost_three k,not_diameterAtMost_two k⟩
theorem fixed_family_claim (k : Nat) : FinalClaim k := fixed_family_target k
theorem d65_161700 : Fintype.card (Vertex 1) = 161700 ∧ (∀ v, (graph 1).degree v ≤ 65) ∧
  DiameterAtMost (graph 1) 3 ∧ ¬DiameterAtMost (graph 1) 2 := fixed_family_target 1
def FinalClaim65 : Prop := Fintype.card (Vertex 1) = 161700 ∧ (∀ v, (graph 1).degree v ≤ 65) ∧
  DiameterAtMost (graph 1) 3 ∧ ¬DiameterAtMost (graph 1) 2
theorem final_claim65 : FinalClaim65 := d65_161700
theorem d66_163350 : Fintype.card (Vertex 2) = 163350 ∧ (∀ v, (graph 2).degree v ≤ 66) ∧
  DiameterAtMost (graph 2) 3 ∧ ¬DiameterAtMost (graph 2) 2 := fixed_family_target 2
def FinalClaim66 : Prop := Fintype.card (Vertex 2) = 163350 ∧ (∀ v, (graph 2).degree v ≤ 66) ∧
  DiameterAtMost (graph 2) 3 ∧ ¬DiameterAtMost (graph 2) 2
theorem final_claim66 : FinalClaim66 := d66_163350
theorem d67_165000 : Fintype.card (Vertex 3) = 165000 ∧ (∀ v, (graph 3).degree v ≤ 67) ∧
  DiameterAtMost (graph 3) 3 ∧ ¬DiameterAtMost (graph 3) 2 := fixed_family_target 3
def FinalClaim67 : Prop := Fintype.card (Vertex 3) = 165000 ∧ (∀ v, (graph 3).degree v ≤ 67) ∧
  DiameterAtMost (graph 3) 3 ∧ ¬DiameterAtMost (graph 3) 2
theorem final_claim67 : FinalClaim67 := d67_165000
theorem d68_166650 : Fintype.card (Vertex 4) = 166650 ∧ (∀ v, (graph 4).degree v ≤ 68) ∧
  DiameterAtMost (graph 4) 3 ∧ ¬DiameterAtMost (graph 4) 2 := fixed_family_target 4
def FinalClaim68 : Prop := Fintype.card (Vertex 4) = 166650 ∧ (∀ v, (graph 4).degree v ≤ 68) ∧
  DiameterAtMost (graph 4) 3 ∧ ¬DiameterAtMost (graph 4) 2
theorem final_claim68 : FinalClaim68 := d68_166650
theorem d69_168300 : Fintype.card (Vertex 5) = 168300 ∧ (∀ v, (graph 5).degree v ≤ 69) ∧
  DiameterAtMost (graph 5) 3 ∧ ¬DiameterAtMost (graph 5) 2 := fixed_family_target 5
def FinalClaim69 : Prop := Fintype.card (Vertex 5) = 168300 ∧ (∀ v, (graph 5).degree v ≤ 69) ∧
  DiameterAtMost (graph 5) 3 ∧ ¬DiameterAtMost (graph 5) 2
theorem final_claim69 : FinalClaim69 := d69_168300
theorem d70_169950 : Fintype.card (Vertex 6) = 169950 ∧ (∀ v, (graph 6).degree v ≤ 70) ∧
  DiameterAtMost (graph 6) 3 ∧ ¬DiameterAtMost (graph 6) 2 := fixed_family_target 6
def FinalClaim70 : Prop := Fintype.card (Vertex 6) = 169950 ∧ (∀ v, (graph 6).degree v ≤ 70) ∧
  DiameterAtMost (graph 6) 3 ∧ ¬DiameterAtMost (graph 6) 2
theorem final_claim70 : FinalClaim70 := d70_169950
theorem d71_171600 : Fintype.card (Vertex 7) = 171600 ∧ (∀ v, (graph 7).degree v ≤ 71) ∧
  DiameterAtMost (graph 7) 3 ∧ ¬DiameterAtMost (graph 7) 2 := fixed_family_target 7
def FinalClaim71 : Prop := Fintype.card (Vertex 7) = 171600 ∧ (∀ v, (graph 7).degree v ≤ 71) ∧
  DiameterAtMost (graph 7) 3 ∧ ¬DiameterAtMost (graph 7) 2
theorem final_claim71 : FinalClaim71 := d71_171600
theorem d72_173250 : Fintype.card (Vertex 8) = 173250 ∧ (∀ v, (graph 8).degree v ≤ 72) ∧
  DiameterAtMost (graph 8) 3 ∧ ¬DiameterAtMost (graph 8) 2 := fixed_family_target 8
def FinalClaim72 : Prop := Fintype.card (Vertex 8) = 173250 ∧ (∀ v, (graph 8).degree v ≤ 72) ∧
  DiameterAtMost (graph 8) 3 ∧ ¬DiameterAtMost (graph 8) 2
theorem final_claim72 : FinalClaim72 := d72_173250
#print axioms fixed_family_target
end DegreeDiameter.Portfolio.GQ77Published33CloneFamily

import DegreeDiameter.Portfolio.EvenQ8SourceFullDerivedInputs
import DegreeDiameter.Portfolio.EvenQ8SourceFullBalancedInputs
namespace DegreeDiameter.Portfolio.EvenQ8SourceFull
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
abbrev graph80 : SimpleGraph DegreeDiameter.Portfolio.EvenQ8Source.Derived.Vertex := DegreeDiameter.Portfolio.EvenQ8Source.Derived.graph
namespace D80_327744
abbrev Vertex := DegreeDiameter.Portfolio.EvenQ8Source.Derived.Vertex
def label : Vertex ≃ Fin 327744 := DegreeDiameter.Portfolio.EvenQ8Source.Derived.label
def FinalClaim : Prop :=
  Fintype.card Vertex = 327744 ∧
  (∀ u, graph80.degree u ≤ 80) ∧
  DiameterAtMost graph80 3 ∧ ¬ DiameterAtMost graph80 2
theorem final_claim : FinalClaim := by
  simpa only [FinalClaim,graph80,Fintype.card_fin] using
    (OppositeIncidenceSpread.order_degree_and_exact_D3
      DegreeDiameter.Portfolio.EvenQ8Source.Derived.oldEquiv DegreeDiameter.Portfolio.EvenQ8Source.Derived.linePoint DegreeDiameter.Portfolio.EvenQ8Source.Derived.pointLine
      DegreeDiameter.Portfolio.EvenQ8Source.Derived.spread DegreeDiameter.Portfolio.EvenQ8Source.Derived.spreadOwner (by decide)
      Derived.hline Derived.howner Derived.project (by decide))
theorem label_old (v : DegreeDiameter.Portfolio.EvenQ8Source.Derived.Old) : (label (.inl v)).val = v.val := rfl
theorem label_new (j : DegreeDiameter.Portfolio.EvenQ8Source.Derived.Helper) : (label (.inr j)).val = 327680+j.val := rfl
#check final_claim
#print axioms final_claim
end D80_327744
theorem d80_327744 : D80_327744.FinalClaim := D80_327744.final_claim
abbrev graph81 : SimpleGraph DegreeDiameter.Portfolio.EvenQ8Source.Balanced.Vertex := DegreeDiameter.Portfolio.EvenQ8Source.Balanced.graph
namespace D81_342290
abbrev Vertex := DegreeDiameter.Portfolio.EvenQ8Source.Balanced.Vertex
def label : Vertex ≃ Fin 342290 := DegreeDiameter.Portfolio.EvenQ8Source.Balanced.label
def FinalClaim : Prop :=
  Fintype.card Vertex = 342290 ∧
  (∀ u, graph81.degree u ≤ 81) ∧
  DiameterAtMost graph81 3 ∧ ¬ DiameterAtMost graph81 2
theorem final_claim : FinalClaim := by
  simpa only [FinalClaim,graph81,Fintype.card_fin] using
    (OppositeIncidenceSpread.order_degree_and_exact_D3
      DegreeDiameter.Portfolio.EvenQ8Source.Balanced.oldEquiv DegreeDiameter.Portfolio.EvenQ8Source.Balanced.linePoint DegreeDiameter.Portfolio.EvenQ8Source.Balanced.pointLine
      DegreeDiameter.Portfolio.EvenQ8Source.Balanced.spread DegreeDiameter.Portfolio.EvenQ8Source.Balanced.spreadOwner (by decide)
      Balanced.hline Balanced.howner Balanced.project (by decide))
theorem label_old (v : DegreeDiameter.Portfolio.EvenQ8Source.Balanced.Old) : (label (.inl v)).val = v.val := rfl
theorem label_new (j : DegreeDiameter.Portfolio.EvenQ8Source.Balanced.Helper) : (label (.inr j)).val = 342225+j.val := rfl
#check final_claim
#print axioms final_claim
end D81_342290
theorem d81_342290 : D81_342290.FinalClaim := D81_342290.final_claim
end DegreeDiameter.Portfolio.EvenQ8SourceFull

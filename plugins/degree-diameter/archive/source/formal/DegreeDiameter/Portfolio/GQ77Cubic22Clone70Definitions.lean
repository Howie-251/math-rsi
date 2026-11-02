import DegreeDiameter.Portfolio.GQ77Cubic22Clone65Definitions
namespace DegreeDiameter.Portfolio.GQ77Cubic22Clone70
namespace Source
abbrev Vertex := OppositeGQ77Spread.Vertex
end Source
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
abbrev CloneIndex := Fin 6600
abbrev Vertex := Source.Vertex ⊕ CloneIndex
def cloneLabel : (Fin 6 × Fin 1100) ≃ CloneIndex := finProdFinEquiv
def clonePair : CloneIndex ≃ (Fin 6 × Fin 1100) := cloneLabel.symm
/-- Six copies of each fixed base center, all in the immutable original160050 source. -/
def center (k : CloneIndex) : Source.Vertex := GQ77Cubic22Clone65.center (clonePair k).2
def graph : SimpleGraph Vertex := FullNeighborhoodClones.graph OppositeGQ77Spread.graph center
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (FullNeighborhoodClones.graph OppositeGQ77Spread.graph center).Adj)
def label : Vertex ≃ Fin 166650 :=
  (Equiv.sumCongr OppositeGQ77Spread.label (Equiv.refl CloneIndex)).trans finSumFinEquiv
theorem clone_label (c : Fin 6) (b : Fin 1100) : (cloneLabel (c,b)).val = b.val+1100*c.val := rfl
theorem label_old (v : Source.Vertex) : (label (.inl v)).val = (OppositeGQ77Spread.label v).val := rfl
theorem label_new (k : CloneIndex) : (label (.inr k)).val = 160050+k.val := rfl
theorem label_new_copy (c : Fin 6) (i : Fin 22) (j : Fin 50) :
    (label (.inr (cloneLabel (c,GQ77Cubic22Clone65.cloneLabel (i,j))))).val =
      160050+1100*c.val+50*i.val+j.val := by
  change 160050+((j.val+50*i.val)+1100*c.val) = 160050+1100*c.val+50*i.val+j.val
  omega
theorem center_source_label (k : CloneIndex) :
    (OppositeGQ77Spread.label (center k)).val =
      (OppositeGQ77Spread.spread (GQ77Cubic22Clone65.clonePair (clonePair k).2).2).val+
        400*(GQ77Cubic22Clone65.ovoid (GQ77Cubic22Clone65.clonePair (clonePair k).2).1).val := rfl
theorem card_vertex : Fintype.card Vertex = 166650 := by
  simp only [Fintype.card_sum,Fintype.card_fin]
def FinalClaim : Prop := Fintype.card Vertex = 166650 ∧ (∀ v, graph.degree v ≤ 70) ∧
  DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#print center
#print graph
#print label
#print FinalClaim
end DegreeDiameter.Portfolio.GQ77Cubic22Clone70

import DegreeDiameter.Portfolio.OppositeGQ77SpreadDefinitions
import DegreeDiameter.Portfolio.OvoidSpreadCloneCapacity
namespace DegreeDiameter.Portfolio.GQ77Cubic22Clone65
namespace Source
abbrev Vertex := OppositeGQ77Spread.Vertex
end Source
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
abbrev CloneIndex := Fin 1100
abbrev Vertex := Source.Vertex ⊕ CloneIndex
/-- The literal ordered three cubic cosets and infinity, bound externally to GF7 geometry. -/
def ovoid : Fin 22 → OppositeGQ77Spread.Point := ![57, 119, 165, 251, 265, 347, 399, 71, 133, 179, 216, 279, 312, 364, 85, 147, 193, 230, 293, 326, 378, 1]
def cloneLabel : (Fin 22 × Fin 50) ≃ CloneIndex := finProdFinEquiv
def clonePair : CloneIndex ≃ (Fin 22 × Fin 50) := cloneLabel.symm
/-- Fixed original160050-source owners; point index outer, original spread index inner.
Every clone uses the immutable original source neighborhood, including its original bonuses. -/
def center (k : CloneIndex) : Source.Vertex :=
  OvoidSpreadCloneCapacity.center OppositeGQ77Spread.oldEquiv ovoid OppositeGQ77Spread.spread (clonePair k)
def graph : SimpleGraph Vertex := FullNeighborhoodClones.graph OppositeGQ77Spread.graph center
instance : DecidableRel graph.Adj := inferInstanceAs
  (DecidableRel (FullNeighborhoodClones.graph OppositeGQ77Spread.graph center).Adj)
def label : Vertex ≃ Fin 161150 :=
  (Equiv.sumCongr OppositeGQ77Spread.label (Equiv.refl CloneIndex)).trans finSumFinEquiv
theorem center_source_label (k : CloneIndex) :
    (OppositeGQ77Spread.label (center k)).val =
      (OppositeGQ77Spread.spread (clonePair k).2).val+400*(ovoid (clonePair k).1).val := rfl
theorem clone_label (i : Fin 22) (j : Fin 50) : (cloneLabel (i,j)).val = j.val+50*i.val := rfl
theorem label_old (v : Source.Vertex) : (label (.inl v)).val = (OppositeGQ77Spread.label v).val := rfl
theorem label_new (k : CloneIndex) : (label (.inr k)).val = 160050+k.val := rfl
theorem card_vertex : Fintype.card Vertex = 161150 := by
  simp only [Fintype.card_sum,Fintype.card_fin]
/-- Auxiliary finite certificate records the unique chosen point index, when present. -/
def ovoidOwnerBlocks : Fin 20 → Fin 20 → Option (Fin 22) := ![![none, some 21, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none], ![none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none], ![none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, some 0, none, none], ![none, none, none, none, none, none, none, none, none, none, none, some 7, none, none, none, none, none, none, none, none], ![none, none, none, none, none, some 14, none, none, none, none, none, none, none, none, none, none, none, none, none, none], ![none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, some 1], ![none, none, none, none, none, none, none, none, none, none, none, none, none, some 8, none, none, none, none, none, none], ![none, none, none, none, none, none, none, some 15, none, none, none, none, none, none, none, none, none, none, none, none], ![none, none, none, none, none, some 2, none, none, none, none, none, none, none, none, none, none, none, none, none, some 9], ![none, none, none, none, none, none, none, none, none, none, none, none, none, some 16, none, none, none, none, none, none], ![none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, some 10, none, none, none], ![none, none, none, none, none, none, none, none, none, none, some 17, none, none, none, none, none, none, none, none, none], ![none, none, none, none, none, none, none, none, none, none, none, some 3, none, none, none, none, none, none, none, none], ![none, none, none, none, none, some 4, none, none, none, none, none, none, none, none, none, none, none, none, none, some 11], ![none, none, none, none, none, none, none, none, none, none, none, none, none, some 18, none, none, none, none, none, none], ![none, none, none, none, none, none, none, none, none, none, none, none, some 12, none, none, none, none, none, none, none], ![none, none, none, none, none, none, some 19, none, none, none, none, none, none, none, none, none, none, none, none, none], ![none, none, none, none, none, none, none, some 5, none, none, none, none, none, none, none, none, none, none, none, none], ![none, none, none, none, some 13, none, none, none, none, none, none, none, none, none, none, none, none, none, some 20, none], ![none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, some 6]]
def ovoidOwner (p : OppositeGQ77Spread.Point) : Option (Fin 22) :=
  OppositeGQ77Spread.lookup400 ovoidOwnerBlocks p
/-- Arbitrary index0 for the224 unoccupied lines; used only in an implication. -/
def lineOvoidIndexBlocks : Fin 20 → Fin 20 → Fin 22 := ![![21, 0, 0, 7, 0, 14, 0, 0, 21, 21, 21, 21, 21, 21, 21, 9, 0, 2, 0, 0], ![16, 0, 8, 0, 0, 15, 1, 0, 0, 0, 3, 10, 17, 0, 0, 0, 11, 4, 0, 0], ![0, 0, 18, 0, 13, 0, 0, 6, 20, 0, 0, 0, 5, 0, 12, 0, 19, 0, 0, 7], ![0, 14, 0, 0, 0, 13, 7, 20, 14, 0, 6, 0, 12, 7, 19, 14, 0, 5, 0, 4], ![7, 11, 14, 18, 0, 0, 10, 7, 17, 14, 0, 3, 0, 2, 7, 9, 14, 16, 0, 0], ![1, 7, 8, 14, 15, 0, 17, 18, 0, 3, 4, 10, 11, 1, 5, 8, 12, 15, 19, 0], ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![0, 0, 0, 0, 0, 0, 0, 0, 6, 9, 13, 16, 20, 0, 2, 19, 16, 0, 5, 2], ![12, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 8, 10, 15], ![17, 0, 1, 4, 6, 11, 13, 18, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 2, 4, 9, 11, 16, 0, 0], ![6, 0, 13, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8], ![0, 15, 0, 0, 1, 0, 12, 17, 19, 0, 3, 5, 10, 20, 15, 0, 6, 1, 13, 8], ![0, 0, 0, 0, 0, 0, 0, 2, 3, 9, 10, 16, 17, 0, 0, 0, 0, 0, 0, 0], ![0, 0, 0, 0, 0, 0, 0, 0, 5, 11, 12, 18, 19, 0, 4, 0, 0, 0, 0, 0], ![0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 4, 1], ![11, 8, 18, 9, 0, 16, 0, 0, 2, 0, 0, 0, 5, 0, 12, 0, 19, 10, 20, 17], ![0, 6, 3, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ![3, 0, 10, 0, 17, 0, 0, 0, 0, 0, 0, 0, 13, 19, 20, 0, 5, 6, 12, 16], ![0, 1, 2, 8, 9, 15, 0, 0, 0, 0, 0, 0, 0, 11, 0, 18, 0, 0, 4, 0]]
def lineOvoidIndex (l : OppositeGQ77Spread.Line) : Fin 22 :=
  OppositeGQ77Spread.lookup400 lineOvoidIndexBlocks l
def FinalClaim : Prop := Fintype.card Vertex = 161150 ∧ (∀ v, graph.degree v ≤ 65) ∧
  DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#print center
#print graph
#print label
#print FinalClaim
end DegreeDiameter.Portfolio.GQ77Cubic22Clone65

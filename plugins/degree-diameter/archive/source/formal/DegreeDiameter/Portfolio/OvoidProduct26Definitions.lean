import DegreeDiameter.Portfolio.OppositeGQ44SpreadExact
import DegreeDiameter.Portfolio.OvoidSpreadCloneCapacity
namespace DegreeDiameter.Portfolio.OvoidProduct26
namespace Source
abbrev Vertex := OppositeGQ44Spread.Vertex
end Source
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
abbrev CloneIndex := Fin 17 × Fin 17
abbrev Vertex := Source.Vertex ⊕ CloneIndex
def ovoid : Fin 17 → OppositeGQ44Spread.Point := ![1, 5, 8, 18, 19, 39, 41, 48, 50, 54, 56, 65, 67, 75, 76, 77, 78]
/-- Fixed original7242-source owners; product order is ovoid index outer,
original spread index inner. The source is never the evolving clone graph. -/
def center : CloneIndex → Source.Vertex :=
  OvoidSpreadCloneCapacity.center OppositeGQ44Spread.oldEquiv ovoid OppositeGQ44Spread.spread

def graph : SimpleGraph Vertex := FullNeighborhoodClones.graph OppositeGQ44Spread.graph center
instance : DecidableRel graph.Adj := inferInstanceAs (DecidableRel (FullNeighborhoodClones.graph OppositeGQ44Spread.graph center).Adj)
def cloneLabel : CloneIndex ≃ Fin 289 := finProdFinEquiv

def label : Vertex ≃ Fin 7531 :=
  (Equiv.sumCongr OppositeGQ44Spread.label cloneLabel).trans finSumFinEquiv

theorem center_source_label (i j : Fin 17) :
    (OppositeGQ44Spread.label (center (i,j))).val = (OppositeGQ44Spread.spread j).val+85*(ovoid i).val := rfl

theorem clone_label (i j : Fin 17) : (cloneLabel (i,j)).val = j.val+17*i.val := rfl

theorem label_old (v : Source.Vertex) : (label (.inl v)).val = (OppositeGQ44Spread.label v).val := rfl

theorem label_new (i j : Fin 17) : (label (.inr (i,j))).val = 7242+17*i.val+j.val := by
  change 7242+(j.val+17*i.val) = 7242+17*i.val+j.val
  omega

theorem card_vertex : Fintype.card Vertex = 7531 := by
  simp only [Fintype.card_sum,Fintype.card_prod,Fintype.card_fin]

/-- Auxiliary finite certificate for at-most-one ovoid INDEX on every line. -/
def ovoidOwner : OppositeGQ44Spread.Point → Option (Fin 17) := ![none, some 0, none, none, none, some 1, none, none, some 2, none, none, none, none, none, none, none, none, none, some 3, some 4, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, none, some 5, none, some 6, none, none, none, none, none, none, some 7, none, some 8, none, none, none, some 9, none, some 10, none, none, none, none, none, none, none, none, some 11, none, some 12, none, none, none, none, none, none, none, some 13, some 14, some 15, some 16, none, none, none, none, none, none]
def lineOvoidIndex : OppositeGQ44Spread.Line → Fin 17 := ![0, 5, 6, 7, 8, 0, 0, 0, 0, 1, 4, 3, 2, 13, 14, 16, 15, 12, 9, 11, 10, 1, 1, 1, 1, 10, 14, 15, 11, 9, 13, 16, 12, 2, 2, 2, 2, 6, 16, 13, 7, 6, 12, 9, 7, 6, 11, 10, 7, 6, 15, 14, 7, 11, 8, 5, 10, 13, 8, 5, 16, 14, 8, 5, 15, 12, 8, 5, 9, 15, 9, 12, 14, 3, 3, 3, 3, 4, 4, 4, 4, 16, 10, 11, 13]
def FinalClaim : Prop := Fintype.card Vertex = 7531 ∧ (∀ v, graph.degree v ≤ 26) ∧
  DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#print center
#print graph
#print label
#print FinalClaim
end DegreeDiameter.Portfolio.OvoidProduct26

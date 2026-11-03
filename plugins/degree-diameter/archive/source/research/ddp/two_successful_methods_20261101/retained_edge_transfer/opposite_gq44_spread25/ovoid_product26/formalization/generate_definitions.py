import json
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;P=D.parent;F=R/'formal/DegreeDiameter/Portfolio';geo=json.loads((P/'OVOID_GEOMETRY_CHECK.json').read_text());ov=geo['ovoid_point_ids'];vec=lambda a:'!['+', '.join(map(str,a))+']'
owner=['none']*85
for i,p in enumerate(ov):owner[p]=f'some {i}'
idx=[ov.index(p) for p in geo['line_to_unique_ovoid_point']]
s='''import DegreeDiameter.Portfolio.OppositeGQ44SpreadExact
import DegreeDiameter.Portfolio.OvoidSpreadCloneCapacity
namespace DegreeDiameter.Portfolio.OvoidProduct26
namespace Source
abbrev Vertex := OppositeGQ44Spread.Vertex
end Source
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
abbrev CloneIndex := Fin 17 × Fin 17
abbrev Vertex := Source.Vertex ⊕ CloneIndex
'''
s+='def ovoid : Fin 17 → OppositeGQ44Spread.Point := '+vec(ov)+'\n'
s+='''/-- Fixed original7242-source owners; product order is ovoid index outer,
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
'''
s+='def ovoidOwner : OppositeGQ44Spread.Point → Option (Fin 17) := '+vec(owner)+'\n'
s+='def lineOvoidIndex : OppositeGQ44Spread.Line → Fin 17 := '+vec(idx)+'\n'
s+='''def FinalClaim : Prop := Fintype.card Vertex = 7531 ∧ (∀ v, graph.degree v ≤ 26) ∧
  DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#print center
#print graph
#print label
#print FinalClaim
end DegreeDiameter.Portfolio.OvoidProduct26
'''
(F/'OvoidProduct26Definitions.lean').write_text(s)

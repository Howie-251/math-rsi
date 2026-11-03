import json,re
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;P=D.parent
x=json.loads((P/'PARAMETERS.json').read_text());lines=[l['points'] for l in x['lines']];through=x['point_incident_lines']
arr=lambda z:'#['+', '.join(map(str,z))+']'
s='''import DegreeDiameter.Portfolio.OppositeGQ35SpreadGeneric
import Mathlib.Logic.Equiv.Fin.Basic
namespace DegreeDiameter.Portfolio.OppositeGQ35Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
abbrev Point := Fin 64
abbrev Line := Fin 96
abbrev Old := Fin 6144
abbrev New := Fin 16
abbrev Vertex := Old ⊕ New
/-- Literal rows in PARAMETERS order; point code is a+4*b+16*c over GF4. -/
'''
s+='def linePointData : Array Nat := '+arr(sum(lines,[]))+'\n'
s+='def pointLineData : Array Nat := '+arr(sum(through,[]))+'\n'
s+='''def linePoint (l : Line) (i : Fin 4) : Point :=
  ⟨linePointData.getD (4*l.val+i.val) 0 % 64, Nat.mod_lt _ (by decide)⟩
def pointLine (p : Point) (i : Fin 6) : Line :=
  ⟨pointLineData.getD (6*p.val+i.val) 0 % 96, Nat.mod_lt _ (by decide)⟩
/-- Incidence is literal membership in the four entries of the chosen line. -/
def Inc (p : Point) (l : Line) : Prop := ∃ i : Fin 4, linePoint l i = p
instance : DecidableRel Inc := fun p l => inferInstanceAs (Decidable (∃ i : Fin 4, linePoint l i = p))
def spread (j : New) : Line := ⟨j.val,by omega⟩
def spreadOwner (p : Point) : New := ⟨p.val / 4,by omega⟩
def oldEquiv : Old ≃ Point × Line := (finProdFinEquiv (m := 64) (n := 96)).symm
def old (p : Point) (l : Line) : Old := oldEquiv.symm (p,l)
def graph : SimpleGraph Vertex := OppositeGQSpread.graph oldEquiv Inc spread
instance : DecidableRel graph.Adj := inferInstanceAs (DecidableRel (OppositeGQSpread.graph oldEquiv Inc spread).Adj)
def label : Vertex ≃ Fin 6160 := finSumFinEquiv

theorem old_label (p : Point) (l : Line) : (old p l).val = l.val+96*p.val := rfl
theorem label_old (v : Old) : (label (.inl v)).val = v.val := rfl
theorem label_new (j : New) : (label (.inr j)).val = 6144+j.val := rfl
theorem card_vertex : Fintype.card Vertex = 6160 := by simp only [Fintype.card_sum,Fintype.card_fin]

/-- The final target: no incidence, projection or capacity premise is exported. -/
def FinalClaim : Prop := Fintype.card Vertex = 6160 ∧ (∀ v, graph.degree v ≤ 24) ∧
  DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#print graph
#print Inc
#print oldEquiv
#print label
#print FinalClaim
end DegreeDiameter.Portfolio.OppositeGQ35Spread
'''
(R/'formal/DegreeDiameter/Portfolio/OppositeGQ35SpreadDefinitions.lean').write_text(s)
binding={'status':'LITERAL_DEFINITION_DATA_MATCH','point_encoding':x['point_label'],'line_rows':len(lines),'line_entries':sum(map(len,lines)),'point_incident_rows':len(through),'point_incident_entries':sum(map(len,through)),'all_points_order_exact':x['points']==[[n%4,n//4%4,n//16] for n in range(64)],'all_spread_labels_order_exact':x['spread_line_labels']==list(range(16)),'old_label':'line+96*point (equal 96*point+line)','new_label':'6144+spread_index','graph_semantics':'old distinct opposite-incidence; old-new iff point belongs to its old line and chosen spread line; new-new false','ASCII_parser_theorem':False,'pending':'readback literal arrays + ordered EXTENSION_STEPS pins after final caller compilation'}
(D/'INPUT_BINDING_CHECK.json').write_text(json.dumps(binding,indent=2)+'\n')

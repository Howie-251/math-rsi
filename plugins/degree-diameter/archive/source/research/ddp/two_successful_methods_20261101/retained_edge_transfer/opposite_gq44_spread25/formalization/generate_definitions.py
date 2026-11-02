import json
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;P=D.parent;F=R/'formal/DegreeDiameter/Portfolio'
x=json.loads((P/'PARAMETERS.json').read_text());ls=[l['points'] for l in x['lines']];pl=x['point_incident_lines'];vec=lambda a:'!['+', '.join(map(str,a))+']'
s='''import DegreeDiameter.Portfolio.OppositeIncidenceSpreadFamily
namespace DegreeDiameter.Portfolio.OppositeGQ44Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
abbrev Point := Fin 85
abbrev Line := Fin 85
abbrev Old := Fin 7225
abbrev New := Fin 17
abbrev Vertex := Old ⊕ New
/-- Actual PARAMETERS order: GF4 projective four-tuples, first nonzero entry1,
lexicographic point labels. Incidence below is the fixed literal line list;
no ZMod4 arithmetic or generic field-existence assertion is used. -/
'''
s+='def linePoint : Line → Fin 5 → Point := !['+', '.join(map(vec,ls))+']\n'
s+='def pointLine : Point → Fin 5 → Line := !['+', '.join(map(vec,pl))+']\n'
s+='def spread : New → Line := '+vec(x['spread_line_labels'])+'\n'
s+='def spreadOwner : Point → New := '+vec(x['point_spread_owner'])+'\n'
s+='''abbrev Inc (p : Point) (l : Line) : Prop := OppositeIncidenceSpread.Inc linePoint p l
instance : DecidableRel Inc := inferInstanceAs (DecidableRel (OppositeIncidenceSpread.Inc linePoint))
def oldEquiv : Old ≃ Point × Line := (finProdFinEquiv (m:=85) (n:=85)).symm
def old (p : Point) (l : Line) : Old := oldEquiv.symm (p,l)
def graph : SimpleGraph Vertex := OppositeIncidenceSpread.graph oldEquiv linePoint spread
instance : DecidableRel graph.Adj := inferInstanceAs (DecidableRel (OppositeIncidenceSpread.graph oldEquiv linePoint spread).Adj)
def label : Vertex ≃ Fin 7242 := finSumFinEquiv

theorem old_label (p : Point) (l : Line) : (old p l).val = l.val+85*p.val := rfl
theorem label_old (v : Old) : (label (.inl v)).val = v.val := rfl
theorem label_new (j : New) : (label (.inr j)).val = 7225+j.val := rfl
theorem card_vertex : Fintype.card Vertex = 7242 := by simp only [Fintype.card_sum,Fintype.card_fin]

def FinalClaim : Prop := Fintype.card Vertex = 7242 ∧ (∀ v, graph.degree v ≤ 25) ∧
  DiameterAtMost graph 3 ∧ ¬DiameterAtMost graph 2
#print graph
#print Inc
#print oldEquiv
#print label
#print FinalClaim
end DegreeDiameter.Portfolio.OppositeGQ44Spread
'''
(F/'OppositeGQ44SpreadDefinitions.lean').write_text(s)
mods=['OppositeIncidenceSpreadSlots','OppositeIncidenceSpreadFamily','OppositeIncidenceSpreadAudit'];receipts=[json.loads((D/f'{m}_RESULT.json').read_text()) for m in mods];assert all(r['exit_code']==0 for r in receipts)
(D/'GENERIC_COMPILE_RESULT.json').write_text(json.dumps({'status':'PASS_CONDITIONAL_REUSABLE_FAMILY_AND_INDEPENDENT_IMPORT_AUDIT','CPU_seconds':sum(r['CPU_seconds'] for r in receipts),'CPU_budget_seconds':200,'concrete_graph_claim_in_this_generic_receipt':False,'axioms':['propext','Classical.choice','Quot.sound'],'old_modules_changed_or_recompiled':False,'receipts':receipts},indent=2)+'\n')

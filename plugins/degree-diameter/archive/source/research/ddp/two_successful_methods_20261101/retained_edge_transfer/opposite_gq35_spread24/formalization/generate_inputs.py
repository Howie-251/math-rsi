import json
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;P=D.parent;F=R/'formal/DegreeDiameter/Portfolio'
x=json.loads((P/'PARAMETERS.json').read_text());lines=[l['points'] for l in x['lines']];through=x['point_incident_lines']
w=[]
for p in range(64):
 for l in range(96):
  choices=[(q,m) for q in lines[l] for m in through[p] if q in lines[m]]
  assert choices
  q,m=choices[0];w.append(q+64*m)
s='''import DegreeDiameter.Portfolio.OppositeGQ35SpreadFastTables
namespace DegreeDiameter.Portfolio.OppositeGQ35Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
/-- Chosen point-line incidence witnesses, packed q+64*m. Kernel row proofs
check all6144 original point-line pairs; this is not a distance table. -/
'''
s+='def projectionData : Fin 64 → Array Nat := !['+', '.join('#['+', '.join(map(str,w[p*96:(p+1)*96]))+']' for p in range(64))+']\n'
s+='''def projectionCode (p : Point) (l : Line) : Nat := (projectionData p).getD l.val 0
def projectionPoint (p : Point) (l : Line) : Point :=
  ⟨projectionCode p l % 64,Nat.mod_lt _ (by decide)⟩
def projectionLine (p : Point) (l : Line) : Line :=
  ⟨projectionCode p l / 64 % 96,Nat.mod_lt _ (by decide)⟩
def InputRow (p : Point) : Prop :=
  (∀ l, Inc (projectionPoint p l) l ∧ Inc p (projectionLine p l) ∧
    Inc (projectionPoint p l) (projectionLine p l)) ∧
  (∀ l, Inc p l → ∃ i : Fin 6, pointLine p i = l) ∧
  (∀ j, Inc p (spread j) → j = spreadOwner p)
end DegreeDiameter.Portfolio.OppositeGQ35Spread
'''
(F/'OppositeGQ35SpreadInputData.lean').write_text(s)
for p in range(64):
 s=f'''import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputData
namespace DegreeDiameter.Portfolio.OppositeGQ35Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
theorem input_row_{p:02} : InputRow {p} := by
  unfold InputRow
  simp only [Inc,linePoint_eq_fast,pointLine_eq_fast]
  decide
end DegreeDiameter.Portfolio.OppositeGQ35Spread
'''
 (F/f'OppositeGQ35SpreadInputRow{p:02}.lean').write_text(s)

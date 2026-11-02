import json
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;P=D.parent;F=R/'formal/DegreeDiameter/Portfolio'
x=json.loads((P/'PARAMETERS.json').read_text());ls=[l['points'] for l in x['lines']];pl=x['point_incident_lines'];w=json.loads((P/'PROJECTION_WITNESSES.json').read_text());witness={(p,l):(q,m) for p,l,q,m in w['rows']};assert len(witness)==6800
for p in range(85):
 ix=[]
 for l in range(85):
  q,m=(p,l) if p in ls[l] else witness[p,l]
  ix.append((ls[l].index(q),pl[p].index(m),ls[m].index(q)))
 s=f'''import DegreeDiameter.Portfolio.OppositeGQ44SpreadInputInterface
namespace DegreeDiameter.Portfolio.OppositeGQ44Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
def projectionIndices{p:02} : Line → Fin 5 × Fin 5 × Fin 5 := !['''+', '.join(f'({a},{b},{c})' for a,b,c in ix)+']\n'
 s+=f'''theorem projection_check_{p:02} : ProjectionIndexCheck {p} projectionIndices{p:02} := by
  unfold ProjectionIndexCheck
  decide
theorem projection_row_{p:02} : ProjectionRow {p} :=
  projection_row_of_check {p} projectionIndices{p:02} projection_check_{p:02}
end DegreeDiameter.Portfolio.OppositeGQ44Spread
'''
 (F/f'OppositeGQ44SpreadInputRow{p:02}.lean').write_text(s)

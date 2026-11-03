import json
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;F=R/'formal/DegreeDiameter/Portfolio'
x=json.loads((D.parent/'PARAMETERS.json').read_text());ls=[l['points'] for l in x['lines']];through=x['point_incident_lines']
s='''import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputData
import DegreeDiameter.Portfolio.OppositeGQ35SpreadIncidence
namespace DegreeDiameter.Portfolio.OppositeGQ35Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
/-- Three supplied incidence indices avoid repeated existential searches.
The checks remain equalities about the original projection point and line. -/
def ProjectionIndexCheck (p : Point) (ix : Line → Fin 4 × Fin 4 × Fin 4) : Prop :=
  ∀ l, fastLinePoint l (ix l).1 = projectionPoint p l ∧
    fastLinePoint (projectionLine p l) (ix l).2.1 = p ∧
    fastLinePoint (projectionLine p l) (ix l).2.2 = projectionPoint p l

theorem inputRow_of_checks (p : Point) (ix : Line → Fin 4 × Fin 4 × Fin 4)
    (h : ProjectionIndexCheck p ix) : InputRow p := by
  refine ⟨?_,pointLine_covers_literal p,spread_unique_literal p⟩
  intro l
  exact ⟨⟨(ix l).1,(linePoint_eq_fast _ _).trans (h l).1⟩,
    ⟨(ix l).2.1,(linePoint_eq_fast _ _).trans (h l).2.1⟩,
    ⟨(ix l).2.2,(linePoint_eq_fast _ _).trans (h l).2.2⟩⟩
end DegreeDiameter.Portfolio.OppositeGQ35Spread
'''
(F/'OppositeGQ35SpreadInputChecks.lean').write_text(s)
for p in range(64):
 indices=[];codes=[]
 for l in range(96):
  q,m=next((q,m) for q in ls[l] for m in through[p] if q in ls[m])
  indices.append((ls[l].index(q),ls[m].index(p),ls[m].index(q)));codes.append(q+64*m)
 s=f'''import DegreeDiameter.Portfolio.OppositeGQ35SpreadInputChecks
namespace DegreeDiameter.Portfolio.OppositeGQ35Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
def projectionIndices{p:02} : Line → Fin 4 × Fin 4 × Fin 4 := !['''+', '.join(f'({a},{b},{c})' for a,b,c in indices)+']\n'
 if 0<p<63:
  s+=f'def localProjectionData{p:02} : Array Nat := #['+', '.join(map(str,codes))+']\n'
  s+=f'theorem projectionData_eq_{p:02} : projectionData {p} = localProjectionData{p:02} := rfl\n'
 selection = f'  simp only [projectionPoint,projectionLine,projectionCode,projectionData_eq_{p:02}]\n' if 0<p<63 else ''
 s+=f'''theorem projection_check_{p:02} : ProjectionIndexCheck {p} projectionIndices{p:02} := by
  unfold ProjectionIndexCheck
{selection}  decide
theorem input_row_{p:02} : InputRow {p} :=
  inputRow_of_checks {p} projectionIndices{p:02} projection_check_{p:02}
end DegreeDiameter.Portfolio.OppositeGQ35Spread
'''
 (F/f'OppositeGQ35SpreadInputRow{p:02}.lean').write_text(s)

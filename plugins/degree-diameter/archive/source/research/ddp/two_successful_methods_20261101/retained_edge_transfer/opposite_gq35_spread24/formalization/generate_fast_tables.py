import json
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent
x=json.loads((D.parent/'PARAMETERS.json').read_text());ls=[r['points'] for r in x['lines']];ps=x['point_incident_lines']
vec=lambda a:'!['+', '.join(map(str,a))+']'
s='''import DegreeDiameter.Portfolio.OppositeGQ35SpreadDefinitions
namespace DegreeDiameter.Portfolio.OppositeGQ35Spread
set_option maxRecDepth 20000
set_option maxHeartbeats 20000000
/-- Alternative evaluation layout only. The two universal equalities below
bind every entry to the original graph's literal table definitions. -/
'''
s+='def fastLinePoint : Line → Fin 4 → Point := !['+', '.join(map(vec,ls))+']\n'
s+='def fastPointLine : Point → Fin 6 → Line := !['+', '.join(map(vec,ps))+']\n'
s+='''theorem linePoint_eq_fast : ∀ l i, linePoint l i = fastLinePoint l i := by decide
theorem pointLine_eq_fast : ∀ p i, pointLine p i = fastPointLine p i := by decide
#print axioms linePoint_eq_fast
#print axioms pointLine_eq_fast
end DegreeDiameter.Portfolio.OppositeGQ35Spread
'''
(R/'formal/DegreeDiameter/Portfolio/OppositeGQ35SpreadFastTables.lean').write_text(s)
p=D/'generate_inputs.py';t=p.read_text().replace('import DegreeDiameter.Portfolio.OppositeGQ35SpreadDefinitions','import DegreeDiameter.Portfolio.OppositeGQ35SpreadFastTables').replace('by unfold InputRow; decide','by\n  unfold InputRow\n  simp only [Inc,linePoint_eq_fast,pointLine_eq_fast]\n  decide')
p.write_text(t)
for f in (R/'formal/DegreeDiameter/Portfolio').glob('OppositeGQ35SpreadInputRow*.lean'):
 t=f.read_text().replace('by unfold InputRow; decide','by\n  unfold InputRow\n  simp only [Inc,linePoint_eq_fast,pointLine_eq_fast]\n  decide');f.write_text(t)
p=R/'formal/DegreeDiameter/Portfolio/OppositeGQ35SpreadInputData.lean';p.write_text(p.read_text().replace('import DegreeDiameter.Portfolio.OppositeGQ35SpreadDefinitions','import DegreeDiameter.Portfolio.OppositeGQ35SpreadFastTables'))

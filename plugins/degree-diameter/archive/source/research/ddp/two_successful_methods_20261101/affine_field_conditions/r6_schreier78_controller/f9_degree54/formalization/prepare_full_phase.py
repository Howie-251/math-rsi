import json,time
from pathlib import Path
R=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math');D=Path(__file__).resolve().parent;Q=R/'formal/DegreeDiameter/Portfolio';ns='F9Graph56862';t=time.process_time()
for c in range(8):
 for b in range(3):
  s=f'''import Mathlib.Logic.Equiv.Fin.Basic
import DegreeDiameter.Portfolio.{ns}RouteData
namespace DegreeDiameter.Portfolio.{ns}
set_option maxRecDepth 30000
set_option maxHeartbeats 100000000
theorem adjacent_chart_{c}_block_{b} : ∀ j : Fin 243,
    let d := (finProdFinEquiv (m:=3) (n:=243)) (({b} : Fin 3),j)
    planeNoise {c} d = decodeVec d := by decide +kernel
#print axioms adjacent_chart_{c}_block_{b}
end DegreeDiameter.Portfolio.{ns}
'''
  (Q/(ns+f'AdjacentChart{c}Block{b}.lean')).write_text(s)
 imports=''.join(f'import DegreeDiameter.Portfolio.{ns}AdjacentChart{c}Block{b}\n' for b in range(3))
 s=imports+f'''namespace DegreeDiameter.Portfolio.{ns}
theorem adjacent_chart_{c} : ∀ d : Fin 729, planeNoise {c} d = decodeVec d := by
  intro d
  obtain ⟨⟨b,j⟩,rfl⟩ := (finProdFinEquiv (m:=3) (n:=243)).surjective d
  fin_cases b
  · exact adjacent_chart_{c}_block_0 j
  · exact adjacent_chart_{c}_block_1 j
  · exact adjacent_chart_{c}_block_2 j
end DegreeDiameter.Portfolio.{ns}
'''
 (Q/(ns+f'AdjacentChart{c}.lean')).write_text(s)
hist=D/'build_history';ps=list(D.glob(ns+'*_RESULT.json'))+list(hist.glob('*_RESULT.json'));cpu=sum(json.loads(p.read_text())['CPU_seconds'] for p in ps)
(D/'PILOT_RESULT.json').write_text(json.dumps(dict(status='PILOT_SUBSTANTIVE_INTERFACE_PASS_RAW_ADJACENT_CHECK_BOUNDED_TIMEOUT',measured_Lean_CPU_all_attempts=cpu,measured_preparation_CPU=0.214918368,total_measured_pilot_CPU=cpu+0.214918368,pilot_CPU_limit=120,single_worker=True,field_graph_matrix_routes_and_linear_closed=True,NB_row00_actual_PASS_CPU=10.614122,raw_chart0_timeout_CPU=12.088509,raw_chart0_limit=10,new_full_phase_chart_blocks=24,full_phase_same_fixed_graph_CPU_limit=1500,expected_full_scope_CPU_range=[1250,1400]),indent=2)+'\n')
(D/'FULL_PHASE_PREPARATION_RESULT.json').write_text(json.dumps(dict(CPU_seconds=time.process_time()-t,chart_blocks=24,each_block_positions=243),indent=2)+'\n')
print('Prepared24 bounded chart blocks; pilot actualCPU',cpu+0.214918368)

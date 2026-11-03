"""One small postprocess of saved672 rows; never constructs Ut or source graph."""
import time
START=time.process_time()
import csv
import itertools
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
PRIOR=1.478501838
PREP=0.05
CAP=0.3
rows=[]
with (HERE/'ALL_T_RESULTS.tsv').open()as f:
    for raw in csv.DictReader(f,delimiter='\t'):
        phase=int(raw['phase']);absolute=list(map(int,raw['phase_counts'].split(',')))
        relative=[absolute[(phase+j)%6]for j in range(6)]
        mask=sum(1<<j for j,v in enumerate(relative)if v==112)
        rows.append(dict(t=int(raw['t']),phase=phase,normal=int(raw['normal']),
                         covered=int(raw['covered']),relative_counts=relative,full_mask=mask))
assert len(rows)==672
subsets=[]
for mask in range(64):
    hits=[r for r in rows if r['full_mask']&mask==mask]
    subsets.append(dict(mask=mask,phases=[j for j in range(6)if mask>>j&1],
                        compatible_t_count=len(hits),first_witness=hits[0]if hits else None))
incompatible=[s for s in subsets if not s['compatible_t_count']]
size=min((len(s['phases'])for s in incompatible),default=None)
minimum=sorted((s for s in incompatible if len(s['phases'])==size),key=lambda s:s['phases'])if size is not None else []
inclusion_minimal=[s for s in incompatible if all(subsets[s['mask']^(1<<j)]['compatible_t_count']>0 for j in s['phases'])]
phase=[]
for j in range(6):
    best=max(r['relative_counts'][j]for r in rows)
    phase.append(dict(relative_phase=j,maximum_saved_count=best,
                      first_max_witness=next(r for r in rows if r['relative_counts'][j]==best),
                      full112_t_count=subsets[1<<j]['compatible_t_count'],
                      first_full_witness=subsets[1<<j]['first_witness']))
chosen=minimum[0]if minimum else None
proper=[]
if chosen:
    for j in chosen['phases']:
        proper.append(subsets[chosen['mask']^(1<<j)])
prediction=all(s['full112_t_count']>0 for s in phase)and size==2
result=dict(status='COMPLETE_SAVED672_PHASE_COMPATIBILITY_DIAGNOSTIC',
    normalization='relativephase=(targetabsolutephase-t.phase)mod6; relative[j]=savedcounts[(t.phase+j)mod6]',
    saved_rows_processed=672,per_phase=phase,
    prediction='all6phasescanindividuallyfill112butaminimallyincompatiblepair exists',
    prediction_supported=prediction,minimum_incompatible_cardinality=size,
    minimum_cardinality_incompatible_subsets=minimum,
    lex_first_minimum_incompatible_subset=chosen,
    chosen_proper_subsets_local_witnesses=proper,
    all_inclusion_minimal_incompatible_subsets=inclusion_minimal,
    all64_subset_compatibilities=subsets,
    prior_case_CPU_seconds=PRIOR,preparation_conservative_charge_CPU_seconds=PREP,
    new_source_Ut_parameter_graph_BFS_validation_solver_runs=0,
    scope='saved672righttranslationmatchingparameters_only;notarbitrarymatching',
    new_graph_parameter_Lean_count=[0,0,0],next='STOP_NO_NEW_T_OR_QUERY')
summary='; '.join(f"phase{p['relative_phase']}: max{p['maximum_saved_count']},fullcases{p['full112_t_count']}"for p in phase)
note=('# Saved672相位兼容性诊断\n\n'
      '只读原ALL_T_RESULTS.tsv的672行，按relative=(targetphase−t.phase)mod6归一；未重算源、U_t、参数或验证。\n\n'
      +summary+'。\n\n'
      +'事前预测'+('SUPPORTED'if prediction else'REFUTED')+'；最小不能同时满的相位数为'+str(size)
      +'，lex首子集为'+str(chosen['phases']if chosen else None)+'。全部最小子集、各相位最大覆盖参数见证和64subset兼容计数保存在JSON。'
      '这些是各相位最大覆盖106的参数见证；实际不存在局部满112的见证，空子集的见证仅为vacuous，不是完整图。全fixedmatching672NO不扩到任意matching。\n\n')
(HERE/'PHASE_COMPATIBILITY_DIAGNOSTIC_NOTE.md').write_text(note)
elapsed=time.process_time()-START
assert PREP+elapsed<CAP,(elapsed,CAP)
result.update(actual_postprocess_CPU_seconds=elapsed,new_charged_CPU_seconds=PREP+elapsed,
              new_CPU_budget_seconds=CAP,cumulative_case_CPU_seconds=PRIOR+PREP+elapsed)
(HERE/'PHASE_COMPATIBILITY_DIAGNOSTIC.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
with (HERE/'PHASE_COMPATIBILITY_DIAGNOSTIC_NOTE.md').open('a')as f:
    f.write(f'实际postprocessCPU={elapsed:.9f}，准备保守charge={PREP}，新增合计{PREP+elapsed:.9f}/{CAP}；沿旧{PRIOR}累计{PRIOR+PREP+elapsed:.9f}CPU秒。完成即停。\n')
print(json.dumps({'status':result['status'],'per_phase_full_counts':[p['full112_t_count']for p in phase],
    'per_phase_max':[p['maximum_saved_count']for p in phase],
    'minimum_incompatible_cardinality':size,'minimum_subsets':[s['phases']for s in minimum],
    'prediction_supported':prediction,'actual_CPU':elapsed,'new_charged_CPU':PREP+elapsed,
    'cumulative_case_CPU':PRIOR+PREP+elapsed},ensure_ascii=False))

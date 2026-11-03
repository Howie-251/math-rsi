"""Projection diagnosis from already-complete saved rows; no controller regeneration."""
import json
from pathlib import Path
p=Path(__file__).resolve().parent
if(p/'PROJECTION_POSTPROCESS.json').exists():raise RuntimeError('projection postprocess already recorded')
a=json.loads((p/'ALL_PARAMETER_RESULTS.json').read_text())
rows=[{'q':x['q'],'r':x['r'],'type0_1_2_reachable':[s['controller_targets_reachable']for s in x['root_summaries']],'one_type_missing':any(s['controller_targets_reachable']<33 for s in x['root_summaries'])}for x in a]
assert len(rows)==100
result={'saved_rows_processed':100,'controller_D3_survivors':sum(not x['one_type_missing']for x in rows),'maximum_of_min_type_reach':max(min(x['type0_1_2_reachable'])for x in rows),'rows':rows,'no_new_controller_words_field_BFS_pointqueries':True}
(p/'PROJECTION_POSTPROCESS.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')

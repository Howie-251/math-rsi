"""Compile, prepare known-zero center exclusions, and run one native enumeration."""
from pathlib import Path
import json
import resource
import subprocess
import time

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
START=time.process_time()
children_start=resource.getrusage(resource.RUSAGE_CHILDREN)
assert json.loads((OUT/'PREDICTION.json').read_text())['frozen_before_native_enumeration']
other=OUT.parent/'h9_other_degrees'
prior=json.loads((other/'degree11_geometry_result.json').read_text())
assert prior['status']=='COMPLETE_FIXED122_CENTER_DEGREE_POOL'
assert prior['nonH_centers']==118 and prior['raw81_lines']==9558
assert prior['degree_feasible_distinct_pinsets']==0
lines=json.loads((other/'degree11_line_witnesses.json').read_text())['records']
centers=sorted({r['center_original_label'] for r in lines if not r['witness']['is_H9_line']})
assert len(centers)==118
(OUT/'known_zero_centers.txt').write_text('\n'.join(map(str,centers))+'\n')
compile_start=resource.getrusage(resource.RUSAGE_CHILDREN)
subprocess.run(['g++','-O3','-std=c++17',str(OUT/'enumerate.cpp'),'-o',str(OUT/'enumerate')],check=True)
compile_end=resource.getrusage(resource.RUSAGE_CHILDREN)
compile_cpu=(compile_end.ru_utime+compile_end.ru_stime)-(compile_start.ru_utime+compile_start.ru_stime)
args=[str(OUT/'enumerate'),
 str(ROOT/'research/ddp/global_coverage_20261027/h9_quadric_line_signature/point_coords.u8.bin'),
 str(other/'point_to_core11.u16.bin'),
 str(ROOT/'research/ddp/breadth_20261027_wave4/pencil_source/deg11_diam5_n37628.txt'),
 str(OUT/'known_zero_centers.txt'),str(OUT),'170']
with (OUT/'native.log').open('w') as log:
 subprocess.run(args,stdout=log,stderr=log,check=True)
d=json.loads((OUT/'native_result.json').read_text())
children_end=resource.getrusage(resource.RUSAGE_CHILDREN)
child_cpu=(children_end.ru_utime+children_end.ru_stime)-(children_start.ru_utime+children_start.ru_stime)
d.update(prediction_id='N11_ALL_UNUSED_Q_LINE_CENTERS',
 prediction_outcome=('SUPPORTED_NONEMPTY_POOL' if d['degree_feasible_distinct_pinsets'] else 'REFUTED_NO_DEGREE_FEASIBLE_FULL_Q_LINE') if d['complete_all66430_center_scope'] else 'UNKNOWN_UNPROCESSED_CENTERS',
 source_n=37628,source_m=205296,target_degree=11,target_D=5,
 mapping_calibration_file='../h9_other_degrees/mapping11_result.json',
 inherited_zero_pool_file='../h9_other_degrees/degree11_geometry_result.json',
 source_mapping='../h9_other_degrees/point_to_core11.u16.bin',
 prior_zero_center_ids=centers,
 original_line_not_doublecounted='Every nonH9 singular line has its unique flatplane center; each center appears once; dual(1,a,b)81 lines each',
 canonical_pinset_deduplication=True,at_least_one_complete10point_witness_per_pool_record=True,
 no_feasibility_inferred_from_firstpoint_only=True,
 compile_CPU_seconds=compile_cpu,total_children_CPU_seconds=child_cpu,
 preparation_CPU_seconds=time.process_time()-START,
 total_CPU_seconds=child_cpu+time.process_time()-START,
 pending=[] if d['complete_all66430_center_scope'] else ['unprocessed centers remain UNKNOWN; no automatic continuation'],
 scope='Fixed current37628 graph and actual4074-split fold. CompleteQ-line mandatory pins only. Degree infeasibility does not exclude changing source, deleting edges/vertices or other attachment mechanisms.')
(OUT/'RESULT.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps(d,indent=2))

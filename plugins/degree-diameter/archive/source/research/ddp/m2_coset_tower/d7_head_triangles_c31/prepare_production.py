from pathlib import Path
import json, resource, subprocess
HERE=Path(__file__).resolve().parent
def cpu():
 a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
 return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu()
assert not (HERE/'production.prepare.json').exists(), 'No repeated preparation/compilation'
scope=json.loads((HERE/'SCOPE.json').read_text())
assert scope['optional_anchor_inversion_representatives']==list(range(16))
assert scope['optional_safe_16_slice_counts_not_used_in_main_scope']['total']==18829360
rows=[json.loads(s) for s in (HERE/'profile.results.jsonl').read_text().splitlines()]
assert len(rows)==1400
with (HERE/'production.calibration.txt').open('w') as f:
 f.write('1400\n')
 for r in rows:f.write(' '.join(map(str,[*r['S'],*r['BB_orbit_masks']]))+'\n')
before=cpu();subprocess.run(['g++','-O3','-std=c++17',str(HERE/'production.cpp'),'-o',str(HERE/'production')],check=True)
compile_cpu=cpu()-before
subprocess.run([str(HERE/'production'),'prepare',str(HERE),'3'],check=True)
actual=json.loads((HERE/'production.iterator_check.json').read_text())
# Match actual C++ iterator pools against the independent scope records, in the real production order.
allocations=[(1,0,4),(1,1,2),(1,2,0),(2,0,2),(2,1,0)]
meta=[];offset=0
for b,(t,np,ni) in enumerate(allocations):
 expected=next(s for s in scope['branches'] if (s['t'],s['internal_pairs'],s['internal_involutions'])==(t,np,ni))
 count=expected['HH_internal_choices']*16*(1 if t==1 else 929)
 assert actual['actual_branch_internal_counts'][b]==expected['HH_internal_choices']
 assert actual['actual_branch_input_counts'][b]==count
 meta.append({'branch':b,'t':t,'internal_pairs':np,'internal_involutions':ni,
  'internal_sets':expected['HH_internal_choices'],'parent_30_anchor_inputs':expected['normalized_marked_inputs'],
  'safe_16_anchor_inputs':count,'cursor_start':offset,'cursor_end':offset+count})
 offset+=count
assert offset==actual['actual_scope']==18829360
metadata={'scope_proof':'SCOPE.md sections1-6','parent_marked_inputs':35305050,
 'safe_16_anchor_inputs':18829360,'anchor_indices':list(range(16)),
 'fixed_anchor_indices_fully_retained':[0,15],'not_uniform_halving':True,
 'safe_map':'T_j=F_(-3^j) composed with C3 inversion; marked anchor j maps to -j',
 't2_multiple_markings_retained':True,'all_HH_legal_generator_sets_preserved':True,
 'order':'branch, actual internal set index, anchor j0..15, second w1 representative ci0..929 skipping ci=31*j+1; t1 has no second representative',
 'second_cross_encoding':'ci%31+31+93*(ci//31)','branches':meta,
 'actual_iterator_matches_independent_scope_counts':True,'all_inputs_HH_legal':True,
 'profile_is_not_production_prefix':True,'production_start_cursor':0,
 'profile_score_cache_used':False,'saved_1400_BB_masks_calibrated_without_new_graph_or_BFS':True,
 'selection':'exact BB filter then actual three-root BFS for every BB survivor',
 'root_statistics_population':'BB survivors only, distinct from all HH legal inputs',
 'stop_on_D5':True,'CPU_budget_cumulative':360,'prior_shared_profile_CPU_seconds':2.805399,
 'independent_final_CPU_accounted_separately':True,'worker_count':1}
(HERE/'production.metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
out={'status':'READY','preparation_compile_calibration_CPU_seconds':cpu()-start,
 'compile_CPU_seconds':compile_cpu,'actual_scope':offset,'no_new_graph_or_BFS':True,
 'saved_BB_calibration_count':1400,'branch_counts':actual['actual_branch_input_counts']}
(HERE/'production.prepare.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

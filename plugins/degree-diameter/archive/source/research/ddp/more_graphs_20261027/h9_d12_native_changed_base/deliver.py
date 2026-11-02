"""Reuse the literal-family appender with this source/schema; no new validation."""
allpool=load(BASE/'h9_global_line_pool_d12/pool.json')['records']
text=(BASE/'h9_d12_changed_base_round2/deliver.py').read_text()
text=text.replace("family['strongest_n']==initial_n==42391 and len(old_steps)==49",
                  "family['strongest_n']==initial_n==42396 and len(old_steps)==54")
text=text.replace("parameters['distinct_explicit_examples']==52","parameters['distinct_explicit_examples']==57")
text=text.replace("family['steps'][:49]","family['steps'][:54]")
text=text.replace('old52','old57').replace('旧52','旧57')
text=text.replace('h9_d12_changed_base_round2','h9_d12_native_changed_base')
text=text.replace('42391','42396')
# The native producer already wrote every accepted complete graph for the next prepare call.
a=text.index('graphdir=OUT/');b=text.index('delivery=OUT.parent/',a)
text=text[:a]+"finalpath=current_file\n"+text[b:]
before=resource.getrusage(resource.RUSAGE_CHILDREN)
before_cpu=before.ru_utime+before.ru_stime
exec(compile(text,str(OUT/'literal_family_appender.py'),'exec'))
after=resource.getrusage(resource.RUSAGE_CHILDREN)
result.update(CPU_total_including_all_native_and_generator_seconds=cpu(),
 generator_child_CPU_seconds=after.ru_utime+after.ru_stime-before_cpu,
 actual_native_prepare_and_verify_CPU_seconds=before_cpu-initial_child.ru_utime-initial_child.ru_stime,
 Python_reverse_target_BFS=0,MIP_calls=0,allsource_BFS=0,externalreview=0,pending=[])
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print('TOTAL_CPU '+str(result['CPU_total_including_all_native_and_generator_seconds']),flush=True)

"""Runs after the finite producer, reusing its accepted sequence and currentadj."""
import copy
import subprocess
from collections import Counter

for k,r in enumerate(accepted,1):
 r['status']='ACCEPTED_ACTUAL_DEGREE_COMPLETE_R4'
 (OUT/f"accepted_{k:02d}_pool{r['pool_index']}.json").write_text(json.dumps(r,indent=2)+'\n')
sequence=OUT/'accepted_extensions.json'
seq=json.loads(sequence.read_text())
seq.update(records=accepted,root_final_independent_acceptance_pending=False,
           verification_basis='User-authorized production actualdegree and completecurrentR4; no repeated allsourceBFS requested')
sequence.write_text(json.dumps(seq,indent=2)+'\n')

graphdir=OUT/'graphs';graphdir.mkdir(exist_ok=True)
finalpath=graphdir/f'graph_d12_D5_n{len(adj)}.edges'
with finalpath.open('w') as stream:
 stream.write(f'{len(adj)} {current_m}\n')
 for u,neighbors in enumerate(adj):
  for v in sorted(neighbors):
   if u<v:stream.write(f'{u} {v}\n')

delivery=OUT.parent/'delivery'
parameter_file=delivery/'families.json'
parameters=json.loads(parameter_file.read_text())
old_steps=copy.deepcopy(parameters['families']['12']['steps'])
old11=copy.deepcopy(parameters['families']['11'])
family=parameters['families']['12']
assert family['strongest_n']==initial_n==42377
assert len(old_steps)==35 and parameters['distinct_explicit_examples']==38
for r in accepted:
 assert family['steps'][-1]['new_n']==r['source_n']
 family['steps'].append(dict(step=len(family['steps'])+1,source_n=r['source_n'],source_m=r['source_m'],
  source=f"degree12 family prefix on labels0..{r['source_n']-1}, retaining all previous edges",
  new_vertex=r['new_vertex'],pins=r['full_neighbor_set'],mandatory_pins=r['mandatory_pins'],anchors=r['anchors'],
  old_pin_degrees=r['neighbors_old_degrees'],new_vertex_degree=r['new_vertex_degree'],new_n=r['new_n'],new_m=r['new_m'],
  complete_currentbase_R4_certificate=True,actual_current_R4_covered=r['actual_current_R4_covered'],
  actual_current_R4_missing=0,
  source_evidence='research/ddp/more_graphs_20261027/h9_d12_global_remainder/accepted_extensions.json:records',
  geometric_witnesses=allpool[r['pool_index']]['geometric_witnesses'],
  verification_scope='Actual insertion degree and one full-neighbor completeR4 production check; no repeated all-sourceBFS or externalreview'))
assert family['steps'][:35]==old_steps and parameters['families']['11']==old11
family.update(example_orders=list(range(42343,len(adj)+1)),example_count=len(family['steps']),strongest_n=len(adj),strongest_m=current_m,
 edge_count_formula='245217 + sum(new_vertex_degree for all applied literalsteps)',
 strongest_complete_verification=dict(kind='actual per-step degree and completeR4 from independently verified42377',
   n=len(adj),m=current_m,max_degree=12,diameter_exact=5,allsource_BFS_after42377=0),
 last_independent_allsource_order=42377)
parameters['distinct_explicit_examples']=len(family['steps'])+parameters['families']['11']['example_count']
parameters['mathematical_strongest_bounds']['N(12,5)']=len(adj)
parameters['latest_mainfamily_extension']=dict(source_n=42377,new_examples=len(accepted),final_n=len(adj),
 method='productiondegree+actualfullR4; no repeated allsourceBFS',source_file=str(finalpath.relative_to(ROOT)),
 old38_literal_steps_preserved=True,independent8pin_branch_merged=False)
parameter_file.write_text(json.dumps(parameters,indent=2)+'\n')

# Preserve the oldREADME as text, with a current-status notice which supersedes its snapshot table.
readme=delivery/'README.md';oldreadme=readme.read_text()
notice=f'''# 当前主family更新：{parameters['distinct_explicit_examples']}例、两组参数

旧38例的literal步骤保持不变；degree12现可生成42343至{len(adj)}的全部{len(family['steps'])}个整数前缀，degree11仍为37629至37631共3例。最强数学下界为N(12,5)≥{len(adj)}、N(11,5)≥37631。

本轮从已独立验收42377起接受{len(accepted)}个完整新点，每步只做必要的实际degree与完整currentR4生产检查；没有再跑全源BFS或外审。42377仍是degree12最新全源BFS阶数，后续前缀由完整逐步覆盖归纳保证。完整Lean图实例仍为0。独立8-pin分支未混入本family。

最新例子：`python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 12 --order {len(adj)} --output /tmp/graph_d12_D5_n{len(adj)}.edges`。

新增字面参数已接入families.json，最强完整边表在`../h9_d12_global_remainder/graphs/graph_d12_D5_n{len(adj)}.edges`。一次生成器edge-set dry-run结果在`../h9_d12_global_remainder/generator_dry_run.json`。下面保留旧38例交付快照，表中“最强”以本段为准。

---

'''
readme.write_text(notice+oldreadme)
command=['python',str(delivery/'family_generator.py'),'--degree','12','--order',str(len(adj)),
         '--dry-run','--compare',str(finalpath)]
with (OUT/'generator_dry_run.json').open('w') as stream:
 subprocess.run(command,stdout=stream,check=True)
check=json.loads((OUT/'generator_dry_run.json').read_text())
assert check['comparison']['edge_set_matches'] and not check['graph_written'] and not check['BFS_performed']
result.update(final_graph_generated_by_producer=True,final_graph=str(finalpath.relative_to(ROOT)),
 row_status_counts=dict(Counter(r['status'] for r in rows)),
 production_complete_current_R4_checks=len(accepted),
 delivery_total_examples=parameters['distinct_explicit_examples'],delivery_old38_steps_preserved=True,
 independent8pin_branch_merged=False,generator_dry_run='generator_dry_run.json',
 allsource_BFS_after42377=0,new_external_review=0,
 whole_process_CPU_seconds=time.process_time()-START,
 generator_child_CPU_seconds=__import__('resource').getrusage(__import__('resource').RUSAGE_CHILDREN).ru_utime+
   __import__('resource').getrusage(__import__('resource').RUSAGE_CHILDREN).ru_stime)
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print('DELIVERED '+json.dumps(dict(final_n=len(adj),final_m=current_m,accepted=len(accepted),
 total_examples=parameters['distinct_explicit_examples'],old38_preserved=True,graph=str(finalpath),
 CPU_seconds=result['whole_process_CPU_seconds'],generator_child_CPU_seconds=result['generator_child_CPU_seconds'])),flush=True)

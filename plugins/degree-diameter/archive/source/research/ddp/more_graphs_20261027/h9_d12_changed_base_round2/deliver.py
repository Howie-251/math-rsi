"""Append only new literal mainfamily steps; no graphwide revalidation."""
import copy
import subprocess
from collections import Counter
import resource

for k,r in enumerate(accepted,1):
 r['status']='ACCEPTED_ACTUAL_DEGREE_COMPLETE_R4'
 (OUT/f"accepted_{k:02d}_pool{r['pool_index']}.json").write_text(json.dumps(r,indent=2)+'\n')
seqfile=OUT/'accepted_extensions.json'
seq=json.loads(seqfile.read_text())
seq.update(records=accepted,root_final_independent_acceptance_pending=False,
           verification_basis='User-authorized actualdegree and completecurrentR4; no newallsourceBFS or externalreview')
seqfile.write_text(json.dumps(seq,indent=2)+'\n')
graphdir=OUT/'graphs';graphdir.mkdir(exist_ok=True)
finalpath=graphdir/f'graph_d12_D5_n{len(adj)}.edges'
with finalpath.open('w') as stream:
 stream.write(f'{len(adj)} {current_m}\n')
 for u,neighbors in enumerate(adj):
  for v in sorted(neighbors):
   if u<v:stream.write(f'{u} {v}\n')
delivery=OUT.parent/'delivery';path=delivery/'families.json'
parameters=json.loads(path.read_text());family=parameters['families']['12']
old_steps=copy.deepcopy(family['steps']);old11=copy.deepcopy(parameters['families']['11'])
assert family['strongest_n']==initial_n==42391 and len(old_steps)==49
assert parameters['distinct_explicit_examples']==52
for r in accepted:
 assert family['steps'][-1]['new_n']==r['source_n']
 family['steps'].append(dict(step=len(family['steps'])+1,source_n=r['source_n'],source_m=r['source_m'],
  source=f"degree12 family prefix on labels0..{r['source_n']-1}, retaining all previous edges",
  new_vertex=r['new_vertex'],pins=r['full_neighbor_set'],mandatory_pins=r['mandatory_pins'],anchors=r['anchors'],
  old_pin_degrees=r['neighbors_old_degrees'],new_vertex_degree=r['new_vertex_degree'],new_n=r['new_n'],new_m=r['new_m'],
  complete_currentbase_R4_certificate=True,actual_current_R4_covered=r['actual_current_R4_covered'],
  actual_current_R4_missing=0,prior_accepted_line_vertices=r['prior_accepted_line_vertices'],
  multiple_vertices_on_same_line=r['multiple_line_vertex'],previous_evaluation=r['last_evaluation'],
  source_evidence='research/ddp/more_graphs_20261027/h9_d12_changed_base_round2/accepted_extensions.json:records',
  geometric_witnesses=allpool[r['pool_index']]['geometric_witnesses'],
  verification_scope='Actual insertion degree and one completefull-neighborR4 production check; no repeatedallsourceBFS or externalreview'))
assert family['steps'][:49]==old_steps and parameters['families']['11']==old11
family.update(example_orders=list(range(42343,len(adj)+1)),example_count=len(family['steps']),
 strongest_n=len(adj),strongest_m=current_m,
 edge_count_formula='245217 + sum(new_vertex_degree for all applied literalsteps)',
 strongest_complete_verification=dict(kind='Actual per-stepdegree and completeR4 from previously certified42391',
   n=len(adj),m=current_m,max_degree=12,diameter_exact=5,allsource_BFS_after42377=0),
 last_independent_allsource_order=42377)
parameters['distinct_explicit_examples']=len(family['steps'])+parameters['families']['11']['example_count']
parameters['package']=f"All{parameters['distinct_explicit_examples']} explicit H9 Q-line+anchor extension examples"
parameters['mathematical_strongest_bounds']['N(12,5)']=len(adj)
parameters['latest_mainfamily_extension']=dict(source_n=42391,new_examples=len(accepted),final_n=len(adj),
 method='productiondegree+actualcompleteR4; no repeatedallsourceBFS',source_file=str(finalpath.relative_to(ROOT)),
 old52_literal_steps_preserved=True,independent8pin_branch_merged=False)
path.write_text(json.dumps(parameters,indent=2)+'\n')
readme=delivery/'README.md';previous=readme.read_text()
notice=f'''# 当前主family：{parameters['distinct_explicit_examples']}例，N(12,5)≥{len(adj)}

本轮从数学已接受42391起新增{len(accepted)}个完整前缀；degree12现覆盖42343..{len(adj)}共{len(family['steps'])}例，degree11仍37629..37631共3例。原52例literal步骤保持原样。每个新点只做必要的实际degree和完整currentR4生产检查，没有新全源BFS或外审；最新全源仍42377，后续由逐步完整覆盖归纳保证。完整Lean实例仍0，非最优值声明。

生成最新例子：`python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 12 --order {len(adj)} --output /tmp/graph_d12_D5_n{len(adj)}.edges`。完整边表在`../h9_d12_changed_base_round2/graphs/graph_d12_D5_n{len(adj)}.edges`，一次生成器edge-set对照记录在该目录generator_dry_run.json。

此次只重试上次评估base早于42391且当前degree合法的冻结列表；same-base失败跳过，不回头旧失败。允许真实degree承载的多重line顶点并逐项标识，未混入独立8pin分支。下方保留先前交付记录；当前例子数与最强值以本段为准。

---

'''
readme.write_text(notice+previous)
with (OUT/'generator_dry_run.json').open('w') as stream:
 subprocess.run(['python',str(delivery/'family_generator.py'),'--degree','12','--order',str(len(adj)),
                 '--dry-run','--compare',str(finalpath)],stdout=stream,check=True)
check=json.loads((OUT/'generator_dry_run.json').read_text())
assert check['comparison']['edge_set_matches'] and not check['graph_written'] and not check['BFS_performed']
result.update(final_graph_generated_by_producer=True,final_graph=str(finalpath.relative_to(ROOT)),
 row_status_counts=dict(Counter(r['status'] for r in rows)),
 production_complete_current_R4_checks=len(accepted),delivery_total_examples=parameters['distinct_explicit_examples'],
 delivery_old52_steps_preserved=True,independent8pin_branch_merged=False,
 last_independent_allsource_order=42377,new_allsource_or_external_review_requested=False,
 accepted_multiple_line_vertices=sum(r['multiple_line_vertex'] for r in accepted),
 generator_dry_run='generator_dry_run.json',whole_process_CPU_seconds=time.process_time()-START,
 generator_child_CPU_seconds=resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime+
                           resource.getrusage(resource.RUSAGE_CHILDREN).ru_stime,pending=[])
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print('DELIVERED '+json.dumps(dict(final_n=len(adj),final_m=current_m,accepted=len(accepted),
 total_examples=parameters['distinct_explicit_examples'],old52_preserved=True,
 CPU_seconds=result['whole_process_CPU_seconds'],generator_child_CPU_seconds=result['generator_child_CPU_seconds'])),flush=True)

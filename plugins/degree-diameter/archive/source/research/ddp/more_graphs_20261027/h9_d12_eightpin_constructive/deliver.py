"""Append the root-produced4 literal8pin+4anchor steps; no new search or BFS."""
import copy
import json
from pathlib import Path
import subprocess

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
data=json.loads((OUT/'RESULT.json').read_text())
records=data['records']
assert len(records)==4 and (data['initial_n'],data['final_n'],data['final_m'])==(42392,42396,245865)
delivery=OUT.parent/'delivery';path=delivery/'families.json'
parameters=json.loads(path.read_text());family=parameters['families']['12']
oldsteps=copy.deepcopy(family['steps']);old11=copy.deepcopy(parameters['families']['11'])
assert parameters['distinct_explicit_examples']==53 and family['strongest_n']==42392 and len(oldsteps)==50
pool=json.loads((OUT.parent/'h9_global_line_pool_d12/pool.json').read_text())['records']
m=245817
for r in records:
 assert family['steps'][-1]['new_n']==r['source_n']==r['new_vertex']
 assert r['source_m']==m and r['missing_count']==0 and r['covered_count']==r['source_n']
 pins=r['full_neighbor_set'];assert pins==sorted(set(pins)) and len(pins)==12
 assert sorted(r['mandatory_pins']+r['anchors'])==pins and max(r['old_degrees'])<12
 m+=len(pins)
 family['steps'].append(dict(step=len(family['steps'])+1,source_n=r['source_n'],source_m=r['source_m'],
  source=f"degree12 family prefix on labels0..{r['source_n']-1}, retaining all previous edges",
  new_vertex=r['new_vertex'],pins=pins,mandatory_pins=r['mandatory_pins'],anchors=r['anchors'],
  old_pin_degrees=r['old_degrees'],new_vertex_degree=len(pins),new_n=r['new_n'],new_m=m,
  complete_currentbase_R4_certificate=True,actual_current_R4_covered=r['covered_count'],actual_current_R4_missing=0,
  source_evidence='research/ddp/more_graphs_20261027/h9_d12_eightpin_constructive/RESULT.json:records',
  geometric_witnesses=pool[r['pool_index']]['geometric_witnesses'],
  anchor_selection='Bounded32x16greedy-prefix plus exacttwo-anchor-tail; acceptance by actual completecurrentR4',
  verification_scope='Production actualdegree and completeR4; no newall-sourceBFS or externalreview'))
assert m==245865 and family['steps'][:50]==oldsteps and parameters['families']['11']==old11
family.update(example_orders=list(range(42343,42397)),example_count=54,strongest_n=42396,strongest_m=245865,
 edge_count_formula='245217 + sum(new_vertex_degree for all applied literalsteps)',
 strongest_complete_verification=dict(kind='Actual per-stepdegree and completeR4',n=42396,m=245865,
                                     max_degree=12,diameter_exact=5,newallsourceBFS=0),
 last_independent_allsource_order=42377)
parameters.update(distinct_explicit_examples=57,package='All57 explicit H9 Q-line+anchor extension examples')
parameters['mathematical_strongest_bounds']['N(12,5)']=42396
parameters['proof_schema']='Retain every oldedge. Each accepted literal neighbor set has actualcurrentdegree within cap and completeR4 cover of its actualoldbase; oldold distances do not increase and newold distances are at most5. All listed prefixes exceed the degree-specificD4Moore upper bound, soD is exactly5. Full all-sourceBFS is not claimed for every prefix.'
parameters['latest_mainfamily_extension']=dict(source_n=42392,new_examples=4,final_n=42396,
 source_file=data['final_graph'],old53_literal_steps_preserved=True,
 method='EightmandatoryQ-linepins plus fouranchors, actualdegree and completecurrentR4 production acceptance',
 new_allsource_BFS=0,new_external_review=0)
path.write_text(json.dumps(parameters,indent=2)+'\n')
readme=delivery/'README.md';previous=readme.read_text()
notice='''# 当前交付：57例，N(12,5)≥42396

主family现为degree12的42343..42396全部54个完整前缀，加degree11的37629..37631共3例，总57例、两组参数。旧53例literal步骤逐项保持，新增4步来自8pin Q-line＋4anchors构造，每步actualcurrent degree与完整R4通过；没有新全源BFS或外审。degree12最新全源阶数仍42377，之后由完整逐步覆盖归纳保证。完整Lean实例仍0，不主张最优值或57种独立方法。

生成最新图：`python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 12 --order 42396 --output /tmp/graph_d12_D5_n42396.edges`。root生产边表在`../h9_d12_eightpin_constructive/graphs/graph_d12_D5_n42396.edges`；一次生成器edge-set对照记录在同目录`generator_dry_run.json`。

下方保留历史交付快照，当前例子数、范围与最强值以本段和families.json为准。

---

'''
readme.write_text(notice+previous)
graph=ROOT/data['final_graph']
with (OUT/'generator_dry_run.json').open('w') as stream:
 subprocess.run(['python',str(delivery/'family_generator.py'),'--degree','12','--order','42396',
                 '--dry-run','--compare',str(graph)],stdout=stream,check=True)
check=json.loads((OUT/'generator_dry_run.json').read_text())
assert check['comparison']['edge_set_matches'] and not check['graph_written'] and not check['BFS_performed']
(OUT/'delivery_update.json').write_text(json.dumps(dict(total_examples=57,degree12_examples=54,
 strongest_n=42396,strongest_m=245865,old53_literal_steps_preserved=True,newliteral_steps=4,
 generator_dry_run='generator_dry_run.json',BFS_performed=False,old_graphs_written=False),indent=2)+'\n')
print('Delivered57examples; old53literals preserved; n42396/m245865 edge-set MATCH; no BFS.')

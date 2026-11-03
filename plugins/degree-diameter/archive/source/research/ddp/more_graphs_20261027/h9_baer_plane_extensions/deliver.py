"""Parentaccepted Baer13 firsthit: one literalappend and one generator comparison."""
from pathlib import Path
import copy,json,subprocess,time,resource

OUT=Path(__file__).resolve().parent;BASE=OUT.parent;ROOT=OUT.parents[3]
load=lambda p:json.loads(p.read_text())
result=load(OUT/'RESULT.json');assert result['accepted_extensions']==1 and result['final_n']==42398
r=result['records'][0];assert r['pool_index']==173 and r['source_n']==42397 and r['anchors']==[41666]
assert len(r['mandatory_pins'])==11 and r['raw_point_count']==13 and r['actual_current_R4_missing']==0
parent_file=OUT/'independent_first_new_root.json';parent=load(parent_file)
parameters=load(BASE/'delivery/families.json');family=parameters['families']['12']
oldsteps=copy.deepcopy(family['steps']);old11=copy.deepcopy(parameters['families']['11'])
assert parameters['distinct_explicit_examples']==58 and family['strongest_n']==42397 and len(oldsteps)==55
family['steps'].append(dict(step=56,source_n=r['source_n'],source_m=r['source_m'],
 source='Previously accepted42397mainfamily with retainedoldedges and completeR4 induction',
 new_vertex=r['new_vertex'],pins=r['full_neighbor_set'],mandatory_pins=r['mandatory_pins'],anchors=r['anchors'],
 old_pin_degrees=r['neighbors_old_degrees'],new_vertex_degree=r['new_vertex_degree'],new_n=r['new_n'],new_m=r['new_m'],
 neighbor_type='Baer PG2(F3) folded blocking set',raw_point_count=13,folded_mandatory_pin_count=11,
 Baer_witness=r['Baer_witness'],Baer_witness_multiplicity=r['witness_multiplicity'],
 complete_currentbase_R4_certificate=True,actual_current_R4_covered=r['actual_current_R4_covered'],actual_current_R4_missing=0,
 source_evidence='research/ddp/more_graphs_20261027/h9_baer_plane_extensions/first_hit.json',
 native_R4_evidence=r['native_selected_R4_file'],
 first_newmechanism_independent_newroot_check='research/ddp/more_graphs_20261027/h9_baer_plane_extensions/independent_first_new_root.json',
 uniform_core_rule_source='research/ddp/more_graphs_20261027/h9_baer_plane_pool/THEOREM.md',
 genericproof_source='ActualcompletecurrentR4, actualdegree and retainedoldedges; not an assertion that this is a completeQline',
 parent_pending=False,accepted_by_parent=True,
 verification_scope='Productionactualdegree+selectedfullR4 and one parentindependentnewroot from expandededgefile. No oldroot/allsourceBFS repeated.'))
assert family['steps'][:55]==oldsteps and parameters['families']['11']==old11
proof='Retain all prior edges. Each literal fullneighbor set is accepted by actualcurrentdegree and actualclosedR4 covering every oldvertex. The neighbor rule may be a fullQline, a pin-deletion subset plusanchors, or a folded13pointBaer PG2(F3)blocking set plusanchors; do not equate these rules or infer subsetcoverage without actualR4. By SingleExtension induction oldold distances do not increase and newold are at most5. Orders exceed their degree-specificD4Moore upper bound, so exactD5. Last independentallsource order remains42377; parentchecked only the firstBaer newroot separately.'
family.update(example_orders=list(range(42343,42399)),example_count=56,strongest_n=42398,strongest_m=245889,
 edge_count_formula="245217 + sum(len(step['pins']) for step in applied_prefix)",proof_scope=proof,
 strongest_complete_verification=dict(kind='Actualdegree/currentR4 induction plus firstBaer independentnewroot',n=42398,m=245889,
   max_degree=12,diameter_exact=5,new_allsource_BFS=0,newroot_check_file=str(parent_file.relative_to(ROOT))),
 last_independent_allsource_order=42377)
parameters.update(package='All59 explicit H9 neighborhood+anchor extension examples',distinct_explicit_examples=59,proof_schema=proof,
 reviewed_example_count=38,Lean_complete_graph_instances=0)
parameters['mathematical_strongest_bounds']['N(12,5)']=42398
parameters['latest_mainfamily_extension']=dict(source_n=42397,new_examples=1,final_n=42398,source_file=result['final_graph'],
 old58_literal_steps_preserved=True,neighbor_type='Baer PG2(F3) folded blocking set',raw_point_count=13,folded_mandatory_pins=11,
 anchors=[41666],parent_first_newroot_accepted=True,new_allsource_BFS=0,last_allsource_retained=42377,reviewed_examples_retained=38,
 Lean_complete_graph_instances=0)
(BASE/'delivery/families.json').write_text(json.dumps(parameters,indent=2)+'\n')
readme=BASE/'delivery/README.md';old=readme.read_text()
readme.write_text('''# 当前交付：59例，N(12,5)≥42398

D12现在42343..42398共56例，D11仍3例。旧58literal保持。本次新邻域明确为 **Baer PG2(F3) folded blocking set**：13个原始点折叠成11个pins，再加anchor41666；不是完整Qline。rank-nullity给统一旧core覆盖，实际degree和完整currentR4负责包括旧extras在内的整个基图。

root只对首Baer新点做了一次独立newroot核验（从完整边表重建，最远5、0bad）；没有重复旧/allsourceBFS，最新全源仍42377，reviewed38、完整Lean0不变。完整literal及原13点坐标witness在families.json；旧Qline与删pin规则保留，通用正确性一律用actualR4＋保留旧边归纳。

最新生成命令：`python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 12 --order 42398 --output /tmp/graph_d12_D5_n42398.edges`。完整图在`../h9_baer_plane_extensions/graphs/graph_d12_D5_n42398.edges`，新机制新根结果和一次生成器edge-set对照在同目录。当前范围仅364个F3-center平面的有限Baer池，不主张其它centers的搜索结论。

下方保留历史交付记录，当前数字以本段和families.json为准。

---

'''+old)
with (OUT/'generator_dry_run.json').open('w') as f:
 subprocess.run(['python',str(BASE/'delivery/family_generator.py'),'--degree','12','--order','42398','--dry-run','--compare',str(ROOT/result['final_graph'])],stdout=f,check=True)
check=load(OUT/'generator_dry_run.json');assert check['comparison']['edge_set_matches'] and not check['BFS_performed'] and not check['graph_written']
result.update(parent_first_newroot_accepted=True,parent_first_newroot_check=str(parent_file.relative_to(ROOT)),
 delivery_modified=True,delivery_total_examples=59,old58_literal_steps_preserved=True,generator_dry_run='generator_dry_run.json',
 pending=[],neighbor_type='Baer PG2(F3) folded blocking set')
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
sequence=load(OUT/'accepted_extensions.json');sequence.update(delivery_waits_for_root_first_newmechanism_acceptance=False,
 parent_first_newroot_accepted=True,pending=[]);(OUT/'accepted_extensions.json').write_text(json.dumps(sequence,indent=2)+'\n')
(OUT/'delivery_update.json').write_text(json.dumps(dict(total_examples=59,degree12_examples=56,strongest_n=42398,strongest_m=245889,
 old58_literal_steps_preserved=True,new_neighbor_type='Baer PG2(F3) folded blocking set',raw13_folded11_anchor41666=True,
 parent_first_newroot_accepted=True,one_generator_edge_set_comparison=True,newallsource_BFS=0,reviewed38=True,Lean_complete0=True),indent=2)+'\n')
print('Delivered59, old58preserved, Baer13folded11+anchor41666; generator edge-set MATCH; no newBFS.')

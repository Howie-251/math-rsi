import copy
from collections import Counter
path=BASE/'delivery/families.json';parameters=load(path);family=parameters['families']['12']
oldsteps=copy.deepcopy(family['steps']);old11=copy.deepcopy(parameters['families']['11'])
assert family['strongest_n']==42397 and len(oldsteps)==55 and parameters['distinct_explicit_examples']==58
pool=load(BASE/'h9_global_line_pool_d12/pool.json')['records']
for r in accepted:
 assert family['steps'][-1]['new_n']==r['source_n']
 family['steps'].append(dict(step=len(family['steps'])+1,source_n=r['source_n'],source_m=r['source_m'],
  source='Previously accepted current mainfamily prefix with completeR4 induction',new_vertex=r['new_vertex'],
  pins=r['full_neighbor_set'],mandatory_pins=r['mandatory_pins'],deleted_saturated_pin=r['deleted_saturated_pin'],anchors=r['anchors'],
  old_pin_degrees=r['neighbors_old_degrees'],new_vertex_degree=r['new_vertex_degree'],new_n=r['new_n'],new_m=r['new_m'],
  complete_currentbase_R4_certificate=True,actual_current_R4_covered=r['actual_current_R4_covered'],actual_current_R4_missing=0,
  source_evidence='research/ddp/more_graphs_20261027/h9_d12_ninepin_coreguard/accepted_extensions.json:records',
  native_R4_evidence=r['native_verify_file'],geometric_witnesses=pool[r['pool_index']]['geometric_witnesses'],
  anchor_selection='Oneeligiblecoreguard plus exactatmosttwo extra-complement anchors, peritem bounded; actualdegree+fullR4 accepted',
  mandatory_pin_scope='Nine-point subset; no geometric wholecore coverage is inferred without actualfullR4',parent_pending=False))
assert family['steps'][:55]==oldsteps and parameters['families']['11']==old11
family.update(example_orders=list(range(42343,len(adj)+1)),example_count=len(family['steps']),strongest_n=len(adj),strongest_m=current_m,
 edge_count_formula="245217 + sum(len(step['pins']) for step in applied_prefix)",
 strongest_complete_verification=dict(kind='productionactualdegree and completecurrentR4',n=len(adj),m=current_m,max_degree=12,diameter_exact=5,newallsourceBFS=0),last_independent_allsource_order=42377)
parameters['distinct_explicit_examples']=len(family['steps'])+parameters['families']['11']['example_count']
parameters['package']=f"All{parameters['distinct_explicit_examples']} explicit H9 neighborhood+anchor extension examples"
parameters['mathematical_strongest_bounds']['N(12,5)']=len(adj)
parameters['latest_mainfamily_extension']=dict(source_n=42397,new_examples=len(accepted),final_n=len(adj),source_file=str(current_file.relative_to(ROOT)),old58_literal_steps_preserved=True,method='Coreguard-first9pin+atmost3anchors',newallsourceBFS=0,newexternalreview=0)
path.write_text(json.dumps(parameters,indent=2)+'\n')
readme=BASE/'delivery/README.md';oldreadme=readme.read_text()
readme.write_text(f"# 当前主family：{parameters['distinct_explicit_examples']}例，N(12,5)≥{len(adj)}\n\n本轮coreguard-first新增{len(accepted)}个完整前缀；D12为42343..{len(adj)}共{len(family['steps'])}例，D11仍3例。旧58literal保持。每步实际degree和一次完整currentR4生产接受，无新全源/外审；最新全源仍42377，Lean完整实例0。九pin子集不继承几何全core覆盖，接受依据完整实际R4。\n\n最新边表`../h9_d12_ninepin_coreguard/graphs/graph_d12_D5_n{len(adj)}.edges`。原生成器可用`--degree 12 --order {len(adj)}`；下方为历史说明，当前数以本段为准。\n\n---\n\n"+oldreadme)
with (OUT/'generator_dry_run.json').open('w') as f:
 subprocess.run(['python',str(BASE/'delivery/family_generator.py'),'--degree','12','--order',str(len(adj)),'--dry-run','--compare',str(current_file)],stdout=f,check=True)
check=load(OUT/'generator_dry_run.json');assert check['comparison']['edge_set_matches'] and not check['BFS_performed'] and not check['graph_written']
result.update(delivery_total_examples=parameters['distinct_explicit_examples'],old58_literal_steps_preserved=True,
 generator_dry_run='generator_dry_run.json',total_parent_plus_children_CPU_seconds=cpu(),
 row_status_counts=dict(Counter(r['status'] for r in rows)),pending=[])
(OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print('DELIVERED '+json.dumps(dict(n=len(adj),m=current_m,total_examples=parameters['distinct_explicit_examples'],CPU_total=cpu())),flush=True)

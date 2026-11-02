from pathlib import Path
from datetime import datetime,timezone
import copy,json,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';B='GRAPH_CATALOG_NAVIGATION_ONLY_20261101';now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
paths=['research/graph_catalog.html','research/graph_catalog.html.txt','research/graph_catalog.csv'];assert all((R/p).is_file()for p in paths)
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());keys=['record_count','validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances'];assert tuple(L[k]for k in keys)==(420,152,43,45)
ident='ddp-d15-d4-current15552-source-gap-20261027';row=copy.deepcopy(next(x for x in L['rows']if x['id']==ident)['source_record'])
node_nav='用户总图清单入口：[HTML清单](../../research/graph_catalog.html) · [HTML原样源码](../../research/graph_catalog.html.txt) · [CSV清单](../../research/graph_catalog.csv)。这是既有总账派生的152行/43参数/Lean45导航，不是第二Wiki或总账；口径为103个历史D5 prefix＋继承F5/3750一图＋48个stage完整实例。107项链接literal边表，45个早期prefix链接原generator/params；不重生成。'
assert node_nav not in row.get('distance_text','');row['distance_text']=node_nav+'\n\n'+row.get('distance_text','')
row['other_metrics']['derived_user_graph_catalog_navigation']=dict(status='NAVIGATION_ONLY_EXISTING_COUNTS_UNCHANGED',HTML=paths[0],HTML_source=paths[1],CSV=paths[2],named_rows=152,parameter_groups=43,concrete_Lean_instances=45,instance_partition=dict(historical_D5_prefixes=103,inherited_F5_3750=1,accepted_stage=48),literal_edge_table_links=107,early_prefix_generator_parameter_links=45,derived_not_second_Wiki_or_ledger=True,graph_regeneration_BFS_compile_network_runs=0)
row['evidence_paths']=list(dict.fromkeys(row.get('evidence_paths',[])+paths));raw=W/f'updates/{B}_ROWS.json';raw.write_text(json.dumps([row],ensure_ascii=False,indent=2)+'\n');calls=[]
def call(*cmd):
 p=subprocess.run([str(x)for x in cmd],cwd=R,text=True,capture_output=True);calls.append(dict(command=[str(x)for x in cmd],returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,(cmd,p.stderr,p.stdout);return p.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',raw).strip())
block=f'''<!-- {B} -->
## 用户总图清单导航

[HTML总图清单](../research/graph_catalog.html) · [HTML原样源码](../research/graph_catalog.html.txt) · [CSV总图清单](../research/graph_catalog.csv)。152行／43参数／Lean45；103个历史D5 prefix＋继承F5/3750一图＋48个stage完整实例。107项链接literal边表，45个早期prefix链接原generator/params。此为现有总账派生的用户导航，不是第二Wiki／总账；本次不重生成图、BFS、编译或网络核验，不改任何计数。

'''
gap=W/'gap_map.md';assert B not in gap.read_text();gap.write_text(block+gap.read_text())
helper=R/'aris_repo/tools/research_wiki.py';call(sys.executable,helper,'rebuild_query_pack',W)
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert tuple(L[k]for k in keys)==(420,152,43,45)
node=(W/'experiments'/f'{ident}.md').read_text();query=(W/'query_pack.md').read_text();assert all(p in node for p in paths)and all('../'+p in query for p in paths)
(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
receipt=dict(status='PASS_NAVIGATION_ONLY_THREE_CATALOG_LINKS_EXISTING_RESULT_NODE_AND_CANONICAL_QUERY_PACK',updated_UTC=now,ledger_records=420,records_added=0,records_updated=1,named_graphs=152,parameters=43,Lean=45,derived_catalog_not_second_Wiki_or_ledger=True,
 links=paths,navigation_visible_in=[f'research-wiki/experiments/{ident}.md','research-wiki/query_pack.md'],query_canonical_source='research-wiki/gap_map.md',scope='103historicalD5prefixes+inheritedF53750+48stage;107literal_edge_links+45original_generator_params_links',
 existing_counts_inherited_not_recomputed=True,three_paths_exist=True,actual_helper_calls=f'research-wiki/updates/{B}_HELPER_CALLS.json',graph_regeneration_BFS_Lean_solver_network_runs=0,mathematics_or_method_changes=0,root_owned_or_catalog_files_modified=False,frozen_packets_modified=False)
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False))

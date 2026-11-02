"""One canonical experiment delta; no source or graph computation."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,json,re,runpy,time
START=time.process_time();R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir());W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';OUT=R/S/'wiki_sync';LABEL='D6D9_SOURCE_SINGLE_SUBDIVISION_TERMINAL_20261101';NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def read(p):return json.loads((R/p).read_text())
P=S+'stale_record_transfer_d6D9/source_interface/'
s=read(P+'RESULT.json');g=read(P+'single_subdivision_R8_gate/RESULT.json');t=read(P+'single_subdivision_R8_gate/TERMINAL.json')
assert s['source_degree']['all_regular'] and s['source_degree']['minimum']==s['source_degree']['maximum']==6
assert s['target']['current_order']==331387 and s['source_edges']==994161
assert g['status']=='COMPLETE_NO_SINGLE_EDGE_SUBDIVISION_D9_ON_FIXED_SOURCE'
assert g['query_count']==3 and g['all_three_types_fail'] and t['all_processes_terminal'] and not t['running']
assert [x['missing_old_count'] for x in g['queries']]==[14088,13875,14028]
assert [x['covered_old_count'] for x in g['queries']]==[317299,317512,317359]
assert [x['first_missing_label'] for x in g['queries']]==[20,6,20]
paths=[P+n for n in ['NOTE.md','RESULT.json','single_subdivision_R8_gate/PRED.md','single_subdivision_R8_gate/NOTE.md','single_subdivision_R8_gate/RESULT.json','single_subdivision_R8_gate/TERMINAL.json','single_subdivision_R8_gate/run.cpp','single_subdivision_R8_gate/run_once.py']]
paths += [s['local_generator'],s['primary_cache']]+[x['receipt'] for x in s['inherited_closed_scopes']]
assert all((R/x).is_file() for x in paths)
rid='ddp-stale-d6d9-331387-source-single-edge-subdivision-all-types-20261101'
row=dict(id=rid,title='6D9旧331387源：无余度append关闭；三generator-type的R8缺口排全部单边细分，非全参数关闭',family='edge subdivision and retained-source routing',idea_family='idea:ddp-open-parameter-construction-20261026',date='2026-11-01',record_type='necessary_route_or_input_transfer_gate',target_Delta=6,target_D=9,savedL=331387,baseline_date='2026-11-01 actual current main; source communicated2012-08-20',n=dict(actual=None,hypothetical=331388),actual_graph_Delta=None,actual_D=None,actual_D_scope='Inherited sourceD9; three exact modified-old endpoint-R8 queries only, no full candidate or old-oldD9 BFS',ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=9,
 scope=g['exact_scope']+' Full-oldedge-preserving connected append also has no spare at cap6. No multi-edge subdivisions, old rewiring or all(6,9) exclusion.',outcome_class=g['status'],new_lower_bound=False,
 distance_text='实际小Crecipe与cached primary给331387/994161全6regular，非新全degree扫描；cap6纯保边append无连接余度。RIGHT Cayley C49⋊41F6763的三inverse-pair代表(25,1254)/(18,541)/(47,4642)在各自删边host中端点B8 union仅覆盖317299/317512/317359，漏14088/13875/14028个旧点；首漏labels20/6/20，新细分点距各至少10。三query覆盖全oldedges的理由是lefttranslation，不是三随机样本。未生成331388完整图、未测oldold或原sourceD9。',
 lesson_and_restart_condition='STOP every single-edge subdivision of this fixed source. NewrootR9 pass would still not certify old-oldD9, but allthree types already fail. Do not repeat the sameedge at other labels or reopen priorF6959/ramified6860 closed families. Other grafts, multiple edited edges or a different source require genuinely changed premises; Moore余量不保证可实现。',
 restart_condition='Only an explicitly changed source/connection operation; no new timer, generator/field ladder or otheredge label for this closed single-subdivision rule.',unclosed_gap='General(6,9) and other edge-edit mechanisms remain open; no new graph or parameter.',
 metrics_raw='Subdivision distance proof: writeH=G−{u,v}. Every simple newz-to-oldt path first takeszu orzv and thereafter stays inH, so d(z,t)=1+min(d_H(u,t),d_H(v,t)). Thus the two-sourceR8 miss gives d(z,t)>=10. Translation proof: for a right Cayley edge{g,gs}, lefttranslation by g^(-1) maps it to{1,s}. Ifs is an inverse generator, lefttranslation by the positive generator maps{1,s^(-1)} to{s,1}. Lefttranslation extends by mapping insertedz to the representative insertedz, so three positive types exhaustalloldedge subdivisions. Noedge-transitivity across the three pairs is assumed. Author left-Cayley and this right-Cayley model are related by the already-bound inversion isomorphism.',
 other_metrics=dict(new_graphs=0,new_parameter_pairs=0,new_Lean_instances=0,new_independent_method_claims=0,Moore_bound=2929687,located_baseline=331387,Moore_space=2598300,Moore_space_is_only_upper_bound_slack=True,
 source_order=331387,source_edges=994161,source_degree_evidence=s['source_degree'],free_vertices_at_cap6=0,total_degree_spare_at_cap6=0,source_D9='INHERITED_NOT_REVERIFIED',source_primary_authors=s['primary_authors'],source_communication_date=s['primary_communication_date'],source_C_recipe=s['local_generator'],actual_source_raw_adjacency_not_downloaded=True,
 group=s['group'],three_endpoint_radius8_queries=g['queries'],all_single_edges_covered_by_lefttranslations=True,three_queries_are_not_random_samples=True,newroot_distance_claim='at least10, no unsupported exactdistance or route',oldold_candidate_BFS=0,original_source_allroot_D9_BFS=0,field_source_validation=0,raw_graph_download_generation=0,
 prior_closed_scopes_inherited=s['inherited_closed_scopes'],cumulative_charged_CPU_seconds=t['cumulative_charged_CPU_seconds'],CPU_budget_seconds=10,prior_source_interface_charge=t['prior_case_CPU_seconds'],preparation_and_failure_history_preserved=True,no_timer_reset=True,terminal=True),evidence_paths=paths)
L=read('research-wiki/DDP_METHOD_LEDGER.json');before=L['record_count'];assert before==429
existing={x['id']:x for x in L['rows']};assert len(existing)==before and rid not in existing and not(W/'experiments'/f'{rid}.md').exists()
keys=['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs'];counts={k:L[k] for k in keys};assert tuple(counts[k] for k in keys[:3])==(152,43,46)
END='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';prefix={}
for fn in ['index.md','query_pack.md','gap_map.md']:
 text=(W/fn).read_text();assert text.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->') and END in text and LABEL not in text;prefix[fn]=text[:text.index(END)+len(END)]
mdpath=W/'DDP_METHOD_LEDGER.md';assert LABEL not in mdpath.read_text()
rawpath=OUT/f'{LABEL}_ROWS.json';rawpath.write_text(json.dumps([row],ensure_ascii=False,indent=2)+'\n')
c=runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'));helper=c['helper'];helper.rebuild_index=lambda *a,**k:None;helper.rebuild_query_pack=lambda *a,**k:None
n=c['normalize'](row);n['goal']['baseline_date']=row['baseline_date']
with (OUT/f'{LABEL}_NODE_CALLS.log').open('w') as log,contextlib.redirect_stdout(log):c['write_node'](n)
existing[rid]=n;L.update(rows=list(existing.values()),record_count=len(existing),updated_UTC=NOW);L['input_counts'][str(rawpath.relative_to(R))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
safe=c['safe'];table='| ['+safe(n['title'])+'](experiments/'+rid+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[原始证据](../'+paths[0]+') |'
md=mdpath.read_text();needle=f'本页有{before}条记录；不以此宣称{before}种独立方法。';assert needle in md
md=md.replace(needle,'本页有430条记录；不以此宣称430种独立方法。',1)
md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 6D9源接口与单细分必要门终态\n\n| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |\n|---|---|---|---|\n'+table+'\n\n只读source接口与三个generator必要门合1实验节点，不增独立方法；所有图／参数／Lean增量0。\n';mdpath.write_text(md)
nav='<!-- '+LABEL+' -->\n### 2026-11-01 最后一项终态：6D9旧源全部单边细分严格STOP\n\n331387/994161全6regular源没有纯append余度。三generator-type删边端点R8 query缺14088／13875／14028，newz距首漏至少10；lefttranslations穷尽该source所有oldedges，因此是全single-subdivision严格NO，不是三个样本，也不是整个6D9无解。Moore空间2598300仅上界余量。累计.827553591/10CPU，0原sourceD9／oldoldBFS／raw下载／field验证；旧F6959全42normalized和ramified6860闭域继承停止。152／43／Lean46、旧n61暂停均不变。\n\n['+n['title']+'](experiments/'+rid+'.md)\n\n'
preserved={}
for fn,pre in prefix.items():
 path=W/fn;text=path.read_text();assert text.startswith(pre);at=len(pre);text=text[:at]+'\n\n'+nav+text[at:]
 if fn=='index.md':
  m=re.search(r'^## Experiments \((\d+)\)$',text,re.M);assert m;text=text[:m.start()]+f'## Experiments ({int(m[1])+1})'+text[m.end():];pos=text.index('\n',m.start())+1;text=text[:pos]+'- `exp:'+rid+'` — '+n['title']+' [no]\n'+text[pos:]
 assert text[:at]==pre;path.write_text(text);preserved[fn]=True
helper.append_log(str(W),LABEL+': one canonical node combines cached331387 full6regular source interface and allthree positivegenerator endpointR8 failures;lefttranslation exhaustsalloldedge subdivisions. Missing14088/13875/14028;no graph/parameter/Lean increment or sourceD9/oldoldBFS/field/raw rerun. OldF6959/ramified6860 scopes inherited;notgeneral6D9closure. Human top blocks preserved;152/43/46 unchanged.')
after=read('research-wiki/DDP_METHOD_LEDGER.json');assert after['record_count']==430 and {k:after[k] for k in keys}==counts
receipt=dict(status='PASS_ONE_CANONICAL_SOURCE_SUBDIVISION_TERMINAL_NODE',updated_UTC=NOW,records_before=before,records_after=430,records_added=1,new_experiment_id=rid,source_interface_and_three_types_one_node=True,full_single_edge_subdivision_scope_closed=True,general6D9_not_closed=True,Moore_space=2598300,human_top_blocks_preserved_exact=preserved,full_index_query_rebuild=False,counts_unchanged=counts,graph_parameter_Lean_method_increments=[0,0,0,0],source_BFS_oldold_BFS_field_raw_solver_Lean_remote_hash_runs=0,root_STATE_REPORT_progress_HTML_frozen_modified=False,writes_limited_to_Wiki_and_stage_wiki_sync=True,CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False,indent=2))

"""Root's actual new16416 Lean acceptance; no graph or formal run."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,copy,json,re,runpy,time
START=time.process_time();R=next(p for p in Path(__file__).resolve().parents if(p/'research-wiki').is_dir())
W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';OUT=R/S/'wiki_sync'
LABEL='D16_16416_LEAN47_ROOT_ACCEPTANCE_20261101';NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
oldid='ddp-d16d4-whole27-fullN-clone864-graph16416-20261101';rid=oldid.lower()
parent='ddp-d15-d4-current15552-source-gap-20261027'
PREVIOUS='D16_16416_715_PACKING1250_DELTA_20261101'
# Canonical normalizer lowercases ids. Repair only this just-created delta's references.
paths=[W/f for f in ['DDP_METHOD_LEDGER.json','DDP_METHOD_LEDGER.md','index.md','query_pack.md','gap_map.md']]
paths+=[W/'experiments'/f'{i}.md' for i in [rid,parent,'ddp-conder1250-edge-subdivision-two-cut-helper-family-20261027','ddp-stale-d11d3-715-fixed-induced-arbitrary-helpers-obstruction-20261101','ddp-stale-d11d3-715-cross-oldclass-helper-min3-tight-route-tradeoff-20261101']]
paths+=[OUT/f'{PREVIOUS}_{suffix}' for suffix in ['ROWS.json','UPSERTS.json','RECEIPT.json']]
paths+=[OUT/'sync_16416_715_packing1250_delta_20261101.py']
fixed=[]
for p in paths:
    text=p.read_text()
    if oldid in text:p.write_text(text.replace(oldid,rid));fixed.append(str(p.relative_to(R)))
def read(p):return json.loads((R/p).read_text())
L=read('research-wiki/DDP_METHOD_LEDGER.json');before=L['record_count'];records={x['id']:x for x in L['rows']}
assert before==438 and L['validated_named_graph_examples']==153 and L['complete_Lean_graph_instances']==46
assert rid in records and not(W/'experiments'/f'{oldid}.md').exists()
P=S+'retained_edge_transfer/published_d15_15552_D4_source_gate/degree16_plane864/'
dispo,final,binding=read(P+'ROOT_FULL_LEAN_DISPOSITION.json'),read(P+'formalization/FINAL.json'),read(P+'formalization/EXTERNAL_BINDING_RESULT.json')
assert dispo['status']=='ROOT_ACCEPTED_COMPLETE_ORIGINAL_CLONE16416_KERNEL_AUDIT_EXTERNAL_BINDING'
assert final['status']=='COMPLETE_CONCRETE_D16_16416_KERNEL_AUDIT_AND_EXTERNAL_BINDING'
assert final['all_processes_terminal'] and final['active_processes']==0
assert final['old16389_graph_PASS_not_used_as_new_graph_evidence'] and final['no_user_JSON_certificates_assumed']
assert binding['typed_I32_equal_producer_and_independent'] and binding['ordered_role_rows']==864
raw=copy.deepcopy(records[rid]['source_record'])
raw['id']=rid;raw['title']='16D4新版本16416：fresh全根exactD4＋新concreteLean/rootAudit实际通过；新ARIS的A/B在途、C未派'
raw['outcome_class']='ROOT_ACCEPTED_16416_MATH_AND_COMPLETE_KERNEL_NEW_ARIS_PENDING'
raw['distance_text']+=' 新concreteLean已实际完成并root全文接受：原无用户certificate目标、真Walk≤4和nonD3、Fin15552⊕Fin864≃Fin16416、160owner式/864roles/12924pins与新typedI32外部小表绑定，四新模块/Audit PASS，14.020610885/200CPU含一次失败；0oldPASS重编/0图BFS。ASCII parser theorem不在范围。新A/B各一次真实发出cell1064仍在途，C未派，不能借旧16389判定。'
raw['lesson_and_restart_condition']='Stop production/BFS and automatic33+packing. This same-mechanism newversion has actual mathematical and newconcreteLean rootacceptance,not inherited old16389PASS. Newscope A/B are actually in flight once each(cell1064),C not dispatched;no newARISPASS. Keep old715+familiarD4 two-question tradeoff and15oldcells priority.'
raw['unclosed_gap']='Latest global priority/originality UNKNOWN;newscope A/B in flight,C not dispatched,no newARIS verdict yet.'
m=raw['other_metrics'];m.update(new_Lean_instances=1,complete_Lean_graph_instance=True,
    new_concrete_Lean_status=dispo['status'],new_scope_ARIS='A_B_IN_FLIGHT_ONCE_EACH_CELL1064_C_NOT_DISPATCHED_NO_VERDICT',
    new_concrete_Lean_CPU_seconds=dispo['CPU_seconds'],new_concrete_Lean_CPU_budget_seconds=200,
    concrete_target=dispo['target'],original_concrete_goal=dispo['original_concrete_goal'],
    formal_label=dispo['label'],formal_true_Walk_le4=True,formal_not_DiameterAtMost3=True,
    formal_no_user_certificate_premises=True,formal_axioms=dispo['axioms'],
    formal_ASCII_parser_theorem=False,old_PASS_Lean_recompiles=0,new_formal_graph_BFS=0,
    new_owner_equations=160,new_typed_role_bindings=864,new_typed_pin_bindings=12924,
    formal_ROOT_disposition=P+'ROOT_FULL_LEAN_DISPOSITION.json',
    formal_FINAL=P+'formalization/FINAL.json',formal_external_binding=P+'formalization/EXTERNAL_BINDING_RESULT.json')
i=m['validated_graph_instances'][0];assert i['n']==16416
i.update(complete_Lean_graph_instance=True,formal_status=dispo['status'],
    formal_final_receipt=P+'formalization/FINAL.json',formal_ROOT_disposition=P+'ROOT_FULL_LEAN_DISPOSITION.json',
    concrete_target=dispo['target'],external_ARIS_AB_freshC='A_B_IN_FLIGHT_ONCE_EACH_CELL1064_C_NOT_DISPATCHED_NO_VERDICT')
extra=[P+'ROOT_FULL_LEAN_DISPOSITION.json',P+'formalization/FINAL.json',P+'formalization/EXTERNAL_BINDING_RESULT.json',
    'formal/DegreeDiameter/Portfolio/F3Graph15552Clone16416Definitions.lean',
    'formal/DegreeDiameter/Portfolio/F3Graph15552Clone16416Inputs.lean',
    'formal/DegreeDiameter/Portfolio/F3Graph15552Clone16416Exact.lean','formal/F3Graph15552Clone16416Audit.lean',
    S+'reviews/D16_D4_16416_A_REQUEST.json',S+'reviews/D16_D4_16416_B_REQUEST.json']
assert all((R/x).is_file() for x in extra)
raw['evidence_paths']+=extra
Q=S+'stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/ROOT_DISPOSITION.json'
assert(R/Q).is_file()
paperid='ddp-stale-d11d3-715-cross-oldclass-helper-min3-tight-route-tradeoff-20261101'
paper=records[paperid]
if Q not in paper['evidence_paths']:
    paper['evidence_paths'].append(Q);paper['source_record']['evidence_paths'].append(Q)
END='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';prefix={}
for fn in ['index.md','query_pack.md','gap_map.md']:
    text=(W/fn).read_text();assert text.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->') and LABEL not in text
    prefix[fn]=text[:text.index(END)+len(END)]
rawpath=OUT/f'{LABEL}_ROW.json';rawpath.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
c=runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'));helper=c['helper']
helper.rebuild_index=lambda*a,**k:None;helper.rebuild_query_pack=lambda*a,**k:None
n=c['normalize'](raw);n['goal']['baseline_date']=raw['baseline_date']
with(OUT/f'{LABEL}_NODE_CALLS.log').open('w') as log,contextlib.redirect_stdout(log):c['write_node'](n)
records[rid]=n;L.update(rows=list(records.values()),updated_UTC=NOW)
L['complete_Lean_graph_instances']=L['complete_deterministic_formula_Lean_graph_instances']=47
assert L['confirmed_publictable_complete_Lean_graph_instances']==1
L['confirmed_publictable_complete_Lean_graph_instances']=2
L['input_counts'][str(rawpath.relative_to(R))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')
safe=c['safe'];table='| ['+safe(n['title'])+'](experiments/'+rid+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[原始证据](../'+n['evidence_paths'][0]+') |'
mp=W/'DDP_METHOD_LEDGER.md';md=mp.read_text();lines=md.splitlines();changed=0
for j,line in enumerate(lines):
    if line.startswith('| [') and '(experiments/'+rid+'.md)' in line:lines[j]=table;changed+=1
assert changed==1;md='\n'.join(lines)+'\n'
head=re.search(r'^更新：[^\n]+',md,re.M);assert head
summary='更新：'+NOW+'。超过保存主表基线4参数／105例；数学合法共153例／43参数。已知被更大公开构造超过43例（其中40例同时超过保存主表）；保存主表外新颖性待核45例／38参数。完整具体公式图Lean47例，16416新kernel/rootAudit及外部小表绑定已实际接受；新A/B在途、C未派。全球确认0，主表计数不是全球纪录认证。'
md=md[:head.start()]+summary+md[head.end():]
md+='\n\n<!-- '+LABEL+' -->\n## '+NOW+' 16416新concreteLean实际root接受；ARIS仍在途\n\n既有16416节点原位更新，不加记录/图/参数/方法；完整具体Lean+1至47。新Fin15552⊕Fin864原目标、真Walk4/nonD3、160owner/864roles/12924pins及typedI32外部绑定通过；14.020610885/200CPU含失败，不重旧PASS/图BFS。A/B各一次真实发出cell1064在途，C未派，未记互审PASS。153/43/47、savedmain105/4、outside45/38、known43(overlap40)、global0。\n';mp.write_text(md)
nav='<!-- '+LABEL+' -->\n### '+NOW+' 最新actual：16416新完整Lean已接受，总计153／43／47\n\nroot已实读并接受16416原具体目标/newDefinitions/Inputs/Exact/Audit/FINAL/typedI32外部小表绑定：无用户certificate前提，真SimpleGraph.Walk≤4且nonD3，Fin15552⊕Fin864≃Fin16416，160新owner式、864orderedroles、12924pins；14.020610885/200CPU含一次失败，0旧PASS重编/0图BFS。新Lean+1，源复现不计；旧16389合法完整Lean及ABfreshC保持。新16416的A/B各一次真实发出cell1064仍在途，C未派，不能记互审PASS或继承旧判定。\n\n当前153图／43参数／47完整具体Lean；savedmain105/4，outside45/38，known43（overlap40），global确认0。715扩域mixedmin3仍未排；1250旧scope继承STOP；一线老715＋一线熟悉D4的真实新图，不自动33+，15老格人工主线、sameGoal ACTIVE及旧N8/n61暂停均保留。\n\n['+n['title']+'](experiments/'+rid+'.md)；[715新paper边界](experiments/'+paperid+'.md)\n\n'
preserved={}
for fn,pre in prefix.items():
    p=W/fn;text=p.read_text();assert text.startswith(pre);at=len(pre);text=text[:at]+'\n\n'+nav+text[at:]
    if fn=='index.md':
        text=re.sub(r'^- `exp:'+re.escape(rid)+r'`[^\n]*','- `exp:'+rid+'` — '+n['title']+' [yes]',text,flags=re.M)
    assert text[:at]==pre;p.write_text(text);preserved[fn]=True
pp=W/'experiments'/f'{parent}.md'
pp.write_text(pp.read_text()+'\n\n<!-- '+LABEL+' -->\n## 新16416后续实际formal终态\n\n前段“新Lean待完成”是接收前快照；现root已接受新16416具体kernel/Audit及typedI32/864role/12924pin外部小表绑定，完整Lean47。A/B仍在途、C未派；旧16389原完整Lean/ABfreshC并未覆盖或改写。见[新版本当前节点]('+rid+'.md)。0新BFS/旧PASS重编，不自动33+。\n')
helper.append_log(str(W),LABEL+': existing16416nodeupsert only;actualnewconcretekernel/Audit/typedI32externalbinding ROOTaccepted,Lean46to47,no graphorparameterorrecordincrement. NewA/Bactuallyinflightcell1064,Cnotdispatched,noreviewPASSinherited. Canonical fulln id references fixed locally;human15oldcells top preserved,153/43/47,savedmain105/4,outside45/38,known43overlap40/global0;no computationsorfullrebuild.')
after=read('research-wiki/DDP_METHOD_LEDGER.json');assert after['record_count']==before and after['complete_Lean_graph_instances']==47
assert after['validated_named_graph_examples']==153 and after['saved_main_table_improvement_graph_examples']==105
assert (W/'experiments'/f'{rid}.md').is_file()
receipt=dict(status='PASS_EXISTING_NEW16416_NODE_ACTUAL_ROOT_LEAN47_DELTA',updated_UTC=NOW,
    records_before=before,records_after=before,records_added=0,canonical_newgraph_id=rid,
    graph_increment=0,parameter_increment=0,Lean_increment=1,independent_method_increment=0,
    final_counts=dict(graphs=153,parameters=43,Lean=47,savedmain_graphs=105,savedmain_parameters=4,
        outside_graphs=45,outside_parameters=38,known_dominated=43,dominated_overlap_savedmain=40,global_confirmed=0),
    formal_ROOT_disposition=P+'ROOT_FULL_LEAN_DISPOSITION.json',new_ARIS=dict(A='IN_FLIGHT_ONCE',B='IN_FLIGHT_ONCE',cell=1064,C='NOT_DISPATCHED',actual_new_verdicts=0),
    old16389_original_math_Lean_ARIS_preserved=True,canonical_id_references_fixed=bool(fixed),
    human_top_blocks_preserved_exact=preserved,full_index_query_rebuild=False,
    source_graph_BFS_Lean_solver_paidreview_hash_runs=0,root_STATE_docs_HTML_REPORT_modified=False,
    writes_limited_to_Wiki_and_stage_wiki_sync=True,CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))

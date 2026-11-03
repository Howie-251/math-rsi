"""Extend the existing P33 row to fifteen actual instances; no research is rerun."""
from pathlib import Path
from datetime import datetime,timezone
import copy,json,re,subprocess,sys
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parents[2];W=ROOT/'research-wiki'
S='research/ddp/two_successful_methods_20261101/'
B=S+'retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/'
L=B+'multiplicity65_72_family/';U=B+'multiplicity73_79_family/';I=U+'independent_acceptance/';F=U+'formalization/'
P=S+'public_baseline_audit/';R=S+'reviews/'
ID='ddp-gq77-published-p33-immutable-fulln64-clone-eight-degree65-72-family-20261101'
STEM='P33_SAME_FAMILY_FIFTEEN_ACCEPTED_140_33_LEAN34_20261101'
read=lambda p:json.loads((ROOT/p).read_text())
state=read(S+'STAGE_STATE.json');assert state['accepted_total_named_legal_instances']==140 and state['complete_concrete_formula_Lean_instances']==34
upper=read(I+'RESULT.json');terminal=read(I+'TERMINAL.json');final=read(F+'FINAL.json');binding=read(F+'INPUT_BINDING_CHECK.json');production=read(U+'RESULT.json')
assert upper['status']=='PASS_ALL_SEVEN_P33_DEGREE73_79_ENDPOINT_GRAPHS' and terminal['status']=='PASS'
assert final['status']=='COMPLETE_SEVEN_UPPER_ORIGINAL_TARGETS_AND_SEPARATE_AUDIT'
assert final['new_modules_compiled']==2 and final['upper_external_rows_bound']==138600
assert not final['degree80_concrete_instance_or_graph_written']
ledger=read('research-wiki/DDP_METHOD_LEDGER.json');row=copy.deepcopy(next(r for r in ledger['rows'] if r['id']==ID)['source_record']);m=row['other_metrics']
assert len(m['validated_graph_instances'])==8
lower_A='4b88cfe2-b903-47cb-ad7f-103068dc5909';lower_B='1b139619-83c2-4bd7-ac92-9a9c7a2df136'
for g in m['validated_graph_instances']:
    g.update(batch='lower8_k1_to8',external_A='ACTUAL_ENCODING_CHECKPOINT_PASS_NOT_FINAL_KERNEL_VERDICT',external_A_cell='423',external_A_thread=lower_A,
             external_B='ACTUAL_PASS_EACH_LOWER8_ORIGINAL_TARGET',external_B_cell='428',external_B_thread=lower_B,
             external_distinctfreshC='notrequested_planned_one_fresh_joint15_original_scope')
window=read(P+'P33_CLONE_DEGREE73_80_WINDOW_20261101.json');pub={r['Delta']:r for r in window['endpoints']}
theorems={e['degree']:e for e in final['original_endpoints']}
for c in upper['cases']:
    e=theorems[c['degree_cap']];assert e['n']==c['n'] and pub[c['degree_cap']]['passes_checked_public_gate']
    # Keep exact multiplicities as their source-class product. In particular,
    # the degree77 value 33*13 overlaps an HTTP token in the existing filter.
    derived=[dict(histogram=h['histogram'],roots_expression=f'{33 if j==0 else 1617}*{c["k"]}') for j,h in enumerate(c['proof_derived_histogram_distribution'])]
    m['validated_graph_instances'].append(dict(Delta=c['degree_cap'],D=3,n=c['n'],m=c['m'],actual_diameter=3,
        mathematically_validated_complete_graph=True,complete_Lean_graph_instance=True,known_nonrecord=False,known_publicly_dominated=False,
        latest_global_record_confirmed=False,confirmed_publictable_improvement=False,
        best_located_public_lower_bound=pub[c['degree_cap']]['current_strongest_checked_public_guarantee'],bounded_gain=50,
        copy_count=c['k'],batch='upper7_k9_to15',graph_path=U+f'graphs/d{c["degree_cap"]}_D3_n{c["n"]}.edges',
        degree_histogram={'64':c['degree64_count'],str(c['degree_cap']):c['high_degree_count']},
        independent_literal_fullN64_rows=c['new_vertices'],actual_new_root_BFS=c['actual_new_literal_R3_BFS_roots'],
        proof_derived_histogram_distribution=derived,actual_BFS_histogram_distribution=c['actual_BFS_histogram_distribution'],
        all_pair_prefix_proof_independent_of_max_BFS=True,max_BFS_used_to_infer_smaller_diameter=False,
        formal_status='COMPLETE_UNCONDITIONAL_UPPER_ORIGINAL_TARGET_AND_SEPARATE_AUDIT_STD3',
        concrete_original_theorem=final['namespace']+'.'+e['theorem'],final_claim=final['namespace']+'.'+e['final_claim'],
        formal_scope='Actual parent graph k9..15 / explicit card,maxdegree,true SimpleGraph.WalkD3,nonD2; no certificate premises, separate7types/body/finalclaims/axiomAudit std3.138600 ordered label bindings external, not Audit#eval.',
        external_A='IN_FLIGHT_EXPLICIT_UPPER7_ENCODING_SCOPE_NOT_INHERITED_LOWER_PASS',external_A_cell='438',external_A_thread=lower_A,
        external_B='IN_FLIGHT_EXPLICIT_UPPER7_ORIGINAL_BRIDGE_SCOPE_NOT_INHERITED_LOWER_PASS',external_B_cell='440',external_B_thread=lower_B,
        external_distinctfreshC='notrequested_planned_one_fresh_joint15_original_scope'))
assert len(m['validated_graph_instances'])==15
row['title']='同一P33规则65..79十五完整图：独验／十五具体Lean-Audit完成，下8A/B通过、上7A/B在途'
row['outcome_class']='FIFTEEN_LITERAL_GRAPHS_FRESH_ACCEPTED_FIFTEEN_CONCRETE_LEAN_AUDIT_PASS_LOWER8_A_B_PASS_UPPER7_A_B_IN_FLIGHT_FINAL_C_NOT_REQUESTED'
row['actual_D_scope']='十五终图各自完整字面旧边/新点N64/degree绑定和old-only全点对/每prefix证明；只两批最大图k8/k15实际新根BFS，非十五图全源BFS。'
row['distance_text']='同一P33×50=1650不可变原N64，k1..15对应degree65..79、n160050+1650k、m5121600+105600k；全部15完整终图fresh独验及各原具体Lean/Audit PASS，各超已核公开保证50。lower8完整绑定59400行/仅k8实际13200新根BFS，upper7绑定138600行/仅k15实际24750新根BFS；合198000绑定、37950实际新根BFS只跨2图。upper1650sourceR2按centerID继承、0重测；0旧R3/field重验。upper仅两新Lean模块9.297359270CPU/无finite重检，parent24不改不编。degree80被公开GQ(7,9)327680阻断，0graph/原目标/Audit实例。'
row['scope']='原已接受filled160050/64regular源、实际33点大小复现归功2007、固定50spread顺序；同一immutable-source-neighborhood复制规则十五终点k1..15，不拆成十五方法、不链用lower endpoint作新源。新68n166650/m5544000与旧70同阶边数但degreehist不同，按(Delta,D,n)区分。'
row['unclosed_gap']='十五完整数学图／十五无前提原具体Lean目标、各final_claim及独立Audit/std3全部actualPASS。lower8的新scope A423 encoding及B428逐原目标actualPASS；upper7追加A438及B440各一次仍在途，下八verdict不覆盖上七。最终C尚未派，计划一次distinctfresh新thread透明联合15原目标逐一给verdict，不是15calls。本地CHECKPOINT_C不是外部C。全球最高／优先权未认证，旧冻结包不含本十五图。'
row['lesson_and_restart_condition']='先由q7标准Payne partialovoid≤42把特定矩形上包络压至2058/degree，消除旧full49假设；再公门实际发现q8直接GQ在80给327680，故只追加k9..15七个竞争端点，80停。新七个完整图及七具体原目标成功，P33整体一个family十五实例；当前只收上七A/B及一次fresh15finalC，不自动80+、controllersearch或新模板。'
m.update(new_named_complete_graphs=15,new_Lean_instances=15,rules=1,accepted_endpoint_instances=15,selected_k=list(range(1,16)),
    new_parameter_pairs=[[d,3] for d in list(range(66,70))+list(range(71,80))],
    independent_new_literal_N64_rows=198000,actual_new_root_BFS=37950,actual_BFS_k_values=[8,15],actual_BFS_graphs=2,
    independent_CPU_seconds=54.503863383,independent_source_parses=2,producer_CPU_seconds=4.337301139000001,producer_source_parses=2,
    formal_current_modules=26,formal_upper_new_modules=2,formal_upper_new_finite_checks=0,
    formal_CPU_seconds=104.33886026799998,formal_lower_accounted_CPU_seconds=95.04150099799998,formal_upper_accounted_CPU_seconds=9.297359270000001,
    formal_actual_original_targets_complete=15,formal_external_ordered_recipe_rows_bound=198000,
    formal_final_receipts=[L+'formalization/FINAL.json',F+'FINAL.json'],formal_stage_status='ALL_FIFTEEN_ORIGINAL_CONCRETE_TARGETS_AND_SEPARATE_LOWER_UPPER_AUDITS_COMPLETE',
    formal_upper_parent24_modified_or_recompiled=False,formal_upper_Audit_eval138600_claim=False,
    source_R2_prediction_batches=1,source_R2_only_centers=1650,upper_source_R2_recomputed=0,
    lower8_review_scope={'A':'ACTUAL_ENCODING_CHECKPOINT_PASS','A_cell':'423','A_thread':lower_A,'B':'ACTUAL_EACH_ORIGINAL_TARGET_PASS','B_cell':'428','B_thread':lower_B,'fresh_C':'notrequested'},
    upper7_review_scope={'A':'IN_FLIGHT_ADDITIONAL7_ENCODING_SCOPE','A_cell':'438','A_thread':lower_A,'B':'IN_FLIGHT_ADDITIONAL7_ORIGINAL_BRIDGE_SCOPE','B_cell':'440','B_thread':lower_B,'lower8_PASS_inherited':False},
    external_final_fresh_C_scope='NOT_YET_REQUESTED; planned one distinctfresh newthread joint15 explicit originaltargets afterupperA/B',
    external_review_A='LOWER8_ENCODING_PASS_UPPER7_ENCODING_IN_FLIGHT',external_review_B='LOWER8_EACH_ORIGINAL_PASS_UPPER7_ADDITIONAL_SCOPE_IN_FLIGHT',
    external_review_distinctfreshC='NOT_YET_REQUESTED_JOINT15_PLANNED',external_all_A_B_freshC_complete=False,
    degree80={'status':'STOPPED_PUBLIC_COMPETITION_NOT_GRAPH_IMPOSSIBILITY','public_GQ7_9_order':327680,'hypothetical_candidate':186450,'graph_written':False,'concrete_original_instantiated':False,'Audit_instantiated':False},
    batches={'lower8_k1_to8':{'binding_rows':59400,'BFS_roots':13200,'BFS_only_k':8,'source_R2_measurements':1650,'independent_CPU':21.419453053,'formal_modules':24,'formal_CPU':95.04150099799998},
             'upper7_k9_to15':{'binding_rows':138600,'BFS_roots':24750,'BFS_only_k':15,'source_R2_measurements':0,'inherited_center_predictions':1650,'independent_CPU':33.084410330000004,'formal_modules':2,'formal_CPU':9.297359270000001}})
for stale in ['actual_BFS_k','other_seven_endpoint_BFS','external_review_A_cell','external_review_B_cell']:
    m.pop(stale,None)
row['positive_guarantees']=[x.replace('八图各自恰D3','十五图各自恰D3').replace('只有k8实际BFS，k1..7为证明导出的histogram','仅k8和k15实际新根BFS，其他端点为证明导出的histogram') for x in row['positive_guarantees']]
row['positive_guarantees'].append('upper7独立case各完整literalbinding与old-only内部路线证明；1650center R2只继承并逐ID绑定，0源R2/R3重复，不以大图BFS外推小图。')
extra=[U+x for x in ['PRED.md','PROOF.md','RESULT.json','TERMINAL.json','ORDERED_CLONE_RECIPE.tsv','PREFIX_LOADS.csv','produce.cpp','run_once.py']]
extra += [I+x for x in ['PRED.md','RESULT.json','SUMMARY.json','TERMINAL.json','PROOF.md','INHERITED_PREDICTION_BINDING.json','SOURCE_R2_PREDICTIONS_INHERITED.csv','verify.cpp','run_once.py','cases/d79_n184800/NEW_ROOT_BFS_PREDICTION_VS_ACTUAL.csv']]
extra += [F+x for x in ['FINAL.json','INPUT_BINDING_CHECK.json','CHECKPOINT_B.md','CHECKPOINT_C.md','GQ77Published33CloneFamilyUpperExact_RESULT.json','GQ77Published33CloneFamilyUpperAudit_RESULT.json']]
extra += ['formal/DegreeDiameter/Portfolio/GQ77Published33CloneFamilyUpperExact.lean','formal/GQ77Published33CloneFamilyUpperAudit.lean']
extra += [P+x for x in ['PAYNE68_FULL_OVOID_SPREAD_CONTINUATION_GATE_20261101.md','PAYNE68_FULL_OVOID_SPREAD_CONTINUATION_GATE_20261101.json','P33_CLONE_DEGREE73_80_WINDOW_20261101.md','P33_CLONE_DEGREE73_80_WINDOW_20261101.json']]
extra += [R+'P33_EIGHT_TARGETS_'+x for x in ['A_GEMINI_RAW.json','A_DISPOSITION.md','B_GEMINI_RAW.json','B_DISPOSITION.md']]
extra += [g['graph_path'] for g in m['validated_graph_instances'] if g.get('batch')=='upper7_k9_to15']
row['evidence_paths']=list(dict.fromkeys(row['evidence_paths']+extra))
assert all((ROOT/p).exists() for p in row['evidence_paths'])
assert sum(g['independent_literal_fullN64_rows'] for g in m['validated_graph_instances'])==198000
assert sum(g['actual_new_root_BFS'] for g in m['validated_graph_instances'])==37950
assert all(g['Delta']<80 and g['complete_Lean_graph_instance'] for g in m['validated_graph_instances'])
raw=W/'updates'/f'{STEM}_ROWS.json';raw.write_text(json.dumps([row],ensure_ascii=False,indent=2)+'\n')
cmd=[sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(raw)]
x=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True);assert x.returncode==0,(x.stdout,x.stderr)
sync=json.loads(x.stdout);now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
intro=f'''<!-- {STEM} -->
# 当前：同一P33规则十五完整图及具体Lean完成，140例／33参数／Lean34

同Goal ACTIVE：140合法图／33参数，阶段36图／30参数，具体Lean34；ledger416复用原family不增行。knownpublicdominated43、savedoverlap40、outsidepending34例／29参数、main103/3、全球认证0。

[P33 family十五图](experiments/{ID}.md)已扩65..79、k1..15，各比已核公开保证+50。lower8绑定59400／实际BFS13200只k8；upper7绑定138600／实际BFS24750只k15，合198000绑定、37950实际新根BFS跨2图，非15图全源。upper继承1650sourceR2、0重测，0旧R3/field重验；upper独验33.084410CPU。

upper七原具体目标／独立Audit实际PASS，两新模块9.297359CPU，parent24不改不编；138600外部行绑定非Audit#eval。lower8 A423/B428 actualPASS；upper7 A438/B440沿各自thread追加明确scope在途，下八PASS不继承。最终C尚未派，计划一次distinctfresh联合15原目标逐一verdict，不是15calls。

degree80已被公开GQ(7,9)327680阻断，0graph／原目标／Audit实例，不续80+。专家15draft由root另派，旧冻结包不动。以下保留历史。

'''
gap=W/'gap_map.md';t=gap.read_text()
if not t.startswith(f'<!-- {STEM} -->'):gap.write_text(intro+t)
h=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md'
if f'<!-- {STEM} -->' not in h.read_text():
    with h.open('a') as f:f.write(f'''\n\n<!-- {STEM} -->
## 2026-11-01 从明确公开门延伸七个端点，同family十五图及Lean全部完成

root实际读upper7独验RESULT/TERMINAL/完整PROOF、UpperExact全文、UpperAudit逐7type/body/std3及FINAL，正式140合法/33参数、stage36/30、Lean34=27+7。唯一Wiki只复用[P33原family](experiments/{ID}.md)，现15validated实例、一个规则，ledger416不增行。旧source/O22图仍合法；knownpublicdominated43、overlap40、main103/3、outsidepending34/29、global0不变。

这次延续基于具体判断：标准q7 Payne partialovoid上界42使所指packing中心≤2058，不能拿不存在的49fullO当已构造阻断；重新代入已核族则发现q8直接GQ在degree80给327680，故从原拟八窗口中停止80，只实际生成73/174900、74/176550、75/178200、76/179850、77/181500、78/183150、79/184800七端点，均+50。degree80没有graph、原theorem或Audit实例，不声称参数无图，不继续80+。

两批核验范围分别保存：lower8为59400新N64完整行绑定／实际13200BFS根仅k8；upper7为138600绑定／实际24750BFS根仅k15。总体198000literalbindings、37950actualBFS跨2张图，不能写成15图全根BFS。upper按centerID及base顺序继承lower1650sourceR2预测，0R2/R3重测；其最大新根495×(1,64,3200,181535)+24255×(1,64,3263,181472)逐根命中。其余六新图各自完整binding＋old-only内部路线/每prefix证明，不依赖最大BFS推小图。upperfresh独验33.084410330CPU。

upper新增两Lean模块，七个无前提原具体目标/各final_claim及独立Audit actualPASS/std3，9.297359270CPU，0新finite检查，parent24模块不改不编；138600外部有序行绑定非Audit#eval，旧59400未重查。[真实upper FINAL](../{F}FINAL.json)保全scope。

lower8 A423 encoding及B428逐原目标actualPASS，raw/处置已保存；upper7 A438与B440分别沿原A/B thread追加一次明确七目标scope仍在途，不能继承lowerPASS。最终C尚未派，计划待upperA/B实际返回后一次distinctfresh新thread联合15原目标逐一结论，非15calls。旧six-target C保持已完成。root另派专家15draft，当前及历史冻结包不修改，不重启研究/数学查询。
''')
helper=ROOT/'aris_repo/tools/research_wiki.py';calls=[]
for args in [('log',str(W),'2026-11-01 existingP33familyextendedlower8plusupper7=15actualinstances/140legal33pairsstage36_30Lean34,ledger416zeroNewRows;upper7rawbindings138600BFS24750onlyk15/sourceR2inheritedzeroRepeat,lower59400and13200onlyk8,total198000binding37950BFSacross2graphsnot15allroots;upper2modules9.29735927CPUparent24unchanged. Lower8A/BactualPASS,upper7A438/B440explicitadditionalScopeinflight,freshjoint15Cnotrequested;degree80public327680stopped0graph/theorem/Audit,global0known43pending34_29frozenpackuntouched.'),('rebuild_index',str(W)),('rebuild_query_pack',str(W))]:
    c=[sys.executable,str(helper),*args];z=subprocess.run(c,cwd=ROOT,text=True,capture_output=True)
    calls.append(dict(command=c,returncode=z.returncode,stdout=z.stdout,stderr=z.stderr));assert z.returncode==0,calls[-1]
cp=W/'updates'/f'{STEM}_HELPER_CALLS.json';cp.write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
current=read('research-wiki/DDP_METHOD_LEDGER.json');expected={'record_count':416,'validated_named_graph_examples':140,'validated_named_parameter_pairs':33,'complete_Lean_graph_instances':34,'known_publicly_dominated_graph_examples':43,'known_publicly_dominated_also_saved_table_improvement_examples':40,'pending_outside_saved_table_graph_examples':34,'pending_outside_saved_table_parameter_pairs':29}
for k,v in expected.items():assert current[k]==v,(k,current[k],v)
checked=0;p=W/'experiments'/f'{ID}.md'
for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
    target=unquote(target.strip('<>').split('#',1)[0])
    if not target or re.match(r'\w+://',target):continue
    assert (p.parent/target).exists(),target;checked+=1
q=(W/'query_pack.md').read_text();assert '140' in q and 'Lean34' in q and 'ledger416' in q and 'A438' in q
receipt=dict(updated_UTC=now,status='PASS_SAME_P33_FAMILY_FIFTEEN_ACTUAL_GRAPHS_LEAN34_SCOPE_SEPARATED',ledger_records=416,records_added=0,records_updated=1,family_rules=1,family_validated_instances=15,family_concrete_Lean_instances=15,named_legal_graphs=140,legal_parameter_pairs=33,stage_graphs=36,stage_pairs=30,complete_formula_Lean=34,known_publicly_dominated=43,saved_table_dominated_overlap=40,pending_outside_saved_table_graphs=34,pending_outside_saved_table_pairs=29,certified_global_records=0,new_accepted_graphs=7,new_Lean_instances=7,new_frameworks=0,lower_binding_BFS=[59400,13200],upper_binding_BFS=[138600,24750],total_binding_BFS=[198000,37950],BFS_graphs=[8,15],upper_source_R2_recomputed=0,upper_independent_CPU_seconds=33.084410330000004,upper_formal_modules=2,upper_formal_CPU_seconds=9.297359270000001,lower8_A_B='ACTUAL_PASS',upper7_A_B='438_440_EXPLICIT_ADDITIONAL_SCOPE_IN_FLIGHT',fresh_final_C='NOT_YET_REQUESTED_ONE_JOINT15_PLANNED',degree80_instances=0,canonical_upsert_command=cmd,canonical_upsert_stdout=sync,actual_helper_calls=str(cp.relative_to(ROOT)),resolved_evidence_paths=len(row['evidence_paths']),checked_local_markdown_links=checked,query_current=True,experiments_rerun=0,root_owned_files_modified=False,frozen_expert_packets_modified=False)
rp=W/'updates'/f'{STEM}_RECEIPT.json';rp.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False))

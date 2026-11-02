"""One S672 complete right-matching experiment delta; no new mathematics runs."""
from pathlib import Path
from datetime import datetime,timezone
import contextlib,copy,json,re,runpy,time
ROOT=Path(__file__).resolve().parents[4];W=ROOT/'research-wiki';S=Path(__file__).resolve().parent
D=ROOT/'research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344'
st=time.process_time();now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
slug='ddp-stale-d8d4-sampels672-all-right-matchings1344-complete-no-20261102';marker='<!-- SOURCE672_RIGHTMATCHING_FULL_DOMAIN_TERMINAL_20261102 -->'
ledger=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert ledger['record_count']==len(ledger['rows'])==453
assert not any(r['id']==slug or 'two672_right_matching1344' in json.dumps(r,ensure_ascii=False) for r in ledger['rows'])
oldrows=copy.deepcopy(ledger['rows']);counts={k:v for k,v in ledger.items() if k not in {'rows','record_count','updated_UTC','input_counts'}}
root=json.loads((D/'ROOT_DISPOSITION.json').read_text());r=json.loads((D/'RESULT.json').read_text());source=json.loads((D/'SOURCE_BINDING.json').read_text());diag=json.loads((D/'PHASE_COMPATIBILITY_DIAGNOSTIC.json').read_text())
assert root['status']=='ROOT_ACCEPTED_COMPLETE_NO_ALL672_RIGHTMATCHINGS_STOP' and root['cumulative_case_CPU']==1.645124787
assert r['checked_parameters']==r['full_domain_size']==672 and r['hit_t'] is None
assert source['identity_closed_ball_counts'][-1]==672 and all(x['maximum_saved_count']==106 and x['full112_t_count']==0 for x in diag['per_phase']) and diag['prediction_supported'] is False
common=runpy.run_path(str(ROOT/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
files=['index.md','query_pack.md','gap_map.md'];original={p:(W/p).read_text() for p in files};end='<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->';human={p:t[:t.index(end)+len(end)] for p,t in original.items()}
base=next(r for r in ledger['rows'] if r['id']=='ddp-stale-d8d4-two684-all-hleft-equivariant-matchings1368-no-20261101')['goal']['savedL']
names=['ROOT_DISPOSITION.json','NOTE.md','READ_GATE.md','READ_GATE.json','PAPER_INTERFACE.md','PRED.md','run_once.py','SOURCE_BINDING.json','SOURCE_GRAPH_CANONICAL.edges','ALL_T_RESULTS.tsv','RESULT.json','TERMINAL.json','ATTEMPT.json','PHASE_COMPATIBILITY_DIAGNOSTIC_PRED.md','diagnose_saved_phase_compatibility.py','PHASE_COMPATIBILITY_DIAGNOSTIC.json','PHASE_COMPATIBILITY_DIAGNOSTIC_NOTE.md']
evidence=[str((D/p).relative_to(ROOT)) for p in names];assert all((ROOT/p).exists() for p in evidence)
raw={
'id':slug,'title':'8D4两份published Sampels672全672右平移匹配NO：六phase各最多106/112，单层已不足',
'family':'Two-copy matching extension on a published Cayley source','idea_family':'idea:ddp-open-parameter-construction-20261026','date':'2026-11-02','wiki_verdict':'no',
'record_type':'fixed_published_Cayley_source_rightmatching_complete_route_experiment_and_saved_phase_diagnostic',
'target_Delta':8,'target_D':4,'savedL':base,'baseline_date':'Inherited8D4main1100; cachedprimarySampels6721997-07-29source; notcurrentglobalprioritycertification',
'n':{'actual':None,'hypothetical':1344},'actual_graph_Delta':None,'actual_D':None,'ordinary_bad_unordered_pairs':None,'ordinary_bad_target_D':4,'new_lower_bound':False,
'actual_D_scope':'Published672/2352simple7regularsourceidentityclosedR4=672isoneknownsourcereproduction,notnewgraphresult. All672actualrightmatchingU_tcrosssetsfailD4;no1344candidateorordinarycandidateBFS/fresh/Lean/ARIS.',
'outcome_class':'ROOT_ACCEPTED_COMPLETE_NO_FIXED_SAMPELS672_ALL_RIGHT_MATCHINGS',
'scope':'FixedpublishedSampels672CayleysourcewithactualRIGHTlaw(a,b)(c,d)=(a+c mod6,b*39^c+d mod112),canonical112a+b(notauthorrawlabels),thefixedinverse-closedS7. Preservealloldedgesoftwocopies;matchingM_t(h)=h*t,allt∈H672. Theseareexactlyallleft-H-equivariantbijectionsforone-regular-orbitCayleysource;donotrequiretselfinverseorsourceR_tAut. All672completedNO. Savedphaseanalysisusesonlysame672storedrows,notnewparameters. Notarbitrarypointmatching,oldedgeedits/otherS/host/general8D4;notold684H342orK19domain.',
'distance_text':'新published RIGHT源canonical672/2352/degree7，identity闭R4=672仅复现。精确跨层endpoint集合U_t=union_(a+b<=3)S^a*t*S^b；≤4的三cross可消matching回退，源同步leftH作用使identity根完整。全部672t完整，0个U_t=H、0个1344候选。保存行诊断事前预测“六phase分别可满112但共享t有pair冲突”，实测六phase各最大106/112、各0局部满，预测被反驳；障碍已经是单层实际端点覆盖不足，不只是相容性冲突。原batch/保存行诊断/root处置累计1.645124787/10CPU，0新图/参数/Lean/candidateBFS/ARIS。',
'lesson_and_restart_condition':'STOPthisSampels672fixedS/allrighttranslationmatchingrule. Thephasepredictionwasrefutedratherthanrelabelledaspartialsuccess:eachindividualrelativephasealreadyfailsforall672t. No justificationforanotherparameterwindoworshared-tpaircompatibilitysearchwithsameS. SourceidentityR4reproductionandlocalphaseargmaxwitnessesarenotnewconstructionresults.',
'restart_condition':'Onlya newlyauthorizedboundedquestionwithmeaningfullychangedsource/generator/edge/matchingrule;noautomaticothert/solver/window/S/action/source. Noold684K19timerresumed.',
'unclosed_gap':'Arbitrarynon-equivariantmatching,oldedgechanges,otherS/host/helperrulesandgeneral8D4remainunexcluded. No1344graphwasgenerated/accepted/formalized. Relativephaseargmaxonlywitnesses106not112;nofullphasewitnessexistsinthisfinitefamily. Sourcecanonicallabelsareexplicitlynewrecipecoordinates,notauthorrawbinding. GoalACTIVE/oldN8n61PAUSED;9D4readonlygateisnotthisnode.',
'positive_guarantees':[
'ActualsourceusespublishedRIGHTlawandfixedS7,notold684laworleftmultiplicationconvention. SourceidentityclosedR4=672isrecordedseparatelyasreproduction,withnonewgraphcount.',
'U_t=union S^a*t*S^bfor a+b<=3recordsactualendpointsandall≤4crossroutes,notwalkcapacityorjustrightshiftprism. SynchronousleftHactsonthejoinedgraph,soidentitycrossrootcoversallrootswithinthisequivariantfamily.',
'Full672rightt-domainwascompletedoncewithallper-tcrosscoverage/firstmissingdataretained. tneednotbeaninvolutionorgraphautomorphism;reverseusesrightt^-1.',
'Phasepostprocessonlynormalizesstoredabsolutephasetorelative(targetphase-t.phase)mod6. Allsixmaxima106andzero112witnessesrefutethepreviousindividually-full/pair-incompatibleprediction.',
'OriginalRESULT/TERMINALphaseCPUvaluesremainhistorical;ROOTdisposition1.645124787includesdiagnosticandrootreadchargewithoutreset.'
],
'other_metrics':{
'new_graphs':0,'new_parameter_pairs':0,'new_Lean_instances':0,'new_independent_method_claims':0,'source_reproductions':1,'source_reproduction_not_new_result':True,
'source':{'group':source['group'],'law':source['operation'],'canonical_labels':source['canonical_labels'],'S7':source['S'],'n':672,'m':2352,'degree':7,'identity_closed_ball_counts':source['identity_closed_ball_counts'],'exact_word_endpoint_counts':source['exact_word_endpoint_counts'],'identity_R4':672},
'rightmatching_domain':{'full_domain':672,'checked':672,'exact_crossfull_hits':0,'mapping':'M_t(h)=h*t','all_leftH_equivariant_matchings':True,'t_involution_or_source_Aut_required':False,'actual_new1344_candidates':0},
'saved_phase_diagnostic':{'savedrows':672,'phase_size':112,'maxima':[106,106,106,106,106,106],'full112_t_counts':[0,0,0,0,0,0],'argmax_t':[p['first_max_witness']['t'] for p in diag['per_phase']],'phase_normalization':diag['normalization'],'preregistered_prediction':diag['prediction'],'prediction_supported':False,'minimum_incompatible_cardinality':1,'single_layer_failure_not_just_shared_parameter_conflict':True,'no_new_Ut_source_or_BFS_queries':True},
'original_native_CPU':.278501838,'original_stage_CPU':1.478501838,'saved_diagnostic_CPU':.016622949,'diagnostic_stage_CPU':1.545124787,'root_disposition_charge':.1,'final_case_CPU':1.645124787,'case_CPU_cap':10,'all_processes_terminal':True,'candidate_BFS_fresh_Lean_ARIS':0,'old684_K19_source_DP_reruns':0,'no_automatic_otherS_t_action_window':True,'same_Goal':'ACTIVE','old_N8_n61':'PAUSED','negative_Lean_required':False
},'evidence_paths':evidence}
row=common['normalize'](raw);row['goal']['baseline_date']=raw['baseline_date'];assert not common['capture'].screen(json.dumps(raw,ensure_ascii=False))
rowfile=S/'SOURCE672_RIGHTMATCHING_FULL_DOMAIN_TERMINAL_20261102_ROW.json';rowfile.write_text(json.dumps(raw,ensure_ascii=False,indent=2)+'\n')
helper=common['helper'];helper.rebuild_index=lambda *_a,**_kw:None;helper.rebuild_query_pack=lambda *_a,**_kw:None
with (S/'SOURCE672_RIGHTMATCHING_FULL_DOMAIN_TERMINAL_20261102_NODE_CALLS.log').open('w') as out,contextlib.redirect_stdout(out):common['write_node'](row)
ledger['rows'].append(row);ledger['record_count']=454;ledger['updated_UTC']=now;ledger['input_counts'][str(rowfile.relative_to(ROOT))]=1
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n');node='experiments/'+slug+'.md'
summary=f'''\n\n{marker}
### {now} published Sampels672全rightmatching已NO：六phase单层各自不足

actualRIGHT source672/2352/7regular、identityR4=672仅为已知图复现，不加新图。全部672个M_t(h)=h*t以exact U_t=union S^a*t*S^b完整检查，无1344候选，关闭此固定source全leftH-equivariant匹配域；不排任意matching/改旧边/其他S或一般8D4。

只处理保存672行的后续诊断：原预测六phase分别可满112、但共享t有pair冲突，被实际六phase各max106/112且0局部满推翻。这里单层actualendpoint已不足，不能解释为只有共享参数不相容；局部argmax不是满覆盖见证。原batch/诊断/root费用全纳final1.645124787/10CPU，全部终态，不othert/S/action/window自动续。

453→454同一个实验记录，0新图/参数/Lean/candidateBFS/ARIS；153/43/47、savedmain105/4/global0保持。旧453rows与人工15格top原文保留，GoalACTIVE/旧N8n61暂停；9D4读取门不混入。

[{raw['title']}]({node})

'''
for name in files:
 text=original[name];assert marker not in text;cut=len(human[name]);text=text[:cut]+summary+text[cut:]
 if name=='index.md':
  m=re.search(r'^## Experiments \((\d+)\)',text,re.M);assert m;oldexp=int(m.group(1));text=text[:m.start(1)]+str(oldexp+1)+text[m.end(1):]
 (W/name).write_text(text);assert (W/name).read_text().startswith(human[name])
md=(W/'DDP_METHOD_LEDGER.md').read_text();assert marker not in md
md+=f'''\n\n{marker}
## {now} Sampels672全672 rightmatchings完整NO

| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |
|---|---|---|---|
| [{raw['title']}]({node}) | (8,4)；主表L{base}；目标1344，无新图 | sourceidentityR4=672只复现；672t exactU全NO。保存phase诊断各max106/112、0局部满，反驳“各自能满但pair冲突”预测。 | 只fixedSampelsRIGHTsource全leftH-equivariant右匹配，非任意matching/general8D4；原batch/诊断/root总1.645124787/10，STOP。[root终态](../{str((D/'ROOT_DISPOSITION.json').relative_to(ROOT))}) |

一个实验453→454，不把source复现/局部argmax记新成果。0新图/参数/Lean/候选BFS/ARIS，153/43/47保持；旧684/K19未重跑，9D4读取未计此节点。人工top保持，GoalACTIVE/旧N8n61暂停。
'''
(W/'DDP_METHOD_LEDGER.md').write_text(md)
after=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert after['record_count']==len(after['rows'])==454 and after['rows'][:-1]==oldrows;assert all(after[k]==v for k,v in counts.items())
receipt={'status':'PASS_ONE_SOURCE672_FULL_RIGHTMATCHING_AND_SAVED_PHASE_DIAGNOSTIC_TERMINAL_NODE','updated_UTC':now,'records_before':453,'records_after':454,'records_added':1,'new_experiment_id':slug,'canonical_node':str((W/node).relative_to(ROOT)),'row_path':str(rowfile.relative_to(ROOT)),'index_experiment_count_before':oldexp,'index_experiment_count_after':oldexp+1,'source_identity_R4':672,'source_reproduction_new_graph_count':0,'full_rightmatching_domain_checked':672,'full_crosscoverage_hits':0,'phase_maxima':[106]*6,'phase_size':112,'phase_local_full_counts':[0]*6,'preregistered_pair_conflict_prediction':'REFUTED_SINGLE_PHASE_ALREADY_NOT_FULL','final_case_CPU_including_root':1.645124787,'case_CPU_cap':10,'all_processes_terminal':True,'graph_parameter_Lean_method_increments':[0,0,0,0],'candidate_BFS_fresh_ARIS_runs':0,'arbitrary_matching_or_general8D4_not_excluded':True,'9D4_readgate_included':False,'old453_rows_preserved_exact':True,'human_top_blocks_preserved_exact':{p:True for p in files},'counts_unchanged':{k:after[k] for k in ['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs']},'full_rebuild_reimport':False,'new_math_solver_BFS_Lean_paid_hash_runs':0,'root_STATE_ROUND_pages_recovery_modified':False,'sameGoal':'ACTIVE','old_N8_n61':'PAUSED','sync_CPU_seconds':time.process_time()-st,'stop':True}
(S/'SOURCE672_RIGHTMATCHING_FULL_DOMAIN_TERMINAL_20261102_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False,indent=2))

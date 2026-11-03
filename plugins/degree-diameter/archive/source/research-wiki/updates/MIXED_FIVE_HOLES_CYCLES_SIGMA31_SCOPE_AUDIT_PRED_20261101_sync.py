from pathlib import Path
from datetime import datetime,timezone
import copy,json,subprocess,sys
R=Path(__file__).resolve().parents[2];W=R/'research-wiki';S='research/ddp/two_successful_methods_20261101/';P=S+'retained_edge_transfer/mixed_copy_cycle_sigma_31/PREDICTION_AND_SCOPE.md';PUB=S+'public_baseline_audit/Q4_NEW_ROLE_REPLICATION_WINDOW27_34_20261101'
B='MIXED_FIVE_HOLES_CYCLES_SIGMA31_SCOPE_AUDIT_PRED_20261101';now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,148,39,42)
rid='ddp-full-ovoid-spread-fixed-cap-singlehelper-rsquare-conditional-saturation-barrier-20261101';r=copy.deepcopy(next(x for x in L['rows']if x['id']==rid)['source_record']);m=r['other_metrics']
sigma_id='ddp-d9-d3-polarity585-involution-parallelclasses-20261027';sigma_note='research-wiki/experiments/'+sigma_id+'.md';sigma_data='research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/involution_probe/sigma.json'
pred=(R/P).read_text();assert '1750'in pred and '130'in pred and '120CPU'in pred and '10076'in pred
m['mixed_five_holes_copycycles_sigma31_experiment']=dict(status='ROOT_ACTUAL_DISPATCHED_ONE_FIXED_EXPERIMENT_FEASIBILITY_UNKNOWN',
    prior_exact_scope_audit='NO_MATCHING_STRICT_CLOSURE_LOCATED_IN_EXISTING420_METHOD_LEDGER',proof_of_feasibility_or_nonexistence_claimed=False,
    retained_closed_scopes=['uniformcomplete_r4_alloldUsaturated_cliqueKt','uniformcomplete_r4_alloldUsaturated_balancedKtt','oldliteral585max9allpreservedextensions'],
    why_prior_uniform_closure_does_not_apply='omitfourthcloneinfiveclasses(a_i,b0);130oldUarenolongersaturatedandareeligiblehelperpins;priorF_onlyrouteclassificationfails',
    prior_filled_q8_diagonal_b5_barrier_not_same_host_or_code=True,
    source='fixedliteral15factorAxsavedactual585factorB;wholeproductselfloopsremoved',published_source_n=8775,published_source_m=118300,published_source_reproduction_not_new_graph=True,
    inherited_sigma_node=sigma_id,inherited_sigma_data=sigma_data,sigma_edge_preservation2600_and_order2_inherited_not_retested=True,sigma_fixed_absolute_b0=0,
    omitted_full_copies=5,omitted_classes='wholeAabsoluterowindexsetatfixedBcolumnb0;(a_i,b0),i0..4',
    expected_retained_copy_vertices=10070,expected_mandatory_edges=151970,expected_freed_old_U_vertices=130,
    free_representatives=1620,copy_cycle_rule='C5normally,C4inthe5holeclasses',sigma_peer_rule='(a,b,j)matchedto(a,sigma(b),j)whenbnotfixed',
    expected_copycycle_peer_edges=1620,expected_sigma_peer_edges=800,expected_G0_n=10070,expected_G0_m=154390,expected_pin_pool=1750,
    expected_pin_spare_by_kind={'F_at_b0':3,'F_other':2,'freed_old_U':1},
    helper_graph='K6',helper_pin_budget_each=26,target_if_feasible=dict(Delta=31,D=3,n=10076),target_complete_graph_accepted=False,
    exact_model='forallhelperh,oldtargetv:ownpinsinclosedB2_G0(v)+otherhelperpinsinclosedB1_G0(v)>=1;actualcompleteG0includescycles_sigma;bothendpointsparebudgets',
    all_targets_constraints_not_badpair_objective=True,individualhelper_D3_prefix_claimed=False,jointbatch_current_graph_model=True,
    source_and_base_prep_CPU_budget=30,matrix_prep_imports_and_MILP_CPU_budget=120,solver_time_limit_seconds=90,workers=1,solver_threads=1,
    automatic_timer_seed_or_second_hole_peer_rule_restart=False,feasibility='UNKNOWN_BEFORE_ACTUAL_RESULT',
    public_comparison=dict(Delta=31,D=3,best_located_inherited_guarantee=10075,target_margin_if_legal=1,checked_date='2026-11-01',
        recipe='publishedq2xq8polarityproduct8775+4*325absoluteproductreplications',public_primary='https://arxiv.org/html/2608.27253v2#S7.SS7',saved_gate=PUB+'.md',global_exhaustion_or_priority_claimed=False),
    new_graph_parameter_Lean_increments=[0,0,0],in86_98_C_scope=False,old585_R2_Steiner_BFS_field_Lean_or_sigma_rechecks_this_sync=0,
    prediction=P,actual_outcome_not_inferred_from_capacity=True)
r['title']='固定uniform cap31两拓扑仍STOP；新五holes/copycycles/σ释放oldU的单规则实验在途UNKNOWN'
r['outcome_class']='OLD_FIXED_UNIFORM_CLOSURES_RETAINED_NEW_MIXED_COPY_RULE_EXACT_SCOPE_NOT_PREVIOUSLY_CLOSED_FEASIBILITY_UNKNOWN'
r['scope']+=' 新唯一mixedcopy实验明确省5个(a_i,b0)class的第四clone，释放130原U为可直接helperpin，再固定C5/C4及旧σ matching、K6helpers；它不满足旧uniformcomplete/allU饱和/F-only前提，因此旧clique/Ktt严格关闭保留而不自动套新规则。已查现ledger未定位精确范围旧strictclosure，不能据此预报可行。'
r['unclosed_gap']+=' 新mixed-copy当前仅ROOTdispatch/PRED，expectedG0=10070/154390/pool1750，目标10076/31/D3仍UNKNOWN；0portfolio/Lean。30CPU prep、120CPU模型含imports/solver90单thread一次，不授权secondpattern/续timer。'
r['lesson_and_restart_condition']+=' 本次重启基于具体连接规则改变：不建5完整clone让130oldU从31回30，允许以前被禁止的helper-U首步；copycycle修同class距离、σpeer修B列路线，然后用actualG0闭B2/B1约束全部点对与spare端点成本。它不是uniformclique重跑；先看这唯一有界模型实际终态，不从容量或no-old-closure推可行，不泛找模板。31公开门直接继承20261101已核10075，目标若合法仅多1/priorityUNKNOWN。'
e=[P,sigma_note,sigma_data,'research/ddp/polarity585_replication/source585.implicit_adj.txt',PUB+'.md',PUB+'.json'];assert all((R/x).is_file()for x in e)
r['evidence_paths']=list(dict.fromkeys(r['evidence_paths']+e));raw=W/f'updates/{B}_ROWS.json';raw.write_text(json.dumps([r],ensure_ascii=False,indent=2)+'\n');calls=[]
def call(*cmd):
 p=subprocess.run([str(x)for x in cmd],cwd=R,text=True,capture_output=True);calls.append(dict(command=[str(x)for x in cmd],returncode=p.returncode,stdout=p.stdout,stderr=p.stderr));assert p.returncode==0,(cmd,p.stderr,p.stdout);return p.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',raw).strip())
L=json.loads((W/'DDP_METHOD_LEDGER.json').read_text());assert (L['record_count'],L['validated_named_graph_examples'],L['validated_named_parameter_pairs'],L['complete_Lean_graph_instances'])==(420,148,39,42)
block=f'''<!-- {B} -->
# 当前：一个真实改规则的小参数mixed-copy试验在途，旧uniform clique/Ktt仍STOP

同Goal ACTIVE，ledger420仅复用[现机制/barrier](experiments/{rid}.md)1节点/0新行，148／39／Lean42、stage44／36、outside42／35、known43/main103_3/global0不变。精确审计现ledger未定位“五holes整A列+copycycles5/4+旧σ+释放oldU pin”旧严格关闭；唯一σ记录是已验sourceautomorphism，不是该product扩张排除。

新规则不建5个(a_i,b0)第四clone，释放130原U余度，固定copycycles与σpeers后预计G0=10070/154390、eligiblepool1750；6helpersK6目标若可行10076/cap31/D3。旧uniformcomplete假定alloldU饱和/helper只接F，本次改变这关键接口，不能套旧clique结论，旧clique/Ktt STOP原样保留。source/baseprep≤30CPU；actualcurrentG0闭B2/B1联合pins模型总≤120CPU/solver≤90/单thread，一次固定rule，UNKNOWN不预报可行。

31公开保证直接继承20261101门：publishedq2×q8+4×325=10075，若新图合法仅+1、priorityUNKNOWN；0新网查/数学/solver/旧585/R2/σ验证。本实验0图/参数/Lean，非86/98两目标Cscope；C672仍原livehandle待真实终态。

'''
p=W/'gap_map.md';assert B not in p.read_text();p.write_text(block+p.read_text())
p=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';p.write_text(p.read_text()+f'''

## {now} 精确ledger检查未见新mixed-copy范围旧strictclosure；以真实oldU余度改生成规则登记一次UNKNOWN试验

现ledger420只复用[原机制/barrier节点](experiments/{rid}.md)，0新方法行，148／39／Lean42、stage44／36、outside42／35、known43/main103_3/global0不变。针对mixed_copy/copycycle/sigma/fiveholes/释放U等查现ledger及experiment，未定位同一精确规则的严格关闭。旧σ命中[对合节点](experiments/{sigma_id}.md)是585actualsource的order2/固定0/其余ports配对/2600edges保持，不是mixedproduct排除。旧585max9任意保边结论保持停；旧filledq8/matching b≤5holes也不是此host/code。

最新[事前PRED](../{P})是有效改规则，不是重跑uniformclique：product325class完整r4的5个整A列(a_i,b0)第四clone不建，130 oldU得到1slot，F1620代表配C5正常/C4穴类及旧σmatching。预计G0=10070/154390、pool1750，F按b0/其余spare3/2、freedU spare1。此前strictclique/Ktt关键假设all8450oldU饱和、helpers只能F已破，因此旧关闭仍有效但不覆盖新K6规则。源S8775复现与G0都不当新portfolio，旧σ与585/R2/Steiner/BFS不重验。

六helperK6每点≤26pins。actualG0含预定peers，所有oldtarget/helper都加ownclosedB2+其他helperclosedB1覆盖及全部实际pin余度约束，是currentgraph联合覆盖、不是降低badpairs目标，也不声称六helper逐个添加每prefixD3。目标若实际feasible并fresh接受才可记10076/max31/exactD3，目前UNKNOWN。source/baseprep30CPU，matrix/imports/MILP总120CPU、solver90单thread一次，无seed/timer/secondpattern重启。31baseline直接继承20261101Q4window公开q2×q8source8775+4×325=10075，source/日期明确，通常不需网查；+1只条件差额、priorityUNKNOWN。0新图/参数/Lean，不属当前86/98 Cscope，不动旧冻包或根文件。C672保持同一原livehandle待真实终态，未重试。
''')
helper=R/'aris_repo/tools/research_wiki.py';call(sys.executable,helper,'log',W,'Exactledger420scopeauditfoundNOpreviousstrictclosurefor5holeswholeAcolumn+copycycles5_4+savedSigma+130freedoldUpins. Olduniformfullmandatoryallsaturatedclique_KttSTOPretained/notapplicablewhenhelperscanmeetfreedU;oldSigmaisverifiedsourceautomorphismnotclosure. OneROOTdispatchedmixedrulePREDG0_10070_154390_pool1750_K6target10076cap31UNKNOWN/prep30CPU/model120inclimports_solver90oneThread/noRestart. Cachedpublic31guarantee10075from20261101q2xq8rep4/noWeb.0graph_parameter_Leanincrements/notnew86_98Cscope/C672samependinghandle. Ledger420oneexistingrow148_39Lean42stage44_36unchanged/0math_solver_old585_BFS_sigmaChecks/rootedits_frozenwrites.')
call(sys.executable,helper,'rebuild_index',W);call(sys.executable,helper,'rebuild_query_pack',W)
(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
receipt=dict(status='PASS_MIXED_COPY_EXACT_SCOPE_AUDIT_NO_PREVIOUS_CLOSURE_LOCATED_ONE_RULE_PRED_WIKI_SYNC',updated_UTC=now,ledger_records=420,records_added=0,records_updated=1,named_legal_graphs=148,legal_parameter_pairs=39,stage_graphs=44,stage_pairs=36,complete_formula_Lean=42,new_graphs=0,new_Lean=0,new_frameworks=0,
    exact_old_strict_closure_located=False,old_uniform_clique_Ktt_STOP_retained=True,new_rule_breaks_old_all_U_saturation_F_only_interface=True,
    current_experiment='ROOT_DISPATCHED_FEASIBILITY_UNKNOWN_NOT_RECORD',expected_base=[10070,154390],expected_pin_pool=1750,conditional_target=[31,3,10076],inherited_public31=10075,inherited_gate_date='2026-11-01',priority='UNKNOWN',prep_CPU_budget=30,total_model_CPU_budget=120,solver_seconds=90,threads=1,
    evidence_paths_checked=len(e),actual_helper_calls=f'research-wiki/updates/{B}_HELPER_CALLS.json',math_BFS_solver_Lean_web_paidreview_runs_this_sync=0,root_owned_files_modified=False,frozen_packets_modified=False)
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n');print(json.dumps(receipt,ensure_ascii=False))

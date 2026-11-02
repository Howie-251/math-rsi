from pathlib import Path
from datetime import datetime, timezone
import copy
import json
import subprocess
import sys

R=Path(__file__).resolve().parents[2]
W=R/'research-wiki'
S='research/ddp/two_successful_methods_20261101/'
Q=S+'retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation/'
B='REPLICATION90_94_ACCEPTED150_41_LEAN44_A707_PENDING_20261101'
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def read(p):return json.loads((R/p).read_text())
keys=['record_count','validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances']
L=read('research-wiki/DDP_METHOD_LEDGER.json')
assert tuple(L[k]for k in keys)==(420,148,39,42)
ident='ddp-even-q8-opposite-gq-spread-fill-complete-pair-d80-327744-d81-342290-20261101'
row=copy.deepcopy(next(x for x in L['rows']if x['id']==ident)['source_record'])
m=row['other_metrics']
f=read(Q+'replication90_94_batch/formalization/FINAL.json')
t=read(Q+'multiplicity9_13_independent_acceptance/TERMINAL.json')
assert f['status']=='BOTH_ORIGINAL_D90_D94_KERNEL_AUDIT_EXTERNAL_ROLE_BINDING_PASS'
assert f['new_module_count']==8 and f['failed_attempts']==0 and not f['running']
assert f['typed_external_binding_rows']==84520 and f['actual_fresh_BFS_total']==136
assert t['status']=='PASS_BOTH_INDEPENDENT_G1_TARGETS' and t['all_children_terminal']
assert t['parent_parse_count']==1 and t['candidate_parses']==2 and t['old_BFS_roots']==0
new_cases=[]
evidence=[Q+x for x in ['replication90_94_batch/COMPLETION.md','replication90_94_batch/formalization/FINAL.json','replication90_94_batch/formalization/Q8DiagonalFill90Audit_attempt001.log','replication90_94_batch/formalization/Q8DiagonalFill94Audit_attempt001.log','multiplicity9_13_independent_acceptance/STRUCTURE_PROOF.md','multiplicity9_13_independent_acceptance/RESULT.json','multiplicity9_13_independent_acceptance/TERMINAL.json','multiplicity9_13_independent_acceptance/PARENT_4226_ROLE_ACTUAL_NEIGHBORS.tsv']]
for degree,n,edge_count,case,extra in [(90,380324,16942770,'multiplicity9_degree90',8),(94,397228,18311670,'multiplicity13_degree94',12)]:
    d=Q+case+'/'
    release=read(d+'ROOT_GRAPH_RELEASE.json')
    a=read(d+'independent_acceptance/RESULT.json')
    final=read(d+'formalization/FINAL.json')
    assert release['status']=='ROOT_ACCEPTED_COMPLETE_MATH_CONCRETE_LEAN_NEW_SCOPE_REVIEWS_PENDING_PRIORITY_UNKNOWN'
    assert (release['Delta'],release['n'],release['m'])==(degree,n,edge_count)
    assert release['updated_counts']==[150,41,44]
    assert a['status']=='PASS' and a['new_roles_bound']==4226*extra
    assert a['actual_lastblock_new_BFS_roots']==68 and a['hist_mismatches']==0
    assert final['no_user_certificate_premises'] and final['genuine_Walk_D3'] and final['not_D2']
    assert final['axioms']==['propext','Classical.choice','Quot.sound']
    assert final['label']=='Fin'+str(n) and not final['running']
    assert not any(g['n']==n for g in m['validated_graph_instances'])
    graph=dict(Delta=degree,D=3,n=n,m=edge_count,actual_diameter=3,
        mathematically_validated_complete_graph=True,complete_Lean_graph_instance=True,
        known_nonrecord=False,known_publicly_dominated=False,latest_global_record_confirmed=False,confirmed_publictable_improvement=False,
        best_located_public_lower_bound=release['public_formula_guarantee'],bounded_gain=release['located_margin'],public_comparison_status='EXCEEDS_CHECKED4225Delta_GUARANTEE_PRIORITY_GLOBAL_UNKNOWN',
        graph_path=d+release['complete_edge_file'],degree_histogram=a['degree_histogram'],
        source_n=346516,source_m=14204970,source_is_actual_G1_not83=True,source_all14204970_edges_retained=True,not_chained_from86_94_98=True,
        additional_role_blocks=extra,total_multiplicity=extra+1,new_roles_complete_N_bound=a['new_roles_bound'],
        actual_new_BFS_roots=68,unmeasured_new_roots=a['unmeasured_new_roots'],old_BFS_roots=0,actual_lastblock_hist_distributions=a['actual_hist_distributions'],
        allpair_every_prefix_old_G1_interior_Walk_proof=True,no_sample_orbit_extrapolation=True,
        complete_concrete_Lean_status=final['status'],concrete_original_target=final['target'],formal_final_receipt=d+'formalization/FINAL.json',formal_label=final['label'],
        formal_standard_axioms=final['axioms'],formal_user_certificate_premises=False,formal_ASCII_parser_or_Audit_eval_all_rows_claimed=False,
        external_A='ONE_NEW_EXPLICIT_TWO_TARGET_SCOPE_ACTUALLY_DISPATCHED_PENDING',external_A_thread='e4b6c102-1c55-4739-82e4-d281acc2e835',external_A_cell=707,
        external_B='NOT_DISPATCHED',external_fresh_C='NOT_DISPATCHED',external_B_C_complete=False,new_case_reviews_complete=False,
        old_three_or86_98_review_or_frozen_packet_inherited=False,independent_result=d+'independent_acceptance/RESULT.json',ROOT_release=d+'ROOT_GRAPH_RELEASE.json',public_priority='UNKNOWN',priority='UNKNOWN')
    m['validated_graph_instances'].append(graph)
    new_cases.append(dict(Delta=degree,D=3,n=n,m=edge_count,extra_G1_role_copies=extra,total_multiplicity=extra+1,new_roles_complete_N_bound=a['new_roles_bound'],
        actual_lastblock_BFS_roots=68,unmeasured_new_roots=a['unmeasured_new_roots'],old_BFS_roots=0,actual_hist_distributions=a['actual_hist_distributions'],public_guarantee=release['public_formula_guarantee'],bounded_gain=release['located_margin'],FINAL=d+'formalization/FINAL.json',ROOT_release=d+'ROOT_GRAPH_RELEASE.json'))
    evidence += [d+x for x in ['ROOT_GRAPH_RELEASE.json','PARAMETERS.json','RESULT.json','TERMINAL.json',release['complete_edge_file'],'independent_acceptance/PRED.md','independent_acceptance/NOTE.md','independent_acceptance/RESULT.json','independent_acceptance/TERMINAL.json','independent_acceptance/ALL_NEW_ROLE_BINDINGS.tsv','independent_acceptance/NON_D2_ACTUAL_LAST_HUB_WITNESS.json','formalization/FINAL.json','formalization/EXTERNAL_INPUT_BINDING.json']]
    evidence += ['formal/DegreeDiameter/Portfolio/'+f'Q8DiagonalFill{degree}{suffix}.lean' for suffix in ['Definitions','Inputs','Exact']]
    evidence += [f'formal/Q8DiagonalFill{degree}Audit.lean']

request=S+'reviews/REPLICATION90_94_A_REQUEST.json'
req=read(request)
assert req['threadId']=='e4b6c102-1c55-4739-82e4-d281acc2e835' and req['shared_calls']==1
assert req['explicit_targets']==[[90,3,380324,16942770],[94,3,397228,18311670]]
evidence.append(request)
assert all((R/x).is_file()for x in evidence)
m['replication90_94_pending_batch'].update(status='SUPERSEDED_BY_ROOT_ACCEPTED_MATH_AND_CONCRETE_KERNEL_BATCH',superseding_field='replication90_94_actual_batch',new_validated_graph_instances_added=2)
for g in m['replication90_94_pending_batch']['targets']:
    g.update(math_accepted=True,concrete_Lean_complete=True)
m['replication90_94_actual_batch']=dict(status='ROOT_ACCEPTED_BOTH_COMPLETE_MATH_KERNEL_AUDIT_BINDING_A707_PENDING_B_C_NOT_DISPATCHED',cases=new_cases,
    source='actualG1_346516_14204970_not83_86_94_98_chain',source_streams=1,candidate_streams=2,new_roles_complete_N_bound=84520,
    actual_lastblock_BFS_per_case=68,actual_BFS_total=136,unmeasured_new_roots=[33740,50644],old_BFS=0,allpair_every_prefix_source_interior_proof=True,
    producer_total_CPU=6.067463983,producer_CPU_budget=30,independent_total_CPU=t['total_CPU_seconds'],independent_CPU_budget=60,
    concrete_Lean_total_CPU=f['CPU_seconds'],concrete_Lean_CPU_budget=300,new_modules=8,all_first_PASS=True,failed_attempts=0,max_module_CPU=f['max_module_CPU_seconds'],
    standard_axioms=['propext','Classical.choice','Quot.sound'],user_certificate_premises=False,new_finite_geometry_or_old_module_recompile=0,all_local_processes_terminal=True,
    A=dict(status='ACTUALLY_DISPATCHED_ONE_NEW_EXPLICIT_TWO_ORIGINAL_SCOPE_PENDING',cell=707,store='endpoint90_94_A_actual',thread=req['threadId'],shared_calls=1,request=request,old_case_PASS_inherited=False),
    B=dict(status='NOT_DISPATCHED'),distinctfreshC=dict(status='NOT_DISPATCHED'),priority='UNKNOWN',global_record_certified=False,
    public_guarantees=[380250,397150],bounded_gains=[74,78],if_filled_H_and_ordinarycopy_public_gains=[9,13],if_same_rule_public_gains=[0,0],
    four_endpoint_expert_lightpage=dict(status='IN_PREPARATION_BY_GQ_NO_EXISTING_FILE_CLAIMED',ZIP_created=False),completion=Q+'replication90_94_batch/COMPLETION.md')
m['future_window84_98_public_gate_only'].update(status='FOUR_SELECTED_ENDPOINTS_ALL_ACTUAL_MATH_KERNEL_COMPLETE_OTHER11_ONLY_PUBLIC_COMPARISON',completed_selected_endpoints=[86,90,94,98],pending_root_acceptance_endpoints=[],new_endpoints_accepted=2,active_queue=0,actual_graphs_or_queue=4,actual_math_kernel_graphs=4,remaining_selected_not_dispatched=[],other11caps_produced=0,other11caps_queued=0)
m['replication86_98_actual_batch']['not_dispatched']=[]
m['new_named_complete_graphs']=len(m['validated_graph_instances'])
m['new_Lean_instances']=len(m['validated_graph_instances'])
m['new_parameter_pairs']=[list(x)for x in sorted({(g['Delta'],g['D'])for g in m['validated_graph_instances']})]
m['accepted_q8_terminal_graphs']=[g['n']for g in m['validated_graph_instances']]
m['all_row_graph_instances_complete_Lean']=True
m['all_row_original_A_B_distinctfreshC_complete']=False
m['all_local_formal_processes_terminal']=True
m['completed_Lean_and_A_B_C_scope']='all9actualq8roworiginalsmath_kernelcomplete;prior7A_B_distinctfreshCcomplete;new90_94A707pending_B_Cnotdispatched;smallhelperandmixedexcluded'
m['all_local_formal_processes_scope']='nineactualq8originalsallterminal;noactiveNativeCompute;onlynew90_94externalA707pending'
row['title']='90/380324与94/397228已数学/kernel验收，q8同机制九实例；150/41/Lean44，新A707在途且B/C未派'
row['outcome_class']='NINE_ACTUAL_Q8_INSTANCES_MATH_KERNEL_COMPLETE_90_94_NEW_REVIEW_SCOPE_PENDING'
row['scope']+=' 当前90/94已由root完整独验和无前提具体Fin原目标/Audit验收，新增两图/两参数/两Lean到150/41/44；同一机制不新method。新A707明确两原目标scope实际派出，B/freshC未派，旧7图PASS不继承。'
row['distance_text']+=' root实际接受90/380324/16942770(r8)与94/397228/18311670(r12)，源固定G1/346516而非98链式。oneproducer6.067463983/30、fresh9.240740672/60，各源parse1/候选各1，完整84520newN绑定。每case实际仅68预选lastblock roots逐预测hist匹配，其他33740/50644new及0old BFS靠完整literalN与oldG1内点真Walk/prefix证明，不称全根BFS。8新Lean首编PASS19.453559765/300、max2.860851，原始FinalClaim/final_claim显式Fin380324/397228/WalkD3/nonD2/std3无证书前提；0新finite/旧module重编，全部本地process终态。新A707同e4thread一次明确两tuple在途，B/C未派；四端点轻量专家页制作中不冒已存在/ZIP。公开margin74/78，Hfillpublic残9/13、同规则public归0，priorityUNKNOWN。'
row['lesson_and_restart_condition']+=' 原finitewindow四个selected86/90/94/98现都实际math/kernelcomplete，其他11cap仍只公开比较/0graph/queue。新90/94下一节点是actualA/B/distinctfreshC，不再生产该window其他cap或继承旧scope；原148/39/42和pending仅保历史，当前150/41/Lean44。专家新四端点页仍制作中，旧146snapshot包与86/98未冻结轻量稿不修改。小31两个试验保持各自已收束scope，不在两新目标外审范围。'
row['evidence_paths']=list(dict.fromkeys(row['evidence_paths']+evidence))
raw=W/f'updates/{B}_ROWS.json';raw.write_text(json.dumps([row],ensure_ascii=False,indent=2)+'\n')
calls=[]
def call(*cmd):
    p=subprocess.run([str(x)for x in cmd],cwd=R,text=True,capture_output=True)
    calls.append(dict(command=[str(x)for x in cmd],returncode=p.returncode,stdout=p.stdout,stderr=p.stderr))
    assert p.returncode==0,(cmd,p.stderr,p.stdout)
    return p.stdout
print(call(sys.executable,R/'research/ddp/more_graphs_20261027/sync_additional_probes.py',raw).strip())
L=read('research-wiki/DDP_METHOD_LEDGER.json');assert tuple(L[k]for k in keys)==(420,150,41,44)
block=f'''<!-- {B} -->
# 当前：90/94已数学与具体kernel验收，150／41／Lean44；新A707在途，B/C未派

同Goal ACTIVE，ledger420只复用[q8现机制](experiments/{ident}.md)，0新method/ledger行。当前150合法named／41参数、stage46／38、具体Lean44、outside44／37；known43/main103_3/global0不变，不称150全球record。

新90/380324/16942770(r8)与94/397228/18311670(r12)实际源G1/346516，非98链式，root已读完整fresh NOTE/RESULT/TERM/STRUCTURE_PROOF及两原目标/Audit/std3/显式Fin无前提收据。producer6.067463983/30、fresh9.240740672/60，全部84520newN绑定；每case仅68lastblock actual BFS逐hist匹配，未测33740/50644新根和0oldroot由full literalN+oldG1内点真Walk/prefix覆盖。8新Lean全首PASS19.453559765/300、max2.860851，旧PASS/finite不重编，localprocess全terminal。

新A707/storeendpoint90_94_A_actual已实际派出，同A e4thread一次新两原目标scope，在途；B/freshC未派，旧86/98/三图PASS不继承。四selected86/90/94/98都已math/kernelcomplete，另外11cap仅publiccomparison/0graph/queue。四端点轻量专家页由gq制作中，未冒存在，0ZIP/旧包不改。4225Δ公开保证给新两图+74/+78，若Hfillpublic残+9/+13、同规则public归0，priorityUNKNOWN。小31试验状态原样继承，不纳新外审scope。

'''
gap=W/'gap_map.md';assert B not in gap.read_text();gap.write_text(block+gap.read_text())
comments=W/'DD82_PROGRESS_AND_COMMENTS_20261018.md';comments.write_text(comments.read_text()+f'\n\n## {now} 两个剩余分散端点实际验收到150/41/Lean44\n\n'+block.split('\n\n',1)[1])
helper=R/'aris_repo/tools/research_wiki.py'
call(sys.executable,helper,'log',W,'Rootactualaccepted90_380324_16942770r8and94_397228_18311670r12fromG1346516not98chain_mathFreshoriginalFinFinalClaimKernelAuditStd3NoPremisescomplete;producer6.067463983of30fresh9.240740672of60_parent1candidateeach1_all84520fullNbinding_only68lastblockBFSpercase_unmeasured33740_50644old0_allpairprefixoldG1interiorTrueWalk;8newLeanfirstPASS19.453559765of300max2.860851_oldfiniteModulesnotrecompiled_alllocalterminal. Existingq8oneRow9validatedinstances_ledger420_150named41pairsLean44stage46_38outside44_37known43main103_3global0. NewA707e4threadshared2originalscopeACTUALDISPATCHpending_BCnotdispatched_noinheritance. Fourselected86_90_94_98mathkernelcomplete_other11publiconly0graphsqueue. Expert4lightpagepreparing_notexistenceclaim0ZIPoldpacketunchanged. Publicmargin74_78Hfillpublic9_13samerule0priorityUNKNOWN. No31scopeExpansion_math_graph_BFS_Lean_solver_web_paidcalls_rootowned_frozenwrites.')
call(sys.executable,helper,'rebuild_index',W);call(sys.executable,helper,'rebuild_query_pack',W)
(W/f'updates/{B}_HELPER_CALLS.json').write_text(json.dumps(calls,ensure_ascii=False,indent=2)+'\n')
node=W/'experiments'/f'{ident}.md';assert row['title']in node.read_text()
assert len(calls)==4 and all(x['returncode']==0 for x in calls)
receipt=dict(status='PASS_EXISTING_Q8_MECHANISM90_94_ROOT_ACCEPTED150_41_LEAN44_NEW_A707_PENDING',updated_UTC=now,ledger_records=420,records_added=0,records_updated=1,
    named_legal_graphs=150,legal_parameter_pairs=41,complete_formula_Lean=44,stage_graphs=46,stage_pairs=38,outside_graphs=44,outside_pairs=37,known_publicly_dominated=43,main103_3=True,global_records=0,
    newly_accepted_graphs=[dict(Delta=90,n=380324,m=16942770),dict(Delta=94,n=397228,m=18311670)],new_Lean=2,new_parameter_pairs=2,new_methods=0,
    actual_q8_row_graph_instances=9,all9math_kernel_complete=True,prior7external_complete=True,new2A707_pending=True,new2B_freshC_not_dispatched=True,
    producer_CPU=6.067463983,fresh_CPU=9.240740672,new8module_Lean_CPU=f['CPU_seconds'],new_roles_complete_N_bound=84520,actual_BFS_per_case=68,unmeasured_new_roots=[33740,50644],old_BFS_roots=0,
    four_selected_endpoints_complete=[86,90,94,98],other11caps_graph_queue=0,four_endpoint_lightpage='IN_PREPARATION_NO_EXISTING_FILE_CLAIM',new_ZIP=0,
    evidence_paths_checked=len(evidence),static_scope_check='PASS_existingNode_fourActualHelperCalls_counts_and_evidencePaths',actual_helper_calls=f'research-wiki/updates/{B}_HELPER_CALLS.json',
    math_graph_BFS_Lean_solver_web_paid_runs_this_sync=0,small31_scope_expanded=False,root_owned_files_modified=False,frozen_packets_modified=False)
(W/f'updates/{B}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False))

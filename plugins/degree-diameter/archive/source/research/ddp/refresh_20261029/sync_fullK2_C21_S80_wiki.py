"""Record actual full-K2 terminal and two new affine-fiber experiment scopes."""
from pathlib import Path
from datetime import datetime,timezone
import copy
import importlib.util
import json
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
WIKI=ROOT/'research-wiki'
NOW=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def load(relative):
    return json.loads((HERE/relative).read_text())


def evidence(folder):
    return [str(p.relative_to(ROOT)) for p in sorted((HERE/folder).rglob('*'))
        if p.is_file() and p.suffix in {'.md','.json','.py','.cpp'} and '__pycache__' not in p.parts]


full=load('d14_K2_allgroup_fulltarget/SOLVER_TERMINAL.json')
fullmodel=load('d14_K2_allgroup_fulltarget/MODEL.json')
recovery=load('d14_K2_allgroup_fulltarget/METADATA_RECOVERY_RESULT.json')
c21=load('c21_flag_uniform100_route_gate/RESULT.json')
s80=load('f5_fiber80_structure_gate/RESULT.json')
c25=load('f5_fiber80_controller25/MODEL.json')
assert full['status']=='UNKNOWN' and full['returncode']==0 and full['actual_solver_calls']==1
assert full['running'] is False and full['pending']==[]
assert (fullmodel['variables'],fullmodel['clauses'],fullmodel['exact_groups'])==(100492,385396,3589)
assert fullmodel['complete_all_groups'] is fullmodel['complete_all_targets'] is True
assert recovery['status']=='COMPLETE_METADATA_RECOVERED_WITHOUT_REBUILD'
assert recovery['native_builder_restarts']==0 and recovery['CNF_modified'] is False
assert c21['control_distance3_ordered_pairs']==168 and c21['every_distance3_pair_words']==2
assert c21['minimum_cross_intersection']==1 and c21['large_graphs_generated']==0
assert s80['fiber_size']==80 and s80['universal_six_image_union_upper_bound']==76
assert (c25['all_variables'],c25['clauses'],c25['solver_calls'])==(333343,1129292,0)
proof=(HERE/'f5_fiber80_structure_gate/PROOF.md').read_text()
assert '## 9 后续独立纸面排除' in proof and 'N≤24' in proof
before=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count']==len(before['rows']) and before['record_count'] in {374,376}
existing={r['id']:r for r in before['rows']}
id14='ddp-d14-d5-literal94186-allfree-k2-cooperative-cover-20261029'
id21='ddp-c21-fano-flag-uniform100-affine-plane-deletion-route-obstruction-16d3-20261030'
id80='ddp-f5-fiber80-two-type-normal-scaling-chart-rigidity-16d3-20261030'
new_records=sum(identifier not in existing for identifier in [id21,id80])
k2=copy.deepcopy(existing[id14]['source_record'])
fullvariant=dict(
    label='all3589_equivalence_groups_complete94186_two_side_target_model_single300s_UNKNOWN_20261030',
    status='UNKNOWN_TERMINAL',all_groups=3589,original_free_ports=3685,
    additional_LP_support_restriction=False,
    exact_group_reconstruction_preserves_original_allfree_K2=True,
    selector_variables=7178,variables=100492,clauses=385396,CNF_bytes=631293647,
    original_two_side_rows=188372,exact_unique_coverage_rows=188138,
    exact_duplicate_rows=234,capacity1_groups=3480,capacity2_groups=109,side_limit=13,
    generator_runs=1,native_builder_succeeded=True,
    initial_driver_metadata_filename_collision=True,
    metadata_recovery_runs=1,native_builder_restarts=0,CNF_modified_by_recovery=False,
    actual_solver_calls=1,solver_option='-t300',solver_returncode=0,
    solver_CPU_seconds=full['solver_CPU_seconds'],
    charged_whole_CPU_seconds=full['charged_whole_CPU_seconds'],
    measured_whole_CPU_lower_bound=full['measured_whole_CPU_lower_bound'],
    preparation_CPU_reservation=90,measured_preparation_components=full['recorded_prepare_CPU_seconds'],
    original_driver_self_CPU_missing=True,exact_measured_whole_CPU_claimed=False,
    whole_CPU_budget=420,observation_timeouts=60,same_PID_waited_to_exit=True,
    SAT_candidates=0,source_graph_reads=0,BFS_runs=0,graphs_generated=0,
    running=False,automatic_continuation=False,pending=[],
    K2_family_excluded=False,
    current_terminal='research/ddp/refresh_20261029/d14_K2_allgroup_fulltarget/SOLVER_TERMINAL.json')
variants={v['label']:v for v in k2['variants']}
variants[fullvariant['label']]=fullvariant
k2['variants']=list(variants.values())
k2['outcome_class']='FULL_ALLGROUP_FULLTARGET_INTEGER_UNKNOWN_FRACTIONAL_FEASIBLE'
k2['failure_or_result']='标准分数全目标精确可行与391受限整数UNKNOWN保留。后续恢复全部3589等价组、全部94186双侧目标，7178selectors/100492vars/385396clauses、631293647字节完整CNF；单次native成功后仅元数据命名冲突，以一次只读恢复完成，无重建。唯一-t300调用UNKNOWN/code0，solver300.091586CPU、chargedwhole390.163813472（含90prepare保守reserve），measuredwhole仅下界303.579241987（原driver self CPU缺失），0候选/图/BFS/source读，已停止，不排K2。'
k2['other_metrics'].update(
    current_numerical_status='FULL_ALLGROUP_FULLTARGET_INTEGER_UNKNOWN',
    current_running=False,allgroup_complete_groups=3589,allgroup_complete_targets=94186,
    allgroup_selector_variables=7178,allgroup_variables=100492,allgroup_clauses=385396,
    allgroup_CNF_bytes=631293647,allgroup_solver_calls=1,
    allgroup_solver_CPU_seconds=full['solver_CPU_seconds'],
    allgroup_charged_whole_CPU_seconds=full['charged_whole_CPU_seconds'],
    allgroup_measured_whole_CPU_lower_bound=full['measured_whole_CPU_lower_bound'],
    allgroup_prepare_reservation=90,allgroup_initial_driver_self_CPU_missing=True,
    allgroup_metadata_recovered_without_rebuild=True,
    allgroup_latest_integer_result='d14_K2_allgroup_fulltarget/SOLVER_TERMINAL.json',
    fixed_K2_family_excluded=False)
k2['lesson_and_restart_condition']='391分数支撑不是整数解的无损限制，因此本轮真正恢复全部等价组和全部双侧target，改变了生成域而非续受限pool。完整模型仍唯一300CPU UNKNOWN，停止，不作全K2无解结论。native构建完成后的元数据错误只做一次原样恢复；CPU缺失明确用prepare90reserve计费，不能伪造精确aggregate。后续需要具体整数覆盖/连接结构，不因未成功自动加时。'
k2['unclosed_gap']='该literal94186的完整allfree K2整数问题仍UNKNOWN，全部3589组/94186双侧target模型已终态停止；分数完整可行不推出整数存在。391受限pool和旧稀行结果为历史，当前整数终态读allgroup SOLVER_TERMINAL，不从prepared MODEL恢复RUN。'
k2['report_paths']=list(dict.fromkeys(k2['report_paths']+evidence('d14_K2_allgroup_fulltarget')))

c21row=dict(
    id=id21,title='Fano flag C21 uniform100: two short words and intersecting cross deficits exclude the specified2100 rule',
    family='four-label affine route-chart lifts',idea_family='idea:ddp-q3-three-step-plane-pencil31',
    date='2026-10-30',record_type='conditional-affine-fiber-generation-rule-paper-obstruction',
    target_Delta=16,target_D=3,savedL=1920,baseline_date='2026-10-29',
    n=dict(actual=None,hypothetical=2100),actual_graph_Delta=None,actual_D=None,
    ordinary_bad_unordered_pairs=None,outcome_class='LOCAL_PAPER_EXCLUDED_SPECIFIED_C21_UNIFORM100_RULE',
    scope='Fixed21Fano-flagcontroller(theHeawoodlinegraph),oneaffineplanedeletedfromeachF5^3fiber,retained100points;edge-specificaffinechartsand1Dnoiseallowed,butnoiseistransversetotargetnormaloneveryedge. Onlythisuniform100generativeruleisexcluded;notarbitraryC21retentionornonuniform/nonplanar/noisechanges.',
    failure_or_result='All168ordereddistance3controllerpairshaveexactly2words. Rank3wordcovers16pointsofeachretained25pointnormalplane,missingacross;anytwocrossesintersect. Rank<=2wordcoversatmost5pointsofthatsliceundertransversality. ThusallrankcombinationsofbothwordsfailD3,no2100graphgenerated. Smallcheck375crosses/70500pairs/minintersection1,0.016508896CPU.',
    positive_guarantees=['Thewholefixedplane-deletiondomainispaper-excludedwithoutenumeratingplanechoices.',
        'Controllerandcrosschecksarelocalinputcalibration,notafinalgraphorlargegraphBFS.',
        'Old105pointA/B/Cflagoperatorgraphisadifferentobjectandwasnotrerun.'],
    other_metrics=dict(controller_vertices=21,controller_degree=4,
        controller_distance3_ordered_pairs=168,words_per_distance3_pair=2,
        retained_points_per_fiber=100,hypothetical_graph_order=2100,
        full_rank_word_slice_coverage=16,low_rank_word_slice_upper=5,
        affine_crosses=375,cross_pairs_checked=70500,minimum_cross_intersection=1,
        local_CPU_seconds=c21['CPU_seconds'],solver_calls=0,large_graphs_generated=0,
        large_graph_BFS=0,plane_choices_enumerated=0,
        external_review_status='NOT_YET_COMPLETED',Lean_formalized=False,new_record=False),
    variants=[dict(label='all168_distance3_pairs_two_words_and_all375_crosses_local_gate_20261030',
        status=c21['status'],controller_vertices=21,ordered_distance3_pairs=168,
        two_words_each=True,crosses=375,cross_pairs_including_diagonal=70500,
        minimum_cross_intersection=1,CPU_seconds=c21['CPU_seconds'],
        solver_calls=0,final_graphs=0)],
    lesson_and_restart_condition='Twoavailablecontrolwordsarenotenoughwhenbothsuffersystematicintermediateplaneexclusions;theirresidualdeficitcrossesmustintersect. StopthisentirefixedC21uniform100rule,notjustoneplaneselection. Anyfuturechangemustaltertheshortwordbudgetordeletions/noisetransversalityassumptions,notrepeatthisdomain.',
    unclosed_gap='GeneralN(16,3),arbitraryC21lifts/nonuniform/nonplanardeletionsandotherchart-noiserulesremainopen. PaperobstructionnotexternallyreviewedorLeanformalized.',
    report_paths=evidence('c21_flag_uniform100_route_gate'),
    hardware_raw='singleCPU,smallcontrollerand25pointlinegeometry',
    duration_raw='0.016508896CPU;no2100pointgraphgeneration')

s80row=dict(
    id=id80,title='S80 two-type normal-scaling affine fibers: local76 gate and tightN25 rigidity imply order<=1920',
    family='four-label affine route-chart lifts',idea_family='idea:ddp-q3-three-step-plane-pencil31',
    date='2026-10-30',record_type='new-fiber-chart-framework-local-paper-rigidity-with-unrun-controller-model',
    target_Delta=16,target_D=3,savedL=1920,baseline_date='2026-10-29',
    n=dict(actual=None,hypothetical=2000),actual_graph_Delta=None,actual_D=None,
    ordinary_bad_unordered_pairs=None,outcome_class='LOCAL_PAPER_FRAMEWORK_N_AT_MOST24_CONTROLLER_SOLVER_NOT_STARTED',
    scope='NewS80={a=x-y!=0,b=z!=0}inF5^3,80points,fourfixeddirectionsandinversepairedAports0/1andBports2/3. Astepsscaleonlypassivenormalb,Bstepsscaleonlypassivenormala;activeF5*normalhasfourchoices. Reverse-compatiblechartsneednotpreserveS80asset. Onanysimplequarticcontroller,the16regularliftcannotD3withN>=25undertheseexacttwo-typeconditions.',
    failure_or_result='76boundforcesnontriangleedgeinC4;wordbudgetN<=29-2t-c4forcesN<=27,thenN26triangledivisibilityandN27C4obstructionleave25. N25hasat2/c40rootwithtight8dist2+12dist3supply;allnonneighborNB2mustmixed,forcingpureA/pureBtriangles. Choosebothendpointnormalsoutsidethreepossiblelevels:all5hiddenfiberpointsaremissed. ThusN<=24,order<=1920. Localcalibration0.025032128CPU;C25necessaryCNF333343/1129292prepared2.399239534CPUbutstoppedbeforeanysolver.',
    positive_guarantees=['Thischangesfiber/charts/controllerandisnotarelabelingoftheclosed3750inducedproblem.',
        'TheglobalframeworkboundcomesfromPROOFsection9,notfromthesinglechart43/55imageunions.',
        'TheunrunfixedC25motifmodelisnecessaryonly;itwasnotreportedUNSAT.'],
    other_metrics=dict(fiber_size=80,neighbors_per_port=4,conditional_lift_degree=16,
        controller_degree=4,hypothetical_controller_N25_order=2000,
        universal_backtrack_union_upper=76,
        control_budget='N<=29-2t-c4',framework_controller_upper_bound=24,
        framework_order_upper_bound=1920,upper_bound_attained_claimed=False,
        local_chart_calibration_CPU_seconds=s80['CPU_seconds'],
        reverse_pairs_checked=1280,backtrack_images_checked=1920,
        sampled_chart_six_union_histogram={'55':160,'43':160},
        all_accepted_charts_preserve_S80_as_a_set_required=False,
        root_degree5_affine_local_static_support=True,external_review_status='PENDING',
        Lean_formalized=False,controller_lifts_generated=0,SAT_calls=0,
        large_graph_BFS=0,general_N16D3_upper_bound_claimed=False,
        nonnormal_preserving_charts_or_other_fibers_excluded=False,new_record=False),
    variants=[
        dict(label='S80_line_and_one_admissible_chart_quadruple_local_calibration_20261030',
            status=s80['status'],fiber_size=80,per_port_degree=4,
            local_CPU_seconds=s80['CPU_seconds'],universal_six_image_upper=76,
            sample_43_or55_union_not_a_universal_obstruction=True,
            solver_calls=0,large_graphs=0),
        dict(label='N25_t2_tight_route_inventory_pure_triangles_hidden5_obstruction_20261030',
            status='LOCAL_PAPER_FRAMEWORK_EXCLUDED_ABOVE1920_EXTERNAL_PENDING',
            mixed_three_word_hidden_values_per_fixed_normals_at_most=4,
            t2root_dist2_targets=8,t2root_dist3_targets=12,
            t2root_NB3_nonneighbor_supply=32,
            same_type_NB2_forbidden_at_nonadjacent_targets=True,
            two_triangles_forced_pure_A_and_pure_B=True,
            excluded_normal_levels_per_coordinate_at_most=3,
            nonzero_normal_choices=4,hidden_targets_entirely_missed=5,
            controller_N25_excluded=True,framework_N_at_most24=True,
            additional_computation_or_solver=0,external_review_status='PENDING'),
        dict(label='C25_fixed_three_triangle_chain_plus6K3_necessary_capacity_model_prepared_then_stopped_20261030',
            status=c25['status'],controller_order=25,fixed_edges=27,
            extra_edge_variables=233,variables=333343,clauses=1129292,
            complete_only_within_fixed_motif=True,
            controls_necessary_not_sufficient_for_S80=True,
            prepare_CPU_seconds=c25['prepare_CPU_seconds'],
            actual_solver_calls=0,charts_constructed=False,large_graphs=0,
            planned_solver_not_launched_due_to_new_rigidity=True)],
    lesson_and_restart_condition='Theinitial76andN25necessaryinventorydidnotconstructalift. Tightwordaccountingatamandatoryt2rootforcesport-typepurity,thenownfiberhiddenvaluesgivetheactualobstruction. StopthisexactS80normal-scalingframeworkandunrunC25solver;changingonlycontrollercyclesortimerscannotfixit. OtherS/normalmixing/noiserelationsremainoutside.',
    unclosed_gap='Thisframeworkcannotexceed1920,butgeneral16degreeD3graphs,otherfiberS,passive-normalmixing/nonuniformorotherrelationsremainopen. Newrigidityislocalpaperproofwithexternalreviewpending,notLean;nogenerated2000graph.',
    report_paths=evidence('f5_fiber80_structure_gate')+evidence('f5_fiber80_controller25'),
    hardware_raw='singleCPU,125pointlocalcalibrationandCNFpreparationonly',
    duration_raw='Local0.025032128CPU;fixedC25CNFprepare2.399239534CPU;rigiditypaper0newsolver')

rows=[k2,c21row,s80row]
report='''# 完整K2与两个新fiber/controller生成域

14度K2实际恢复全部3589组和全部94186双侧targets：100492变量/385396子句、631293647字节。native一次完整成功后元数据文件名冲突，只读恢复一次，没有重建CNF。唯一-t300 UNKNOWN/code0，300.091586solverCPU；保守chargedwhole390.163813472含prepare90reserve，measuredwhole仅下界303.579241987，原driver self缺失不能填成精确总计。0候选/source读/BFS/图，停止不排K2；preparedMODEL不能覆盖SOLVER_TERMINAL。

C21为Fano旗/Heawood线图的新controller，不是旧105点旗算子。其168个距离3有序对均只有2word；uniform100单plane删除的rank3word每normal平面覆盖16、缺cross，两个cross必相交；低秩slice≤5，故全指定机制纸面排除。仅0.016508896CPU小检查、0大图/solver，未外审。

新S80=F5×(F5*)²的两type normal-scaling框架先由76门和word预算缩到N25；新PROOF§9的t2 tight→mixedNB2→pureA/Btriangles→同fiber5hiddenmiss最终排N25，N≤24、阶数≤1920。不是一般N16上界，不排其它S/normal混合/非uniform规则。local0.025032128CPU；C25必要模型333343/1129292准备2.399239534CPU，因rigidity未启动solver，不能冒UNSAT。外审待回执。

为两个实际不同生成域新增2条aggregate实验，沿用既有affine-route-chart idea/family；C25只是S80变体，不另method。原K2一行加变体，ledger376是实验/来源记录而非方法数；合法104/4、confirmed103/3、Lean1不变。15度K2仅派发、尚无actual回执，不记RUN。专家23:55冻结不重包，root未改；最后query等root新恢复phase与最终结果。
'''
report_path=HERE/'FULLK2_C21_S80_WIKI_REPORT.md'
spec=importlib.util.spec_from_file_location('capture_filter',ROOT/'aris_repo/tools/capture_filter.py')
capture=importlib.util.module_from_spec(spec);spec.loader.exec_module(capture)
assert not capture.screen(report)
report_path.write_text(report)
for row in rows:
    row['report_paths']=list(dict.fromkeys(row['report_paths']+[str(report_path.relative_to(ROOT))]))
    assert all((ROOT/p).exists() for p in row['report_paths'])
    assert not capture.screen(json.dumps(row,ensure_ascii=False))
pending=HERE/'FULLK2_C21_S80_WIKI_ROWS.json'
pending.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
command=[sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(pending)]
run=subprocess.run(command,cwd=ROOT,text=True,capture_output=True,check=True)
after=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count']==len(after['rows'])==before['record_count']+new_records==376
for key in ['validated_graph_examples_including_novelty_pending','validated_parameter_pairs_including_novelty_pending',
            'confirmed_publictable_graph_examples','confirmed_publictable_improved_parameter_pairs','complete_Lean_graph_instances']:
    assert before[key]==after[key]
gap_path=WIKI/'gap_map.md'
gap=gap_path.read_text()
if '账本现374条实验／来源记录' in gap[:1800]:
    gap=gap.replace('账本现374条实验／来源记录','账本现376条实验／来源记录',1)
    gap_path.write_text(gap)
receipt=dict(status='PASS_FULLK2_TERMINAL_C21_S80_GENERATIVE_ROWS_PENDING_FINAL',
    updated_UTC=NOW,record_count=376,new_experiments=new_records,new_independent_methods_claimed=0,
    updated_existing_id=id14,new_ids=[id21,id80],
    D14_fullallgroup_status='UNKNOWN',D14_solver_CPU_seconds=full['solver_CPU_seconds'],
    D14_charged_whole_CPU_seconds=full['charged_whole_CPU_seconds'],
    D14_measured_whole_CPU_lower_bound=full['measured_whole_CPU_lower_bound'],
    D14_exact_aggregate_claimed=False,
    C21_uniform100_scope_paper_excluded=True,
    S80_two_type_framework_order_at_most1920=True,S80_C25_solver_calls=0,
    new_papers_external_review='PENDING',D15_K2_actual_result_recorded=False,
    new_valid_graphs=0,valid_examples=104,valid_pairs=4,confirmed_examples=103,confirmed_pairs=3,Lean_instances=1,
    final_query_rebuild_after_root_update_pending=True,helper_stdout=run.stdout.strip())
out=HERE/'FULLK2_C21_S80_WIKI_RECEIPT.json'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=receipt['status'],receipt=str(out.relative_to(ROOT)),
    record_count=376,new_experiments=new_records),ensure_ascii=False))

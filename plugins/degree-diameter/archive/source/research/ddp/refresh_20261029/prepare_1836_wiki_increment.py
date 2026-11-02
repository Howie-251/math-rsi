"""Prepare saved source, guard-cover and auxiliary-graph results for Wiki sync.

This script does not modify the Wiki or run any experiment or solver.
The root confirms the external-factor terminal state before final serial sync.
"""
from pathlib import Path
import copy
import json
import sys

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'aris_repo/tools'))
import capture_filter
ledger=json.loads((ROOT/'research-wiki/DDP_METHOD_LEDGER.json').read_text())

def rel(p):return str(p.relative_to(ROOT))
def paths(folder,names):
    result=[rel(folder/name) for name in names]
    assert all((ROOT/p).exists() for p in result)
    return result

d9=HERE/'d9_D6_source_mechanism_gate'
data9=json.loads((d9/'RAW_ANALYSIS_FIELDS.json').read_text())
source9=dict(id='ddp-d9-d6-current77418-regular-source-gate-20261029',
    title='Current77418 source is9regular: no retained-edge expansion slots',
    family='generalized-polygon source / retained-edge applicability',
    idea_family='idea:ddp-open-parameter-construction-20261026',
    record_type='actual-source-eligibility-profile',
    target_Delta=9,target_D=6,savedL=77418,baseline_date='2026-10-29',date='2026-10-29',
    n=dict(actual=77418,hypothetical=None),actual_graph_Delta=9,actual_D=6,
    actual_D_scope='Official current-sourceD6 assertion inherited; no source distance BFS.',
    ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=None,
    status=data9['status'],outcome_class='source-recovery-regular-retained-edge-applicability-closed',wiki_verdict='partial',
    scope='Current official77418 literal only: one full degree/edge parse, two primary pages/files. Source H8 plus flag-subdivision/K5/external3 recipe, not the182618/186033 tower.',
    failure_or_result='实际77418/348381/simple/symmetric/all9regular，free0/slots0。固定保全部旧顶点与旧边的任何非空connected增广在max9下不可能；普通degree不足证明无需距离球。sourceD6继承官方，CPU.641021884、2primary、0距离BFS/球/solver/候选。',
    positive_guarantees=[
        '直接literal确认每个旧点已经满9度；oldedges全保则无法给任一旧点添加连接到新点的边。',
        'Recipe中每新点2old+4clique+3external=9；actual triangle表明整个modified source非二分，不能直接称全源异色锚层。'],
    lesson_and_restart_condition='此源不支持保边append，停止该入口；只有实质删边／重接规则或不同source才是新问题，不借free0开启proxy/guard梯子。',
    unclosed_gap='一般(9,6)、删旧边手术、不同source未排；10D6=137180 literal未下载或profile，不混为本次已测。',
    other_metrics=dict(actual_source_n=77418,actual_source_m=348381,
        actual_source_degree_histogram={'9':77418},free_vertices=0,free_slots=0,
        CPU_seconds=data9['numerical_cpu_seconds'],primary_pages_or_files=2,
        original_H8_n=74898,modified_spread_lines=504,new_vertices=2520,
        current_modified_source_bipartite=False,
        source_D6_inherited=True,source_distance_BFS=0,new_balls=0,
        candidate_graphs=0,solver_calls=0,new_lower_bound_mathematically_verified=False,
        independent_new_method=False,source_credit='Official Comellas current77418 H8 flag-subdivision construction'),
    report_paths=data9['report_paths'])

joint=HERE/'d13_joint_capacity_read'
guard=HERE/'d13_v4580_fourguard'
frac=HERE/'d13_v4580_fractional_gate'
joint_data=json.loads((joint/'ANALYSIS.json').read_text())
literal=json.loads((joint/'CURRENT_LITERAL_CAPACITY.json').read_text())
sat=json.loads((guard/'RESULT.json').read_text())
model=json.loads((guard/'MODEL.json').read_text())
lp=json.loads((frac/'RESULT.json').read_text())
assert literal['mandatory_still_free']==38 and literal['mandatory_blocked']==13
assert sat['status']=='UNKNOWN' and lp['status']=='LP_UNKNOWN_NO_CERTIFICATE'
gpaths=paths(joint,['READ_SCOPE.json','REPORT.md','ANALYSIS.json','CURRENT_LITERAL_CAPACITY.json'])
gpaths+=paths(guard,['PREDICTION.json','prepared.json','MODEL.json','RESULT.json','TERMINAL.json',
    'PREPARE_TERMINAL.json','SAT_TERMINAL.json','HANDLE.json','mandatory.pins.txt','run_once.py'])
gpaths+=paths(frac,['PREDICTION.md','RESULT.json','HANDLE.json','lp_once.py'])
gpaths += [
    'research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/accepted_family40.json',
    'research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/frozen91.json']
guardrow=dict(id='ddp-d13-v4580-current51457-fourguard-unknown-20261029',
    title='Current51457 prototype4580: complete<=4guard SAT and fractional LP UNKNOWN',
    family='H9 prototype-neighborhood extension',idea_family='idea:ddp-breadth-20261027',
    record_type='complete-current-target-single-prototype-cover-model',
    target_Delta=13,target_D=5,savedL=51457,baseline_date='2026-10-29',date='2026-10-29',
    n=dict(actual=None,hypothetical=51458),actual_graph_Delta=None,actual_D=None,
    actual_D_scope='No candidate graph or global diameter computed; source51457 D5 accepted earlier.',
    ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=None,
    status='SAT_AND_LP_UNKNOWN_NO_CERTIFICATE',outcome_class='solver-UNKNOWN-complete-current-fourguard-model',wiki_verdict='partial',
    scope='当前51457固定prototype4580，删去唯一sat pin45089后的mandatory9全free；全部2755个当前缺项、13057个非零不同guard列、独立guard数<=4。不是旧51445/750目标四guardMIP，也不是41helper joint packing。',
    failure_or_result='一次完整2755target/13057column SAT60秒UNKNOWN、code0，无模型；aggregate68.829465935CPU。另一次同完整矩阵fractional LP20秒limit UNKNOWN、无primal/dual下界证书，22.439896875CPU；合91.269362810CPU。0新图/全源BFS，不续timer。',
    positive_guarantees=[
        'Source/current target/column绑定完整；mandatory9确有余量，SAT目标是精确guard联合覆盖，不是old2752目标缓存的拼接。',
        '旧40邻点集均只用原51417标签，旧51失败原型中38个mandatory在final仍全free，13个blocked；不能把前38个失败归因于贪心端口锁。',
        '五个两两互斥closedB1支持组只证明强一阶proxy至少5guards；不能否定允许长R4路线的完整四guard域。'],
    lesson_and_restart_condition='本完整SAT与LP预算均终止，UNKNOWN保持开放，不能用五组强proxy否定替代R4模型；不恢复51445旧MIP或给本例自动加时。Joint重排需真实原base静态覆盖池，当前40项动态接受证据不能反向当作此池。',
    unclosed_gap='固定v4580/current51457完整<=4guard是否可覆仍OPEN；一般partial-star、其它mandatory集与共同容量问题未排。',
    variants=[dict(label='strong_closedB1_proxy_certificate_only',
        sufficient_certificate='N(45089) subset closedB1(mandatory union guards)',
        guard_lower_bound=5,available_guard_budget=4,
        five_disjoint_supports=joint_data['v4580']['strong_proxy_obstruction']['five_disjoint_supports'],
        current_graph_extension_argument=joint_data['v4580']['strong_proxy_obstruction']['applicability'],
        excludes_full_R4_model=False)],
    other_metrics=dict(source_n=51457,source_m=324863,prototype=4580,omitted_saturated_pin=45089,
        mandatory_pins=joint_data['v4580']['mandatory'],mandatory_count=9,
        missing_current_targets=2755,eligible_current_guards=13115,unique_nonzero_guard_masks=13057,
        guard_budget=4,SAT_variables=model['total_variables'],SAT_clauses=model['clauses'],
        SAT_calls=1,SAT_status='UNKNOWN',SAT_child_CPU_seconds=sat['child_CPU_seconds'],
        SAT_aggregate_CPU_seconds=sat['aggregate_CPU_seconds'],LP_calls=1,
        LP_status='UNKNOWN_NO_CERTIFICATE',LP_nnz=lp['matrix_nnz'],
        LP_CPU_seconds=lp['worker_CPU_seconds'],combined_CPU_seconds=sat['aggregate_CPU_seconds']+lp['worker_CPU_seconds'],
        source_allroot_BFS=0,new_candidate_graphs=0,incumbent=None,
        LP_primal_certificate=None,LP_dual_certificate=None,
        current_mandatory_free_prototypes=38,current_mandatory_blocked_prototypes=13,
        old_static_51417_target_count=2752,do_not_mix_old_masks=True,
        old51445_problem_is_distinct=True),report_paths=gpaths)

success_id='ddp-d13-singlefault-star-family-51457-20261027'
success=copy.deepcopy(next(r['source_record'] for r in ledger['rows'] if r['id']==success_id))
success['matched_existing_id']=success_id
label='actual_final_capacity_of_old51_failed_prototypes_20261029'
success['variants']=[v for v in success.get('variants',[]) if v.get('label')!=label]+[dict(
    label=label,all40_neighbor_sets_use_only_original51417_labels=True,
    old_failed_prototypes=51,mandatory_still_free=38,mandatory_blocked=13,
    joint_static_original_base_cover_pool_available=False,
    conclusion='Do not attribute failure of all38 still-free mandatory sets to sequential port locking; oldcurrent cover certificates cannot be reversed to original-base static covers.',
    full_v4580_followup_experiment='exp:'+guardrow['id'],
    old_v51445_MIP_is_distinct=True,new_graphs=0,new_source_BFS=0)]
success['report_paths']=list(dict.fromkeys(success.get('report_paths',[])+paths(joint,['REPORT.md','ANALYSIS.json','CURRENT_LITERAL_CAPACITY.json'])))

affine=HERE/'q8_fiber_K64_affine_gate';factor=HERE/'q8_K64_external_factor_sat'
ag=json.loads((affine/'TERMINAL.json').read_text())
fm=json.loads((factor/'MODEL.json').read_text())
factor_saved=json.loads((factor/'RESULT.json').read_text())
assert ag['full_scope_completed'] and ag['candidates_evaluated']==3840
qpaths=paths(affine,['PREDICTION.md','INPUT.json','REPORT.md','CASES.jsonl','TERMINAL.json','HANDLE.json','run.py'])
qpaths+=paths(factor,['PREDICTION.md','MODEL.json','EDGE_VARIABLES.json','RESULT.json','TERMINAL.json','HANDLE.json','run_once.py'])
qpaths+=['research/ddp/refresh_20261029/d11_D6_mechanism_read/paper_extracted.txt',
         'research/ddp/refresh_20261029/d11_D6_mechanism_read/README.md']
qrow=dict(id='ddp-q8-k64-cube-external2factor-13d3-20261029',
    title='q8/13D3 conditional1088: fixed affine3840 fail; complete cross-pencil2factor model',
    family='generalized-quadrangle fibre extension / auxiliary graph',
    idea_family='idea:ddp-open-parameter-construction-20261026',
    record_type='auxiliary_graph_family_and_conditional_main_graph',
    target_Delta=13,target_D=3,savedL=972,baseline_date='2026-10-29',date='2026-10-29',
    n=dict(actual=None,hypothetical=1088),actual_graph_Delta=None,actual_D=None,
    actual_D_scope='No1088 main graph constructed. Auxiliary candidates64 vertices;3840 fixed affine cases fail their first complete R3 root gate.',
    ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=None,
    status='PENDING_ROOT_FACTOR_TERMINAL_CONFIRMATION',
    outcome_class='auxiliary-model-status-pending-confirmation',wiki_verdict='partial',
    scope='Rajiv Theorem1 q8:Xprime={1,2,4},X={3,5,6,7}。K64须包含8个指定Q3并maxdegree5、D<=3。固定affine类与任意跨pencil2factor是两个明确辅助域，不是已构建1088图或全部K64图。',
    failure_or_result='固定sigma的J5+I1、两个coset三元组共3840项实际K64 simple5regular候选均首root0R3失败，CPU.42158127；0未试/正例/1088图。全cross-pencil2factor模型的最终状态等待root确认后再同步。',
    positive_guarantees=[
        'Rajiv原文PDF第3–4页Theorem1提供完整条件充分覆盖：q8主图1088，pointdegree13、linedegree8+degK，故K64max5/D3足够。作者已有1088/14并明确未找到degree2 extra gadget，不能称该机会未被作者尝试。',
        '固定affine3840类每项含指定8个Q3、加真逆sigma两邻，simple5regular；完整域失败不排其它affine／辅助图。',
        '完整cross-pencil2factor模型保所有1792潜在外边、每点额外degree2，固定cube覆盖同pencil，R2/R3真实路径条件覆盖全部1792跨pencil无序对。'],
    lesson_and_restart_condition='不恢复已闭J5+I1 affine类。外部2factor唯一solver调用按实际终态记录，不自动续timer；SAT必须先导K64并实际验收，再生成/独验1088主图，局部或CNF派发都不是新图成果。',
    unclosed_gap='全cross-pencil2factor域的数值状态等root确认；一般K64允许pencil内新增边的更宽域、其他辅助图和一般(13,3)未排。',
    variants=[dict(label='fixed_J5plusI1_two_coset_triplets3840',status=ag['status'],
        candidate_auxiliary_graphs=3840,auxiliary_n=64,auxiliary_degree=5,
        root_checks=3840,first_failed_root=0,positive_all64_root_graphs=0,
        branch_counts=[1920,1920],new_main1088_graphs=0,CPU_seconds=ag['CPU_seconds'],
        exact_scope=ag['scope']),
        dict(label='all_cross_pencil_external_2factor',status='PENDING_ROOT_TERMINAL_CONFIRMATION',
        vertices=64,fixed_cube_edges=96,external_edge_variables=1792,
        all_variables=fm['all_variables'],clauses=fm['clauses'],target_unordered_pairs=1792,
        external_degree=2,WLOG_external_edges=[[0,8],[0,16]],
        normalization_lemma='If no vertex has external neighbors in distinct pencils, its outside-pencilR3<=50<56. Otherwise pencil/cube relabeling gives the two fixed external edges.',
        model_scope='All simple2factors crossing distinct pencils only; no internal-pencil extra edges.',
        observed_saved_result=factor_saved,
        whole_main1088_graphs=0)],
    other_metrics=dict(conditional_main_order=1088,conditional_degree_bound=13,
        public_bound_in_parent_frozen_prediction=972,author_known1088_degree14=True,
        Theorem1_source='Rishabh Rajiv, Zenodo23052995, PDFpp3-4',
        Xprime=[1,2,4],X=[3,5,6,7],auxiliary_required_n=64,auxiliary_required_maxdegree=5,
        fixed_affine_auxiliary_graphs=3840,fixed_affine_root_R3_checks=3840,
        actual_main_graphs=0,new_lower_bound_mathematically_verified=False,
        actual_main_D=None,new_Lean_instances=0),report_paths=qpaths)

rows=[source9,success,guardrow,qrow]
for r in rows:
    assert not capture_filter.screen(json.dumps(r,ensure_ascii=False)),r['id']
    assert all((ROOT/p).exists() for p in r['report_paths']),r['id']
out=HERE/'SOURCE_GUARD_Q8_PENDING_WIKI_ROWS.json'
out.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status='PREPARED_ONLY_NOT_SYNCED',raw=rel(out),
    new_ids=[source9['id'],guardrow['id'],qrow['id']],existing_id_updated=success_id,
    projected_new_ledger_rows=3,projected_record_count=ledger['record_count']+3,
    no_Wiki_write=True,awaiting_root_factor_terminal_confirmation=True),ensure_ascii=False))

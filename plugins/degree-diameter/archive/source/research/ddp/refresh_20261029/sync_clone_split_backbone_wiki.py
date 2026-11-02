"""One incremental update of completed clone/split/K8 facts; no research run."""
from pathlib import Path
from datetime import datetime, timezone
import copy
import importlib.util
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
WIKI = ROOT / 'research-wiki'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def load(folder, name='RESULT.json'):
    return json.loads((HERE / folder / name).read_text())


def evidence(folder):
    return [str(p.relative_to(ROOT)) for p in sorted((HERE / folder).rglob('*'))
            if p.is_file() and p.suffix in {'.md', '.json', '.py', '.cpp'} and '__pycache__' not in p.parts]


def variant(row, item):
    row['variants'] = [v for v in row.get('variants', []) if v.get('label') != item['label']] + [item]


clone = load('d11_to_d12_clone_capacity')
split = load('d13_accepted_helper_split')
diagnostic = load('d15_K8_shared_backbone_gate')
model = load('d15_K8_backbone_integer', 'MODEL.json')
terminal = load('d15_K8_backbone_integer', 'SOLVER_TERMINAL.json')
assert clone['clone_count_upper'] == 4017 and clone['final_order_upper'] == 41648
assert clone['source_edge_reads'] == clone['solver_calls'] == clone['graphs_generated'] == 0
assert split['objects_tested'] == split['singleton_rejected_objects'] == split['BFS_roots'] == 40
assert split['status'] == 'COMPLETE_ALL40_ADJACENT_HELPER_SPLITS_EXCLUDED'
assert split['graph_exports'] == split['solver_calls'] == 0
assert diagnostic['distinct_R2_provider_triples'] == 648
assert model['complete_all648_ports'] and model['complete_all15552_targets']
assert terminal['status'] == 'UNKNOWN_NO_ACCEPTED_BACKBONE'
assert terminal['raw_status'] == 1 and terminal['solver_calls'] == 1
assert terminal['candidate_count'] == terminal['coloring_solver_calls'] == terminal['complete_new_graphs'] == 0
assert terminal['running'] is False and terminal['pending'] == []
whole_K8 = diagnostic['CPU_seconds'] + model['preparation_CPU_seconds'] + terminal['process_CPU_seconds']
before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
existing = {r['id']: r for r in before['rows']}
assert before['record_count'] == len(existing) and before['record_count'] in {378, 379}
id_clone = 'ddp-accepted-d11-d12-full-neighborhood-clone-scan-20261028'
id_split = 'ddp-d13-singlefault-star-family-51457-20261027'
id_K8 = 'ddp-d15-d4-literal15552-K8-shared64-backbone-20261030'
new_records = int(id_K8 not in existing)
rows = []

c = copy.deepcopy(existing[id_clone]['source_record'])
variant(c, dict(label='accepted37631_cap12_complete_old_neighborhood_integer_clone_capacity_20261030',
    status=clone['status'], target_Delta=12, target_D=5, savedL=42402,
    source_n=37631, source_m=205329, old_degree_cap=11, new_degree_cap=12,
    scope=clone['newly_excluded_scope'], inherited_every_prototype_has_saturated11_neighbor=True,
    multiplicity_per_prototype_upper=1, total_old_pin_capacity=40914,
    old_degree11_slack=3283, weighted_bound='11 sum(k) <= 40914+3283=44197',
    clone_count_upper=4017, final_order_upper=41648, needed_clones_to_beat42402=4772,
    bound_claimed_attainable=False, source_reads=0, BFS_runs=0,
    LP_calls=0, solver_calls=0, graph_generations=0,
    local_static_proof=True, external_review_status='NOT_YET_RECORDED',
    old_cap11_failure_extrapolated=False,
    extra_new_new_edges_do_not_reduce_old_pin_load=True))
c['scope'] += '；新cap迁移另按37631旧源、保全旧边及完整原N(v)整数复制处理：cap12每原型k≤1、总clone≤4017、最终≤41648；不是从旧cap11无首clone直接外推。'
c['failure_or_result'] += '；继承完整degree/sat-neighbor profile的两行加权证书给11Σk≤44197，Σk≤4017，达不到超过42402所需4772。0源读/BFS/LP/solver/新图；上界不称可达。'
c['lesson_and_restart_condition'] += '；停止该固定源cap12完整原邻域packing，不值得再求最大packing；保持原N(v)时添加新新边也不能逃过旧端口负载上界。'
c['unclosed_gap'] += '；其他源、改变邻域/删旧边/动态生成或合作改造均不由4017上界排除。'
c['other_metrics'].update(cap12_clone_count_upper=4017, cap12_final_order_upper=41648,
    cap12_integer_packing_solved=False, cap12_upper_bound_attainable_claimed=False)
c['report_paths'] = list(dict.fromkeys(c['report_paths'] + evidence('d11_to_d12_clone_capacity')))
rows.append(c)

s = copy.deepcopy(existing[id_split]['source_record'])
variant(s, dict(label='current51457_all40_accepted_helper_adjacent_splits_complete_singleton_gate_20261030',
    status=split['status'], scope='Currentliteral51457, each of40 accepted added vertices51417..51456 separately. Partition its complete old neighbor set between retained h and one new adjacent vertex; preserve all other edges and each old-port load. All partitions including empty sides covered; not simultaneous multi-vertex changes.',
    prediction='At least one of40 helpers admits the adjacent split', prediction_result='REFUTED',
    tested_helpers=40, degree_histogram={'10':30,'11':8,'12':2},
    source_reads=1, BFS_roots=40, all40_singleton_rejections=True,
    first_witness=dict(h=51417,target=0,unique_first_neighbor=50577,support_mask=512),
    normalized_partitions_enumerated=0,
    complete_partition_exclusion_reason='Each object has a distance5 target with singleton shortest first-neighbor support; the opposite split side is forced to distance6 for every partition.',
    old_old_D5_inherited_from_static40_and780=True, old_static_checks_recomputed=False,
    native_CPU_seconds=split['native_CPU_seconds'], whole_CPU_seconds=split['whole_CPU_seconds'],
    graph_exports=0, accepted_graphs=0, solver_calls=0,
    local_exact_gate=True, external_review_status='NOT_YET_RECORDED',
    result='research/ddp/refresh_20261029/d13_accepted_helper_split/RESULT.json',
    witness_cases='research/ddp/refresh_20261029/d13_accepted_helper_split/CASES.json'))
s['scope'] += '；当前51457中全部40个已接受外围的单点相邻拆分整域由40个singleton首步支持排除；保全原B0及其余39外围，不排多点共同改造。'
s['failure_or_result'] += '；新预测至少一个可split被完整40对象门推翻，1源读/40规定根BFS，各对象均有distance5 singleton支持；首51417→0只能先50577。native0.211257/whole1.159890927CPU，0划分穷举/图/solver；singleton已否定该对象所有二分，不需反复导失败图。'
s['lesson_and_restart_condition'] += '；停止这40对象的单点邻边二分，不逐个加guard补洞。要再改造须真正改变唯一首步路线，而非换划分；多点联合规则仍需自己的保径依据。'
s['unclosed_gap'] += '；本轮split仅排当前40外围各自单点相邻二分；不是其他顶点/多个外围/新增边或一般扩张排除。U=397原端口总B0容量706、旧usage412、剩294；固定40/43邻域max40不是全U任意重分配上界。全U目标provider容量尚未计算。'
s['other_metrics'].update(accepted40_single_helper_adjacent_split_complete=True,
    accepted40_adjacent_split_singleton_rejections=40,
    accepted40_split_new_graphs=0, accepted40_split_BFS_roots=40,
    old397_port_pool_original_total_capacity=706,
    old397_port_pool_actual_usage=412, old397_port_pool_residual=294,
    arbitrary397_port_neighborhood_reallocation_excluded=False)
s['report_paths'] = list(dict.fromkeys(s['report_paths'] + evidence('d13_accepted_helper_split')))
rows.append(s)

k8 = dict(id=id_K8,
    title='Literal15552(15,4) K8共同64端口骨架：完整支持诊断与必要整数门UNKNOWN',
    family='fixed-source spare-neighbor route cover', idea_family='idea:ddp-breadth-20261027',
    date='2026-10-30', record_type='fixed-source-complete-port-target-clique-cooperative-backbone-model',
    target_Delta=15,target_D=4,savedL=15552,baseline_date='2026-10-26',
    n=dict(actual=None,hypothetical=15560),actual_graph_Delta=None,actual_D=None,
    ordinary_bad_unordered_pairs=None,outcome_class='COMPLETE_ALL648_ALL15552_NECESSARY_K8_BACKBONE_UNKNOWN',
    scope='Preserve all edges of the accepted literal15552 degree15/D4 source. Add8 mutually adjacent helpers, each attached to8 distinct degree14 old ports; all8 groups disjoint, forming64-port T. Filling groups to8 loses no solution because648 spare1 ports are available. K8 maximizes h(16-h) common pins in this degree15 clique rule. Whole648 columns and15552 targets encoded; no LP pool/fiber-color/line/symmetry restriction. The current model decides only the necessary uncolored T gate, not full8-color graph feasibility.',
    failure_or_result='Cached diagnostic:5184 sparse R2 targets reduce to648 literal provider triples, each port lies in3 triples and covers24 sparse targets, so any64-pin T leaves at least3648 sparse targets requiring8-color R3 coverage. Triples are actual affine lines in3 independent directions;72 R3 block/count signatures do not permit merging distinct literal supports. Diagnostic0.143200583CPU,0BFS/balls/source read. Full backbone648binary variables/15553rows/1497528nnz, constraints sumT=64 and R3count+7R2count>=8 for every target, prepared0.354100389CPU. Actual sole HiGHS45s window returned raw1/Status13 time limit: UNKNOWN_NO_ACCEPTED_BACKBONE, solver47.065159115/process47.296332646CPU, aggregate47.793633618CPU including both prior stages.0accepted T/0coloringcalls/0newgraphs; stop, not K8 exclusion.',
    positive_guarantees=[
        'All literal target rows and648 ports retained; R2 subset R3 checked before exact binary OR inequality encoding.',
        'If R2(T) misses a target, every one of8 helper colors needs its own selected R3 provider; uncolored count>=8 is necessary only.',
        'A future accepted T would still require8-color disjoint groups and complete graph acceptance; no T was returned in this run.',
        'Source-only coloring code was not executed and is not counted as a failed experiment.'],
    other_metrics=dict(source_n=15552,source_m=116316,ports=648,spare_per_port=1,
        helper_count=8,pins_per_helper=8,common_T_size=64,conditional_n=15560,
        sparse_R2_targets=5184,literal_R2_provider_triples=648,
        sparse_targets_per_port=24,uncovered_sparse_targets_lower_bound=3648,
        R3_block_signatures=72,R3_count_signatures=72,literal_R3_supports_not_merged=True,
        diagnostic_CPU_seconds=diagnostic['CPU_seconds'],prepare_CPU_seconds=model['preparation_CPU_seconds'],
        binary_variables=648,rows=15553,target_rows=15552,matrix_nnz=1497528,
        complete_all_ports=True,complete_all_targets=True,
        backbone_model_is_necessary_not_complete_graph_model=True,
        actual_solver_status=terminal['status'],raw_HiGHS_status=1,raw_HiGHS_model_status=13,
        solver_calls=1,solver_CPU_seconds=terminal['solver_CPU_seconds'],
        process_CPU_seconds=terminal['process_CPU_seconds'],whole_batch_CPU_seconds=whole_K8,
        accepted_backbones=0,coloring_solver_calls=0,source_only_coloring_executed=False,
        source_graph_reads=0,BFS_runs=0,new_graphs=0,current_running=False,pending=[],
        K8_family_excluded=False,automatic_continuation=False,new_record=False,
        external_static_review_status='NOT_YET_RECORDED'),
    variants=[
        dict(label='cached5184_sparse_target_literal_triples_and_R3_shared_signature_diagnostic_20261030',
            status=diagnostic['status'],targets=5184,triples=648,
            each_port_sparse_target_multiplicity=24,at_least3648_sparse_targets_still_need_coloring=True,
            same_fiber_one_color_restriction_rejected=True,literal_R3_support_rows_not_merged=True,
            CPU_seconds=diagnostic['CPU_seconds'],source_reads=0,BFS_runs=0,solver_calls=0),
        dict(label='full648_by15552_uncolored_K8_backbone_integer_single45window_20261030',
            status=terminal['status'],variables=648,rows=15553,matrix_nnz=1497528,
            exact_binary_constraint='R3count+7R2count>=8; sumT=64',
            model_scope='Necessary uncolored T gate only; not sufficient for8-color construction',
            actual_solver_calls=1,raw_status=1,raw_HiGHS_status=13,
            solver_CPU_seconds=terminal['solver_CPU_seconds'],process_CPU_seconds=terminal['process_CPU_seconds'],
            whole_batch_CPU_seconds=whole_K8,candidates=0,coloring_solver_calls=0,new_graphs=0,
            source_only_coloring_script_executed=False,K8_family_excluded=False,running=False,pending=[])],
    lesson_and_restart_condition='Shared R2 skeleton geometry has real redundancy but64 ports cannot remove8-color requirements for at least3648 sparse targets. Preserve literal mixed-fiber colors. The complete necessary backbone model stopped at its sole time limit with no T; do not infer infeasibility or extend timer/seed/clique-size ladder. A materially new coverage or integrality fact is needed to reopen this batch.',
    unclosed_gap='K8 extension remains UNKNOWN. No accepted T, no coloring call, no15560 graph. Exact8-color feasibility is unresolved and unexecuted; a source-only coloring script is not a failed full model. Existing K2 UNKNOWN is separate.',
    report_paths=evidence('d15_K8_shared_backbone_gate')+evidence('d15_K8_backbone_integer'),
    hardware_raw='Single-thread HiGHS feasibility call, one45s window; whole batch cap90CPU.',
    duration_raw='Diagnostic.143200583+prepare.354100389+process47.296332646=47.793633618CPU;solver47.065159115CPU.')
rows.append(k8)

spec = importlib.util.spec_from_file_location('capture_filter',ROOT/'aris_repo/tools/capture_filter.py')
capture = importlib.util.module_from_spec(spec);spec.loader.exec_module(capture)
for row in rows:
    assert all((ROOT/p).exists() for p in row['report_paths'])
    assert not capture.screen(json.dumps(row,ensure_ascii=False))
raw_path = HERE/'CLONE_SPLIT_BACKBONE_WIKI_ROWS.json'
raw_path.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
run = subprocess.run([sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(raw_path)],
    cwd=ROOT,capture_output=True,text=True,check=True)
after = json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count'] == len(after['rows']) == before['record_count']+new_records == 379
for key in ['validated_graph_examples_including_novelty_pending','validated_parameter_pairs_including_novelty_pending',
            'confirmed_publictable_graph_examples','confirmed_publictable_improved_parameter_pairs','complete_Lean_graph_instances']:
    assert before[key] == after[key]
f5 = next(r for r in after['rows'] if r['id']=='ddp-f5-full3750-d20-d3-validated-novelty-pending-20261029')
assert f5['other_metrics']['latest_global_record_confirmed'] is False
comments = WIKI/'DD82_PROGRESS_AND_COMMENTS_20261018.md'
marker = '<!-- HUMAN_SOTA_COUNT_CORRECTION_20261030 -->'
note = f'''
## {NOW} 人工询问新增数量与3750全球比较口径

用户本次追问“现在新增多少”以及“3750全球原来多少，为什么说全球sota”。根已明确纠正并沿用以下记账：已确认公开主表改善仍为103个完整实例／3参数；另有3750点20度直径3合法完整图1例，故数学合法总104例／4参数，但不能混称104个新纪录。3750最新全球新颖性尚待核查，不得称已确认全球SOTA。

2783仅为已经核读的Rajiv September2026来源值，其此前值2750；它不等于已绑定的当前全球最高。3750相对该指定来源多967，只是有界来源比较。latest_global_record_confirmed=false保持，完整具体公式Lean1的既有范围不扩大。

这段是人工口径纠正，不是新构造或额外方法。专家EXPERT_HANDOFF_20261030的02:02 UTC快照冻结，不重包；Goal ACTIVE、D2暂停。当前clone容量、40split与K8骨架实际终态正进行本批唯一Wiki同步，最后query待根最终phase及真实审阅处置，不把文档更新当研究产出。
'''
if marker not in comments.read_text():
    assert not capture.screen(note)
    with comments.open('a') as out:out.write('\n\n'+marker+'\n'+note)
gap_path = WIKI/'gap_map.md'
gap = gap_path.read_text().replace('账本现378条实验／来源记录','账本现379条实验／来源记录',1)
gap_path.write_text(gap)
receipt = dict(status='PASS_CLONE_SPLIT_K8_TERMINALS_AND_HUMAN_SOTA_CORRECTION_SYNCED_PENDING_ROOT_FINAL',
    updated_UTC=NOW,record_count=379,updated_ids=[id_clone,id_split,id_K8],
    new_experiment_records=new_records,new_independent_methods_claimed=0,
    clone_cap12_upper=4017,split_objects=40,split_singletons=40,
    K8_status=terminal['status'],K8_solver_calls=1,K8_coloring_calls=0,K8_whole_CPU_seconds=whole_K8,
    mathematical_review_result_not_yet_recorded=True,
    new_accepted_graphs=0,valid_examples=104,valid_pairs=4,confirmed_examples=103,confirmed_pairs=3,Lean_instances=1,
    latest_global_3750_record_confirmed=False,human_SOTA_correction_recorded=True,
    expert_snapshot_UTC='2026-10-30 02:02 UTC',root_or_expert_files_modified=False,
    final_query_after_root_update_pending=True,helper_stdout=run.stdout.strip())
out = HERE/'CLONE_SPLIT_BACKBONE_WIKI_RECEIPT.json'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=receipt['status'],record_count=379,new_experiment_records=new_records,
    receipt=str(out.relative_to(ROOT))),ensure_ascii=False))

"""Record actual new-fiber review and the new-parameter K2 terminal."""
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


def evidence(folder):
    return [str(p.relative_to(ROOT)) for p in sorted((HERE/folder).rglob('*'))
        if p.is_file() and p.suffix in {'.md','.json','.py','.cpp'} and '__pycache__' not in p.parts]


prefix=ROOT/'reviews/ddp/new_fiber_route_obstructions_20261030'
review=json.loads(prefix.with_suffix('.response.json').read_text())['structuredContent']
assert (review['status'],review['model'],review['effort'])==('SUCCESS','gemini-3.8-flash-high','high')
gate=json.loads((HERE/'d15_D4_K2_route_gate/RESULT.json').read_text())
model=json.loads((HERE/'d15_D4_K2_fulltarget/MODEL.json').read_text())
terminal=json.loads((HERE/'d15_D4_K2_fulltarget/SOLVER_TERMINAL.json').read_text())
assert gate['T0_size']==0 and gate['ports']==648 and gate['computed_R2_balls']==648
assert (gate['all_target_R2_provider_min'],gate['all_target_R2_provider_max'],gate['all_target_R3_provider_min'])==(3,18,67)
assert gate['R2_provider_count_histogram']['3']==5184
assert terminal['status']=='UNKNOWN' and terminal['returncode']==0 and terminal['actual_solver_calls']==1
assert terminal['running'] is False and terminal['pending']==[]
assert (model['selectors'],model['all_variables'],model['total_clauses'])==(1296,19440,69306)
assert model['complete_all_ports'] is model['complete_all_targets'] is True
before=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count']==len(before['rows']) and before['record_count'] in {376,377}
existing={r['id']:r for r in before['rows']}
ids=['ddp-c21-fano-flag-uniform100-affine-plane-deletion-route-obstruction-16d3-20261030',
     'ddp-f5-fiber80-two-type-normal-scaling-chart-rigidity-16d3-20261030']
id15='ddp-d15-d4-literal15552-all648-k2-cooperative-cover-20261030'
new_records=int(id15 not in existing)
rows=[]
review_meta=dict(status='SUCCESS_SOUND_AS_STATED',actual_model=review['model'],effort=review['effort'],
    thread_id=review['threadId'],
    C21_scope='FixedFanoflagC21,uniform100singleaffineplanedeletion,everystepnoisetransversetotargetnormal;edge-specificchartsandfiber-specificplanesallowed.',
    S80_scope='F5*_a×F5*_b×F5_h,twoinversepairedtypesApassiveb/Bpassiveaonlynonzeroscale;thewholeframehascontrollerN<=24.',
    generalN16D3_upper_bound_claimed=False,
    old3750_LRAT_used_as_basis_for_these_newrules=False,
    reviewer_executed_C25_or_largegraph_or_LRAT_or_Lean=False,
    response=str(prefix.with_suffix('.response.json').relative_to(ROOT)),
    disposition=str(prefix.with_suffix('.DISPOSITION.md').relative_to(ROOT)))
for identifier in ids:
    row=copy.deepcopy(existing[identifier]['source_record'])
    row['other_metrics']['external_review_status']='SUCCESS_SOUND_AS_STATED'
    row['other_metrics']['actual_external_review']=review_meta
    for v in row['variants']:
        if v.get('external_review_status')=='PENDING':
            v['external_review_status']='SUCCESS_SOUND_AS_STATED'
            v['actual_external_review']=review_meta
    if identifier==ids[0]:
        row['outcome_class']='PAPER_EXCLUDED_SPECIFIED_C21_UNIFORM100_RULE_STATIC_REVIEW_SUPPORTED'
        row['unclosed_gap']='指定C21 uniform100单plane删除/逐步noise横截规则已纸面排除并获实际GeminiSUCCESS/SOUND AS STATED；不排其它C21保留/非uniform/非平面/noise规则，一般N(16,3)仍开放；未Lean、无2100点图。'
    else:
        row['outcome_class']='PAPER_FRAMEWORK_N_AT_MOST24_STATIC_REVIEW_SUPPORTED_C25_SOLVER_STOPPED'
        row['unclosed_gap']='精确定义S80两type normal-scaling框架N≤24、阶数≤1920，实际外审SUCCESS/SOUND AS STATED。其它S/被动normal混合/非uniform/其它关系与一般N(16,3)未排。C25必要模型仅prepare，因定理停止启动，不能写solverUNSAT；未Lean、未生成2000图。'
    row['report_paths']=list(dict.fromkeys(row['report_paths']+[
        str(prefix.with_suffix(s).relative_to(ROOT)) for s in ['.prompt.md','.response.json','.DISPOSITION.md']]))
    rows.append(row)

d15=dict(
    id=id15,title='Literal15552(15,4) all648-port K2 cooperation: exact route gate, direct fractional witness and complete integer UNKNOWN',
    family='fixed-source spare-neighbor route cover',idea_family='idea:ddp-breadth-20261027',
    date='2026-10-30',record_type='new-parameter-fixed-source-allport-fulltarget-K2-integer-model',
    target_Delta=15,target_D=4,savedL=15552,baseline_date='2026-10-26',
    savedL_source='context/DD_PORTFOLIO_START_20261026/registry/cases.json',
    n=dict(actual=None,hypothetical=15554),actual_graph_Delta=None,actual_D=None,
    ordinary_bad_unordered_pairs=None,outcome_class='FULL_ALL648_LITERALPORT_FULL15552_TARGET_K2_UNKNOWN',
    scope='Fixedliteral15552/116316source,oldD4inheritedandalloldedgesretained. Addadjacenthelpersy,zandchooseA,Bfromall648degree14/spare1oldvertices,|A|,|B|<=14,AintersectionBempty. ExactcoverageR3(A)unionR2(B)=VandR3(B)unionR2(A)=V. NoLPpoolfilter,grouping,symmetryorline restriction.',
    failure_or_result='T0empty;alltargetR2providers3..18(5184targetshave3),R3providers67..185. OneR2cachegeneration648balls/oneoldsource_read,oldR3reused,1.111414086CPU. Complete1296selectors/19440vars/69306clausescontainsall31104two-sidecoverage rows. Actualone-t120UNKNOWN/code0,120.009668solver/121.957097678wholeCPU,24samePIDobservationtimeouts,0candidate/source-read/BFS/newgraphduringintegercall;stopped,notK2infeasibility.',
    positive_guarantees=[
        'Newsourceanddiameterradiiwereselectedexplicitly;thisisnottheoldsinglehelpertaskor14degreetimerresume.',
        'Everyoldtargetisencodedonbothsidesfromliteralcacheorder,withoutdiscardingdistinctports.',
        'ThefractionalrelaxationhasanexplicituniformrationalwitnesswithoutanLPcall;thisdoesnotgiveintegerpins.'],
    other_metrics=dict(source_n=15552,source_m=116316,source_D4_inherited=True,
        literal_ports=648,all_port_spares=1,side_pin_limit=14,
        source_file=gate['source_file'],old_R3_cache=gate['input_R3'],
        route_source_reads=1,new_R2_balls=648,old_R3_recomputed=0,old_source_D4_BFS=0,
        R2_provider_min=3,R2_provider_max=18,R2_min_count_targets=5184,
        R3_provider_min=67,R3_provider_max=185,T0_size=0,
        route_gate_CPU_seconds=gate['aggregate_CPU_seconds'],
        prepare_CPU_seconds=model['prepare_CPU_seconds'],
        selectors=1296,variables=19440,clauses=69306,
        coverage_rows_all=31104,coverage_rows_unique=31104,
        all_ports_and_targets_encoded=True,
        solver_status='UNKNOWN',actual_solver_calls=1,
        solver_CPU_seconds=terminal['solver_CPU_seconds'],
        whole_CPU_seconds=terminal['whole_CPU_seconds'],
        observation_timeouts=24,same_PID_waited_to_exit=True,
        current_running=False,graphs_generated=0,integer_K2_family_excluded=False,
        direct_fractional_each_side_port_weight='1/70',
        direct_fractional_each_side_sum='324/35',side_limit=14,
        direct_fractional_minimum_coverage='(67+3)/70>=1',
        direct_fractional_joint_usage_per_port='1/35<=1',
        direct_fractional_new_LP_calls=0,direct_fractional_optimality_claimed=False,
        integer_existence_inferred_from_fractional=False,new_record=False),
    variants=[
        dict(label='all648_literal_R2_provider_gate_reuse_R3_20261030',
            status=gate['status'],T0_size=0,computed_R2_balls=648,
            R2_min=3,R2_max=18,R2_min_count_targets=5184,R3_min=67,R3_max=185,
            source_reads=1,R3_recomputed=0,old_source_D4_BFS=0,
            aggregate_CPU_seconds=gate['aggregate_CPU_seconds'],solver_calls=0,new_graphs=0),
        dict(label='uniform_one_over70_per_side_exact_fractional_witness_from_provider_bounds_20261030',
            status='DIRECT_RATIONAL_RELAXATION_FEASIBLE_NO_LP',
            ports_per_side=648,each_variable='1/70',each_side_total='324/35<14',
            coverage_at_least='(67+3)/70=1',joint_per_port='1/35<=1',
            LP_calls=0,integer_pins_or_graph_claimed=False),
        dict(label='all648_literalports_full15552_two_side_integer_single120s_call_20261030',
            status='UNKNOWN_TERMINAL',selectors=1296,variables=19440,clauses=69306,
            all_target_rows=31104,all_ports_included=True,
            side_pin_limit=14,capacity1_mutexes=648,
            grouping=False,symmetry=False,line_constraint=False,LP_support_filter=False,
            driver_pid=3068247,solver_pid=3068250,
            actual_solver_calls=1,returncode=0,
            solver_CPU_seconds=terminal['solver_CPU_seconds'],whole_CPU_seconds=terminal['whole_CPU_seconds'],
            observation_timeouts=24,same_PID_waited_to_exit=True,
            whole_CPU_budget=150,solver_window=120,
            SAT_candidates=0,source_reads=0,BFS_runs=0,graphs_generated=0,
            running=False,automatic_continuation=False,pending=[],
            current_result='research/ddp/refresh_20261029/d15_D4_K2_fulltarget/SOLVER_TERMINAL.json')],
    lesson_and_restart_condition='Thetwo-helpermechanismtransferswithradii3/2andspare1disjointports,notbyassuming14degreefacts. T0gatehasnoobstructionandproviderboundsalreadygivefullfractionalfeasibility,sointegercompatibilityistheunresolvedquestion. ThefullunrestrictedliteralportselectorbatchactuallyendedUNKNOWN;stopwithoutinfeasibilityclaimorautomatictimer/seed/source-laddercontinuation.',
    unclosed_gap='Thespecificall648-portK2extensionof15552sourceisUNKNOWN,nocandidate15554graph. DirectfractionalfeasibilitydoesnotresolveintegerA/B. Originalsinglehelperandother15degreesourcesarenotrerunorexcluded.',
    report_paths=evidence('d15_D4_K2_route_gate')+evidence('d15_D4_K2_fulltarget'),
    hardware_raw='singleworker;oneboundedintegercall',
    duration_raw='Route1.111414086CPU+prepare0.809767605CPU;terminalsolver120.009668/whole121.957097678CPU')
rows.append(d15)
report='''# 新fiber证明实际外审及K2向(15,4)迁移

C21 uniform100与S80 normal-scaling框架的新外审实际SUCCESS/gemini-3.8-flash-high/high/原thread12c1d715-0369-4a25-9755-3fb41033c3bd，两项SOUND AS STATED。范围由DISPOSITION明确：C21固定单plane删除+逐步横截noise不能D3；S80两type被动normal非零缩放框架N≤24。不是一般16度上界，不引用旧3750LRAT作新源证明；C25仍0solver，停止启动。

15度源15552/116316上all648字面余度点的K2迁移已实际完成routegate：新648R2、旧R3不重算，T0空，R2支持3..18且有5184个target支持数3，R3min67，1.111414086CPU。每侧全部648变量取1/70给总324/35<14，覆盖至少(67+3)/70=1、每port合用1/35≤1，无需新LP；不是整数构造。

完整两侧31104行、1296selectors、19440vars/69306clauses已真实唯一求解；读取时actualSOLVER_HANDLE/TERMINAL均UNKNOWN/code0，120.009668solver/121.957097678wholeCPU，24次观察超时始终同PID，0候选/图。按真实终态记录，不恢复preparedMODEL或过期RUN。无LP支撑/对称/成线/分组限制，不排该域存在性。

新增1条15K2 aggregate实验，沿已有fixed-source route-cover family/idea；ledger377不是方法数。104/4合法例、confirmed103/3、Lean1保持，专家23:55冻结不重包。等待root新phase后最后query。
'''
spec=importlib.util.spec_from_file_location('capture_filter',ROOT/'aris_repo/tools/capture_filter.py')
capture=importlib.util.module_from_spec(spec);spec.loader.exec_module(capture)
assert not capture.screen(report)
report_path=HERE/'NEWFIBER_REVIEW_D15_K2_WIKI_REPORT.md';report_path.write_text(report)
for row in rows:
    row['report_paths']=list(dict.fromkeys(row['report_paths']+[str(report_path.relative_to(ROOT))]))
    assert all((ROOT/p).exists() for p in row['report_paths'])
    assert not capture.screen(json.dumps(row,ensure_ascii=False))
gap_path=WIKI/'gap_map.md'
gap=gap_path.read_text()
if '账本现376条实验／来源记录' in gap[:1800]:
    gap=gap.replace('账本现376条实验／来源记录','账本现377条实验／来源记录',1)
    gap_path.write_text(gap)
pending=HERE/'NEWFIBER_REVIEW_D15_K2_WIKI_ROWS.json'
pending.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
command=[sys.executable,str(ROOT/'research/ddp/more_graphs_20261027/sync_additional_probes.py'),str(pending)]
run=subprocess.run(command,cwd=ROOT,text=True,capture_output=True,check=True)
after=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count']==len(after['rows'])==before['record_count']+new_records==377
for key in ['validated_graph_examples_including_novelty_pending','validated_parameter_pairs_including_novelty_pending',
            'confirmed_publictable_graph_examples','confirmed_publictable_improved_parameter_pairs','complete_Lean_graph_instances']:
    assert before[key]==after[key]
receipt=dict(status='PASS_NEWFIBER_ACTUAL_REVIEW_D15_K2_TERMINAL_PENDING_ROOT_FINAL',
    updated_UTC=NOW,record_count=377,new_experiments=new_records,new_independent_methods_claimed=0,
    updated_ids=ids,new_id=id15,newfiber_actual_review=review_meta,
    D15_actual_status='UNKNOWN_TERMINAL',D15_solver_CPU_seconds=terminal['solver_CPU_seconds'],
    D15_whole_CPU_seconds=terminal['whole_CPU_seconds'],D15_solver_calls=1,
    D15_direct_fractional_witness=True,D15_new_LP_calls=0,
    new_valid_graphs=0,valid_examples=104,valid_pairs=4,confirmed_examples=103,confirmed_pairs=3,Lean_instances=1,
    final_query_rebuild_after_root_update_pending=True,helper_stdout=run.stdout.strip())
out=HERE/'NEWFIBER_REVIEW_D15_K2_WIKI_RECEIPT.json'
out.write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(status=receipt['status'],receipt=str(out.relative_to(ROOT)),
    record_count=377,new_experiments=new_records),ensure_ascii=False))

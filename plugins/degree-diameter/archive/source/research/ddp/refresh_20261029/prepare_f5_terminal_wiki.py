"""Prepare completed full-F5 and two restricted-noise records from saved evidence.

No generator, BFS, solver, formal compiler, reviewer, or baseline request runs here.
"""
from pathlib import Path
import copy
import json
import sys

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'aris_repo/tools'))
import capture_filter
WIKI=ROOT/'research-wiki'
ledger=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
full=HERE/'f5_full_d20_D3'
base=HERE/'f5_complementary_triples/baseline_check'
globalnoise=HERE/'f5_restricted_noise_d10_D4'
typenoise=HERE/'f5_triangle_noise_d10_D4'
validation=json.loads((full/'INDEPENDENT_VALIDATION.json').read_text())
generation=json.loads((full/'GENERATION_RESULT.json').read_text())
repro=json.loads((full/'REPRODUCTION_CHECK.json').read_text())
baseline=json.loads((base/'RESULT.json').read_text())
g=json.loads((globalnoise/'RESULT.json').read_text())
t=json.loads((typenoise/'RESULT.json').read_text())
local=json.loads((typenoise/'LOCAL_PREDICTION_CHECK.json').read_text())
review_path=ROOT/'reviews/ddp/f5_full3750_20261029.response.json'
review=json.loads(review_path.read_text())['structuredContent']
assert validation['status']=='PASS_COMPLETE_LITERAL_GRAPH_D3'
assert validation['roots_checked']==3750 and validation['diameter_exact']==3
assert review['status']=='SUCCESS'
assert baseline['latest_global_record_confirmed'] is False
assert g['complete_cases']==100 and t['complete_cases']==100
assert local['status']=='LOCAL_PREDICTION_SUPPORTED_GLOBAL_EXISTENCE_REFUTED'

def rel(p):return str(p.relative_to(ROOT))
def saved_paths(folder,names):return [rel(folder/n) for n in names]
full_id='ddp-f5-full3750-d20-d3-validated-novelty-pending-20261029'
noise_id='ddp-f5-fixed3750-restricted-noise-d10d4-two100-families-20261029'
full_paths=saved_paths(full,['EXECUTION_SCOPE.md','PARAMETERS.json','generate.py',
    'GENERATION_RESULT.json','graph_d20_D3_n3750.edges','independent_verify.py',
    'INDEPENDENT_VALIDATION.json','REPRODUCTION_CHECK.json','README.md',
    'FORMAL_BINDING_PLAN.md','FORMAL_COMPILE_HANDLE.json','FORMAL_COMPILE_LOG.txt',
    'COMPILE_RESULT.json','FORMAL_COMPILED_BINDING_SNAPSHOT.lean','RESULT_OVERVIEW.json'])
full_paths+=saved_paths(base,['RESULT.json','REPORT.md','PRIMARY_SOURCES.json'])
full_paths+=[
    'reviews/ddp/f5_full3750_20261029.DISPOSITION.md',
    'reviews/ddp/f5_full3750_20261029.response.json',
    'reviews/ddp/f5_full3750_20261029.prompt.md',
    'formal/DegreeDiameter/Portfolio/F5Graph3750.lean',
    'research/ddp/refresh_20261029/f5_complementary_triples/PROOF_SCOPE.md',
    'research/ddp/refresh_20261029/f5_complementary_triples/ROOT_NB3_BINDING.json',
    'research/ddp/refresh_20261029/f5_complementary_triples/MATRICES_AND_PENCILS.json']
new_graph=dict(id=full_id,
    title='Full-F5 literal3750/37500: independently validated20regular D3; latest-global novelty pending',
    family='four-label affine route-chart lifts',
    idea_family='idea:ddp-q3-three-step-plane-pencil31',
    record_type='validated-complete-literal-graph-with-pending-global-novelty',
    target_Delta=20,target_D=3,savedL=2783,baseline_date='September2026',
    n=dict(actual=3750,hypothetical=None),actual_graph_Delta=20,actual_D=3,
    actual_D_scope='Independent all3750-root BFS from literal edge list only; no source maps/balls; exact global D3.',
    ordinary_bad_unordered_pairs=0,ordinary_bad_target_D=3,
    status='MATH_ACCEPTED_LATEST_GLOBAL_NOVELTY_PENDING',
    outcome_class='positive-mathematically-validated-literal-graph-global-record-pending',
    date='2026-10-29',wiki_verdict='yes',
    scope='固定原source30 controller、四F5互补方向矩阵、全部F5五值噪声，实际完整边表3750/37500。生成定义／度数生产检查后独立代理仅读边表重建邻接、全部3750根验D3。不是旧1920复验、10度限噪声样本或仅条件图。公开比较仅本次实际读到的September2026 published2783；最新global未确认。',
    failure_or_result='实际simple/connected/20regular/3750/37500，独立all3750roots PASS、exactD3、普通>3无序对0；生成CPU0.106811736、独验CPU1.824719026。3750超过已核对published2783多967，但bounded三primary没有取得CW最新内容、未穷尽全网，latest-global novelty pending。新跨模回SUCCESS/ACCEPT_WITH_QUALIFICATIONS，静态审阅不是第二次BFS。完整具体图Lean仍0。',
    positive_guarantees=[
        '字面3750图全部3750根独立BFS已实际通过，数学合法性不再只是局部／条件证书。',
        '完整参数、标准库generator及独立edge-list verifier已保存，生成器dry-run边集相等PASS，未重复旧103图。',
        '来源Mizuno F4 controller/框架与本项目F5参数变更署名分列；published比较与latest-global新颖性分列。'
    ],
    lesson_and_restart_condition='原F5正对照有明确构造价值；主表只到16度不能据此否定已验20度图。当前只主张N(20,3)>=3750的数学实例及超过特定已读published2783，不主张最新全球最大／公开采用。有限查新与完整Lean仍有具体缺口，不重跑全源验证或无关历史；下一投入依据真实问题决定。',
    unclosed_gap='Latest-global record/完整公开新颖性未确认；具体graph Lean的全图20regular、ediam<=3与导出边表对应尚未证明。局部定义/有限证书已编译，不计completeLean实例。',
    other_metrics=dict(
        mathematically_validated_complete_graph=True,validated_example_orders=[3750],
        mathematical_graph_validity='ACCEPTED',actual_n=3750,actual_m=37500,
        max_degree=20,min_degree=20,diameter_exact=3,simple=True,connected=True,
        roots_checked=3750,ordinary_bad_unordered_pairs_D3=0,
        ordered_distance_counts_including_self=validation['ordered_distance_counts_including_self'],
        ordinary_unordered_distance_counts=validation['ordinary_unordered_distance_counts'],
        generation_CPU_seconds=generation['CPU_seconds'],
        independent_validation_CPU_seconds=validation['CPU_seconds'],
        reproduction_CPU_seconds=repro['CPU_seconds'],
        CPU_sum_generation_validation_reproduction=generation['CPU_seconds']+validation['CPU_seconds']+repro['CPU_seconds'],
        original103_graphs_reverified=False,
        compared_published_lower_bound=2783,compared_published_as_of='September2026',
        baseline_checked_date='2026-10-29',improvement_versus_compared_published_bound=967,
        latest_global_record_confirmed=False,public_adoption=False,
        novelty_status='bounded-published-comparison-positive-latest-global-unconfirmed',
        primary_families_consulted=3,primary_families_with_numeric_contents=2,
        current_CW_value=None,exhaustive_literature_search=False,
        confirmed_publictable_record=False,
        legacy_record_counter_flag_note='No new_lower_bound_mathematically_verified flag is set: that legacy ledger flag counts confirmed public-table improvements. This graph is mathematically validated separately.',
        review_status='SUCCESS',review_verdict='ACCEPT_WITH_QUALIFICATIONS',
        review_requested_model=review['requestedModel'],review_returned_model=review['model'],
        review_effort=review['effort'],review_thread=review['threadId'],
        review_code_execution=False,
        formal_compiled_module='formal/DegreeDiameter/Portfolio/F5Graph3750.lean',
        formal_compiled_source_snapshot='research/ddp/refresh_20261029/f5_full_d20_D3/FORMAL_COMPILED_BINDING_SNAPSHOT.lean',
        formal_snapshot_scope='First successful definition/controller/root binding only; ongoing inverse/degree proof edits excluded.',
        formal_completed_finite_checks=['120 controller reverse ports','controller no loops and distinct ports','root20 distinct forward neighbors and adjacency'],
        formal_actual_compile_exit=0,complete_Lean_graph_instance=False,
        formal_degree_diameter_theorem_completed=False),
    report_paths=full_paths)

# A completed inverse/degree batch supersedes the earlier binding-only snapshot.
# Never relabel an active ediam edit as compiled merely because this batch passed.
inverse_path=full/'INVERSE_COMPILE_RESULT.json'
if inverse_path.exists():
    inverse=json.loads(inverse_path.read_text())
    assert inverse['compiled'] and inverse['exit_code']==0
    new_graph['other_metrics'].update(
        formal_compiled_source_snapshot=inverse['compiled_source_snapshot'],
        formal_snapshot_scope='Completed inverse/all-vertex adjacency and degree<=20 batch; later ediam edits excluded.',
        formal_inverse_inputs=2500,
        formal_forward_reverse_all_vertices=True,
        formal_adjacency_iff_forward_generators=True,
        formal_maximum_degree_at_most20_all_vertices=True,
        formal_full_regular_degree20_proved=False,
        formal_ediam_proved=False,
        formal_actual_compile_wall_seconds=inverse['wall_seconds'])
    new_graph['other_metrics']['formal_completed_finite_checks'] += [
        '2500 fiberStep_reverse inputs', 'forward_reverse for arbitrary Fin3750 vertices',
        'adjacency iff forward generators', 'degree_le_twenty for all vertices']
    new_graph['unclosed_gap']='Latest-global record/完整公开新颖性未确认。Lean全顶点degree<=20义务已闭；ediam<=3及导出边表Lean内对应未闭，completeLean仍0。精确20regular等号尚未Lean证明，但不是degree上界义务。'
    new_graph['report_paths'] += saved_paths(full,[
        'INVERSE_COMPILE_RESULT.json','FORMAL_COMPILED_INVERSE_SNAPSHOT.lean',
        'FORMAL_INVERSE_COMPILE_LOG.txt'])

# Final kernel receipts supersede the earlier partial compilation snapshots.
# These files are read only; preparing Wiki notes never invokes Lean.
final_path=full/'FINAL_COMPILE_RESULT.json'
if final_path.exists():
    final=json.loads(final_path.read_text())
    audit=json.loads((full/'PROOF_AUDIT.json').read_text())
    assert final['core_formula_Lean_verified'] and final['all_final_processes_terminal']
    assert final['final_decoder_batch']['all_modules_compiled']
    assert final['final_exact_batch']['all_modules_compiled']
    assert audit['audit_skill']=='proof-checker' and audit['proof_axis_status']=='verified'
    assert audit['deterministic_kernel_verdict']=='PASS'
    new_graph['other_metrics'].update(
        formal_compiled_module='formal/DegreeDiameter/Portfolio/F5Graph3750Exact.lean',
        formal_compiled_source_snapshot=final['source_snapshot_directory'],
        formal_snapshot_scope='Complete fixed Fin3750 formula graph: order3750, all-vertex degree<=20 and exact diameter3 in the project true-Walk definition.',
        complete_Lean_graph_instance=True,
        complete_deterministic_formula_Lean_graph_instances=1,
        formal_degree_diameter_theorem_completed=True,
        formal_DiameterAtMost_walk_definition_proved=True,
        formal_exact_diameter_three_proved=True,
        formal_full_regular_degree20_proved=False,
        literal_edge_text_equality_Lean=False,
        exact20regular_Lean=False,
        formal_ediam_proved=False,
        formal_mathlib_ediam_theorem_claimed=False,
        formal_concrete_construction_theorem=final['concrete_construction_theorem'],
        formal_exact_diameter_theorem=final['exact_diameter_theorem'],
        formal_controller_cells=900,
        formal_NB_decoder_checks=4500,
        formal_adjacent_decoder_checks=500,
        formal_axioms=final['axioms'],
        formal_sorry_used=False,formal_native_decide_used=False,formal_new_axioms_used=False,
        proof_checker_provenance=rel(full/'PROOF_AUDIT.json'),
        verified_claim_id='claim:ddp-f5-fin3750-order-degree20-exactd3-20261029',
        formal_final_decoder_batch=final['final_decoder_batch'],
        formal_final_exact_batch=final['final_exact_batch'],
        original103_complete_Lean_graph_instances=0)
    new_graph['other_metrics']['formal_completed_finite_checks'] += [
        '900 controller cells', '4500 NB decoder inputs', '500 adjacent decoder inputs',
        'arbitrary u,v actual graph Walk of length<=3',
        'actual vertices0 and6 have no Walk of length<=2',
        'closed concrete_order_degree_and_D3 and diameter_exact_three_in_project_definition']
    new_graph['failure_or_result']=new_graph['failure_or_result'].replace(
        '完整具体图Lean仍0。',
        '固定Fin3750参数公式图的完整Lean见证现为1：阶数3750、全顶点degree<=20、真实Walk定义恰D3均kernel通过；两个无额外前提定理仅用三项标准公理。旧103图Lean仍0。')
    new_graph['positive_guarantees'].append(
        'proof-checker审计PASS且最终kernel回执齐备：具体确定性公式图满足N(20,3)>=3750的数学见证；不以论文或模型意见替代kernel。')
    new_graph['unclosed_gap']='最新全球纪录／公开采用仍未确认。固定参数公式图的完整order/degree<=20/恰D3 Lean见证已完成1例。Lean未证明ASCII边表解析等同性、恰20正则或mathlib字面ediam等式；这些不是本次公式图见证的缺失前提。旧103图Lean仍0，整个Goal不据此完成。'
    new_graph['lesson_and_restart_condition']='保存具体固定参数公式图的kernel见证与最新global novelty分账。Goal允许确定性生成器及字面参数，故无需另加Lean文本parser门才接受本见证；不称世界纪录／全局最优，不重编旧源或复验旧103图。'
    new_graph['report_paths'] += saved_paths(full,[
        'FINAL_COMPILE_RESULT.json','PROOF_AUDIT.json','PROOF_AUDIT.md',
        'PROOF_SKELETON.md','FORMAL_INPUT_BINDING_CHECK.json','FORMAL_FINAL_SOURCES'])
    new_graph['report_paths'] += [
        'formal/DegreeDiameter/Portfolio/F5Graph3750Exact.lean',
        'formal/DegreeDiameter/Portfolio/F5Graph3750Diameter.lean']

variants=[]
for folder,res,label in [(globalnoise,g,'global_inverse_port_pairs_2_and_3'),(typenoise,t,'triangle3_externalC5_2')]:
    with (folder/'CASES.jsonl').open() as f:first=json.loads(next(f))
    v=dict(label=label,target_Delta=10,target_D=4,target=[10,4],savedL=2485,
        n=dict(actual=3750,hypothetical=None),m=18750,degree=10,
        actual_candidate_graphs=100,complete_cases=100,untested=0,
        complete_target_passes=0,first_failed_root=0,all_cases_root0_failed=True,
        actual_global_D=None,ordinary_bad_unordered_pairs=None,
        native_CPU_seconds=res['CPU_seconds'],
        first_case_first_missing=first['first_missing'],
        first_case_root_layers=first['last_root_layers'],
        joint_existence_prediction='REFUTED',source_BFS=0,
        exported_positive_graphs=0,new_solver_calls=0)
    if folder==typenoise:
        v.update(local_prediction='SUPPORTED',
            local_word=[0,1,2,3],local_controller_walk=[0,18,0,2,0],
            repaired_old_labels=[26,52],local_endpoint_plane_size=25,
            triangle_sets_checked=10,total_literal_cases_covered=100,
            local_check_new_graph_generation=0,local_check_new_BFS=0,
            local_check_CPU_seconds=local['CPU_seconds'])
    variants.append(v)
noise_paths=[]
for folder in [globalnoise,typenoise]:
    noise_paths+=saved_paths(folder,['PREDICTION.md','RESULT.json','INPUT_PARAMETERS.json',
        'CASES.jsonl','prepare.py','run.cpp','HANDLE.json'])
noise_paths += [rel(typenoise/'LOCAL_PREDICTION_CHECK.json')]
noise=dict(id=noise_id,
    title='Fixed F5 matrices, degree10/D4: global-port100 and triangle/external100 full root gates fail',
    family='four-label affine route-chart lifts',idea_family='idea:ddp-q3-three-step-plane-pencil31',
    record_type='complete-fixed-restricted-noise-candidate-graph-families',
    target_Delta=10,target_D=4,savedL=2485,baseline_date='2026-10-29',
    n=dict(actual=3750,hypothetical=None),actual_graph_Delta=10,actual_D=None,
    actual_D_scope='Each actual3750/18750 simple10regular candidate checked to first complete-root R4 counterexample; all200 fail atroot0. No exact global D/allpairs reported.',
    ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=None,
    outcome_class='complete-two-fixed-noise-families-no-D4-hit',date='2026-10-29',wiki_verdict='no',
    scope='原30controller、F5^3与四真逆矩阵固定。域一A0二元/A1取负、A2三元/A3取负，共100；域二真实triangle边三元、externalC5边二元，每无向边按u<v同类型集合、反向取负，共100。实际200个3750/18750/simple10regular图，未声称非同构；不是controller设置。每项首root0 R4失败即停该图，无导出positive。',
    failure_or_result='两域分别100/100全失败、0未试，nativeCPU0.082468/0.087869。旧global对称首例root layers[1,10,86,708,2474]，首漏26；新type首例[1,10,84,682,2471]，首漏6。type局部预测另真实10个triangle集×全部external选择覆盖100项：往返word[0,1,2,3]均得25点平面并修复旧26/52，CPU0.000858224、0新增图/BFS；局部SUPPORTED而globalexistenceREFUTED。普通无序坏对及exactglobalD未算。',
    positive_guarantees=[
        '真逆与系数取负保证无向，四目标controller互异保证simple；两域每点度10，新增真实噪声约束不继承full20度D3。',
        'type域与global域分支分配实质不同；任三元Atri差集F5给两次triangle往返的25点平面，旧26/52全100项实际修复。',
        '局部修复不能替代其余同fiber/跨fiber的共同R4覆盖；每项完整首root反例足以否定D4。'
    ],
    lesson_and_restart_condition='停止两个完整固定噪声域，不按缺点变少续seed／第三类型／field／参数。full-F5 20regular D3正图另列；不能拿两组10度失败回退其数学合法性，也不把200个失败候选算成200项成果。',
    unclosed_gap='其它噪声规则、矩阵／controller／连接机制或一般(10,4)图未排；本批无后续自动搜索。',
    variants=variants,
    other_metrics=dict(actual_candidate_graphs_generated=200,
        actual_graph_n=3750,actual_graph_m=18750,actual_graph_degree=10,
        graph_counts_by_variant={'global_port':100,'triangle_external':100},
        first_root_failures=200,source_BFS=0,solver_calls=0,untested=0,
        native_CPU_seconds_sum=g['CPU_seconds']+t['CPU_seconds'],
        local_saved_rule_check_CPU_seconds=local['CPU_seconds'],
        CPU_scope='Saved native worker timings; prepare/compile costs not reconstructed.',
        actual_global_D=None,ordinary_bad_unordered_pairs=None,
        new_lower_bound_mathematically_verified=False,
        same_affine_family_not_independent_methods=True),report_paths=noise_paths)

source=copy.deepcopy(next(r['source_record'] for r in ledger['rows'] if r['id']=='ddp-wave4-mizuno-d3-source'))
source['matched_existing_id']='ddp-wave4-mizuno-d3-source'
for v in source.get('variants',[]):
    if v.get('label')=='fixed_F5_complementary_triples_and_adjacent_pencils_20261029':
        v['subsequent_literal_graph_status']='MATH_ACCEPTED_FULL3750; see dedicated experiment'
        v['subsequent_literal_graph_experiment']='exp:'+full_id
        v['subsequent_actual_n']=3750
        v['subsequent_actual_D']=3
        v['latest_global_novelty']='pending; checked published2783 only'
source['other_metrics']['F5_literal_graph_followup']={'experiment_id':'exp:'+full_id,'actual_n':3750,'m':37500,'degree':20,'D_exact':3,'mathematical_validity':'accepted','latest_global_record_confirmed':False,'complete_Lean_instance':bool(new_graph['other_metrics']['complete_Lean_graph_instance'])}
extra=' 后续full3750已实际生成并从边表独立all3750roots验收simple/20regular/exactD3，不再是未导图；published2783比较+967、最新global待确认，沿独立literalgraph实验记录。早期local控制中“未导图／未比较”是当时阶段，已由此后续补齐实际边表与有界比较，不能回退最新状态。'
if extra.strip() not in source['failure_or_result']:source['failure_or_result']+=extra
source['report_paths']=list(dict.fromkeys(source.get('report_paths',[])+[rel(full/'README.md'),rel(full/'INDEPENDENT_VALIDATION.json'),'reviews/ddp/f5_full3750_20261029.DISPOSITION.md']))

# Preserve later additive diagnostics when preparing the same three old nodes.
# Current canonical formal fields above still take precedence over old values.
for row in [source,new_graph,noise]:
    previous=next((r['source_record'] for r in ledger['rows'] if r['id']==row['id']),None)
    if previous:
        row['other_metrics']={**previous.get('other_metrics',{}),**row.get('other_metrics',{})}
        labels={v.get('label') for v in row.get('variants',[])}
        row['variants']=[v for v in previous.get('variants',[]) if v.get('label') not in labels]+row.get('variants',[])
        row['report_paths']=list(dict.fromkeys(previous.get('report_paths',[])+row['report_paths']))
    for path in row.get('report_paths',[]):assert (ROOT/path).exists(),path
    assert not capture_filter.screen(json.dumps(row,ensure_ascii=False))
(HERE/'F5_TERMINAL_WIKI_ROWS.json').write_text(json.dumps([source,new_graph,noise],ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(updated_source='ddp-wave4-mizuno-d3-source',new_literal_graph_experiment=full_id,
    new_combined_noise_experiment=noise_id,new_method_claims=0,
    new_ledger_rows=sum(rid not in {r['id'] for r in ledger['rows']} for rid in [full_id,noise_id]),
    raw=rel(HERE/'F5_TERMINAL_WIKI_ROWS.json'),computations_rerun=0),ensure_ascii=False))

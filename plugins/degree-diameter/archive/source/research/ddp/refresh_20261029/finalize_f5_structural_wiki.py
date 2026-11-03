"""Accept the saved review disposition and serially update existing F5 nodes.

Persistence only: no algebra, graph, BFS, solver, Lean, web access or hash.
"""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import json
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
WIKI=ROOT/'research-wiki'
sys.path.insert(0,str(ROOT/'aris_repo/tools'))
import capture_filter
import research_wiki as helper

def rel(p):return str(p.relative_to(ROOT))
def screened(text):
    found=capture_filter.screen(text)
    assert not found,found
    return text
def add_paths(row,paths):
    assert all((ROOT/p).exists() for p in paths)
    row['report_paths']=list(dict.fromkeys(row.get('report_paths',[])+paths))
def append_result(row,paragraph):
    if paragraph not in row['failure_or_result']:
        row['failure_or_result']+=' '+paragraph

before=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count']==368
claims_before=sorted(p.name for p in (WIKI/'claims').glob('*.md'))
exps_before=sorted(p.name for p in (WIKI/'experiments').glob('*.md'))
rows=json.loads((HERE/'F5_STRUCTURAL_PENDING_REVIEW_WIKI_ROWS.json').read_text())
full=next(r for r in rows if r['id']=='ddp-f5-full3750-d20-d3-validated-novelty-pending-20261029')
source=next(r for r in rows if r['id']=='ddp-wave4-mizuno-d3-source')
noise=next(r for r in rows if r['id']=='ddp-f5-fixed3750-restricted-noise-d10d4-two100-families-20261029')
review_rel='reviews/ddp/f5_d10_oddcycle_20261029.response.json'
disp_rel='reviews/ddp/f5_d10_oddcycle_20261029.DISPOSITION.md'
prompt_rel='reviews/ddp/f5_d10_oddcycle_20261029.prompt.md'
review=json.loads((ROOT/review_rel).read_text())['structuredContent']
disposition=(ROOT/disp_rel).read_text()
assert review['status']=='SUCCESS'
assert 'SOUND AS STATED' in review['content'] and 'SOUND AS STATED' in disposition
assert '10^60' in disposition

ov=next(v for v in noise['variants'] if v['label']=='edgewise_independent_tri3_ext2_fixed_matrices_oddC5_obstruction_20261029')
ov.update(status='MATHEMATICALLY_ACCEPTED_FIXED_EDGEWISE_FAMILY_D4_EXCLUDED',
    review_status='SUCCESS',review_verdict='SOUND AS STATED (NO FLAWS FOUND)',
    review_disposition=disp_rel,review_response=review_rel,
    review_model=review['model'],review_effort=review['effort'],review_thread=review['threadId'],
    review_code_execution=False,review_new_BFS=False,
    prediction='SUPPORTED_BY_FINAL_EXACT_CERTIFICATES_AND_ACCEPTED_SCOPED_PROOF',
    accepted_closed_scope='All10^60 literal fixed per-controller-edge3/2 subset assignments with the old fixed matrices/directions and no dependence on fiber coordinate.',
    proof_status='mathematically_accepted_finite_exact_algebra_not_Lean',
    excluded_only_after_review=None)
ov['evidence_paths']+= [review_rel,disp_rel,prompt_rel]
add_paths(noise,[review_rel,disp_rel,prompt_rel])
noise['other_metrics']['edgewise_tri3_ext2_obstruction']={
    'mathematically_accepted':True,'literal_parameter_settings':'10^60',
    'actual_full_settings_enumerated':0,'new_graphs':0,'new_BFS':0,
    'formalized_in_Lean':False,'new_Lean_instances':0,
    'fixed_controller_and_matrices':True,'coefficients_independent_of_fiber_coordinate':True,
    'review_status':'SUCCESS','review_verdict':'SOUND AS STATED',
    'review_disposition':disp_rel,'final_cycle_CPU_seconds':4.40427237}
append_result(noise,'后续从原200项样本升级为数学统一排除：固定旧controller/矩阵/方向、每条边独立选择且不随x变化的triangle3/external2系数，全部10^60字面赋值不能D4；依据五根完整局部短闭路线及奇五环差集交替矛盾，最终有限检查CPU4.40427237，实际全图枚举0。一次Gemini实际SUCCESS/SOUND AS STATED，静态审阅不冒新数值或Lean。')

flat=HERE/'f5_flat_conic_local'
fr=json.loads((flat/'RESULT.json').read_text())
assert fr['status']=='SINGLE_CONIC_LOCAL_PREDICTION_REFUTED'
flat_paths=[rel(flat/n) for n in ['PREDICTION.md','INPUT.json','RESULT.json','REPORT.md','TERMINAL.json','check_local.py']+
            [f'ROOT_{r}.json' for r in [0,20,28,22,9]]]
add_paths(noise,flat_paths)
flat_variant=dict(label='one_flat_identity_matrix_proper6color_conic_control_20261029',
    status=fr['status'],prediction='REFUTED',target_Delta=10,target_D=4,
    n=dict(actual=None,hypothetical=3750),actual_expanded_graph=None,
    rule='All matrices I; conic vectors(1,t,t^2),t inF5,and(0,0,1); one canonical proper6edge-coloring; triangle{0,1,-1},external{1,-1}.',
    changed_matrices=True,covered_by_old_matrix_oddcycle_proof=False,
    exact_scope='One deterministic conic coloring with symmetric3/2 coefficients; not all identity-map lifts/direction assignments.',
    literal_candidate_rules=1,roots=[0,20,28,22,9],
    same_fiber_endpoint_counts=[r['total'] for r in fr['roots']],
    all_source_coordinates_equivalent_by_translation=True,
    exact_counterexample=dict(controller=0,source_fiber_coordinate=[0,0,0],
        target_fiber_displacement=[0,2,0],reachable_within4=False),
    actual_global_D=None,connectivity=None,ordinary_bad_unordered_pairs=None,
    whole_graphs_expanded=0,new_BFS=0,new_solver_calls=0,
    new_controller_word_enumerations=0,coloring_searches=0,
    CPU_seconds=fr['CPU_seconds'],new_Lean_instances=0,evidence_paths=flat_paths)
noise['variants']=[v for v in noise['variants'] if v.get('label')!=flat_variant['label']]+[flat_variant]
noise['other_metrics']['changed_matrix_single_control']={
    'H_identity':True,'local_prediction':'REFUTED','same_fiber_counts':[111,111,107,111,105],
    'actual_full_graphs':0,'BFS':0,'global_D':None,'CPU_seconds':fr['CPU_seconds']}
append_result(noise,'一次实质改矩阵对照另列：全部T改I、唯一proper6color圆锥方向和对称3/2系数，同fiber五根仅111/111/107/111/105，root0位移(0,2,0)不可≤4；CPU.019305658、0展开图/BFS。仅关该一控制，不用旧矩阵奇环命题冒排所有平移提升。')
noise['lesson_and_restart_condition']='停止旧固定矩阵全部edgewise/x-independent3/2系数域，不按seed或缺点分数续算；改变矩阵后单个flat-conic控制仍失败，亦停止该具体规则。不同矩阵、coordinate-dependent系数、不同branch分配和一般(10,4)仍开放；本批无下一搜索自动授权。'
noise['unclosed_gap']='已接受的统一排除只作用于固定旧controller/四矩阵/方向且系数逐边固定、不随x变化的3/2域。新增T=I对照仅单规则失败；一般平移提升、coordinate-dependent系数、其它branch或控制器和一般3750点10度D4不排。'

append_result(full,'后续固定源纯删边诊断证明37500边全部D3critical：120定向控制弧均有远端唯一3path并且36噪声词可逆；任非空纯删边保全3750点都会失D3。未实际生成删边图或重跑源BFS，不排重接/加入新边。')
full['other_metrics']['edge_criticality_producer_CPU_seconds']={
    'controller_and_rank':0.002462428,'pencil_summary':0.003276951}

qv=next(v for v in source['variants'] if v['label']=='fixed_F5_translation_quotient750_and_ordinary_cover_ceiling_20261029')
qv.update(target_Delta=20,target_D=3)
source['other_metrics']['fixed_F5_quotient_transfer']={
    'prediction_no_translation':'REFUTED','translation_nullity':1,'h':[0,3,1],
    'formula_quotient_n':750,'maxdegree':20,'exact_D':3,'actual_edge_export':False,
    'source_is_ordinary_5sheet_cover':True,'fixed_quotient_D3_cover_sheet_ceiling':5,
    'new_improved_graph_examples':0,'new_Lean_instances':0,
    'CPU_seconds':0.046521764}
append_result(source,'后续F5商诊断推翻“无共同平移”预测：h=(0,3,1)给750点20正则D3公式商，3750原图为其普通5重cover。缓存unique0→3控制词与投影rank2证明该固定750商的D3普通cover层数≤5。CPU.046521764、0新图/BFS/路线枚举；该商被原3750支配，不增目标合法改进例数。')

follow=HERE/'f5_complementary_triples/20D3_targeted_followup_20261029'
follow_result=json.loads((follow/'RESULT.json').read_text())
assert follow_result['new_accesses_or_queries']==3
assert follow_result['current_CombinatoricsWiki_20D3_value'] is None
assert follow_result['latest_global_record_confirmed'] is False
follow_paths=[rel(follow/n) for n in ['SCOPE.json','RESULT.json','REPORT.md','TERMINAL.json',
    'ACCESS_1_SEARCH_RECEIPT.json','ACCESS_2_RECEIPT.json','ACCESS_3_RECEIPT.json']]
add_paths(full,follow_paths)
full['other_metrics']['bounded_20D3_novelty_followup']={
    'new_accesses_or_queries':3,'new_numeric_primary_contents_obtained':0,
    'current_maintained_value':None,'entry_revision_date':None,
    'latest_global_record_confirmed':False,'old_baseline_receipts_unchanged':True,
    'additional_requests_queued':False,'absence_is_not_a_novelty_proof':True}
full['variants'].append(dict(label='bounded_three_access_20D3_followup_pending_20261029',
    status='BOUNDED_FOLLOWUP_STOPPED_MAINTAINED_VALUE_PENDING',new_accesses_or_queries=3,
    new_numeric_primary_contents=0,current_maintained_value=None,latest_global_record_confirmed=False,
    inherited_numerical_comparison=dict(order=2783,asof='September2026',difference=967),
    observation_scope='No maintained20D3 numeric contents obtained; no inference of absent earlier3750 construction.',
    new_graphs=0,new_BFS=0,new_Lean_instances=0,evidence_paths=follow_paths))

turn=rel(HERE/'F5_STRUCTURAL_TURN_RESULT.json')
for row in rows:
    add_paths(row,[turn])
    screened(json.dumps(row,ensure_ascii=False))
raw_path=HERE/'F5_STRUCTURAL_FINAL_WIKI_ROWS.json'
raw_path.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
command=[sys.executable,'research/ddp/more_graphs_20261027/sync_additional_probes.py',rel(raw_path)]
sync=subprocess.run(command,cwd=ROOT,text=True,capture_output=True,check=True)
sync_receipt=json.loads(sync.stdout)
assert sync_receipt['record_count']==368 and sync_receipt['complete_Lean_graph_instances']==1

summary='''本次数学结构批次全部终态：完整3750图的37500边各有唯一≤3path远端见证，故保全顶点的任非空纯删边不能保持D3；共同平移h=(0,3,1)给750点20regular/D3公式商，且缓存唯一控制词给该固定商普通D3覆盖最多5层。两项均无新大图／BFS，750商不计改进例。

旧固定四矩阵的降度域现由五环矛盾统一排除：每条triangle边独立任3子集／每条external边独立任2子集，系数不随纤维坐标变化；10^60为字面赋值量，实际完整图枚举0。最终局部有限证据4.40427237CPU，一次实际Gemini SUCCESS／SOUND AS STATED；新排除未Lean化，不增加verified claim。初始同边四次通过差集错误保留历史，最终采用两个差集之和。

该负反馈促成一次真正改矩阵的I-map圆锥6色控制：五同fiber端点数111/111/107/111/105，root0位移(0,2,0)缺失，局部预测失败。没有展开图／BFS，不能外推全部平移提升。三个追加查新访问未得到维护表数值，原published2783比较保持，最新全球novelty仍pending；不把访问缺口当不存在先例的证据。

本轮是改变允许下一动作的数学结构判断，不是新增完整图；上一专家交付turn为资料交付progress，不冒数学突破。数学合法104／4、confirmed主表103／3、具体公式图Lean1、pending1及Goal ACTIVE不变；账本368条仍为来源／实验／变体记录，不是方法数。本次Wiki写入不启动任何新计算。'''
screened(summary)
report='''# F5 structural results merged into existing experiments

'''+summary+'''

Evidence: f5_d20_edge_criticality_20261029/EDGE_CRITICALITY.md; f5_fiber_quotient_transfer/REPORT.md; f5_d10_closed_route_diagnosis/PROOF_PACKAGE.md and CYCLE_RESULT.json; reviews/ddp/f5_d10_oddcycle_20261029.DISPOSITION.md; f5_flat_conic_local/REPORT.md; F5_STRUCTURAL_TURN_RESULT.json.

Three existing nodes updated; zero new experiment nodes, ledger rows or verified claim nodes. Root-owned brief, plan, recovery and HTML were not edited by this writer; a final query refresh follows the root's new brief.
'''
(HERE/'F5_STRUCTURAL_FINAL_WIKI_REPORT.md').write_text(screened(report))

comments=WIKI/'DD82_PROGRESS_AND_COMMENTS_20261018.md'
marker='<!-- F5_STRUCTURAL_TURN_20261029_TERMINAL -->'
if marker not in comments.read_text():
    note='\n\n'+marker+'\n## 2026-10-29 F5数学结构检验终态\n\n这是执行记录，不是新用户原话。\n\n'+summary+'\n\n[本轮结果](../research/ddp/refresh_20261029/F5_STRUCTURAL_TURN_RESULT.json)；[合并报告](../research/ddp/refresh_20261029/F5_STRUCTURAL_FINAL_WIKI_REPORT.md)；[实际审阅处置](../reviews/ddp/f5_d10_oddcycle_20261029.DISPOSITION.md)。\n'
    comments.write_text(comments.read_text().rstrip()+screened(note))

idea=WIKI/'ideas/ddp-q3-three-step-plane-pencil31.md'
marker='<!-- F5_STRUCTURAL_TURN_20261029 -->'
if marker not in idea.read_text():
    note='\n\n'+marker+'\n## 从局部失败到完整固定域障碍\n\n'+summary+'\n\n[证明与有限证据](../../research/ddp/refresh_20261029/f5_d10_closed_route_diagnosis/PROOF_PACKAGE.md)；[纯删边见证](../../research/ddp/refresh_20261029/f5_d20_edge_criticality_20261029/EDGE_CRITICALITY.md)；[750商及覆盖上限](../../research/ddp/refresh_20261029/f5_fiber_quotient_transfer/REPORT.md)。\n'
    text=idea.read_text();idea.write_text(text.replace('\n## Connections\n',screened(note)+'\n## Connections\n',1))
with (HERE/'F5_STRUCTURAL_FINAL_WIKI.sync.log').open('a') as log,contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI),'F5 structural turn: three existing nodes gain edge-criticality, fixed quotient/cover ceiling, accepted fixed-matrix oddcycle exclusion and one failed identity-map control; no new ledger/claim nodes or improved graph/Lean instances. Ledger368;104/4 versus confirmed103/3;Lean1;novelty pending. Root brief untouched.')

# Keep the saved combined raw consistent with the latest same-node diagnostics.
combined=HERE/'F5_TERMINAL_WIKI_ROWS.json'
old=json.loads(combined.read_text());byid={r['id']:r for r in rows}
combined.write_text(json.dumps([byid.get(r['id'],r) for r in old],ensure_ascii=False,indent=2)+'\n')

after=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert len(after['rows'])==after['record_count']==368
assert after['validated_graph_examples_including_novelty_pending']==104
assert after['validated_parameter_pairs_including_novelty_pending']==4
assert after['confirmed_publictable_graph_examples']==103
assert after['confirmed_publictable_improved_parameter_pairs']==3
assert after['complete_Lean_graph_instances']==1 and after['novelty_pending_valid_graph_examples']==1
assert sorted(p.name for p in (WIKI/'claims').glob('*.md'))==claims_before
assert sorted(p.name for p in (WIKI/'experiments').glob('*.md'))==exps_before
errors=[]
for row in rows:
    p=WIKI/'experiments'/f"{row['id']}.md"
    text=p.read_text()
    for name in ['type','node_id','title','verdict','idea_id','provenance']:
        if not re.search(rf'(?m)^{name}:',text):errors.append(f'{p.name}: missing{name}')
    for target in re.findall(r'\]\(([^)]+)\)',text):
        if '://' not in target and not target.startswith('#') and not (p.parent/target.split('#')[0]).exists():
            errors.append(f'{p.name}:missinglink{target}')
assert not errors,errors
receipt=dict(status='PASS_F5_STRUCTURAL_FINAL_EXISTING_NODE_LINT',
    applied_UTC=datetime.now(timezone.utc).isoformat(),
    existing_ids_updated=['exp:'+r['id'] for r in rows],new_ledger_rows=0,
    record_count=368,new_experiment_nodes=0,new_claim_nodes=0,
    validated_graph_examples=104,validated_parameter_pairs=4,
    confirmed_publictable_examples=103,confirmed_publictable_pairs=3,
    complete_Lean_graph_instances=1,new_Lean_graph_instances=0,
    novelty_pending_examples=1,goal_status='ACTIVE',
    actual_10pow60_full_graph_enumerations=0,
    oddcycle_review_status=review['status'],oddcycle_review_model=review['model'],
    oddcycle_review_verdict='SOUND AS STATED (NO FLAWS FOUND)',review_disposition=disp_rel,
    flat_control_scope='One deterministic changed-matrix conic rule only',
    new_numerics_by_writer=0,new_BFS_by_writer=0,new_compilations_by_writer=0,
    new_solver_calls_by_writer=0,new_external_reviews_by_writer=0,
    root_owned_files_edited=False,
    final_query_refresh='Deferred until root refreshes brief; normal experiment helper rebuilt its ordinary derived query during upserts.',
    command=' '.join(command),lint_scope='Touched experiment schemas and local links, unchanged node sets and separated math/formal/novelty counts',lint_errors=errors)
(HERE/'F5_STRUCTURAL_FINAL_WIKI_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False))

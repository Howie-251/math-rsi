"""Persist saved final kernel receipts and the one bounded 11D6 resource gate.

No graph generation, compiler, BFS, radius query, solver or reviewer is invoked.
The existing ledger helper and canonical ARIS claim/edge helpers own writes.
"""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import copy
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
WIKI = ROOT / 'research-wiki'
sys.path.insert(0, str(ROOT / 'aris_repo/tools'))
import capture_filter
import research_wiki as helper

FULL_ID = 'ddp-f5-full3750-d20-d3-validated-novelty-pending-20261029'
OLD_SOURCE_ID = 'ddp-wave4-mizuno-d3-source'
SOURCE11_ID = 'ddp-d11-d6-current186033-source-20261027'
CLAIM_SLUG = 'ddp-f5-fin3750-order-degree20-exactd3-20261029'
CLAIM_ID = 'claim:' + CLAIM_SLUG
FULL = HERE / 'f5_full_d20_D3'
LAYER = HERE / 'd11_D6_mechanism_read/layer_binding'

def rel(p):
    return str(p.relative_to(ROOT))

def screened(text):
    findings = capture_filter.screen(text)
    assert not findings, findings
    return text

before = json.loads((WIKI / 'DDP_METHOD_LEDGER.json').read_text())
assert len(before['rows']) == 368
raw = json.loads((HERE / 'F5_TERMINAL_WIKI_ROWS.json').read_text())
full = copy.deepcopy(next(r for r in raw if r['id'] == FULL_ID))
old_source = copy.deepcopy(next(r for r in raw if r['id'] == OLD_SOURCE_ID))
assert full['other_metrics']['complete_Lean_graph_instance']
assert full['other_metrics']['formal_exact_diameter_three_proved']
audit = json.loads((FULL / 'PROOF_AUDIT.json').read_text())
assert audit['audit_skill'] == 'proof-checker'
assert audit['proof_axis_status'] == 'verified'
assert audit['deterministic_kernel_verdict'] == 'PASS'
assert audit['fatal_issues'] == 0 and audit['critical_issues'] == 0
assert audit['formal_graph_instances_completed'] == 1
final = json.loads((FULL / 'FINAL_COMPILE_RESULT.json').read_text())
assert final['core_formula_Lean_verified'] and final['diameter_exact'] == 3
assert not final['literal_edge_file_equality_Lean_verified']
assert not final['degree_exact20_Lean_verified']

source = copy.deepcopy(next(r['source_record'] for r in before['rows'] if r['id'] == SOURCE11_ID))
source['matched_existing_id'] = SOURCE11_ID
layer = json.loads((LAYER / 'RAW_ANALYSIS_FIELDS.json').read_text())
variant_label = 'actual_tower_prefix_and_fixed_K6_halfclass_capacity_20261029'
variant = dict(label=variant_label, record_type='source-label-binding-and-fixed-rule-resource-gate',
    target_Delta=11, target_D=6, source_n=186033,
    n=dict(actual=None, hypothetical=186039),
    status=layer['status'],
    scope=layer['scope'],
    result=layer['result'],
    prefix_signature_prediction='SUPPORTED',
    six_half_free_port_prediction='REFUTED',
    closed_scope=layer['closed_scope'], unclosed_gap=layer['unclosed_gap'],
    source_D6_BFS=0, new_balls=0, solver_calls=0, candidate_graphs=0,
    measured_successful_worker_CPU_seconds=layer['measured_successful_worker_CPU_seconds'],
    other_half_class_counts='H7 color1 and both H5 colors not checked after decisive H7 color0 failure',
    evidence_paths=layer['report_paths'])
source['variants'] = [v for v in source.get('variants', []) if v.get('label') != variant_label] + [variant]
source.setdefault('other_metrics', {})['tower_prefix_and_fixed_K6_gate'] = {
    'prefix_signature': 'SUPPORTED', 'fixed_K6_capacity': 'REFUTED',
    'successful_worker_CPU_seconds': 1.214964867,
    'four_connected_bipartite_layer_checks': 4,
    'opposite_color_two_anchor_checks': 63030,
    'H9_half_free_counts': [12353, 12280], 'H7_color0_free_count': 0,
    'half_classes_checked': 3, 'half_classes_unchecked': 3,
    'source_D6_distance_BFS': 0, 'new_balls': 0, 'solver_calls': 0,
    'candidate_graphs': 0, 'alternative_partitions_tried': 0,
    'generalized_hexagon_isomorphism_proved': False,
    'fixed_K6_closed_only': True}
addition = (' 后续一次真实prefix标签门通过四层degree/连通二分签名与63030异色双锚条件；'
    '固定K6所需六半类资源门被H7 color0的0个free反驳，CPU1.214964867。'
    '另三半类未计数；未生成K6图／新球／solver或重验sourceD6，不外推其它helper规则。')
if addition.strip() not in source['failure_or_result']:
    source['failure_or_result'] += addition
source.setdefault('positive_guarantees', []).append(
    'Actual four-prefix degree/connectivity/bipartition and opposite-color anchor signatures bind cached labels; this does not prove generalized-hexagon isomorphism or internal D6.')
source['positive_guarantees'] = list(dict.fromkeys(source['positive_guarantees']))
source['unclosed_gap'] = ('已闭固定mandatory9+至多2guard及本次固定K6半类资源规则；'
    '一般11D6增广、其它helper连接规则、内部几何同构未排。H7 color1及H5两色资源未在本门统计。')
source['report_paths'] = list(dict.fromkeys(source.get('report_paths', []) + layer['report_paths']))

rows = [old_source, full, source]
for row in rows:
    screened(json.dumps(row, ensure_ascii=False))
    for path in row['report_paths']:
        assert (ROOT / path).exists(), path
raw_path = HERE / 'F5_FINAL_LEAN_AND_LAYER_WIKI_ROWS.json'
raw_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
command = [sys.executable, 'research/ddp/more_graphs_20261027/sync_additional_probes.py', rel(raw_path)]
sync = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=True)
sync_receipt = json.loads(sync.stdout)
assert sync_receipt['record_count'] == 368
assert sync_receipt['complete_Lean_graph_instances'] == 1

statement = '''固定 `DegreeDiameter.Portfolio.F5Graph3750.graph : SimpleGraph (Fin 3750)` 满足：

- 顶点数为3750；
- 对每个顶点u，`graph.degree u ≤ 20`；
- 对每个u,v，存在真实图上Walk，长度≤3；并且存在一对顶点没有长度≤2的Walk，故直径恰3。

这是具体确定性参数图的存在见证，给出数学下界 `N(20,3) ≥ 3750`。
最终无参数、无额外前提的Lean定理为 `concrete_order_degree_and_D3` 与 `diameter_exact_three_in_project_definition`。'''
scope = '''只针对本节点所链接的固定30控制器、F5矩阵／方向／逆端口字面参数以及编码 `125*a+x0+5*x1+25*x2` 定义的公式图，不是一般F5族或任意输入图定理。真实直径使用项目定义 `DiameterAtMost G D := ∀u v, ∃p : G.Walk u v, p.length ≤ D`；未另称mathlib字面ediam定理。

Lean没有解析并证明磁盘ASCII边表等于公式图，也没有证明所有顶点度数恰20。二者均不影响本次阶数／最大度／真实直径构造见证；Goal允许确定性生成器与字面参数。边表本身已有独立全3750根验收，但不能把它写成Lean文本解析定理。

最新全球纪录、最优性与公开采用未确认。已核对published2783的比较与本数学下界分账；旧103个confirmed主表图并未因此获得Lean证明，整个Goal未据此完成。'''
evidence = f'''证明出生依据：[proof-checker审计]({ '../../' + rel(FULL/'PROOF_AUDIT.json') })，`proof_axis_status=verified`、`deterministic_kernel_verdict=PASS`、fatal/critical均0。

- [最终编译与公理回执](../../{rel(FULL/'FINAL_COMPILE_RESULT.json')})：最终decoder与exact批均COMPLETE、相关模块exit0；900控制器单元、4500 NB decoder与500 adjacent decoder已在kernel核验。
- [输入绑定](../../{rel(FULL/'FORMAL_INPUT_BINDING_CHECK.json')})：controller、matrix、direction、inversePort四组字面数据与PARAMETERS匹配；坐标／噪声公式与生成器匹配。
- [完整成功源快照](../../{rel(FULL/'FORMAL_FINAL_SOURCES')})、[证明骨架](../../{rel(FULL/'PROOF_SKELETON.md')})与[审计正文](../../{rel(FULL/'PROOF_AUDIT.md')})。

两个最终定理仅依赖 `propext`、`Classical.choice`、`Quot.sound`；没有sorry、新增公理或native_decide。fresh只读语义审阅标same-family/provisional，确定性验收依据是实际Lean kernel，不以模型同意、论文或Python输出代替证明。本次Wiki写入没有重编译、BFS或求解。'''
for text in [statement, scope, evidence]:
    screened(text)
# Repair only the two case-mismatched endpoints caught by the first delta lint.
# Their replacement edges are written by add_edge below, with canonical IDs.
edge_path = WIKI / 'graph/edges.jsonl'
old_case_id = CLAIM_ID.replace('exactd3', 'exactD3')
existing_edges = [json.loads(s) for s in edge_path.read_text().splitlines() if s.strip()]
mistyped = [e for e in existing_edges if old_case_id in (e['from'], e['to'])]
if mistyped:
    assert all((e['from'],e['type'],e['to']) in [
        ('exp:'+FULL_ID,'supports',old_case_id),
        (old_case_id,'tested_by','exp:'+FULL_ID)] for e in mistyped)
    retained = [e for e in existing_edges if e not in mistyped]
    edge_path.write_text(''.join(json.dumps(e,ensure_ascii=False)+'\n' for e in retained))
with (HERE / 'F5_FINAL_LEAN_WIKI.sync.log').open('w') as log, contextlib.redirect_stdout(log):
    claim_path = helper.add_claim(str(WIKI), CLAIM_SLUG,
        '具体Fin3750公式图：阶数3750、最大度≤20、直径恰3',
        description='Kernel-verified fixed deterministic formula graph witnesses N(20,3)>=3750; latest-global novelty remains unconfirmed.',
        status='verified', provenance=rel(FULL/'PROOF_AUDIT.json'),
        statement=statement, scope=scope, evidence=evidence,
        tags=['degree-diameter', 'Lean-kernel', 'fixed-formula-graph', 'diameter3'],
        addresses=['DDP1'], update_on_exist=True)
    helper.add_edge(str(WIKI), 'exp:'+FULL_ID, CLAIM_ID, 'supports',
        'Same fixed literal parameters; full graph experiment and final proof-checker/kernel receipts support this concrete formula-graph statement. Latest-global novelty is outside scope.')
    helper.add_edge(str(WIKI), CLAIM_ID, 'exp:'+FULL_ID, 'tested_by',
        'Concrete Fin3750 order/degree-bound/exact-D3 kernel witness is stored with the existing full3750 experiment; no new graph experiment.')

idea = WIKI / 'ideas/ddp-q3-three-step-plane-pencil31.md'
text = idea.read_text().replace(old_case_id[6:], CLAIM_SLUG)
text = text.replace('已产出独立验收的3750点20regular/D3图；最新global novelty和完整Lean仍待定。',
    '已产出独立验收的3750点20regular/D3图；固定公式图完整Lean见证已完成1例，最新global novelty仍待定。')
text = text.replace('原局部检验并未重复，最新global novelty与完整Lean仍未决。',
    '原局部检验并未重复；后续公式图完整Lean已闭，最新global novelty仍未决。')
old_start = '新的[Fin3750定义与有限证书编译快照]' if '新的[Fin3750定义与有限证书编译快照]' in text else '原binding-only与inverse-only编译快照'
start = text.index(old_start)
end = text.index('\n\n当前通过目标度数', start)
paragraph = f'''原binding-only与inverse-only编译快照保留为历史；当前[最终kernel回执](../../{rel(FULL/'FINAL_COMPILE_RESULT.json')})已完成固定Fin3750公式图的完整见证：全顶点degree≤20、全u/v真实Walk长≤3，以及实际0→6无≤2步路，所以恰D3。900控制器单元、4500／500 decoder已核，两个最终定理无额外假设、仅三项标准公理。见[verified claim](../claims/{CLAIM_SLUG}.md)及[proof-checker审计](../../{rel(FULL/'PROOF_AUDIT.json')})。完整具体公式图Lean实例现为1；不声称Lean文本parser等同性、恰20正则或mathlib字面ediam等式。旧103图Lean仍0。'''
text = text[:start] + paragraph + text[end:]
text = text.replace('没有新增proved claim节点。', '新增1个由proof-checker出生的固定参数公式图verified claim，不把实例／变体数当独立方法数。')
text = text.replace('Current-global record novelty and complete formal degree/diameter remain unresolved;',
    'Current-global record novelty remains unresolved; the fixed formula graph now has a complete kernel-verified order/degree-bound/exact-diameter witness;')
idea.write_text(screened(text))

gap = WIKI / 'gap_map.md'
text = gap.read_text()
text = text.replace('完整具体Lean实例0。旧D2暂停；以下旧“当前”段仅作历史。',
    '完整具体确定性公式图Lean实例1（新3750图）；旧103图Lean仍0。旧D2暂停；以下旧“当前”段仅作历史。', 1)
start = text.index('<!-- F5_LITERAL_CURRENT_20261029 -->')
end = text.index('\n---', start)
current = f'''<!-- F5_LITERAL_CURRENT_20261029 -->
当前：[3750点20regular/D3字面图](experiments/{FULL_ID}.md)已独立全3750根通过；固定参数公式图进一步完成完整Lean实例1，见[verified claim](claims/{CLAIM_SLUG}.md)：阶数3750、全顶点degree≤20及真实Walk定义恰D3，无额外假设、仅三项标准公理。字面边表的Lean解析等同性／恰20正则等号未证，均不冒充结论或额外验收门。最新global novelty仍待确认，confirmed主表103／3与数学合法104／4保持。

两种10度噪声100域均停止；局部26/52修复不能替代全D4。11D6新一次prefix标签结构门SUPPORTED，四层连通二分与63030双锚条件真实通过；固定K6半类资源被H7 color0 free0阻断，1.214964867CPU，无新球／solver／图，余三半类未计数，不排一般协作规则。'''
text = text[:start] + current + text[end:]
gap.write_text(screened(text))

map_path = WIKI / 'ideas/ddp-math-challenges-and-records.md'
text = map_path.read_text().replace('完整Lean仍0，已有实际编译的Fin3750局部绑定不当作完整证明。',
    '完整固定公式图Lean现1：Fin3750阶数／degree≤20／真实Walk恰D3全部kernel通过；旧103图Lean仍0。Lean文本解析等同性和恰20正则未证，不冒充结论。')
map_path.write_text(screened(text))

report = '''# Final formula-graph Lean witness and bounded11D6 gate persisted

The fixed Fin3750 formula graph now has one completed kernel-verified graph instance: order3750, all-vertex maximum degree at most20 and exact diameter3 in the project actual-Walk definition. Two final theorems have no extra premises and use only the three standard listed axioms. The proof-checker PASS audit owns the verified claim; a model opinion or literature statement does not replace kernel evidence.

The graph is still the same already independently validated3750/37500 literal graph. Text-file parsing equality inside Lean, exact20regularity inside Lean and a separate mathlib.ediam theorem are not claimed. Goal permits a deterministic generator with literal parameters, so those extra deliverables are not imposed as a new gate for this complete formula-graph witness. Current-global record novelty and public adoption remain unconfirmed.

The existing186033 source row gained one bounded tower-prefix/K6 variant. Four fixed layers passed internal-degree, connected-bipartite and63030 opposite-color anchor checks. H7 color0 has0 currentfree vertices, so the fixed six-half-class K6 rule fails its resource gate. Three other half classes were not counted. CPU1.214964867 belongs to the saved successful producer; this writer did not repeat it. No new balls, solver or graph were made.

Three existing experiment/source rows were upserted, with zero new ledger records or graph experiments. One new verified claim was born from the existing PROOF_AUDIT.json. Ledger368, validated constructions104/4, confirmed public-table improvements103/3, novelty-pending1 and complete deterministic-formula Lean graph instances1 are separate counts. Historical confirmed103 graph Lean count stays0.
'''
(HERE / 'F5_FINAL_LEAN_WIKI_REPORT.md').write_text(screened(report))
with (HERE / 'F5_FINAL_LEAN_WIKI.sync.log').open('a') as log, contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI), 'Final F5 kernel witness persisted: one proof-checker-born verified fixed Fin3750 claim, existing graph/source rows updated; complete formula Lean1; ledger368 and validated104/4 versus confirmed103/3 retained. One bounded11D6 prefix/K6 capacity variant; no computation reruns.')
    helper.rebuild_index(str(WIKI))
    helper.rebuild_query_pack(str(WIKI))

# Incremental schema/links/relationships/count lint; no historical proof audit.
errors = []
nodes = {}
for directory in ['papers', 'ideas', 'experiments', 'claims']:
    for p in (WIKI / directory).glob('*.md'):
        match = re.search(r'(?m)^node_id:\s*(.+)$', p.read_text())
        if match:
            node_id = match.group(1).strip().strip('"')
            if node_id in nodes:
                errors.append('duplicate node_id '+node_id)
            nodes[node_id] = p
touched = ['exp:'+r['id'] for r in rows] + [CLAIM_ID, 'idea:ddp-q3-three-step-plane-pencil31', 'idea:ddp-math-challenges-and-records']
for node_id in touched:
    p = nodes[node_id]
    text = p.read_text()
    meta = helper._load_paper_frontmatter(p)
    required = ['type','node_id','name','status','provenance'] if node_id.startswith('claim:') else ['type','node_id','title']
    for field in required:
        if not re.search(rf'(?m)^{field}:', text):
            errors.append(f'missing {field}: {node_id}')
    if node_id == CLAIM_ID:
        assert meta['status'] == 'verified'
        assert meta['provenance'] == rel(FULL/'PROOF_AUDIT.json')
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if '://' not in target and not target.startswith('#'):
            if not (p.parent / target.split('#')[0]).exists():
                errors.append(f'missing local link {node_id}: {target}')
edges = [json.loads(line) for line in (WIKI/'graph/edges.jsonl').read_text().splitlines() if line.strip()]
claim_edges = [e for e in edges if e['from']==CLAIM_ID or e['to']==CLAIM_ID]
assert any(e['from']=='exp:'+FULL_ID and e['to']==CLAIM_ID and e['type']=='supports' for e in claim_edges)
for e in claim_edges:
    for target in [e['from'], e['to']]:
        if not target.startswith('gap:') and target not in nodes:
            errors.append('dangling '+target)
after = json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count']==368 and len(after['rows'])==368
assert after['validated_graph_examples_including_novelty_pending']==104
assert after['validated_parameter_pairs_including_novelty_pending']==4
assert after['confirmed_publictable_graph_examples']==103
assert after['confirmed_publictable_improved_parameter_pairs']==3
assert after['novelty_pending_valid_graph_examples']==1
assert after['complete_Lean_graph_instances']==1
assert after['confirmed_publictable_complete_Lean_graph_instances']==0
assert len((WIKI/'query_pack.md').read_text())<=8000
assert not errors, errors
receipt = dict(status='PASS_FINAL_KERNEL_CLAIM_AND_LAYER_INCREMENTAL_LINT',
    applied_UTC=datetime.now(timezone.utc).isoformat(),
    record_count=368, existing_rows_updated=[r['id'] for r in rows], new_records=0,
    verified_claim_id=CLAIM_ID, claim_provenance=rel(FULL/'PROOF_AUDIT.json'),
    complete_deterministic_formula_Lean_graph_instances=1,
    confirmed_publictable_Lean_graph_instances=0,
    validated_graph_examples=104, validated_parameter_pairs=4,
    confirmed_publictable_examples=103, confirmed_publictable_cells=3,
    novelty_pending_examples=1,
    literal_edge_text_equality_Lean=False, exact20regular_Lean=False,
    new_BFS=0, new_compilers=0, new_solver_calls=0, new_hashes=0,
    query_pack_chars=len((WIKI/'query_pack.md').read_text()),
    ledger_command=' '.join(command),
    claim_helper='aris_repo/tools/research_wiki.py:add_claim(status=verified, provenance=PROOF_AUDIT.json)',
    lint_scope='Touched schemas/local links, canonical claim edges, unique node IDs, unchanged ledger count, separated math/novelty/formal counters; no old proof or graph audit.',
    lint_errors=errors)
(HERE/'F5_FINAL_LEAN_WIKI_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False))

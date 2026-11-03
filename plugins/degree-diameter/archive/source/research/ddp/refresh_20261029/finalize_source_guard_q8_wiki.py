"""Persist the completed source/guard/q8 batch via the existing Wiki helper.

No graph, radius computation, path enumeration, solver, compiler, web request
or hash is run here. The root separately refreshes global status and brief.
"""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import copy
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
    findings=capture_filter.screen(text)
    assert not findings,findings
    return text

before=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert before['record_count']==368
before_ids={r['id'] for r in before['rows']}
claims_before={p.name for p in (WIKI/'claims').glob('*.md')}
rows=json.loads((HERE/'SOURCE_GUARD_Q8_PENDING_WIKI_ROWS.json').read_text())
source9=next(r for r in rows if 'current77418' in r['id'])
guard=next(r for r in rows if 'v4580-current51457' in r['id'])
old_success=next(r for r in rows if r['id']=='ddp-d13-singlefault-star-family-51457-20261027')
q8=next(r for r in rows if r['id']=='ddp-q8-k64-cube-external2factor-13d3-20261029')
factor=HERE/'q8_K64_external_factor_sat'
factor_result=json.loads((factor/'RESULT.json').read_text())
factor_terminal=json.loads((factor/'TERMINAL.json').read_text())
assert factor_result['status']==factor_terminal['status']=='UNKNOWN'
assert factor_result['solver_calls']==1 and factor_result['solver_exit_code']==0
assert factor_result['auxiliary_positive_graphs']==factor_result['main1088_graphs']==0
q8['title']='q8 conditional1088: affine3840 fail, external2factor UNKNOWN, published-source deletion blocked'
q8['status']='COMPLETE_FINITE_GATES_AND_EXTERNAL_FACTOR_UNKNOWN'
q8['outcome_class']='auxiliary-family-gates-closed-general-cross-pencil-model-UNKNOWN'
q8['failure_or_result']='固定J5+I1/two-coset affine类3840项实际64点5regular辅助候选均首root0R3失败，CPU.42158127，0未试。全跨pencil2factor模型唯一90秒SAT返回UNKNOWN/code0，aggregate90.975846255CPU，无候选、0辅助正例/1088主图。另从published K64/6regular恢复96cube+96extra，5934条≤3简单路径证94/96extra为D3critical，60个vertex三条extra全critical；vertex0即排固定source保cube纯extra删边到max5/D3，未运行删边SAT。'
q8['unclosed_gap']='全跨pencil2factor仍UNKNOWN，不排该域；published源纯删边与固定affine3840类已各按本scope停止。一般K64允许pencil内新增边的更宽域、其它辅助图和一般(13,3)开放，未产生1088图。'
q8['lesson_and_restart_condition']='本批全部终态，不续原90秒SAT或固定affine类，不从2条非critical extra推出可降到5度。当前缺口是共同短路与2factor约束的可实现性，source全regular或局部rank都不保证它；任何后续须有具体新规则和独立预算。'
fv=next(v for v in q8['variants'] if v['label']=='all_cross_pencil_external_2factor')
fv.update(status='UNKNOWN',solver_running=False,solver_calls=1,
    solver_exit_code=0,solver_wall_limit_seconds=90,
    aggregate_CPU_seconds=factor_result['aggregate_CPU_seconds'],
    terminal_result=factor_result,scope_closed=False,
    positive_auxiliary_graphs=0,main1088_graphs=0)
fv.pop('observed_saved_result',None)
q8['other_metrics'].update(external_factor_solver_calls=1,
    external_factor_status='UNKNOWN',external_factor_solver_exit_code=0,
    external_factor_all_variables=197152,external_factor_clauses=684450,
    external_factor_CPU_seconds=factor_result['aggregate_CPU_seconds'],
    all_numerical_jobs_terminal=True)

published=HERE/'q8_published_gadget_matching_gate'
source_fields=json.loads((published/'RAW_SOURCE_FIELDS.json').read_text())
credit=json.loads((published/'SOURCE_CREDIT.json').read_text())
pr=json.loads((published/'RESULT.json').read_text())
mr=json.loads((published/'MATCHING_RESULT.json').read_text())
assert mr['D3_critical_extra_edges']==94 and mr['removable_domain_extra_edges']==96
blocked=mr['vertices_with_all_three_extra_edges_critical']
assert len(blocked)==60 and 0 in blocked
assert mr['solver_calls']==0 and mr['source_all_pairs_have_path_at_most3']
pubpaths=source_fields['report_paths']+[
    rel(published/n) for n in ['MATCHING_PREDICTION.md','MATCHING_RESULT.json',
        'MATCHING_TERMINAL.json','CRITICAL_EXTRA_EDGES.json','analyze_matching.py',
        'K64_192.edges','extra96.edges']]
assert all((ROOT/p).exists() for p in pubpaths)
published_variant=dict(label='published_Rajiv_K64_extra_edge_deletion_gate_20261029',
    status=mr['status'],source_credit=credit,
    source_reconstruction=dict(n=64,m=192,degree=6,cube_edges=96,extra_edges=96,
        extra_degree=3,extra_cross_pencil=True,source_D3_initially_inherited=True,
        original_main1088_adjacency_downloaded=False,
        CPU_seconds=pr['cpu_seconds']),
    source_short_simple_path_enumeration=dict(
        total_unordered_endpoint_simple_paths_length_at_most3=5934,
        all_source_pairs_actually_reachable_within3=True,
        D3_critical_extra_edges=94,
        vertices_with_all_three_extra_critical=blocked,
        blocked_vertex_count=len(blocked),decisive_vertex=0),
    closed_scope='On this exact published64/192/6regular source, keep all96cube edges and only delete extra edges while retaining all64 vertices: no resulting maximumdegree<=5 graph hasD<=3. This includes all extra-perfectmatching deletions.',
    proof_reason='Vertex0 must lose at least1 of its3extra edges to reduce degree6 to<=5, but each is on every<=3path of a saved endpoint pair; further deletions cannot create paths.',
    not_excluded=['arbitrary cross-pencil2factors','rewiring/added edges','other K64 auxiliary graphs','general q8 fibre extensions'],
    actual_deleted_candidate_graphs=0,solver_calls=0,
    source_main1088_BFS=0,new_main1088_graphs=0,
    matching_gate_CPU_seconds=mr['worker_CPU_seconds'],
    auxiliary_positive_graphs=0,new_Lean_instances=0,evidence_paths=pubpaths)
q8['variants']=[v for v in q8['variants'] if v.get('label')!=published_variant['label']]+[published_variant]
q8['report_paths']=list(dict.fromkeys(q8['report_paths']+pubpaths))
q8['other_metrics'].update(published_auxiliary_source_n=64,published_auxiliary_source_m=192,
    published_auxiliary_source_degree=6,published_extra_edges=96,
    published_extra_critical_edges=94,published_all_extra_critical_vertex_count=len(blocked),
    published_source_simple_short_paths=5934,
    published_source_restore_CPU_seconds=pr['cpu_seconds'],
    published_source_deletion_gate_CPU_seconds=mr['worker_CPU_seconds'],
    published_source_deletion_SAT_calls=0,
    total_recorded_q8_worker_CPU_seconds=(0.42158127+factor_result['aggregate_CPU_seconds']+
        pr['cpu_seconds']+mr['worker_CPU_seconds']),
    recorded_CPU_scope='Sum of saved affine worker, external-factor batch, published-source restoration and deletion gate; primary retrieval wall time separate.')

summary='''# Source eligibility, exact guard cover and q8 auxiliary graph: final batch

The current77418 source is actually77418/348381/simple/all9regular. The9-degree retained-edge connected-append entrance is closed by0spare slots; officialD6 is inherited, with0distanceBFS/balls/solver/candidate. Two primary pages/files were read; profilingCPU.641021884. Its H8 subdivision/clique construction is not the186033 tower.

The accepted40 D13 neighbor sets use original51417 labels. Of51 earlier failed mandatory sets,38 remain entirelyfree on51457 and13areblocked, so mandatory-port consumption cannot explain all38 failures. Existing dynamic coverage certificates do not produce an original-base static joint-packing pool. Five disjoint closedB1 support groups prove only that one strong local proxy needs at least5guards; they do not exclude longR4 coverage by4guards.

Actual prototype4580/current51457 has9mandatory pins and remaining4guard capacity. Its complete2755target/13057column SAT ran once60seconds and returnedUNKNOWN; aggregate68.829465935CPU. Its one full fractional LP20second run also returnedUNKNOWN with no exact certificate;22.439896875CPU. Combined91.269362810CPU, no new graph or source-allrootBFS, no renewal. This is distinct from oldprototype51445/750targets/13026columns MIPUNKNOWN.

For q8, Rajiv PDFpp3-4 Theorem1 gives a conditional1088-point degree13/D3 graph if K64 contains the eight designatedQ3s and hasmaximumdegree5/D3. The author already gave1088/14 and explicitly had not found the requireddegree2extra gadget. FixedJ5+I1/two-coset triples3840were completely evaluated: every actual64-vertex5regular auxiliary candidate fails its firstrootR3. That finiteclass is closed, not allK64s.

The completecross-pencil external2factor model is a separate domain, not merely that affine class:1792edge selectors,197152allvariables/684450clauses, trueR2/R3 and soundnormalization. One90secondcall returnedUNKNOWN, code0, aggregate90.975846255CPU, no witness; that domain remainsopen and is not renewed.

One exact publishedK64 source was reconstructed from the small Rajivwitness:64/192/6regular,96cube plus96extra edges, not an1088graph revalidation. Enumerating5934unordered-endpoint simplepaths oflength<=3 verifies allsourcepairs and finds94extraedges D3critical. The actual saved list has60vertices with all3extraedges critical; vertex0 alone forbids keeping allcubeedges and purely deletingextras to maximumdegree5/D3. The gate stopped beforeSAT;CPU.025104680, no auxiliarypositive/main1088. This does not exclude arbitrary2factors, rewiring or generalq8extensions.

All jobs areterminal. Main targetgraphs thisturn0, newLean0. Validated104examples/4parameters,confirmed103/3,completeformulaLean1 and current-global noveltypending1 remainunchanged. Three new source/problemrecords plus one oldfamilyvariant are not three new independentmethods. No newverifiedclaim is created. This persistence script performs no numerical calculation, BFS, solver, compiler, retrieval or hash.
'''
(HERE/'SOURCE_GUARD_Q8_FINAL_WIKI_REPORT.md').write_text(screened(summary))
report_path=rel(HERE/'SOURCE_GUARD_Q8_FINAL_WIKI_REPORT.md')
for row in rows:
    row['report_paths']=list(dict.fromkeys(row.get('report_paths',[])+[report_path]))
    screened(json.dumps(row,ensure_ascii=False))
    assert all((ROOT/p).exists() for p in row['report_paths']),row['id']
new_ids=[r['id'] for r in rows if r['id'] not in before_ids]
assert len(new_ids)==3
raw_path=HERE/'SOURCE_GUARD_Q8_FINAL_WIKI_ROWS.json'
raw_path.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
command=[sys.executable,'research/ddp/more_graphs_20261027/sync_additional_probes.py',rel(raw_path)]
result=subprocess.run(command,cwd=ROOT,text=True,capture_output=True,check=True)
sync=json.loads(result.stdout)
assert sync['record_count']==371

comments=WIKI/'DD82_PROGRESS_AND_COMMENTS_20261018.md'
marker='<!-- SOURCE_GUARD_Q8_TERMINAL_20261029 -->'
if marker not in comments.read_text():
    note='\n\n'+marker+'\n## 2026-10-29 source／guard／q8辅助机制终态\n\n这是研究执行记录，不是新用户原话。77418实际全9正则/free0，保边connected append无入口；D13当前38个失败mandatory仍全free，不能以贪心锁端口解释其失败。v4580完整4guard SAT和fractional LP均UNKNOWN，无证书；强B1五支持组只排强proxy。q8固定affine3840类全拒，但全cross-pencil2factor一次90秒UNKNOWN仍开放。恢复的published K64有94/96extra critical及60个三extra全critical顶点，因此保cube纯删extra到max5/D3不可能；0删边SAT，不冒一般q8无解。\n\n本turn目标新图0、新Lean0；原104／4、confirmed103／3、Lean1、novelty-pending及ACTIVE不变。账本由368增至371条来源／实验／变体记录，不是增加3种独立方法。[最终合并报告](../'+report_path+')；当前所有数值终态，不续timer／已闭affine类。\n'
    comments.write_text(comments.read_text().rstrip()+screened(note))

with (HERE/'SOURCE_GUARD_Q8_FINAL_WIKI.sync.log').open('a') as log,contextlib.redirect_stdout(log):
    helper.append_log(str(WIKI),'Source/guard/q8 terminal batch: add3 source/problem records, updateoldD13capacityvariant. Ledger368->371;mainnewgraphs0;validated104/4,confirmed103/3,formulaLean1 unchanged. Fourguard SAT/LP and generalcross-pencil2factor UNKNOWN remainopen; only statedsource/deletion/affine gates closed. Rootglobalfiles untouched.')

after=json.loads((WIKI/'DDP_METHOD_LEDGER.json').read_text())
assert after['record_count']==len(after['rows'])==371
assert after['validated_graph_examples_including_novelty_pending']==104
assert after['validated_parameter_pairs_including_novelty_pending']==4
assert after['confirmed_publictable_graph_examples']==103
assert after['confirmed_publictable_improved_parameter_pairs']==3
assert after['complete_Lean_graph_instances']==1 and after['novelty_pending_valid_graph_examples']==1
assert {p.name for p in (WIKI/'claims').glob('*.md')}==claims_before
errors=[]
nodes={}
for directory in ['papers','ideas','experiments','claims']:
    for p in (WIKI/directory).glob('*.md'):
        m=re.search(r'(?m)^node_id:\s*(.+)$',p.read_text())
        if m:
            nid=m.group(1).strip().strip('"')
            if nid in nodes:errors.append('duplicate node '+nid)
            nodes[nid]=p
for row in rows:
    nid='exp:'+row['id'];p=nodes[nid];text=p.read_text()
    for field in ['type','node_id','title','verdict','idea_id','provenance']:
        if not re.search(rf'(?m)^{field}:',text):errors.append(f'{nid} missing{field}')
    for target in re.findall(r'\]\(([^)]+)\)',text):
        if '://' not in target and not target.startswith('#') and not (p.parent/target.split('#')[0]).exists():
            errors.append(f'{nid} missinglink{target}')
edges=[json.loads(s) for s in (WIKI/'graph/edges.jsonl').read_text().splitlines() if s.strip()]
for rid in new_ids:
    assert any(e['to']=='exp:'+rid and e['type']=='tested_by' for e in edges),rid
assert not errors,errors
receipt=dict(status='PASS_SOURCE_GUARD_Q8_FINAL_INCREMENTAL_LINT',
    applied_UTC=datetime.now(timezone.utc).isoformat(),
    record_count_before=368,record_count=371,new_ledger_records=3,
    new_ids=['exp:'+rid for rid in new_ids],
    updated_existing_id='exp:'+old_success['id'],new_verified_claims=0,
    mathematical_valid_examples=104,mathematical_valid_parameter_pairs=4,
    confirmed_publictable_examples=103,confirmed_publictable_parameter_pairs=3,
    complete_Lean_graph_instances=1,new_Lean_instances=0,current_global_novelty='pending',
    goal_status='ACTIVE',new_main_target_graphs=0,
    v4580_SAT_status='UNKNOWN',v4580_LP_status='UNKNOWN_NO_CERTIFICATE',
    v4580_SAT_plus_LP_CPU_seconds=91.26936281,
    q8_external_factor_status='UNKNOWN',q8_affine_complete_cases=3840,
    q8_published_extra_critical_edges=94,q8_published_blocked_vertex_count=len(blocked),
    q8_published_extra_deletion_to_max5_D3='EXCLUDED_FIXED_PUBLISHED_SOURCE_ONLY',
    q8_factor_CPU_seconds=factor_result['aggregate_CPU_seconds'],
    root_owned_files_edited=False,new_numerics_by_writer=0,
    final_query_refresh='Await root brief refresh; normal node helper generated its ordinary query during upserts.',
    command=' '.join(command),lint_scope='Touched schemas/links, unique node IDs, newtested_by edges, unchanged claimnode set and separated math/formal/novelty counts',lint_errors=errors)
(HERE/'SOURCE_GUARD_Q8_FINAL_WIKI_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False))

"""One A3645 terminal node from accepted receipts; no source/graph computations."""
from pathlib import Path
import copy
import json
import runpy
import time

ROOT = Path(__file__).resolve().parents[4]
S = Path(__file__).resolve().parent
W = ROOT / 'research-wiki'
D = ROOT / 'research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646'
PREFIX = 'SOURCE3645_SINGLECUT_MAXSTAR_AND_NONBASEBASE_BOUND_20261102'
SLUG = 'ddp-d4-actual3645-singlecut-maxstar3646-complete-no-and-two-nonbasebase-bound-20261102'
MARKER = '<!-- ' + PREFIX + ' -->'
started = time.process_time()
H = runpy.run_path(str(S / 'sync_source650_then_d4_binary_terminals_20261102.py'))
load, relative = H['load'], H['relative']
now = H['stamp']()
root = load(D / 'ROOT_DISPOSITION.json')
result = load(D / 'RESULT.json')
post = load(D / 'CACHED_EDGE_CLASS_CAPACITY_POSTPROCESS.json')
n = result['native']
assert root['status'] == 'ROOT_ACCEPTED_COMPLETE_SINGLECUT_MAXSTAR_NO_WITH_CACHED_TWO_NONBASEBASE_BOUND_STOP'
assert root['all_numeric_terminal'] and root['final_case_CPU'] == 2.943111119 and root['case_cap'] == 15
assert n['complete_domain'] and n['domain_edges'] == n['source_m'] == 20044
assert n['cached_R3_roots_reused'] == 1993 and n['new_R3_queries'] == 1652
assert n['newroot_pass'] == n['candidate_oldroot_BFS'] == n['source_singlepair_diagnostic_queries'] == 0
assert n['best_missing_holes'] == 305 and n['best_cut'] == [108, 1643]
assert post['holes_to_cover'] == 743 and post['two_non_basebase_upper'] == 712
assert [post['classes'][c]['maximum_holes_covered'] for c in ['base_base', 'base_inserted', 'inserted_inserted']] == [438, 356, 338]
assert result['failed_input_preparation_CPU_charge'] == 0.1
assert post['conservative_postprocess_CPU_charge'] == 0.05
ledger_path = W / 'DDP_METHOD_LEDGER.json'
ledger = load(ledger_path)
assert ledger['record_count'] == len(ledger['rows']) == 459
assert not any(row['id'] == SLUG or '/one_cut_all_free_star3646/' in json.dumps(row, ensure_ascii=False) for row in ledger['rows'])
assert not (S / (PREFIX + '_RECEIPT.json')).exists()
before = copy.deepcopy(ledger)
old, human, index_before = H['page_snapshot'](MARKER)
md_before = (W / 'DDP_METHOD_LEDGER.md').read_text()
assert MARKER not in md_before
names = ['PRED.md', 'run_once.py', 'run.cpp', 'CACHE_BINDING.json', 'PREPARATION_ATTEMPT1.json',
         'RESULT.json', 'TERMINAL.json', 'ALL_EDGES.tsv', 'ALL_SOURCE_R3_SUPPORTS.bin',
         'CACHED_EDGE_CLASS_CAPACITY_POSTPROCESS.json', 'ONE_CUT_TERMINAL_SCOPE_REVIEW.md',
         'ROOT_DISPOSITION.json', 'NOTE.md']
evidence = [D / name for name in names]
interface = ROOT / root['paper_interface']
evidence.append(interface)
assert all(path.exists() for path in evidence)
raw = {
    'id': SLUG,
    'title': 'A3645单cut最大star完整20044 NO；缓存界排两cut均非base-base子域，仅paper推论',
    'family': 'Edge absorption with all available pins and one new star',
    'idea_family': 'idea:ddp-open-parameter-construction-20261026',
    'date': '2026-11-02', 'wiki_verdict': 'no',
    'record_type': 'complete_singlecut_maxstar_exclusion_and_cached_two_cut_bound',
    'target_Delta': 11, 'target_D': 4, 'savedL': 3645,
    'baseline_date': 'Inherited actual3645/max11/D4 and preserved-edge closed scopes; no new public query/sourceD4validation in this publication',
    'n': {'actual': None, 'hypothetical': 3646},
    'actual_graph_Delta': None, 'actual_D': None,
    'ordinary_bad_unordered_pairs': None, 'ordinary_bad_target_D': 4, 'new_lower_bound': False,
    'actual_D_scope': 'Complete20044single-sourceedge maximal-star newrootgate failsall. No candidateoldoldstage,source singlepairdiagnostic or targetgraphBFSentered. Cached edge-class coverage maxima yield only a paper two-nonbasebase-cut capacity bound,no two-cut enumeration or positivegraph.',
    'outcome_class': root['status'],
    'scope': 'Fixedactual3645/20044 max11/D4 with7degree10freevertices. DeleteexactlyoneORIGINALedgeuv,keepallotheroldedges,andaddonezwithonlynewoldspokes. MaximallegalpoolP=all7free union{u,v},size<=9,dominatesalllegalsubstars. All20044maximalstars failnewrootR4,soevery singlecut/onlystar/nootheroldoldedit variantNO. Separatepapercorollary: anytwo distinctcuts,possiblysharingends,bothnon-basebase(relative to first3444labels),P<=11,onlynewstar/nootheroldedits alsoNO by356+356<743. No claim two-cutdomainenumerated or feasiblewhenonebasebasecutpresent. Notgeneral3646/(11,4),otherhosts,repair/multihelper orbroaderedits.',
    'distance_text': '实际source只有7个10度free。单cut全端点和7free作最大star合法且支配所有子star，d_(G−cuts)(P,t)=dG(P,t)使sourceR3覆盖为新根精确门。完整20044条旧edge全newrootfail，BB18485/BI914/II645均0pass；最优(108,1643)仍缺305，故oldold未进入而非已安全或受损。复用1993R3/新增1652深3，不重原7free球或sourceD4。缓存743holes的单edge端点max覆盖BB438/BI356/II338，所以两cut若均非BB即使共享端点且P<=11也最多712<743、至少漏31；仅paper推论，没有枚两cut或宣称含BB会过。含准备KeyError保守.1及postprocess.05后final2.943111119/15，0新图/solver/Lean/ARIS。',
    'lesson_and_restart_condition': 'Changingfrompurepreservedappendtooneabsorbededge didnotprovide enoughnewrootcoverage: maximalstar dominanceclosesallitslegalspokesubsets,notjustasample. Classmaximafromsavedrowsgiveaconcretetwo-cutnecessaryrestrictionwithoutanothersearch: at leastonebasebasecutwouldberequired. Stoptheexactsinglecutlinewithoutautomaticsecondcut/repair/seed; broaderquestionsneednewexplicitrules. PreserveoldpurepreservedNOand2673/679 scopeswithoutreinterpretation.',
    'restart_condition': 'STOP completefixedsource/singleORIGINALcut/onlynewoldstar/nootheredits. No automaticsecondcut/repair/seed; cachednonbasebasepaperboundmustbe inheritedifafutureseparatelyauthorizedtwo-cutquestionisraised. No positivefreshsuite.',
    'unclosed_gap': 'General(11,4)/3646,otheractualsources,oldoldrepair,otherhelpersandbroadereditsremainunexcluded. Two-cutcaseswithatleastonebasebaseedge remainunclassifiedbythisbound. OldpurepreservedNO,old2673/679 andotherhistoricalrecordsremainunchanged;new743holesmustnotbeconflatedwiththem. No graph/parameter/Lean/method/recordclaim. Bworkandnatural364helper14readgatesarenotpartofthisnode.',
    'positive_guarantees': [
        'Sourceformat/degree/freevertices/sourceD4facts areinherited. Only1993oldR3supports reusedand1652missingrootscomputedforthisnewquestion; old7free-R3unionandD4validationnotrepeated.',
        'For eachcut everylegalnewneighborliesinthe7free/cutends pool; maximalpoolhasatmost9<=11spokes andallsubstarsaresubgraphs. A negative maximalstar thereforeexcludesallitslegalsubsets.',
        'AllcutendsinP implydistance-to-Punchangedbycutdeletion,soall20044maxstarnewrootfailuresareexact,beforeoldoldchecks.',
        'Actualedgeclassesuselabelthreshold3444:18485basebase,914baseinserted,645insertedinserted. No unprovedtransitivityorotherlabelsemanticsassumed.',
        'Cachedcoveragecounts438/356/338supportthepaperunionbound712<743fortwononbasebaseedges,evenwithsharedends. Itisnot two-cutenumeration,notafeasibilityclaimwithbasebasepresent.',
        'PreparationfieldKeyError occurredbeforecompilation/numerics anditsconservative.1costispreserved;postprocess.05alsoincluded. Allprocessesterminal,notimerreset.',
        'NoactualnewrootpassmeansoldoldstageNOT_ENTERED,notoldoldproven;noacceptedtargetgraph,solver,Lean,ARISorpositiveverifier.'
    ],
    'other_metrics': {
        'new_graphs': 0, 'new_parameter_pairs': 0, 'new_Lean_instances': 0, 'new_independent_method_claims': 0,
        'single_research_record': True, 'source_n': 3645, 'source_m': 20044,
        'source_maxdegree': 11, 'source_free_vertices': 7, 'free_degree': 10,
        'singlecut_domain': 20044, 'singlecut_complete': True, 'maximalstar_size_atmost': 9,
        'newroot_pass': 0, 'candidate_oldroot_BFS': 0, 'source_singlepairdiagnostic': 0,
        'best_missing_holes': 305, 'best_cut': [108, 1643],
        'source_R3_reused': 1993, 'new_source_depth3_supports': 1652,
        'old_free_R3_recomputed': False, 'source_D4_revalidation': False,
        'edgeclasses': n['classes'],
        'cached_class_capacity_paper': post,
        'two_cut_paper_only_no_new_enum': True, 'two_cut_sharedends_allowed': True,
        'two_cut_maximalstar_size_atmost': 11, 'holes': 743,
        'old2673_679_and_purepreserved_scopes_unchanged': True,
        'preparation_failure_charge': 0.1, 'preparation_failure_type': 'KeyError',
        'cached_postprocess_charge': 0.05, 'numeric_case_CPU_before_post': result['case_CPU'],
        'samecase_CPU': 2.943111119, 'case_cap': 15, 'all_processes_terminal': True,
        'new_solver_Lean_ARIS_accepted_target_graph': 0,
        'B_or_natural364helper14_included': False, 'same_Goal': 'ACTIVE', 'old_N8_n61': 'PAUSED'
    },
    'evidence_paths': [relative(path) for path in evidence]
}
row, rowfile = H['write_node'](raw, PREFIX)
ledger['rows'].append(row)
ledger['record_count'] = 460
H['persist'](ledger, rowfile, now)
node = 'experiments/' + SLUG + '.md'
summary = f'''\n\n{MARKER}
### {now} A3645完整单cut最大star NO；两非BB cut缓存界仅paper

固定3645/20044/max11/D4及7个10度free。删任一原edge，newz连all7free与cutends的最大合法star支配其全部子star。20044条原edge完整全newrootfail，最优仍缺305；0oldold阶段，不误称旧旧已安全或受损。复用1993R3＋新增1652深3支持，原7free球/sourceD4未重验，准备字段KeyError保守.1保留。

保存rows对743holes的端点覆盖max为BB438/BI356/II338。两cuts都非前3444点内部BB时，合并≤712<743，允许共享端点、最大starP≤11，也至少漏31；这是paper推论，未枚两cut，更不保证含BB会成功。旧purepreservedNO与2673/679范围不改，不混B或natural364helper14。

finalcase2.943111119/15含postprocess.05，0新图/solver/Lean/ARIS，当前STOP无第二cut/repair/seed。459→460仅一研究节点，0图/参数/Lean/方法增量，153/43/47及旧459rows/人工顶块保持。[canonical节点]({node})；[root终态](../{relative(D / 'ROOT_DISPOSITION.json')})；[scope paper](../{relative(D / 'ONE_CUT_TERMINAL_SCOPE_REVIEW.md')})。

'''
H['update_pages'](old, human, summary, 1)
(W / 'DDP_METHOD_LEDGER.md').write_text(md_before + summary.replace('### ', '## ', 1))
after = load(ledger_path)
assert after['record_count'] == len(after['rows']) == 460
assert after['rows'][:-1] == before['rows']
H['unchanged_top'](before, after)
receipt = {
    'status': 'PASS_ONE_SOURCE3645_SINGLECUT_MAXSTAR_AND_NONBASEBASE_PAPER_BOUND_NODE',
    'updated_UTC': now, 'records_before': 459, 'records_after': 460, 'records_added': 1,
    'new_experiment_id': SLUG, 'canonical_node': 'research-wiki/' + node, 'row_path': relative(rowfile),
    'singlecut_domain_complete': 20044, 'newroot_pass': 0, 'oldold_stage': 'NOT_ENTERED',
    'cached_R3_reused': 1993, 'new_R3': 1652, 'source_D4_validation': 0,
    'classmax_BB_BI_II': [438, 356, 338], 'holes': 743, 'two_nonBB_upper': 712,
    'two_cut_bound_is_paper_not_enumeration': True, 'sharedends_allowed_P_atmost11': True,
    'two_cut_with_BB_not_claimed_feasible_or_closed': True,
    'old_purepreserved_2673_679_scopes_untouched': True,
    'samecase_CPU': 2.943111119, 'case_cap': 15,
    'preparation_KeyError_charge_preserved': 0.1, 'postprocess_charge_preserved': 0.05,
    'other459rows_preserved_exact': True, 'row_order_preserved': True,
    'human_top_blocks_preserved_exact': {name: True for name in H['FILES']},
    'index_experiments_before': index_before, 'index_experiments_after': index_before + 1,
    'graph_parameter_Lean_method_increments': [0, 0, 0, 0],
    'graph_parameter_Lean_snapshot_preserved': [153, 43, 47],
    'full_rebuild_reimport': False, 'root_STATE_ROUND_HTML_recovery_modified': False,
    'new_math_solver_BFS_field_Lean_ARIS': 0, 'B_or_natural364helper14_included': False,
    'modified_outputs': ['research-wiki/' + node, 'research-wiki/DDP_METHOD_LEDGER.json', 'research-wiki/DDP_METHOD_LEDGER.md'] + ['research-wiki/' + name for name in H['FILES']] + [relative(rowfile)],
    'sync_process_CPU_seconds': time.process_time() - started,
    'stop': True
}
receipt_path = S / (PREFIX + '_RECEIPT.json')
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'receipt': relative(receipt_path), 'before': 459, 'after': 460, 'add': 1, 'CPU': receipt['sync_process_CPU_seconds']}, ensure_ascii=False), flush=True)

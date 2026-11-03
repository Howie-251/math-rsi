"""Publish one accepted fixed-base/four-global-coefficient D5 terminal node."""
from pathlib import Path
import copy
import json
import runpy
import time

ROOT = Path(__file__).resolve().parents[4]
S = Path(__file__).resolve().parent
W = ROOT / 'research-wiki'
D = ROOT / 'research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D5/binary_C30_base240_C23_cover'
PREFIX = 'D5_BASE240_C23_FOUR_COEFFICIENT_TERMINAL_20261102'
SLUG = 'ddp-d5-fixed-binary240-four-global-coefficient-c23-cover5520-complete-no-20261102'
MARKER = '<!-- ' + PREFIX + ' -->'
started = time.process_time()
H = runpy.run_path(str(S / 'sync_source650_then_d4_binary_terminals_20261102.py'))
load, relative = H['load'], H['relative']
now = H['stamp']()
root = load(D / 'ROOT_DISPOSITION.json')
base = load(D / 'BASE_RESULT.json')
packet = load(D / 'CRITICAL_PACKET_RESULT.json')
assert root['root_status'] == 'ROOT_ACCEPTED_FIXED_FOUR_COEFFICIENT_C23_NO_STOP'
assert root['samecase_CPU'] == 1.496812969 and root['samecase_cap'] == 5
assert base['native']['source_n'] == 240 and base['native']['source_m'] == 960
assert base['native']['source_degree'] == 8 and base['native']['base_diameter'] == 4
assert base['native']['minimum_NB_walks0to5'] == 66 and base['native']['ordered_pairs_below23'] == 0
assert packet['pair'] == [8, 70] and packet['NB_paths'] == 66 and packet['distinct_forms'] == 26
assert packet['parameter_representatives_tested'] == 12720 and packet['parameter_survivors'] == 0
assert packet['maximum_phase_coverage'] == 22 and not packet['all_pairs_tested']
assert not packet['target5520_graph_generated']
review = D / 'CRITICAL_PACKET_SCOPE_REVIEW.md'
assert review.exists(), 'Wait for the already-assigned paper review; no numerical rerun.'
ledger_path = W / 'DDP_METHOD_LEDGER.json'
ledger = load(ledger_path)
assert ledger['record_count'] == len(ledger['rows']) == 458
assert not any(row['id'] == SLUG or '/binary_C30_base240_C23_cover/' in json.dumps(row, ensure_ascii=False) for row in ledger['rows'])
assert not (S / (PREFIX + '_RECEIPT.json')).exists()
before = copy.deepcopy(ledger)
old, human, index_before = H['page_snapshot'](MARKER)
md_before = (W / 'DDP_METHOD_LEDGER.md').read_text()
assert MARKER not in md_before
names = ['PAPER_INTERFACE.md', 'PRED_BASE_NB_GATE.md', 'run_base_once.py', 'base_nb.cpp',
         'BASE_RESULT.json', 'BASE_TERMINAL.json', 'BASE_ROOT_NB_STATS.tsv',
         'PRED_ONE_CRITICAL_PACKET.md', 'run_critical_packet_once.py',
         'CRITICAL_PACKET_PATHS.json', 'CRITICAL_PACKET_FORMS.json', 'CRITICAL_PACKET_PHASE_COUNTS.tsv',
         'CRITICAL_PACKET_RESULT.json', 'CRITICAL_PACKET_TERMINAL.json', 'CRITICAL_PACKET_SURVIVORS.json',
         'CRITICAL_PACKET_SCOPE_REVIEW.md', 'ROOT_DISPOSITION.json', 'NOTE.md']
evidence = [D / name for name in names]
assert all(path.exists() for path in evidence)
raw = {
    'id': SLUG,
    'title': 'D5 fixed binary240→C23：全pair容量通过，紧packet26forms但12720规范共享电压全NO',
    'family': 'Ordinary cyclic covers of controlled binary route-packet base graphs',
    'idea_family': 'idea:ddp-open-parameter-construction-20261026',
    'date': '2026-11-02', 'wiki_verdict': 'no',
    'record_type': 'fixed_base_four_global_voltage_coefficient_family_exclusion',
    'target_Delta': 8, 'target_D': 5, 'savedL': 5334,
    'baseline_date': 'Inherited current-main(8,5)=5334; no fresh priority claim or primary comparison in this publication',
    'n': {'actual': None, 'hypothetical': 5520},
    'actual_graph_Delta': None, 'actual_D': None, 'ordinary_bad_unordered_pairs': None,
    'ordinary_bad_target_D': 5, 'new_lower_bound': False,
    'actual_D_scope': 'No5520targetgraphgenerated. Theactual240/960/8regularbasehasD4fromitsnewcalibration240rootcheck,notanewtargetrecord. BaseNB0..5allpaircapacitypass; onefrozenpair8to70packetexcludesallfourglobalcoefficients. No voltageassignedallpairD5testor targetgraphBFS.',
    'outcome_class': root['root_status'],
    'scope': 'Only fixed actualbinary240base plus ordinaryC23translationcover with fourGLOBALcoefficients(cA,dA,cB,dB): port0 cA+lambda*dA,port1negative,port2 cB+lambda*dB,port3negative,actualreversekeepslambda. All12720nonzeroscalar-normalizedF23^4representatives failtheonepacket8to70;zerois23disconnectedcopies. Notarbitraryedge-dependent23voltages,permutationcovers,otherbases or general(8,5).',
    'distance_text': '240/960全8度底图只是校准来源，实际D4不计目标成果。全240roots的所有有序basepair NB≤5路径容量最小66≥23，无不足pair；8→70按长3/4/5为1/10/55。先存PRED后从已存typed实际pointedge得66paths/26distinct四系数forms，数量预测被支持；全部12720非零scalar规范参数在此一pair无survivor，max phase覆盖22，存在一组覆盖23的预测被反驳。一个必要packet的完整参数NO足够关闭四共享系数规则；没有把全pairs容量过当cover。全零断开，非零并不自动连通/互不同构。samecase1.496812969/5；0target5520graph/solver/Lean/ARIS。',
    'lesson_and_restart_condition': 'TheoldD3binarypacketmechanism can supply anactualbase withample NBroutecapacity for a D5ordinarycover,but routecounts anddistinctlinearforms areonlynecessary. Sharedglobalcoefficients force endpointaliases:26forms neverevaluateontoall23phases across thecompletefiniteprojectivedomain. Thisdoesnotmake same-formcollisionsunavoidableforarbitraryedgevoltages. Stopfixedfourcoefffamily; nofield/fold/base/seed/parameterladder or targetgraphclaim.',
    'restart_condition': 'STOP this fixedbase/fourglobalcoeffC23family. A separatelyauthorized changedrule may readthealready-savedpaths to distinguishglobal-formaliases fromactualedge-voltage constraints; no automaticnewordinarycover search or repeatedpacket evaluation.',
    'unclosed_gap': 'Arbitraryedge-dependentC23covers,permutationcovers,otherbases andgeneral(8,5) remainopen. No full5520graph,newlowerbound,parameter,Lean,independentmethodorpriorityclaim. Base240D4calibrationisnotaportfoliotargetresult. The66path/26form/12720parameter counts aredistinctobjects,notnumbersofnewgraphs.',
    'positive_guarantees': [
        'Use actualpoint-edgeinverse(p,lambda)<->(barp,lambda); lambda is anintegerbitbeforemod23,notanF2toF23fieldhomomorphism.',
        'NB removesonlyimmediatereversalofthesameactualpointedge; controllerportreversewithadifferentlambda isnotautomaticallydeleted. Emptywalksincludedwhereapplicable.',
        'Everyordinarybasepathhasuniquelift,soallpairNBcount>=23isonlyanecessarycapacitygate; theactualminimum66supportscontinuedparameterworkwithoutprovingacover.',
        'For fixedfourglobalcoefficients eachpathvoltageisitsintegercoeffvector mod23 dotparameter; theactual66paths yield26forms. Onefixedpairfailureforallparameters refutesthewholefixedrule.',
        'Commonnonzeroscalargivesfibrephasere-labeling;firstnonzero=1representsallnonzerovectorsin12720classes,notnecessarilyconnectedornonisomorphicgraphs. Zeroisdisconnected.',
        'Thepaperreviewdistinguishestheglobalformcollision(paths1/14)fromarbitraryactualedgevoltages,includingtheparticularedge8–104separationexample; no extra numericaledge-voltage gate is claimed.',
        'PRED_ONE_CRITICAL_PACKETprecedesrunning. Existingbasecalibration/packetfees arepreservedwithin1.496812969/5;nonewsourcevalidation,solver,Lean,ARIS or targetgraphBFS.'
    ],
    'other_metrics': {
        'new_graphs': 0, 'new_parameter_pairs': 0, 'new_Lean_instances': 0, 'new_independent_method_claims': 0,
        'single_research_record': True, 'base_calibration_not_target_record': True,
        'base_n': 240, 'base_m': 960, 'base_degree': 8, 'base_actual_D': 4,
        'new_base_calibration_BFS_roots': 240, 'target_order': 5520, 'target_degree': 8, 'target_D': 5,
        'base_capacity_allorderedpairs_complete': True, 'minimum_NB0to5_paths': 66,
        'ordered_basepairs_below23': 0, 'critical_pair': [8, 70],
        'critical_packet_paths': 66, 'critical_steps0to5': [0, 0, 0, 1, 10, 55],
        'distinct_four_coefficient_forms': 26, 'forms_atleast23_prediction': 'SUPPORTED',
        'cover23phase_parameter_exists_prediction': 'REFUTED_COMPLETE_PROJECTIVE_DOMAIN',
        'nonzero_normalized_parameters_checked': 12720, 'parameter_survivors': 0,
        'maximum_actual_phase_coverage': 22, 'zero_parameter_disconnected_paper': True,
        'nonzero_not_claimed_connected_or_nonisomorphic': True,
        'allpair_voltage_search_performed': False, 'target5520_graph_generated': False,
        'samecase_CPU': 1.496812969, 'case_cap': 5,
        'base_initial_case_CPU': 1.148210378, 'new_packet_preparation_CPU': 0.15,
        'new_packet_process_CPU': 0.198602591,
        'new_solver_Lean_ARIS_oldsource_validation_target_BFS': 0,
        'sameform_not_arbitrary_edgevoltage_obstruction': True,
        'all_processes_terminal': True, 'same_Goal': 'ACTIVE', 'old_N8_n61': 'PAUSED'
    },
    'evidence_paths': [relative(path) for path in evidence]
}
row, rowfile = H['write_node'](raw, PREFIX)
ledger['rows'].append(row)
ledger['record_count'] = 459
H['persist'](ledger, rowfile, now)
node = 'experiments/' + SLUG + '.md'
summary = f'''\n\n{MARKER}
### {now} D5 fixed binary240普通C23：容量足够，四共享系数完整NO

240/960/全8度、actualD4是新校准底图，不计targetrecord。全部basepair NB≤5容量≥66≥23；最紧8→70有66paths（长3/4/5为1/10/55）。运行前PRED先冻结该packet，26distinctforms支持数量预测；全部12720非零scalar规范四系数0survivor、max仅22phase，覆盖23的预测被反驳。全零23份断开，规范代表不等于连通或非同构图。

严格NO只限fixedbase/四GLOBAL系数普通C23，不排任意逐实际边电压、一般23covers或8D5。实际reverse保同lambda，按整数bit累加后mod23；NB不误删不同lambda的controllerbacktrack。paper paths1/14同form与edge8–104可分离示例只说明scope，不新跑逐边搜索。0目标5520图/solver/Lean/ARIS/目标图BFS，最终1.496812969/5，全STOP，不field/fold/base/参数梯。

458→459只一个研究节点，0新图/参数/Lean/方法；153/43/47、旧458rows/人工顶块保持。[canonical节点]({node})；[root终态](../{relative(D / 'ROOT_DISPOSITION.json')})；[scope paper](../{relative(review)})。

'''
H['update_pages'](old, human, summary, 1)
(W / 'DDP_METHOD_LEDGER.md').write_text(md_before + summary.replace('### ', '## ', 1))
after = load(ledger_path)
assert after['record_count'] == len(after['rows']) == 459
assert after['rows'][:-1] == before['rows']
H['unchanged_top'](before, after)
receipt = {
    'status': 'PASS_ONE_D5_BASE240_FOUR_GLOBAL_COEFFICIENT_C23_TERMINAL_NODE',
    'updated_UTC': now, 'records_before': 458, 'records_after': 459, 'records_added': 1,
    'new_experiment_id': SLUG, 'canonical_node': 'research-wiki/' + node, 'row_path': relative(rowfile),
    'actual_base_calibration': {'n': 240, 'm': 960, 'degree': 8, 'D': 4, 'not_target_record': True},
    'allpair_NB_capacity_pass_minimum': 66,
    'critical_packet': {'pair': [8, 70], 'paths': 66, 'forms': 26, 'tested_parameters': 12720, 'survivors': 0, 'maxphasecoverage': 22},
    'pred_before_run_preserved': True,
    'strict_scope': 'Onlyfixedbase/fourglobalcoefficients/ordinaryC23',
    'arbitrary_edge_voltages_and_other23covers_not_excluded': True,
    'scope_review_linked_actual_existing': relative(review),
    'samecase_CPU': 1.496812969, 'case_cap': 5,
    'target_graph_generated': False, 'new_math_solver_BFS_field_Lean_ARIS': 0,
    'other458rows_preserved_exact': True, 'row_order_preserved': True,
    'human_top_blocks_preserved_exact': {name: True for name in H['FILES']},
    'index_experiments_before': index_before, 'index_experiments_after': index_before + 1,
    'graph_parameter_Lean_method_increments': [0, 0, 0, 0],
    'graph_parameter_Lean_snapshot_preserved': [153, 43, 47],
    'full_rebuild_reimport': False, 'root_STATE_ROUND_HTML_AGENTS_modified': False,
    'modified_outputs': ['research-wiki/' + node, 'research-wiki/DDP_METHOD_LEDGER.json', 'research-wiki/DDP_METHOD_LEDGER.md'] + ['research-wiki/' + name for name in H['FILES']] + [relative(rowfile)],
    'sync_process_CPU_seconds': time.process_time() - started,
    'stop': True
}
receipt_path = S / (PREFIX + '_RECEIPT.json')
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'receipt': relative(receipt_path), 'before': 458, 'after': 459, 'add': 1, 'CPU': receipt['sync_process_CPU_seconds']}, ensure_ascii=False), flush=True)

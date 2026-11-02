"""Upsert the existing D5 node, preserving its complete four-coefficient NO."""
from pathlib import Path
import copy
import json
import runpy
import time

ROOT = Path(__file__).resolve().parents[4]
S = Path(__file__).resolve().parent
W = ROOT / 'research-wiki'
D = ROOT / 'research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D5/binary_C30_base240_C23_cover'
PREFIX = 'EDGE_VOLTAGE_LOCAL_FULL_AND_GLOBAL32_20261102'
SLUG = 'ddp-d5-fixed-binary240-four-global-coefficient-c23-cover5520-complete-no-20261102'
MARKER = '<!-- ' + PREFIX + ' -->'
started = time.process_time()
H = runpy.run_path(str(S / 'sync_source650_then_d4_binary_terminals_20261102.py'))
load, relative = H['load'], H['relative']
now = H['stamp']()
root = load(D / 'EDGE_VOLTAGE_ROOT_DISPOSITION.json')
one = load(D / 'edge_voltage_packet/RESULT.json')
allpair = load(D / 'allpair_edgeflow_gate/RESULT.json')
sample = load(D / 'conditional_global32/RESULT.json')
an, sn = allpair['native'], sample['native']
assert root['status'] == 'ROOT_ACCEPTED_EDGE_VOLTAGE_LOCAL_CONSTRUCTION_ALLPAIR_CAPACITY_PASS_32_NOHIT_FAMILY_UNKNOWN_STOP'
assert root['all_numeric_terminal'] and not root['complete_new_target_graph']
assert root['old_four_global_coefficient_NO_preserved']
assert one['distinct_signed_edge_flows'] == 66 and one['flow_difference_rank_mod23'] == 65
assert one['edge_support'] == 148 and one['witness_phase_coverage'] == 23
assert one['nonzero_edge_voltages'] == 21
assert an['unordered_packets'] == 28920 and an['total_NB_paths_saved_direction'] == an['total_distinct_signed_flows'] == 2699760
assert an['minimum_distinct_signed_flows'] == 66 and an['packets_below23_distinctflows'] == 0
assert an['diagonal_sign_pair_failures'] == 0 and an['diagonal_zero_flow_packets'] == 240
assert an['witness_full23_packets'] == 1 and an['first_witness_covered_phases'] == 9
assert sn['samples'] == 32 and sn['critical_packet_preserved_all']
assert sn['joint_critical_and_first_diagonal_full_samples'] == 24
assert not sn['full_D5_hit'] and sn['best_sample'] == 27
assert [sn[k] for k in ['best_full_packets', 'best_minimum_phase_coverage', 'best_diagonal_full', 'best_missing_phase_obligations']] == [19987, 18, 200, 10784]
assert abs(sample['samecase_CPU'] - 5.704705500) < 1e-12 and sample['case_cap'] == 20
ledger_path = W / 'DDP_METHOD_LEDGER.json'
ledger = load(ledger_path)
assert ledger['record_count'] == len(ledger['rows']) == 459
positions = [i for i, row in enumerate(ledger['rows']) if row['id'] == SLUG]
assert len(positions) == 1
pos = positions[0]
before = copy.deepcopy(ledger)
raw = copy.deepcopy(ledger['rows'][pos]['source_record'])
historical = copy.deepcopy(raw)
assert historical['outcome_class'] == 'ROOT_ACCEPTED_FIXED_FOUR_COEFFICIENT_C23_NO_STOP'
assert historical['other_metrics']['nonzero_normalized_parameters_checked'] == 12720
assert historical['other_metrics']['parameter_survivors'] == 0
assert historical['other_metrics']['samecase_CPU'] == 1.496812969
assert not (S / (PREFIX + '_RECEIPT.json')).exists()
old, human, index_before = H['page_snapshot'](MARKER)
md_before = (W / 'DDP_METHOD_LEDGER.md').read_text()
assert MARKER not in md_before
evidence = [D / name for name in ['EDGE_VOLTAGE_ROOT_DISPOSITION.json', 'EDGE_VOLTAGE_NOTE.md', 'EDGE_VOLTAGE_INTERFACE.md', 'EDGE_FLOW_SCOPE_ATTACK.md', 'ONE_PACKET_AND_ALLPAIR_SCOPE_REVIEW.md', 'CONDITIONAL_GLOBAL_VOLTAGE_INTERFACE.md']]
for sub, names in [
    ('edge_voltage_packet', ['PRED.md', 'run_once.py', 'RESULT.json', 'TERMINAL.json', 'SIGNED_EDGE_FLOWS.json', 'VOLTAGE_WITNESS.json']),
    ('allpair_edgeflow_gate', ['PRED.md', 'run.cpp', 'run_once.py', 'RESULT.json', 'TERMINAL.json', 'PACKETS.tsv', 'PACKET_CACHE_OFFSETS.tsv', 'ALL_PACKET_FLOWS.bin']),
    ('conditional_global32', ['PRED.md', 'run_once.py', 'run.cpp', 'RESULT.json', 'TERMINAL.json', 'SAMPLES.tsv', 'ALL_VOLTAGES.tsv', 'BEST_VOLTAGE.json', 'BEST_PACKET_PHASES.tsv', 'BEST_BY_NB_COUNT.tsv', 'CONSTRAINT_RREF.json'])
]:
    evidence += [D / sub / name for name in names]
assert all(path.exists() for path in evidence), [relative(path) for path in evidence if not path.exists()]

raw.update({
    'title': 'D5 fixed binary240逐边C23：单packet构造成功、全flow容量过，32全局参数无hit仍UNKNOWN',
    'wiki_verdict': 'partial',
    'record_type': 'fixed_base_ordinary_C23_local_voltage_construction_and_bounded_global_sample_UNKNOWN',
    'baseline_date': 'Inherited actual main(8,5)=5334,root last read2026-11-02 02:10:08UTC; no new comparison performed by Wiki sync',
    'actual_D_scope': 'No complete5520targetgraphorD5hit. Earlieractual240/960/8regularD4basecalibrationisnotatargetrecord. Oneexplicit960edgevoltagecovers8to70all23phases; all28920basepackets pass flowcapacity,butthat21nonzeroedgewitnessfailsglobalD5. A fixed32sample conditionalglobalbatch yields nofullD5hit; familyUNKNOWN,notexhaustiveNO.',
    'outcome_class': root['status'],
    'scope': 'OneexistingD5researchchainonfixedbinary240andordinaryC23antisymmetricactualpoint-edgevoltages. HistoricalfourGLOBALcoefficients remainstrictNOafterall12720nonzeroscalarrepresentatives. Independent960edgevoltagesareanewlargerconnectionrule:66savedpathsbecome66flows/rank65,and22independentpathdifferencesgiveonecriticalfull23witness. OnefreshallpairNBflowcachehasnoaliasedpaths/min66. Thenonly32fixed-seedparametersin22prescribedequationaffinespacearecheckedglobally;nocompleteD5hit,soevenconditionalfamilyremainsUNKNOWN. The22equationsarenotWLOGforarbitrarysuccessfulcovers. No arbitrarypermutationcoverNO,nofold/base/seedladder.',
    'distance_text': '旧four-globalcoeff 12720严格NO保留完整历史。新增逐实际边电压：原66paths的flows全不同/148边支撑/相对rank65；解22独立差得到21非零边显式电压，8→70满23，真正移除旧共享障碍。全28920含diagonal packets一次枚2699760paths，flows也2699760/min66，diagonal81..97、每个含唯一0、0反号缺配；容量未排。但稀疏局部解仅关键1packet满23，首diag0→0只有9。改为22约束仿射空间中938free坐标固定seed32样本：32critical均23，24同时修首diag；0完整D5 hit。best27为19987/28920满23、最低18、diag200/240、missingphase义务10784。它们不是目标普通坏点对数。累计5.704705500/20，0目标5520边表/目标BFS/solver/Lean/ARIS，不第33例或hillclimb。',
    'lesson_and_restart_condition': 'Separate three mechanisms: four-globalformsharingcausedtheoldNO; independentedgeflowrank65constructivelyremovesonepacketobstruction; sparsechoiceofunusedvariablesleavesotherpacketsbad. Fixedconditionalglobal32samplingrepairscritical+firstdiagonaltogetherin24casesbutdoesnotcoordinateallpackets. Stopunstructuredfreevoltage samplingwithout33rdsample/seed/hillclimb; anewquestionmustprovideaconcretemultipacketcompatibilityrule. Do not convert32samples intoa wholeaffinespaceorordinarycoverNO.',
    'restart_condition': 'STOP currentconditionalfreeedgevoltage sampling; no33rdsample,newseed,hillclimb,field/fold/base ladder orpositivegraphsuite. A future separatelyauthorized structuralrule must keepfixedfourcoeffNO,localfull23constructionandglobalUNKNOWNseparate.',
    'unclosed_gap': 'AllindependentantisymmetricC23edgevoltagesonthisbase remainUNKNOWN,asdoes thechosen22equationaffinespace. ThoseprescribedphaseconstraintsarenotWLOGforallD5covers. Arbitrarypermutationcovers,otherbasesandgeneral(8,5)alsoremainunexcluded. No fulltargetgraph,newrecord,parameter,Lean orindependentmethodclaim. A3645sourcework is notincludedinthisnode.',
    'positive_guarantees': [
        'ThecompleteoldfourglobalcoefficientNOanditsfullrawsource_recordarepreservedverbatimunderhistorical_four_global_coefficient_record_before_edge_voltage_20261102; itsROOT/NOTEfilesarenotmodified.',
        'Independentactualpoint-edgevoltagesuseminlabel-to-maxlabelorientationandreverseminus. The66savedpathflowdifferenceshaveactualrank65; solving22independentdifferencesandcheckingall66phasesconstructsonefull23packetwithoutnewwords/BFS.',
        'AllpairDFSonlyfiltersrecordedendpointu<=v,notintermediatelabels. Reversepathnegatesflow,diagonalemptywalkretained,so28920storedpacketsarecompleteforC23phasecoverage.',
        'All2699760NBflowsareuniquewithintheirpackets/min66; diagonalzeroandsignpairchecksagreewiththeintegerflowcontract. This isnecessarycapacitypass,notexistenceorallpermutationcoverevidence.',
        'RREFreconstructiongiveseveryoneofthefixed32samplesall22equations,criticalfull23checkedexplicitly. EachsampleusescompleteflowcachewithnoextraBFS/pathgeneration;all32globaltestsareexactfortheirparameters.',
        'Packetfullcountsandmissingphaseobligationsarenot5520ordinarybadpaircounts. Bestsampleisbystaticreporting,notfeedbackhillclimb; nofullD5hitmeansnosavedcompleteedgefileoracceptedgraph.',
        'RawcaseCPUprogress1.496812969->1.713051688->3.535598698->5.704705500isretainedwithauthorizedcapchanges,notresetbydocumentation. No33rdsampleornewsolver/source/field/Lean/ARIS.'
    ]
})
raw['other_metrics'] = {
    'new_graphs': 0, 'new_parameter_pairs': 0, 'new_Lean_instances': 0, 'new_independent_method_claims': 0,
    'same_existing_research_node_no_new_record': True,
    'historical_four_global_coefficient_record_before_edge_voltage_20261102': historical,
    'four_global_coefficient_closed_subfamily': {
        'status': 'COMPLETE_NO_FIXED_BASE_FOUR_GLOBAL_COEFFICIENT_C23_FAMILY',
        'paths': 66, 'forms': 26, 'scalar_representatives': 12720, 'survivors': 0, 'maxphases': 22,
        'original_case_CPU': 1.496812969, 'original_cap': 5, 'not_rerun': True
    },
    'base_calibration': {'n': 240, 'm': 960, 'degree': 8, 'D': 4, 'not_target_record': True, 'initial_calibration_roots': 240, 'not_rerun': True},
    'target': [8, 5, 5520], 'saved_main': 5334,
    'one_packet': one,
    'allpair_flow_gate': allpair,
    'conditional_global32': sample,
    'all_independent_edge_voltage_family': 'UNKNOWN',
    'conditional22equation_family': 'UNKNOWN_NOT_EXHAUSTIVE',
    'conditional22constraints_are_not_WLOG': True,
    'samecase_CPU': 5.704705500, 'case_cap': 20,
    'CPU_stage_history': [1.496812969, 1.713051688, 3.535598698, 5.704705500],
    'all_stages_terminal': True, 'target5520_edgefile_generated': False,
    'new_target_BFS_source_validation_solver_Lean_ARIS': 0,
    'current_publication_recomputations': 0,
    'no33rdsample_seed_hillclimb': True, 'A3645_readgate_included': False,
    'same_Goal': 'ACTIVE', 'old_N8_n61': 'PAUSED'
}
raw['evidence_paths'] = list(dict.fromkeys(historical['evidence_paths'] + [relative(path) for path in evidence]))

# The old node's frontmatter says "no" for the closed four-coefficient rule.
# Its broader current chain is UNKNOWN; change only this node's metadata.
helper = H['COMMON']['helper']
original_loader = helper._load_paper_frontmatter
nodepath = W / 'experiments' / (SLUG + '.md')
def target_meta(path):
    meta = original_loader(path)
    if Path(path).resolve() == nodepath.resolve():
        meta = dict(meta)
        meta['verdict'] = 'partial'
        meta['duration'] = 'samecase5.704705500/20CPU; originalfourcoeff1.496812969/5historyretained'
    return meta
helper._load_paper_frontmatter = target_meta
try:
    row, rowfile = H['write_node'](raw, PREFIX)
finally:
    helper._load_paper_frontmatter = original_loader
ledger['rows'][pos] = row
H['persist'](ledger, rowfile, now)
node = 'experiments/' + SLUG + '.md'
summary = f'''\n\n{MARKER}
### {now} 同D5节点累计更新：逐边电压局部构造满23，32全局样本仍UNKNOWN

旧fixedbase/fourGLOBALcoeff12720严格NO完整保历史。改独立point-edge电压后，原66paths变66flows、148edge支撑、差rank65；22独立差构造显式21非零边解，8→70实际满23。一次全pair流门28920含diagonal packets/2699760paths与flows均等、min66；diag81..97、唯一0、无±缺配，容量没有排。局部稀疏解却仅1packet满23，首diag0→0仅9。

保关键22等式，固定seed从完整仿射解空间采32例（不是穷尽、这些等式也非WLOG）：32critical恒23、24同时修0→0；0 fullD5 hit。best27有19987/28920packet满23、最低18、diag200/240、10784missingphase义务，非普通坏对数。全独立C23及条件子空间仍UNKNOWN，不能升级NO或新图。累计5.704705500/20，0目标边表/BFS/solver/Lean/ARIS，停止第33例/seed/hillclimb。

459→459/add0，只原位更新同研究节点；旧458rows/人工顶块与153/43/47保持，不混A3645。[canonical节点]({node})；[新root聚合终态](../{relative(D / 'EDGE_VOLTAGE_ROOT_DISPOSITION.json')})；[scope核读](../{relative(D / 'ONE_PACKET_AND_ALLPAIR_SCOPE_REVIEW.md')})。

'''
H['update_pages'](old, human, summary, 0)
(W / 'DDP_METHOD_LEDGER.md').write_text(md_before + summary.replace('### ', '## ', 1))
after = load(ledger_path)
assert after['record_count'] == len(after['rows']) == 459
assert [r['id'] for r in after['rows']] == [r['id'] for r in before['rows']]
assert all(after['rows'][i] == before['rows'][i] for i in range(459) if i != pos)
assert row['source_record']['other_metrics']['historical_four_global_coefficient_record_before_edge_voltage_20261102'] == historical
assert original_loader(nodepath)['verdict'] == 'partial'
H['unchanged_top'](before, after)
receipt = {
    'status': 'PASS_EXISTING_D5_NODE_LOCAL_EDGE_VOLTAGE_AND_GLOBAL32_UNKNOWN_UPSERT',
    'updated_UTC': now, 'records_before': 459, 'records_after': 459, 'records_added': 0,
    'updated_id': SLUG, 'canonical_node': relative(nodepath), 'row_path': relative(rowfile),
    'historical_four_global_coeff_record_preserved_exact': True,
    'four_global_coeff_strict_NO_12720_preserved': True,
    'original_four_coeff_ROOT_NOTE_untouched': True,
    'current_verdict': 'partial', 'current_independent_edge_voltage_family': 'UNKNOWN',
    'conditional22constraints_not_WLOG_or_exhaustive': True,
    'one_packet': {'paths': 66, 'flows': 66, 'support_edges': 148, 'relative_rank': 65, 'phasecoverage': 23, 'nonzero_edges': 21},
    'allpair': {'packets': 28920, 'paths_and_distinctflows': 2699760, 'minflow': 66, 'diagonal_range': [81, 97], 'zero_packets': 240, 'signpair_fail': 0, 'localwitness_full_packets': 1, 'firstdiagonal_covered': 9},
    'conditional_global32': {'samples': 32, 'criticalall23': True, 'jointfirstdiagonal_full': 24, 'fullD5hit': False, 'best_sample': 27, 'fullpackets': 19987, 'minimum_coverage': 18, 'diagonal_full': 200, 'missingphase_obligations': 10784},
    'samecase_CPU_preserved': 5.704705500, 'case_cap': 20, 'no_doc_timer_reset': True,
    'other458rows_preserved_exact': True, 'row_order_preserved': True,
    'human_top_blocks_preserved_exact': {name: True for name in H['FILES']},
    'index_experiments_before': index_before, 'index_experiments_after': index_before,
    'graph_parameter_Lean_method_increments': [0, 0, 0, 0],
    'graph_parameter_Lean_snapshot_preserved': [153, 43, 47],
    'full_rebuild_reimport': False, 'root_STATE_ROUND_HTML_AGENTS_modified': False,
    'new_math_solver_BFS_field_Lean_ARIS': 0, 'A3645_included': False,
    'modified_outputs': [relative(nodepath), 'research-wiki/DDP_METHOD_LEDGER.json', 'research-wiki/DDP_METHOD_LEDGER.md'] + ['research-wiki/' + name for name in H['FILES']] + [relative(rowfile)],
    'sync_process_CPU_seconds': time.process_time() - started,
    'stop': True
}
receipt_path = S / (PREFIX + '_RECEIPT.json')
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'receipt': relative(receipt_path), 'before': 459, 'after': 459, 'add': 0, 'CPU': receipt['sync_process_CPU_seconds']}, ensure_ascii=False), flush=True)

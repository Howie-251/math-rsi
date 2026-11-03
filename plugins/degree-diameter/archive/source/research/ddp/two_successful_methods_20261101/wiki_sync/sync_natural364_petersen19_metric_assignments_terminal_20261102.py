"""Publish one Petersen19 cohort from accepted metric/SAT terminal evidence."""
from pathlib import Path
import copy
import json
import runpy
import time

ROOT = Path(__file__).resolve().parents[4]
S = Path(__file__).resolve().parent
W = ROOT / 'research-wiki'
D = ROOT / 'research/ddp/two_successful_methods_20261101/retained_edge_transfer/natural364_petersen_subdivision19'
PREFIX = 'NATURAL364_PETERSEN19_METRIC_ASSIGNMENTS_TERMINAL_20261102'
SLUG = 'ddp-natural364-petersen19-subdivision-metric-and-port-assignment-raw-terminal-20261102'
MARKER = '<!-- ' + PREFIX + ' -->'
started = time.process_time()
H = runpy.run_path(str(S / 'sync_source650_then_d4_binary_terminals_20261102.py'))
load, relative = H['load'], H['relative']
now = H['stamp']()
root = load(D / 'ROOT_DISPOSITION.json')
metric = load(D / 'RESULT.json')
first5 = load(D / 'port_assignment_sat/RESULT.json')
sixth = load(D / 'port_assignment_sat/remaining_orbit5/RESULT.json')
diag = load(D / 'port_assignment_sat/coverage_split_diagnostic/RESULT.json')
model0 = load(D / 'port_assignment_sat/orbit0/MODEL.json')
review = D / 'port_assignment_sat/PORT_ASSIGNMENT_TERMINAL_SCOPE_REVIEW.md'
assert review.exists(), 'Wait for the already-accepted scope review to be saved; do not rerun any model.'
assert root['status'] == 'ROOT_ACCEPTED_HELPER19_METRIC_SURVIVORS_ALL6_ASSIGNMENT_RAW_UNSAT_DIAGNOSTIC_UNKNOWN_STOP'
assert root['all_numeric_terminal'] and root['samecase_CPU'] == 9.371241682 and root['samecase_cap'] == 40
assert metric['patterns'] == metric['expected_domain'] == 5005
assert metric['survivors'] == 235 and metric['diameter_histogram'] == {'5': 4770, '4': 235}
assert metric['helper_metric_BFS_roots'] == 95095
assert root['helper_orbits'] == 6 and root['orbits_untested'] == 0
assert len(root['all_solver_cases']) == 6
assert all(case['status'] == 'RAW_UNSAT_NOT_PROOFCHECKED' and case['returncode'] == 20 and not case['proof_checked'] for case in root['all_solver_cases'])
assert first5['orbits_tested'] == 5 and first5['orbits_untested'] == 1
assert sixth['orbits_tested'] == 1 and sixth['orbits_untested'] == 0
assert diag['status'] == 'UNKNOWN_SUBMODEL_STOP' and diag['incompatible_split'] is None
assert [case['status'] for case in diag['cases']] == ['RAW_UNSAT', 'RAW_UNSAT', 'UNKNOWN']
assert [case['helpers'] for case in diag['cases']] == [list(range(9)), list(range(4)), list(range(2))]
assert not root['formal_UNSAT_proof_checked'] and not root['complete383_graph_generated']
assert model0['variables'] == 1848 and model0['clauses'] == 10528 and model0['coverage_clauses'] == 6916
ledger_path = W / 'DDP_METHOD_LEDGER.json'
ledger = load(ledger_path)
assert ledger['record_count'] == len(ledger['rows']) == 460
assert not any(row['id'] == SLUG or '/natural364_petersen_subdivision19/' in json.dumps(row, ensure_ascii=False) for row in ledger['rows'])
assert not (S / (PREFIX + '_RECEIPT.json')).exists()
before = copy.deepcopy(ledger)
old, human, index_before = H['page_snapshot'](MARKER)
md_before = (W / 'DDP_METHOD_LEDGER.md').read_text()
assert MARKER not in md_before
evidence = [D / name for name in ['PRED.md', 'run_once.py', 'SKELETON.json', 'RESULT.json', 'TERMINAL.json', 'ALL_PATTERN_METRICS.json', 'SURVIVORS.json', 'BEST_METRIC_PATTERN.json', 'ASSIGNMENT_EXACTNESS_PAPER.md', 'ROOT_DISPOSITION.json', 'NOTE.md']]
for sub, names in [
    ('port_assignment_sat', ['PRED.md', 'run_once.py', 'HELPER_ORBITS.json', 'RESULT.json', 'TERMINAL.json', 'PORT_ASSIGNMENT_TERMINAL_SCOPE_REVIEW.md']),
    ('port_assignment_sat/remaining_orbit5', ['PRED.md', 'run_once.py', 'RESULT.json', 'TERMINAL.json', 'orbit5/MODEL.json', 'orbit5/RESULT.json']),
    ('port_assignment_sat/coverage_split_diagnostic', ['PRED.md', 'run_once.py', 'RESULT.json', 'TERMINAL.json'])
]:
    evidence += [D / sub / name for name in names]
for orbit in range(5):
    evidence += [D / 'port_assignment_sat' / ('orbit' + str(orbit)) / name for name in ['MODEL.json', 'RESULT.json']]
assert all(path.exists() for path in evidence)
raw = {
    'id': SLUG,
    'title': '自然364 Petersen19合作骨架：235 metric过门→6helper轨道全raw UNSAT，诊断仍UNKNOWN',
    'family': 'Natural H3 polarity port extension',
    'idea_family': 'idea:ddp-open-parameter-construction-20261026',
    'date': '2026-11-02', 'wiki_verdict': 'partial',
    'record_type': 'helper_metric_and_exact_port_assignment_raw_solver_cohort',
    'target_Delta': 4, 'target_D': 5, 'savedL': 364,
    'baseline_date': 'Inherited natural364/714 polarityhost and sourceD5; no new primary comparison or record claim',
    'n': {'actual': None, 'hypothetical': 383},
    'actual_graph_Delta': None, 'actual_D': None,
    'ordinary_bad_unordered_pairs': None, 'ordinary_bad_target_D': 5, 'new_lower_bound': False,
    'actual_D_scope': 'No complete383targetgraphgenerated. 5005labelledPetersen9-edge-subdivisionhelperpatterns getsmallHmetricqueries;235diam4patternsform6helperorbits. SixexactportassignmentCNFsreturnrawUNSATwithoutprooflogging/checking; orbit0coverage-localization stopsUNKNOWN athelpers0..1. NotactualtargetdiametermeasurementorformalglobalNO.',
    'outcome_class': root['status'],
    'scope': 'Fixednatural364/714 oldgraphpreserved,noaddedoldold,max4/D5,28actualdegree3ports. HelperH isPetersen10with9distinctedges eachsubdividedonce,H19/m24;10originalhelpersown1porteach,9subdivisionhelpersown2each. All5005labelledpatternsmetricchecked;235necessarysurvivorsreducevia120Petersenautomorphismsto6helperorbits,withoutassuminganyoldporttransitivity. AllsixassignmentmodelsareterminalrawUNSAT_NOT_PROOFCHECKED;noformalUNSATcertificate/no383file. Orbit0diagnostic0..8and0..3rawUNSAT,0..1two-secondUNKNOWN;noclaimofminimalcore,singlehelperimpossibilityorclassifiedsharedconflict. Nototherhelpergraphs,othersubdivisioncounts,arbitraryfiniteH,general383/(4,5).',
    'distance_text': '改变14helper叶/无port父点弱点，选全部helper有oldports的Petersen19。5005labelledpatterns中235的Hdiam4、4770的Hdiam5，metric正预测支持；95095是helper小图root queries，不是source/383BFS。120Petersenautomorphisms给6helper轨道，只重标helper，不猜旧ports对称。exactassignment用每port唯一owner/总容量28及19×364=6916覆盖OR，orbit0 MODEL1848vars/10528clauses；R2–R4旧缓存、R0/R1现有邻接。前5和此前未测第6各rawUNSAT/return20，无proofchecked，不能冒formal族NO。orbit0诊断0..8、0..3 rawUNSAT，0..1在2秒UNKNOWN；尚不能区分单helper自身覆盖还是sharedassignment冲突，不叫最小核。case9.371241682/40，0target383graph/BFS/Lean/ARIS。',
    'lesson_and_restart_condition': 'A newhelperconnectionrule genuinely passes metric while oldk14NOdoesnottransfer: allhelpersownports andsomeH19havediameter4. Exacthelper-oldcoverage is still a separateassignmentobligation. Completehelperorbitcoverage plusrawUNSAT provides boundednegativeevidence atsolverlevel,butnoproofcheckedformalNO. Diagnosticshrinksrawconflictto0..3coverageyet0..1UNKNOWNstopsclassification; donotclaimwhichmechanismfailed. StopthisfixedPetersen19familywithoutmorewindows,subdivisioncounts,seeds orproofchecking.',
    'restart_condition': 'STOP thisPetersen9-subdivisionhelperfamily andtheorbit0diagnostic; noresumingoldsixwindows,newseed/subdivisioncount orautomaticproofchecking. A separatelyauthorized changedmechanism mustnotinheritoldk14NOoutsideitsscope.',
    'unclosed_gap': 'RawUNSATwasnotproofchecked. General383/(4,5),otherhelpergraphs,otherhosts,oldedgechanges,addedoldold,andlargerk remainoutside thisboundedmodelscope. No classificationofsinglehelpervsjointassignmentobstruction,no minimalUNSATcore. New3D9readsandoldBfourcoeffNOarenotpartofthisnode. No graph/parameter/Lean/independentmethod/recordclaim.',
    'positive_guarantees': [
        'Sourceisnatural364/714with28freeports,notpublic364/728all4regular. RetainedoldedgesinheritoldoldD5; thecandidateorder383isconditionalonly.',
        '5005islabelledsubdivisionparametercount,notnonisomorphicgraphcount. The235metricdiam4patternsareanecessarygatebecauseeveryhelperownsaportarclength1;Hdiam5cannotcovereachothersportswithin5.',
        'Petersen120automorphismsreducehelperpatterns to6orbits; no oldportautomorphism/labelgaugeassumed. Helperpermutationpreservescapacityandthecompleteassignmentproblem.',
        'Atoldportspacing5,helper-to-oldwalk<=5cannottraversebetweenoldportsandreturntoH. Thusunion_g R_(4-dH)(P_g)exactlymodelshelper-oldcoverage; H-Hdiam4andoldoldinheritedcompleteD5cases.',
        'Portoneownerandhelpercapacitycardinality areexact; representativeorbit0has1848vars/10528clauses/6916coverageOR. Prefixatmostkencodingreviewissaved; no CNF orcoverage rerun bypublisher.',
        'All6rawUNSATstatusesretainproof_logged=false/proof_checked=false. First5historicalbatchandonesixthneworbitwindowareseparate,notoldtimerrestart.',
        'Diagnostic0..8and0..3rawUNSATwith0..1UNKNOWNdoesnotidentifya minimumUNSATcore orsinglehelper/sharedconflict. Stoppingatthelimitispreserved.',
        'Allnumericsterminal,source/target383BFS,oldballrecompute,LeanandARISzero. Newacceptedgraph/parameter/methodcountsremainzero.'
    ],
    'other_metrics': {
        'new_graphs': 0, 'new_parameter_pairs': 0, 'new_Lean_instances': 0, 'new_independent_method_claims': 0,
        'single_cohort_research_record': True,
        'source_n': 364, 'source_m': 714, 'free_ports': 28,
        'helper_n': 19, 'helper_m': 24, 'subdivided_distinct_Petersenedges': 9,
        'helper_spoke_capacities': {'original10': 1, 'subdivision9': 2},
        'conditional_target_n': 383, 'conditional_target_m': 766, 'conditional_degree': 4,
        'metric_stage': metric,
        'Petersen_automorphisms': 120, 'metric_survivors': 235, 'helper_orbits': 6,
        'oldports_transitivity_assumed': False,
        'representative_orbit0_model': {'variables': 1848, 'assignment_variables': 532, 'clauses': 10528, 'coverage_clauses': 6916},
        'all_solver_cases': root['all_solver_cases'], 'orbits_untested': 0,
        'original_first5_batch_preserved': first5,
        'sixth_previously_untested_orbit_batch': sixth,
        'coverage_split_diagnostic': diag,
        'proof_logged': False, 'proof_checked': False,
        'single_or_shared_obstruction_classified': False, 'minimal_UNSAT_core_claimed': False,
        'samecase_CPU': 9.371241682, 'case_cap': 40,
        'source_or_target383_BFS_oldball_Lean_ARIS': 0,
        'complete383_graph_generated': False, 'all_numeric_terminal': True,
        'helper14_node_or_Bfourcoeff_scope_changed': False,
        'same_Goal': 'ACTIVE', 'old_N8_n61': 'PAUSED'
    },
    'evidence_paths': [relative(path) for path in evidence]
}
row, rowfile = H['write_node'](raw, PREFIX)
ledger['rows'].append(row)
ledger['record_count'] = 461
H['persist'](ledger, rowfile, now)
node = 'experiments/' + SLUG + '.md'
summary = f'''\n\n{MARKER}
### {now} Petersen19单cohort：metric有235幸存，六assignment rawUNSAT，诊断停UNKNOWN

固定自然364/714保边/无oldold，Petersen10细分9条不同edge成H19/m24；10原helper各1port、9细分helper各2port，若成才有383/766全4度。5005labelledpatterns完整metric：235的Hdiam4、4770的Hdiam5，95095次只查helper小图。120Petersenautomorphisms给6helper轨道，不借旧port对称；完整assignment的6916helper-old OR与固定H下D5等价。

六主模型均rawUNSAT/return20、无prooflogged/checked；前5原结果不改，第6是此前未测orbit的新窗口，不续旧timer。orbit0覆盖诊断0..8、0..3 rawUNSAT，0..1的2秒窗口UNKNOWN；不能判单helper已不够、shared冲突或最小核，不冒formal整族NO。case9.371241682/40，0target383graph/source或383BFS/旧球重算/Lean/ARIS。

460→461只一个聚合研究节点，0图/参数/Lean/方法增量；153/43/47、旧460rows/人工顶块、helper14原node和B旧fourcoeffNO均保持。停止Petersen19，不换细分数或续模型，下一新读门不混入。[canonical节点]({node})；[root终态](../{relative(D / 'ROOT_DISPOSITION.json')})；[scope review](../{relative(review)})。

'''
H['update_pages'](old, human, summary, 1)
(W / 'DDP_METHOD_LEDGER.md').write_text(md_before + summary.replace('### ', '## ', 1))
after = load(ledger_path)
assert after['record_count'] == len(after['rows']) == 461
assert after['rows'][:-1] == before['rows']
H['unchanged_top'](before, after)
receipt = {
    'status': 'PASS_ONE_NATURAL364_PETERSEN19_METRIC_ASSIGNMENT_COHORT_NODE',
    'updated_UTC': now, 'records_before': 460, 'records_after': 461, 'records_added': 1,
    'new_experiment_id': SLUG, 'canonical_node': 'research-wiki/' + node, 'row_path': relative(rowfile),
    'metric': {'patterns': 5005, 'diam4': 235, 'diam5': 4770, 'helper_metric_roots': 95095},
    'Petersen120_automorphisms_helper_orbits': 6, 'oldport_symmetry_assumed': False,
    'main_assignment_cases': 6, 'main_rawUNSAT': 6, 'main_untested': 0,
    'proof_logged_or_checked': False,
    'representative_model': {'variables': 1848, 'clauses': 10528, 'coverage': 6916},
    'diagnostic': {'0to8': 'RAW_UNSAT', '0to3': 'RAW_UNSAT', '0to1': 'UNKNOWN_2SECOND', 'single_vs_shared_classification': None, 'minimum_core_claim': False},
    'samecase_CPU': 9.371241682, 'case_cap': 40, 'complete383_graph_generated': False,
    'old460rows_preserved_exact': True, 'row_order_preserved': True,
    'helper14_and_Bfourcoeff_scopes_preserved': True,
    'human_top_blocks_preserved_exact': {name: True for name in H['FILES']},
    'index_experiments_before': index_before, 'index_experiments_after': index_before + 1,
    'graph_parameter_Lean_method_increments': [0, 0, 0, 0],
    'graph_parameter_Lean_snapshot_preserved': [153, 43, 47],
    'full_rebuild_reimport': False, 'root_STATE_ROUND_HTML_modified': False,
    'new_math_solver_proofchecking_BFS_field_Lean_ARIS': 0,
    'modified_outputs': ['research-wiki/' + node, 'research-wiki/DDP_METHOD_LEDGER.json', 'research-wiki/DDP_METHOD_LEDGER.md'] + ['research-wiki/' + name for name in H['FILES']] + [relative(rowfile)],
    'sync_process_CPU_seconds': time.process_time() - started, 'stop': True
}
receipt_path = S / (PREFIX + '_RECEIPT.json')
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'receipt': relative(receipt_path), 'before': 460, 'after': 461, 'add': 1, 'CPU': receipt['sync_process_CPU_seconds']}, ensure_ascii=False), flush=True)

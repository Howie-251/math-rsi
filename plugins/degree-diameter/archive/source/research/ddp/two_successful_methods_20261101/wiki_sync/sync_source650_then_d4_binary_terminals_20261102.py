"""Two serial canonical Wiki updates from root-accepted terminal receipts only."""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import copy
import json
import re
import runpy
import time

ROOT = Path(__file__).resolve().parents[4]
W = ROOT / 'research-wiki'
S = Path(__file__).resolve().parent
STAGE = ROOT / 'research/ddp/two_successful_methods_20261101'
LEDGER = W / 'DDP_METHOD_LEDGER.json'
FILES = ['index.md', 'query_pack.md', 'gap_map.md']
HUMAN_END = '<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->'
COMMON = runpy.run_path(str(ROOT / 'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
COMMON['helper'].rebuild_index = lambda *_a, **_kw: None
COMMON['helper'].rebuild_query_pack = lambda *_a, **_kw: None


def load(path):
    return json.loads(path.read_text())


def relative(path):
    return str(path.relative_to(ROOT))


def stamp():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')


def page_snapshot(marker):
    old = {name: (W / name).read_text() for name in FILES}
    assert all(marker not in text and HUMAN_END in text for text in old.values())
    human = {name: text[:text.index(HUMAN_END) + len(HUMAN_END)] for name, text in old.items()}
    count = int(re.search(r'^## Experiments \((\d+)\)', old['index.md'], re.M).group(1))
    return old, human, count


def update_pages(old, human, summary, increment):
    for name in FILES:
        cut = len(human[name])
        text = old[name][:cut] + summary + old[name][cut:]
        if name == 'index.md' and increment:
            m = re.search(r'^## Experiments \((\d+)\)', text, re.M)
            text = text[:m.start(1)] + str(int(m.group(1)) + increment) + text[m.end(1):]
        (W / name).write_text(text)
        assert text.startswith(human[name])
        restored = text.replace(summary, '', 1)
        if name == 'index.md' and increment:
            m = re.search(r'^## Experiments \((\d+)\)', restored, re.M)
            restored = restored[:m.start(1)] + str(int(m.group(1)) - increment) + restored[m.end(1):]
        assert restored == old[name]


def write_node(raw, prefix):
    row = COMMON['normalize'](raw)
    row['goal']['baseline_date'] = raw['baseline_date']
    assert row['actual_order'] is None and row['actual_diameter'] is None
    assert not COMMON['capture'].screen(json.dumps(raw, ensure_ascii=False))
    rowfile = S / (prefix + '_ROW.json')
    rowfile.write_text(json.dumps(raw, ensure_ascii=False, indent=2) + '\n')
    with (S / (prefix + '_NODE_CALLS.log')).open('w') as out, contextlib.redirect_stdout(out):
        COMMON['write_node'](row)
    return row, rowfile


def persist(ledger, rowfile, now):
    ledger['updated_UTC'] = now
    ledger['input_counts'][relative(rowfile)] = 1
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + '\n')


def unchanged_top(before, after):
    for key, value in before.items():
        if key not in {'rows', 'record_count', 'updated_UTC', 'input_counts'}:
            assert after[key] == value
    for key, value in before['input_counts'].items():
        assert after['input_counts'][key] == value


def source650_update():
    started = time.process_time()
    now = stamp()
    prefix = 'SOURCE650_CAPACITY_AND_PROJECTED_TERMINAL_20261102'
    marker = '<!-- ' + prefix + ' -->'
    slug = 'ddp-stale-d10d3-650-eight-fp-endpoint-transfer651-mip-unknown-20261101'
    d = STAGE / 'stale_record_transfer_d10D3/fp_endpoint_transfer651'
    root = load(d / 'STRUCTURAL_AND_PROJECTED_ROOT.json')
    capacity = load(d / 'twin_class_packet_capacity_gate/RESULT.json')
    projected = load(d / 'projected_F_cover_once/RESULT.json')
    returned = load(d / 'projected_F_cover_once/SOLVER_RETURN.json')
    assert root['whole_rule_status'] == 'UNKNOWN' and root['wholecase_CPU'] == 42.416193092
    assert root['actual_capacity_pairs'] == root['capacity_upper_pass'] == 8385
    assert root['capacity_upper_fail'] == 0 and root['minimum_upper_surplus'] == 46
    assert root['C_f_size'] == 72 and root['D_p_size'] == 86 and root['twin_D_equal_count'] == 0
    assert projected['variables'] == 650 and projected['rows'] == 652 and projected['nnz'] == 50440
    assert returned['status'] == 1 and returned['incumbent'] is None
    assert not projected['actual_F_cover_object']
    ledger = load(LEDGER)
    assert ledger['record_count'] == len(ledger['rows']) == 456
    before = copy.deepcopy(ledger)
    positions = [i for i, row in enumerate(ledger['rows']) if row['id'] == slug]
    assert len(positions) == 1
    pos = positions[0]
    raw = copy.deepcopy(ledger['rows'][pos]['source_record'])
    historical = copy.deepcopy(raw)
    assert raw['other_metrics']['model_binary_variables'] == 1170
    assert raw['other_metrics']['wholecase_CPU_seconds'] == 22.084731374
    assert 'structural_and_projected_terminal_20261102' not in raw['other_metrics']
    old, human, old_index = page_snapshot(marker)
    md_before = (W / 'DDP_METHOD_LEDGER.md').read_text()
    assert marker not in md_before
    raw.update({
        'title': '10D3 actual650 FP转移：8385容量全过，650变量精确投影18秒仍UNKNOWN，0候选',
        'record_type': 'fixed_host_FP_twin_packet_capacity_and_exact_projected_cover_UNKNOWN',
        'outcome_class': root['status'],
        'wiki_verdict': 'partial',
        'actual_D_scope': 'No F-cover object,651candidate,donorassignment,PPpairing,newrootoroldrootBFS. Old1170window and new650integerprojectionboth timed outwithoutincumbent; complete8385capacityuppergate excludednone.',
        'scope': 'Fixed actual650/3250 all10 source,F520/P130/65K8,2twinclasses and PP cycles79/21/30. EightFPcuts have distinctF/Pends; newz joins8F+2selecteddonorP; remaining6P may be repaired by15pairings, retaining already-oldPPedges as legaldegree9 branches. The650binary projection is integer-equivalent only to the oldF-cover selection,notfull651/D3. All8385actualstarPpairs pass the capacityupperbound; no actualFcover found. Two distinct explicitlyauthorized solverencodings each had onewindow,notanoldtimercontinuation.',
        'distance_text': '旧1170/1302/90480唯一20秒UNKNOWN及22.084731374CPU完整保历史。新包容量门8385/8385全upper-pass、0fail、minsurplus46；Cf均72/Dp均86，65对twin的D全不同。首P0/73的U366、T449、实际八包并337，漏29，只展示该argmax重复，不能排其它cover。按K8,2消去donor得到650binary/652rows/50440nnz的整数精确F-cover投影，sole18秒HiGHS实际18.007674689CPU、status1/TimeLimit/primalNone，仍UNKNOWN。无F-cover、donor/PP/651graph/BFS。最终42.416193092/45含root整理，禁止第三solve/seed。',
        'lesson_and_restart_condition': 'Capacity was not scarce: ignoring cross-class overlap leaves every starpair unexcluded, while the first argmax stillmisses29. Exact integer projection removes locally reconstructible donor assignments without merging actualstarP Dcolumns or promising speedup. The new18secondwindow yielded noincumbent,notinfeasibility. Stop this source/FP-cover line; no thirdsolve,seed,morecuts,canonical-donor extrapolation or unexecutedrepairstage failure claims.',
        'restart_condition': 'STOP current650FP-cover chain. No thirdsolve/seed or automaticdonor/15pairing/BFS. A future separatelyauthorized genuinelynewstructuralquestion must retain both UNKNOWN solver histories and exactscope.',
        'unclosed_gap': 'The fixedFP-transferF-cover and general651/D3 questions remainUNKNOWN. No integer Fcover,donor assignment,PPrepair or fullD3candidate exists. A futurefeasible y/z can have atmost256 localdonor assignments; onecanonicalfailure cannot rejecttheothers. No globalrecord,newgraph,parameter,Lean ormethodclaim.',
        'positive_guarantees': [
            'Historical original1170binary/1302rows/90480nnz sole20secondUNKNOWN is preserved verbatim in historical_original_1170_record_before_structural_projection_20261102.',
            'All8385unorderedactualstarPpairs were visited;65sametwinpairs retained. C/Dpackets were extracted fromcachedoldcovercoefficients without source/A2/A3 ornewBFS.',
            'Class0/1/2capacity is a valid upperbound; its decreasingmarginal top6 optimization is exact for that bound,notactualglobalcover. Allpairs pass and the firstactualunion337<U366.',
            'Everyclass isK8,2: sumy<=2 and sumz<=sumy permit exactinteger donor reconstruction. Actual130starPcolumns remain separate; twinDcolumns differ.',
            'The new650variablemodel got its own single18secondwindow and noincumbent; compression neither proves speedup norinfeasibility. It doesnotresume theoldsolver.',
            'ExistingPPedges may remain withdegree9. Downstreamdonor/pairing/newroot/oldold stages were neverentered. Singlecanonicaldonorfailure wouldnotcloseotherassignments.'
        ]
    })
    metrics = raw['other_metrics']
    metrics['historical_original_1170_record_before_structural_projection_20261102'] = historical
    metrics.update({
        'model_binary_variables': 650, 'model_rows': 652, 'model_nonzeros': 50440,
        'current_model_F_variables': 520, 'current_model_starP_variables': 130,
        'solver_time_limit_seconds': 18, 'solver_calls': 2,
        'current_projection_solver_calls': 1, 'old_solver_resumed': False,
        'solver_actual_status': 1, 'solver_message': returned['message'],
        'solver_incumbent': None, 'solver_returned_infeasible': False,
        'certified_infeasibility': False, 'solver_CPU_seconds': projected['solver_CPU'],
        'wholecase_CPU_seconds': 42.416193092, 'all_processes_terminal': True,
        'prediction_status': 'CAPACITY_UPPER_PASS_SUPPORTED; ACTUAL_F_COVER_EXISTENCE_UNRESOLVED',
        'capacity_pairs_checked': 8385, 'capacity_upper_pass': 8385,
        'capacity_upper_fail': 0, 'capacity_minimum_surplus': 46,
        'C_f_uniform_packet_size': 72, 'D_p_uniform_packet_size': 86,
        'twin_D_equal_pairs': 0,
        'first_capacity_witness': {'starP': [0, 73], 'U': 366, 'upper': 449, 'actual_residual_union': 337, 'missing': 29, 'not_a_candidate': True},
        'current_integer_projection_equivalent_to_old_F_cover_only': True,
        'maximum_safe_donor_assignment_bound_per_yz': 256,
        'single_canonical_donor_failure_not_full_yz_exclusion': True,
        'structural_and_projected_terminal_20261102': root,
        'new_source_A2_A3_BFS_graph_Lean_ARIS': 0,
        'no_third_solve_or_seed': True
    })
    evidence = [d / 'STRUCTURAL_AND_PROJECTED_ROOT.json', d / 'STRUCTURAL_AND_PROJECTED_NOTE.md',
                d / 'NEXT_STRUCTURAL_READ_GATE.md', d / 'NEXT_STRUCTURAL_READ_GATE.json',
                d / 'PROJECTED_F_COVER_EQUIVALENCE.md']
    for sub, names in [('twin_class_packet_capacity_gate', ['PRED.md', 'run_once.py', 'run.cpp', 'RESULT.json', 'TERMINAL.json', 'FIRST_CAPACITY_PASS_WITNESS.json', 'PAPER_SCOPE_REVIEW.md']),
                       ('projected_F_cover_once', ['PRED.md', 'run_once.py', 'MODEL.json', 'RESULT.json', 'TERMINAL.json', 'SOLVER_RETURN.json'])]:
        evidence += [d / sub / name for name in names]
    assert all(path.exists() for path in evidence)
    raw['evidence_paths'] = list(dict.fromkeys(raw['evidence_paths'] + [relative(path) for path in evidence]))
    row, rowfile = write_node(raw, prefix)
    ledger['rows'][pos] = row
    persist(ledger, rowfile, now)
    node = 'experiments/' + slug + '.md'
    summary = f'''\n\n{marker}
### {now} actual650原节点：完整容量门未排，精确整数投影仍UNKNOWN

旧1170/1302/90480单20秒UNKNOWN完整保历史。新8385个实际star-P pair全部upper-pass、0fail、min surplus46；Cf72/Dp86，65对twins的D全不同。首P0/73：U366、T449、实际八包并337，漏29；上界过松，既不是F-cover对象，也不能排F-cover。

新650binary/652rows/50440nnz为旧F-cover的精确整数投影，独立一次18秒窗口仍status1/primalNone；未恢复donor、0/15配对、0候选/BFS。相同y/z最多256donor指派，一个canonical失败不排其它；旧PP边的degree9分支合法。最终42.416193092/45，全STOP，不第三solve/seed，不称压缩必更快或无解。456→456/add0，153/43/47与所有其它455rows/人工top保持。

[原位650节点]({node})；[root终态](../{relative(d / 'STRUCTURAL_AND_PROJECTED_ROOT.json')})；[纸面scope](../{relative(d / 'twin_class_packet_capacity_gate/PAPER_SCOPE_REVIEW.md')})。

'''
    update_pages(old, human, summary, 0)
    (W / 'DDP_METHOD_LEDGER.md').write_text(md_before + summary.replace('### ', '## ', 1))
    after = load(LEDGER)
    assert after['record_count'] == len(after['rows']) == 456
    assert all(after['rows'][i] == before['rows'][i] for i in range(456) if i != pos)
    assert [r['id'] for r in after['rows']] == [r['id'] for r in before['rows']]
    unchanged_top(before, after)
    assert row['source_record']['other_metrics']['historical_original_1170_record_before_structural_projection_20261102'] == historical
    receipt = {
        'status': 'PASS_EXISTING650_NODE_CAPACITY_AND_PROJECTED_UNKNOWN_TERMINAL_UPSERT',
        'updated_UTC': now, 'records_before': 456, 'records_after': 456, 'records_added': 0,
        'updated_id': slug, 'canonical_node': 'research-wiki/' + node, 'row_path': relative(rowfile),
        'old1170_20second_UNKNOWN_record_preserved_exact': True,
        'capacity_actual': {'pairs': 8385, 'upperpass': 8385, 'upperfail': 0, 'minsurplus': 46, 'first_U_T_actual': [366, 449, 337], 'Cf_size': 72, 'Dp_size': 86, 'twinD_equal': 0},
        'projection': {'variables': 650, 'rows': 652, 'nnz': 50440, 'window': 18, 'solver_CPU': projected['solver_CPU'], 'raw_status': 1, 'incumbent': None, 'integer_equivalent_F_cover_only': True},
        'final_samecase_CPU': 42.416193092, 'case_cap': 45, 'whole_rule': 'UNKNOWN',
        'Fcover_donor_pairing_graph_BFS': [0, 0, 0, 0, 0],
        'other455rows_preserved_exact': True, 'row_order_preserved': True,
        'human_top_blocks_preserved_exact': {name: True for name in FILES},
        'index_experiments_before': old_index, 'index_experiments_after': old_index,
        'graph_parameter_Lean_method_increments': [0, 0, 0, 0],
        'graph_parameter_Lean_snapshot_preserved': [153, 43, 47],
        'full_rebuild_reimport': False, 'root_STATE_ROUND_pages_recovery_modified': False,
        'new_math_solver_BFS_field_Lean_ARIS': 0, 'third_solve_prohibited': True,
        'sync_CPU_seconds': time.process_time() - started,
        'modified_outputs': ['research-wiki/' + node, 'research-wiki/DDP_METHOD_LEDGER.json', 'research-wiki/DDP_METHOD_LEDGER.md'] + ['research-wiki/' + name for name in FILES] + [relative(rowfile)],
        'stop': True
    }
    path = S / (prefix + '_RECEIPT.json')
    path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'receipt': relative(path), 'before': 456, 'after': 456, 'add': 0, 'CPU': receipt['sync_CPU_seconds']}, ensure_ascii=False), flush=True)


def d4_binary_add():
    started = time.process_time()
    now = stamp()
    prefix = 'D4_BINARY_PAIR_AND_CROSS_CHART_TERMINALS_20261102'
    marker = '<!-- ' + prefix + ' -->'
    slug = 'ddp-d4-c192-two-binary-inverse-charts-and-cross-packet-repair3072-20261102'
    parent = STAGE / 'retained_edge_transfer/published_d15_15552_D4_source_gate'
    d = parent / 'binary_cross_coupled3072'
    root = load(d / 'ROOT_DISPOSITION.json')
    assert root['case_CPU'] == 1.233294418 and root['case_cap'] == 10
    assert root['allpointgates_complete'] and not root['graph_generated']
    assert root['actual_bar'] == [0, 3, 4, 1, 2]
    assert root['baseline_chart']['same_fibre_roots_complete'] == root['cross_chart']['same_fibre_roots_complete'] == 192
    assert root['baseline_chart']['source_fibre_all16_counts'] == [8] * 16
    assert set(root['cross_chart']['new_first_bad']['whole_fibre_source_counts']) == {12, 14}
    ledger = load(LEDGER)
    assert ledger['record_count'] == len(ledger['rows']) == 456
    assert not any(row['id'] == slug or '/binary_cross_coupled3072/' in json.dumps(row, ensure_ascii=False) for row in ledger['rows'])
    before = copy.deepcopy(ledger)
    old, human, old_index = page_snapshot(marker)
    md_before = (W / 'DDP_METHOD_LEDGER.md').read_text()
    assert marker not in md_before
    evidence = [d / 'ROOT_DISPOSITION.json', d / 'NOTE.md']
    for sub, names in [
        ('binary_identity_chart3072', ['READ_GATE.md', 'READ_GATE.json']),
        ('binary_pair_swaps3072', ['PRED.md', 'run_once.py', 'RESULT.json', 'TERMINAL.json', 'FIRST_BAD_PACKET.json']),
        ('binary_cross_coupled3072', ['PRED.md', 'run_once.py', 'RESULT.json', 'TERMINAL.json', 'FIRST_BAD_PACKET.json', 'PAPER_INTERFACE.md']),
        ('cap15_arbitrary_pin_extension15553', ['READ_GATE.md'])
    ]:
        evidence += [parent / sub / name for name in names]
    assert all(path.exists() for path in evidence)
    raw = {
        'id': slug,
        'title': 'D4 C192二元受控chart：同层全16，局部跨组8→16但其它pair仍漏，两个固定chart NO',
        'family': 'Controlled binary affine route packets on actual192 typed controller',
        'idea_family': 'idea:ddp-open-parameter-construction-20261026',
        'date': '2026-11-02', 'wiki_verdict': 'partial',
        'record_type': 'controlled_binary_F2_four_chart_route_union_fixed_family_exclusions',
        'target_Delta': 10, 'target_D': 4, 'savedL': 2556,
        'baseline_date': 'Inherited current-main(10,4)=2556; no new primary query or record claim in this sync',
        'n': {'actual': None, 'hypothetical': 3072},
        'actual_graph_Delta': None, 'actual_D': None, 'ordinary_bad_unordered_pairs': None,
        'ordinary_bad_target_D': 4, 'new_lower_bound': False,
        'actual_D_scope': 'No complete3072literalgraphorgraphBFS. Two fixed inverse-compatibleF2^4charts were checked by actualordinarytypedwordimageunions0..4,all192controllers/all16sourcefibrecoordinates for self-fibres,and at leastonecrossfailurepercontrollerroot. Samefibrecoverpositive; crossD4failsbothfixedcharts.',
        'outcome_class': root['status'],
        'scope': 'ActualC192 typed5porttransitionJSON with bar[0,3,4,1,2],zeroaffineconstants,192xF2^4. Identitybaselinepaperonly: five distinctcircuits withallI violate realreversecontract; pairingidentitynoises leaves span<=3/disconnected. Thetwoexplicitnonidentitycolumnmatrixcharts inroot each have completeordinary<=4route checks asstated. Onlythesefixedcharts areNO,notallbinarymaps/general3072/(10,4). Oldcap15 arbitraryfreepin MILP/SATUNKNOWN inherited without rerun,newentry or changedverdict. No completegraph produced.',
        'distance_text': '真实bar[0,3,4,1,2]阻止五distinctnoise/allI的误设；合法pairedidentity零offset只span<=3，不连通。第一chart M0=I，M1/3交换e1/e2、M2/4交换e3/e4，v=[15,1,4,2,8]。两return的五circuit支持samefibre<=4，实际全部192×16self均16；但每controllerroot有cross失败。首0→1仅2022/4020，两image嵌套8。依据此缺口改唯一M0 columns[4,7,1,13]，原packet8→16支持且self全16保留，却另0→3的234/0234/4323只并12或14；x0首漏y9。两个各781ordinarywords含backtracks，逐全部16sourcecoords，0完整图/BFS/solver/Lean/ARIS。最终1.233294418/10，停止第三matrix/field。',
        'lesson_and_restart_condition': 'Completed true reverse and fivecircuit returns can cover the self-fibre while cross-controllertransport stillhasinvariantspaces/cosetgaps. A concreteM0 repair fixes the targeted8-to16packet without making a globalD4construction: anotherpairmisses12/14. Keepthislocalpositive distinctfromglobalgraphsuccess and stopthisfixedchartchain without thirdmatrix/field. Theoldcap15UNKNOWN isnotnewnumerics or a familyNO.',
        'restart_condition': 'STOP twoexplicitbinarycharts and identitybaseline. No thirdmatrix/field or automaticF2/Fq/controllerladder. Only a separatelyauthorized materiallydifferentquestion outsidefixedchartscope canrestart.',
        'unclosed_gap': 'Other inverse-compatiblebinary maps,offsetrules,controllers and general(10,4)/3072 remainunexcluded. Oldcap15sourceextension remainsUNKNOWN. No fulltargetgraph,actualgraphD4,newlowerbound,parameter,Lean,methodorpriorityclaim. NewsmallD4sourcereadgates are notpartofthisnode.',
        'positive_guarantees': [
            'Use actualtypedtransitionorder,not sortedACTUAL_CONTROLLER_TARGETSneighborlists; actualreverseportbar is[0,3,4,1,2].',
            'Both explicitcharts satisfy therealreversecontract. All192x16self-fibreimageunions cover16,not merelysourcex0.',
            'All781ordinarywords0..4 include shortwords andcontrollerbacktracks; full-labelholdingsteps maycontract,not samecontroller/differentfibresteps.',
            'Thefirstchartbadpacket2022/4020 is nested8 for all16sourcecoordinates; thecrosscoupledM0fixesit to16 but the new0to3packet stillgives12/14.',
            'Oldcap15arbitraryfreepinMILP/SATUNKNOWN is inheritedonly. No oldF3field,sourceD4validation,oldR3,BFS,solver,Lean orARIS rerun.',
            'ThetwofixedchartNO is completeatitsactualroutegate level; itdoesnotexcludeallF2^4charts or createa graph/methodcount.'
        ],
        'other_metrics': {
            'new_graphs': 0, 'new_parameter_pairs': 0, 'new_Lean_instances': 0, 'new_independent_method_claims': 0,
            'single_aggregate_research_record': True,
            'hypothetical_target': [10, 4, 3072], 'base_controller_order': 192, 'fibre_size': 16,
            'actual_bar': [0, 3, 4, 1, 2],
            'old_cap15_unrestricted_extension_status': 'MILP_AND_SAT_UNKNOWN_INHERITED_ONLY',
            'old_cap15_not_rerun_or_new_record': True,
            'identity_baseline_five_distinct_noises_illegal': True,
            'legal_paired_identity_zerooffset_span_atmost': 3,
            'legal_paired_identity_zerooffset_disconnected': True,
            'baseline_chart': root['baseline_chart'], 'cross_chart': root['cross_chart'],
            'same_fibre_roots_eachchart': 192, 'source_fibre_coordinates_eachroot': 16,
            'all_same_fibre_counts': 16, 'cross_root_failures_eachchart': 192,
            'ordinary_words_length0to4_eachchart': 781,
            'samefibre_prediction_supported': True, 'targeted_crosspacket_8to16_supported': True,
            'wholeD4_prediction_refuted_for_two_fixedcharts': True,
            'general_binary_chart_family_NO': False,
            'actual_native_CPU': root['actual_native_total'], 'wholecase_CPU': 1.233294418, 'case_cap': 10,
            'full_target_graph_generated': False, 'source_F3_oldR3_fullgraphBFS_Lean_ARIS_solver': 0,
            'new_small_source_readgates_included': False, 'all_stages_terminal': True,
            'same_Goal': 'ACTIVE', 'old_N8_n61': 'PAUSED'
        },
        'evidence_paths': [relative(path) for path in evidence]
    }
    row, rowfile = write_node(raw, prefix)
    ledger['rows'].append(row)
    ledger['record_count'] = 457
    persist(ledger, rowfile, now)
    node = 'experiments/' + slug + '.md'
    summary = f'''\n\n{marker}
### {now} D4 C192二元受控路线：同层覆盖与跨组缺口分开记录

旧cap15任意freepin补点MILP/SAT UNKNOWN仅继承，未重跑。真实bar[0,3,4,1,2]下五distinctnoise/allI不合法，合法pairedidentity零offset方向span≤3而不连通。两个新固定nonidentityF2⁴chart实际全部192×16self-fibre都覆盖16，但每controllerroot均有cross失败。

第一pair-swaps chart的0→1 packet2022/4020嵌套8；跨组M0修到16、samefibre保满，另0→3的234/0234/4323仍只并12/14。局部修好不当整体构造。两个各781ordinarywords0..4含backtracks，逐16sourcecoords；仅两个固定chart NO，一般binarymaps/(10,4)/3072未排。最终1.233294418/10，停止第三matrix/field，0完整图/BFS/Lean/ARIS/solver。

456→457仅一个聚合研究节点，不是图或独立方法。图/参数/Lean153/43/47与所有旧456rows、人工top保留；新小D4源readgates不混入。[canonical节点]({node})；[root终态](../{relative(d / 'ROOT_DISPOSITION.json')})。

'''
    update_pages(old, human, summary, 1)
    (W / 'DDP_METHOD_LEDGER.md').write_text(md_before + summary.replace('### ', '## ', 1))
    after = load(LEDGER)
    assert after['record_count'] == len(after['rows']) == 457
    assert after['rows'][:-1] == before['rows']
    unchanged_top(before, after)
    receipt = {
        'status': 'PASS_ONE_D4_BINARY_PAIR_AND_CROSS_CHART_AGGREGATE_TERMINAL_NODE',
        'updated_UTC': now, 'records_before': 456, 'records_after': 457, 'records_added': 1,
        'new_experiment_id': slug, 'canonical_node': 'research-wiki/' + node, 'row_path': relative(rowfile),
        'actual_bar': [0, 3, 4, 1, 2], 'identity_baseline': 'illegal_distinct_or_legal_paired_span3_disconnected',
        'old_cap15_MILP_SAT_UNKNOWN_inherited_only_not_new_count': True,
        'two_fixed_chart_samefibre_each': {'controllers': 192, 'sourcecoords': 16, 'covered': 16},
        'first_cross_packet': {'pair': [0, 1], 'words': ['2022', '4020'], 'old_nested': 8, 'repaired': 16},
        'repaired_chart_new_bad_pair': {'pair': [0, 3], 'counts': [12, 14]},
        'local_success_not_global_construction': True, 'NO_only_two_fixed_charts_not_all_binary': True,
        'final_case_CPU': 1.233294418, 'case_cap': 10, 'no_third_matrix_field': True,
        'full_target_graph_BFS_Lean_ARIS_solver': 0,
        'other456rows_preserved_exact': True, 'row_order_preserved': True,
        'human_top_blocks_preserved_exact': {name: True for name in FILES},
        'index_experiments_before': old_index, 'index_experiments_after': old_index + 1,
        'graph_parameter_Lean_method_increments': [0, 0, 0, 0],
        'graph_parameter_Lean_snapshot_preserved': [153, 43, 47],
        'full_rebuild_reimport': False, 'root_STATE_ROUND_pages_recovery_modified': False,
        'new_small_source_readgates_included': False, 'new_math_solver_BFS_field_Lean_ARIS': 0,
        'sync_CPU_seconds': time.process_time() - started,
        'modified_outputs': ['research-wiki/' + node, 'research-wiki/DDP_METHOD_LEDGER.json', 'research-wiki/DDP_METHOD_LEDGER.md'] + ['research-wiki/' + name for name in FILES] + [relative(rowfile)],
        'stop': True
    }
    path = S / (prefix + '_RECEIPT.json')
    path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'receipt': relative(path), 'before': 456, 'after': 457, 'add': 1, 'CPU': receipt['sync_CPU_seconds']}, ensure_ascii=False), flush=True)


if __name__ == '__main__':
    source650_update()
    d4_binary_add()

"""Root dispositions plus one small-D4 cohort Wiki node; no mathematics runs."""
from pathlib import Path
import copy
import json
import runpy
import time

ROOT = Path(__file__).resolve().parents[4]
S = Path(__file__).resolve().parent
STAGE = ROOT / 'research/ddp/two_successful_methods_20261101'
W = ROOT / 'research-wiki'
P252 = STAGE / 'stale_record_transfer_d5D4/source252_two_cut_star253'
P104 = STAGE / 'stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b'
PREFIX = 'SMALL_D4_TWO_CUT_STAR_COHORT_TERMINAL_20261102'
SLUG = 'ddp-small-d4-rajiv252-bhakar104-cohort-two-cut-four-star-complete-no-20261102'
MARKER = '<!-- ' + PREFIX + ' -->'
start = time.process_time()
H = runpy.run_path(str(S / 'sync_source650_then_d4_binary_terminals_20261102.py'))
load, relative, stamp = H['load'], H['relative'], H['stamp']
now = stamp()
ledger = load(W / 'DDP_METHOD_LEDGER.json')
assert ledger['record_count'] == len(ledger['rows']) == 457
assert not any(row['id'] == SLUG for row in ledger['rows'])
assert not (S / (PREFIX + '_RECEIPT.json')).exists()
before = copy.deepcopy(ledger)
r252 = load(P252 / 'RESULT.json')
r104 = load(P104 / 'RESULT.json')
assert r252 == load(P252 / 'TERMINAL.json')
assert r104 == load(P104 / 'TERMINAL.json')
n252 = r252['native']
assert n252['domain_complete'] and n252['legal_pairs_checked'] == n252['domain_expected'] == 195615
assert n252['newroot_R4_pass'] == n252['candidate_oldroot_BFS'] == 0
assert n252['maximum_newroot_oldpoint_coverage'] == 222
a, b = r104['sources']
assert [a['alias'], b['alias']] == ['a_unlettered', 'b']
assert all(item['native']['domain_complete'] and item['native']['legal_pairs_checked'] == 20904 for item in [a, b])
assert [item['native']['newroot_R4_pass'] for item in [a, b]] == [16, 24]
assert [item['native']['candidate_oldroot_fail'] for item in [a, b]] == [16, 24]
assert [item['native']['candidate_oldroot_BFS'] for item in [a, b]] == [18, 27]
failures = [load(P104 / item['output_directory'] / 'FIRST_OLD_FAILURE.json') for item in [a, b]]
assert all(f['source_distance'] == 4 and f['newdistance'] == 5 for f in failures)
assert all(f['cuts'] == [[0, 8], [4, 12]] and f['one_source_route'][:2] == [0, 8] for f in failures)


def write_json(path, value):
    assert not path.exists()
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')


root252 = {
    'status': 'ROOT_ACCEPTED_COMPLETE_NO_RAJIV252_TWO_DISJOINT_CUTS_FOUR_STAR_STOP',
    'updated_UTC': now, 'target': [5, 4, 253],
    'source': 'actual Rajiv252 literal,n252/m630/all5; primary and previous sourceD4 inherited',
    'closed_scope': 'Fixed Rajiv252 literal; delete any two vertex-disjoint ORIGINAL source edges; connect all four endpoints to one new4star; no other edits. Not general253/(5,4),other sources,thirdcut,oldoldrepair or multiplehelpers.',
    'newroot_exact_lemma': 'All cutends inP imply d_(G-cuts)(P,t)=dG(P,t) by restart at the downstreamP endpoint; newrootR4 iff four sourceclosedR3supports cover all252.',
    'raw_edgepairs': 198135, 'shared_endpoint_pairs_excluded': 2520,
    'legal_pairs_checked': 195615, 'complete_domain': True,
    'newroot_R4_pass': 0, 'maximum_source_R3_P_coverage': 222,
    'candidate_oldroot_BFS': 0, 'source_depth3_newquestion_support_queries': 252,
    'source_singlepair_diagnostic_queries': 0, 'source_D4_revalidation_BFS': 0,
    'newroot_prediction_atleast_one_pass': 'REFUTED_COMPLETE_DOMAIN',
    'full_graph_hit': False, 'new_graph_parameter_Lean_method': [0, 0, 0, 0],
    'measured_batch_case_CPU': r252['case_CPU'], 'case_cap': 10,
    'CPU_accounting': 'Original RESULT/TERM CPU preserved; this root/Wiki documentation cost is recorded separately in the sync receipt,not a reset or new mathematical window.',
    'root_read': ['RESULT.json', 'TERMINAL.json', 'run.cpp', 'run_once.py', 'SOURCE_BINDING.json', '../../stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/TWO_SOURCE_SCOPE_REVIEW.md'],
    'all_processes_terminal': True, 'source_BFS_validation_field_Lean_ARIS_solver_reruns': 0,
    'stop': 'No furthercuts,seed,source replacement or fresh positive suite from this completeNO.',
    'Goal_complete': False
}
root104 = {
    'status': 'ROOT_ACCEPTED_COMPLETE_NO_BOTH_PUBLIC104_LITERALS_TWO_CUT_STAR_STOP',
    'updated_UTC': now, 'target': [4, 4, 105],
    'sources': ['Bhakar104 officialunlettered,experimentalias a', 'Bhakar104b'],
    'official_unlettered_name': '104_d4D4.txt; internal source104a.header.edges is an experiment alias,not an official104a filename',
    'source_D4_nonisomorphism': 'Primary inherited only; no new D4/nonisomorphism validation',
    'closed_scope': 'Each fixed actual104/208/all4 source separately; delete any two vertex-disjoint ORIGINAL edges,add a new4star on their four endpoints,and make no other changes. Not general105/(4,4),thirdcut,repair,multiplehelpers or another source.',
    'newroot_exact_lemma': root252['newroot_exact_lemma'].replace('252', '104'),
    'per_source_raw_pairs': 21528, 'per_source_shared_endpoint_pairs_excluded': 624,
    'per_source_legal_pairs': 20904, 'both_complete': True,
    'newroot_R4_pass_a_b': [16, 24], 'candidate_oldroot_fail_a_b': [16, 24],
    'candidate_oldroot_BFS_a_b': [18, 27],
    'source_depth3_newquestion_support_queries_a_b': [104, 104],
    'source_singlepair_diagnostic_queries_a_b': [1, 1],
    'source_D4_revalidation_BFS': 0,
    'first_failure_a_b': failures,
    'cuts_on_shown_old_route_a_b': [[[0, 8]], [[0, 8]]],
    'source_route_uniqueness_claimed': False,
    'newroot_prediction_atleast_one_pass': 'SUPPORTED_BOTH_SOURCES',
    'full_graph_prediction': 'NOT_OBTAINED; all newroot-pass candidates fail actualoldold',
    'old104c': 'Complete20904NO same architecture inherited from oldcase,not rerun or counted as newnumerics',
    'full_graph_hit': False, 'new_graph_parameter_Lean_method': [0, 0, 0, 0],
    'measured_batch_case_CPU': r104['case_CPU'], 'case_cap': 10,
    'CPU_accounting': root252['CPU_accounting'],
    'root_read': ['RESULT.json', 'TERMINAL.json', 'run_once.py', 'INPUT_BINDING_RESULT.json', 'a_unlettered_run/FIRST_OLD_FAILURE.json', 'b_run/FIRST_OLD_FAILURE.json', 'TWO_SOURCE_SCOPE_REVIEW.md', '../../../stale_record_transfer_d5D4/source252_two_cut_star253/run.cpp'],
    'all_processes_terminal': True, 'source_BFS_validation_field_Lean_ARIS_solver_reruns': 0,
    'stop': 'No thirdcut,repair,seed or fresh positive suite; old104c stays inherited.',
    'Goal_complete': False
}
write_json(P252 / 'ROOT_DISPOSITION.json', root252)
write_json(P104 / 'ROOT_DISPOSITION.json', root104)
(P252 / 'NOTE.md').write_text('''# Rajiv252两cut／四星：完整域NO

固定actual Rajiv252/630/all5源，删两条顶点不交的原边，四端点接新z；n253/m632，旧点保持5度、新点4度，不改其它边。全部cut端点均在P，最短P路线可在最后cut下游P端点重启，所以d_(G−cuts)(P,t)=dG(P,t)，source closedR3(P)恰好判新根R4。

事前至少一组P通过的预测被完整域反驳：630边的198135无序边对剔除2520共端点对，195615全部完成；四球最大覆盖仅222/252，0newroot pass，因此0candidate旧root BFS/0完整图。252次新问题深3支持不是source D4全验收，原D4继承；没有source单pair诊断。

原RESULT/TERM实测case2.151099672/10CPU保留，编译亦在原账内；本次只补root和Wiki文档，不新数学、不重置预算。共同paper见[核读说明](../../stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/TWO_SOURCE_SCOPE_REVIEW.md)。结论仅固定源/two-disjoint-originalcuts/one4star/nootheredits，不排一般253/(5,4)或repair/第三cut/其它源。全STOP，0新图/参数/Lean/独立方法。
''')
(P104 / 'NOTE.md').write_text('''# Bhakar104 unlettered(a)／b两cut／四星：新根可过、旧路线仍断

官方unlettered文件是104_d4D4.txt，a_unlettered及source104a.header.edges只是实验alias；另一个输入为104b。两者各104/208/全4度，source D4/非同构继承primary，未重验。旧104c同规则20904 NO只继承，不重跑。

两源各21528无序原边对剔除624共端点对，20904合法组完整。四端点P含全部cutends，source closedR3(P)是newroot R4精确门；a有16、b有24案通过，支持newroot预测，但全被actualcandidate旧旧距离拒绝。累计旧root普通BFS为18/27次，不是失败图数或source D4全验证。新深3支持各104次，保存反例的source单pair诊断各1次。

两首案cuts均0–8、4–12。a的0→19 source4路0–8–2–27–19，新图最短5路0–14–6–31–23–19；b的0→22 source4路0–8–16–47–22，新图最短5路0–4–60–52–14–22。展示的旧路都经过被删0–8；不是声称旧路唯一。实际新图最短5才是拒绝证据，说明newroot覆盖不继承oldold D4。

原RESULT/TERM case0.574206988/10CPU保留，通用engine编译已记在252原case，无重复编译费用。详见[TWO_SOURCE_SCOPE_REVIEW](TWO_SOURCE_SCOPE_REVIEW.md)。当前严格NO只限每个fixedliteral/two-disjoint-originalcuts/one4star/nootheredits，不排一般105/(4,4)、第三cut、repair或其它helpers。0完整命中、新图/参数/Lean/独立方法；停止，无fresh正例套件。
''')

old, human, index_before = H['page_snapshot'](MARKER)
md_before = (W / 'DDP_METHOD_LEDGER.md').read_text()
assert MARKER not in md_before
evidence = []
for directory, names in [
    (P252, ['READ_GATE.md', 'READ_GATE.json', 'PRED.md', 'run_once.py', 'run.cpp', 'SOURCE_BINDING.json', 'RESULT.json', 'TERMINAL.json', 'ROOT_DISPOSITION.json', 'NOTE.md']),
    (P104.parent, ['READ_GATE.md', 'READ_GATE.json']),
    (P104, ['READ_GATE.md', 'READ_GATE.json', 'PRED.md', 'run_once.py', 'INPUT_BINDING_RESULT.json', 'RESULT.json', 'TERMINAL.json', 'ROOT_DISPOSITION.json', 'NOTE.md', 'TWO_SOURCE_SCOPE_REVIEW.md', 'a_unlettered_run/FIRST_OLD_FAILURE.json', 'b_run/FIRST_OLD_FAILURE.json'])
]:
    evidence += [directory / name for name in names]
assert all(path.exists() for path in evidence)
raw = {
    'id': SLUG,
    'title': '小D4三literal两cut四星完整NO：Rajiv252新根全拒，Bhakar104 a/b新根过而旧旧失败',
    'family': 'Two disjoint original-edge cuts replaced by one four-spoke star',
    'idea_family': 'idea:ddp-open-parameter-construction-20261026',
    'date': '2026-11-02', 'wiki_verdict': 'no',
    'record_type': 'complete_two_cut_four_star_cohort_exclusion',
    'target_Delta': None, 'target_D': 4, 'savedL': None, 'target_is_multivalued': True,
    'baseline_date': 'Inherited primary Rajiv252/(5,4) and Bhakar104/(4,4); no new publiccomparison or recordclaim',
    'n': {'actual': None, 'hypothetical': None},
    'actual_graph_Delta': None, 'actual_D': None, 'ordinary_bad_unordered_pairs': None,
    'ordinary_bad_target_D': 4, 'new_lower_bound': False,
    'actual_D_scope': 'No legalnewtargetgraph. Exactnewroot supportgate for allfixed-source disjointcutpairs; only104a/b surviving16/24cases constructactualin-memorycandidate andrunordinaryoldrootBFS to firstfailure. Savedoldpairs source4/new5,source singlepairdiagnostic oneeach. No sourceD4allroot revalidation.',
    'outcome_class': 'ROOT_ACCEPTED_COMPLETE_NO_THREE_LITERAL_TWO_CUT_STAR_COHORT_STOP',
    'scope': 'One aggregate researchcohort,notanewmethod. For each actualRajiv252,officialBhakar104unlettered(aliasa),and104b literal independently: delete any unorderedpair ofvertex-disjoint ORIGINAL sourceedges,add onenewvertex joinedtoallfourendpoints,keepallotheredges. Complete195615/20904/20904domainsNo. Old104c same20904No inheritedonly,notrerun. No claimgeneral253/(5,4),105/(4,4),otherhosts,thirdcut,oldoldrepair,othernewneighbors ormultiplehelpers.',
    'distance_text': '两cut全端点P给d_(G−cuts)(P,t)=dG(P,t)，所以source closedR3四球并是newroot R4精确门。252：198135raw−2520共享=195615，全拒/max覆盖222，0candidateoldroots。104a/b：各21528−624=20904完整，newroot通过16/24，actualoldold全fail16/24，ordinaryoldrootBFS18/27。首a0→19与b0→22均source4→candidate5，所示旧路含cut0–8；source单pair诊断各1不算source D4验收，不称旧路唯一。旧104c20904No继承0重跑；a仅实验alias，官方raw是104_d4D4.txt。原caseCPU252=2.151099672/10、104双源=.574206988/10分别保留，无重置或重复编译计费。',
    'lesson_and_restart_condition': 'Newroot-first gate is exactbecause allcutends belongtoP,notbecause sourceD4 survivesedge deletion. The252 newrootexistence prediction is refuted completely;104a/b newrootpredictions supportedyet everyactualsurvivorfailsoldold. Preserve firstshortestdistance5witnesses toidentify theold-route obligation that a newroot coverdoesnotresolve. Stopthisexactarchitecture withoutautomaticthirdcut/repair/seed orsource ladder.',
    'restart_condition': 'STOP exactfixedsources/two-disjoint-originalcuts/one4star architecture; no freshpositiveverification andno automaticthirdcut/repair/seed. A separatelyauthorized materiallychangedrule must retainthisclosedscope.',
    'unclosed_gap': 'General(5,4)/(4,4),otherfixedsources,threecuts,oldoldrepair,multiplehelpers orotherstarneighbors remainunexcluded. No targetgraph,globalrecord,parameter,Lean orindependentmethodclaim. SourceD4 andcohortnonisomorphism are inheritedprimaryfacts,notnewchecks.',
    'positive_guarantees': [
        'Allcutends inP imply restartatlastcut downstreamendpoint,so minimumsourceP-distance isunchanged bydeletingthecuts; sourceclosedR3exactlydecidesnewrootR4.',
        'Simple-source domainchoose(m,2)minus sumchoose(deg(v),2) iscomplete; engine visits alllegalpairs withoutunprovedsymmetryreduction.',
        'Onlynewrootpass candidates areactuallyconstructed; oldroot BFS includesallnewandoldtargets andstops atfirstactualfailure,which iscompleteforrejectingthatcandidate.',
        'Source4/new5savedpairs demonstrate actualold-route damage. Showingoneoldroutecontains0–8doesnotclaimuniquegeodesic; candidateBFSdistance5 istherefutation.',
        'Source252raw and104raw areheaderlessedgelists,notmisparsedheaders. Internal104a is anexperimentaliasforofficialunlettered104_d4D4.txt.',
        'Old104ccompleteNo islinkedandnotrerun. NewsourceD4validation,field,solver,Lean,ARISandacceptedgraphincrementsarezero.'
    ],
    'variants': [
        {'label': 'Rajiv252', 'target': [5, 4, 253], 'target_Delta': 5, 'target_D': 4, 'savedL': 252, 'actual_order': None, 'domain': 195615, 'newrootpass': 0, 'max_sourceR3P': 222, 'oldrootBFS': 0, 'status': 'COMPLETE_NO'},
        {'label': 'Bhakar104 officialunlettered(aliasa)', 'target': [4, 4, 105], 'target_Delta': 4, 'target_D': 4, 'savedL': 104, 'actual_order': None, 'domain': 20904, 'newrootpass': 16, 'oldoldfail': 16, 'oldrootBFS': 18, 'status': 'COMPLETE_NO'},
        {'label': 'Bhakar104b', 'target': [4, 4, 105], 'target_Delta': 4, 'target_D': 4, 'savedL': 104, 'actual_order': None, 'domain': 20904, 'newrootpass': 24, 'oldoldfail': 24, 'oldrootBFS': 27, 'status': 'COMPLETE_NO'},
        {'label': 'Bhakar104c oldonly', 'target': [4, 4, 105], 'target_Delta': 4, 'target_D': 4, 'savedL': 104, 'domain': 20904, 'status': 'OLD_COMPLETE_NO_INHERITED_NOT_RERUN'}
    ],
    'other_metrics': {
        'new_graphs': 0, 'new_parameter_pairs': 0, 'new_Lean_instances': 0, 'new_independent_method_claims': 0,
        'single_cohort_research_record': True, 'new_actual_source_cases': 3,
        'source252': {'n': 252, 'm': 630, 'degree': 5, 'rawpairs': 198135, 'sharedpairs': 2520, 'legal': 195615, 'newrootpass': 0, 'max_sourceR3P': 222, 'oldrootBFS': 0, 'newdepth3supports': 252, 'source_singlepairdiagnostic': 0, 'caseCPU': r252['case_CPU'], 'casecap': 10},
        'source104a': {'officialraw': '104_d4D4.txt', 'experimentalias': 'a_unlettered', 'n': 104, 'm': 208, 'degree': 4, 'rawpairs': 21528, 'sharedpairs': 624, 'legal': 20904, 'newrootpass': 16, 'oldoldfail': 16, 'oldrootBFS': 18, 'newdepth3supports': 104, 'source_singlepairdiagnostic': 1, 'first_failure': failures[0]},
        'source104b': {'officialraw': '104b_d4D4.txt', 'n': 104, 'm': 208, 'degree': 4, 'rawpairs': 21528, 'sharedpairs': 624, 'legal': 20904, 'newrootpass': 24, 'oldoldfail': 24, 'oldrootBFS': 27, 'newdepth3supports': 104, 'source_singlepairdiagnostic': 1, 'first_failure': failures[1]},
        'source104ab_jointcaseCPU': r104['case_CPU'], 'source104ab_casecap': 10,
        'source104c_oldcomplete_domain': 20904, 'source104c_newrun': False,
        'source_newroot_support_query_is_not_D4validation': True,
        'oldsource_D4validation_BFS': 0, 'new_field_solver_Lean_ARIS': 0,
        'new_accepted_complete_target_graphs': 0,
        'cutroute_witnesses_not_uniquegeodesic_claims': True,
        'same_Goal': 'ACTIVE', 'old_N8_n61': 'PAUSED', 'all_processes_terminal': True
    },
    'evidence_paths': [relative(path) for path in evidence]
}
row, rowfile = H['write_node'](raw, PREFIX)
ledger['rows'].append(row)
ledger['record_count'] = 458
H['persist'](ledger, rowfile, now)
node = 'experiments/' + SLUG + '.md'
summary = f'''\n\n{MARKER}
### {now} 小D4两cut四星cohort：三个新literal域完整NO

Rajiv252：195615合法边对完整，newroot门0pass、source R3(P)最大222，0candidateoldroots。Bhakar104 officialunlettered（实验alias a）/b各20904完整；newroot通过16/24却actualoldold全fail，ordinaryoldrootBFS18/27。首旧点对source4→new5，两条保存旧路都含cut0–8；各1次source单pair诊断不是source D4验收，也不声称旧路唯一。旧104c相同20904No只继承，0重跑。

全cutends在P使d_(G−cuts)(P,t)=dG(P,t)，所以source closedR3并是newroot R4精确门，不能据此继承oldold。只关闭各fixedliteral/two-disjoint-originalcuts/one4star/nootheredits，不排一般105/253、repair、第三cut或其它源。252原case2.151099672/10、104双源.574206988/10保留，0新sourceD4/field/solver/Lean/ARIS；停止，不正例套件或扩规则。

457→458仅一个cohort研究节点，0新图/参数/Lean/独立方法，153/43/47与旧457rows/人工顶块保持。[canonical节点]({node})；[共同paper](../{relative(P104 / 'TWO_SOURCE_SCOPE_REVIEW.md')})。

'''
H['update_pages'](old, human, summary, 1)
(W / 'DDP_METHOD_LEDGER.md').write_text(md_before + summary.replace('### ', '## ', 1))
after = load(W / 'DDP_METHOD_LEDGER.json')
assert after['record_count'] == len(after['rows']) == 458
assert after['rows'][:-1] == before['rows']
H['unchanged_top'](before, after)
receipt = {
    'status': 'PASS_ROOT_DISPOSITIONS_AND_ONE_SMALL_D4_TWO_CUT_STAR_COHORT_NODE',
    'updated_UTC': now, 'records_before': 457, 'records_after': 458, 'records_added': 1,
    'new_experiment_id': SLUG, 'canonical_node': 'research-wiki/' + node, 'row_path': relative(rowfile),
    'source252': {'completelegal': 195615, 'newrootpass': 0, 'max_sourceR3P': 222, 'oldroots': 0, 'caseCPU': r252['case_CPU']},
    'source104ab': {'completelegal_each': 20904, 'newrootpass': [16, 24], 'oldoldfail': [16, 24], 'oldrootBFS': [18, 27], 'source_singlepairdiagnostics': [1, 1], 'caseCPU': r104['case_CPU']},
    'old104c20904_NO_inherited_not_rerun': True,
    'newroot_exact_setdistance_lemma_preserved': True,
    'firstsource4_to_candidate5_savedroutes_not_unique_claims': True,
    'official_unlettered_alias_preserved': True,
    'closed_scope': 'Only fixedliteral/twovertexdisjointoriginalcuts/new4star/nootheredits',
    'other457rows_preserved_exact': True, 'row_order_preserved': True,
    'human_top_blocks_preserved_exact': {name: True for name in H['FILES']},
    'index_experiments_before': index_before, 'index_experiments_after': index_before + 1,
    'graph_parameter_Lean_method_increments': [0, 0, 0, 0],
    'graph_parameter_Lean_snapshot_preserved': [153, 43, 47],
    'full_rebuild_reimport': False, 'root_STATE_ROUND_HTML_AGENTS_modified': False,
    'new_math_solver_BFS_field_Lean_ARIS': 0,
    'root_dispositions': [relative(P252 / 'ROOT_DISPOSITION.json'), relative(P104 / 'ROOT_DISPOSITION.json')],
    'notes': [relative(P252 / 'NOTE.md'), relative(P104 / 'NOTE.md')],
    'modified_outputs': [relative(P252 / 'ROOT_DISPOSITION.json'), relative(P252 / 'NOTE.md'), relative(P104 / 'ROOT_DISPOSITION.json'), relative(P104 / 'NOTE.md'), 'research-wiki/' + node, 'research-wiki/DDP_METHOD_LEDGER.json', 'research-wiki/DDP_METHOD_LEDGER.md'] + ['research-wiki/' + name for name in H['FILES']] + [relative(rowfile)],
    'root_documentation_and_sync_process_CPU_seconds': time.process_time() - start,
    'CPU_note': 'Measured documentation/sync process only; original numerical case receipts remain unchanged and no new mathematical window was run.',
    'stop': True
}
receipt_path = S / (PREFIX + '_RECEIPT.json')
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'receipt': relative(receipt_path), 'records_before': 457, 'records_after': 458, 'added': 1, 'doc_sync_CPU': receipt['root_documentation_and_sync_process_CPU_seconds']}, ensure_ascii=False), flush=True)

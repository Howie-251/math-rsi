"""Three mechanism-level deltas through the existing canonical Wiki API.

This imports no old Wiki and runs no mathematical or traffic experiment.
"""
from pathlib import Path
from datetime import datetime, timezone
import contextlib, copy, json, re, runpy, time

START = time.process_time()
R = next(p for p in Path(__file__).resolve().parents if (p / 'research-wiki').is_dir())
W = R / 'research-wiki'
S = 'research/ddp/two_successful_methods_20261101/'
OUT = R / S / 'wiki_sync'
LABEL = 'THREE_TERMINAL_SCOPES_20261101'
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def read(path):
    return json.loads((R / path).read_text())

def evidence(base, names):
    paths = [base + name for name in names]
    assert all((R / path).is_file() for path in paths)
    return paths

def row(rid, title, family, degree, diameter, baseline, target, kind, status,
        scope, distance, lesson, metrics, paths):
    return dict(id=rid, title=title, family=family,
        idea_family='idea:ddp-open-parameter-construction-20261026',
        date='2026-11-01', record_type=kind, target_Delta=degree,
        target_D=diameter, savedL=baseline,
        baseline_date='2026-11-01; previously accepted source metadata inherited',
        n=dict(actual=None, hypothetical=target), actual_graph_Delta=None,
        actual_D=None, actual_D_scope='No newly accepted mathematical graph; exact experiment scope below',
        ordinary_bad_unordered_pairs=None, ordinary_bad_target_D=diameter,
        scope=scope, outcome_class=status, new_lower_bound=False,
        distance_text=distance, lesson_and_restart_condition=lesson,
        restart_condition=lesson,
        unclosed_gap='Only the stated completed or sampled scope stops. Same Goal remains ACTIVE; no new graph or global record is claimed.',
        other_metrics=dict(new_graphs=0, new_parameter_pairs=0,
            new_Lean_instances=0, new_independent_method_claims=0, **metrics),
        evidence_paths=paths)

P = S + 'stale_record_transfer_d6D9/source_interface/shared_tau_remaining_actions_batch/'
a, at, domain = read(P + 'RESULT.json'), read(P + 'TERMINAL.json'), read(P + 'DOMAIN.json')
assert a['status'] == 'COMPLETE_NO_PRIMITIVE49_F6959_FIXED_PHASE_ALL_NORMAL_FAMILY'
assert a['new_numeric_actions_run'] == a['new_representative_domains_completed'] == 20
assert a['new_numeric_representatives_rejected'] == 139180
assert not a['remaining_uncompleted_domains'] and a['complete42_primitive_action_coverage']
assert a['old1512_andzero_inherited'] and not a['old_field_primitiveorder_or_sourceD9_rechecked']
assert at['all_processes_terminal'] and not at['running']
id6 = 'ddp-stale-d6d9-f6959-primitive49-all-normal-remaining-batch-terminal-20261101'
paths6 = evidence(P, ['PRED.md', 'DOMAIN.json', 'RESULT.json', 'TERMINAL.json',
    'NOTE.md', 'PAPER_BATCH_DOMAIN.md', 'PAPER_DOMAIN_REVIEW.md', 'run_once.py'])
paths6 += evidence(S + 'stale_record_transfer_d6D9/source_interface/shared_tau5155_pilot/',
    ['RESULT.json', 'TERMINAL.json', 'PAPER_DOMAIN.md'])
for name in ['ROOT_DISPOSITION.json', 'ROOT_TERMINAL_DISPOSITION.md', 'ROOT_DISPOSITION.md']:
    if (R / P / name).is_file():
        paths6.append(P + name)
rows = [row(id6,
    '6D9固定F6959／primitive49／phases1,36,45：20新域全NO，继承逆action后全部normal族终态',
    'semidirect Cayley shared-translation routing', 6, 9, 331387, 340991,
    'necessary_route_parameter_image_gate', a['status'],
    a['exact_scope'] + ' New numeric work is20 inverse-pair representatives,139180 new projective normal representatives; previous5155/2789 pair and fixed1512/zero controls inherited. The other21 actions use the proved inverse-action bijection, not duplicated numeric runs. No other fields, order7/1 actions, phase triples, controllers or general6D9 exclusion.',
    '原先不知道剩余40个primitive actions能否用自由translation补齐所有phase。先有β5155的phase0修复但最终全NO，再按已证明的逆action同构固定20个独立代表域；20域各6959新P1代表全部有实际缺失phase，139180案均NO、0未决、0图/BFS。连既有5155逆pair与各action旧1512和zero，严格关闭此固定F6959/exactorder49/phases1,36,45的全部normal translations。不是每代表49phase都算，也不是42次数值run。',
    'STOP this complete fixed family: no rerun of20 actions, old1512/zero, inverse duplicates, field/order/source-D9 controls or automatic field/action ladder. Otherfields/order7/order1/otherphases/general6D9 remain outside. The reason to stop is exact finite-domain closure, not unused CPU or a small bad-pair improvement.',
    dict(Moore_bound=2929687, located_baseline=331387, Moore_space=2598300,
        Moore_gap_is_not_constructibility=True, hypothetical_margin_if_legal=9604,
        field=6959, primitive_action_exact_order=49, fixed_positive_phases=[1,36,45],
        new_numeric_actions=20, new_projective_representatives_rejected=139180,
        new_numeric_inverse_pairs=domain['remaining_domains'],
        inherited_previous_complete_inverse_pair=domain['previous_complete_pair'],
        total_numerically_closed_inverse_pair_representatives=21,
        primitive_actions_closed_by_numeric_plus_paper=42,
        inverse_action_transport='Paper isomorphism r→r^-1,tau→tau*r^-9; no doubled numerical count',
        old1512_and_zero_inherited=True, complete_exact_family_exclusion=True,
        all49phases_per_representative_required=False, unresolved_domains=0,
        cumulative_charged_CPU_seconds=at['cumulative_charged_CPU_seconds'],
        CPU_budget_seconds=at['cumulative_CPU_budget_seconds'], no_timer_reset=True,
        source_field_order_BFS_Lean_solver_remote_runs=0, target_graph_BFS=0, terminal=True), paths6)]

Q = S + 'stale_record_transfer_d4D5/port_matching_core2_star365/'
b, bt = read(Q + 'RESULT.json'), read(Q + 'TERMINAL.json')
assert b['status'] == 'UNKNOWN_10000_SAMPLE_NO_HIT'
assert b['distinct_configurations_finished'] == b['rejected_newroot_R5'] == 10000
assert b['newroot_R5_passed'] == b['rejected_old_old'] == b['final_candidate_old_label_BFS_roots'] == 0
assert not b['whole_rule_exclusion'] and bt['all_processes_terminal'] and not bt['running']
id4 = 'ddp-stale-d4d5-natural364-port-matching-two-core-cuts-star365-sample-20261101'
paths4 = evidence(Q, ['PRED.md', 'RESULT.json', 'TERMINAL.json', 'NOTE.md',
    'run_once.py', 'run.cpp', 'ATTEMPTS.csv', 'MATCHING_AND_CUTS.csv'])
if (R / Q / 'PAPER_SCOPE_REVIEW.md').is_file():
    paths4.append(Q + 'PAPER_SCOPE_REVIEW.md')
if (R / Q / 'ROOT_DISPOSITION.json').is_file():
    paths4.append(Q + 'ROOT_DISPOSITION.json')
rows.append(row(id4,
    '4D5 natural364→365：28port完美匹配＋两core删边四星，10000样本全漏新根覆盖而族仍UNKNOWN',
    'source edge surgery and port matching', 4, 5, 364, 365,
    'bounded_candidate_sample', b['status'],
    'Only natural polarity364/714 (28 degree3 ports,336 degree4 core), not the separate public364/728 regular graph. Add14 old-port perfectmatching edges, delete2 disjoint old core-core edges, join newroot364 to the4 cut endpoints. One fixedseed202611010405,10000 distinct configurations. This changes old-old edges and host-edge retention, so is outside old pureappend/≤13helper strict scopes; this sample is not familyNO.',
    '预测至少一个样本让新根R5覆盖全部old364；实际10000案均在新根门失败，0案进入old-old阶段，预测在该样本中不支持。首案实际路径364–43–54–56–360–345–0长6；不能声称已观察到old-old路线损坏。目标365/730为4regular、保留712/714旧边的度数记账合法，但无完整合法D5图。',
    'STOP this one bounded matching+two-core-cut batch with its fixedseed; no automatic more samples, changedseed/cut pattern or H14. Keep the complete rule UNKNOWN, not a family exclusion. Newroot coverage is the observed bottleneck; old-old preservation remains untested here. Inherit sourceD5/portballs rather than rerunning old validation.',
    dict(Moore_bound=485, located_baseline=364, Moore_space=121,
        Moore_gap_is_not_constructibility=True, source_n=364, source_m=714,
        source_degree_histogram=b['source_degree_histogram'], target_n=365, target_m=730,
        degree_accounting_regular4=True, oldsource_edges_retained=712,
        oldsource_edges_deleted=2, added_oldport_matching_edges=14, newroot_core_edges=4,
        seed=b['seed'], distinct_configurations_finished=10000, newroot_R5_passed=0,
        rejected_newroot_R5=10000, rejected_old_old=0, final_candidate_old_label_BFS_roots=0,
        prediction_newroot_supported=False, first_newroot_failure=b['first_newroot_failure'],
        complete_rule_exclusion=False, cumulative_charged_CPU_seconds=bt['total_charged_CPU_seconds'],
        CPU_budget_seconds=bt['CPU_budget_seconds'], no_timer_reset=True,
        source_D5_BFS_portballs_field_solver_Lean_remote_runs=0, terminal=True), paths4))

E = S + 'engineering_pilot_20261101/'
e, et = read(E + 'RESULT.json'), read(E + 'TERMINAL.json')
assert e['status'] == 'BOUNDED_ENGINEERING_PILOT_COMPLETE' and et['all_processes_terminal']
assert et['traffic_route_BFS_total'] == 32 and et['old_allroot_validity_BFS'] == 0
assert e['baseline']['total_hops_of_routed_flows'] == 690
assert e['one_link_removed']['total_hops_of_routed_flows'] == 696
assert e['baseline']['peak_directed_link_unit_flow_load'] == e['one_link_removed']['peak_directed_link_unit_flow_load'] == 4
idE = 'ddp-bounded-engineering-port-budget-fixed-traffic-one-link-pilot-20261101'
pathsE = evidence(E, ['PRED.md', 'RESULT.json', 'TERMINAL.json', 'NOTE.md',
    'run_once.py', 'flow_paths.csv', 'pilot.html', 'pilot.html.txt'])
pathsE += evidence(S + 'retained_edge_transfer/engineering_pilot/', ['RESULT.json', 'REPORT.md'])
if (R / E / 'ROOT_DISPOSITION.json').is_file():
    pathsE.append(E + 'ROOT_DISPOSITION.json')
eng = row(idE,
    '有限工程pilot：16port余度16200→4554；3750图240固定流单边删除后平均2.875→2.9hop',
    'engineering port and fixed-traffic evaluation (not mathematical construction)',
    None, None, None, None, 'bounded_engineering_evaluation', e['status'],
    e['scope'] + ' A: inherited15552/final16389 degree histograms with physical16ports, each networkedge consumes2 endpoints; no large graph parse. B: acceptedF5/3750 parsedonce for16 endpoints floor(i*3750/16),240 ordered nonself unit flows, sorted-neighbor first-parent shortest paths; each directedlink capacity1 full duplex. Delete only the sample busiest undirectedlink (sum two directions,tie lex) and reroute sameflows. Prior engineering workload differs; not a graph/method or throughput/faultdiameter certificate.',
    '16port模型：15552源余16200portslots，16389终图余4554，+837switches却−11646slots，因为+12519网络边占25038端口、大于新增物理端口13392。3750固定240流baseline总hop690/均2.875/峰directedload4/共同flowrate上界1/4。仅删sample最忙(122,1171)，双向负载8：240流仍通，总hop696/均2.9/峰4/上界1/4，8路径变化、6流绕1hop、maxdetour1。预测该样本仍连通且detour≤1得到支持。',
    'STOP independent finite engineering pilot. Keep results as abstract port accounting and this fixed workload/link/router only; no industrial advantage, hardware measurement, optimal network throughput, allpair/global failure diameter, bisection, wiring or cost inference. Capacity1/L is the fixed-route common-flow upperbound under the stated link units; do not compare directly with prior1/15 ECMP demand. No new graph, parameter, Lean instance or mathematical method.',
    dict(mathematical_method_entry=False, engineering_only=True,
        inherited_sources_and_accepted_graphs=True, physical_ports_per_switch_A=16,
        port_accounting_16ports=e['port_accounting_16ports'],
        port_accounting_change=e['port_accounting_change'],
        source3750_P24_P32_inherited_server_port_slots={'24':15000,'32':45000},
        endpoints=e['workload_endpoints'], ordered_nonself_unit_flows=240,
        routing=e['routing'], link_capacity_model=e['link_capacity_model'],
        baseline={k:e['baseline'][k] for k in ['reachable_flows','unreachable_flows','total_hops_of_routed_flows','mean_hops_of_routed_flows','peak_directed_link_unit_flow_load','fixed_route_common_flow_rate_upper_bound']},
        one_link_removed={k:e['one_link_removed'][k] for k in ['reachable_flows','unreachable_flows','total_hops_of_routed_flows','mean_hops_of_routed_flows','peak_directed_link_unit_flow_load','fixed_route_common_flow_rate_upper_bound']},
        changes=e['changes'], prediction_supported=e['prediction_all_sample_flows_connected_and_max_detour_at_most1'],
        new_workload_differs_from_old_pilot=e['new_workload_differs_from_old_pilot'],
        new_traffic_graph_parses=1, source15552_final16389_graph_parses=0,
        new_traffic_route_BFS_total=32, old_allroot_validity_D3_BFS=0,
        cumulative_charged_CPU_seconds=et['cumulative_charged_CPU_seconds'], CPU_budget_seconds=5,
        industrial_advantage_claimed=False, hardware_throughput_measured=False,
        global_fault_diameter_claimed=False, terminal=True), pathsE)
eng['wiki_verdict'] = 'partial'
eng['actual_D_scope'] = 'Engineering-only fixed workload and port arithmetic; no new graph validity/diameter claim'
rows.append(eng)

# Snapshot current ledger and navigation once, then add only these three nodes.
L = read('research-wiki/DDP_METHOD_LEDGER.json')
before = L['record_count']
existing = {n['id']:n for n in L['rows']}
assert len(existing) == before
ids = [r['id'] for r in rows]
assert all(rid not in existing and not (W/'experiments'/f'{rid}.md').exists() for rid in ids)
assert not any('engineering_pilot' in p for n in existing.values() for p in n.get('evidence_paths', [])), 'Reuse a newly existing engineering node instead'
keys = ['validated_named_graph_examples','validated_named_parameter_pairs','complete_Lean_graph_instances','saved_main_table_improvement_graph_examples','saved_main_table_improvement_parameter_pairs']
counts = {k:L[k] for k in keys}
assert tuple(counts[k] for k in keys[:3]) == (152,43,46)
END = '<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101_END -->'
prefix = {}
for fn in ['index.md','query_pack.md','gap_map.md']:
    text = (W/fn).read_text()
    assert text.startswith('<!-- STALE_MAIN_MOORE_HUMAN_REVISION_20261101 -->') and END in text and LABEL not in text
    prefix[fn] = text[:text.index(END)+len(END)]
mdpath = W/'DDP_METHOD_LEDGER.md'
assert LABEL not in mdpath.read_text()
oldids = ['ddp-stale-d6d9-beta5155-free-tau-complete-inverse-action-20261101',
          'ddp-current331387-normalized-f6959-all42-embeddings-6d9-20261028']
oldtexts = {rid:(W/'experiments'/f'{rid}.md').read_text() for rid in oldids}
assert all(rid in existing and LABEL not in oldtexts[rid] for rid in oldids)
rawpath = OUT/f'{LABEL}_ROWS.json'
rawpath.write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n')
c = runpy.run_path(str(R/'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
helper = c['helper']
helper.rebuild_index = lambda *a,**k:None
helper.rebuild_query_pack = lambda *a,**k:None
norm = []
with (OUT/f'{LABEL}_NODE_CALLS.log').open('w') as log, contextlib.redirect_stdout(log):
    for r in rows:
        n = c['normalize'](r)
        n['goal']['baseline_date'] = r['baseline_date']
        c['write_node'](n)
        norm.append(n)

# Historical statements stay intact; the later closure pointer resolves old "40 open" text.
for rid, oldtext in oldtexts.items():
    (W/'experiments'/f'{rid}.md').write_text(oldtext+'\n\n<!-- '+LABEL+' -->\n## 后续完整primitive49族终态（2026-11-01，以上历史原文保留）\n\n以上旧scope仍有效；此前“remaining40 freeτ open”是本轮之前的历史状态。后续20个数值inverse-pair代表域／139180新normal代表全部NO，连既有5155逆pair与旧1512/zero，由纸面逆action同构关闭全部42primitive exactorder49 actions的完整normal族。严格限定F6959及positivephases1/36/45；不是otherfields、order7/1、otherphases或一般6D9无解。见[全族终态与停止范围]('+id6+'.md)。0新图，未重复旧控制或逆action数值计算。\n')
    update = dict(path='research-wiki/experiments/'+id6+'.md',date='2026-11-01',
        note='Later complete fixedF6959/exactorder49/phases1,36,45 allnormal familyNO supersedes historical remaining40free-tau-open state; other scopes stay outside.')
    existing[rid].setdefault('other_metrics',{}).setdefault('later_scope_updates',[]).append(update)
    existing[rid]['source_record'].setdefault('other_metrics',{}).setdefault('later_scope_updates',[]).append(copy.deepcopy(update))
for n in norm:
    existing[n['id']] = n
L.update(rows=list(existing.values()),record_count=len(existing),updated_UTC=NOW)
L['input_counts'][str(rawpath.relative_to(R))] = 3
(W/'DDP_METHOD_LEDGER.json').write_text(json.dumps(L,ensure_ascii=False,indent=2)+'\n')

def table(n):
    safe = c['safe']
    return '| ['+safe(n['title'])+'](experiments/'+n['id']+'.md) | '+safe(c['goal_text'](n))+' | '+safe(c['gap_text'](n))+' | '+safe(n['exact_scope'])+'；'+safe(n['lesson'])+'；[原始证据](../'+n['evidence_paths'][0]+') |'
md = mdpath.read_text()
needle = f'本页有{before}条记录；不以此宣称{before}种独立方法。'
assert needle in md
md = md.replace(needle,f'本页有{len(existing)}条记录；不以此宣称{len(existing)}种独立方法。',1)
md += '\n\n<!-- '+LABEL+' -->\n## '+NOW+' 三项终态：完整normal域、365改边样本、独立工程模型\n\n| 方法／实验 | 目标与对象 | 距目标的证据 | 范围、启发与证据 |\n|---|---|---|---|\n'+'\n'.join(table(n) for n in norm)+'\n\n20actions合为一个机制终态；natural364规则为单seed10000样本UNKNOWN而非族NO；engineering单独标为工程评估，不计数学方法或新图。152／43／Lean46不变；同一Goal ACTIVE，旧N8/n61暂停。继续继承最新人工15老格（14格十年以上＋1格八年）＋Moore余量选题，余量不等于可实现；以上exactscope停止，非自动开启field、seed或模板大筛。\n'
mdpath.write_text(md)
links = '；'.join('['+n['title']+'](experiments/'+n['id']+'.md)' for n in norm)
nav = '<!-- '+LABEL+' -->\n### 2026-11-01 最新终态：固定normal族NO；365样本UNKNOWN；工程pilot完成\n\n6D9新增20数值域／139180normal代表全NO；继承5155逆pair、旧1512/zero及逆action同构后，固定F6959／primitive exactorder49／positivephases1,36,45的全部normal族关闭，累计60.133230490/90CPU。仅此exactscope，otherfields/order7/1/otherphases/一般6D9不在排除内。旧“remaining40 open”段落是历史，后续指针已补。natural364/714的28port完美匹配＋两core删边＋新四星：10000案全漏newrootR5，0oldold BFS，1.537876879/20CPU；样本UNKNOWN，不能称整族NO。独立工程pilot0.322702775/5CPU：16portslots16200→4554；3750固定240流删sample最忙(122,1171)后全通、mean2.875→2.9、peakdirectedload4，上界1/4；仅固定流与抽象容量，不是工业优势／全pair fault结论。三项均terminal，不自动续算。\n\n保留人工15老格（14格十年以上＋1格八年）＋Moore余量主线；[候选与原始来源](../research/stale_record_candidates.html)。152／43／Lean46不变，0新数学方法／图／参数／Lean；同Goal ACTIVE、旧N8/n61暂停，不重启旧队列。\n\n'+links+'\n\n'
preserved = {}
for fn, pre in prefix.items():
    path = W/fn
    text = path.read_text()
    assert text.startswith(pre)
    at = len(pre)
    text = text[:at]+'\n\n'+nav+text[at:]
    if fn == 'index.md':
        match = re.search(r'^## Experiments \((\d+)\)$',text,re.M)
        assert match
        text = text[:match.start()]+f'## Experiments ({int(match[1])+3})'+text[match.end():]
        pos = text.index('\n',match.start())+1
        text = text[:pos]+''.join('- `exp:'+n['id']+'` — '+n['title']+(' [partial]\n' if n['id'] in [id4,idE] else ' [no]\n') for n in norm)+text[pos:]
    assert text[:at] == pre
    path.write_text(text)
    preserved[fn] = True
helper.append_log(str(W),LABEL+': three canonical mechanism-level nodes only;20new numerical inverse-pair domains139180normal representatives plus inherited5155/old1512/zero close only fixedF6959 primitive49 phases1,36,45 allnormal family; natural364 portmatching/twocorecut10000sampleUNKNOWN with0oldold BFS; finite engineering model separately marked engineering not mathematical method. Prior6D9 historical text retained with later-scope pointers. Human15oldcells top preserved;152/43/46 unchanged,sameGoalACTIVE,oldN8/n61paused,no automatic restarts or full import/rebuild.')
after = read('research-wiki/DDP_METHOD_LEDGER.json')
assert after['record_count'] == before+3 and {k:after[k] for k in keys} == counts
receipt = dict(status='PASS_THREE_MECHANISM_TERMINALS_MINIMAL_INCREMENTAL_WIKI_DELTA',
    updated_UTC=NOW, records_before=before, records_after=after['record_count'],records_added=3,
    new_experiment_ids=ids, numeric20actions_merged_into_one_mechanism_node=True,
    mathematical_terminal_nodes_added=2, engineering_evaluation_nodes_added=1,
    prior_standalone_engineering_node_found=False, engineering_is_mathematical_method=False,
    all42_primitive_normal_family_closed_only_fixed_scope=True,
    natural364_sample_unknown_not_family_NO=True,
    old6D9_original_text_preserved_with_later_scope_pointers=oldids,
    human_top_blocks_preserved_exact=preserved, human15oldcells_memory_preserved=True,
    full_index_query_rebuild=False, counts_unchanged=counts,
    graph_parameter_Lean_method_increments=[0,0,0,0],same_goal='ACTIVE',old_N8_n61='PAUSED',
    source_graph_field_BFS_solver_Lean_remote_hash_runs=0,
    root_STATE_REPORT_progress_HTML_frozen_modified=False,
    writes_limited_to_Wiki_and_stage_wiki_sync=True,
    changed_recovery_entries=['research-wiki/index.md','research-wiki/query_pack.md','research-wiki/gap_map.md','research-wiki/DDP_METHOD_LEDGER.md','research-wiki/DDP_METHOD_LEDGER.json'],
    CPU_seconds=time.process_time()-START,stop=True)
(OUT/f'{LABEL}_RECEIPT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(receipt,ensure_ascii=False,indent=2))

"""Persist already executed finite experiments; never launch a search or BFS."""
from pathlib import Path
import contextlib
import copy
import json
import runpy

ROOT = Path(__file__).resolve().parents[3]
WORK = Path(__file__).resolve().parent
WIKI = ROOT / 'research-wiki'
common = runpy.run_path(str(ROOT / 'research/ddp/wiki_backfill_20261027/sync_ledger.py'))
NOW = common['NOW']
base = 'research/ddp/more_graphs_20261027/'
rows = []

def row(slug, title, family, delta, diameter, baseline, directory, result, lesson,
        hypothetical=None, actual=None, actual_d=None, degree=None, metrics=None,
        kind='finite-construction-experiment', verdict='no', scope=None, paths=None):
    r = dict(id=slug, title=title, family=family, record_type=kind,
             target_Delta=delta, target_D=diameter, savedL=baseline,
             n=dict(actual=actual, hypothetical=hypothetical), actual_D=actual_d,
             actual_graph_Delta=degree, ordinary_bad_unordered_pairs=None,
             ordinary_bad_target_D=diameter,
             scope=scope or result, failure_or_result=result,
             lesson_and_restart_condition=lesson,
             unclosed_gap='Complete new graph and final Lean remain required; finite scope is not the general graph problem.',
             outcome_class=kind, wiki_verdict=verdict, other_metrics=metrics or {},
             report_paths=[base+directory+'/REPORT.md',base+directory+'/RESULT.json']+(paths or []))
    rows.append(r)
    return r

family = 'PSL2 coset transfer'
row('ddp-psl23-c3-2024-degree6-20261027', 'PSL2(F23)/C3：4661个六价轨道组合全失败', family, 6, 5, 1518,
    'd6_psl23_coset_transfer/p23_c3',
    '全部4661个G-invariant degree6无向轨道组合完成，0命中、0未试；代表根R5最少漏97。纯2024点作用，不是旧3542二轨道试算。',
    'normalizer覆盖与外部覆盖不能同时实现；停止固定作用，不沿最优97漏点样本局部微调。其它作用/稳定子仍开放。',
    hypothetical=2024, metrics=dict(evaluated=4661, hits=0, root_R5_missing_min=97, CPU_seconds=4.237507044, old3542_rerun=False),
    scope='All degree6 unions of undirected orbitals of this fixed PSL2(F23)/C3 action only.')
row('ddp-psl25-c4-1950-c6-profile-20261027', 'PSL2(F25)/C4：保持C6的78项迁移失败', family, 6, 5, 1518,
    'd6_psl23_coset_transfer/q25_c4_profile',
    '同torus12/normalizer24的源4+1+1规则全部78项完成，0命中。1950为候选作用阶数，未导出合法D5图。',
    '局部normalizer结构可以保持但全群五步覆盖失败；改C6为C3因子做受控比较，而非重复这78项。',
    hypothetical=1950, metrics=dict(evaluated=78, hits=0, CPU_seconds=0.461226825), scope='Fixed C4 action; normalized two-reflection matching choice, all78 self-paired external degree4 orbitals.')
row('ddp-psl25-c4-1950-c3-profile-20261027', 'PSL2(F25)/C4：改C3因子，修636却丢32；全78项仍失败', family, 6, 5, 1518,
    'd6_psl23_coset_transfer/q25_c4_triangles',
    '固定同一外部轨道的对照修回636个旧漏点、丢32个旧已覆盖点；normalizer仍6/6。全部78项无命中，最佳代表根漏379。',
    '覆盖互补预测部分支持，但全图预测失败。两类profile合起来穷尽固定PSL2(F25)/C4的G-invariant degree6规则；停止该作用，结论不外推任意1950点图。',
    hypothetical=1950, metrics=dict(evaluated=78, hits=0, paired_control_repaired=636, paired_control_lost=32, root_R5_missing_min=379, CPU_seconds=0.4068066),
    scope='Unique inverse-paired normalizer rotation orbital plus each78 external degree4 orbitals; together with prior row completes this fixed action.')
row('ddp-psl25-c5-1560-profile-20261027', 'PSL2(F25)/unipotent C5：60项5+1规则全失败', family, 6, 5, 1518,
    'd6_psl23_coset_transfer/q25_unipotent_c5',
    '全部60个外部五价轨道加固定normalizer matching完成，0命中，最佳代表根漏35=5个normalizer点+30个外部点。至少一项全覆盖normalizer的预测被反驳。',
    '必须同时改变normalizer与外部路线；不因只差35点自动续修、换域或换稳定子。',
    hypothetical=1560, metrics=dict(evaluated=60, hits=0, root_R5_missing_min=35, CPU_seconds=0.319778456), scope='Fixed F5-unipotent C5 action and all60 external involution H-classes only.')

family = 'H9 blocking-neighborhood extension'
row('ddp-h9-redei15-blocking-shape-20261027', 'Rédei15新覆盖形状：5固定点+5共轭对，10+s pins', family, 12, 5, 42342,
    'h9_redei15/theory',
    'f(x)=x^5的9个图点加6方向点阻塞PG2(F9)全部91条线；最小阻塞、无完整Q-line/Baer13子集。5个Frobenius固定点和5对给10+s pins。极化论证给bare-core R4覆盖。',
    '新覆盖邻域允许保住旧核心同时给extras留最多2个anchors；这是改变连接规则的数学依据。actual degree/extras仍须检查，不把局部定理作完整新图。',
    verdict='yes', kind='positive-local-theorem', metrics=dict(raw_points=15, fixed_points=5, conjugate_pairs=5, fully_folded_pins=10, lines_blocked=91),
    paths=[base+'h9_redei15/SHAPE.json', base+'h9_redei15/theory/PROOF.md', 'reviews/ddp/redei15_20261027.DISPOSITION.md'])
rows[-1]['report_paths'][0] = base+'h9_redei15/theory/PROOF.md'
row('ddp-h9-redei15-fixed-pool-20261027', 'Rédei15固定702×1120池：N12有85项，N11为空', family, 12, 5, 42342,
    'h9_redei15/pool',
    '786240个placement一次完成，N12得到85个不同degree合法邻域，N11得到0。未在此阶段算R4或anchors。',
    'N12存在可执行的覆盖对象，立即交生产；N11同一degree池空则停止。仅702个F3射影轨道，不外推全部F9变换。',
    metrics=dict(orbit=702, planes=1120, placements=786240, pool12=85, pool11=0, CPU_seconds=0.209619),
    scope='Fixed PGL3(F3) orbit and1120 F3-defined singular planes on actual42398/37631 bases only.')
row('ddp-h9-redei15-new-four-20261027', 'Rédei15已产四图：42399–42402，固定池终态', family, 12, 5, 42342,
    'h9_redei15/production/continuation',
    '85项once-policy全部终态：4成功、23当时degree阻断、58当时coverage失败，0UNKNOWN。四图完整新增degree与actual-current R4遗漏均0；最强42402/m245937/max12/D5。',
    '新阻塞规则预测得到支持，已交付四个完整阶数。停止已完成固定池；早期失败属于当时基图，不声称最终42402静态不可扩张。当前数学主力迁往其他参数。',
    actual=42402, actual_d=5, degree=12, verdict='yes', kind='mathematically-verified-new-lower-bound-subfamily',
    metrics=dict(new_lower_bound_mathematically_verified=True, example_orders=list(range(42399,42403)), example_count=4, strongest_n=42402, strongest_m=245937, accepted=4, degree_blocked=23, coverage_fail=58, UNKNOWN=0, full_Lean_instances=0, review_status='ACCEPTED_WITH_ARITHMETIC_CORRECTION', actual_reviewer_model='gemini-3.8-flash-high'),
    paths=[base+'h9_redei15/production/accepted_sequence.json', base+'h9_redei15/production/independent_newroot42399.json', 'reviews/ddp/redei15_20261027.DISPOSITION.md'])

family = 'Natural H3 polarity port extension'
row('ddp-h3-364-single-port-barrier-20261027', '自然H3/364源：28个独立端口要求排除单点增广', family, 4, 5, 364,
    'd4_D5_polarity_extensions/source_and_single',
    '源364点714边，有28个degree3 ports；R4(p)与port集仅交{p}，28个R2球划分全部364点。最小port R4 cover恰28，故≤4 pins的新点不可能；均匀排除20475项，实际枚举0。',
    '端口彼此距离5决定失败；不能靠同一host换4个pins修复。与全4regular的Delorme364源不同，不混用源。',
    hypothetical=365, metrics=dict(source_m=714, ports=28, exact_port_cover=28, combinations_excluded=20475, combinations_evaluated=0, CPU_seconds=0.039194522))
row('ddp-h3-364-two-root-port-barrier-20261027', '自然H3两新根：互助仅盖6/28端口，均匀排除', family, 4, 5, 364,
    'd4_D5_polarity_extensions/two_root',
    '相邻新根各接3个不同旧ports，R4(A)∪R3(B)在port集仅A∪B，必漏22；3767400对全部由同一障碍排除，实际枚举/编译/BFS均0。假设族D恰6，无实际新图。',
    '双新点互助不能越过旧port间距；停止小根组合枚举，改整体helper必要结构研究。',
    hypothetical=366, metrics=dict(unordered_pairs_excluded=3767400, pairs_evaluated=0, missing_ports_per_root=22, CPU_seconds=0.001109331))
row('ddp-h3-364-helper-minimum13-20261027', '自然H3固定host：所有合法helper增广至少13新点', family, 4, 5, 364,
    'd4_D5_polarity_extensions',
    '保留旧边且不加old-old边时，D5迫使全部28 ports接新点，helper诱导图连通；4k≥28+2(k−1)推出k≥13，故1..12点增广全不可能。k13须tree、全4regular，可能阶数377未构造/未排除。',
    '跳过3..12个helper的机械试算；377需要整体路由设计，当前降低优先级，不据此关闭(4,5)。',
    hypothetical=377, kind='positive-local-theorem', verdict='yes', metrics=dict(minimum_helpers=13, first_possible_order=377, new_experiments=0),
    scope='Only this fixed364/714 host, old edges retained and no new old-old edges.', paths=[base+'d4_D5_polarity_extensions/MULTI_VERTEX_PORT_BARRIER.md'])
rows[-1]['report_paths'][0] = base+'d4_D5_polarity_extensions/MULTI_VERTEX_PORT_BARRIER.md'

family = 'H9 degree13 transfer'
row('ddp-h9-d13-51417-source-binding-20261027', '公开(13,5)51417图绑定：50554核心+863 extras', family, 13, 5, 51417,
    'd13_D5_h9_transfer',
    '源51417/m324451/max13，核心50554的33397类商图与F逐边一致；current核心与旧core有2706边替换，不能假设旧raw orientation。每个类块complete或perfect matching，故可lift所有F短路，whole-class阻塞邻域保证核心R4。',
    '稳定B15可不依赖pair orientation迁移；raw非稳定集合须先恢复真正映射或取whole-class closure。实际13248点有degree余量，但不推出邻域合法。',
    actual=51417, actual_d=None, degree=13, kind='source-recovery', verdict='partial', metrics=dict(core_n=50554, extras=863, free_vertices=13248, free_core_vertices=12946, free_extra_vertices=302, removed_core_edges=2706, added_core_edges=2706),
    scope='Actual published51417 source binding and stable/whole-class core coverage only; sourceD5 inherited publicly, not allsource reverified.', paths=[base+'d13_D5_h9_transfer/CORE_COVER_TRANSFER.md',base+'d13_D5_h9_transfer/READY_FOR_POOL.json'])
row('ddp-h9-d13-redei702-pool-empty-20261027', '(13,5)稳定Rédei迁移：786240项degree合法池为空', family, 13, 5, 51417,
    'd13_D5_h9_transfer/redei_pool',
    '现成702轨道×1120planes完整检查，raw degree合法0、不同pinset0；至少一项合法预测被反驳。没有BFS/anchor/新图。364个F3点中仍108个free，失败不能归因为所有F3点满度。',
    '停止同一固定池；下一规则改非稳定Baer13或whole-class closure以避开固定五个F3点的分布，先绑定映射。',
    hypothetical=51418, metrics=dict(placements=786240, distinct_feasible_pinsets=0, prediction_verdict='REFUTED', CPU_seconds=0.210511479, BFS=0, anchor_tests=0),
    scope='Only702 F3-projectivity Rédei15 shapes ×1120 saved F3-defined singular planes on current51417 source.')

row('ddp-h9-d13-raw-gauge-obstruction-20261027', '(13,5)旧raw映射恢复失败：pairflip不改变边块大小', family, 13, 5, 51417,
    'd13_D5_h9_transfer/raw_map_recovery',
    '完整166425个F边块比较：1345个旧4→当前2、1345个旧2→当前4；另8个同计数matching变化。最短反例Fedge26—15837从K2,2变matching，因此任何类内pairflip都不能恢复旧raw同态。',
    '明确停止虚构旧raw orientation。whole-class closure仍可用已证F短路lift保证core覆盖，属于不同规则；不排任意重标或其它raw实现。',
    kind='positive-local-obstruction', verdict='yes', metrics=dict(blocks_checked=166425, complete_to_matching=1345, matching_to_complete=1345, matching_parity_changed=8),
    scope='Class-preserving pairflip gauge of the fixed oldcore onto the actual51417 currentcore only.')
row('ddp-h9-d13-baer-wholeclass-empty-20261027', '(13,5)Baer whole-class迁移：8467200项card预算排空', family, 13, 5, 51417,
    'd13_D5_h9_transfer/baer13_transfer',
    '7560个Baer13形状×1120个F3-defined平面完整一次检查，1740次whole-class closure全部pins有度数余量，但card21/22/26分别814/158/768，均超过13；合法池0，事前存在预测被反驳。CPU0.98348703，0BFS/R4/anchors。',
    '停止这个固定source/whole-class规则，不因有1740项degree通过而继续不可装入13的邻域。转其它参数；非F3-defined平面、其它blocking规则未排。',
    hypothetical=51418, metrics=dict(placements=8467200, allpins_degree_legal_occurrences=1740, card_histogram={'21':814,'22':158,'26':768}, feasible_pinsets=0, CPU_seconds=0.98348703, prediction_verdict='REFUTED', BFS=0),
    scope='All7560 Baer13 coefficient sets in1120 saved F3-defined planes, whole currentFrobenius-class closure, on actual51417 source only.')

ledger_path = WIKI/'DDP_METHOD_LEDGER.json'
ledger = json.loads(ledger_path.read_text())
existing = {r['id']:r for r in ledger['rows']}
old = existing['ddp-h9-qline-d12-family-42377']
full = copy.deepcopy(old['source_record'])
full.update(title='完整新图族：(12,5)42343–42402，共60个阶数', family='H9 blocking-neighborhood extension',
            n=dict(actual=42402,hypothetical=None),
            scope='Literal extension sequence from public42342; every integer42343..42402 is a fullD5 graph. Includes Q-line, Baer13 and Rédei15 neighborhoods.',
            failure_or_result='最强42402/m245937/max12/D5，共60阶数。新Rédei15机制产生最后4图；首步42399 fresh edge-file new-root检查通过，其余完整currentR4归纳，无重复old全BFS。')
full['other_metrics'].update(example_orders=list(range(42343,42403)),example_count=60,strongest_n=42402,strongest_m=245937,improvement=60,latest_examples_review_executed=True,latest_review_scope='New Redei15 theorem and four extensions; accepted with85-count arithmetic correction',prior_review_scope_examples=38)
full['variants']=[dict(order=n,D5_by_complete_induction=True,not_independent_method=True,allsource_BFS_here=n in (42343,42345,42377)) for n in range(42343,42403)]
full['report_paths'] += [base+'h9_redei15/production/accepted_sequence.json',base+'h9_redei15/theory/PROOF.md',base+'h9_redei15/production/independent_newroot42399.json','reviews/ddp/redei15_20261027.DISPOSITION.md']
rows.append(full)
(WORK/'redei_and_otherparams_rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
with (WORK/'redei_otherparams_wiki_sync.log').open('w') as log, contextlib.redirect_stdout(log):
    for raw in rows:
        normalized=common['normalize'](raw)
        assert normalized['evidence_paths'], normalized['id']
        common['write_node'](normalized)
        existing[normalized['id']]=normalized
allrows=list(existing.values())
examples={(r['goal']['Delta'],r['goal']['D'],n) for r in allrows if r['other_metrics'].get('new_lower_bound_mathematically_verified') for n in r['other_metrics'].get('example_orders',[])}
assert len(examples)==63, len(examples)
ledger.update(updated_UTC=NOW,record_count=len(allrows),rows=allrows,new_lower_bounds=2,mathematical_new_lower_bounds=2,mathematically_improved_parameter_pairs=2,valid_new_graph_examples=len(examples),formally_completed_new_lower_bounds=0)
ledger['input_counts']['../more_graphs_20261027/redei_and_otherparams_rows.json']=len(rows)
ledger_path.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n')
page=common['render'](allrows)
assert not common['capture'].screen(page)
(WIKI/'DDP_METHOD_LEDGER.md').write_text(page)
with (WORK/'redei_otherparams_wiki_sync.log').open('a') as log, contextlib.redirect_stdout(log):
    common['helper'].rebuild_index(str(WIKI))
    common['helper'].rebuild_query_pack(str(WIKI))
result=dict(updated_UTC=NOW,record_count=len(allrows),records_written=len(rows),valid_new_graph_examples=len(examples),improved_parameter_pairs=2,complete_Lean_instances=0,experiments_rerun=0)
(WORK/'REDEI_OTHERPARAMS_WIKI_SYNC_RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))

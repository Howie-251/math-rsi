"""Unique Wiki increment from saved actual receipts; no mathematical job is run."""
from pathlib import Path
import copy
import json

ROOT = Path(__file__).resolve().parents[2]
WIKI = ROOT / 'research-wiki'
STEM = 'R7_F11_LOCAL_PUBLIC77_FIXEDM50_M33_TERMINAL_20261101'
STAGE = 'research/ddp/two_successful_methods_20261101/'
AFF = STAGE + 'affine_field_conditions/'
LOCAL = AFF + 'r7_f11_port_orbits/'
THREE = AFF + 'r7_schreier_controller_gate/'
FOUR = AFF + 'r7_fourbase_triangle_controller/'
PUBLIC = STAGE + 'public_baseline_audit/DEGREE77_R7_F11_TARGET_GATE_20261101'
IDS = [
    'ddp-r7-f11-four-orbit-twofive-typed-true-inverse-tenchart-local-interface-20261101',
    'ddp-degree77-r7-f11-public-tallini15-gq7-generalduplication-169750-controller-threshold128-20261101',
    'ddp-r7-threebase-fixed-m50-symbolic-capacity50-exactcover-all32-fail01-20261101',
    'ddp-r7-fourbase-triangle-m33-global2000000-unknown-cap-reached-20261101',
]
ZERO = dict(new_named_complete_graphs=0, new_Lean_instances=0, new_frameworks=0,
            full_graphs_generated=0, BFS_runs=0, Lean_compilations=0)
BASE = dict(family='Affine lift with typed inverse ports',
            idea_family='idea:ddp-open-parameter-construction-20261026', date='2026-11-01',
            target_Delta=77, target_D=3, savedL=None,
            baseline_date='2026-11-01 bounded primary-source derived guarantee; global/priority uncertified',
            n=dict(actual=None, hypothetical=None), actual_graph_Delta=None, actual_D=None,
            ordinary_bad_unordered_pairs=None, ordinary_bad_target_D=3, wiki_verdict='partial')

def row(**kw):
    r = copy.deepcopy(BASE)
    r.update(kw)
    return r

rows = [row(
    id=IDS[0], title='F11七port：两轨预测被推翻，132类2+5与10张真逆chart实际成立',
    record_type='local_finite_typed_port_analysis',
    actual_D_scope='有限PGL轨道、选定端口及10真逆chart；未造controller或完整图。',
    outcome_class='PREDICTION_PARTLY_REFUTED_FIXED_TYPED_LOCAL_INTERFACE_PASS',
    distance_text='预测264+660两轨被实际110/220/264/330四轨推翻；792七子集132为(0,0,2,5)、660为(1,2,2,2)。只前132类给264×2+330×5；finalports=[1,4,inf,0,2,3,5]、pi=[1,0,3,2,4,5,6]。10真实逆chart的360个NBturn全rank3，各12plane相邻覆盖1331，含重标.131403188CPU。独立单chart反例.000518141CPU：归一PGL逆的quotient多6倍，(0,1,1)错误往返(0,6,6)，reverse noise不能修；producer真实逆无缺陷。',
    scope='固定F11/132-profile对象/finalpi；非任意七子集、sorted邻标、任意same-type配对或所有29chart验证。端口接口是两directed2factor加三perfectmatching。',
    positive_guarantees=['实际1320个PGL置换、924六子集、792七子集；六子集四轨各自补集不变。',
                         '真实反向必须T^-1和noise=-t；PGL尺度等价不能替代字面线性逆。',
                         '已继承机制：中间chart的36秩条件覆盖NB三步，相邻12plane互补，同纤维靠controller三角；本次只实际检验F11接口，不当一般常识的新定理。'],
    unclosed_gap='局部PASS仍缺符合固定port的完整controller；0图/BFS/Lean，不计新构造。',
    lesson_and_restart_condition='预测被推翻后实际改变生成规则：只选132类和固定真逆角色，弃任意sorted标号/PGL归一逆；随后先核公开竞争门再派有界controller实验。',
    other_metrics={**ZERO, 'six_orbit_sizes':[110,220,264,330], 'seven_profiles':[{'counts':[0,0,2,5],'objects':132},{'counts':[1,2,2,2],'objects':660}], 'final_ports':[1,4,'inf',0,2,3,5], 'reverse_ports':[1,0,3,2,4,5,6], 'charts_checked':10, 'NBturn_rank3_checks':360, 'planes_per_pencil':12, 'producer_CPU_seconds':0.131403188, 'independent_counterexample_CPU_seconds':0.0005181409999999997, 'two_orbits_prediction_refuted':True, 'producer_inverse_defect_found':False, 'all_processes_terminal':True},
    evidence_paths=[LOCAL+x for x in ['PRED.md','PARAMETERS.json','RESULT.json','TERMINAL.json','PROOF.md','CHART_CHECKS.json','CONTROLLER_INTERFACE.md','INDEPENDENT_MECHANISM_NOTE.md','INDEPENDENT_INVERSE_COUNTEREXAMPLE.json','INDEPENDENT_INVERSE_COUNTEREXAMPLE.py']]),
row(
    id=IDS[1], title='77度公开门169750：Tallini15×GQ7/spread一般复制；F11纤维需H≥128',
    family='Published-source comparison gate', record_type='published_method_direct_scalar_comparison',
    actual_D_scope='已发表机制的标量代入和可核推论；0controller/图/BFS/Lean。',
    outcome_class='BEST_LOCATED_DERIVED_PUBLIC_GUARANTEE_169750_MIN_CONTROLLER128',
    distance_text='公开oppositeGQ(7,7)160000/64度，Tallini15 partialovoid×50 spread给750中心，一般Delorme§7复制13次推出169750=160000+13×750。中心诱导105K2+540isolates，复制有newnew匹配，不能用dist≥3特例。PolarStar IQ684合法组合max137424(q53,d23,degree77)，Paley417组合max129903(q49,d26,degree76)。F11³=1331，H127给169037不足，H128给170368；三base/evenm最小H132/m44。',
    scope='一次4primary查询、已存原始论文及.020526023CPU标量；169750是本次组合已发表机制的推论，不是原论文列数值或独立公开边表。只用公开Tallini15，不用本地160050/O22；任意公开augmentation/全球最高/priority未穷尽。',
    positive_guarantees=['Tallini15存在性据primary研究论文Ceria等§1/Table1所引结果；未取得原坐标，不冒复现169750边表。', '原始Delorme§7适用matching中心；已核其他GQ产品/复制与全部合法PolarStar窗口均不超过本门。', 'H132/175692只条件例子，不预判可行controller。'],
    unclosed_gap='degree77全球维护表、任意复制最优与优先权未穷尽；本门不产图。',
    lesson_and_restart_condition='先据169750筛选有竞争力的规模，再有界计算；局部PASS/条件点数不计图，完整fiber须另外生成验收。',
    other_metrics={**ZERO,'best_located_derived_guarantee':169750,'source_n':160000,'source_degree':64,'public_partial_ovoid':15,'spread_lines':50,'centers':750,'replications':13,'center_matching_edges':105,'center_isolates':540,'PolarStarIQ_legal_cases':684,'PolarStarPaley_legal_cases':417,'PolarStarIQmax':137424,'PolarStarPaleymax':129903,'minimumH':128,'minimum_threebase_evenH':132,'minimum_threebase_evenm':44,'scalar_CPU_seconds':0.020526023,'primary_query_batches':1,'queries':4,'unpublished_local_graph_used_as_public':False,'global_record_or_priority_certified':False},
    evidence_paths=[PUBLIC+x for x in ['.md','.json','_scalar_check.py']]),
row(
    id=IDS[2], title='固定三base七port m50严格闭域：26+3×8支持，32tiling全缺0→1路线',
    record_type='fixed_controller_topology_strict_exclusion', wiki_verdict='no',
    n=dict(actual=None,hypothetical=199650),
    actual_D_scope='固定三baseA/B/S/T/R、simple七port、m50完整A³严格排除；fullF11³无intrafi边lift亦失败，非一般7D3上界。',
    outcome_class='STRICT_FIXED_THREEBASE_M50_COMPLETE_DOMAIN_ALL32_TILINGS_FAIL01',
    distance_text='R只base0 half、交换base1/2避旧S/T重复。实际1029词counts=[[50,64,64],[64,52,56],[64,56,52]]，只该topology evenm≤50。m50 root00必须50型无重复，独立symbolicidentity给26base+三8块；a0归一2/10，d三值排序保图。4802outer全域、844可行base、3736blocks、8140pairnodes，32root00tiling全在0→1失败，0未试/0完整controller。含prepare/编译/identity .919086454CPU。',
    scope='仅此三base拓扑m50、simple和完整A³；旧mod10 passingprofile是必要门旧OPEN，已被本次完整exactcover严格终态覆盖。smaller evenm≤48开放，无自动48/46/44梯子；非所有七port或其他F11机制排除。',
    positive_guarantees=['事前symbolic最小>36获支持、实际50，使最高端m50成为明确有限门。', '50真实wordforms与26+三8块逐整数向量相等；不重复旧residue枚举。', '缺三walk的0→1 pair非邻（相邻总有backtrack三walk）；继承障碍代入F11，两步至多7×121=847<1331，故此固定fullfiber确不D3；非新普适定理。'],
    unclosed_gap='m50严格失败；同topology evenm≤48/其他拓扑开放，不自动降模数。',
    lesson_and_restart_condition='同层可行32对象均无法同时补0→1，缺的是兼容路线；停止最高端，改四base生成规则且保B三角，再过symbolic/公开门做一次global批次，避免按坏对微降续算。',
    other_metrics={**ZERO,'symbolic_words':1029,'symbolic_counts':[[50,64,64],[64,52,56],[64,56,52]],'fixed_topology_even_m_bound':50,'fixed_topology_controller_bound':150,'outer_visited':4802,'outer_total':4802,'root00_tilings':32,'full_support_tests':32,'first_failure_pair':[0,1],'passing_controllers':0,'unvisited':0,'accounted_CPU_seconds':0.919086454,'old_mod10_OPEN_superseded':True,'smaller_even_m_remaining_upper':48,'automatic_lower_modulus_authorized':False,'all_processes_terminal':True},
    evidence_paths=[THREE+x for x in ['PRED.md','SYMBOLIC_RESULT.json','M50_RESIDUE_RESULT.json','DISTINCT_FORMS.tsv','INDEPENDENT_M50_NOTE.md','m50_exact_cover/PRED.md','m50_exact_cover/PROOF.md','m50_exact_cover/RESULT.json','m50_exact_cover/TERMINAL.json','m50_exact_cover/SYMBOLIC_IDENTITY_RESULT.json','m50_exact_cover/check_symbolic_identity.py','m50_exact_cover/gate.cpp','m50_exact_cover/run_gate.py']]),
row(
    id=IDS[3], title='四base三角m33：1372词容量门支持；200万合法global样本终态UNKNOWN',
    record_type='fixed_controller_topology_bounded_global_sampling_unknown',
    n=dict(actual=None,hypothetical=175692),
    actual_D_scope='固定四base m33/e11有限global参数采样；0完整controller witness/图；非全族排除。',
    outcome_class='UNKNOWN_SAMPLE_CAP_REACHED_2000000_LEGAL_NO_CONTROLLER_NOT_EXHAUSTIVE',
    distance_text='A四循环，B在012零电压三循环、base3平移m/3；S/T/R三无固定base匹配。实际1372词16类最小51、3|m，首competitive m33/H132条件175692（对169750+5942）。实际batch用a3=0 gauge、保e11单位五轨[1,2,3,11,22]各400000，共2000000合法，seed2026110107、16191788原PRNG输出。终态UNKNOWN_SAMPLE_CAP_REACHED，0witness，含编译1.822285705CPU<30。首(3,3)失败1962566，02:36946/11:386/01:84/12:15/03:3；37434过首门、488过02，最后3在03止。',
    scope='单固定topology/Z33、归一branch内合法global随机样本；非全域穷举/非family排除。24MB按序实际attempt记录保存；因无witness未执行132controller与17424pairword导出。unusedCPU不自动授权下一批。',
    positive_guarantees=['symboliccounts=[[69,62,56,66],[62,61,62,67],[56,62,69,66],[66,67,66,51]]，只给此规则m≤51且3|m，不证明m33存在。', '每候选独立生成，覆盖反馈不改变下一候选，0hillclimb。', '实际报告代表(22,26,31,0,25,17,21,21,4,27)的signature=[[33,33,33,32],[33,33,33,32],[33,33,31,33],[32,32,33,33]]；缺03{5}/13{8}/22{9,24}/30{28}/31{25}，仅报告代表，非全族或样本整体最优断言。'],
    unclosed_gap='无完整exact3walk controller；采样UNKNOWN仍不知m33是否存在，0F11完整图/BFS/Lean。',
    lesson_and_restart_condition='改变结构让部分16类同时覆盖，但少量缺口不足以无限计算。51型同层门贡献绝大多数失败，应据缺路线及首失败分布作root下一机制决策；当前停止，不自动第二seed/hillclimb/m梯子或模板清单。',
    other_metrics={**ZERO,'symbolic_words':1372,'symbolic_counts':[[69,62,56,66],[62,61,62,67],[56,62,69,66],[66,67,66,51]],'symbolic_minimum':51,'symbolic_CPU_seconds':0.011546033,'m':33,'conditional_controller_order':132,'conditional_gain':5942,'legal_candidates':2000000,'legal_limit':2000000,'branch_representatives':[1,2,3,11,22],'branch_counts':[400000]*5,'seed':2026110107,'raw_PRNG_draws':16191788,'first_failure_counts':[0,84,36946,3,0,386,15,0,0,0,0,0,0,0,0,1962566],'representative_parameters':[22,26,31,0,25,17,21,21,4,27],'representative_signature':[[33,33,33,32],[33,33,33,32],[33,33,31,33],[32,32,33,33]],'attempt_file_bytes':24000000,'accounted_CPU_seconds':1.8222857049999996,'CPU_budget':30,'family_exclusion':False,'search_complete':False,'literal_controller_exported':False,'automatic_retry_authorized':False,'all_processes_terminal':True},
    evidence_paths=[FOUR+x for x in ['PRED.md','PROOF.md','RESULT.json','TERMINAL.json','DISTINCT_FORMS.tsv','count_symbolic.py','m33_global_batch/PRED.md','m33_global_batch/PROOF.md','m33_global_batch/RESULT.json','m33_global_batch/TERMINAL.json','m33_global_batch/EXAMPLE_COVERAGE.json','m33_global_batch/search.cpp','m33_global_batch/run_once.py']]),
]

# Update the already-existing family only to replace its now-stale next-B status.
old = json.loads((WIKI/'updates/F9_SIX_TARGET_FINAL_C_AND_DEGREE77_GATE_20261101_ROWS.json').read_text())
u = next(r for r in old if r['id']=='ddp-f9-controller-u10-plane-clone-degree55-59-window-public-stop60-20261101')
u['lesson_and_restart_condition'] = u['lesson_and_restart_condition'].split('下一新B')[0] + '下一B现已F11局部接口PASS，公开77门169750，固定三base m50严格失败，继而四base m33一次200万合法global样本终态UNKNOWN；0controller/图，不自动续算。见本轮r7四节点。原family五图及六target A/B/freshC实际全部完成不变。'
rows.append(u)
out = WIKI/'updates'/f'{STEM}_ROWS.json'
out.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
missing = [(r['id'],p) for r in rows for p in r['evidence_paths'] if not (ROOT/p).exists()]
assert not missing, missing
print(json.dumps(dict(rows=len(rows),new_ids=IDS,evidence_paths=sum(len(r['evidence_paths']) for r in rows)),ensure_ascii=False))

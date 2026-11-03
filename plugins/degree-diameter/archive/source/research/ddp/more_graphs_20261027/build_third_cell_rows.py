"""Capture completed third-cell construction and its specific supporting experiments."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[3]
WORK=Path(__file__).resolve().parent
BASE='research/ddp/more_graphs_20261027/'
rows=[]

def add(id,title,family,delta,D,L,folder,result,lesson,metrics=None,actual=None,hyp=None,
        kind='finite-construction-experiment',verdict='no',degree=None,diameter=None,paths=()):
    r=dict(id=id,title=title,family=family,record_type=kind,target_Delta=delta,target_D=D,savedL=L,
           n=dict(actual=actual,hypothetical=hyp),actual_graph_Delta=degree,actual_D=diameter,
           ordinary_bad_unordered_pairs=None,ordinary_bad_target_D=D,
           scope=result,failure_or_result=result,lesson_and_restart_condition=lesson,
           unclosed_gap='No general source-family maximality is claimed; final concrete Lean remains incomplete.',
           other_metrics=metrics or {},outcome_class=kind,wiki_verdict=verdict,
           report_paths=[BASE+folder+'/REPORT.md',BASE+folder+'/RESULT.json']+list(paths))
    rows.append(r)
    return r

star=add('ddp-spare-star-actual-three-sources-20261027',
    '完整邻域复制三源检查：N13最少1满邻点，N14最少9，均无直接twin',
    'Prototype-neighborhood extension',None,5,None,'spare_star_transfer',
    '实际51417/94186源逐v完整N(v)扫描均无合法fullstar；最少满邻点分别1（91 prototypes）和9（20 prototypes）。D15源到后同一native扫描100132个v也无fullstar。0BFS/新图。',
    'N13恰1满邻点提示可以有依据删1并修复私有路线；N14至少9不适合照搬单缺口规则。完整N(v)保边复制失败不排near-neighborhood修复。',
    dict(source13_minimum_saturated_neighbors=1,source13_minimum_attainers=91,
         source14_minimum_saturated_neighbors=9,source14_minimum_attainers=20,
         source15_prototypes_scanned=100132,fullstar_hits=0,source13_14_CPU_seconds=.67839,BFS=0))
star['target_is_multivalued']=True
star['variants']=[dict(label='source13',target_Delta=13,target_D=5,savedL=51417),dict(label='source14',target_Delta=14,target_D=5,savedL=94186),dict(label='source15',target_Delta=15,target_D=5,savedL=100132)]

b=BASE+'d13_D5_h9_transfer/singlefault_star_probe/'
add('ddp-d13-singlefault-star-family-51457-20261027',
    '第三参数完整新图族：(13,5)51418–51457，共40阶数',
    'H9 prototype-neighborhood extension',13,5,51417,'d13_D5_h9_transfer/singlefault_star_probe/continuation',
    '91个单满邻点prototype先冻结；首38项得51418，余53项once-policy得39张。全91终态40accepted+13当时degreeblocked+38限定guard失败=91。最强51457/m324863/max13/Dexact5。首51418从literal边表fresh核验新root，并比对original官方raw全部边；后39步完整实际currentR4/degree归纳。',
    '从degreeblocked完整geometric邻域转近完整旧prototype star，成功修好整个私有远端类而非仅减少坏点。原37失败未刷新，原53续完只3.209CPU。停止已完91池，失败仅限定所记录旧base及≤min(剩余预算,2)guards，不作51457最大性结论。',
    dict(new_lower_bound_mathematically_verified=True,improved_parameter_pair=[13,5],
         example_orders=list(range(51418,51458)),example_count=40,strongest_n=51457,strongest_m=324863,
         public_baseline=51417,baseline_checked_UTC='2026-10-27 17:38:52 UTC',
         original_frozen_prototypes=91,accepted=40,current_degree_blocked=13,limited_guard_failures=38,
         unattempted=0,producer_CPU_seconds=12.853252,
         first_independent_newroot_n=51418,first_independent_CPU_seconds=.922139902,
         old_source_allBFS=False,later_independent_BFS_count=0,
         complete_Lean_instances=0,Goal_complete=False,public_submission=False,
         review_status='GEMINI_ACCEPTED_FIRST_GRAPH_AND_INDUCTION',
         actual_reviewer_model='gemini-3.8-flash-high',actual_reviewer_effort='high',
         review_extra_perstep_BFS_advice_adopted=False,
         guaranteed_bad_pairs_by_complete_induction=0,
         source_author='Dharunish Yugeswardeenoo; partial-fold foundation Rishabh Rajiv'),
    actual=51457,kind='mathematically-verified-new-lower-bound-family',verdict='yes',degree=13,diameter=5,
    paths=[b+'first_hit.json',b+'independent_newroot51418.json',b+'accepted_family40.json',
           b+'continuation/accepted_sequence.json',b+'continuation/graphs/graph_d13_D5_n51457.edges',
           BASE+'delivery/families.json',BASE+'delivery/family_generator.py',
           'reviews/ddp/d13_singlefault_star_20261027.DISPOSITION.md'])
rows[-1]['actual_D_scope']='First newroot independentBFS plus originalpublicraw edge retention; everylater currentgraph completeR4+degree induction; orders exceed D4 Moorebound24506. PublishedoriginalsourceD5 inherited.'

add('ddp-d13-singlefault-star-guard-mechanism-20261027',
    '成功机制实测：同10个core邻点的free代理补全3614私有目标',
    'H9 prototype-neighborhood extension',13,5,51417,'d13_D5_h9_transfer/singlefault_star_probe',
    'prototype51013删满pin11352后缺3535core+79extras；guard50577完整补齐。D/G共享全部10core邻点，D-only=[50848,51013,51287]、G-only=[51275]均是extras，非fulltwins。3608洞有经共享分支的guard最短路，6core洞由G-only分支给更短路；每个原prototype≤5私有路线都须先经被删pin。',
    '优先找满pin的free核心邻域代理，先看代理是否已在保留集合，再完整currentR4；不是任意allanchor试配。最小对照3962删6216的10pins在ORIGINAL51417已全覆/degree合法，且保留50638已同core邻域；首seed对此例旧target覆盖非必要，其它39原base未复算，不能外推全部。',
    dict(missing_core=3535,missing_extras=79,shared_core_neighbors=10,
         guard_shared_shortest_route_targets=3608,guard_only_shortest_branch_targets=6,
         guard_is_full_twin=False,originalbase_control_prototype=3962,
         originalbase_control_missing=0,originalbase_control_retained_core_proxy=50638,
         originalbase_control_cases=1,total_analysis_CPU_seconds=.376492091,
         other39_originalbase_checks=0,newgraphs=0),
    kind='source-route-analysis',verdict='yes',actual=51417,
    paths=[b+'MECHANISM.md',b+'MECHANISM.json',b+'ORIGINALBASE_CONTROL.json',b+'CONTROL_PREDICTION.json'])

add('ddp-d14-global-cover-mip-unknown-20261027',
    '(14,5)全局选边模型：一次incumbent失败，第二模型终止，UNKNOWN',
    'Mizuno current-source extension',14,5,94186,'d14_D5_mizuno_extension/global_cover_mip',
    '保留全部3685binary columns，Σx≤14；256真实target约束先得14pin incumbent，完整94186cache验缺6430，加973实际violatedcuts成1229约束。第二模型SIGKILL/137，未返回新incumbent。不是UNSAT或整族无解。',
    '全局协调与贪心不同，但此预算没有解决同时覆盖。停止此模型，不冷启。仅求解器time_limit不能保证进程CPU窗口；未来有具体理由重新实现时应把单次solver隔离在外部CPU guard下，不能伪报未回传累计CPU。',
    dict(models_started=2,models_returned=1,integer_candidates_checked=1,first_candidate_missing=6430,
         added_original_constraints=973,final_active_constraints=1229,status='UNKNOWN',exitcode=137,
         solver_CPU_observed_lower_bound=2.412668242,whole_CPU_observed_lower_bound=2.782928979,
         solver_CPU_total=None,whole_CPU_total=None,budget_compliance='NOT_ESTABLISHED',
         strict_exclusion=False,BFS=0),hyp=94187,kind='UNKNOWN-global-cover-MIP',verdict='partial')

add('ddp-d15-source-and-20ball-prediction-20261027',
    '(15,5)100132源与覆盖预测：同单余量类20.11%对17.39%',
    'Mizuno current-source extension',15,5,100132,'d15_D5_mizuno_extension',
    '实际100132/m749732/max15，degree13:18、14:2480、15:97634，free2498/slots2516。首20free点R4平均20042.3，占20.0159%；先前D14rare15为16.1100%。纠正余量类型后，完整单余量population的D15平均20.1129%、D14平均17.3888%，相同lex20规则也支持更高覆盖比例。',
    '球密度预测获支持，只支持转实际构造，不证明15连接能共同覆盖，更不能把不同source/degree/field的比较当fieldsize单独因果效应。原fiber标签未绑定，不假定前100000就是旧core。',
    dict(source_n=100132,source_m=749732,free_vertices=2498,free_slots=2516,
         sampled_R4_balls=20,first20_mean_fraction=.200158790396676,
         matched_one_slot_mean_D15=.20112948488640156,matched_one_slot_mean_D14=.17388806171752097,
         matched_one_slot_comparison_CPU=.158289577,
         source_and20ball_CPU=1.742385652,oldsource_allBFS=0,
         sphere_prediction='SUPPORTED',global_atmost15_existence='UNRESOLVED'),
    actual=100132,kind='source-recovery-and-prediction',verdict='yes',degree=15,
    paths=[BASE+'d15_D5_mizuno_extension/one_slot_comparison/PREDICTION.json',
           BASE+'d15_D5_mizuno_extension/one_slot_comparison/RESULT.json'])
add('ddp-d15-allfree64-cover-probe-20261027',
    '(15,5)全2498可接点：64个完整15pin方案无命中',
    'Mizuno current-source extension',15,5,100132,'d15_D5_mizuno_extension/allfree_cover_probe',
    '复用20球、一次补2478球，完整allfree union全盖100132，每target支持364..651。冻结64方案全部完成，0hit，漏1848..2064。0新图/0source全BFS。',
    '局部球比例提高获支持，但同一有限离散选择仍未共同cover；停止该规则，不按1848少于3705续算。所有31MB球缓存保留。任意≤15cover存在性仍UNRESOLVED，不能把64无命中登记为整族无望。',
    dict(candidates=2498,reused_R4_balls=20,new_R4_balls=2478,allfree_union_missing=0,
         target_support_min=364,target_support_max=651,frozen_candidates=64,evaluated=64,hits=0,
         newroot_uncovered_targets_min=1848,newroot_uncovered_targets_max=2064,
         CPU_including_compile=4.066048549,operation_prediction='REFUTED',
         global_existence='UNRESOLVED',BFS=0,cache_bytes=31274960),hyp=100133)

for D,L,k,folder,cpu,slots in [(6,132,2,'cubic_D6_twofold70',.02555,1204),(7,200,3,'cubic_D7_threefold70',.04134,364)]:
    add(f'ddp-afy70-{k}fold-D{D}-capacity-20261027',
        f'(3,{D})AFY70的{k}重cover：短闭路/路线容量均匀排除',
        'AFY70 ordinary covers',3,D,L,folder,
        f'固定官方AFY70源70/105，在D={D}内70个diagonal槽均只有identity路径，另有不同点容量1槽；全部4900端点槽检查，{slots}槽只有1个raw NBroute/form，不能覆盖{k}sheets。0电压赋值/线性求解/BFS/新图。',
        f'先检查同fiber短闭路和端点路线数，避免盲扫电压。任何此source普通{k}重cover都不能D≤{D}（或不连通），不排其它70source/新基图/任意degree3图。D6结果促使有依据查D7，D7仍失败后停止该机制，不续D8长尾。',
        dict(base_n=70,base_m=105,cover_fibers=k,ordered_slots=4900,capacity_one_slots=slots,
             diagonal_identity_only=70,voltage_assignments=0,linear_system_run=False,CPU_seconds=cpu,
             strict_scope_excluded=True,arbitrary_graph_excluded=False),hyp=70*k,
        kind='positive-local-capacity-obstruction',verdict='yes')

(WORK/'third_cell_and_related_rows.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print('Captured',len(rows),'completed records; newgraph counts only from D13 family.')

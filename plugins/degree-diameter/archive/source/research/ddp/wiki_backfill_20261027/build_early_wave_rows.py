"""Read REPORT/JSON metadata only; leave recent_rows and wiki unchanged."""
from pathlib import Path
import json
import re

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
cases=json.loads((ROOT/'context/DD_PORTFOLIO_START_20261026/registry/cases.json').read_text())['cases']
L={(x['degree_cap'],x['diameter_cap']):x['baseline_order'] for x in cases}
rows=[]

def add(w,slug,title,family,kind,delta,D,n,scope,result,positive,gap,restart,
        actual_n=None,actual_delta=None,actual_D=None,bad=None,metrics=None,relations=None,variants=None):
    p=ROOT/f'research/ddp/breadth_20261027_wave{w}'/slug
    reports=[x for x in p.rglob('*') if x.is_file() and x.name in ('REPORT.md','README.md','THEOREM_SCOPE_REVIEW.md','SOURCE_NOTES.md')]
    for x in reports:x.read_text()
    statuses={}
    for x in p.rglob('*.json'):
        if x.name in ('RESULT.json','RESULTS.json','SCOUT.json','terminal.json','result.json','search_result.json'):
            z=json.loads(x.read_text())
            if isinstance(z,dict):statuses[str(x.relative_to(p))]=z.get('status')
    evidence=[str(x.relative_to(ROOT)) for x in sorted(p.rglob('*')) if x.is_file()
              and x.suffix in ('.md','.json','.edges','.xz','.txt','.jsonl','.states')
              and not re.search(r'hash|sha256|checksum',x.name,re.I)]
    r=dict(id=f'ddp-wave{w}-{slug.replace("_","-")}',title=title,family=family,wave=w,
           record_type=kind,target_Delta=delta,target_D=D,savedL=L.get((delta,D)),
           n=dict(actual=actual_n,hypothetical=n),actual_D=actual_D,
           actual_D_scope='saved_explicit_graph' if actual_D is not None else None,
           actual_graph_Delta=actual_delta,ordinary_bad_unordered_pairs=bad,
           ordinary_bad_target_D=D if bad is not None else None,
           scope=scope,failure_or_result=result,positive_guarantees=positive,
           unclosed_gap=gap,lesson_and_restart_condition=restart,
           other_metrics=metrics or {},relations=relations or [],variants=variants or [],
           primary_source_directory=str(p.relative_to(ROOT)),source_statuses=statuses,
           report_paths=[str(x.relative_to(ROOT)) for x in reports],evidence_paths=evidence,
           new_lower_bound=False)
    rows.append(r);return r

route='four-label affine route-chart lifts'
geom='H9 partial-fold split/copy/twin geometry'
add(2,'extension105_d4','固定104c→105单点四spoke增阶','source-edge deletion and vertex insertion','finite-family-exhaustion',4,4,105,
    '固定104c删两条不接边、加一点连其四端点；后续两个局部邻域属于本源跟进',
    '20904合法候选全部无D4；bestD5/8。两局部跟进也无改善，best复用同一图验收。',
    ['所有候选simple4regular105/210','完整既定参数范围'],
    '不排其他增阶操作或一般105图；不是整个source扩张族穷尽。',
    '此source已收束，不追加局部自由点或多边交换。',actual_n=105,actual_delta=4,actual_D=5,bad=8,
    metrics={'raw_source_edge_pairs':21528,'legal_candidates':20904},variants=[
        {'id':'complete-two-edge-switch-neighborhood','scope':'保存best的全部普通单步2switch','legal_neighbors':40740,'strict_improvements':0,'best_unchanged':True,'actual_D_reused':5,'bad_unordered_reused':8},
        {'id':'fixed-nine-vertex-degree-completion','scope':'只释放12/13的八条incident边，九点准确残余degree','completions':230,'best_unchanged':True,'actual_D_reused':5,'bad_unordered_reused':8}])
add(2,'extension254_d4','252→254四matching-edge双点增阶','source-edge deletion and vertex insertion','finite-profile',5,4,254,
    '固定252源四条不接边及方向；8starts×10000提案',
    'bestD5/133，完成有限批次，不是所有四matching扩张穷尽。',['全部候选simple5regular254/635'],
    '其他四matching赋值和其他254图仍开放。','固定批次停止，不加seed/删边数/source。',
    actual_n=254,actual_delta=5,actual_D=5,bad=133,metrics={'proposals':80000,'legal_trials':78252},relations=['same_mechanism_as:ddp-wave2-extension105-d4'])
add(2,'lexicographic_products','全部27格均匀lexicographic产品阶数界','uniform graph products','parameter/capacity',None,None,None,
    'G[H]，connected|G|≥2、任意simple|H|≥2；含均匀independent blowup',
    '330个参数对的Moore/degree数值上界筛；无可越线入口。',
    ['Δ(G[H])=|H|Δ(G)+Δ(H)','D由base及局部replacement约束'],
    '不含非均匀blowup或任意replacement。','必须改变均匀产品模板，不能换seed。',metrics={'parameter_pairs':330,'graphs_generated':0})
add(2,'line1664_d4','固定Bhakar104×F2⁴二邻点线关系提升','fixed-controller affine line relations','capacity',8,4,1664,
    '固定104投影、16fiber、无内部边、每控制边最多两个邻点，含非线性关系放宽',
    '0→32只有唯一三路且无其他≤4walk，至多8<16，指定投影模板统一排除。',
    ['完整walk包含反走','源104D4复用'],
    '不排其他控制图、内部边、更大branch或一般1664图。','须改变投影路线容量；矩阵/seed不能补足。',metrics={'capacity':8,'required_states':16,'graphs_generated':0,'source_n':104,'all_walk_witness':[0,24,4,32]})
add(2,'ternary8424_degree_budget','固定104×81三邻点degree预算提升','fixed-controller affine line relations','capacity',12,4,8424,
    '固定104、branch cap3、Δ12；允许内部预算但独占四路迫使全边branch3',
    '全部208控制边被迫branch3，内部余量0；0→32唯一三路仅27<81。',
    ['2208个unique-distance4有序槽用于强迫预算','另有真实无四walk的三路见证'],
    '不排更高branch/不同控制器/任意lift。','须改变degree/路径机制，不能仅换域赋值。',metrics={'forced_edges':208,'unique_distance4_ordered_slots':2208,'capacity':27,'required_states':81,'graphs_generated':0},relations=['degree_variant_of:ddp-wave2-line1664-d4','later_wide_chart_screen:ddp-wave5-bhakar104-wide-screen'])
add(2,'sl23_c8_biorbit384_d5','SL2(F3)×C8双轨道2+2模板','bi-orbit Cayley/voltage constructions','capacity',4,5,384,
    '固定group及2+2分配全部13824个SL quotient triples',
    '最大最小fiber容量5<8，全固定模板排除；未开实际图profile。',[],
    '不排其他生成元组成、群或非同模板图。','需改变quotient短路容量。',metrics={'quotient_triples':13824,'capacity':5,'required_states':8,'graphs_generated':0})
add(2,'two_orbit128_scout','Q64双轨道2+4：phase容量来源筛','bi-orbit Cayley/voltage constructions','capacity-pass-scout',6,3,128,
    '32个phase模式；只是必要容量筛',
    '14模式通过，未作参数搜索；交给后续独立有限profile。',['32phasefiber各需32状态','短词算术校准'],
    '容量通过不是D3存在证据。','只建议一次有界实际profile，已由search执行。',metrics={'phase_patterns':32,'surviving_patterns':14,'actual_searches':0},relations=['prepares:ddp-wave2-two-orbit128-search'])
add(2,'two_orbit128_search','Q64双轨道128实际14phase有限试验','bi-orbit Cayley/voltage constructions','finite-profile',6,3,128,
    '14个通过phase，各固定三段邻域/两次kick；非全部Q64参数穷尽',
    'bestD4/928；所有预定phase完成后停止。',['two-orbit作用代表根数与全图计数相符'],
    '代表根deficit29不是928无序坏对。','该有限profile停止，不能以余预算加kick。',
    actual_n=128,actual_delta=6,actual_D=4,bad=928,metrics={'representative_deficit_sum':29,'translation_factor_to_unordered':32,'legal_score_evaluations':13422},relations=['profile_of:ddp-wave2-two-orbit128-scout'])
for slug,n,bad,deficit,slots in [('triangle_factor33_controller',33,12,684,28),('triangle_bowtie32_controller',32,4,324,14)]:
    add(2,slug,f'{n}点三角端口控制系统固定有限合成',route,'finite-profile',12,3,27*n,
        '固定三角骨架+external2factor，8starts各100000提案；32是33的共享三角结构跟进',
        f'best controllerD4/{bad}普通坏对；容量U缺量{deficit}、{slots}个有序不足槽。',
        ['simplequartic及固定三角边/externaldegree保持','优化U=I+3A+9A²+27A³完整必要上界'],
        'U≥27也非实际fiber覆盖；本次未达必要条件，未生成提升图。',
        '三角端口骨架已收束，不追加31/34/seed；不排整个控制器族。',actual_n=n,actual_delta=4,actual_D=4,bad=bad,
        metrics={'capacity_deficit_ordered':deficit,'capacity_insufficient_ordered_slots':slots,'proposals':800000,'large_lift_generated':False},
        relations=(['structural_followup_of:ddp-wave2-triangle-factor33-controller'] if n==32 else []))

add(3,'source_scout','通用F3⁵五步chart与180/186控制器固定群筛',route,'word-rank/source-scout',12,5,42525,
    '原文通用chart；Cayley控制器子试验为从属有限群范围，不是独立新大类',
    '324/324词rank5且逆一致；尚无≥175点quartic exact-NB5控制器。',
    ['任意合格逆标号controller C给243|C|点、degree12、D≤5'],
    'ordinaryD≤5不足以代替exactNB5；chart正向结果不等于新图。',
    '仅有明确新控制器结构/路由覆盖才继续，不排队换群。',metrics={'rank5_words':324,'minimum_controller_order':175},variants=[
        {'id':'A5xC3-180','hypothetical_lift_n':43740,'scope':'全部13296个四元inverse-closed S','actual_sets_checked':11931,'two_noninvolution_inverse_pair_sets':3321,'mixed_onepair_twoinvolutions':8610,'four_involution_sets_disconnected':1365,'best_exactNB5_endpoints_two_pair':163,'best_exactNB5_endpoints_mixed':162,'all_scope_excluded':True,'actual_D':None},
        {'id':'F31:C6-186','hypothetical_lift_n':45198,'scope':'仅2926个二非对合逆对组成','actual_sets_checked':2926,'all_scope_excluded':True,'other_compositions_open':True,'actual_D':None}])
add(3,'pentagon175_controller','35个C5固定骨架的175控制器',route,'finite-profile',12,5,42525,
    '四starts各10000外2factor交换提案；不排整个C5骨架',
    'best controller ordinaryD6/315；exactNB5缺2696有序对。',
    ['每点C5保证self有NB5闭路','simplequartic逆标号一致'],
    '其他ordered pair的exactNB5未闭，未生成42525图。','profile停止，不追加starts/group。',
    actual_n=175,actual_delta=4,actual_D=6,bad=315,metrics={'exact_NB5_missing_ordered_pairs':2696,'proposals':40000},relations=['uses_chart:ddp-wave3-source-scout'])
add(3,'controller_lift192','原6点base的C4×C8电压192控制器',route,'finite-profile',12,5,46656,
    '固定base/group，八starts×25000单坐标提案；非全部电压空间',
    'best controller ordinaryD6/144；exactNB5缺2752有序对。',
    ['沿原144结构移植校准','32fiber平移作用使代表缺86×32=2752'],
    '所有exactNB5槽仍未闭，未生成46656提升。','父profile停止，不扩group/sheet/base。',
    actual_n=192,actual_delta=4,actual_D=6,bad=144,metrics={'representative_NB5_misses':86,'exact_NB5_missing_ordered_pairs':2752,'proposals':200000},relations=['uses_chart:ddp-wave3-source-scout'])
add(3,'binary_route_chart4','F2⁴四逆标签通用四步chart完整空间',route,'word-rank',8,4,1104,
    'F2维4、四无不动点逆标签、一步单参数、全部108约化四词均满秩',
    '2419200规范候选全部失败；只此规范模型统一排除。',['aaaa循环基规范完整','单保存候选108词独立校准'],
    '没有chart/控制器/大图；不能假定72controller。','必须改变通用路由要求或机制，不加seed。',metrics={'canonical_space':2419200,'examined':2419200,'words':108,'minimum_hypothetical_controller_order':69,'graphs_generated':0})
add(3,'cubic_nb5_bounds','三价exact-NB4/NB5控制器谱与计数界',route,'theoretical-controller-bound',None,None,None,
    '仅cubic exact-NB4/5控制器，odd-label fiber chart尚未给出',
    'NB4阶≤20；NB5阶≤44，42/44开放，不声称≤40。',['自含有理谱与有限域算术检查'],
    '未构造42/44图；不能自动映射到某个27格提升目标。','有真实odd-label chart和控制器正向结构才继续。',metrics={'controller_Delta':3,'exact_NB4_order_bound':20,'exact_NB5_order_bound':44,'NB5_open_orders':[42,44],'graphs_generated':0})
add(3,'debruijn256','无向4字母4位状态移位图256及补边障碍','state-shift / de Bruijn graphs','explicit-graph-plus-capacity',8,3,256,
    '固定x--(4x+a)mod256去loops/duplicates；全部旧边保留的Δ8补边',
    '实际D4/12354；(27,73)到全部亏度点各至少2步，新增边路线≥5，所有单调补边失败。',
    ['真实入边恢复反向邻居，不用模256除4','固定源connected'],
    '不排删边重连或其他state图。','必须改变旧边保留约束，不能填度余量继续搜。',
    actual_n=256,actual_delta=8,actual_D=4,bad=12354,metrics={'edges':1014,'degree_histogram':{'6':4,'7':12,'8':240},'deficit_vertices':16,'deficit_slots':20})
add(3,'binary_branch364','364核binary branching必要matching MILP','branched binary covers','solver-UNKNOWN',5,5,728,
    '固定364核；edge关系bijection或K2,2，必要matching必须击中全部unique5 geodesics',
    '25秒求解无incumbent、无不可行证明，UNKNOWN；未生成728图。',
    ['固定源D5及34860唯一路义务已准备'],
    '必要matching尚未解决；即使通过仍非全图D5证书。','需新结构/明确有限授权，不能把UNKNOWN当UNSAT。',metrics={'unique_path_constraints':34860,'solver_status':'UNKNOWN','incumbent_returned':False,'graphs_generated':0})
add(3,'hexagon_partial_fold_scout','H9任意split/copy/twin定理与逐点witness恢复',geom,'source-recovery',12,5,None,
    '原H9/duality与部分折叠作者资料；已有41699成品的局部结构恢复',
    'V/E与degree公式恢复；原witness S7959+copies280+twins63=41699，非新record。',
    ['点到线≤5奇路径投影给任意合法S/c的D≤5','H3完整blowup和旧邻居twins保留D≤5'],
    '原PSL/PΓL轨道作用未恢复，后续pencil邻接/证明缺失；未做大BFS。','已有逐点Q数据足够解除轨道常值约束，无需换群。',
    metrics={'known_author_n':41699,'known_core_n':41636,'Q_vertices':33033,'H3_vertices':364,'target_core_gain':707,'source_known_D_upper_bound':5})
add(3,'hexagon_partial_fold_greedy','H9逐点解除orbit常值：四序greedy与单调闭包',geom,'finite-profile-plus-monotone-exclusion',12,5,42343,
    '原S固定为子集、H3 copies固定280；任意重染也包含在root后续闭包排除内',
    '四序新增0；root强迫闭包禁全部25074 merged，故该指定单调cone任何真S超集不可能。',
    ['合法状态仍有几何D≤5保证','逐点degree精确维护与独立重算'],
    '允许删除旧split或改变copies仍开放；未展开新大图。','必须做结构交换，不再加批量split或重染。',metrics={'partial_state_core_order':41636,'split_fibers':7959,'copies':280,'merged_forbidden':25074,'actual_D_measured':False},relations=['uses_source:ddp-wave3-hexagon-partial-fold-scout'])
add(3,'hexagon_partial_fold_joint','H9四预定region联合S/c/copies MILP',geom,'finite-local-optimization',12,5,42343,
    '四预定region、域外固定，freegeneric820/820/899/901；copy变量1/1/28/28',
    '四区均Optimal gap0，gain0；best核心41636且state未变。',
    ['允许删除/加split、重染、改copies','边界外degree约束完整纳入','所有逐点degree通过'],
    '仅局部子问题optimal，不排全局部分折叠；没有展开大图。','不扩大旧区域；须新的全局结构步骤。',metrics={'partial_state_core_order':41636,'solver_statuses':['Optimal']*4,'objective_gain':0},relations=['structural_followup_of:ddp-wave3-hexagon-partial-fold-greedy'])
add(3,'tits585_batch_extension','Tits585批量spoke增阶来源和严格子类界','multi-vertex extension with spoke cooperation','source-scout/capacity',12,3,None,
    '保留585旧核；12个单组贪心仅来源试验，独立二步支配组装填子类另有界',
    '所有样本回到旧复制；独立支配组在Δ12总n≤796<810。未排共享spoke/新点互助一般模型。',
    ['旧old-old≤3保持','给出一般批量新旧/新新完整覆盖条件'],
    '没有新的同时满足degree预算的批量图；12样本不是全部组枚举。','须设计非复制组并用互助覆盖，不仅把组大小8变9/10。',metrics={'source_n':585,'source_degree_histogram':{'8':65,'9':520},'greedy_starts':12,'independent_group_order_bound_Delta12':796,'graphs_generated':0})

add(4,'global_partial_fold','H9全局三态三起点固定单点退火',geom,'finite-profile-partial-state',12,5,42343,
    '全部33033generic自由三态，copies固定0；三starts各50CPU秒',
    '最好合法核心38383/S4986；另两终态1068/1124实际点度13，不能当Δ12图。',
    ['允许先删后增，不再固定作者S','合法state的D≤5仍由原几何定理提供'],
    '未越逐点degree能垒；未证明全局模型不行；没有展开大图。','本单点惩罚profile停止，需结构变化非追加时限。',metrics={'partial_state_core_order':38383,'best_legal_S':4986,'fixed_copies':0,'starts':3,'search_CPU_seconds':150.021963},relations=['global_followup_of:ddp-wave3-hexagon-partial-fold-joint'])
add(4,'equitable_global','H9单锚点equitable全局cell MILP',geom,'solver-UNKNOWN',12,5,42343,
    '一个几何绝对点anchor，650genericcells/12H3cells，全部cell常值；无固定域外',
    '一次MILP无incumbent，UNKNOWN；未生成大图。',['33397点逐项检查equitable','非从作者S局部改进模型'],
    'cell常值是实际限制；无不可行证明。','须新的结构/单独授权有限profile，不能写全逐fiber排除。',metrics={'variables':1312,'constraint_rows':2613,'generic_cells':650,'H3_cells':12,'incumbent_returned':False,'solver_status':'UNKNOWN'},relations=['same_geometry_as:ddp-wave4-global-partial-fold'])
add(4,'pencil_source','Dhar后续pencil资料：当前37628/42342原图已得','H9 partial fold with later pencil augmentation','source-recovery',12,5,None,
    'Zenodo23653049及主表实际href原始图；不猜作者未公开性',
    '原图已得，pencil生成邻接、witness及D证明未恢复。',['source直接邻接与主表数据匹配','可用旧点degree余量已恢复'],
    '只有图数据，无可迁移新pencil规则。','需明确原始规则后才能以pencil做生成，不继续泛搜。',metrics={'source_orders':[37628,42342],'source_known_D':5,'actual_D_measured':False})
for slug,delta,base,eligible,cap,miss in [('record37628_single_extension',11,37628,2504,11,115),('record42342_single_extension',12,42342,14396,12,648)]:
    add(4,slug,f'{base}→{base+1}纪录图单点全R4覆盖有限试验','record-graph monotone vertex extension','finite-cover-profile',delta,5,base+1,
        f'全部{eligible}可接旧点R4球；8个起始profile，每个greedy补至{cap}邻居并扫一轮全部坐标',
        f'best仍漏{miss}个new-old目标，独立multi-source覆盖检查MATCH；未展开新图。',
        ['old-old距离不增','单点D5完整条件恰为所选R4球覆盖全部旧点','度预算通过'],
        '覆盖miss不是已展开图的全源无序坏对；有限profile不排其他邻居集。',
        '不增加seed/坐标轮数；8是起始profile数，绝非8邻居上限，firstpin也可替换。',
        metrics={'source_n':base,'source_known_D_upper_bound':5,'coverage_uncovered_vertices':miss,'profiles':8,'neighbor_cap':cap,'eight_means':'initial profiles, not pins cap','all_coordinates_mutable':True,'expanded_graph_generated':False},
        relations=(['degree_variant_of:ddp-wave4-record42342-single-extension'] if delta==11 else []))
add(4,'record37628_global_cover','37628单点全部2504候选的全局覆盖MILP','record-graph monotone vertex extension','solver-UNKNOWN',11,5,37629,
    '全部37628覆盖行、2504二元变量、sum≤11；单solverhandle',
    'CPU硬限终止，solver未返回，无incumbent/不可行证明，UNKNOWN。',
    ['模型含全部候选，不是只8候选','20260765非零覆盖关系已构建'],
    '未找到覆盖不等于UNSAT；无新图/D。','该solverhandle已停不重启；如有新结构证据再独立决定。',metrics={'variables':2504,'coverage_rows':37628,'cardinality_cap':11,'solver_status':'UNKNOWN','incumbent_returned':False,'solver_returned':False,'total_CPU_seconds':59.066855350999994},relations=['global_followup_of:ddp-wave4-record37628-single-extension'])
add(4,'controller364_quotient','H3显式对合商192与所有单调补度障碍',route,'explicit-controller-plus-capacity',12,5,46656,
    '固定H3对合商，保留全部旧边、maximumdegree4的所有simple补边',
    '商图普通D5但exactNB5缺6288有序对；root10对角短障碍排除所有指定加边补度。',
    ['真实置换逐边核对involution','商图simple connected','degree2/3/4共4/36/152点'],
    'ordinary>5坏对0不表示exactNB5通过；不排其他商/删边/一般192控制器。','需改变projection或允许删边，不能补度继续搜。',actual_n=192,actual_delta=4,actual_D=5,bad=0,
    metrics={'edges':362,'exact_NB5_missing_ordered_pairs':6288,'exact_NB5_missing_diagonal':192,'deficit_vertices':40,'deficit_slots':44,'large_lift_generated':False})
add(4,'mizuno_d3_source','Mizuno新版D3边局部矩阵与18个F3模式',route,'source-recovery/word-rank',12,3,837,
    '原30控制器=10K3及6C5，2-(6,3,2)交汇；q4原图1920，q3是另问题',
    '18局部模式/pencil已恢复；原框架good计数给controller n≤31，q3越810只剩31。',
    ['无内部translation','每相邻fiber平面pencil覆盖27','边矩阵可随edge变，不强加通用chart'],
    '30×27=810仅公式，不宣称q3全局证书/图已复现；尚缺31控制器。',
    '应构造真正global31证书，不恢复旧32/33profile。',metrics={'source_controller_n':30,'source_q':4,'source_n':1920,'source_Delta':16,'source_reported_D':3,'q3_naive_n':810,'q3_graph_generated':False,'local_patterns':18,'controller_order_bound':31})
add(4,'controller31_triangle_extension','31三角重叠扩张2760完整指定族',route,'finite-family-exhaustion',12,3,837,
    '345不同triangle/C5点对×8指定插入，2760不同标号quartic图',
    'raw passers0；best controllerD4/15，requiredNB3缺34有序对。',
    ['全部候选simplequartic','完整实际三角计数11/12均未漏'],
    '没有patternCSP或837图；只排这指定插入族。','该族停止，不排一般31控制器。',actual_n=31,actual_delta=4,actual_D=4,bad=15,
    metrics={'candidates':2760,'raw_passers':0,'required_NB3_missing_ordered_pairs':34},relations=['uses_local_rule:ddp-wave4-mizuno-d3-source'])

# Broad targets and exact fixed-source variants remain subordinate rows.
for r in rows:
    if r['id']=='ddp-wave2-lexicographic-products':
        x=json.loads((ROOT/r['primary_source_directory']/'RESULTS.json').read_text())
        r['target_cells']=x['all_cases']
    if r['id']=='ddp-wave3-tits585-batch-extension':
        r['target_cells']=[dict(Delta=d,D=3,savedL=L[d,3]) for d in (10,11,12)]
    if r['id']=='ddp-wave4-pencil-source':
        r['target_cells']=[dict(Delta=d,D=5,savedL=L[d,5]) for d in (11,12)]
    if 'controller' in Path(r['primary_source_directory']).name and r['actual_D'] is not None:
        r['actual_D_scope']='saved_controller_only;hypothetical_lift_not_generated'
    k=r['record_type']
    r['outcome_class']=('positive-local-rule-with-scoped-controller-failures' if r['id']=='ddp-wave3-source-scout' else
                        'solver-UNKNOWN-not-infeasible' if k=='solver-UNKNOWN' else
                        'source-recovery-no-new-graph' if 'source-recovery' in k else
                        'finite-profile-failure-not-whole-family-exclusion' if k in ('finite-profile','finite-cover-profile','finite-profile-partial-state') else
                        'specified-finite-family-exclusion' if k=='finite-family-exhaustion' else
                        'specified-monotone-cone-exclusion-plus-profile' if 'monotone-exclusion' in k else
                        'finite-local-optimum-not-global-exclusion' if k=='finite-local-optimization' else
                        'specified-model-bound-or-exclusion')

notes={str(p.relative_to(ROOT)):p.read_text() for p in (ROOT/'research-wiki').rglob('*.md')}
aggregates=['research-wiki/experiments/ddp-wave3-route-chart-controller-20261027.md',
            'research-wiki/experiments/ddp-wave3-chart-geometry-followup-20261027.md',
            'research-wiki/experiments/ddp-wave4-global-geometry-and-record-cover-20261027.md']
for r in rows:
    slug=Path(r['primary_source_directory']).name
    matches=[p for p,t in notes.items() if p not in aggregates and
             (r['primary_source_directory'] in t or slug in t or slug.replace('_','-') in p)]
    experiments=[p for p in matches if p.startswith('research-wiki/experiments/')]
    ids=[]
    for p in experiments:
        m=re.search(r'^node_id:\s*(.*)$',notes[p],re.M)
        if m:ids.append(m.group(1).strip().strip('"'))
    r['matched_existing_id']=ids[0] if len(ids)==1 else ids or None
    r['wiki']=dict(round_aggregates=[p for p in aggregates if f'wave{r["wave"]}' in p],
                   independent_experiment_nodes_found=experiments,
                   related_nonexperiment_nodes=[p for p in matches if p not in experiments],
                   missing_independent_experiment_node=not bool(experiments),
                   creation_action='reuse-existing-do-not-duplicate' if experiments else 'backfill-needed')

expected={str(d.relative_to(ROOT)) for w in (2,3,4) for d in (ROOT/f'research/ddp/breadth_20261027_wave{w}').iterdir() if d.is_dir() and d.name!='sources'}
assert {r['primary_source_directory'] for r in rows}==expected
result=dict(schema='ddp-wiki-recent-rows-v1',date='2026-10-27',source_waves=[2,3,4],
            threshold_snapshot='context/DD_PORTFOLIO_START_20261026/registry/cases.json',
            row_count=len(rows),rows_are_not_independent_method_count=True,
            wave9='ONGOING_EXCLUDED_FROM_RESULT_AUDIT',rows=rows,
            wiki_gaps=dict(aggregate_notes_read=aggregates,
                           matched_existing=[dict(id=r['id'],matched_existing_id=r['matched_existing_id']) for r in rows if r['matched_existing_id']],
                           missing_independent_row_ids=[r['id'] for r in rows if r['wiki']['missing_independent_experiment_node']],
                           asset_directories_not_experiments=['research/ddp/breadth_20261027_wave2/sources'],
                           correction='record37628/42342 used8 initial profiles and11/12 neighbors, every coordinate mutable; not8pin cap',
                           no_wiki_writes_performed=True))
(OUT/'early_wave_rows.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(rows=len(rows),existing=result['wiki_gaps']['matched_existing'],missing=len(result['wiki_gaps']['missing_independent_row_ids'])),ensure_ascii=False))

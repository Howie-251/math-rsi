"""Read existing experiment evidence only; prepare rows for root's wiki helper."""
from pathlib import Path
import json
import re

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
cases=json.loads((ROOT/'context/DD_PORTFOLIO_START_20261026/registry/cases.json').read_text())['cases']
threshold={(c['degree_cap'],c['diameter_cap']):c['baseline_order'] for c in cases}
rows=[]

def row(w,slug,title,family,kind,delta,D,n,scope,reason,positive,gap,restart,
        actual_n=None,actual_delta=None,actual_D=None,bad=None,metrics=None,relations=None,variants=None):
    d=ROOT/f'research/ddp/breadth_20261027_wave{w}'/slug
    reports=[p for p in d.rglob('*') if p.is_file() and p.name in ('REPORT.md','README.md')]
    # Read every local report and primary result/terminal file; do not execute them.
    for p in reports:p.read_text()
    raw_status={}
    for p in d.glob('*.json'):
        if p.name in ('RESULT.json','RESULTS.json','terminal.json','search_result.json','SCOUT.json'):
            x=json.loads(p.read_text())
            raw_status[p.name]=x.get('status') if isinstance(x,dict) else None
    evidence=[str(p.relative_to(ROOT)) for p in sorted(d.rglob('*')) if p.is_file()
              and p.suffix in ('.md','.json','.edges','.cpp','.py','.txt','.u8','.xz')
              and not re.search(r'hash|sha256|checksum',p.name,re.I)]
    r=dict(id=f'ddp-wave{w}-{slug.replace("_","-")}',title=title,family=family,wave=w,
           record_type=kind,target_Delta=delta,target_D=D,
           savedL=threshold.get((delta,D)) if delta is not None else None,
           n=dict(actual=actual_n,hypothetical=n),
           actual_D=actual_D,actual_D_scope=('saved_explicit_graph' if actual_D is not None else None),
           actual_graph_Delta=actual_delta,ordinary_bad_unordered_pairs=bad,
           ordinary_bad_target_D=(D if bad is not None else None),
           scope=scope,failure_or_result=reason,positive_guarantees=positive,
           unclosed_gap=gap,lesson_and_restart_condition=restart,
           other_metrics=metrics or {},relations=relations or [],variants=variants or [],
           primary_source_directory=str(d.relative_to(ROOT)),source_statuses=raw_status,
           report_paths=[str(p.relative_to(ROOT)) for p in reports],evidence_paths=evidence,
           new_lower_bound=False)
    rows.append(r)
    return r

route='four-label affine route-chart lifts'
row(5,'chart4_quotient_probe','F3⁴通用四步chart：108词满秩',route,'word-rank',12,4,5913,
    '保存F3⁵ chart公共不变线的四维商；局部线性规则，不是整图',
    '108/108约化长度四词rank4；正向结果。',
    ['任意quartic exact-NB4 controller C可条件性给81|C|点、degree12、D≤4'],
    '尚缺≥73点合格controller；不能沿用原72的pencil修补到此quotient chart。',
    '有明确控制器结构与覆盖证书时才值得继续；不要把局部满秩当新下界。',
    metrics={'rank_words_total':108,'rank4_words':108,'minimum_controller_order_to_exceed':73})
row(5,'mizuno_d4_source','Mizuno72宽D4证书恢复及从属容量筛',route,'source-recovery/capacity',12,4,None,
    '原72控制器的I∪R2∪100RG4充分证书；多项从属结构容量检查',
    '原chart支持局部self与12个R2 pencil；exact-NB4不足不否定宽证书。',
    ['原chart18个rank2 planes覆盖self全部81点','12个R2词各自四超平面pencil覆盖81点','100个RG4词满秩'],
    'source证书≠新控制器；quotient chart的self/R2仅33/45，不能混用。',
    '改变容量瓶颈或有新controller证书；原C10父profile已另行终态。',
    metrics={'source_controller_n':72,'source_record_n':5832,'source_reported_D':4,
             'source_exact_NB4_missing_ordered_pairs':720,'source_exact_NB4_missing_diagonal':72},
    variants=[
      {'id':'source8base-exactNB4','kind':'capacity','hypothetical_controller_n':80,'hypothetical_lift_n':6480,'scope':'固定8base的uniform≥10sheet exact-NB4','result':'闭词碰撞至多9状态；只排exact条件，不排宽证书'},
      {'id':'alternative4base-C19','kind':'capacity','hypothetical_controller_n':76,'hypothetical_lift_n':6156,'result':'紧槽18<19；固定模板全部赋值失败','evidence':'alternative76_capacity.json'},
      {'id':'source8base-C10-forced20C4','kind':'capacity','hypothetical_controller_n':80,'hypothetical_lift_n':6480,'result':'六自由强制C4族宽容量9<10；未枚举10^6','evidence':'C4_wide_C10_capacity.json'},
      {'id':'source8base-C10-ninefree','kind':'capacity-pass','hypothetical_controller_n':80,'hypothetical_lift_n':6480,'result':'宽容量最小10，通过必要筛；有限profile另记','evidence':'wide_C10_capacity.json'}])
row(5,'mizuno_d4_C10_wide_search','8base×C10九自由电压宽证书试验',route,'finite-profile',12,4,6480,
    '8个固定starts×25000电压提案；只此九自由父族有限批次',
    '最佳80控制图D5、20个>4无序对；wide还缺160有序对。',
    ['I/R2/100RG4为原chart可复用充分条件','控制图simple quartic connected'],
    '宽证书未闭；最佳控制图D5更给投影提升D≥5真实阻断。',
    '该父profile停止；只有改变真实结构/覆盖条件才值得重启，不追加seed/sheet/base。',
    actual_n=80,actual_delta=4,actual_D=5,bad=20,
    metrics={'wide_missing_representative_targets':16,'wide_missing_ordered_controller_pairs':160,'ordinary_scope':'80controller only;6480 lift not generated','proposals':200000},
    relations=['variant_of:ddp-wave5-mizuno-d4-source'])
row(5,'affine_flag80_trade','AG(2,4) rainbow trade80旗标控制器',route,'finite-prefix-profile',12,4,6480,
    '固定parallelclass、lex前8个rainbow exact-cover、固定B次序与方向',
    '8图宽证书全部失败；最佳图普通D5/208坏对，其他7图未普通BFS。',
    ['self、相邻、NB2端点全部由宽证书覆盖','全部A/B边具有rank-good四步替代'],
    '其他远端controller pairs未覆盖；未排全部rainbow trade。',
    '需要新的全局几何覆盖步骤，不能靠追加exact-cover解/方向/次序。',
    actual_n=80,actual_delta=4,actual_D=5,bad=208,
    metrics={'controllers_generated':8,'best_wide_missing_ordered_pairs':784,'other7_actual_D':None,'large_lift_generated':False},
    relations=['uses_source_certificate:ddp-wave5-mizuno-d4-source'])
row(5,'nb4_base_capacity','两个6点基图×C13的exact-NB4必要筛',route,'capacity',12,4,6318,
    '原144机制6base及octahedron两固定base，所有电压赋值；不排其他base',
    '两base各有slot仅8条具名NB4词，8<13；甚至同base任意uniform≥9fiber均不行。',
    ['具名平行边按真实反走规则处理','完整36槽形式计数'],
    '仅阻断这两base；不是普通D4或一般78controller不存在。',
    '必须更换路径容量不足的结构，换电压/群不补足8条词。',
    metrics={'hypothetical_controller_n':78,'required_sheet_states':13,'witness_word_capacity':8,'graphs_generated':0},
    relations=['uses_chart:ddp-wave5-chart4-quotient-probe'])
row(5,'cayley84_nb4','固定F7⋊₃C12 quartic Cayley控制器完整筛',route,'word-endpoint-exhaustion',12,4,6804,
    '该固定84阶群全部820个simple inverse-closed四元生成集',
    '722组phase容量不足，98组真群词仅到12或44点，无exact-NB4。',
    ['完整inverse-closed组成已覆盖','Cayley左作用使单位根端点代表全部根'],
    '未排其他群或非Cayley84控制器；无普通D测量。',
    '固定群范围关闭，不能仅追加seed/另种S组成。',
    metrics={'hypothetical_controller_n':84,'sets_examined':820,'phase_rejected':722,'true_word_passers':98,'max_exact_NB4_endpoint_count_among_passers':44,'words_per_set':108})
row(5,'bhakar104_wide_screen','固定Bhakar104的宽chart必要筛与唯一短路容量',route,'capacity',12,4,8424,
    '固定104投影、81fiber、每控制边每点至多3邻点且无额外fiber/非投影边',
    '0→32全部≤4walk恰唯一三路，至多27<81；固定投影提升统一不行。',
    ['复用源104 ordinaryD4','raw必要筛先于标号搜索'],
    'raw I/NB2/NB4缺口本身只排充分证书；真正提升排除另由唯一全walk容量证明。',
    '只有改变固定投影或允许不同边机制才可能突破，改标签不够。',
    metrics={'source_n':104,'source_known_D':4,'raw_missing_ordered_pairs':3008,'raw_missing_unordered_pairs':1504,'all_walk_counts_len0_to4':[0,0,0,1,0],'fiber_capacity':27,'required':81})
row(5,'global31_two_bowties','31点两bowtie quartic控制器全局交换',route,'finite-profile',12,3,837,
    '一个架构，3固定fresh starts各200000合法交换；不排全部31图',
    'raw passers=0；最佳controller普通D4/7坏对，required NB3缺18有序对。',
    ['逆一致端口局部规则可由18pattern实现','全图搜索允许外部端口交换'],
    'raw覆盖未过，因此未调用后续pattern CSP，未生成837图。',
    '须有新的raw可行controller架构，不追加同架构起点。',
    actual_n=31,actual_delta=4,actual_D=4,bad=7,
    metrics={'required_NB3_missing_ordered_pairs':18,'raw_passers':0,'legal_proposals':600000,'ordinary_scope':'31controller only'},
    relations=['feeds_tool:ddp-wave5-controller31-pattern-solver'])
row(5,'controller31_pattern_solver','31点edge-local十八模式稀疏证书求解工具',route,'tool',12,3,837,
    '固定31输入的精确pattern模型；本批没有上游raw passer',
    '工具已校准，输入0、MILP调用0、新图0。',
    ['确定性Euler交替2factor与inverseports','reverse路径配对及1116binary稀疏模型已校准'],
    '没有对一般31控制图做UNSAT声明。',
    '仅当明确raw31 passer出现再用工具；不自行生成输入。',
    metrics={'solver_calls':0,'candidates_received':0,'calibration':'original30 actual matrices plus old31 immediate raw rejection'},
    relations=['tool_for:ddp-wave5-global31-two-bowties'])
row(5,'binary_route_chart3','F2³通用三步chart完整枚举与Fano障碍',route,'word-rank',8,3,256,
    '四个固定逆矩阵、一步一个binary参数、全部36约化三词单route满秩',
    '197568规范输入全部失败，最好28/36；Fano商空间短证明统一排除该模型。',
    ['规范空间完备','保存候选36词以全部8参数赋值独立校准'],
    '不排多route、edge-local matrices或一般(8,3)图。',
    '要改变通用单route要求，而非换此空间seed。',
    metrics={'normalized_inputs':197568,'words':36,'best_rank3_words':28,'graphs_generated':0})
row(5,'hs850_branch_lift','HS50×C17固定非均匀分支template', 'HS branch affine lifts','capacity',12,3,850,
    '固定branch位置和大小(4,2,2,1,1)，六参数及同位置同大小常数替换',
    '非邻fiber≤3端点至多12<17，指定整个template不可能D3。',
    ['任意六参数均定义simple12regular','两平移轨道','self及相邻fiber完整覆盖'],
    '不排改变branch位置/大小或其他HS提升。',
    '必须改变非邻fiber容量；不能继续六参数赋值。',
    metrics={'capacity':12,'required_states':17,'parameter_assignments':0,'graphs_generated':0})
row(5,'hs850_orbit10_relaxation','HS850十轨道26参数结构放宽','HS branch affine lifts','finite-profile',12,3,850,
    '一次固定4starts×25000提案的26参数家族；允许突破旧六参阻断',
    '最佳850图D4、26180个>3无序对；有限批次失败，家族仍开放。',
    ['已证10个translationorbits各85','所有slot符号容量≥17'],
    '必要容量通过不保证统一赋值，616代表缺项未闭。',
    '需覆盖结构新进展；本轮不追加batch。',
    actual_n=850,actual_delta=12,actual_D=4,bad=26180,
    metrics={'representative_misses':616,'ordered_bad_pairs':52360,'representative_orbit_factor':85,'proposals':100000},
    relations=['structural_relaxation_of:ddp-wave5-hs850-branch-lift'])
row(5,'fano_split42','Fano独立集拆点42固定完整族','vertex splitting and matching','finite-family-exhaustion',4,3,42,
    'O4中7个Fano点各3种unordered2+2partition及6个固定matching shifts，共13122项',
    '全13122候选无D3；最佳显式图D4、45坏对。',
    ['全部候选simple4regular','旧O4三步覆盖已核对'],
    '未排其他orientation、任意matching或一般42点图。',
    '须改变明确模板，不加相同族参数。',
    actual_n=42,actual_delta=4,actual_D=4,bad=45,metrics={'candidates_examined':13122})

row(5,'heisenberg729_capacity','UT3(F9)五逆对Cayley完整机制容量','Heisenberg central-extension Cayley','capacity',10,3,729,
    'UT3(F9)任意五个inverse generator pairs；全部projection关系weight',
    '投影秩不足4则断连；满秩五类关系的central fiber容量为6/6/6/1/1，均<9。',
    ['121条关系线及1111短词微小检查吻合','形式容量允许独立B_ij，故为真实参数的上界'],
    '不排不同生成元配额、其他群或一般729点图。',
    '需改变central-fiber路径容量；不搜索域参数或seed。',
    metrics={'relation_lines':121,'all_short_words':1111,'maximum_obstructing_fiber_capacity':6,'required_states':9,'parameter_assignments':0,'graphs_generated':0})

row(6,'tensor_product_screen','保存因子的普通categorical tensor产品筛','plain tensor products','parameter/capacity',None,None,None,
    '保存source orders及oddcycles，2/3因子、目标27格；不含未知因子或修补产品',
    '7个数值越线组合全部同步walk/奇偶障碍，D4/D5无数值越线组合。',
    ['n为因子阶乘积，degree为因子degree乘积','完整同步walk条件'],
    '一般产品修补和未知更大因子未排。',
    '只有新因子或改变同步路线规则才值得重启。',
    metrics={'two_factor_rows':90,'three_factor_rows':40,'numerical_exceeders':7,'graphs_generated':0})
row(6,'voltage2008_scout','Loz–Širáň2008 B/D/T/X原规则门槛筛','metacyclic base voltage constructions','source-recovery/parameter-screen',None,None,None,
    '原文给定D3/4/5、degree≤12实例与27格保存门槛比较',
    '无越线；(8,4)=1100仅追平。未试过的完整T(1,1)例D8超范围。',
    ['恢复完整边规则与all ordered base slots voltage coverage条件'],
    '概率引理有存在前提，不能倒置为新参数存在证明。',
    '需有可验证越线参数和覆盖步骤，不能再开群名队列。',
    metrics={'formulas':{'B':'n=mn,degree=s+2l','D':'n=2mn,degree=2l+e','T':'n=3mn,degree=2l+2e','X':'n=4mn,degree=2l+3e'},'untried_source_example':{'n':3243,'Delta':4,'source_reported_D':8}})
row(6,'lamplighter384_capacity','F2⁶⋊C6 shift/toggle完整参数容量','shift/toggle Cayley','capacity',4,5,384,
    '固定四生成元{t,t^-1,a,b}全部delta,u,v，允许t阶12',
    'phase0全部≤5词仅30形式<64，因此整个指定参数族不行。',
    ['完整1365短词校准delta抵消','351返回phase0词'],
    '不排其他ring长度或generator机制。',
    '须改变phase0路径容量，不搜mask。',metrics={'phase0_capacity':30,'required_states':64,'graphs_generated':0})
row(6,'cyclic_cover369','Allwright41(1a)普通C9电压覆盖','ordinary cyclic voltage covers','capacity',4,5,369,
    '固定Allwright41(1a)全部C9电压赋值；树gauge无损',
    '根0 self≤5只有{0,±T,±P}五种形式，5<9；整个固定投影不可能。',
    ['源41实际simple4regularD3已首次检查','ordinary cover保持degree4'],
    '不排其他41底图或非普通cover；未生成369图。',
    '只有改变base闭路容量才值得继续。',metrics={'source_n':41,'source_known_D':3,'capacity':5,'required_states':9,'starts':0,'graphs_generated':0})
row(6,'cyclic_cover1560','120点D3源的普通C13覆盖','ordinary cyclic voltage covers','finite-profile',6,5,1560,
    '固定120源、树gauge、两starts各2000单边电压提案',
    '所有槽容量通过；最佳1560图D6、31655个>5无序对，有限profile失败。',
    ['14400槽符号容量19–49≥13','保留simple6regular'],
    '代表4870缺状态未闭，不等于无序坏对。',
    '本profile停止，不加底图/层数/seed。',
    actual_n=1560,actual_delta=6,actual_D=6,bad=31655,
    metrics={'missing_root_target_sheet_states':4870,'ordered_bad_pairs':63310,'translation_factor':13,'proposals':4000},
    relations=['same_mechanism_as:ddp-wave6-cyclic-cover369'])
row(6,'affine_linker504','AG(2,3)/K7三层504点全局H交换','incidence-design layered linker graphs','finite-profile',6,4,504,
    '固定A/C/CB与任意simple cubic B层H；只2starts×2000合法H交换',
    '最佳504图D6、17073个>4无序对；有限失败不排全部H。',
    ['全部A-A≤4','samepoint A-C≤3及C-C≤4','intersecting-label C-C≤4','图connected独立于H'],
    '跨cell不交标签及B相关远端未闭；best相关端点698<粗必要840。',
    '需要全局端点覆盖新结构，不能把坏对下降当接近D4或加seed。',
    actual_n=504,actual_delta=6,actual_D=6,bad=17073,
    metrics={'proposals':4000,'best_relevant_H_short_endpoint_pairs':698,'coarse_necessary':840,'bad_layers':{'AB':2255,'AC':1572,'BB':3575,'BC':6485,'CC':3186}})
row(6,'metacyclic78_degree5','78阶degree5 Cayley入口文献止损','pure Cayley low-degree D3','literature-scout',5,3,78,
    '所读文献报告pureCayley(5,3)最优60；本地未独立复核原分类证明',
    '拟定16887集合枚举实际0；不是本地新UNSAT。',[],
    '原始最优性证明未在本地重验；一般非Cayley图不受限制。',
    '只有可信反例或机制转到非Cayley才值得继续，不重证旧分类。',metrics={'planned_sets':16887,'actual_sets':0,'literature_reported_pure_Cayley_optimum':60,'graphs_generated':0})
row(6,'record252_mechanism_scout','Rajiv252三轨道原规则来源恢复','A7 three-orbit / cell-design graphs','source-recovery',5,4,None,
    '原文A7及42/105/105轨道配额；缺ZIP原置换数组',
    '原生成元附件未取得，未找新参数；后由wave7组合坐标完整恢复。',
    ['原边表存在且旧检查已完成','AC5/2、BB2、BC3/3配额'],
    '作者原A7具体作用/生成元仍未下载；不能以252数值当本次复现。',
    '已由组合规则绕开附件，不重试下载。',metrics={'known_source_n':252,'source_known_D':4,'new_graphs':0},relations=['completed_by:ddp-wave7-rajiv252-cell-structure'])

row(7,'shortcut_matching_scout','650层结构与加matching降径参数准备','degree-plus-one matching shortcuts','source-recovery/parameter-screen',6,4,650,
    '27格来源和Moore筛后选固定650源；本目录没有matching搜索',
    '恢复500/125/25三层及87800旧D5无序对；full500作用不容许invariant perfectmatching。',
    ['old-old≤4加边后保持','完整必要判定含1或2条matching边'],
    '无明确全对称匹配规则；源远端尚未缩短。',
    '已进入独立shortcut650有限profile；不是另一独立方法。',metrics={'old_D5_unordered_pairs':87800,'matching_search':False},relations=['prepares:ddp-wave7-shortcut650'])
row(7,'shortcut650','固定650源加全局perfectmatching降径','degree-plus-one matching shortcuts','finite-profile',6,4,650,
    '两固定starts各5000合法matching switches；允许打破初态对称性/远距限制',
    '最佳图D5、31918个>4无序对；不排其他全局matching。',
    ['旧1625边全保留','新增325条perfectmatching','全部原≤4点对保持','评分包括两条新匹配边路径'],
    '所有LL/LB/LH/BB/BH/HH层对仍有缺项。',
    '该profile停止，需不同覆盖结构，不追加HH修补或seed。',
    actual_n=650,actual_delta=6,actual_D=5,bad=31918,
    metrics={'old_bad_unordered_pairs':87800,'legal_proposals':10000},relations=['profile_of:ddp-wave7-shortcut-matching-scout'])
row(7,'signed_double340','170源的signed double加vertical matching','signed/branched double covers','capacity',8,3,340,
    '固定170源全部edge signings，全部加fiber内matching',
    '源0→50唯一三路，只给一个sheet；全部signings理论上恰D4。未生成340图。',
    ['原≤2距离对可由一次vertical补另一sheet','原D3保证所有lift点对≤4'],
    '只排固定base签名族，不排一般340图。',
    '必须使唯一三路能分支，换sign不够。',metrics={'proven_all_family_D':4,'ordinary_bad_unordered_lower_bound':10260,'unique3_unordered_source_pairs':5130,'graphs_generated':0})
row(7,'branched_double340_capacity','signed double的matching K2,2分支跟进','signed/branched double covers','capacity',8,3,340,
    '固定170源、branch baseedges构成matching、未覆盖点加vertical、全部signings',
    '必须击中5130条必需唯一路；任意matching权重≤2810，统一排除。',
    ['degree始终8','整数对偶证书不依赖唯一路枚举完备性'],
    '不排其他branch集合/度预算或base。',
    '只有改变matching分支模板才能重启；不能搜matching或sign。',
    metrics={'required_unique_paths':5130,'matching_hit_upper_bound':2810,'ordinary_bad_unordered_lower_bound':4640,'graphs_generated':0},
    relations=['structural_followup_of:ddp-wave7-signed-double340'])
row(7,'rajiv252_cell_structure','Rajiv252七胞元完整组合坐标恢复','A7 three-orbit / cell-design graphs','source-recovery',5,4,None,
    '从旧252边表恢复七K6胞元、35B三角形及pentad/syntheme坐标；不是新record',
    '42+105+105点、630边按组合规则逐边重建完全相等。',
    ['完整V/E生成规则已恢复','固定胞元/三角形模板D4要求胞元≤7'],
    'A7作者原生成元未恢复；该七胞元上限不限制一般(5,4)图。',
    '后续须改变模板的远端覆盖条件，不能只加第八胞元。',metrics={'known_source_n':252,'reconstructed_edges':630,'edge_equality':True,'new_BFS':False},relations=['completes:ddp-wave6-record252-mechanism-scout'])

row(8,'insertion171','170→171：删三条matching边并连六端点','edge subdivision / cooperative vertex insertion','finite-family-exhaustion',7,3,171,
    '固定170源所有三条两两不接旧边，共32846935合法matching',
    '全部新根三球不满，最少仍漏11；指定整族无D3。保存fallbackD4/79不是全族坏对最优。',
    ['所有旧≤2点对保持≤3','S旧二步支配等价新根三步全覆盖','所有候选理论D≤4'],
    '不排其他171图或不同插入结构；formal unique/full候选筛实际调用0。',
    '须改变插入结构，不能继续同三边族；fallback79不能当全族最小坏对。',
    actual_n=171,actual_delta=7,actual_D=4,bad=79,
    metrics={'raw_edge_triples':34930665,'legal_three_edge_matchings':32846935,'newroot_capacity_passers':0,'minimum_newroot_missing':11,'formal_full_candidate_checks':0,'fallback_new_old_bad':11,'fallback_old_old_bad':68,'proven_all_family_D':4})
row(8,'menon1296_screen','Menon16/6/2×K9：方向类保留模板必要筛','incidence-design layered linker graphs','capacity',8,4,1296,
    '固定Menon/K9/B三角形，所有保留四方向类的incidence置换，含每类内任意S9',
    '块外point、不同方向类的B-C必dist≥5；整个指定模板排除D4。',
    ['simple8regular connected','samepoint A-C≤3,C-C≤4','12个AG匹配组正确'],
    '一般S36混类π不受此障碍；一般三色CSP未解且不需要求。',
    '必须混合方向类；已由一般S36profile跟进，不开a CSP。',
    metrics={'ordinary_bad_unordered_lower_bound':155520,'ordered_bad_BC_and_CB_lower_bound':311040,'proven_D_lower_bound':5,'graphs_generated':0,'a_CSP_run':False},relations=['structural_followup_to:ddp-wave6-affine-linker504'])
row(8,'menon1296_unrestricted','Menon1296：96独立S36混类置换有限试验','incidence-design layered linker graphs','finite-profile',8,4,1296,
    '全部96incidence独立S36；两固定seed各1000合法transpositions',
    '最佳图root唯一全1296源确认D5、69737个>4无序对。',
    ['simple8regular connected','samepointAA≤2,AC≤3,CC≤4在最终检查兑现','第一swap完整6066576短walk校准MATCH'],
    '跨point AC及其他层远端尚缺；没有一般S36不可能性结论。',
    '固定profile停止，不加πmoves/seeds/H自由度或类修补。',
    actual_n=1296,actual_delta=8,actual_D=5,bad=69737,
    metrics={'legal_proposals':2000,'bad_layers':{'AA':91,'AC':15253,'AB':2296,'CC':3841,'BC':40661,'BB':7595}},
    relations=['removes_class_obstruction_of:ddp-wave8-menon1296-screen'])
row(8,'cooperative_extension_scout','两相邻新点合作扩张：来源准备未执行','cooperative multi-vertex extension','source-scout',None,5,None,
    '保留旧边、添加a-b、各连至多Delta-1个oldpins；仅恢复完整条件与来源',
    '尚无新profile/MILP/图；全局可行性UNKNOWN，不能登记实际失败。',
    ['old-old距离保持','完整条件R4(A)∪R3(B)=V及对称式','全部spare点R4并集覆盖两源'],
    '有限小pin集合是否同时覆盖未知；旧37628全局单点MILP是UNKNOWN不是UNSAT。',
    '另行授权有限双新点profile，不能把旧8起点误说8邻居预算。',
    metrics={'new_profile_executed':False,'targets':[{'Delta':12,'D':5,'savedL':42342,'hypothetical_n':42344,'pin_cap_each':11},{'Delta':11,'D':5,'savedL':37628,'hypothetical_n':37630,'pin_cap_each':10}]})

# Attach exact broad-screen parameter rows without treating them as new methods.
for r in rows:
    if r['id']=='ddp-wave6-tensor-product-screen':
        x=json.loads((ROOT/r['primary_source_directory']/'RESULTS.json').read_text())
        r['target_cells']=x['all27_target_cells'];r['variants']=x['numerical_exceeders']
    if r['id']=='ddp-wave6-voltage2008-scout':
        r['target_cells']=[dict(Delta=c['degree_cap'],D=c['diameter_cap'],savedL=c['baseline_order']) for c in cases]
    if r['id']=='ddp-wave7-shortcut-matching-scout':
        x=json.loads((ROOT/r['primary_source_directory']/'RESULT.json').read_text())
        r['parameter_screen']=x['parameter_cases'];r['variants']=x['candidates']

# Compare only existing markdown nodes. A related idea is not an independent experiment.
notes={str(p.relative_to(ROOT)):p.read_text() for p in (ROOT/'research-wiki').rglob('*.md')}
aggregates={5:'research-wiki/experiments/ddp-wave5-controller-capacity-20261027.md',
            6:'research-wiki/experiments/ddp-wave6-covers-linker-20261027.md',
            7:'research-wiki/experiments/ddp-wave7-matching-signing-20261027.md'}
for r in rows:
    slug=Path(r['primary_source_directory']).name
    matches=[p for p,t in notes.items() if p not in aggregates.values() and
             (r['primary_source_directory'] in t or slug in t or slug.replace('_','-') in p)]
    experiments=[p for p in matches if p.startswith('research-wiki/experiments/')]
    r['wiki']=dict(round_aggregate=aggregates.get(r['wave']),
                   independent_experiment_nodes_found=experiments,
                   related_nonexperiment_nodes=[p for p in matches if p not in experiments],
                   missing_independent_experiment_node=not bool(experiments),
                   coverage_status=('independent-node-found' if experiments else
                                    'round-aggregate-only-or-indirect' if r['wave'] in aggregates else 'no-wave8-node-found'))
    # Metrics on a controller must never become actual measurements of a hypothetical lift.
    if r['id'] in ('ddp-wave5-global31-two-bowties','ddp-wave5-affine-flag80-trade','ddp-wave5-mizuno-d4-C10-wide-search'):
        r['actual_D_scope']='saved_controller_only;hypothetical_lift_not_generated'
    kind=r['record_type']
    r['outcome_class']=('positive-local-rule' if r['id']=='ddp-wave5-chart4-quotient-probe' else
                        'unexecuted-source-scout' if r['id']=='ddp-wave8-cooperative-extension-scout' else
                        'tool-ready-no-input' if kind=='tool' else
                        'literature-stop-not-local-exclusion' if kind=='literature-scout' else
                        'source-recovery' if 'source-recovery' in kind else
                        'finite-profile-failure-not-whole-family-exclusion' if kind in ('finite-profile','finite-prefix-profile') else
                        'specified-finite-family-exclusion' if kind=='finite-family-exhaustion' else
                        'specified-model-exclusion' if kind in ('capacity','word-rank','word-endpoint-exhaustion') else
                        'saved-parameter-screen-no-qualifying-profile')

result=dict(schema='ddp-wiki-recent-rows-v1',date='2026-10-27',
            threshold_snapshot='context/DD_PORTFOLIO_START_20261026/registry/cases.json',
            source_waves=[5,6,7,8],wave9='ONGOING_EXCLUDED_FROM_RESULT_AUDIT',
            rows_are_not_independent_method_count=True,
            metric_rules=['ordinary_bad_unordered_pairs is an actual explicit-graph measurement only',
                          'NB,wide,ordered,representative and theoretical lower bounds are separate other_metrics fields',
                          'capacity/word-rank/tool/source-only rows have actual_D=null',
                          'finite failure does not exclude the whole unconstrained family',
                          'cooperative scout is unexecuted, not a failed profile'],
            row_count=len(rows),rows=rows,
            wiki_gaps=dict(aggregate_notes_read=list(aggregates.values()),
                           missing_independent_row_ids=[r['id'] for r in rows if r['wiki']['missing_independent_experiment_node']],
                           stale_note={'path':aggregates[7],'issue':'171仍写待执行；实际已完整枚举固定族并保存D4/79 fallback'},
                           wave8_priority=['ddp-wave8-insertion171','ddp-wave8-menon1296-screen','ddp-wave8-menon1296-unrestricted'],
                           no_wiki_writes_performed=True))
(OUT/'recent_rows.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(rows=len(rows),missing_independent_nodes=len(result['wiki_gaps']['missing_independent_row_ids']),
                     existing_independent_matches={r['id']:r['wiki']['independent_experiment_nodes_found'] for r in rows if r['wiki']['independent_experiment_nodes_found']}),ensure_ascii=False))

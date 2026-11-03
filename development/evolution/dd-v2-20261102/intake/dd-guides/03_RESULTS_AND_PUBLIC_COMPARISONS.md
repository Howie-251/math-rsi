# 153张完整图、43组参数：成果与公开比较

**本地已保存153张合法命名图，覆盖43组度数／直径参数，其中47张完成各自具体公式图的Lean证明。当前各参数的最强本地图中，40组超过本篇采用的已核对比较保证：3组直接超过已核对Comellas主表，另37组超过已核对公开构造或已发表方法的具体推论。**

最值得先展示的成果：

- **(16,4)：16,384→16,416，超过已核对主表32点。** 图已完整独立验收，并完成该具体公式图的Lean；本地上一版本16,389→16,416又增加27点。
- **(11,5)：37,628→37,631；(12,5)：42,342→42,402。** 在原度数和直径上限不变的条件下，分别增加3点和60点；后者保存每个整数阶数的合法扩张前缀。
- **D3的20至26度七组最强本地图均高于本轮已定位外部保证。** 本地图依次为3,840、3,984、4,192、4,336、6,160、7,242、7,532点；具体来源和差额见下表，不能把较弱的旧来源当成全球纪录表。
- **(54,3)：56,862点，超过已补强的55,512点公开方法保证1,350点。** 其后55至59度最强本地图形成五个完整端点，各自均有具体Lean。
- **当前最大已接受实例为(98,3)的414,132点图。** 相对本篇已核对的414,050点公开公式保证多82点；86、90、94、98是同一保存规则的不同参数端点，不包装成四种独立新方法。

全球最高阶和最早公开归属尚未统一认证；以下明确写出每项已经超过的对象，并保留确有更大公开构造的反例。

## 1. 这份表在比较什么

参数(Δ,D)表示最大度数至多Δ、直径至多D。构造一张n点合法图，就给出下界`N(Δ,D)≥n`。本项目没有证明这些n是该参数的数学最大阶；“最强本地图”只指已接受本地实例中阶数最多者。

本篇采用当前[153行图目录](../research/graph_catalog.csv)与[43行公开比较CSV](../research/public_comparison_current.csv)，并引用原始证明、验收和已保存的公开审计。成果总数与最新研究状态对应2026-11-02 02:51:52 UTC的本地快照；四个主表值于2026-11-02由根代理实际重读，37,628／42,342／51,417／16,384均未变，[本次主表事实快照](../publication/COMELLAS_CURRENT_20261102.json)随包保存。其他公开比较主要来自2026-11-01的定向核读；根代理另在2026-11-02实际重读Mizuno作者13D5 README，88,452点事实仍在。论文的发表日期、作者图包的发布日期、我们核读的日期分别记录，不把它们混为同一时间。

同一张低于Δ度的公开图也满足最大度至多Δ；例如公开19度2,783点图可以参与20度比较。已发表通用方法的合法数值代入可以作为比较保证，但必须说明该数字是我们代入所得，不能冒充作者原文印出的逐项纪录或作者发布的边表。

## 2. 主表内四组：都超过当前表项，(13,5)另有更大公开图

来源代码M、Z等在第5节给出原文URL、日期和本地审计。

| 参数(Δ,D) | 当前最强本地图 | 本篇主要比较值 | 本地减比较值 | 来源代码 | 可以直接使用的结论 | 具体Lean／本地证据 |
| --- | ---: | ---: | ---: | --- | --- | --- |
| (11,5) | **37,631** | 37,628 | +3 | M | 超过已核对主表 | 未完成；[本地图证据](../research/ddp/more_graphs_20261027/h9_d11_followups/accepted_sequence.json) |
| (12,5) | **42,402** | 42,342 | +60 | M | 超过已核对主表 | 未完成；[本地图证据](../research/ddp/more_graphs_20261027/h9_redei15/production/accepted_sequence.json) |
| (13,5) | **51,457** | 88,452 | -36,995 | Z | 主表仍为51,417；已有公开88,452图超过本地 | 未完成；[本地图证据](../research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/continuation/accepted_sequence.json) |
| (16,4) | **16,416** | 16,384 | +32 | M | 超过已核对主表 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/degree16_plane864/ROOT_FULL_LEAN_DISPOSITION.json) |

(13,5)的40个本地前缀51,418..51,457仍是合法结果，也都超过保存主表51,417。作者Mizuno于2026-10-13已经公开13正则、D5、88,452点图；我们的最强51,457比它少36,995点。这一格应展示为构造轨迹和合法性成果，不能继续标成当前纪录竞争优势。[作者包](https://github.com/rmizuno42/ddp/blob/main/results/degree13-diameter5/README.md)和[本地来源核读](../research/ddp/two_successful_methods_20261101/public_baseline_audit/MIZUNO13_PRIMARY_READOUT.md)保留了这个更正。

D5三组的具体Lean均未完成。37,631有独立全源检查；42,402由60步当前完整图覆盖／度数归纳成立，独立全源代表检查到42,377；51,457由首步检查和40步当前图证书归纳成立。不能把“本项目共有47个具体Lean”迁移到这103个D5前缀，也不能把代表全源检查扩大成每个前缀分别全源检查。

## 3. D3的17至59度：明确外部对手与当前最强本地图

| 参数(Δ,D) | 当前最强本地图 | 本篇主要比较值 | 本地减比较值 | 来源代码 | 可以直接使用的结论 | 具体Lean／本地证据 |
| --- | ---: | ---: | ---: | --- | --- | --- |
| (17,3) | **2,016** | 未核定 | 未核定 | U | 源1920→本地2016；当前公开最强比较缺项 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d16_1920_source_transfer_gate/degree17_plane96/ROOT_GRAPH_RELEASE.json) |
| (20,3) | **3,840** | 2,791 | +1,049 | R＋D | 超过已核对外部构造／公式保证 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/f4_c60_edge_projective/independent_acceptance/SUMMARY.json) |
| (21,3) | **3,984** | 2,928 | +1,056 | P | 超过已核对外部构造／公式保证 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/f4_c60_plane_blocks/independent_acceptance/SUMMARY.json) |
| (22,3) | **4,192** | 3,294 | +898 | P | 超过已核对外部构造／公式保证 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/f4_c60_plane_blocks/independent_acceptance/SUMMARY.json) |
| (23,3) | **4,336** | 3,549 | +787 | P | 超过已核对外部构造／公式保证 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/f4_c60_load_sums_23_24/independent_acceptance/SUMMARY.md) |
| (24,3) | **6,160** | 6,144 | +16 | G | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq35_spread24/RESULT.json) |
| (25,3) | **7,242** | 7,225 | +17 | G | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq44_spread25/ROOT_GRAPH_RELEASE.json) |
| (26,3) | **7,532** | 7,514 | +18 | G＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq44_spread25/ovoid_product26/diagonal_fill_reallocation/ROOT_GRAPH_RELEASE.json) |
| (35,3) | **20,580** | 35,875 | -15,295 | D | 已发表方法可推出更大图，保留为合法构造例 | 未完成；[本地图证据](../research/ddp/two_successful_methods_20261101/f7_c60_d35/independent_acceptance/SUMMARY.json) |
| (54,3) | **56,862** | 55,512 | +1,350 | D12 | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/independent_acceptance/SUMMARY.json) |
| (55,3) | **57,672** | 56,540 | +1,132 | D12 | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/u10_plane_clone_family/independent_acceptance/SUMMARY.json) |
| (56,3) | **58,482** | 57,568 | +914 | D12 | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/u10_plane_clone_family/independent_acceptance/SUMMARY.json) |
| (57,3) | **59,292** | 58,596 | +696 | D12 | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/u10_plane_clone_family/independent_acceptance/SUMMARY.json) |
| (58,3) | **60,102** | 59,624 | +478 | D12 | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/u10_plane_clone_family/independent_acceptance/SUMMARY.json) |
| (59,3) | **60,912** | 60,652 | +260 | D12 | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/affine_field_conditions/r6_schreier78_controller/f9_degree54/u10_plane_clone_family/independent_acceptance/SUMMARY.json) |

20至26度的比较身份分别是：

- **20度：** Rajiv的2026年9月公开实例为最大度19、2,783点；结合已核对一般复制规则，我们的既有审计给出20度至少2,791点。当前3,840超过这一保证1,049点。用户另报3,250点线索仍缺链接／作者／参数绑定；若确认是20度D3，则3,840相对它仍多590点，但本篇没有把未绑定线索升级为已核对基线。该来源若确认，也会提高21度的公开保证，届时应同步更新当前2,928这一对手。
- **21、22度：** PolarStar合法IQ参数分别给2,928、3,294点。**23度：** Brown/ER底图`q=16`和Paley(13)超节点给3,549点。三个数字是所读论文公式在合法参数下的具体保证。
- **24、25度：** Delorme opposite-GQ公开公式在实际GQ(3,5)、GQ(4,4)上分别给6,144、7,225点；本地spread填补图分别增加16、17点。
- **26度：** 从公开7,225点源、17点ovoid、17线spread和Delorme一般诱导子图复制，可以推出7,514点。当前7,532比它多18点；不能只拿7,225作26度对手以夸大幅度。
- **35度：** 20,580是完整合法F7/C60构造例，未做该具体图Lean。Delorme合法`q=32`极性商33度33,825点图本身已满足最大度≤35并大于本地图；再用原文绝对点复制可推35度35,875点。因而这张图没有当前公开竞争优势，但保留了成功生成和路线覆盖的完整研究价值。

54至59度采用补强后的公开对手，而不是早期较弱的55,350／56,375：Delorme的q16 duality-product、spread与一般诱导子图复制，结合审计中明确给出的12点控制器，保证`52,428+(Δ−51)×1,028`点。六个比较值55,512..60,652已分别写入本篇表。这个具体控制器代入和数值组合由本项目审计补齐，原1985论文没有逐项印出这些数字，也未定位对应作者边表。[完整适用性及已执行小证据](../research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101.md)保留原文位置与matching条件。

17度当前本地图2,016是公开1,920源的具体完整扩张，且本地图已完成Lean。现行比较CSV没有核定该格当前最强公开比较值，因此本篇不补造一个“全球原值”；源1,920→本地2,016的具体构造增加96点可以单独展示。

## 4. D3的64至98度：每组最强本地图及公开公式比较

| 参数(Δ,D) | 当前最强本地图 | 本篇主要比较值 | 本地减比较值 | 来源代码 | 可以直接使用的结论 | 具体Lean／本地证据 |
| --- | ---: | ---: | ---: | --- | --- | --- |
| (64,3) | **160,050** | 160,000 | +50 | G | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/independent_acceptance/SUMMARY.json) |
| (65,3) | **161,700** | 161,650 | +50 | G＋C33＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity65_72_family/independent_acceptance/SUMMARY.json) |
| (66,3) | **163,350** | 163,300 | +50 | G＋C33＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity65_72_family/independent_acceptance/SUMMARY.json) |
| (67,3) | **165,000** | 164,950 | +50 | G＋C33＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity65_72_family/independent_acceptance/SUMMARY.json) |
| (68,3) | **166,650** | 166,600 | +50 | G＋C33＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity65_72_family/independent_acceptance/SUMMARY.json) |
| (69,3) | **168,300** | 168,250 | +50 | G＋C33＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity65_72_family/independent_acceptance/SUMMARY.json) |
| (70,3) | **169,950** | 169,900 | +50 | G＋C33＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity65_72_family/independent_acceptance/SUMMARY.json) |
| (71,3) | **171,600** | 171,550 | +50 | G＋C33＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity65_72_family/independent_acceptance/SUMMARY.json) |
| (72,3) | **173,250** | 173,200 | +50 | G＋C33＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity65_72_family/independent_acceptance/SUMMARY.json) |
| (73,3) | **174,900** | 174,850 | +50 | G＋C33＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity73_79_family/independent_acceptance/SUMMARY.json) |
| (74,3) | **176,550** | 176,500 | +50 | G＋C33＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity73_79_family/independent_acceptance/SUMMARY.json) |
| (75,3) | **178,200** | 178,150 | +50 | G＋C33＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity73_79_family/independent_acceptance/SUMMARY.json) |
| (76,3) | **179,850** | 179,800 | +50 | G＋C33＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity73_79_family/independent_acceptance/SUMMARY.json) |
| (77,3) | **181,500** | 181,450 | +50 | G＋C33＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity73_79_family/independent_acceptance/SUMMARY.json) |
| (78,3) | **183,150** | 183,100 | +50 | G＋C33＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity73_79_family/independent_acceptance/SUMMARY.json) |
| (79,3) | **184,800** | 184,750 | +50 | G＋C33＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/opposite_gq77_spread64/published_partial_ovoid33/multiplicity73_79_family/independent_acceptance/SUMMARY.json) |
| (80,3) | **327,744** | 327,680 | +64 | G | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/independent_acceptance/SUMMARY.json) |
| (81,3) | **342,290** | 342,225 | +65 | G | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/independent_acceptance/SUMMARY.json) |
| (82,3) | **346,516** | 346,450 | +66 | Q8＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation/ROOT_GRAPH_RELEASE.json) |
| (83,3) | **350,742** | 350,675 | +67 | Q8＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation/multiplicity2_degree83/ROOT_GRAPH_RELEASE.json) |
| (86,3) | **363,420** | 363,350 | +70 | Q8＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation/multiplicity5_degree86/ROOT_GRAPH_RELEASE.json) |
| (90,3) | **380,324** | 380,250 | +74 | Q8＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation/multiplicity9_degree90/ROOT_GRAPH_RELEASE.json) |
| (94,3) | **397,228** | 397,150 | +78 | Q8＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation/multiplicity13_degree94/ROOT_GRAPH_RELEASE.json) |
| (98,3) | **414,132** | 414,050 | +82 | Q8＋D | 超过已核对公开方法的具体推论 | 已完成；[本地图证据](../research/ddp/two_successful_methods_20261101/retained_edge_transfer/even_q8_gq_source80_81/balanced_full_ovoid_copy82/diagonal_fill_reallocation/multiplicity17_degree98/ROOT_GRAPH_RELEASE.json) |

### 4.1 64至79度：公开P33对手已纳入

64度160,050相对公开opposite-GQ(7,7)的160,000点源增加50点。65至79度使用的较强公开保证是：

```text
160,000 + (Δ−64) × (33×50) = 160,000 + (Δ−64) × 1,650.
```

33来自Cimráková–Fack 2007论文W(7)的实际partial-ovoid构造，50来自所用spread；再结合公开opposite-GQ与Delorme一般复制。原论文Table5中43是上界列，**33才是实际找到的对象大小**。这15个图数是我们组合已发表前提得到的推论，不是2007论文直接发布的D3图表。

现在的P33十五个本地端点161,700..184,800各比相应保证多50点。此前65度161,150和70度166,650已分别低于161,650和169,900；保留它们的边表、证明和Lean作为研究轨迹，但记录竞争成果时采用同参数更新后的161,700和169,950。

本地+50的具体公开归属仍需核对Delorme的JGT1985全文与直接后续：现有审计未取得该文全文；如果相同160,050填补源及相同复制接口已公开，这15个端点相对该更强来源的+50会消失。这里精确保留待核项，不把已经核对的“超过160,000未填补源组合保证”取消，也不把该比较升级成首创认定。[来源原件、33/43辨析与组合条件](../research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md)；[source-fill归属缺口](../research/ddp/two_successful_methods_20261101/public_baseline_audit/SPREAD_FILL_SOURCE_PRIORITY_20261101.md)。

### 4.2 80、81度及82度以上的确定数字

80度的327,744对应已核对GQ(7,9)公开源327,680，加64点；81度342,290对应已核对GQ(8,8)公开源342,225，加65点。82、83、86、90、94、98的公开比较保证统一为已核对q8极性乘积及复制的`4,225Δ`，当前本地图分别多66、67、70、74、78、82点。

这些差额各自有完整具体图和Lean，而不是只列未生成公式。另一条研究轨迹也应保存：82度先得到346,515，再得到346,516；更高degree沿已接受的实际346,516源复制固定角色邻域。若342,290填补源与普通复制已公开，则86/90/94/98相对它的余下增加为5/9/13/17；若相同重分配规则本身也已公开，则需更新其原创性说明。精确比较基线与条件在[84至98有限窗口审计](../research/ddp/two_successful_methods_20261101/public_baseline_audit/Q8_NEW_ROLE_REPLICATION_WINDOW84_98_20261101.md)和[目标归属核查](../research/ddp/two_successful_methods_20261101/public_baseline_audit/DIAGONAL_FILL_REALLOCATION_TARGETED_QUERY_20261101.md)中已有记录，本篇没有新增推导。

## 5. 原文来源、发表日期与本地核读入口

| 来源代码 | 原始来源与发表／公开时间 | 本篇使用范围 | 已保存的本地审计 |
| --- | --- | --- | --- |
| M | [Comellas degree/diameter主表](https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html)；根代理2026-11-02实际重读四格均未变，[本次主表事实快照](../publication/COMELLAS_CURRENT_20261102.json)。[URSA 16D4原构造说明](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html#164)通信日期2026-09-18，记录16,384点及LANL的J. Amarel等作者 | (11,5)、(12,5)、(13,5)保存主表；(16,4)当前16,384对手 | [16D4 packing32公开门](../research/ddp/two_successful_methods_20261101/public_baseline_audit/D16_D4_PACK32_TARGET_20261101.md)；[比较状态](../research/ddp/two_successful_methods_20261101/public_baseline_audit/COMPARISON_AND_NOVELTY_STATUS_20261101.json) |
| Z | [Ryosuke Mizuno公开13D5图包](https://github.com/rmizuno42/ddp/blob/main/results/degree13-diameter5/README.md)，记录2026-10-13加入88,452点、574,938边、13正则D5图；本地2026-11-01核读，根代理2026-11-02再读[作者raw README](https://raw.githubusercontent.com/rmizuno42/ddp/main/results/degree13-diameter5/README.md)仍一致 | 对13D5旧主表的决定性更正 | [原始核读](../research/ddp/two_successful_methods_20261101/public_baseline_audit/MIZUNO13_PRIMARY_READOUT.md)；[图包历史](../research/ddp/two_successful_methods_20261101/public_baseline_audit/MIZUNO13_PACKAGE_HISTORY.json) |
| R | [Rishabh Rajiv，2026年9月公开报告](https://doi.org/10.5281/zenodo.23052995)；其前序[7月报告](https://doi.org/10.5281/zenodo.21180071)、[8月报告](https://doi.org/10.5281/zenodo.22073603)另有较弱历史数值 | 明确发表的19/20度2,783点实例；20度2,791还使用D的一般复制 | [最初来源比较](../research/ddp/two_successful_methods_20261101/public_baseline_audit/REPORT.md)；[20–23专项核读](../research/ddp/two_successful_methods_20261101/public_baseline_audit/D3_CAP20_23_USER_PRIMARY_SEARCH_20261101.md)；[3250人工线索](../research/ddp/two_successful_methods_20261101/public_baseline_audit/USER3250_RECONCILIATION_20261101.md) |
| P | [PolarStar，SPAA 2024，作者原文](https://spcl.inf.ethz.ch/Publications/.pdf/lakhotia-PolarStar.pdf)，Theorem3、Table2、Proposition2/Corollary1及§7.1；本地2026-11-01核读 | Brown/ER与IQ/Paley有效参数保证；本篇21–23度比较 | [23/24补查](../research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE23_24_EXTENSION.md)；[20–23原文声明与后续引用](../research/ddp/two_successful_methods_20261101/public_baseline_audit/D3_PAPER_CLAIMS_FORWARD_CITATIONS_20_23_20261101.md) |
| D | [Charles Delorme，Grands Graphes de Degré et Diamètre Donnés，EJC6(1985),291–302](https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf)，§2、§6、§7、§8；本地已有全文提取 | 极性商、duality-product、spread及一般诱导子图复制；各数值推论须连同适用条件阅读 | [三项被公开方法超过的来源追溯](../research/ddp/two_successful_methods_20261101/public_baseline_audit/SOURCE_TRACE_D3_DOMINATED_NOTE.md)；[原文提取](../research/ddp/two_successful_methods_20261101/public_baseline_audit/delorme1985_primary_text.txt) |
| D12 | D的§§1/6/7/8(a)，结合本地审计明确的标准12点控制器；数值组合核对日期2026-11-01 | 54–59度的1,028Δ保证；这不是另找到的六份作者数值边表 | [补强比较及适用性全文](../research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101.md)；[小控制器实际证书](../research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE54_55_DUALITY_PRODUCT_REPLICATION_20261101_SMALL_CERTIFICATE.json) |
| G | Delorme，Large bipartite graphs with given degree and diameter，JGT9(1985),325–334，[DOI](https://doi.org/10.1002/jgt.3190090304)；本地未取得全文。实际公式依据[Isham–Lakhotia–Monroe–Petrini，arXiv:2608.27253v2 §3.4.2](https://arxiv.org/html/2608.27253v2#S3.SS4.SSS2)，2026年10月v2；本地2026-11-01核读 | opposite-GQ源24/25/64/80/81及后续合法组合 | [25度条件](../research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE25_EXTENSION_20261101.md)；[26度条件](../research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE26_EXTENSION_20261101.md)；[Q8源比较](../research/ddp/two_successful_methods_20261101/public_baseline_audit/Q8_FILLED_SOURCE80_81_GATE_20261101.md) |
| C33 | [Cimráková–Fack，Clique Algorithms for Finding Substructures in Generalized Quadrangles，JCMCC63(2007),129–143](https://combinatorialpress.com/article/jcmcc/Volume%20063/vol-063-paper%2012.pdf#page=12)，§4.3印刷p140 Table5；出版社页日期2007-11-30；本地2026-11-01直接读扫描页 | W(7)实际33点partial ovoid，与50线spread及G/D组合给65–79度保证 | [原文表格与对象核对](../research/ddp/two_successful_methods_20261101/public_baseline_audit/W3_F7_PUBLIC_PARTIAL_OVOID_THRESHOLD25_20261101.md) |
| Q8 | [Isham等2026v2 §7.4／§7.7](https://arxiv.org/html/2608.27253v2#S7.SS7)与D的复制规则；本地2026-11-01核读／合法标量代入 | 已公开q8极性乘积342,225点、81度与4,225中心复制，给82度以上的4,225Δ比较保证 | [82度比较门](../research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE82_BALANCED_FULL_OVOID_COPY_TARGET_GATE_20261101.md)；[83度比较门](../research/ddp/two_successful_methods_20261101/public_baseline_audit/DEGREE83_DIAGONAL_REALLOCATION_K2_TARGET_GATE_20261101.md)；[84–98窗口](../research/ddp/two_successful_methods_20261101/public_baseline_audit/Q8_NEW_ROLE_REPLICATION_WINDOW84_98_20261101.md) |
| U | 17度当前公开最强比较尚缺核定；公开1920源的具体recipe已保存 | 本地2016的生成来源有据，缺的是当前最强公共对手的完成比较 | `research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json`；`research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d16_1920_source_transfer_gate/degree17_plane96/PARAMETERS.json` |

这些source都各有适用范围。例如q16普通Brown合法，不能据此假设特殊GQ极性族也允许q16；P33比较必须用一般诱导子图复制而非独立中心特例。上述本地审计已经记录这些区别，后续提炼时应继承原条件。

## 6. 153、105、43、45、38这些数字怎样同时成立

以最新目录为准：

| 口径 | 数量 | 准确含义 |
| --- | ---: | --- |
| 合法命名图版本 | **153** | 103个早期D5前缀＋原3750实例＋49个后期终图 |
| 参数对 | **43** | 以(最大度数上限,直径上限)去重；同参数允许不同阶数版本 |
| 完整具体Lean实例 | **47** | 各自有具体公式原目标及记录；不是153张全有Lean |
| 超过保存主表的实例 | **105／4参数** | 11D5的3个＋12D5的60个＋13D5的40个＋16D4的2个；这里含13D5历史主表优势 |
| 已知被更大公开构造／已发表方法保证超过的实例 | **43** | 40个13D5前缀＋35D3/20580＋旧65D3/161150＋旧70D3/166650 |
| 上两行重叠 | **40** | 正是13D5的40个前缀：既超过保存主表，也低于作者另行公开的更大图 |
| 保存主表改善集合之外、且不在已知被超过三例中的实例 | **45／38参数** | 状态账本的pending outside集合；并非只有45张图合法，也不是另加45个新纪录 |
| 每参数最强本地图相对本篇比较值呈正差额 | **40／43参数** | 三组主表正优势＋37组外部构造／合法公式正优势；另2组为负，17度一组缺项 |

因此153可以按互不相交的现有账本分为`105＋3＋45`；已知被超过的43中有40已经包含在105里，不能算成`105＋43＋45`。38参数也不能直接加在4个主表参数上冒称覆盖全部43：35度是另一个已知被公开方法超过的参数，65/70则已有更强本地版本留在38集合中。

[当前stage状态](../research/ddp/two_successful_methods_20261101/STAGE_STATE.json)中的顶层153／43／47与CSV一致，但其中历史嵌套graph_catalog字段仍可能保留152／45等旧快照。早期专家包里的104、112、140等计数也只属于各自时间点。用于当前总数时优先读本篇对应的CSV和顶层接受字段，不把历史交付时间线抹掉。

## 7. 同参数非最强实例：保留轨迹，不重复当纪录

| 参数／轨迹 | 需要保留的版本 | 本次成果陈述方式 |
| --- | --- | --- |
| (11,5) | 37,629、37,630、37,631 | 三个合法前缀；最强代表37,631，来自同一连续扩张序列 |
| (12,5) | 42,343..42,402 | 60个合法前缀；最强代表42,402，不说60种新方法 |
| (13,5) | 51,418..51,457 | 40个合法前缀，全部低于公开88,452；是复用与失败比较的研究原料 |
| (16,4) | 16,389→16,416 | 两个已接受具体图；当前代表16,416 |
| (20,3) | 3,750→3,840 | 两张均合法且有各自Lean；当前3840替代3750作为比较代表 |
| (21,3)／(22,3) | 3,900→3,984；4,125→4,192 | 前者原F5复制图保留，后者F4来源图成为当前最强；3900/4125未完成具体Lean |
| (26,3) | 7,531→7,532 | 两张均保留；当前7,532相对7,514保证多18点 |
| (55,3)／(56,3) | 56,943→57,672；57,834→58,482 | 旧端点合法／已有Lean，新的同源块选择给更强代表 |
| (65,3)／(70,3) | 161,150→161,700；166,650→169,950 | 旧版本被公开P33方法保证超过；更新版本各比相应保证多50 |
| (82,3) | 346,515→346,516 | 明确的一点连接重分配改进；更高multiplicity共享后者作为固定源 |

原图参数、完整生成器、字面绑定、验收和形式化记录应与这些轨迹一起保留。这个表解释已接受结果怎样更新，不增加新的图、参数、方法或纪录数量。

## 8. 贡献归属与交付中的亮点措辞

- D5源图继承Dharunish Yugeswardeenoo；H(9)对偶／部分折叠基础继承Rishabh Rajiv。本项目具体贡献是保存的新邻域、锚点／守卫、阻塞集选择和完整扩张序列。
- C30与通用仿射route-chart框架继承Ryosuke Mizuno；公开1920、15552源也保留作者来源。本项目记录具体F5、F4、F9字面参数、共同相容选择、块负载实现和完整实例。
- C60、三base Schreier等控制器来源保留Bhakar／f4t4nt作者仓库，不把既有控制器或提升框架写成本项目发明。
- 经典有限域、广义四边形、Payne导出、spread、ovoid、Delorme opposite-product及复制理论均保留原作者归属；P33部分明确标记对已发表33点对象的复现。
- 本地same-cap flag填补、具体连接重分配和新实例是可被逐项阅读的候选增量，其精确公开归属问题与图的合法性、具体Lean状态分别记录。

推荐直接使用的发布描述是：“我们保存了153张完整合法图，覆盖43组参数，47张有具体Lean；当前最强结果有3组超过已核对主表，另37组超过已核对外部构造或已发表方法的具体保证。结果、完整图源码与研究轨迹均可追溯。”随后展示本篇对应的数字和来源，即可把已完成成果放在最前面。

本篇只是根据现有目录和既有公开审计整理交付说明，没有重新全网检索、推导新的比较下界或运行图／BFS／Lean计算。

# 旧 n61 `[3,3]` 完整 RAW 记录的证据边界

2026-10-18。响应新旧 n61 有界对齐要求，仅检查旧 `[3,3]` 四轨道的直接
分类、源码、输入说明及运行记录。没有运行旧 SAT、重新生成旧 CNF、检查
旧证明证书或启动 Lean；没有审计其他阶数。

**可继承的结论：三角形自由根、异常父数轮廓 `[3,3]` 的四个轨道都有
实际 solver-level RAW UNSAT 记录。不能继承为独立认证排除。**
四轨道的覆盖可直接证明；其计算排除仍缺证明证书，而且两版实际运行所
引用的八份 CNF 原文件目前均不在对应保存位置。

## 路径约定与实际找到的材料

以下相对路径均以本文件所在目录 `proofs/dd82/n61/` 为起点：

- `A = ../../../context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/`
- `O = ../../../../mathagent/degree_diameter_sat/`
- `F2 = O/results/n61_v2/formulas/n61_root_v2_u3_c1row_20260824/baseline_complete/`
- `R1 = O/results/n61_all_templates/runs/20260816T140107Z/`
- `R2 = O/results/n61_v2/n61_root_v2_u3_c1row_20260824/baseline_complete/runs/baseline_12h_20260824T105452Z/`

已完整阅读 [vanilla报告](../../../context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/materials/n61/vanilla_baseline.md)
和 [Iteration 1报告](../../../context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/materials/n61/20260825_iteration1.md)。
前者L192–205、后者L347–354给出原出处。精选包的
[README](../../../context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/README.md)
L21–31明确说不是完整可复现发行版；
[code导航](../../../context/dd82/archive/N8_AI_FOR_MATH_LLM_SAT_REVIEW_20260929/code/README.md)
L74说明包内 n61 源码来自较晚 CP02，不是这两轮原始生成器。

只读检查原 ZIP 的成员列表也确认没有收录 V1/V2 生成器、两轮原始日志或
本问题证书。但是原报告引用的相邻 `mathagent` 工程仍可读取，实际保留了
两版生成器、manifest、统计、运行状态和日志，V2还保留固定图与变量映射。
因此“精选档案未收录”不能写成“这些源码与日志已经丢失”。

## `[3,3]` 恰为四个完整轨道

旧根记为 r，X=N(r)，|X|=8，Y=V\N[r]，|Y|=52；本支 H=G[X]=∅。
恰有两个**不同的Y顶点**具有三个父点，其父集分别为 S、T；S=T允许，
表示两个顶点有相同父集，并非把它们合并。

两个三元子集在 S8 下的轨道完全由 k=|S∩T| 决定。给定 k，分别双射
S∩T、S\T、T\S、X\(S∪T) 即得到任意两对父集之间的置换；k可以为
3、2、1、0，且其并集最多6点，四种均合法。因此无需信任整个60模板
枚举，就可单独确认本支恰有以下四个完整轨道：

| 原生成器ID | 两异常父集（X标签1..8） | k |
| --- | --- | ---: |
| t0_05_p3_3 | 123；123 | 3 |
| t0_06_p3_3 | 123；124 | 2 |
| t0_07_p3_3 | 123；145 | 1 |
| t0_08_p3_3 | 123；456 | 0 |

这四项直接在 [V1生成器](../../../../mathagent/degree_diameter_sat/n61_all_templates_cnf.py)
L76–80（内部用0..7标签）。每个 x∈X 的单父纤维大小被八正则性强制为
`7−1[x∈S]−1[x∈T]`，合计50个普通Y点，再加两个异常点即52点；
同文件L228–248正是该构造。其余1326条Y内部边全部为变量，不固定
异常点是否邻接、不固定其共同邻居或其他Y内部结构。

全局60清单的实际数量也与两篇报告一致：t=0各轮廓1、3、4、14、23个，
t=1各轮廓3、12个，总计45+15=60。V1的
[manifest](../../../../mathagent/degree_diameter_sat/results/n61_all_templates/manifest.jsonl)
共有60条，四个本支条目在L5–8；V2的
[universe_manifest](../../../../mathagent/degree_diameter_sat/results/n61_v2/formulas/n61_root_v2_u3_c1row_20260824/baseline_complete/universe_manifest.json)
L4–6保留60总域、55活动域。这里没有重新证明其余轮廓的全部分类。

不同清单不能仅按数字ID合并。
[V2生成器](../../../../mathagent/degree_diameter_sat/n61_all_templates_cnf_v2.py)
L62–87对固定X边及异常父集**多重集**作完整S8规范化，L112–122给出
保存的结构键。本次按结构键确认上述四例，而非推测ID顺序。

## 实际约束及规范排序是否另加假设

V1源码L405–455约束Y内部精确度、所有尚未覆盖的X–Y和Y–Y点对；
L291–362、L457–471加入由每点缺陷预算4推出的纤维内部边上界。
旧覆盖辅助位只有“见证为真则两条边为真”的方向，这足够用于存在性OR；
它们在V1并未被误作精确共同邻居计数。

唯一额外排序是V1 L473–489：在每个**同父单点纤维**内部，按该顶点
到固定异常Y顶点的邻接比特签名降序排列。每个纤维内的点对根和X具有
相同固定邻接，且全部Y边仍自由；在该纤维内按签名重标即可满足排序，
不改变图或父集。不同纤维可以独立排序。这保留至少一个代表，不是
固定跨纤维关联或预先选定异常邻域。四例保存stats均记 `symmetry_break=true`。

V2的实际 [active_manifest](../../../../mathagent/degree_diameter_sat/results/n61_v2/formulas/n61_root_v2_u3_c1row_20260824/baseline_complete/active_manifest.jsonl)
L4–7全部记 `mode=baseline_complete`，只启用：

1. U1：每个X点的精确缺陷行等式；V2源码L282–345。
2. U2：`sum_z E_yz (|P(y)∩P(z)|+|P(z)|−1) ≤ 5−|P(y)|`，本支根无三角；
   V2源码L347–368。它由Y点的精确局部余量恒等式丢弃非负项而来，
   原 [理论交付](../../../../mathagent/CODEX_N61_CONSOLIDATED_THEORY_SAT_HANDOFF.md)L198–258。
3. U3：相邻点共同邻居≤2，非邻点共同邻居≤5；V2源码L370–411。
   这些是61点、八正则、直径2的局部预算后果。V2 L249–257为实际计数
   增加双向AND定义，没有继续使用V1单向见证作精确计数。

四例的 `enabled_constraints` 都没有 `c1_nonedge_common_cap`、
`c1_root_row_spectral_table`。源码L173–174、L191–194、L384–385明确
将这些额外条件隔离到 `c1_research`；实际运行summary L28也记
`conditional_result=false`。因此本次 `[3,3]` 四例RAW不附带缺陷支撑
连通性 c=1、谱表、I12H 或 noO 假设。

这是对本问题承重范围与假设的有界核对，不宣称重新完成两版全部辅助
计数器审计，也不能以当前同版本源码替代已经缺失的当次CNF原件。

## 实际运行结果，不能把RAW提升为证书

V1在四例中只关闭05、06、08，07到期；见
[progress.json](../../../../mathagent/degree_diameter_sat/results/n61_all_templates/progress.json)L59–94。
V2补上07，并重复得到其余三例RAW；见
[summary.json](../../../../mathagent/degree_diameter_sat/results/n61_v2/n61_root_v2_u3_c1row_20260824/baseline_complete/runs/baseline_12h_20260824T105452Z/summary.json)L103–196。

| ID | V1实际结局／决定性墙钟秒 | V2变量／子句（保存metadata） | V2实际结局／墙钟秒 |
| --- | --- | --- | --- |
| t0_05_p3_3 | raw UNSAT／1182.979 | 598545／1563479 | raw_unsat／822.694 |
| t0_06_p3_3 | raw UNSAT／22988.709 | 598551／1562567 | raw_unsat／4212.021 |
| t0_07_p3_3 | DEADLINE，非UNSAT | 598556／1561653 | raw_unsat／5631.030 |
| t0_08_p3_3 | raw UNSAT／9471.652 | 598560／1560738 | raw_unsat／192.947 |

时间来自状态中的 `wall_seconds`，不是本次实测CPU；V1决定性尝试不含
此前超时尝试。V1原state的四段分别为L125–173、174–208、209–261、
262–298，路径为 `R1/state.json`。

实际终态日志已读取：

| 轨道 | V2日志（路径相对本文件） | 终态行 |
| --- | --- | ---: |
| 05 | [solver.log](../../../../mathagent/degree_diameter_sat/results/n61_v2/n61_root_v2_u3_c1row_20260824/baseline_complete/runs/baseline_12h_20260824T105452Z/tasks/t0_05_p3_3/attempt_01/solver.log) | L1 |
| 06 | [solver.log](../../../../mathagent/degree_diameter_sat/results/n61_v2/n61_root_v2_u3_c1row_20260824/baseline_complete/runs/baseline_12h_20260824T105452Z/tasks/t0_06_p3_3/attempt_01/solver.log) | L1 |
| 07 | [solver.log](../../../../mathagent/degree_diameter_sat/results/n61_v2/n61_root_v2_u3_c1row_20260824/baseline_complete/runs/baseline_12h_20260824T105452Z/tasks/t0_07_p3_3/attempt_01/solver.log) | L1 |
| 08 | [solver.log](../../../../mathagent/degree_diameter_sat/results/n61_v2/n61_root_v2_u3_c1row_20260824/baseline_complete/runs/baseline_12h_20260824T105452Z/tasks/t0_08_p3_3/attempt_01/solver.log) | L1 |

四行均为 `s UNSATISFIABLE`，四份 `R2/cases/<ID>.json` 的L36均为
`proof:null`、L39均为 `return_code:20`、L42均为 `raw_unsat`。
例如 [07 case](../../../../mathagent/degree_diameter_sat/results/n61_v2/n61_root_v2_u3_c1row_20260824/baseline_complete/runs/baseline_12h_20260824T105452Z/cases/t0_07_p3_3.json)L30–42
还保留当次solver命令及输入路径。四个attempt目录都只有solver.log。

V1决定性日志也确实存在：`R1/logs/t0_05_p3_3/attempt_03_ae_kissat_mab.log`
L1、`R1/logs/t0_06_p3_3/attempt_02_ae_kissat_mab.log` L1、
`R1/logs/t0_08_p3_3/attempt_02_cadical_unsat.log` L7062均为UNSAT。
最后一份L14–17还打印旧输入路径、88398变量／224086子句，L7127打印exit20。

V1队列仅凭exit20写入 `UNSAT`（
[队列源码](../../../../mathagent/degree_diameter_sat/run55/run_n61_template_queue.py)L332–334），
其名称不代表认证。V2明确分级：
[队列源码](../../../../mathagent/degree_diameter_sat/run55/run_n61_v2_queue.py)L551–574
先检查exit20和终态行，只有另行证明检查成功才转为 `certified_unsat`。
本次 `R2/state.json` L18的 `proof_checker:null`，summary L18–24记
17 raw、0 certified、38 timeout，与两篇报告的证据说明一致。

## 保存缺口与可继承边界

已逐项只读检查以下八个路径，原文件均不存在；在这两个直接结果子树中
按四个case名查找也未找到 `.cnf.gz/.xz` 或证明替代件：

- `O/results/n61_all_templates/cnf/{t0_05_p3_3,t0_06_p3_3,t0_07_p3_3,t0_08_p3_3}.cnf`
- `F2/cnf/{t0_05_p3_3,t0_06_p3_3,t0_07_p3_3,t0_08_p3_3}.cnf`

这与“运行从未发生”不同：manifest、stats、命令、exit20、实际终态日志
共同支持已发生RAW运行；但缺失的历史CNF和从未生成的证明，阻止把它
升级为对保存输入独立检查的UNSAT证据。V2每例 `stats/maps/fixed` 文件
仍在，生成器版本标签也与运行相符；本次未发现直接运行目录内冻结的
生成器副本，不将当前工程源码声称为逐字节确认的历史快照。
该缺口影响历史计算证据的保真核验；四轨道的数学覆盖仍由上面的集合
置换论证独立成立，纤维排序也保留合法代表。

另按已完整读过的两份报告核对相邻旧范围：t0 `[4,2]` 的三个轨道均已有
V1 RAW，V2也重复RAW（vanilla L108–110；Iteration 1 L198–200）；
t0 `[5]` 早先RAW，Iteration 1已列入无条件数学排除（L78–87，尤其L80）。
这分别是根代理所述 B=3、B=4 点对转根后应比对的范围；因此V3的 B≤2
不能笼统宣传为首次得到所有相应旧范围的排除迹象，其新增可以在更强的
数学／独立证书证据上。这里未使用 t1 `[3]` 去对应 B=3，也未进一步
审计这些相邻范围的全部历史运行。

可以据此说“旧 `[3,3]` 完整族已有四轨道RAW结果，新的数学映射若落在
此族，就与旧计算范围重叠”。不能据此说“该族已获独立证书排除”，
不能把旧RAW作为新引理的已证前提，也不能越过选根映射扩展为整个61阶
排除。数学映射与V3新结果的关系由本次独立数学对齐文件说明。

没有恢复旧搜索或提出自动认证重跑；本文件保存的是当前实际证据等级。

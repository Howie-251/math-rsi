# 读门结论：实际是 incidence + 两侧任意完美匹配，五个旧窗口都未解

实际 source 已完整缓存：W(3,3) 的40 points/40 lines，160 incidence edges，4 regular；labels 为 points0..39、lines40..79。`geometry.json` 保存有序点坐标、每线的4个点和每点的4条线；`incidence.edges` 是完整 source。旧 `run.py` 明确保全160条 incidence，另在 points、lines 各加20边 perfect matching，故目标确为80/200、5 regular，而非猜测的跨侧补边模型。源 incidence D4 与 GQ 数据继承，本轮不生成几何或验证直径。

原 unrestricted 域是两侧全部 unordered pairs 的1560个二元变量、80个 matching degree equalities、1080个 exact far-cover rows。跨侧点对原≤3，同侧 collinear pairs 原≤2，待补的是每侧540个 noncollinear pairs；每条覆盖式41变量，own-first/last合25、opposite relay16。matching-only的多步只会沿唯一 mate 往返，所以这些路线式在 matching 约束下确为 D3 充要条件。

旧史不只“45秒 UNKNOWN”：原15秒MILP无 incumbent；随后45秒配置窗口在 worker37CPU后被杀、未返回 solver result；再有 unrestricted CNF、girth5 CNF、girth5加localbudget CNF 各30秒，全部 UNKNOWN。girth5两轮只限制 noncollinear P、nonintersecting Q、无 mixed rectangles，不得用于关闭 unrestricted 原族。第五轮增加的是已有 valid a_x<=3 的传播编码，没有改变其 girth5 可行图域。

**没有旧 augmented candidate、failed matching pair 或实际 bad-pair histogram 可继承。** 五轮 incumbent 都为0、BFS都为0；1080 far cover rows 是结构目标类别，solver conflicts/decisions 不是图坏点对。完整路径和各窗口预算/状态列在 `HISTORY_SOURCE_GATE.json`，不能将任何 UNKNOWN 登记为严格 NO。

可复用的 S/C 接口不用新 field：从已有 `lines`、`point_incident_lines` 可得到闭 C 和 S=C\{self}；原 `model.json` 已有全部 far pair 的 own/relay variable supports，old `overlap_cuts.json` 有3120支持集，`COUNTERS.json` 有每个 S 的54近邻 matching inputs。`geometry.json` 本身只序列化 C 的大小/交大小，没有偷偷声称它存了完整 C 矩阵。restricted DIMACS map 也已保存，导出图时 line-side 才统一加40。

最初读门的 a_0=3 局部分割正假设已登记、未执行。root 后续选择一个新生成约束：两 matching 均保持同一个 free order5/C5 collineation。按指定 node 与原始 model/code 的有限检索，五窗均没有 symmetry constraints，未定位此 C5 受限族的旧试验或 strict NO。当前 geometry 有实际 B form、40 pointvectors、40 line4sets 可复用；没有定位已存 order5 matrix/permutations 或 Sp4 generators。因此下一步实际缺的是一个 concrete symplectic A 及其在原有 labels 上的点/线作用绑定，不能将预期 orbit 个数当成已完成数据。

本读门没有构造 A、压缩模型或求解，也不新建 canonical Wiki 节点、不变更旧模型/结果；此处仅作恢复入口，原方法节点仍唯一。下一批如获授权，须以 C5 受限域的实际兼容性预测为准，不自动续旧 timer，也不同时派发原 a_0=3 局部预测。

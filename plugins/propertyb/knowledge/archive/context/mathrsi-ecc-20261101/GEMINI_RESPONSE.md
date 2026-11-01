# 第二领域 ECC 对 `mathrsi-base` + 插件架构的检验与修订建议

> **本轮实际只读核查文件（未运行程序、未修改文件）：**
> [BRIEF.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/BRIEF.md)、[MATH_RSI_DESIGN.md](file:///Users/rfy_naiveai/Desktop/aris4math/MATH_RSI_DESIGN.md)、[00_README.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/00_README.md)、[01_PACKAGE_SCOPE.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/01_PACKAGE_SCOPE.md)、[FORMAL_SPEC_45_11_17.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/FORMAL_SPEC_45_11_17.md)、[ECC_LESSONS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/research-wiki/ECC_LESSONS.md)、[NONEXISTENCE_43_10_17.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/results/NONEXISTENCE_43_10_17.md)、[ECC_45_11_17_PROGRESS_20261013.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/ECC_45_11_17_PROGRESS_20261013.md)、[n37_pair_swap_compression/REPORT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/work/goal-45-11-17-20261007/wave6/n37_pair_swap_compression/REPORT.md)（注：交流包未收录的约 1.68GB 拒绝流及部分历史子目录属已知打包边界，涉及未完成分支的端到端总成本记为未知）。

---

### 一、 哪些原设计获两领域共同证据支持，哪些必须修订？

**获共同证据支持、予以保留的设计：**
1. **三层拆分与状态隔离**：`mathrsi-base`（流程/义务图/证据范围/资源调度）、领域插件（`mathrsi-propertyB` / `mathrsi-ecc`）与单题工作区（如 `[43,10,17]` 与 `[45,11,17]` 各自独立的矩阵库与分支状态）边界清晰。例如同批 172 个 `[40,7,18]` 母码在两题中承担不同的扩张维数（44 位 10 维 vs. 46 位 11 维，见 [ECC_45_11_17_PROGRESS_20261013.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/ECC_45_11_17_PROGRESS_20261013.md#L39)），插件保留母码与通用算法，工作区隔离本题扩张义务。
2. **正确性与完备性分验**：两领域均证实“留下的候选正确”不等于“该留下的没有遗漏”，且模型审阅、双实现复算与数学覆盖各自承担正交义务（[ECC_LESSONS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/research-wiki/ECC_LESSONS.md#L24-L27)、[MATH_RSI_DESIGN.md](file:///Users/rfy_naiveai/Desktop/aris4math/MATH_RSI_DESIGN.md#L17-L19)）。

**ECC 暴露的原设计局限与五项实质修订：**

1. **区分目标的逻辑量词与验证器作用，废除笼统的单一 `PASS`**：
   Property B 下界本质是全称命题（$\forall H$ 可二染），容易让 `base` 默认“必须完成全局分类覆盖”。而 `[45,11,17]` 是未决的**存在/不存在二分问题**（[FORMAL_SPEC_45_11_17.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/FORMAL_SPEC_45_11_17.md#L7-L15)）：
   * **存在性构造（$\exists G$）**：只需找到**一个**秩 11 的 $11\times 45$ 二元矩阵并通过全部 2047 个非零消息的重量检验（$\ge 17$）即可直接终结全题，**完全不需要全局分类或无损归约证明**。
   * **全称不存在性（$\neg\exists G$）**：并不存在现成的“全域自动 verifier”，必须结合无损归约推导、外部定理进口（如 `[43,10,17]` 依赖 E1/E2，见 [NONEXISTENCE_43_10_17.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/results/NONEXISTENCE_43_10_17.md#L5)）与完备分支拒绝证书。
   * **固定范围排除与条件引理**：排除单个准循环 `[45,10,18]` 母码的 $2^{34}$ 奇陪集（约 139 CPU 秒，见 [FORMAL_SPEC_45_11_17.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/FORMAL_SPEC_45_11_17.md#L46)）或算完标准六尾 172 例（尚待整支证明组合与正式审计，见 [ECC_45_11_17_PROGRESS_20261013.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/ECC_45_11_17_PROGRESS_20261013.md#L159-L172)），只能记为**局部域排除**，不能用同一个 `PASS` 冒充全题闭合。

2. **归约接口必须标明逻辑方向，并保存同步坐标/基运输信息**：
   `base` 的桥接契约须区分四类变换：① **双向等价**（如 `[45,11,>=17]` $\iff$ 偶 `[46,11,>=18]`，但构造成功仍须显式穿孔回 $11\times 45$ 矩阵复验，见 [FORMAL_SPEC_45_11_17.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/FORMAL_SPEC_45_11_17.md#L24)、[L32](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/FORMAL_SPEC_45_11_17.md#L32)）；② **必要覆盖**（用于排除，须防止跨分支混用条件，如 $d_4=36$ 的剪枝不能搬入 $d_4=35$ 的 `Q42`，见 [ECC_45_11_17_PROGRESS_20261013.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/ECC_45_11_17_PROGRESS_20261013.md#L251)）；③ **充分/启发式子族**（如准循环、固定母码或由 172 类缩短补出的 1373 个偶 39/6 母码，不能用于全局排除，但完全合法作为构造捷径，见 [ECC_LESSONS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/research-wiki/ECC_LESSONS.md#L55-L57)）。同时，当涉及多行扩张或模块拼接时，**坐标置换与基变换必须同步作用于所有相关对象**，后续规范化只能在稳定子内进行（如九尾先规范 $x$，再用 $D_{(p=0)}$ 稳定子规范 $y$ 并保存 `swap_mask`，见 [n37_pair_swap_compression/REPORT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/work/goal-45-11-17-20261007/wave6/n37_pair_swap_compression/REPORT.md#L26-L28)；单模块规范代表也不能直接叠加冒充共同嵌入覆盖，见 [ECC_LESSONS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/research-wiki/ECC_LESSONS.md#L50)）。

3. **彻底解耦“启发式候选发现”与“严格结果核验”**：
   完备性要求只施加在最终结论所依赖的验证环节，绝不要求每个探索程序自证完备：
   * `[43,10,17]` 中 172 个母码代表可由任意启发式手段找出，只要独立验证其满支撑、秩、距离与两两不等价，再结合文献 E2“至多 172 类”即获得严格完备覆盖（[NONEXISTENCE_43_10_17.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/results/NONEXISTENCE_43_10_17.md#L20)）。
   * `Kohnert48` 随机搜出的 39 个低权子空间，一旦经独立程序核实为全部 1128 种两位缩短各提供 15 个低权字，即构成固定父码的严格排除证书；同理，求解器 UNSAT 转成 51,028 步 LRAT 证明后只需独立检查器重放（[ECC_LESSONS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/research-wiki/ECC_LESSONS.md#L48-L49)）。

4. **按全链路与联合自由度核算真实成本，警惕“小母码数”与“微秒内核”幻觉**：
   * **不把单步内核耗时当端到端成本**：九尾 `from40_class5` 实例将 $7,854,553,165,656$ 原始配对经标签桶（$3,413,228,288$）与 7 对交换群取商压至 $26,665,846$ 个代表，307 块扫描进程仅 $0.473743$ CPU 秒（其中纯查询仅 $0.061671$ 秒），恢复并验距 $17,403$ 份 `[42,8,18]` 矩阵耗时 $2.088232$ CPU 秒；但这不含前置 $F_M$（$3,963,472$ 项）生成与推导实现，且其 128 样本同构分类评测得 127 类、线性外推全分类需约 $64.02$ CPU 秒（超 40 秒门槛而依规停算），后续 $Q\to E$ 扩张与其余母码成本仍未知，更不能把 7 对重复列的 128 倍压缩外推到少重复对母码（[n37_pair_swap_compression/REPORT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/work/goal-45-11-17-20261007/wave6/n37_pair_swap_compression/REPORT.md#L13-L45)、[ECC_45_11_17_PROGRESS_20261013.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/ECC_45_11_17_PROGRESS_20261013.md#L215-L220)）。
   * **不把母码少当成联合搜索便宜**：十一尾虽仅剩 $3\text{ 核心}\times 3\text{ 尾型}=9$ 个入口、单步颜色表仅 $14,606$ 项，但七个新增头的 127 个非零组合须同时满足距离界（每核危险头三空间仍约 $40.92$ 亿），9 个局部试验（共 $18,874,368$ 输入）全非空即果断停算（[ECC_LESSONS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/research-wiki/ECC_LESSONS.md#L80-L89)、[ECC_45_11_17_PROGRESS_20261013.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/ECC_45_11_17_PROGRESS_20261013.md#L225-L232)）。反之，当完整有限域经位并行或共享集合压缩后已可实算完（如标准六尾最后 162 例用共享 $P_a/Q_{a,b}$ 在约 11.84 CPU 小时 / 4.53 墙钟小时算完，见 [ECC_45_11_17_PROGRESS_20261013.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/ECC_45_11_17_PROGRESS_20261013.md#L149-L170)），应直接算完，不必强求纯解析证明。

5. **“同一实际对象的共同约束”值得升为 `base` 通用诊断提示，但具体代数/组合机制留在插件（且不夸大跨学科普适性）**：
   * **两领域共同证据**：无论是 Property B 中同一超图 $H$ 的跨位置共同坏对与共享外点列守恒，还是 ECC 中同一目标码要求 $a,b,a+b$ 同属合法集（六尾仿射立方体 $x+U\subseteq F$、九尾二维线 $\{B,C,B+C\}\subseteq F_M$、十一尾 127 个线性组合及 `Q41` 多个 $35/4$ 核心共享同一头矩阵，见 [ECC_LESSONS.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/mathrsi-ecc-20261101/sources/ecc/research-wiki/ECC_LESSONS.md#L73-L75)），失败根源都是**“单分量边际可行，但丢失了同一底层对象的联合耦合与同步变换”**。将这一检查升为 `base` 的通用诊断提示有坚实依据。
   * **诚实范围边界**：$\mathbb{F}_2$ 线性子空间闭合、对偶广义重量 $d_r(E)\leftrightarrow d_t(E^\perp)$、重复列交换群留在 `mathrsi-ecc`；度数超额与排列概率留在 `mathrsi-propertyB`。且两项目均属**离散数学**，由此提炼的接口目前仍是架构设计建议，不能宣称已在连续分析或几何领域验证了通用性。

---

### 二、 可直接纳入 `MATH_RSI_DESIGN.md` 成稿的跨领域比较与契约补充

> **跨领域检验（Property B 与 ECC）及最小插件契约补充**
>
> 引入编码理论（`[43,10,17]` 不存在性证明与 `[45,11,17]` 未决探索）作为第二领域对照后，三层架构保持稳定，同时在以下四方面补齐了单靠 Property B 容易忽略的边界：
>
> | 维度 | Property B（超图二染色下界） | ECC（二元线性码最优距离） | `mathrsi-base` 提炼的通用规则 |
> |---|---|---|---|
> | **目标量词与终结捷径** | 全称证明（$\forall H$ 边数 $\le M$ 可二染） | 存在/全称二分（找一个合格矩阵 $\exists G$，或证全域 $\neg\exists G$） | 区分**存在性见证、全称排除、固定范围排除、条件引理**；允许受限子族作为构造捷径直接终结 $\exists$ 目标，不强迫所有探索先做全局分类 |
> | **发现与核验关系** | 浮点 LP 找候选乘子 $\to$ 精确有理数对偶不等式核验 | 启发式找 172 母码 / 随机找 39 低权空间 $\to$ 结合文献上限或逐对低权字做完备核验 | **候选发现与结果核验解耦**：探索程序无需自证完备，完备性与无漏检查只施加在最终结论依赖的核验链上 |
> | **共同对象耦合** | 同一 $H$ 的共同坏边对、共享外点池列守恒 | 多行扩张线性组合闭合（$x+U\subseteq F$）、多核共享头矩阵、同步坐标交换与稳定子规范化 | 局部受阻或组合膨胀时，`base` 提示检查**是否将同一对象的耦合分量拆开独立取边际/独立规范化**；具体耦合公式与同步运输映射由插件维护 |
> | **真实端到端成本** | 数学减域 + 活跃项诊断 + 重证书拆块编译 | 前置集合生成 + 共享中间结构（$P_a/Q_{a,b}$、交换商）+ 输出分类与下层扩张成本 | 完整有限域可算时直接算完；评估分支成本须计入**前置生成、联合自由度、输出规模与下游连接**，不以母码个数或单步内核秒数外推全题进度 |
>
> **最小插件契约的五项补充字段（示意语义，非强制 schema）：**
> 1. **目标逻辑角色（`claim_role`）**：标明当前任务或产物的性质是 `existential_witness`（单见证即可闭合存在性）、`universal_bound_or_exclusion`（需完整覆盖证明）、`fixed_scope_exclusion`（仅排除固定母码/参数窗）还是 `conditional_reduction`。
> 2. **变换方向与回退映射（`reduction_type & pullback`）**：标明变换是双向等价、必要覆盖还是启发式构造子族；若涉及坐标/基变换或群轨道取商，说明如何同步运输相关向量及如何将结果还原为原始验收对象（如 $11\times 45$ 显式矩阵或原超图染色）。
> 3. **发现与核验分离声明（`discovery_vs_verification`）**：允许启发式、随机采样或外部求解器产出候选；明确独立验证器实际检查什么（如直接读矩阵验 2047 码字、重放拒绝见证流、核对文献分类上限），不把求解器退出码 0 当作全域证明。
> 4. **共同约束与联合自由度（`joint_coupling`）**：记录跨分支或跨行的共享变量（如同一母码 $K$、同一头矩阵、重复对标签三元组 $p,q,p+q$ 或共同坏对槽），防止子任务做破坏联合相容性的独立规范化。
> 5. **全链路成本分解（`full_chain_cost`）**：分别记录前置数据生成、当前核扫描、输出候选规模（区分记录数与不等价类数）及下游未闭扩张的预估门槛，支持基于实测 Profile 的有依据停算或继续压缩。
> *(注：以上设计建立在 Property B 与 ECC 两个离散数学项目的真实证据之上，尚不构成跨连续分析、几何或新运行时提速的实验定论。)*


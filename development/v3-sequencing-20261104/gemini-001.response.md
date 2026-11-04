基于对当前仓库实现与本轮新案例底稿的只读核查，以下就五个核心问题给出具体设计建议。

### 实际读取的关键文件
- **Base 与契约**：[V2_CHANGES.md](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/V2_CHANGES.md)、[PLUGIN_CONTRACT.md](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/PLUGIN_CONTRACT.md)、[mathrsi-meta-evolve/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/SKILL.md)、[mathrsi-route-loop/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-route-loop/SKILL.md)、[mathrsi-prove/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prove/SKILL.md)、[mathrsi-verify/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-verify/SKILL.md)、[mathrsi-handoff/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-handoff/SKILL.md)
- **ECC 现行插件**：[mathrsi-ecc/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/ecc/skills/mathrsi-ecc/SKILL.md)、[source-map.md](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/ecc/skills/mathrsi-ecc/references/source-map.md)
- **本轮新成果底稿**：[README.md](file:///Users/rfy_naiveai/Desktop/aris4math/mathrsi_new_results/_intake/three-cases-20261104/README.md)、[ecc/EVOLUTION.md](file:///Users/rfy_naiveai/Desktop/aris4math/mathrsi_new_results/_intake/three-cases-20261104/ecc/EVOLUTION.md)、[erdos86/LESSONS.md](file:///Users/rfy_naiveai/Desktop/aris4math/mathrsi_new_results/_intake/three-cases-20261104/erdos86/LESSONS.md)、[ruskey-savage/LESSONS.md](file:///Users/rfy_naiveai/Desktop/aris4math/mathrsi_new_results/_intake/three-cases-20261104/ruskey-savage/LESSONS.md)

---

### A. 推荐先后顺序：主线先做轻量扎实的 v3，支线并行做网页成果与视觉底稿

推荐采用**“v3 增量实现先行收口，网页的数学成果展板并行准备”**的双轨顺序：
1. **现在即可并行的部分（不依赖 v3 代码）**：六大主题（Property B、DD、Happy Ending、ECC、Erdős 86、Ruskey–Savage $Q_6$）的数学结论、核心转折故事及核心图示（如 ECC“任意码→172母码→陪集兼容排除”流图、Erdős 86“共享根方格的同角/邻角/对角同步作用”图、$Q_6$“1024满秩短森林跨越137亿匹配”图）事实已齐备，可立即设计网页结构、文案与 SVG/TikZ 视觉图。
2. **应等 v3 落地的部分**：[mathrsi-meta-evolve/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-meta-evolve/SKILL.md) 明确规定“不把升级计划写成已完成版本”。网页中关于 **v0→v1→v2→v3 演进闭环图、ECC 正式插件入口、Base v3 具体改动链接**，应等运行 `mathrsi-meta-evolve` 完成本地 v3 修改后再填入，使宣传页的每一句工作流叙述都有真实仓内文件支撑。

---

### B. Base v3 最小但扎实的完成范围（4 项真实增量改动）

v2 已具备“纯形式目标直通 Lean、公开基线更新消费队列、变换后正负证据分别继承、单路局部充分门失败回读共同覆盖并”四项能力（见 [V2_CHANGES.md](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/V2_CHANGES.md#L9-L14)）。v3 绝不重复这些原则，而是针对新案例暴露的真实工作流缺口，在现有文件中做 **4 处增量修改**：

| 拟增机制（真实科学触发） | Base 增量改动位置与具体动作 | 领域 Plugin 归属 | 单题材料保留（不入 Base） |
|---|---|---|---|
| **1. 受限池/工作集优化与全域分离回流**<br>*(Erdős 86 活动池 0.59175 放回全域恶化至 0.83472；末轮劣于 iter178)* | 改 [mathrsi-route-loop/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-route-loop/SKILL.md) §Phase C 与 [mathrsi-prove/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prove/SKILL.md) §2/§4：迭代/列生成求解并列记录 `restricted / full-domain / best`；全域分离出的违反项直接回流工作集触发下一轮，精确化只绑定历史 `best` 证书快照而非末行日志。 | 旗代数 $LL^T$ 整数 Gram 精确化、全域分离筛选条件、对偶定价语义。 | 初始 3500 池、分母 $5\times 10^7$、3,312,331 代表索引留 `erdos86` 档案。 |
| **2. 有限生成元全称化探针与失败池降级复用**<br>*($Q_6$ 用 1024 短森林满秩跨越 $1.37\times 10^{10}$ 匹配；12 孔缺秩池 8031/8192 转作局部正证书)* | 改 [mathrsi-route-loop/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-route-loop/SKILL.md) §Phase C 与 [mathrsi-prove/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prove/SKILL.md) §1/§4：扩算巨型枚举前先检查是否存在“有限算子/生成元满秩或代数上界”全称化机制；若全称满秩失败，将池内合法对象降级复用为局部极大域的逐实例正证书，不弃置也不误作否定。 | 连通矩阵 GF(2) 秩转移、保自由根极大化、$s=2$ 路径删除修复 $s\ge 3$ 接口。 | 九孔层 2–18 划分、1024 森林记录、各孔轨道数留 $Q_6$ 档案。 |
| **3. 被标记对象（Pointed Objects）在归约与取商中的同步保持**<br>*($Q_6$ 避零生成漏掉删根极大与自由根轨道；Erdős 86 独立取商抹掉共享根相对朝向)* | 改 [mathrsi-prove/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-prove/SKILL.md) §1/§3 与 [mathrsi-verify/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-verify/SKILL.md) §1：含指定根/自由端点/必含子图的问题，归约与对称取商须声明固定标记子结构的同步稳定子作用（pointed orbit），并在增广补全后恢复原伙伴身份（区分原跨边伙伴 $h$ 与增广辅助伙伴 $h^*$）。 | ECC 首行稳定子运输、Erdős 86 根方格 $D_4$ 同步商、$Q_6$ 禁对 $F+R$ 整体无圈。 | $Q_2$ 的 `{23}` 反例、五种根面表、具体尾型参数留各自单题。 |
| **4. 混合形式化边界装配与搜索/便携复核解耦**<br>*(ECC 第二波双 Lean 工程接实际矩阵与外部前提；ECC/Erdős/Happy Ending 轻量重放脱离重搜索环境)* | 改 [mathrsi-verify/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-verify/SKILL.md) §1/§4 与 [mathrsi-handoff/SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-handoff/SKILL.md) §4：① 混合 Lean 工程核内绑定显式小矩阵/参数，外部定理与穷尽目录作为具名假设显式审计，区分“无 `sorryAx`”与“外部计算核内化”；② 强制分离重型搜索依赖与零搜索依赖的便携 checker，在独立目录实测轻量重放。 | **升级 `plugins/ecc` 为自包含正式插件**；提供 SAT/RUP、整数 Gram、陪集重放说明。 | 1.68GB 原始 pair 见证流、历史运行日志按只读归档引用。 |

---

### C. ECC 插件形态与版本关系：同一插件原地演进，不与 Base 硬绑定

1. **同一插件 `plugins/ecc` 的两代演进，绝不建两个并列插件**：
   目前 `plugins/ecc` 仅有 [SKILL.md](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/ecc/skills/mathrsi-ecc/SKILL.md)、[source-map.md](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/ecc/skills/mathrsi-ecc/references/source-map.md) 和 `fixed-parent.md` 三份文件，无 `README.md`，且 [PLUGIN_CONTRACT.md](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/PLUGIN_CONTRACT.md#L81) 明确标其为“待完善的旧草案”（代码/数据未随仓）。ECC 第二波的 Lean 归约、实际矩阵连接、便携重放与 42/16 文献路线，处理的是同一数学对象与同一套五层义务，正好将 `plugins/ecc` 从“v1 外链路径草案”原地补齐为“v3 随仓自包含插件”（补齐 `plugins/ecc/README.md`、随仓收入 5 个下界矩阵与 172 母码有限数据、ECC43/ECC42 Lean 接口与薄验证脚本）。若拆成两个插件，反而造成 `.claude/skills/mathrsi-ecc` 入口分裂。
2. **Base 与插件版本无需硬绑定**：
   两者仅通过 [PLUGIN_CONTRACT.md](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/PLUGIN_CONTRACT.md#L5-L31) 的五阶段自然语言输入/返回契约交互。只需在 `plugins/ecc/README.md` 顶部放一段清晰说明即可：

```markdown
# ECC 二元线性码插件（随 MathRSI v3 升级为自包含版）

- **演进记录**：
  - 初版草案（随 v1 建立）：提炼构造验距、五层否定义务、陪集无遗漏与联合扩张判断（原代码与数据外链）。
  - 自包含升级（随 v3 落地）：吸收第二波形式化与便携交接成果，随仓附带 5 个最优下界矩阵、172 类母码有限目录、轻量独立验距/重放入口，以及 ECC43/ECC42 两个 Lean 归约工程接口与 42/16 文献归一化路线。
- **与 Base 配合**：通过 `mathrsi-ecc` 接入 base 的 `prepare/survey`、`route-loop`、`prove`、`verify`、`handoff`，返回当前调用处，不绑死特定 base 小版本。
```

---

### D. v0→v1→v2→v3 的研究反馈故事（自然正面概括）

- **已做事实**：v0 用独立技能取得 Property B 与 ECC（$d_2(43,10)=16$ 及 172 母码双扫）原始突破 → v1 提炼出 5 个子工作流与首批插件 → v2 建立 `mathrsi-meta-evolve` 并实际吸收 DD，同时用这套工作流支撑了 ECC 第二波、Erdős 86、Ruskey–Savage $Q_6$ 与 Happy Ending 的深入研究。
- **待本次做**：运行 `mathrsi-meta-evolve` 将这批新研究的机制与 ECC 自包含资产正式写回 v3。

**可直接用于网页/导言的概括段落**：
> **MathRSI 的核心是“数学突破与研究工作流的双向反馈循环”。** 在 **v0** 阶段，我们依靠独立研究技能攻克了 Property B 超图二染色界与二元线性码 $d_2(43,10)=16$（含 172 类母码双完整扫描与 6.19 亿对陪集拒绝）。**v1** 从这两场战役的真实推导与排错中，提炼出“准备与文献、路线循环、证明推进、装配验证、复现交接”五个自适应子工作流及首批领域插件。进入 **v2**，我们构建了外层演化技能 `mathrsi-meta-evolve` 并吸收度直径问题（DD）经验，让工作流具备了基线更新自动修剪队列、对象变换后正负证据分别继承与纯形式目标直通 Lean 的能力。依托 v1/v2 的这套研究方法，我们在后续课题中实现了多维度的跃升：**ECC** 在既有主结果上打通了两个 Lean 形式化归约工程、整合 $d_2(42,16)=12$ 文献路线并建成零搜索依赖的便携证书重放包；**Erdős 问题 86** 通过共享根方格的同步稳定子作用与全域分离反馈，将超立方体无四环渐近边密度上界推进至 $0.59155154$；**Ruskey–Savage 猜想**则利用保自由根极大化与 1024 个短森林的满秩全称化机制，跨越百亿级匹配域，完整解决六维情形 $Q_6$ 并推广至任意维六方向匹配。如今，**v3** 通过 `mathrsi-meta-evolve` 将这些跨领域实战中长出的新机制——受限池与全域分离闭环、有限满秩生成元跨巨域与缺秩池降级复用、标记对象同步取商、以及混合 Lean 装配与便携复核——反哺回 Base 与自包含的 ECC 插件，完成了从“做出新数学”到“沉淀更强研究工具”的完整迭代。

---

### E. 何时停止 v3、切入网站开发（防延迟硬门禁）

为避免“不完备焦虑”导致无限拖延，建议设定 **4 条硬性停机线**，达标即刻封板 v3 转入网页：
1. **Base 只改 4 处，不扩写主干**：完成上述 B 中的 4 处原文件 diff 与 `development/evolution/` 下的本轮 `EVOLUTION.md`，做一轮针对 diff 的 `research-review` 维护审阅并修完实质漏洞即停。
2. **插件不做全量重型搬迁**：本次插件工程**只把 `plugins/ecc` 补齐为自包含正式版**；Erdős 86、$Q_6$、Happy Ending 的经验作为 `mathrsi-meta-evolve/references/` 下的跨领域证据案例与只读档案索引收入，不强求为每个新题都新建一套四技能大插件，也不把 1.68GB 原始见证流塞进 Git 主仓。
3. **验证只跑有界轻量入口**：直接复用 `_intake/three-cases-20261104` 已证实秒级通过的轻量核对（ECC 5 个矩阵与 172 母码有限表、Erdős 86 `prepare-only` 整数 Gram、$Q_6$ 1024 森林秩核对），由协调者沿新改动的 `base → plugin` 实际调用一次即完成验收；**绝不重跑 $172\times 2^{32}$ 双扫描、全量 Lean 重编译或造跨版本对照实验**。
4. **开放问题如实挂牌即切换**：将 $d_2(45,11)=17$、Erdős 86 的 $1/2$ 猜想、$Q_n$（$n\ge 7$）一般匹配列为“当前开放边界”，即刻冻结 v3 并全力制作宣传网页。


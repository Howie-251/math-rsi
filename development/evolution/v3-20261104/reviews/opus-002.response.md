threadId: cd13834d-466f-4108-8d2b-8e766757047a

# Hypercube 两插件：composed RR Step 3 意见

本次按 composed 维护适配只做了原件读取和 Step 3 意见产出，没有进入 Step 4–5 的论文共识循环。全程只读，没有运行任何程序，下面的结论交回维护协调者处理。

## 总体判断

两个插件都已经是能实际使用的领域技能，不是空模板或薄摘要。数学内容我对照原件逐项核过，能对上：

- **hypercube-extremal**
  - 共同 Q4 引理 K=(A,B,S)（S 是 A∩B 的独立集）、同步根稳定子、状态数 240/212/190/187/170 及顶点 9 态，与原理论 guide02 一致；无序旗对轨道合计 36579，也与 guide02 一致。
  - 高维误差公式 `C+M_F/(n−3)+M_v(4n−6)/((n−2)(n−3))` 与原件一致。其中 `(1−p)/p=(4n−6)/((n−2)(n−3))` 我手算核过。
  - 技能 §6 明确：有限 n 必须保留修正项，不能直接用渐近常数 C。
- **工作集、全域、整数证书、高维平均四层是分开写的。** 活动池约 0.59175 → 全域 0.83472、末行与最佳分开、负定价不等于证书不 PSD、q5_cuts=[]，都与原 history 和 guide 对得上。
- **重放命令与输出可信。** `verify_final_q4.py` 和 `verify_local.cpp` 我实际读过；日志 `final-q4-replay.log` 里的计数和最大值与 reproduction.md 写的预期一致；archive 保留了最终检查所需的全部输入。
- **hypercube-hamilton**
  - P6 的量词（自由根 u、异奇偶目标 v、v 可以已被覆盖）、保根极大化的 23≤|L|≤31、补全后真实伙伴 h 与补全伙伴 h\* 的区分、以及 `L'⊆L*'`、`D=D*∪(L*'−L')`，与 `TWELVE_STAR_MAXIMAL_A_REDUCTION.md` 第 43–87 行一致。
  - 1024 行满秩如何覆盖任意配对 F 的论证（引用 CKN 秩上界 → 选中行张成全部行空间 → 每列非零），与 `A10_ORBIT3_UNIVERSAL_PROOF.md` §3 一致。
  - 缺秩森林池只作为逐实例正证书复用，没有声称池穷尽或满秩。
- **A10 检查器确实独立。** `A10_ORBIT3_UNIVERSAL_REVIEW_check.py` 用 DSU 重算全部 1048576 个连通位，再用低列高斯消元独立求秩，没有使用生产者保存的消元组合。共享边排除断言（第 75 行）也是对的。
- **范围写得诚实。** A10 有限复算只关闭最后五个几何轨道；整题 P6 仍是 same-family/provisional、显式文献进口、无 Lean。这样写准确，不需要重跑整题。

以下 4 项是需要修的地方，第 1 项最实质。

---

## 问题与最小修法

### E1｜新候选证书无法用现有包装器核验（extremal，最实质）
- **涉及文件：** [verify_final_q4.py](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/hypercube-extremal/archive/source/tools/verify_final_q4.py#L26-L39)、SKILL [§4–5](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/hypercube-extremal/skills/mathrsi-hypercube-extremal/SKILL.md#L50-L64) 及 verify 一行。
- **问题：** 包装器把最终 bound、M_F、M_v 写成了固定值（`require(bound==23662061277957791/…)` 等）。技能要求的“新候选 → 整数化 → 全域重算 → 只有更好才替换 best → 由新矩阵重算 M_F/M_v”这条路，用它只能重放已冻结的那份证书。任何新候选都会在 `Unexpected final bound` 处失败。
- **其实底层已经支持：** `verify_local.cpp` 第 104、107 行在 `target<0` 时只计算最大值、不设阈值，正好是新候选需要的模式。
- **最小修法：**
  - 在插件里加一个约 40 行的 `tools/check_q4_candidate.py`，不改 archive：
    - 复用 prepare 的形状、整数、q5 为空、64 位安全检查；
    - 去掉三处固定值等式；
    - 写入 `target=-1` 调用原 C++；
    - 输出 EXACT_MAX/den 约分后的 C、由新矩阵算出的 M_F 和 M_v；
    - 可选 `--n` 参数，输出该有限 n 下的精确分数界。
  - 适用范围写明：只适用于同一个六块 Q4 模型；模型变了要另写检查器。
  - 有界使用：
    - 在冻结证书上跑一次，应得到同样结果；
    - 若 `certificates/Q4_optimized_certificate_20261028/` 的格式相同，再跑一次，应得到 236634773493897/400000000000000。这能证明工具没有硬编码。我没有核对该证书 JSON 的字段是否一致。

### E2｜接续搜索的路径会失败，archive 说明有一处错（extremal）
- **涉及文件：** [archive/README.md](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/hypercube-extremal/archive/README.md#L5-L7)、[reproduction.md](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/hypercube-extremal/skills/mathrsi-hypercube-extremal/references/reproduction.md#L25)、`archive/source/tools/materialize_research.py`。
- **archive README 写错了省略项：**
  - README 说省略的是“4 份大表 + .DS_Store”；
  - 实际 [INVENTORY](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/hypercube-extremal/archive/INVENTORY.json#L7-L33) 的 omitted 是 5 个 .bin（face_indices、graphs、pair_index、shadows、vertex_indices），合计 451,339,260 字节，里面没有 .DS_Store。
- **接续入口会崩：**
  - 原 REPRODUCE 和 guide06 的接续入口是 `materialize_research.py`；
  - 它遍历原 inventory.json 的全部行并对每一行 `read_bytes()`；
  - 原包中这 5 个文件是“已归档”，所以在插件 archive 里会在第一个缺失文件处报错。这是我按源码推断的，没有实际执行。
- **重建链存在，但插件没写出来：**
  - `prepare_data.py` 由 keys.bin 生成 pair_index.bin；
  - `generate_models.cpp` 生成另外 4 张表；
  - 再编译 evaluate.so，然后运行 `column_lift.py --no-q5`。
- **最小修法：**
  - 改正 README 的省略清单；
  - 在 reproduction.md 加一节“接续搜索（本轮未执行）”，写明上述步骤、跳过 5 个省略项的物化方式（手工复制目录，或一个约 10 行、带 skip 参数的插件内工具）、NumPy/SciPy 及私有 `_highspy` 依赖，最后接 E1 的工具。

### H1｜全称森林秩门只能重放旧证书，不能用于新几何（hamilton）
- **涉及文件：** SKILL [§3](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/hypercube-hamilton/skills/mathrsi-hypercube-hamilton/SKILL.md#L44-L48)、[reproduction.md](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/hypercube-hamilton/skills/mathrsi-hypercube-hamilton/references/reproduction.md)。
- **问题：** “A10 示例可直接执行”实际只能重放冻结证书。检查器里 H、K 和 manifest 都是写死的；生产者 `A10_ORBIT3_UNIVERSAL_rank.cpp`（见 manifest）在插件中没有被点名。
- **为什么值得参数化：** 这道秩门在包内至少用了两次——A10 是 22 个端点、秩 1024；十六孔 smallcut 是 18 个端点、秩 256（插件自己的说法，我没有读该原件）。两者都符合 CKN 上界 2^{|K|/2−1}。所以它是可复用的机制，不是一次性证书。
- **最小修法：**
  - 由 REVIEW_check 改出一个薄的插件工具，参数为 `--dim --root --holes --forests --columns`；
  - 记录宽度由 |K| 推出，所需秩等于 2^{|K|/2−1}；
  - 保留短边、度数、无圈、端点配对、DSU 连通位和低列消元这些检查，manifest 绑定改为可选；
  - reproduction.md 写明生产者 rank.cpp 的输入输出；
  - 只参数化 A10 同型的约束。十六孔那种保留必含边 e、避开禁对 R 的额外约束，等真实需要时再加。
  - 有界使用：用参数化版本重跑 A10，得到同样的 1024 即可。

### H2｜原猜想陈述漏了“匹配”（hamilton，一行）
- **涉及文件：** SKILL [§1 第 26 行](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/hypercube-hamilton/skills/mathrsi-hypercube-hamilton/SKILL.md#L26)。
- **问题：** “任意 `M⊆E(Q_n)`”漏掉了 M 必须是匹配，量词变成了任意边集。这个插件本身强调量词精确，所以值得改。
- **最小修法：** 改为“任意匹配 M⊆E(Q_n)”。

---

## 实际读取范围

- **已读：**
  - v3 EVOLUTION；
  - 两个插件的 README、SKILL、各 3 份 references、IMPLEMENTATION、archive README 和两份 replay 日志；
  - extremal 的 INVENTORY 前约 860 行（含完整的 omitted 段）；
  - extremal 原件：guide02、guide06、REPRODUCE、verify_final_q4.py、verify_local.cpp、materialize_research.py、prepare_data.py、generate_models.cpp、model.py 前 30 行、column_lift.py 前 40 行、run_manifest.json；
  - hamilton 原件：A10_ORBIT3_UNIVERSAL_PROOF、REVIEW_check.py、MANIFEST、TWELVE_STAR_MAXIMAL_A_REDUCTION。
- **未读：**
  - hamilton 的 INVENTORY、P6_FULL_CLOSURE/REVIEW、SIXTEEN_SMALLCUT、十二孔有限证明和 checker、SOURCE_AUDIT、CKN 原文定位文件；
  - extremal 的研究报告、guide04/05、各 history；
  - development 下的 USE.json。
- **范围外：** Root 正在做的主入口、双端别名、文档集成，以及在途的 Happy 插件，本轮不评。


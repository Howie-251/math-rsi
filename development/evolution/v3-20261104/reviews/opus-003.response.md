threadId: cd13834d-466f-4108-8d2b-8e766757047a

# 定点复核：hypercube 两插件第二轮修复

**结论：** 四项修复都已真实落地。两个新工具数学上正确，也确实能接受新的同型候选，而不只是重放历史证书；它们的输出能经 DOMAIN_ROUTING 和主入口回到原义务。还剩 3 处文字或记录层面的小问题，各一行到几行就能改，都不需要重跑。

## 认可的部分

**check_q4_candidate.py（E1）**
- 写入 `target=-1` 后，原 C++ 会遍历完整合法域求真实最大值；C 取 EXACT_MAX/(192D²)，不用证书自带的 bound 元数据。
- 64 位安全界与 C++ 里的累加上界一致。我手核了：边项、面项、顶点项各自不超过 192·max，加起来不超过 192(D²+Σmax)。
- M_F、M_v 取自 Q=LLᵀ 的对角元。群平均后的 Qbar 对角元不会超过这个最大值，所以拿它当误差常数是合法的上界。
- 有限 n 公式要求 n≥4。两份 n=100 的数值我按十进制粗算核过：约 0.62371 和 0.623784，都对得上。
- 两份不同证书分别得到不同的 C、M_F、M_v（final 是 0.591551…，optimized 是 236634773493897/400000000000000）。这说明工具没有硬编码；optimized 的 M_F 也落在其 manifest 给出的十进制上界 1.031063 之内。
- 补充一点，不需要改：可靠性本身不依赖“状态顺序相同”。C++ 用自己的状态解释计分并做同步平均，平均论证对任意 PSD 块都成立。所以顺序不对的输入只会得到更差、但仍然合法的 C，不会产生假上界。文档里“相同状态顺序”的限定算稳妥写法，不用再加额外校验。

**check_forest_rank.py（H1）**
- 森林边数 `2^dim−1−t/2`、记录宽度、各点度数（root 为 0，K 为 1，holes−root 为 2）、无圈、端点配对、列覆盖 K、DSU 连通位、共享边断言、低列消元求秩，都与原 REVIEW_check 和 A10 证明 §1–3 一致。
- 不会出现只由 holes 构成的分量：这种分量里每点度数都是 2，但有限树至少有两片叶子，矛盾。工具只检查 K 分组的写法因此是充分的。
- 所需秩取 CKN 上界 2^{t/2−1}。判据用 `rank==required`，森林行数多于所需秩时也成立。工具把“合法”（status）和“门满足”（`universal_rank_gate_met`）分成两个字段，这样做是对的。
- Q3 小例我手核过：K 上 3 个完全匹配构成的矩阵是 J−I，GF(2) 秩为 2，与结果一致。A10 参数化版本得到 1048576 位、158674 个 1、秩 1024，与冻结 checker 的结果一致。
- 适用范围写成 A10 同型，并明确未实现必含边 e 和禁对 R 的约束，这样写合适。

**materialize_search.py 与接续搜索文档（E2）**
- 恰好跳过 5 张表，archive 原件不动。
- 后续链条 prepare_data → generate_models → evaluate.so → `column_lift --no-q5` 与原 REPRODUCE、源码对得上，并明确写了“本轮未执行”。

**H2：** 已改为“任意**匹配** M”，确认无误。

**回到原义务的链路**
- [mathrsi-research 第 73–75 行](file:///Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/SKILL.md#L73-L75)按对象加载 DOMAIN_ROUTING，结果交回调用阶段。
- DOMAIN_ROUTING 中 Hamilton 的 route-loop、prove、verify 各行，能接住森林秩门的合法性、`universal_rank_gate_met`，以及“缺秩池转逐实例正证书”这条路线。

## 剩余 3 处小问题

1. **extremal SKILL §5 末句与前文矛盾**
   - 位置：[SKILL.md 第 60 行](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/hypercube-extremal/skills/mathrsi-hypercube-extremal/SKILL.md#L60)。
   - 问题：段尾仍写“使用原包装器先计算整数上界…再运行完整几何checker”，可同一段前面刚说过原包装器不能接受新候选。
   - 修法：改成“上述工具（冻结证书重放时用原包装器）先计算整数上界…”。

2. **DOMAIN_ROUTING 的 extremal verify 行只写了冻结证书**
   - 位置：[DOMAIN_ROUTING.md 第 55 行](file:///Users/rfy_naiveai/Desktop/MathRSI/docs/DOMAIN_ROUTING.md#L55)。
   - 问题：输入列只写“冻结的最终整数证书”。prove 或 route-loop 交来新的同型候选时，路由表上看不到 `check_q4_candidate.py` 这条入口。SKILL 里已经写了，所以影响有限。
   - 修法：输入列改为“冻结证书（原包装器重放）或同型新候选（tools/check_q4_candidate.py）”，返回列补“新 C、M_F、M_v；只有优于已接受 best 才替换”。

3. **materialize 结果文件里有一个字段不是脚本写的**
   - 位置：[materialize-search-result.json](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/hypercube-extremal/evidence/materialize-search-result.json#L13) 中的 `key_aliases_present: true`。
   - 问题：[materialize_search.py](file:///Users/rfy_naiveai/Desktop/MathRSI/plugins/hypercube-extremal/tools/materialize_search.py#L32-L34) 并不输出这个字段，而 reproduction.md 说“必需别名均存在”恰恰依据它。也就是说，这份证据不完全是脚本本身的输出。
   - 修法（二选一）：
     - 在脚本里加几行，检查后续步骤实际要读的文件：optimization 目录下的 prepare_data.py、keys.bin、generate_models.cpp、face_pair_lookup.bin、evaluate.cpp、model.py、sdp_core.py、full_meta.npz、full_C.npz、face_orbit_meta.npz、face_block_*.npz、q5control_best.npz，以及 q5_empty_moment 目录下的 column_lift.py；由脚本自己输出缺失列表。
     - 或者在 evidence 里注明这个字段来自另一次人工核对，并列出核对了哪些文件。

## 实际读取范围

- **已读：**
  - OPUS_002_FIXES；
  - 两个新工具全文，以及 materialize_search.py 全文；
  - extremal 的 reproduction.md 全文、SKILL §4–7、candidate-inputs/README、candidate-optimized/RESULT.json、materialize-search-result.json；
  - hamilton 的 IMPLEMENTATION、reproduction.md 全文、parameterized-a10-result.json、small-geometry/RESULT.json；
  - DOMAIN_ROUTING 全文、mathrsi-research 主入口全文。
- **未读：**
  - candidate-final/RESULT.json，以及两个运行目录里的 PROCESS.json；
  - optimized-q4-only.json 的 PROVENANCE；
  - parameterized-a10.log；small-geometry 的二进制输入；
  - 修订后的 extremal archive/README（E2 的纠正以 OPUS 记录和 INVENTORY 为准）。
- **未做：** 没有运行任何命令。


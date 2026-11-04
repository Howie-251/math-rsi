# 给查验者的交接：二元线性 [43,10,17] 码不存在

交接日期：2026-10-07。项目：aris4math_v2。

本项目提交的结论是：**不存在长度 43、维数 10、最小距离至少 17 的二元线性码。** 交付包括完整书面证明、172 个实际分类代表、两套完整扩张域扫描，以及全部配对拒绝见证的独立重放。证明使用下文明确列出的两项已发表结果，并依赖所列计算程序的正确执行；没有提交 Lean 内核形式化。

请独立检查命题、数学归约和计算证据之间的对应关系。已有模型的赞同不作为你的推理前提。完整阅读版是 [PROOF_PACKAGE.html](PROOF_PACKAGE.html)，可编辑规范源为 [PROOF_PACKAGE.md](PROOF_PACKAGE.md)。

## 1. 要查验的原命题

在二元域 $\mathbb F_2$ 上，原任务要求寻找

$$G\in\mathbb F_2^{10\times43},\qquad \operatorname{rank}(G)=10,$$

使得

$$\forall u\in\mathbb F_2^{10}\setminus\{0\},\qquad \operatorname{wt}(uG)\ge17.$$

本次证明上述矩阵不存在，亦即 $d_2(43,10)\le16$。这里的 $d_2(n,k)$ 表示长度 $n$、维数 $k$ 的二元线性码能够达到的最大最小距离。目标是排除距离**至少** 17，并非只排除距离恰好 17。

原量词允许任意二元矩阵：没有预设循环或准循环结构、自同构群、固定种子、固定 residual、hull 维数、零列禁令或列互异条件。证明中用到的列独立性由假设存在目标码后推导，不能预先添加。母码也不假设 projective。

原始规格以 [FORMAL_SPEC.md](FORMAL_SPEC.md) 的“核心问题与成功条件”为准。该文件还保存探索时的其他可用归约；最终证明采用下面的四坐标缩短路线，不依赖那些历史候选路线全部成功。

若查验者找到一个满足原规格的实际 $10\times43$ 矩阵，只需核秩和全部 1023 个非零消息重量，就足以反驳本次结论。原始题目的构造 verifier 不能单独验收不存在性；后者还需要完整覆盖证明和计算检查器。

## 2. 推荐阅读顺序

| 顺序 | 文件 | 用途 |
|---|---|---|
|1|[PROOF_PACKAGE.html](PROOF_PACKAGE.html)|单卷完整证明；问题、定义、逐步归约、计算原理、172 类逐例数据和实际矩阵均在正文或附录；公式可离线阅读|
|2|[FORMAL_SPEC.md](FORMAL_SPEC.md)|独立核对原参数、量词与构造/不存在性两种验收标准|
|3|[计算覆盖清单](work/goal-20261006-wave2/global_closure/COMPUTATIONAL_COVERAGE.json)|逐一连接 172 个实际母码、两套扫描输入、完整结果、F 文件和 pair 见证文件|
|4|[冻结矩阵快照](work/goal-20261006-wave2/global_closure/actual172_matrices.json)|七行生成矩阵、全部 128 码字、127 个非零重量、hull 和来源标签|
|5|[复现说明](work/goal-20261006-wave2/global_closure/REPRODUCE.md)|轻量目录检查、输入绑定、完整扫描和配对证书重放的准确接口|
|6|[全 pair 独立重放报告](work/goal-20261006-wave2/global_closure/pair_certificate_replay/REPORT.md)|619,053,789 个实际拒绝见证的检查逻辑、执行记录和逐例输出|
|7|[原证明审计](work/goal-20261006-wave2/global_closure/PROOF_AUDIT.md)|原全链证明的 fresh proof-checker 范围及跨家族审阅记录|

根目录 Markdown 是本次中文单卷的规范源，HTML 由它生成。原验收时的 [英文完整证明](work/goal-20261006-wave2/global_closure/PROOF_PACKAGE.md) 和 [证明义务表](work/goal-20261006-wave2/global_closure/PROOF_SKELETON.md) 原样保留，便于比较新稿与既有数学证据。提出问题时请引用新稿的章、引理或公式，以及对应证据文件，不只给生成 HTML 的行号。

## 3. 证明主线与重点核对位置

全链为：任意目标码 → 奇偶扩展成偶 $[44,10,\ge18]$ → 任意三列独立 → 对偶中必有重量 4 码字 → 在其支撑上缩短 → 全支撑偶 $[40,7,18]$ 母码 → 完整 172 类之一 → 三个尾扩张向量 → 偶陪集兼容图中的三角形。实际计算证明 172 个兼容图全部无边，因而产生矛盾。

| 环节 | 需要独立核对的实质问题 | 主要证据 |
|---|---|---|
|奇偶扩展|距离从至少 17 变成至少 18；反向穿孔不降秩；没有添加原任务没有的结构假设|单卷的问题设定与奇偶扩展证明|
|三列独立|三列秩至多 2 时缩短后维数至少 8；取 8 维子码，用 Griesmer 界排除距离大于 18，再使用 E1|单卷三坐标归约；E1 原文|
|对偶四元支撑|MacWilliams 恒等式的归一化、$P(w)$ 的非负性和常数正确；得出 $B_4\ge12$|单卷 Krawtchouk 多项式推导|
|母码合法性|选择的是**某个对偶重量 4 码字的支撑**；四列秩恰为 3；缩短维数为 7、距离恰为 18，且确实全支撑|单卷四列缩短与全支撑证明|
|完整分类|本机实际 172 个对象合格且两两坐标不等价；结合外部“至多 172 类”才得到覆盖；hull 分布不替代覆盖证明|E2、冻结矩阵、双色关联图规范化检查|
|尾部标准形|仅换生成基和置换坐标，将尾部取为 $1001,0101,0011$；没有把一般可逆线性变换当作保距离坐标操作|单卷尾部标准形及七种非零尾和的距离条件|
|陪集归一化|$E_{40}/K$ 的维数为 32；每个陪集只有一个 pivot 为零的偶代表；规范化保持所需距离|单卷归一化引理；两套核输入|
|F 完备性|两套完整 $2^{32}$ 遍历均终止，域映射为双射，接受条件精确；不同规范下转换后比较的是完整集合，不只是数量|两套 C++ 核、172 例完整运行记录、逐例比较|
|pair 排除|全部 $\binom{|F|}{2}$ 个无序对各有实际码字使距离小于 16；索引、字节数、EOF 均核对；无边足以排除所需三角形|独立 literal 40-bit checker 及全部见证流|
|返回原命题|任意目标均被前述链覆盖；同一陪集不能充当两条扩张行；不需要再对已经无边的图搜索三角形|单卷最终反证|

### 两项外部数学输入

**E1：不存在二元线性 $[41,8,18]$ 码。** 已读 Bouyukliev 的 2008 年学位论文 §6.2.2、Theorem 6.3，印刷页 147 / PDF 第 149 页。这一定理没有要求偶性、projectivity 或特定 hull。见 [作者论文 PDF](work/goal-20261006-wave2/three_coordinate_rank_bound/author_thesis.pdf)、[该页截图](work/goal-20261006-wave2/three_coordinate_rank_bound/thesis_p147.png) 和 [核读报告](work/goal-20261006-wave2/three_coordinate_rank_bound/REPORT.md)。对应期刊来源为 Bouyukliev–Jaffe–Vavrek，IEEE Transactions on Information Theory 46(4), 1539–1544 (2000)，[DOI](https://doi.org/10.1109/18.850690)。本项目没有取得该期刊全文，不把书目信息冒充全文核读。

**E2：全支撑二元线性 $[40,7,18]$ 码至多有 172 个坐标等价类。** 作者论文 Table 6.2，印刷页 158 / PDF 第 160 页，给出 172 及偶重量集合，见 [表格截图](work/goal-20261006-wave2/dual4_mother_funnel/thesis_table6_2_p158.png)。2025 年 Bouyuklieva–Dzhumalieva-Stoeva 的 [Optimal Linear Codes and Their Hulls](https://www.mdpi.com/2227-7390/13/15/2491) 在 §2 / PDF p.2 说明全支撑约定，§5 / p.8 再得 172，Table A5 / p.16 给出 hull 分布 33、62、77；[本地 PDF](ecc_mathagent_harness_20260929/project/idea-stage/sources/bouyuklieva_dzhumalieva_stoeva_hulls_2025.pdf)。较早分类期刊来源为 Bouyukliev–Jaffe，Discrete Mathematics 226, 51–70 (2001)，[DOI](https://doi.org/10.1016/S0012-365X%2800%2900125-4)。该期刊全文同样没有在本项目中取得。

本项目没有从头重做 E1 或 E2 原作者的全部分类计算。当前书面证明准确的验收含义是 **在这两项已发表结果及所说明的计算正确性前提下，原命题得到完整排除**。本机重建的 172 个实际代表并不要求与原作者目录逐个同名；172 个两两不等价的合格对象，加上至多 172 类的外部上界，已足以证明覆盖。

部分早期工作笔记仍保存“只得到一个母码”“缺两类”等当时状态。它们是探索记录；当前覆盖以冻结 172 快照、最终清单和单卷证明为准。

## 4. 复现环境与轻量检查

需要 Python ≥ 3.10、`pynauty` 和支持 C++17 的 `clang++`。本机验收使用 Python 3.14.6、pynauty 2.8.8.1；C++ 核仅使用标准库。统一 pair driver 使用 Unix 的 `resource` 模块，已经在 macOS 运行。验收不需要 OR-Tools、ARIS、Grok/Gemini 账号或联网。

下面是**当前机器**可直接执行的命令。清单含当前项目的绝对路径，因此迁移到别的机器时必须保留完整证据树并重定位清单与输入中的路径，再核对输入绑定；本次没有把它包装成任意目录解压即用的便携包。

### 建立一个全新的复查输出目录

```sh
cd /Users/rfy_naiveai/Desktop/aris4math_v2
ECC_PY="$PWD/.venv-ecc/bin/python"
ECC_WAVE="$PWD/work/goal-20261006-wave2"
ECC_REPRO="$ECC_WAVE/global_closure/reproduce/reproduce.py"
ECC_OUT="$PWD/results/ecc-review-20261007"

"$ECC_PY" "$ECC_REPRO" prepare --output-dir "$ECC_OUT"
```

`ECC_OUT` 必须尚不存在；第二次复查换一个目录名。`prepare` 创建新的输出位置、暂存两个 manifest 脚本并链接只读输入，不启动搜索，也不覆盖原始结果。

### 检查 172 个实际母码及其不等价性

```sh
"$ECC_PY" "$ECC_REPRO" catalogue \
  --snapshot "$ECC_WAVE/global_closure/actual172_matrices.json" \
  --output-dir "$ECC_OUT/catalogue_check"
```

预期 `catalogue_check.json` 为 PASS：172 个秩 7、偶、距离 18、全支撑码；全部 21,844 个非零重量；hull 分布 33/62/77；172 个双色关联图 canonical 结果互异。图的一侧为 40 个坐标，另一侧为全部 128 个码字，只按这两侧着色，不添加会阻止合法等价的任意标签。

### 重建并读回逐例证据绑定

```sh
"$ECC_PY" "$ECC_OUT/global_closure/build_manifest.py"
"$ECC_PY" "$ECC_OUT/global_closure/check_manifest.py"
```

预期新 `manifest_check.json` 为 PASS：344 条母码到两套扫描输入的绑定、172 个完整 case、0 个 partial、F 总数 429,024、pair 总数 619,053,789。绑定通过显式坐标置换后的完整 128 码字集合相等建立；它不是仅比较文件哈希或重量谱。

这些命令还核对第二套实现的 32 维基、与母码合并后的秩 39、保存接受记录的 Gray 下标与实际向量，以及两套规范下 F 集合的完全相等。**它们不重新遍历 $2^{32}$ 域，也不逐个重放全部 pair。**

已有 [交付检查](work/goal-20261006-wave2/global_closure/reproduce/DELIVERY_CHECK.json) 记录这些命令在新 stage 的真实执行。其时 catalogue 用时 0.181 CPU 秒，builder 6.873 CPU 秒，独立读回 0.463 CPU 秒；这些数字仅是当时机器上的测量。

## 5. 计算检查：完整扫描与证书重放

### A. 重新执行完整 F 扫描

每个母码有 $2^{32}$ 个规范偶代表。第一套核采用低 6 位并行掩码，第二套核采用独立规范和实际 40 位 Gray 遍历。每套覆盖 172 个母码，总计 738,734,374,912 个代表；两套合计是这个数的两倍。

先编译到上一节创建的新目录：

```sh
clang++ -std=c++17 -O3 \
  "$ECC_WAVE/even40k7_rank3_extension/even_scan.cpp" \
  -o "$ECC_OUT/bin/even_scan"

clang++ -std=c++17 -O3 \
  "$ECC_WAVE/even40k7_rank3_extension/coverage_audit/full_replay/literal_gray_replay.cpp" \
  -o "$ECC_OUT/bin/literal_gray_replay"
```

下面只生成准确命令和核对输入，不执行完整扫描：

```sh
"$ECC_PY" "$ECC_REPRO" full-f --stage "$ECC_OUT" \
  --all --implementation both --cpu-seconds 120
```

如要完整复算，在同一命令加 `--run`：

```sh
"$ECC_PY" "$ECC_REPRO" full-f --stage "$ECC_OUT" \
  --all --implementation both --cpu-seconds 120 --run
```

预期 344 次完整运行均完成，逐例与归档 F 集合完全相等，每个实现的 F 总数均为 429,024。`--cpu-seconds 120` 是每个 native 进程的限额，不是整批限额。既有记录中两套总 CPU 分别为 1768.447900 秒和 2221.114856 秒，合计约 66.5 CPU 分钟。预算不足导致的中断或 partial 不能算通过。

只复查一例时，可把 `--all` 换成 `--case new172_hull14`，预期 F 数为 3,785；这仅验证这一例。不同实际运行须使用新的 stage，避免覆盖。现有 `reproduce/all172_dry_run_check.json` 已核对全部 344 条命令与输入；本次文档编写没有再次执行整批完整扫描。

### B. 重放所有配对拒绝见证

```sh
python3 "$ECC_WAVE/global_closure/pair_certificate_replay/replay_all.py" \
  --manifest "$ECC_WAVE/global_closure/COMPUTATIONAL_COVERAGE.json" \
  --output-dir "$ECC_OUT/pair_replay"
```

该命令编译独立检查器，先验证全部保存 F 的 54,915,072 项 F—码字实际距离，再逐个读取并验算全部 619,053,789 个拒绝见证。149 例为逐 pair 的 uint8 消息，23 例为 TSV；所有流的索引、记录数和严格 EOF 都被核对。每个见证给出 $u\in\mathbb F_2^7$，直接验证 $\operatorname{wt}(a_i+a_j+uG_K)<16$。

预期 `native_result.json` 为 PASS：`cases_completed=172`，`F_count=429024`，`pairs_replayed=619053789`，所有 invalid、sentinel、nonrejecting 均为 0，`F_domains_rerun=0`。完整实际输出见 [native_result.json](work/goal-20261006-wave2/global_closure/pair_certificate_replay/run_output/native_result.json) 及 [172 例记录](work/goal-20261006-wave2/global_closure/pair_certificate_replay/run_output/case_results.jsonl)。

已有重放实际读取 1,679,770,064 字节 pair 见证，native 用时 43.894951 CPU 秒，准备加 native 共 43.977642 CPU 秒，native 墙钟 56.947853 秒。现有 driver 设 native 硬 CPU 上限 118 秒、墙钟超时 150 秒；更慢机器若触及限额，应记录为未完成，不能据此前例宣称复现成功。

**这一步证明保存的 F 向量合格，且保存 F 上所有 pair 均不兼容；F 是否遗漏由 A 的完整遍历和对应数学论证承担。** 它也不重新证明外部 E1、E2。

## 6. 既有审阅、ARIS 的作用与证据边界

原全链证明已通过一次 fresh `proof-checker` 审计。该 reviewer 为 GPT-6-Astra / ultra，与主代理同属 OpenAI，记录为 `review_independence: same-family`、`acceptance_status: provisional`。它检查证明义务，并实际完成接受集的两种规范距离复算等限定检查；没有重新跑 344 个完整搜索域。完整记录见 [review_r1_fresh/REVIEW.md](work/goal-20261006-wave2/global_closure/review_r1_fresh/REVIEW.md)。

原全链的 Grok 与 Gemini 审阅也已完成，均给出 `SOUND_MODULO_STATED_IMPORTS_AND_COMPUTATION`。Grok 实际返回 `grok-4.7-build / xhigh`；Gemini CLI 记录选择 `gemini-3.8-flash-high / high`。Gemini 的选择记录并不是独立的服务端身份鉴定。两者没有亲自重跑全 F 或全 pair；统一 pair 重放由另行保存的确定性检查器执行。见 [原始回应及逐项核对](context/reviews/WAVE9_GLOBAL172_RECONCILIATION.md)。

**本次新写的中文单卷证明和这份 handoff，已经由 Grok、Gemini 分别审阅。** 两者均给出证明 `SOUND_MODULO_STATED_IMPORTS_AND_COMPUTATION`、handoff `ACCURATE`，未提出实质问题。它们独立核算关键推导，核读证据和复现说明，没有重新执行完整 F 或 pair 计算。新文档审阅的原始返回、实际范围与最终判定统一保存在 [本次交付审阅记录](context/proof-delivery-20261007/REVIEW_RECONCILIATION.md)。原全链审阅与这次文档审阅是两组不同记录。

ARIS 在此项目中提供的是研究组织和可追溯性：`research-wiki` 持续记录文献、已验证事实、失败路线和待闭合义务；`proof-writer` 组织完整推导；`proof-checker` 把覆盖问题拆成可查验义务；多代理分担实际母码重建、独立复算与来源核对；`render-html` 生成单卷阅读版。wiki 让接续任务能够直接从尚未解决的义务开始，并保留审阅意见被采纳或纠正的依据。见 [研究 wiki](research-wiki/index.md) 和 [恢复入口](NEXT_SESSION.md)。

跨模型咨询的具体贡献见 [完整证明第 29 节](PROOF_PACKAGE.html#29-grok-与-gemini-的具体贡献)：Gemini 的原生早退筛选建议推动了性能试验，具体位并行实现由本地研究完成；Grok 明确要求第二套完整 F 域复算，项目随后实际完成全部 172 类的独立扫描。后期两模型主要承担关键推导与交付说明的复核。这些角色分别按原始建议和后续执行记录归因。

这些工作流提高组织与检查效率。定理的依据仍是写出的数学论证、明确引用的外部结果及实际计算证据；wiki 的状态、模型票数和代理的“完成”标签本身没有证明力。本次没有提交人类同行评审结论，也没有声称普通 C++/Python/pynauty 执行等同于 Lean 内核检查。

## 7. 建议的反馈格式

请优先给出一个可以定位和判定的具体问题：

```text
查验者 / 日期：
实际阅读范围：
命题是否与原规格一致：
实际执行的命令、环境及输出路径：
问题位置（章/引理/公式/代码行/具体 case）：
问题及推导，或可复现反例：
影响（原命题 / 覆盖 / 计算证据 / 复现说明 / 仅表述）：
整体判断及仍未检查的部分：
```

例如，“某个 case 的见证文件提前结束”“某个规范化步骤遗漏偶陪集”“文献中的 172 只覆盖一个额外受限子类”都是可直接影响结论的问题，需要给出对应材料。若只是尚未执行昂贵复算，请如实记为未复算，不将它写成已经发现反例，也不将已保存的 PASS 写成你本人的运行结果。

## 8. 交付材料与继续工作

`PROOF_PACKAGE.html` 内嵌公式 SVG，离线打开即可阅读完整论证和矩阵附录；相对链接指向本项目的证据。单个 HTML 不包含约 1.68 GB 的逐 pair 原始见证流，也不能独自完成计算复现。进行计算复查时，需要一起保留 `work/goal-20261006-wave2/` 中清单所指的输入、结果和见证，以及上述文献 PDF 与验证程序。规范清单列出所有逐例路径。

移交到另一台机器时，应保留清单引用的完整证据文件，完成路径重定位和一次新目录复现；汇总 JSON 本身不能替代实际见证流。

原研究 Goal 已于 2026-10-07 按不存在性分支完成。本次是完整证明整理与复核交付。继续接手时，从单卷证明、此 handoff 和 [NEXT_SESSION.md](NEXT_SESSION.md) 进入；若发现实质缺口，应按其影响重新打开对应义务，并及时更新 research wiki。

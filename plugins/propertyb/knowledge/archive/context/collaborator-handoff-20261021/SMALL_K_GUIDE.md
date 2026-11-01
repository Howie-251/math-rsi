# Property B 小参数材料：阅读、来源与复算

本说明整理 `k=5,…,12` 的下界材料，日期为 2026-10-21。全部命题的原始对象均为任意有限简单 k 元超图；点对覆盖、有限点数窗口和锁点条件是证明内的约化，不是原命题新增假设。这里的 `m(k)≥L` 等价于至多 `L−1` 条边均可二染色。

本次仅清点现有源码、证书和既有日志，没有重新运行大表、Lean 或研究 Goal。以下状态区分完整纸面候选、实际算术重放和完整 Lean 验收。

| k | 阅读材料中的下界 | 可染边数预算 M | 主要阅读入口 | 已有核验及边界 |
|---:|---:|---:|---|---|
|5|35|34|`M5_GE35.html`；同名 Markdown|完整自然语言候选与分支证书；至多34边的无条件 Lean 主定理尚未闭合。已完整 Lean 验收的上一档是 `m(5)≥34`，见 `M5_GE34.html`。|
|6|65|64|`propertyB_small_k/propertyB_m6_proof.md`|200 个原 Fraction 局部型在本机重放通过；本次未作新的全链验收。|
|7|130|129|`propertyB_small_k/propertyB_m7_proof.md`|115 个原 Fraction 局部型在本机重放通过；未 Lean。|
|8|266|265|`propertyB_small_k/propertyB_k8_k9_proof.md`|1290 个原 Fraction 局部型在本机重放通过；未 Lean。|
|9|542|541|同上|2568 个原 Fraction 局部型在本机重放通过；未 Lean。|
|10|1112|1111|`propertyB_small_k/propertyB_k10_k11_research.md`|28545 个原整数外舍入局部型在本机重放通过；另有一个最紧双锁型独立 Fraction 复算。|
|11|2275|2274|同上|70472 个原整数外舍入局部型在本机重放通过；另有一个最紧双锁型独立 Fraction 复算。|
|12|4661|4660|`context/propertyb-general/k12-lock-pilot-20261021/DERIVATION_PACKAGE.md`|691429 个原整数外舍入型完整通过；第二实现完整核参数域、31 个 Fraction 边界型和全部3348个零／一锁型。两／三锁未第二次全量算术重放，未 Lean，保持计算机辅助证明候选。|

k=6,…,11 是合作者原材料；其方法和原始证明归属保持不变。六组重放总数为 **103190**，不是独立新分类、整图枚举或新的完整第三方验收。报告中静态数学阅读标为 same-family/provisional。k=12 是复用其一般锁点准则得到的新实例；已有 Grok 讨论审的是一般准则迁移，不是 M4660 整张数值表的最终审阅。这里不宣称这些数值为截至当前的最强公开纪录。

## 阅读顺序与文件位置

先读 `M5_GE35.html` 或其 Markdown 的原题约化、概率引理和全部点数分流，再按各章末证书索引查原 JSON。`context/propertyb34/round01/PAPER_CANDIDATE_MAP.md` 是 m(5)≥35 的源文件地图；`paper-audit/PROOF_AUDIT.md` 记录完整纸面候选的首轮审阅范围，`reviews/REVIEW_DISPOSITION.md` 记录跨模型关键义务的实际范围。它们不会使尚未完成的 Lean 自动成为完整证明。HTML 已内嵌公式，可离线阅读；本组原材料没有与上述每个小 k 下界一一对应的既有证明 PDF。

k=6,…,11 可先读根目录 [离线原稿合卷](../../PROPERTY_B_SMALL_K_6_11.html)，其 [Markdown](../../PROPERTY_B_SMALL_K_6_11.md) 逐字收入四份原稿。原文件仍在 `propertyB_small_k/`。`research-wiki/PROPERTY_B_SMALL_K_TRANSFER.md` 汇总原稿与脚本的公式、输入覆盖、103190 型实际重放和方法边界。详细命令、时长及原输出分别在：

- `context/collaborator-small-k-20261019/m6-m7/REPORT.md`、`EXECUTION.json`、`m6.log`、`m7.log`；
- `context/collaborator-small-k-20261019/m8-m9/REPORT.md`、`RUN_RESULTS.json`、`SCOPE_CHECKS.json`、`m8-stdout.txt`、`m9-stdout.txt`；
- `context/collaborator-small-k-20261019/m10-m11/REPORT.md`、`LOCAL_REPLAY_SUMMARY.json`、`LOCAL_REPLAY_K10.log`、`LOCAL_REPLAY_K11.log`、`INDEPENDENT_CHECKS.json`。

k=12 的完整数学重述在 `DERIVATION_PACKAGE.md`。同目录 `pilot/REPORT.md` 和 `pilot/M4660.json` 分别给逐段总结及全部逐 v 参数记录；`independent/REPORT.md`、`DOMAIN_CHECK.json`、`RESULT.json`、`INTEGER01.json` 说明第二实现的准确范围。`STRUCTURAL_TRANSFER.md` 保存较早迁移推导，末尾含当时“在途”快照；当前计算结果以 `pilot/REPORT.md` 和本说明为准，不把历史状态当最新结论。

## 环境与可移植运行方式

在解压包根目录运行，保留原来的 `context/`、`computations/`、`propertyB_small_k/` 相对层级。部分脚本从当前工作目录定位模块，部分从自身路径定位，不能把脚本单独移动到扁平目录。建议复制解压目录作为复算副本：验证器会重写自己的 `_VERIFIED.json` 或结果 JSON。所有命令均保留断言，**不要使用 Python 的 `-O`**。

Python≥3.10。k=6,…,9 原脚本及本文列出的 m5 独立算术重放使用标准库；k=10,…,12 的快速整数实现另需 NumPy。重新搜索 m5 的 LP 布局才需要 SciPy；现有精确证书重放不要求重新求解 LP。原本机日志主要使用 Python3.14，移植不要求复制 `.tools/` 或虚拟环境。

可按需准备环境，下面仅为用户复现命令，本次没有执行安装：

```sh
python3 -m venv .venv
.venv/bin/python -m pip install numpy
```

以下用 `.venv/bin/python` 表示该解释器。限制 BLAS/OMP 为单线程可重现原来的资源安排；机器速度不同，历史秒数仅作参考。

## k=6,…,11：完整原证书重放

```sh
.venv/bin/python -B propertyB_small_k/propertyB_m6_certificate.py
.venv/bin/python -B propertyB_small_k/propertyB_m7_certificate.py
.venv/bin/python -B propertyB_small_k/propertyB_m8_certificate_v2.py
.venv/bin/python -B propertyB_small_k/propertyB_m9_certificate_v2.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 .venv/bin/python -B context/collaborator-small-k-20261019/m10-m11/propertyB_k10_k11_verified.py 10
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 .venv/bin/python -B context/collaborator-small-k-20261019/m10-m11/propertyB_k10_k11_verified.py 11
.venv/bin/python -B context/collaborator-small-k-20261019/m10-m11/independent_checks.py
```

最后一条是两份最紧边界的独立 Fraction 重放，另含文档中明确标注的 k5 方法失败诊断；它不是六组全量第二实现。k6、k7 原完整运行约0.36秒、0.18秒；k8、k9约5.02秒、15.16秒，历史记录详见各 REPORT。原程序通过条件是全部实际枚举型的严格有理或整数上界小于1，不以展示小数作判定。

**k10/11 的依赖已平铺保存，毋须嵌套解 ZIP。** `propertyB_small_k/propertyB_k10_k11_verified.py` 导入同目录的 `propertyB_k10_k11_certified.py`，但后者原先仅在归档内；孤立复制该前者不能运行。上面的命令改用已有完整解包副本，其中有 `verified.py`、`certified.py`、`fast_exact_triple.py`、原稿和作者两份日志。其稿与 verified.py 与原目录同名文件逐字一致，清单不含原嵌套 ZIP。

## k=12：完整原计算与独立核查

从包根目录执行完整 M4660 计算：

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 .venv/bin/python -B context/propertyb-general/k12-lock-pilot-20261021/pilot/scan.py 4660 --seconds 350
```

原实测墙钟86.712秒、CPU84.620秒、峰值RSS42.8MB。慢机器可提高 `--seconds`；超时或失败前缀不能算完整通过。完成后检查 `M4660.json` 的 `complete=true`，候选 v 恰为93…782，四段型数依次419、2929、87807、600274，总计691429。

`scan.py` 复用已有解包副本中的 `FastExact` 和 `FixedCertificate`。统一分母为 `2^52`，概率项向上舍入，坏对扣除向下舍入；每个实际权表检查 int64 正项中间和界，最终总和用 Python 无界整数。新增 driver 对三锁 D 搜完整区间 `[d0,M]`，不沿用旧 helper 的 `d0+50` 截断。

包中同时保留先行 M4647 的完整结果。可直接用现有结果做汇总与标量重放；若要从头重建所有相关输入，先额外执行第一条：

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 .venv/bin/python -B context/propertyb-general/k12-lock-pilot-20261021/pilot/scan.py 4647 --seconds 350
.venv/bin/python -B context/propertyb-general/k12-lock-pilot-20261021/pilot/summarize.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 .venv/bin/python -B context/propertyb-general/k12-lock-pilot-20261021/pilot/replay.py
.venv/bin/python -B context/propertyb-general/k12-lock-pilot-20261021/independent/check.py
.venv/bin/python -B context/propertyb-general/k12-lock-pilot-20261021/independent/integer01.py
```

顺序有意义：`summarize.py` 为两个完整 JSON 补充度数范围、存在性余量和汇总字段，独立 checker 检查这些字段。`replay.py` 在原作者纯 Python 大整数路径重放两份 M 的七个分段最紧型并汇总全部使用表的溢出安全界；它不是691429型第二次全算。独立 `check.py` 不导入作者 scanner 或证书模块，它重建全部参数域并用 Fraction 重算31型。`integer01.py` 用另一分母 `10^20` 重算全部3348个零／一锁型。两／三锁的独立完整概率重放仍未完成；原实现的完整计算与第二实现的覆盖范围须分别报告。

保存的 M4670 结果是模式失败的前缀，`complete=false`，不构成下界4671，不应继续计算或补表来完成本次交接。

## m(5)≥35：分支证书复算入口

这份纸面证明按19…25点分流，算术资料分布在两轮目录，没有一个已经存在的单文件命令能重新证明全部纸面链。目录清单保留完整分支源、生成器、精确证书、覆盖绑定和既有日志。数学阅读要同时检查最小反例约化、选点存在、分类完整性与真实输入绑定；只执行概率重放不能替代这些推导。也不能执行未闭合的 `ThirtyFour/Assembly.lean` 后宣布目标已形式化。

下面给出有明确输入的现有独立重放／覆盖绑定命令，可分别运行。它们是所列分支的检查入口，不把这一短清单冒作整个 m5 新验收。

```sh
.venv/bin/python -B context/propertyb34/round01/twentyone-math/verify_exact.py context/propertyb34/round01/twentyone-math/MULTIPLE_SIX_WITNESSES.json
.venv/bin/python -B context/propertyb34/round01/twentyone-math/verify_exact.py context/propertyb34/round01/twentyone-math/SIX_WITH_SEVENS_WITNESSES.json
.venv/bin/python -B context/propertyb34/round01/twentyone-math/verify_exact.py context/propertyb34/round01/twentyone-math/EQUALITY_QUAD.json
.venv/bin/python -B context/propertyb34/round01/twentyone-math/verify_joint.py context/propertyb34/round01/twentyone-math/ONE_SEVEN_FIVE_DUAL_JOINT.json
.venv/bin/python -B context/propertyb34/round01/middle-math/audit_new23_certificates.py
.venv/bin/python -B context/propertyb34/round01/high-math/audit_v23_three_low.py
.venv/bin/python -B context/propertyb34/round01/high-math/audit_full24_matching.py
.venv/bin/python -B context/propertyb34/round01/high-math/audit_six_low_coverage.py
.venv/bin/python -B context/propertyb34/round01/high-math/audit_full25.py
```

21点其他最小度分支见同目录 `COMPLETE_TWENTYONE.md` 和 `REPORT.md`，其所有 witnesses 与 joint 文件均随清单保留。23点最小度七的完整入口是 `twentythree-seven-math/N23_MIN_SEVEN.md` 及 `N23_COMPLETE_DISPATCHER.md`；其 `STRICT_WITNESSES.json`、`SIX_DEGREE_THREE.json`、`SEVEN_SELECTED_STRICT.json` 等已经整理成 `verify_exact.py` 接受的同一 schema，可按相同调用格式传入，精确文件名以目录为准。其 joint 文件使用21点的通用 `verify_joint.py`，JSON 的 `source` 字段绑定对应原输入。

24/25点 audit 一部分是目录再生成与证书绑定，另一部分是独立注入概率／弱对偶重放；各脚本 docstring 和输出 JSON 记录准确范围。例如 `audit_full25.py` 重新核局部扩张、轨道及真实重数绑定，但不会重新计算每个九锁概率值；概率记录中的 `independent_ABC` 是既有计算字段。请依据所需义务选择脚本，而非把所有名为 audit 的脚本当成相同强度。

m5 验证器共享五个小模块：`computations/{multilock,independent_structure_bounds,enumerate_pair_partitions}.py` 和 `computations/propertyb33/round01/{pure_quota,avoided_lock_quotas}.py`。新旧轮次的分支脚本还互相导入 `low-math`、`high-math`；这些目录须保持原层级完整。NumPy/SciPy 求布局的提案脚本与无需 SciPy 的精确重放脚本都保留在源目录中，不必重新搜索布局才能阅读或核对保存的证书。

## 打包清单、体积与本次未完成事项

`small_k_paths.json` 是现存普通文件的根相对路径数组，原始证明／证据选择为831文件、457571627字节（436.37 MiB，压缩前）；另加入新合卷、生成器及其已有渲染依赖，最终清单为838文件。已排除嵌套 ZIP、`__pycache__`、pyc、Lean olean/ilean。较大的 m5 内容是实际局部目录与证书，不应作为“缓存”删掉；约160MB的 `twentyone-lean/unique-actual-r29-sample.txt` 等构建／抽样大文件未纳入。

主要体积：m5四个数学分支目录合计377721938字节，第一小时材料64214843字节，k12资料1802942字节；k6…11原稿／代码78988字节，既有重放材料306216字节。M5_GE35 离线HTML6278257字节，Markdown133399字节。清单中的少量 `formal/ThirtyFour` 文件只是正文链接对应的源码，完整Lean环境由总交接的形式化部分统一提供，不能单独据这两个文件构建整个工程。

新增 k6…11 离线合卷含347条内嵌公式，HTML2097888字节；生成器为本目录 `render_small_k.py`。重新生成时需已有 ARIS render-html helper／模板、Playwright与Chromium，并在同一 shell 设置 `ARIS_REPO` 指向实际 ARIS 仓库后执行 `python3 -B context/collaborator-handoff-20261021/render_small_k.py`。合卷阅读与数学证书重放不依赖这些渲染工具。

没有发现本清单所需的原稿、已存证书或明确依赖模块缺失。尚缺的质量层次仍是：m5≥35完整 Lean；k6…11新的完整独立全链验收；k12两／三锁第二次全量算术重放及新实例最终审阅／Lean。这些是现有成果的状态边界，本次文件整理不启动其后续工作。

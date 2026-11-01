# 复现入口核查：33、34、35与通用引理

核查日期：2026-10-14。以下命令依据现有源码、命令入口和已保存日志核对；本次打包未重新运行 Lean 或大表算术，也没有在另一台机器复现。所有相对路径均从解压后的项目根目录解释，除非命令明确先进入 `formal/`。

## 1. 三个数字对应三个不同命题

| 下界 | 超图边数上界 | 当前交付事实 | Lean 主入口 |
|---|---:|---|---|
| m(5) ≥ 33 | ≤32，即 T32 | 完整书面证明、完整 Lean 主定理及本机构建/原题审计 | `formal/Aris4Math/Main.lean` |
| m(5) ≥ 34 | ≤33，即 T33 | 完整书面证明、完整 Lean 主定理及本机构建/原题审计 | `formal/Aris4Math/ThirtyThree/Main.lean` |
| m(5) ≥ 35 | ≤34，即 T34 | 完整自然语言候选证明与局部精确证书；端到端 Lean 未完成 | `formal/Aris4Math/ThirtyFour/Assembly.lean` 仅证明目标与剩余义务等价 |

T34 的 `RemainingGoal` 仍包括：21点最小度7且七度点数为2、3或4；以及22–25点全部34边、点对覆盖输入。`OneAudit.lean`、`ManyAudit.lean` 中的 `conditional_original` 显式假设这个 RemainingGoal，不能将其编译成功解释成 m(5)≥35 已形式化。

## 2. 可移植的 Lean 重建命令

在查验者机器上安装 elan，并保证 `lean`、`lake` 在 PATH 中。保留随包的 `formal/lean-toolchain`、`formal/lakefile.toml`、`formal/lake-manifest.json`，无需设置作者的 ELAN_HOME，也不要用 `lake update` 改写依赖。

工具链固定为 `leanprover/lean4:v4.24.0`；manifest 中 Mathlib 提交为 `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`。首次工具链/依赖缓存下载需要联网。

从项目根目录运行：

```sh
cd formal
lean --version
lake exe cache get
lake build Aris4Math.Main
lake env lean ReviewAudit.lean
lake build Aris4Math.ThirtyThree.Main
lake env lean ReviewAudit33.lean
```

两份 ReviewAudit 用裸 `[Finite V]`、`Finset (Finset V)`、五元性和原始边数界复述命题，再调用实际主定理；它们用于命题对齐和公理核对，不是另一份独立数学证明。预期构建及审计均 exit 0，所列顶层声明的传递公理仅 `propext`、`Classical.choice`、`Quot.sound`。

默认 `lake build` 只指向旧的 `Aris4Math.Main`。请明确指定 T33 模块，不能凭默认构建判断新结果。

若只验证35的**已完成形式化范围**，在同一 `formal/` 工作目录运行：

```sh
lake build Aris4Math.ThirtyFour.Assembly
lake env lean ../context/propertyb34/round01/twentyone-lean/OneAudit.lean
lake env lean ../context/propertyb34/round01/twentyone-lean/ManyAudit.lean
lake build Aris4Math.ThirtyFour.TwentyThreeFewLowFourClassified
```

最后一个模块含23点3→4锁实际分类及80个严格局部项的调用。它保留22+19个残型，既不证明完整23点分支，也不证明35。覆盖与分类文件内自带相应 `#print axioms`。

构建含较重的局部精确计算，建议逐条执行上述命令，先看首个失败处；不要并发启动几套重构建。包内应只交付源码和依赖锁，不携带作者 `.lake/build`、`.olean` 或 `.tools/elan`。若查验者在已有目录主动要求重建本项目，可先用 `lake clean aris4math`，不必清理依赖缓存。

## 3. 对应的历史证据精确路径

### T32：m(5)≥33

- 主声明：`Aris4Math.propertyB_of_at_most_thirty_two : Target`。
- 另两入口：`two_colorable_of_at_most_thirty_two`、`non_propertyB_edges_ge_thirty_three`。
- 独立命题复述：`formal/ReviewAudit.lean`。
- 原构建：`.aris/traces/proof-checker/2026-10-06_run09/lean-main-build.log`。
- 原导入/公理审计：同目录 `lean-main-import-audit.lean`、`lean-main-import-audit.log`。
- 人工交接入口审计：`context/handoff/local-review-audit.log` 与同目录 JSON。
- 数学/形式义务对应：`context/FORMAL_VERIFICATION_PROGRESS.md`。

### T33：m(5)≥34

- 主声明：`Aris4Math.propertyB_of_at_most_thirty_three : Target33`。
- 另两入口：`two_colorable_of_at_most_thirty_three`、`non_propertyB_edges_ge_thirty_four`。
- 独立原题、每边两色及等价下界复述：`formal/ReviewAudit33.lean`。
- 显式新Main构建：`context/propertyb33/round02/final-assembly/main-build.log`、`main-build.meta.json`；日志为1138 jobs完成。
- 构建之后的原题审计：同目录 `original-statement-post-build-audit.log`、`original-statement-post-build-audit.meta.json`。优先采用这一 post-build 记录。
- 完整审计：`context/propertyb33/round02/final-audit/PROOF_AUDIT.md`、`PROOF_AUDIT.json`。
- 模型原回应与实际范围：`context/propertyb33/round02/reviews/REVIEW_DISPOSITION.md` 及所指原文件。

### T34：35的局部形式成果

- 准确剩余：`formal/Aris4Math/ThirtyFour/Assembly.lean` 的 `RemainingGoal` 与 `target_iff_remaining_goal`。
- 最新收卷：`context/propertyb34/round01/FINAL_30_MINUTES_REPORT.md`。
- 机器读状态：`context/propertyb34/round01/twentyone-lean/CHECKPOINT.json`。
- 21点唯一七度分支：`TwentyOneSevenOne.propertyB_of_one_seven`；`context/propertyb34/round01/twentyone-lean/build-unique-one-r35.log`、`OneAudit.lean`、`one-audit-final.log`。
- 21点至少五七度分支：`TwentyOneSevenMany.propertyB_of_many_sevens`；同目录 `build-many-r38.log`、`build-many-assembly.log`、`ManyAudit.lean`、`many-audit.log`。
- 23点首步实际分类：`formal/Aris4Math/ThirtyFour/TwentyThreeFewLowFour{Data,Numeric,Coverage,Classified}.lean`。
- 这一步的最新构建与六项公理输出：`context/propertyb34/round01/twentyone-lean/build-23-four-classified-r39.log`；完整1055 jobs。数据/算术的历史日志为同目录 `build-23-four-data-r26.log`、`build-23-four-numeric-r37.log`。
- 实际覆盖解释与 Python 重建记录：`context/propertyb34/round01/middle-lean/FOUR_PROMOTION_COVERAGE.md`、`FOUR_PROMOTION_COVERAGE_REPLAY.json`。
- 后续接口地图：`context/propertyb34/round01/twentyone-lean/DEGREE_SEVEN_CONTINUATION.md`。不要将源码已生成、单个batch已通过当作整个分支已构建。

## 4. 通用引理怎样核查

阅读入口为 `PROPERTY_B_TOOLKIT.html` 和 `research-wiki/PROPERTY_B_REUSABLE_LEMMAS.md`。该文逐组标明假设、证明、导出范围与 Lean 路径；一般索引定理、五元实际输入接口、仅纸面的推广分开。

可以在 `formal/` 中单独构建这些代表性模块：

```sh
lake build Aris4Math.ThirtyFour.MixedLayoutDual
lake build Aris4Math.ThirtyFour.BoundedAllocations
lake build Aris4Math.ThirtyFour.LockProjection
lake build Aris4Math.ThirtyFour.LockExtension
lake build Aris4Math.ThirtyFour.PromotionCatalog
lake build Aris4Math.ThirtyFour.PromotionReconstruction
lake build Aris4Math.ThirtyFour.MixedLayoutApplication
```

`MixedLayoutDual.quota_repair` 在任意有限索引、ℚ上证明容量修复弱对偶；`average_le`、`exists_strict_of_average` 是布局联合的代数核心。`MixedLayoutApplication.propertyB_of_mixed_layouts` 才把这类界接回实际五元超图。实际锁点投影/增锁接口中的“锁数可变”不等于已经将宿主五元边改成任意均匀度。

`BoundedAllocations.mem_enumerate` 证明容量剪枝不漏实际输入；它本身不是完整超图分类。`ThirtyThree.MultiLockRecovery` 的部分基础恒等式可复用，但末端 `realizes_recovered` 包装仍固定33边，不能直接当作34边接口。

## 5. 数学证书复算：工作目录、命令与依赖

以下命令均从解压后的**项目根目录**执行。Python 3.10及以上。脚本会写回对应 `_VERIFIED.json`、`_INDEPENDENT.json` 或覆盖报告；请在解压工作副本运行，保留原交付包供比较。这里只列已有入口，不建议无差别重跑所有研究生成器。

### 原T32算术与计数对照：仅标准库

```sh
python3 computations/enumerate_pair_partitions.py
python3 computations/reproduce_bounds.py
python3 computations/check_probabilities_by_permutations.py
python3 computations/independent_structure_bounds.py
```

前三类区分局部类型、精确概率和小实例公式测试。小实例排列测试不是一般计数证明；它是实现交叉核查。Python结果没有作为公理导入已完成的Lean证明。

### T34的21点：保存证书的精确重放，仅标准库

```sh
python3 context/propertyb34/round01/twentyone-math/verify_exact.py context/propertyb34/round01/twentyone-math/EQUALITY_QUAD.json
python3 context/propertyb34/round01/twentyone-math/verify_exact.py context/propertyb34/round01/twentyone-math/MULTIPLE_SIX_WITNESSES.json
python3 context/propertyb34/round01/twentyone-math/verify_exact.py context/propertyb34/round01/twentyone-math/SIX_WITH_SEVENS_WITNESSES.json
python3 context/propertyb34/round01/twentyone-math/verify_joint.py context/propertyb34/round01/twentyone-math/ONE_SEVEN_FIVE_DUAL_JOINT.json
```

相同 `verify_exact.py <文件>` 接口还可用于 `EIGHT_WITNESSES.json`、`MANY_SEVENS_WITNESSES.json`、`UNIQUE_SEVEN_WITNESSES.json`、`TWO_SEVENS_WITNESSES.json`、`THREE_FOUR_SEVENS_WITNESSES.json`；相同 `verify_joint.py <文件>` 接口用于各支已保留的 `*_STRICT_JOINT.json` 或报告明确采用的JOINT文件。不能把早期未完全严格的候选JOINT文件当最终证书。

**工作目录细节：** 21点 `verify_joint.py` 直接用 `Path(data['source'])` 读取输入JSON记录的来源。本次检查这些 `source` 都是项目根相对路径，没有作者绝对路径。只要在根目录执行上述完整相对命令即可；切到脚本目录再只传basename会失去该相对路径基准。

### T34的22/23点：仅标准库的独立重放入口

```sh
python3 context/propertyb34/round01/middle-math/verify_joint_layout.py
python3 context/propertyb34/round01/middle-math/verify_low_tables.py FOUR_LOW_22.json FOUR_LOW_23.json EXTEND_LOW_23_5.json EXTEND_LOW_23_6.json
python3 context/propertyb34/round01/middle-math/audit_new23_certificates.py
python3 context/propertyb34/round01/middle-math/low_coverage_audit.py
```

第一条无参数，绑定最初22点13残型与最终证书，输出 `THIRTEEN_INDEPENDENT.json`。第二条参数故意是basename：该脚本将每项解析为自身目录下的文件；不能给它重复的项目根相对前缀。第三条检查新23点一二低、四五低的保存证书及实际剖面绑定。第四条从点对预算重新生成四低域，属于局部覆盖核查。

### T34的24/25点：标准库覆盖/重放入口

```sh
python3 context/propertyb34/round01/high-math/verify_mixtures.py context/propertyb34/round01/high-math/SEVEN_MIXTURE.json 7
python3 context/propertyb34/round01/high-math/verify_joint.py context/propertyb34/round01/high-math/MIXED_SIX_JOINT.json mixed
python3 context/propertyb34/round01/high-math/audit_six_low_coverage.py
python3 context/propertyb34/round01/high-math/audit_seven_temporary_negative.py
python3 context/propertyb34/round01/high-math/audit_full24_matching.py
python3 context/propertyb34/round01/high-math/audit_full25.py
```

后两项涵盖较大的局部扩张域；不将其描述为秒级试跑。覆盖审计会重建/比较对应局部类型并核对已存证书的绑定；每项实际独立程度以脚本docstring和报告的scope为准。例如 `audit_full24_matching.py` 明示扩张生成器复用原实现，不是第二套完全独立的分类算法；`audit_full25.py` 包含独立局部提升递归，但部分直接界读取保存的已验精确值与 `independent_ABC` 标志，并非重算全部概率行。

### 23点三低完整域重建：额外导入依赖

```sh
python3 context/propertyb34/round01/high-math/audit_v23_three_low.py
```

该文件本身是覆盖与证书审计，但导入 `v23_three_low` → `extend_low` / `joint_layout_lp` 时加载 NumPy 与 SciPy，因此实际需要 `numpy`、`scipy`。保存系数的严格验算仍是有理数运算，浮点LP不是其结论依据。没有这些依赖时，不能把导入失败当成数学证书失败。

本次只核对依赖，没有安装或替查验者配置环境。完整重放需保留跨目录本地依赖：`computations/`、`computations/propertyb33/round01/`、`context/propertyb34-hour1-20261013/`、`context/propertyb34/round01/`。仅打包几份verify脚本会缺失实际导入和所读JSON。

## 6. 可移植性判断与最小修改建议

- 本文列出的主要数学核查脚本通过 `__file__` 定位项目根，或在约定的项目根工作目录解析相对路径；没有发现需要替换作者 `/Users/...` 的执行路径。保持包的原目录结构即可。
- 历史 `formal/README.md`、原Mac运行示例和日志内包含作者的 `.tools/elan` 绝对路径。合作者使用本文的PATH版命令；无需修改数学源码，也无需复制工具链。
- 如未来希望21点 `verify_joint.py` 支持任意工作目录，最小修改是将 `Path(data['source'])` 的相对路径基准改为脚本已算出的 `ROOT`；这是可选便利，不是当前根目录命令的阻塞。本次未改此脚本。
- 若希望 `audit_v23_three_low.py` 在纯标准库环境工作，最小工程修法是将生成器模块里的 NumPy/SciPy 及求解器导入延迟到真正的搜索函数中。当前交接应如实列依赖，不以空壳模块或伪造结果绕过导入。本次未改数学/生成脚本。
- 旧T33打包器 `context/propertyb33/round02/final-audit/build_review_bundle.py` 只以T32和T33 Main为导入闭包根，不能直接用来交付35现状。新包至少另含完整T34源码/支持模块、上述当前审计、全部纸面分支与所用证书。打包测试成功不表示从解压包重新构建过Lean。

本文核查范围是路径、复现命令、入口范围和导入依赖。纸面论证、有限分类覆盖、实际输入与证书的连接，以及查验者自己的数学判断仍须在对应证明正文和源码中检查。

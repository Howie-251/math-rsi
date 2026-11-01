# Lean 复现与源码交接

本说明对应 2026-10-21 的交付快照。包内保留完整 `formal/` 源码，包含已完成的 T32、T33、一般 k≥12 增长定理，以及暂停中的 T34 工作。此次交接只检查源码、导入和既有日志，没有重新运行 Lean，也没有恢复研究。

## 固定环境

需要 Git、可用网络及 elan（Lean 工具链管理器）。elan 的官方安装入口是 <https://github.com/leanprover/elan#installation>。安装后使 `elan`、`lean`、`lake` 在 PATH 中可用。以下命令从解压后的项目根目录运行，不需要原作者的用户名或 `.tools/elan`：

```sh
elan toolchain install leanprover/lean4:v4.24.0
cd formal
lean --version
lake exe cache get
```

`lean --version` 应显示 Lean 4.24.0。`formal/lean-toolchain` 会为这个目录选择该版本。`lake exe cache get` 按已有 manifest 获取 Mathlib 及其依赖并下载匹配缓存；新机器首次需要网络和磁盘空间。请保留 `lake-manifest.json`，不要把 `lake update` 当作复现步骤。

固定配置为：

- Lean：`leanprover/lean4:v4.24.0`。
- Mathlib：`v4.24.0`，锁定提交 `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`。
- 其余依赖的精确提交：`formal/lake-manifest.json`。
- 项目配置：`formal/lakefile.toml`，无外部本地路径依赖。

包中不携带原作者的 `.tools/elan`、`.lake` 或编译产物。已有运行时间多为依赖缓存保留时的增量构建，不能据此预计新机器的首次耗时。尤其暂停的 T34 含较重的有限算术模块；复现已完成成果时请只构建下面选定的入口。

## 选定成果的精确命令

以下命令均在 `formal/` 目录执行。第一条编译指定主模块及其真实依赖；第二条在构建后独立编译原题复述，打印定义、声明类型和传递公理。

|成果|指定构建|构建后原题审计|
|---|---|---|
|一般定理，全部自然数 k≥12|`lake build Aris4Math.General.Growth.Twelve`|`lake env lean ReviewAuditGeneralGrowth12.lean`|
|T32：至多32边可染，m(5)≥33|`lake build Aris4Math.Main`|`lake env lean ReviewAudit.lean`|
|T33：至多33边可染，m(5)≥34|`lake build Aris4Math.ThirtyThree.Main`|`lake env lean ReviewAudit33.lean`|

**默认 `lake build` 只构建 `Aris4Math.Main`（旧 T32）。** 它不能代替 T33 或一般定理的指定构建。也不要用全库构建验证已完成成果，因为完整源码中同时保留了暂停研究。

从项目根目录也可选用随包脚本：

```sh
bash context/collaborator-handoff-20261021/scripts/check_lean.sh general
bash context/collaborator-handoff-20261021/scripts/check_lean.sh t32
bash context/collaborator-handoff-20261021/scripts/check_lean.sh t33
```

不传参数时只运行 `general`。脚本不安装工具、不更新依赖、不获取缓存，也不构建暂停的 T34。环境安装与缓存下载按上一节先行完成。建议根据所需成果选择一条命令，而非默认执行全部。

旧的一般 k≥17 结果及 RS 试点也完整保留，按需可运行：

```sh
lake build Aris4Math.General.Growth.Main
lake env lean ReviewAuditGeneralGrowth.lean
lake build Aris4Math.General.RS.PilotMain
lake env lean ReviewAuditGeneralRSPilot.lean
```

复现当前 k≥12 主结果不需要先单独运行这两组命令；Lake 会处理其导入依赖。

## 当前已完成的命题

T32、T33 都量化任意有限顶点类型及简单五元边集，不以点对覆盖、固定顶点数、正则性或平衡染色为外部假设。对应主导出分别为 `Aris4Math.propertyB_of_at_most_thirty_two` 和 `Aris4Math.propertyB_of_at_most_thirty_three`。

一般主导出 `Aris4Math.General.RS.propertyB_of_general_growth_twelve` 量化任意有限类型 `V`、`E : Finset (Finset V)` 和自然数 k≥12。只假设每条原边基数为 k，以及 `E.card ≤ rsBudget k + integerGain k (rsBudget k)`，输出每条原边同时含 true 和 false 的 Bool 染色。

其中 `rsBudget k` 是本文指定精确 RS 积分判据在**全部正整数预算**中的最大元；不是把有限截断、概率见证或内部证书列为外部假设。`integerGain k M` 是 `floor(sqrt(M)/(8(1+log k)))` 的自然数下取整；已证明在 k≥12、M=`rsBudget k` 时至少为2。故得到 `m(k) ≥ rsBudget k + integerGain k (rsBudget k) + 1`。审计文件直接展开原积分、最大性的全域量词及原 Bool 染色结论。

已有正式构建及构建后审计记录中，所查顶层定理和原题复述的传递公理都仅有 `propext`、`Classical.choice`、`Quot.sound`；没有 `sorryAx`、新增未证公理或 `native_decide`。这些记录是原作者本机执行证据。接收者按上述命令执行并保留自己的输出后，才形成接收者的独立复现记录；审计文件使用现有证明，并非另一份独立数学证明。

一般比较定理 D/E 仍是纸面结论，未在这里完成 Lean。图中 C.2 的具体数值求值、锁点数值候选及其他小参数成果也不能因为一般主定理已编译而被称作逐项 Lean 核验。

## 暂停中的 m(5)≥35 形式化

目录 `formal/Aris4Math/ThirtyFour/` 对应 T34：至多34边可染，即 m(5)≥35。目录名表示边数预算，不表示已经证明 m(5)≥34 的旧 T33。这里保留大量已完成的内部支和未接齐的模块；完整 T34 主定理尚未闭合，研究仍暂停。

`ThirtyFour/Assembly.lean` 明确说明 `This file does not prove T34`。其 `target_iff_remaining_goal` 只证明原目标与 `RemainingGoal` 的等价，不提供剩余义务的证明。暂停检查点列出的 Lean 缺口为：21点恰2/3个七度点；22整支；23至多六个六度点；24至少一个六度点的剩余支；25整支连接；最终 Main、原题审计及终审交付。已有完整纸面候选与 Lean 未闭合状态应分别阅读，不能以 Assembly 编译成功宣称 m(5)≥35 已形式化。

准确停止点见 `context/propertyb34/round02/PAUSE_CHECKPOINT_20261015.md`。后来的 m(5)≥36 纸面探索也继续暂停，见 `context/propertyb35-paper/PAUSE_HANDOFF_20261021.md`；它不改变上述 Lean 完成范围。

## 源码完整性及可选生成器

此次静态检查在排除 `.lake`、`.git`、`.tools` 后发现4,133个项目 `.lean` 文件（68,326,255字节），无源码符号链接；所有 `Aris4Math...` 导入均能在 `formal/` 中找到。外部导入仅来自 Lean 和 Mathlib，依赖由 manifest 固定。所需项目导入闭包为：T32共38模块、T33共171模块、一般 k≥12 共27模块；暂停 Assembly 共715模块。为保留后续研究，请打包完整 `formal/`，无需根据闭包删文件。

`.lean` 源码中未发现构建时读取外部文件、运行外部进程或原作者绝对路径的调用。`formal/generate_numeric_certificate.py` 是可选的旧静态数据生成器，会读取 `results/reproduced_bounds.json` 并改写已有 `Numeric.lean`；已生成的 Lean 数据已在源码内，正常复现不需要运行生成器。若要维护并重生成它，另带上该 JSON。其他研究脚本与历史原数据属于数学过程证据，不是上述 Lean 构建的运行依赖。

`lean_paths.json` 汇总必需源码、入口、证据和排除规则。正文报告中的原作者绝对路径是历史执行位置；复现请使用本说明的相对路径命令。

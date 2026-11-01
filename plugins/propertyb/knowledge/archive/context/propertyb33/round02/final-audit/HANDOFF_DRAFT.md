# T33 人工查验交接稿

本项目已经在 Lean 中证明：任意有限顶点集上的简单五元超图，只要边数至多 33，就存在使每条边同时含两种颜色的染色。因此 **m(5) ≥ 34**。这不确定 m(5) 的等号。

本交接稿正在补齐最后的统一构建记录和模型终审，尚未作为最终交付版本发布。主定理的直接编译和独立原题导入已经通过；以下命令与入口均指新 T33。

## 查验顺序

先读 `context/propertyb33-preparation/FORMAL_SPEC_PROPERTYB_33.md` 固定原命题，再读 `proofs/propertyb33/PROOF_PACKAGE_DRAFT.md` 的完整推导。其前四节给出无损约化、条件排列计数、实际迹重数、坏边对扣除与分类覆盖；第 5–11 节处理全部 19–25 点分支；第 12 节汇总严格有理界。

然后检查 `formal/ReviewAudit33.lean`。它使用裸的有限顶点类型、五元子集边集和 33 边上界，调用新主定理，导出每条边中真、假两色都存在。这能直观确认 Lean 所证明的对象与原题一致。

证明链的关键入口是 `formal/Aris4Math/ThirtyThree/Main.lean`，导出：

```lean
Aris4Math.propertyB_of_at_most_thirty_three : Target33
Aris4Math.two_colorable_of_at_most_thirty_three
Aris4Math.non_propertyB_edges_ge_thirty_four
```

前两个证明原染色命题，第三个给不可二染色超图至少 34 边的等价表述。顶层没有点对覆盖、顶点数、度数、局部表、概率界或证书存在性作为额外假设。

## 本机复现

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd /Users/rfy_naiveai/Desktop/aris4math/formal
lake build Aris4Math.ThirtyThree.Main
lake env lean ReviewAudit33.lean
```

工具链固定为 Lean 4.24.0，Mathlib 与其他依赖由 `formal/lake-manifest.json` 锁定。默认 `lake build` 仍构建旧 T32；查验本结果必须指定上述新模块。

在另一台已安装 elan 的机器上，从交接包的 `formal/` 目录执行：

```sh
lake exe cache get
lake build Aris4Math.ThirtyThree.Main
lake env lean ReviewAudit33.lean
```

保持随包的 `lean-toolchain`、`lakefile.toml`、`lake-manifest.json`；复现不需要运行 `lake update`，也不需要 ARIS、Grok 或 Gemini 账号。依赖下载与数学构建是不同步骤；首次构建包含较重的局部精确计算，安静运行一段时间不等于失败。

## 已有证据与逻辑基础

`context/propertyb33/round02/final-assembly/` 保存实际执行命令、退出码、直接编译及原题导入日志。独立原题导入打印了原对象、Property B 和 Target33 的定义，以及八项顶层声明的传递公理。输出全部只有：

```text
propext
Classical.choice
Quot.sound
```

没有 `sorryAx`、新增未证公理或 `native_decide` 依赖。独立导入文件是对原命题的独立表达和真实调用，不是第二份独立数学证明，也不表示另一位研究者已经重建成功。

## 数学阅读重点

1. 最小顶点反例中合并不共边点，及补至恰 33 边，是否保持所需反证方向；整数度数如何排除 26 点以上。
2. 贪心失败只被 critical-pair 事件覆盖；单边端点与单交有序边对的条件排列公式是否使用正确的无放回联合计数。
3. 锁点、实际坏边对和标签置换是否在随机排列前选定；真实边的精确迹是否与数值输入逐项一致。
4. 全部局部分类是否覆盖实际输入，特别是三低分支允许低三点迹重数二、六锁允许五元迹但排除六元迹、25 点八锁三元族的完整十四型分类。
5. 扣除是否基于真实不同坏边对，是否正确处理两个有序方向、零权重和配额重叠，并先改 C 项再取逐位置最小值。

这些义务均在新主定理的形式依赖链中。局部有限数据的核验是证明的一部分；随机整图样例和未找到反例不承担全称结论。

## 如何反馈

请给出文件、定理或公式位置，说明具体前提、可疑推理及影响范围。有反例时列明对象并检查它满足被质疑结论的全部前提；有构建问题时附实际命令、Lean 版本和首个相关错误。文字笔误、形式命题不一致、数学缺口和复现环境问题分别处理。

原 T32 规格、证明包与交接保持独立保存。本次交接只针对 T33，不开启新的 34 边研究目标。

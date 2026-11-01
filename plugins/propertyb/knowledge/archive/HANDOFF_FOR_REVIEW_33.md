# T33 人工查验交接：m(5) ≥ 34

本项目已经在 Lean 中证明：任意有限顶点集上的简单五元超图，只要边数至多 33，就存在使每条边同时含两种颜色的染色。因此 **m(5) ≥ 34**。这不确定 m(5) 的等号。

显式构建 `Aris4Math.ThirtyThree.Main` 已完成 1138 jobs，随后独立原题导入通过；八项顶层声明的传递公理均只有 Lean 的标准三项。完整数学正文、源码和实际执行记录可一起交给查验者。

## 阅读与源码入口

- [单卷离线证明 HTML](PROOF_PACKAGE_33.html)：完整定义、约化、概率引理、19–25 点全部分支和精确界。
- [正式数学规格](context/propertyb33-preparation/FORMAL_SPEC_PROPERTYB_33.md)：原始对象、量词与验收结论。
- [完整证明 Markdown](proofs/propertyb33/PROOF_PACKAGE.md)：与 HTML 对应的数学正文。
- [主定理源码](formal/Aris4Math/ThirtyThree/Main.lean)与[原题独立复述](formal/ReviewAudit33.lean)。
- [形式核验说明](context/propertyb33/FORMAL_VERIFICATION.md)、[完整审计](context/propertyb33/round02/final-audit/PROOF_AUDIT.md)与[构建原始记录](context/propertyb33/round02/final-assembly/REPORT.md)。
- [转交包](aris4math_t33_review_bundle.zip)：可读证明、所需项目源码、依赖锁定文件、审计和复现记录。

建议先读规格，再读正文前四节的无损约化、条件排列计数、实际迹重数、坏边对扣除与分类覆盖。第 5–11 节处理全部 19–25 点分支，第 12 节汇总严格有理界，第 13 节对应 Lean 实现。

然后检查 `formal/ReviewAudit33.lean`。它以裸的有限顶点类型、五元子集边集和 33 边上界表达原题，调用新主定理，导出每条边中真、假两色都存在。证明链的主入口导出：

```lean
Aris4Math.propertyB_of_at_most_thirty_three : Target33
Aris4Math.two_colorable_of_at_most_thirty_three
Aris4Math.non_propertyB_edges_ge_thirty_four
```

前两个证明原染色命题，第三个给不可二染色超图至少 34 边的等价表述。顶层没有点对覆盖、顶点数、度数、局部表、概率界或证书存在性作为额外假设。

## 复现

在另一台已安装 elan 的机器上，解压交接包并进入其中的 `formal/` 目录：

```sh
lake exe cache get
lake build Aris4Math.ThirtyThree.Main
lake env lean ReviewAudit33.lean
```

工具链为 Lean 4.24.0，Mathlib 与其他依赖由 `lake-manifest.json` 固定。保留随包的 `lean-toolchain`、`lakefile.toml` 和 `lake-manifest.json`；不需要运行 `lake update`，也不需要 ARIS、Grok 或 Gemini 账号。默认 `lake build` 仍构建独立保留的旧 T32；查验本结果须指定新模块。首次构建包含较重的局部精确计算，依赖缓存下载完成后仍可能运行较长时间。

在原 Mac 上可以使用已有项目工具链：

```sh
export ELAN_HOME=/Users/rfy_naiveai/Desktop/aris4math/.tools/elan
export PATH="$ELAN_HOME/bin:$PATH"
cd /Users/rfy_naiveai/Desktop/aris4math/formal
lake build Aris4Math.ThirtyThree.Main
lake env lean ReviewAudit33.lean
```

## 已有证据与审阅范围

`context/propertyb33/round02/final-assembly/` 保存实际命令、退出码和原始日志。其中 `main-build.log` 记录新 Main 的 1138 jobs 构建成功；`original-statement-post-build-audit.log` 记录其后独立原题导入、具体定义、导出类型和八项传递公理。输出全部只有：

```text
propext
Classical.choice
Quot.sound
```

没有 `sorryAx`、新增未证公理或 `native_decide` 依赖。本机执行为保留锁定缓存的增量构建，独立导入调用同一套数学证明；尚未据此声称其他研究者或另一台机器已经复现。

Grok 与 Gemini 的最终跨家族审阅均已有效返回，在各自实际阅读范围内未发现命题不对齐或实质数学缺口。两者静态读取源码及日志，没有执行 Lean。fresh proof-checker 对完整正文的两项轻微统计说明纠正已落实；同家族意见仍保留 provisional 属性。模型原回应与处置见 [REVIEW_DISPOSITION.md](context/propertyb33/round02/reviews/REVIEW_DISPOSITION.md)，数学接受依据是完整证明、实际命题与 Lean 核验，不是模型投票。

## 数学阅读重点

1. 最小顶点反例中合并不共边点，及补至恰 33 边，是否保持所需反证方向；整数度数如何排除 26 点以上。
2. 贪心失败被临界边对事件覆盖；单边端点与单交有序边对的条件排列公式是否使用正确的无放回联合计数。
3. 锁点、实际坏边对和标签置换是否在随机排列前选定；真实边的精确迹是否与数值输入逐项一致。
4. 全部局部分类是否覆盖实际输入，特别是三低分支允许低三点迹重数二、六锁允许五元迹但排除六元迹、25 点八锁三元族的完整十四型分类。
5. 扣除是否基于真实不同坏边对，是否正确处理两个有序方向、零权重和配额重叠，并先改 C 项再取逐位置最小值。

这些义务均在新主定理的形式依赖链中。有限局部数据与分类覆盖属于证明的一部分；随机整图样例和搜索未命中不承担全称结论。

## 反馈

请给出文件、定理或公式位置，说明具体前提、可疑推理及影响范围。有反例时列明对象并检查它满足被质疑结论的全部前提；有构建问题时附实际命令、Lean 版本和首个相关错误。文字笔误、形式命题不一致、数学缺口和复现环境问题分别处理。

原 T32 规格、证明包与交接独立保存；本交接针对至多 33 边的 T33。

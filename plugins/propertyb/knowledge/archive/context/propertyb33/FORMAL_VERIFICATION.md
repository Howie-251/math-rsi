# T33：原主定理的形式核验

**原命题已由端到端 Lean 证明：任意有限简单五元超图，至多 33 边即有 Property B，故 m(5)≥34。** 七个点数分支、局部分类与真实输入连接都在证明内部。2026-10-13 的显式 `lake build Aris4Math.ThirtyThree.Main` 完成 1138 jobs；随后的独立原题导入与八项传递公理审计也全部通过。

## 原声明与独立原题表达

新入口为 `formal/Aris4Math/ThirtyThree/Main.lean`：

```lean
Aris4Math.propertyB_of_at_most_thirty_three : Aris4Math.Target33
```

`Target33` 展开为任意 `V : Type u`、`[Fintype V]` 和 `H : Simple5Hypergraph V`，从 `H.edges.card ≤ 33` 推出 `PropertyB H`。`Simple5Hypergraph` 的唯一数据是有限边集和每边恰五点；`PropertyB` 是一个 Bool 染色，使每边真色点数为一至四。

`formal/ReviewAudit33.lean` 独立写成：

```text
任意有限类型 V，任意 E : Finset (Finset V)，
若每个 e∈E 的大小为5且|E|≤33，
则存在 c : V→Bool，使每个e同时含一个真色点和一个假色点。
```

它实际调用新主定理，不输入点对覆盖、点数范围、正则性、概率界、分类表或证书。`non_propertyB_edges_ge_thirty_four` 与独立 `original_lower_bound` 给出等价下界。

## 已执行的核验

|检查|实际结果|证据|
|---|---|---|
|23点六支装配|直接编译exit0|`round02/final-assembly/twenty-three-direct.log`|
|新原主定理Main|直接编译exit0|`round02/final-assembly/main-direct.log`|
|独立原题导入|exit0，完整原类型|`round02/final-assembly/original-statement-import-audit.log`|
|八项顶层传递公理|均为标准三项|同上|
|显式Lake构建新Main|1138 jobs，exit0|`round02/final-assembly/main-build.log` 与同名 `.meta.json`|
|Lake构建后再次独立导入|exit0，八项传递公理均为标准三项|`round02/final-assembly/original-statement-post-build-audit.log` 与同名 `.meta.json`|
|最终Grok C|有效返回，实际静态审阅范围内未发现实质缺口|`round02/reviews/grok_final_C.json`|
|最终Gemini C|全新会话 retry1 为 SUCCESS，实际静态审阅范围内未发现实质缺口|`round02/reviews/gemini_final_C_retry1.json`|
|单卷HTML保真|PASS；离线桌面与手机检查通过|`.aris/traces/render-html/2026-10-13_t33_run01/review.json`（项目根目录下）|

实际命令、耗时和退出码在 `round02/final-assembly/EXECUTION_SUMMARY.json`。上述 Lake 构建保留了锁定依赖与已验证模块的缓存，随后原题导入的输出与先前直接编译后的审计一致。

Grok 与 Gemini 均读取源码和已有输出，没有执行 Lean；其意见与本机实际构建分开记录。Gemini 首次最终 C 调用因连接错误未完成，没有计为通过；有效结论来自上述新会话。两个有效回应中的旧“构建在途”描述已被本表的后续实际输出覆盖。详细审阅范围与处置见 `round02/reviews/REVIEW_DISPOSITION.md`。同家族的正文与 HTML 审阅保留 `provisional` 标记；本记录不表示已有他人或另一台机器完成复现。

## 证明义务地图

最小顶点反例通过合并不共边点得到点对覆盖；平衡染色排除至多18点，整数度数排除至少26点，再补边到恰33边。`ThirtyThree/Assembly.lean` 将19、20、21、22、24、25点与23点合成有限目标，`Reduction.lean` 返回任意有限原对象。

23点的六支分别为无六度点、至少四个六度点、恰三个、恰两个，以及唯一六度点的两类七度邻接。`TwentyThreeComplete.lean` 穷尽全部分支。每支都由真实选点产生实际迹、共度和坏槽；有限目录的覆盖及标签运输有证明，实际重数由点对、度数和边数恒等式恢复。

条件排列计数按无放回联合空间计算。真实坏边对的两个方向、零权重、子族配额重叠及逐位置 `min` 均在形式链中处理。有限内核计算核验明确类型与精确有理数，未枚举所有超图。

逐项假设的产生和消除、定理接口与依赖图见 `round02/final-audit/PROOF_SKELETON.md`。可读证明为 `proofs/propertyb33/PROOF_PACKAGE.md`；离线版为根目录 `PROOF_PACKAGE_33.html`。

## 逻辑基础

原主定理及原题复述的传递公理只有 `propext`、`Classical.choice`、`Quot.sound`。没有 `sorryAx`、新增未证公理或 `native_decide` 依赖。源文本检索用于辅助诊断；最终依据是实际导出类型和传递公理输出。

独立数学审阅发现两处正文汇总错误，已修正：21点最大界为3292/3315；三低完整带标签域1796项，先规范低预算后844项。两项均未改变Lean源码或原命题。原回应、独立复算与处置保留在final-audit及proof-checker trace中。

## 复现

在 `formal/` 目录，用锁定的 Lean 4.24.0 及 `lake-manifest.json`：

```sh
lake build Aris4Math.ThirtyThree.Main
lake env lean ReviewAudit33.lean
```

本机工具链见 `formal/README_T33.md`。另一台装有elan的机器可先执行 `lake exe cache get` 下载锁定依赖的缓存，再执行以上命令；不要运行 `lake update` 更换依赖。默认 `lake build` 仍是旧T32入口。

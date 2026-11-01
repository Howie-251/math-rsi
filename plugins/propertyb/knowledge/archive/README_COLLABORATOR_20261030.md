# Property B：最新合作者查验包

2026-10-30 · 小参数下界、一般增长定理与完整源码证据

本包集中提供 **k=5–12 的具体整数下界**及**全部 k≥12 的统一增长定理**，附完整证明、局部证书、验算程序、Lean 源码、固定依赖和已有审阅记录。m(k) 是不具有 Property B 的有限简单 k 元超图的最少边数；Property B 指存在二染色，使每条边同时含两色。原命题允许任意有限顶点集。

## 先读什么

请先完整解压 ZIP，再打开 **START_HERE.html**。页面与补充资料按相对路径连接，核心数学阅读页的公式和图已经嵌入，可离线阅读。

1. [总览、比较图与一般定理](PROPERTY_B_GENERAL_BOUND.html)：统一定义—定理—证明及准确文献定位。
2. [小参数查验指南](context/collaborator-handoff-20261030/SMALL_K_GUIDE.md)：最新正文、全部证据、程序入口和准确核验范围。
3. [一般定理指南](context/collaborator-handoff-20261030/GENERAL_GUIDE.md)与[完整 Lean 阅读页](PROPERTY_B_GENERAL_LEAN.html)：一般主定理的数学及形式证明连接。
4. [Lean 复现说明](context/collaborator-handoff-20261030/LEAN_REPRODUCE.md)：新机器的固定环境及准确主模块命令。
5. [通用引理阅读页](PROPERTY_B_TOOLKIT.html)：可复用数学工具与方法。

## 本次具体下界

|k|固定参考下界|本包下界|增益|最新阅读入口与状态|
|---:|---:|---:|---:|---|
|5|32|35|3|[M5_GE35.html](M5_GE35.html)：完整纸面候选；35 的 Lean 尚未闭合。另附已完成 Lean 的 m(5)≥33、≥34。|
|6|64|67|3|[M6_GE67.html](M6_GE67.html)：完整计算机辅助证明，全部分支独立精确复算；Grok/Gemini 整卷静态终审。|
|7|128|131|3|[最新正文](context/propertyb-m7-131-20261029/PROOF_M7_GE131.md)：424 型全量独立复算；尚无跨家族终审。|
|8|263|267|4|[八／九元阅读页](M8_M9_IMPROVEMENTS.html)：2094 型全量独立复算，299 组件配额另核；Grok/Gemini 整卷静态终审。|
|9|538|543|5|同页：3450 型全量独立复算及完整决策树重建；Grok/Gemini 整卷静态终审。|
|10|1085|1112|27|[合作者原稿合卷](PROPERTY_B_SMALL_K_6_11.html)：保留原证明与原证书重放状态。|
|11|2245|2275|30|同上；两项的完整程序依赖、日志及边界复算均随包保留。|
|12|4633|4664|31|[最新正文](context/propertyb-k12-4664-20261029/PROOF_M12_GE4664.md)：664355 型完整原计算及固定切点重跑；独核全域与20个 Fraction 型，Grok 指定覆盖链静态审阅。|

6、8、9 的当前验收为 **sound-modulo-imports**，尚无相应 Lean；审阅者静态读取正文、源码和日志，未执行程序。7 的全量独算、12 的覆盖／部分算术独核与各自审阅范围分别记录，不合并为同等强度的验收。上表固定参考集合不是穷尽文献的世界最佳声明。

旧合卷中的 k6–9 数值65、130、266、542及旧 k12 页面4661按历史理解；当前值以本表和各最新正文为准。原合作者材料和归属完整保留。

## 一般定理与紫色数值

对每个 k≥12，B_RS(k) 是本文组合 RS 正关联估计与精确积分后定义的最大整数接受预算，Δ(k)=floor(√B_RS(k)/(8(1+ln k)))。已完成端到端 Lean：任意有限简单 k 元超图在边数≤B_RS(k)+Δ(k)时可二染，且 Δ(k)≥2，因此 m(k)≥B_RS(k)+Δ(k)+1。

|k|固定参考包络|统一公式的保守下界|加强判据 C.2 直接求值|锁点法具体下界|
|---:|---:|---:|---:|---:|
|12|4633|4635|4647|4664|
|13|9539|9542|9564|本包无新完整锁点结果|

蓝色统一定理、紫色 C.2 数值与红色锁点结果各有自己的证据。C.2 数值经精确证书和独立区间／递推复算；比较 D/E 为纸面结论，均未逐项 Lean 化。

## 在新机器复现

按 [Lean 说明](context/collaborator-handoff-20261030/LEAN_REPRODUCE.md)准备 elan 后，从解压包根运行：

```sh
cd formal
lake exe cache get
lake build Aris4Math.General.Growth.Twelve
lake env lean ReviewAuditGeneralGrowth12.lean
```

Lean 固定为4.24.0，依赖由 manifest 固定。首次下载需要网络；不要执行 lake update 更换依赖。默认 lake build 仍只构建旧 T32，不能代替上面的一般主模块。T32/T33 的准确复现命令及小参数 Python 复算见相应指南。

小参数可用[便携复算入口](context/collaborator-handoff-20261030/PORTABLE_REPRODUCE.md)，先运行 `python3 context/collaborator-handoff-20261030/scripts/replay.py --list` 查看各模式的实际范围。入口在独立工作副本运行，原始证书和日志保持不变。

## 文件与交接范围

- `proofs/`、`ref/`：规范证明与实际使用的文献。
- `formal/`：完整 Lean 源码、固定依赖声明及原题审计文件；不带工具链和编译缓存。
- `propertyB_small_k/`、`context/`：合作者原稿与各次最新证明、原始证书、独立实现、日志和审阅记录。
- `research-wiki/`、`figures/propertyb_bounds/`：方法积累及可复用矢量图。
- `PACKAGE_CONTENTS.txt`、`PACKAGE_CHECKS.json`：归档文件清单及本次可移植性检查记录。

本次是现有成果的交接快照：检查归档、相对链接和源码依赖；不把打包成功记为新一轮数学验收或 Lean 构建。旧35形式化／36研究继续暂停。本包不包含也不操作独立编码理论项目。反馈请附具体定理、文件位置、疑问或失败命令及输出。

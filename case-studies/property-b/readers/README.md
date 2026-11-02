# Property B 原始成果阅读页

这些完整阅读页来自先前使用 ARIS 开展的 Property B 研究。MathRSI 随后从这些研究及其实际转折中提炼工作流；这些页面不是 MathRSI 从头运行该研究的记录。

可以直接在克隆仓库中打开 HTML。公式与图以原有 SVG 内嵌，页面不需要网络、MathJax、构建步骤或作者机器。通过本地 HTTP 服务浏览时，链接的 Markdown、Lean、JSON 和日志也可作为原始文件读取。

| 阅读页 | 内容与范围 |
| --- | --- |
| [一般下界完整正文](PROPERTY_B_GENERAL_BOUND.html) | 一般整数增益定理、明确参考界比较、小参数成果及其各自状态；当前小参数展示包括五至十二元的 35、67、131、267、543、1112、2275、4664。 |
| [一般下界完整 Lean 阅读页](PROPERTY_B_GENERAL_LEAN.html) | 全部 k≥12 的一般增长下界及原题调用、构建和传递公理审计；对应的完整 Lean 源码复用插件 archive。 |
| [RS 核心与十七元 Lean 试点](PROPERTY_B_GENERAL_LEAN_PILOT.html) | 当时试点阶段的完整报告。后续一般增长成果见上一页；保留原有阶段状态。 |
| [六元 m(6)≥67](M6_GE67.html) | 完整计算机辅助证明、各分支和独立算术复核；本参数没有 Lean。 |
| [八元与九元改进](M8_M9_IMPROVEMENTS.html) | m(8)≥267、m(9)≥543 的完整证明、覆盖与独立精确复算；两参数没有 Lean。 |
| [十二元锁点比较](K12_LOCK_COMPARISON.html) | 2026-10-21 的历史 m(12)≥4661 候选与方法比较。后来 4664 的状态和正文由一般下界页及其直接链接的规范源提供；不将这份旧页更新为新证明。 |

原文的结论、假设、证明、表格、公式、图、阶段状态和生成元数据全部保留。唯一 HTML 改动为本地 `href`／`src` 路径，使其指向这里的阅读页、已有 `plugins/propertyb/knowledge/archive/`、本案例补入的直接证据或图件。原目录链接 `context/propertyb-general-lean-pilot/reviews/C` 明确指向其现存 `DISPOSITION.md`。

`sources/` 保留六份原阅读稿；`evidence/` 只补入 HTML 直接引用、原插件 archive 尚未包含的 82 份证据。它们没有改写。原文中的作者机器命令和绝对路径是历史复现记录；新机器使用 [案例首页的克隆复现命令](../README.md#inspect-or-reproduce)；[原 Lean 工程说明](../../../plugins/propertyb/knowledge/archive/formal/README.md)保留历史路径和当时默认构建目标。这次打包没有安装工具链、重新运行数学程序或 Lean，也没有扩大任何成果的验证状态。

本地链接验证的范围是六份 HTML 的所有直接 `href`／`src` 目标和 HTML 锚点。链接进入既有 archive、原始 Markdown、源码或日志之后，其中的历史相对链接、外部网站及原机器路径不属于递归搬运范围；它们保留来源语境。这份案例不是整个历史工作区的镜像，也不包含所有历史 ZIP。引用论文已复用 archive 中的 PDF。

在任意目录可以运行不依赖原工作区的检查：

```sh
python3 /path/to/math-rsi/case-studies/property-b/tools/package_readers.py --check
```

维护者如仍持有原 Property B 工作区，可显式传 `--source /path/to/original/workspace` 重建便携副本并执行全文保真比较。适配器只复制和改链接，不渲染新数学。完整逐链接转换、来源相对路径、原始字节数和修改时间见 [PORTABILITY_MANIFEST.json](PORTABILITY_MANIFEST.json)；实测范围与结果见 [PORTABILITY.md](../../../development/propertyb-case-20261102/PORTABILITY.md)。

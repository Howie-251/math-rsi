# Property B 阅读页便携化记录

本次把已存在的完整离线阅读页带入 MathRSI 案例，不重新渲染正文，也不运行研究、数学验证程序、模型审阅或 Lean。原研究先于 MathRSI；MathRSI 提炼其工作流，而非产生这些历史结果。

来源是原 Property B 工作区中 2026-11-02 实际读取的文件。源工作区只读，ECC 工作区未读取。逐文件来源相对路径、原文件大小与修改时间保留在 `case-studies/property-b/readers/PORTABILITY_MANIFEST.json`。HTML 原有 `aris:source-path`、原有源稿 SHA256（原页有则保留）与生成时间全部保留；它们描述原始渲染，不改写为本次打包时间。原有四份带 SHA256 的页面与对应原源稿相符；六元和八／九元原页没有该字段，本次没有补造。

## 转换与包含范围

六份完整 HTML 共 12,816,124 字节：

| 文件 | 便携副本字节 | 数学容器 | SVG 元素 | 本地 href/src 次数 |
| --- | ---: | ---: | ---: | ---: |
| PROPERTY_B_GENERAL_BOUND.html | 5,544,284 | 1049 | 1105 | 90 |
| PROPERTY_B_GENERAL_LEAN.html | 587,477 | 118 | 122 | 37 |
| PROPERTY_B_GENERAL_LEAN_PILOT.html | 187,194 | 11 | 11 | 61 |
| M6_GE67.html | 3,958,749 | 902 | 948 | 143 |
| M8_M9_IMPROVEMENTS.html | 1,416,420 | 256 | 280 | 45 |
| K12_LOCK_COMPARISON.html | 1,122,000 | 232 | 234 | 26 |

合计 2568 个数学容器、2700 个 SVG 元素、402 次本地链接／资源引用。数学容器和 SVG 数量分别统计；一个 SVG 不一定是一条公式。

适配器只重写普通 HTML `href`／`src` 的本地文件路径，保留 query／fragment，不改 SVG 的 `xlink:href`、文本、样式或元数据。对应目标分为六份阅读页、已有插件 archive 文件、补入的直接原始证据、原始阅读稿及案例图件。唯一目录到文件映射是 RS 试点的 `reviews/C` 转到已有 `reviews/C/DISPOSITION.md`，避免克隆读者依赖文件服务器列目录。

补入的 94 个支持文件共 9,456,137 字节：

- `readers/evidence/`：82 个直接 JSON／日志／回复等文件，8,244,218 字节。
- `readers/sources/`：六份原始阅读稿，273,965 字节，包括两份由原有元数据指定的 `reader-source.md`。
- `assets/`：当前 `delta.svg`、`delta.png`、`small.svg`、`small.png`，以及页面直接链接的 `overview.svg`、`propertyb_bounds.pdf`，共 937,954 字节。

重复的文献 PDF、规范证明、Lean 源码和已归档证据继续引用已有 `plugins/propertyb/knowledge/archive/`，没有再复制整个历史 archive 或 ZIP。K12 旧比较页继续准确保留 4661 的当时范围；较新的 4664 完整材料由主阅读页链接既有 archive 的证明、独核与审阅处置。

## 实际检查

运行：

```sh
python3 case-studies/property-b/tools/package_readers.py --source /path/to/original/property-b/workspace
python3 case-studies/property-b/tools/package_readers.py --check
```

第一次对六份页面逐一反向应用记录的链接转换，得到与原 HTML 完全相同的全文；所有 94 个复制文件也与原文件逐字节相等。这个检查同时覆盖公式 SVG、正文、表格、图和状态，而不是仅比较提取文本。第二次在不提供原工作区的条件下检查克隆可用的本地目标；不会覆写首次全文保真报告。

六份页面的全部 402 次本地 `href`／`src`（含 HTML 锚点）均可解析；零缺失，零远程 `src`。页面没有 script、外部样式表或 CSS `url()` 运行时依赖。结果见 [PORTABILITY.json](PORTABILITY.json) 与 [PORTABILITY_CLONE_CHECK.json](PORTABILITY_CLONE_CHECK.json)。

另用 Microsoft Edge headless 的独立浏览上下文，在阻断全部 HTTP(S) 请求时打开六份本地页面，分别检查 1440×1000 与 390×844 视口。十二组均无页面错误、失败请求或页面级横向溢出。主正文与 Lean 页的桌面／手机首屏及实际证明段共八张截图已逐张目视检查，公式和正文可读，窄屏长代码保留内部横滚。六元页 902 个数学容器中 901 个显示，余一个位于原 CSS 隐藏的重复正文标题；不是证明公式缺失。各页闭合 lightbox 内原有无 src 的空 img 也不属于请求失败。详细结果与截图路径见 [BROWSER_READERS.json](BROWSER_READERS.json)；此次没有改动 CSS 或内容。

检查没有递归验证历史 archive 或原始 Markdown 内的所有链接。它们属于保留来源语境的研究材料；其中原机器命令、旧运行入口、未打包的旁支与外部链接均不承诺由本案例完整镜像。HTML 中的原机器命令仍是历史记录，新克隆的 Lean 使用入口是案例首页 README 的 `Inspect or reproduce`；插件 archive 的 `formal/README.md` 仍保留原机器路径和历史构建目标。不因可读、链接可用或复制完整就提升历史数学验收等级。

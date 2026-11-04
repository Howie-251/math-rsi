# Ruskey–Savage 猜想 n=6 完整研究包

先读 **START_HERE.txt** 与 **guide/** 的五份导读；打开 **index.html**，或双击 OPEN.cmd。所有显示页、源码、证书及轨迹均在本目录内，不依赖 E 盘、F 盘或 CDN 阅读。整体移动目录后仍可阅读和执行清单校验。

## 成果

P6：任意 Q6 短边匹配、任意自由根、任意异奇偶目标（含已覆盖目标）的 Hamilton 路延拓。结合已发表完美匹配定理，得到完整六维 Ruskey–Savage 圈结论；结合有限维提升框架，得到任意维数至多六方向的圈延拓。

保证等级 same-family/provisional。原证明包是计算辅助证明，不是外部同行评议或证明助手形式化证明。

## 文件导航

- index.html：离线汇总、嵌入讲稿、搜索全部文件。
- Ruskey-Savage_Q6_研究报告.html / .md：最新成果、文献表、详细证明主线。
- Ruskey-Savage_Q6_证明资料汇编.html / .md：231份原始证明/审读材料的可展开汇编。
- research/six_directions：全部现存证书、搜索源码、程序、日志、失败尝试、审计与状态原件。
- research/openai_math_20261031：最初文献研究的现存材料；目录为空时不补造内容。
- trajectories：本研究根会话及显式子代理的可见对话、工具执行、会话索引和审计依赖。
- ARIS_framework：ARIS当前框架快照，含proof-writer/proof-checker说明、模板与工具。
- literature：取得的参考论文、来源与SHA-256。
- runtime：便携Python；VERIFY.ps1与REPLAY_FINAL.ps1使用该运行时。
- PACKAGE_MANIFEST.json：全部交付静态文件的SHA-256清单。
- REPRODUCE.md / SELF_CONTAINED.md / ARIS_RSI_GUIDE.md：复现、边界与后续迭代。

## 快速校验

在本目录运行 `powershell -ExecutionPolicy Bypass -File .\VERIFY.ps1` 校验所有绑定文件；约需读取整个包一次。

运行 `powershell -ExecutionPolicy Bypass -File .\REPLAY_FINAL.ps1` 重新执行原始最终总装检查。输出写入verification_runs，不改原始证据。

不要直接在冻结目录运行带生产输出的搜索程序；先复制到新实验目录。所有历史失败与条件性状态按原样保留，应以最终P6_FULL_REVIEW.json的范围为准。
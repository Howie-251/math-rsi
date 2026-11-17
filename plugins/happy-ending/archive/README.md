# Happy Ending原件归档

来源：用户提供n7-upper-bounds-20261103展开包。`source/`保留原相对路径：source/report.md、working/package/整个原数学发布包（含proofs/source-tree与sat-756的源码、历史收据、25点颜色及95项evidence）、figures/与根render_report.py。当前归档291文件、13,859,415字节，未修改原件。

排除working/reference：该目录标题与wiki实为误带的Degree–Diameter材料，不能作为本案例知识库。排除working/z重复展开包、备份/预览/QA、重复压缩包，不以重复载体增加成果数。working/package内部为原发布数学组织保留其嵌套结构、figures与renderer；不为去重破坏原链接。

原包本来未提供的55原始CNF、TB级证明主体、历史checker二进制及部分封存生成闭包没有被“补齐”。注册表中的原Linux路径仅用于历史追踪；本克隆不隐含依赖作者服务器。没有25点平面坐标，只有抽象色表；两份Lean摘录属对照工作，缺其依赖模块，不是本项目形式化工程。

实际阅读：本次作者完整读source/report.md、CURRENT、sat-756 README、独立checker；消费已有READING_REPORT、STRUCTURAL_CHAIN、SAT_EVIDENCE和RESEARCH_LESSONS的详细取证并核关键原件路径，未声称逐字读完约14MB全部历史。已有intake的原阅读范围保存在[evidence/intake](../evidence/intake/)供核对，保持“当时未运行SAT/Lean”的原文，不把其静态阅读改写成本次执行。

renderer作为原件保留，不是新任务默认命令。根renderer可能查作者上层helper；包内working/package/render_report.py可找相邻rendering/aris_render_html.py，仍需matplotlib等原依赖，本轮未运行渲染。当前可直接执行的复核入口是插件tools/check_lower25.py；没有为展示需要改数学源稿。

## 2026-11-08 增量：完整75/76新原件

`n7-20261103/`逐字复制用户原包`aris4math/mathrsi_new_results/n7-upper-bounds-20261103-proofs/`，303文件、16,258,090字节。保留原报告、四份新数学主稿及更新、全部包内依赖/历史/源码/SAT收据、图与renderer、来源清单和两份文献PDF；原相对结构不改，旧`source/`归档原样保留。与旧档案重复的依赖用于保持新包自包含，不按重复份数计新增知识。

主导航[n7-20261103/proofs/CURRENT.md](n7-20261103/proofs/CURRENT.md)，本轮整理层为[取等与交换](../skills/mathrsi-happy-ending/references/equality-exchange.md)。复制不是重放：55份TB级证明、checker二进制等原缺件仍未补齐；两份Lean摘录仍不构成完整工程。新75/76/ES77工作证明及regular共同根条件定理保持same-session/unreviewed/unaccepted。历史稿的旧界和开放余类是当时状态，当前源稿结论从CURRENT顺读，不能覆盖新稿，也不能因新稿语气升级验证。

本轮亲读新主稿：替锁75/76、依赖/单through、t=0、regular共根，及全供给原稿；核旧根§1–3等关键依赖，复用已有v3阅读与源状态，不声称本轮重读整个历史archive。固定小反例和25见证的执行范围另记于维护使用报告。新任务对本目录只读，输出写自己的任务目录。

## 2026-11-17 增量：N(m,r,s) 七、八、九参数与一般 m 综合交接包

`nmrs-20261117/` 从完整交付包 `NMRS-results-20261117(1).zip`（1,608 文件，269.89 MiB）中逐字节原样收录 **955 份文件（48.18 MiB，单文件最大 9.56 MiB）**，详见 [nmrs-20261117/README.md](nmrs-20261117/README.md) 与 [nmrs-20261117/INVENTORY.json](nmrs-20261117/INVENTORY.json)。主交接文档 [nmrs-20261117/HANDOFF.md](nmrs-20261117/HANDOFF.md) 的全部 125 处本地相对链接均在本目录内完整可达；全部五套有限证书（`run-988-d2`、`run-d9-d3` 含 `fractional-grid.json`、`milestone9`、`octagon-source-replay/finite-inputs.zip`、`lock-blocks/q5` 与 `E21/color.tsv`）均随仓保留并经跨平台核验通过。仅省略预渲染 `reading/*.md.html`、`milestone9.tgz` 重复包及 $\ge 2\text{ MiB}$ 的中间探索 `.cnf/.drat/tmp` 文件（SHA-256 完整登记于 `INVENTORY.json`）。源包中 22 次外部 `claude-review-deep` CLI 调用均因宿主机返回 `exit_code=1, tool_calls=0` 未完成，所有新增结构与装配稿如实保持 `unreviewed / unaccepted` 工作证明状态。

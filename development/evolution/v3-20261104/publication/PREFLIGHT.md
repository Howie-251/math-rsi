# v3 publication preflight — 2026-11-04

只读核查截至本地HEAD `1586b611`，分支`feat/mathrsi-v3-evidence-evolution`；未改README或其它维护入口。本轮用户已授权发布，以下给Root/Gemini同步成稿及实际push/PR/merge状态，不把尚未执行的远端动作写成完成。

## 版本史应讲清的事实

- **v0**是独立ARIS基础研究工具及早期领域研究阶段，不是本仓现存固定tag。不能暗示已发布一个可下载v0快照。
- **v1**固定`847490841644a78d83100a06ecc84e552974444f`。实读git tree为**9项**MathRSI base技能；Property B已实质接入，ECC入口存在但为草案，尚无DD插件。
- **v2**固定`67dfbeba27fe49377cffa136143dab2f1cc3390f`。增加`mathrsi-meta-evolve`成为**10项**base技能，吸收DD研究并加入DD插件及定点流程修正。ECC当时仍草案；旧标签应保持原状。
- **v3**在现有v2上增强工作集/全域/接受best、标记运输、有限全称机制与失败资产复用、Lean显式参数读取；base仍10项。同一ECC插件第二轮升级并新增ecc-certificate；新增超立方体极值、Hamilton延拓和Happy Ending三个领域，当前六领域十四领域技能。
- ECC叙述保留**v0初始成果→继承v1/v2方法与workflow继续深化→反馈v3**。不要求每次研究动作严格调用固定release；旧172母码双扫/43-10保持历史归属，新Lean/实际矩阵连接及便携证书是深化，45/11距离17仍开放。
- **PR #7是流程patch**：`679e6241`改4文件、9增3删（派活/实际产物交付/恢复快照），由`8bbdb828`合入main，已吸收到v3分支；不是另一次研究驱动迭代，也不是v3本身。可一笔说明，不占主版本时间线。

证据来自本地`git rev-parse v1^{} v2^{}`、两个tag的实际树、PR7本地提交差异与当前EVOLUTION；未据用户记忆移动任何tag。

## 发布动作完成后须同步的准确位置

| 文件与当前行 | 现文问题 | 最小同步建议 |
|---|---|---|
| `README.md:5` | says local branch / not tagged or pushed | Gemini主写版本史后，按真实发布阶段改状态；实际创建v3 tag后才补该固定tag和ZIP链接，v1/v2保留 |
| `README.md:194` | “The local v3 implementation” | 发布合并后改“v3”，保留真实检查和review范围 |
| `README.zh-CN.md:5` | 本地完成，尚未tag/push | 与英文同一版本和实际远端状态；不要只更新一版 |
| `docs/QUICKSTART.md:5` | local development branch, not a published tag | 成功发布后改当前v3入口，保留记录实际checkout revision的做法 |
| `docs/V3_CHANGES.md:3` | local / not tagged or pushed | 发布后改实际v3 tag/PR；四项base变化和十技能事实不变 |
| `docs/V3_CHANGES.md:98` | local implementation, not published tag | 与首段同步，PR7只是patch的解释保留 |
| `docs/EVOLUTION_WORKFLOW.md:31` | 通用说明误称“现有v1” | 改“现有版本”，避免将未来维护固定回v1 |
| `docs/EVOLUTION_WORKFLOW.md:47` | “DD是本轮v1→v2”“本轮记录” | 标为v2历史案例，再补当前v3案例/记录链接 |
| `docs/EVOLUTION_WORKFLOW.md:57` | “当前v2”及旧本轮记录 | 将v2标历史，并给当前v3四项动作、新领域与EVOLUTION入口 |
| `AGENTS.md:3,9` | 顶部仍v3本地完成/未推送 | 新增或修顶部current，记录本次授权、实际PR/merge/tag；下方历史快照保留 |
| `development/evolution/v3-20261104/EVOLUTION.md:3,43` | 本地完成/未push/未PR/未tag | 用实际动作结果更新当前状态与恢复入口，不改研究/核验历史 |

两README对旧图已准确标**v2历史快照**，其中ECC draft/future-v3是图的历史状态；可保留不重画。当前文字领域表已替代ECC draft默认排除。Happy75/76仍待原件，局部证书重放不是全题数学终审；这些事实不因发布而改变。

## 本次新增文件的有界检查

只检查`git diff --name-only --diff-filter=A origin/main...HEAD`列出的新增路径，不扫描原研究或用户磁盘。当前origin/main=`8bbdb828a478a8a842189527b5a4216aecfaa548`。

- 新增8769路径，其中8757常规文件（其余为发现链接），常规文件合计353619813 bytes。
- **没有>100,000,000 bytes的单文件**。最大为`plugins/hypercube-extremal/archive/source/research/Q4_059970530_research/full_C.npz`，5194410 bytes。
- **没有意外编译产物**：新增文件中未发现`.so/.dylib/.dll/.o/.obj/.exe/.pyc/.olean`，也未发现ELF、Mach-O或PE可执行magic。科学`.bin/.npz`是已登记输入/证书，不作为编译产物误报。
- 检查时工作树干净；随后仅新增本PREFLIGHT文件。后续Gemini/Root写入的文稿不在本轮数字内，数目变动不需重跑数学。

结论：本次新增科学资产无GitHub单文件大小障碍，无需清理编译物；当前真正待同步的是版本史表达与发布状态入口。

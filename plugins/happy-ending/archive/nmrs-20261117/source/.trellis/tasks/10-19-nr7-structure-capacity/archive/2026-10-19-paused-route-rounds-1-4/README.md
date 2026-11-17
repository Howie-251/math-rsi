# 四轮原文完整归档

日期：2026-10-19。

**已暂停路线：尚未降低无条件全局 gap；新数学稿未独立审阅或正式验收。**

本次完整保存整理前的 10 个根文件及 research/00–16 共 17 个文件，总计 27 份原文。snapshot/ 保留历史相对布局及原始字节；归档前已记录 SHA256 和字节数，归档后逐文件核验一致。

将要重写的 check.jsonl、design.md、implement.jsonl、implement.md、prd.md、STAGE_SUMMARY.md、task.json 共 7 个根文件先复制入 snapshot；ROUND1–3 和整个原 research 目录在核对绝对源/目标路径都位于本任务内后移动入 snapshot，未删除历史。

原文中的旧相对引用未改写，应根据 MANIFEST.json 的 original_absolute_path 及原任务根目录解析；归档内部材料可按 snapshot 对应路径找到，外部依赖仍在原位置。

归档中的旧待办、路线建议和继续请求均为历史记录，**不是当前指令**；snapshot 中旧 task.json 的 notes 或文档状态也不覆盖当前暂停入口。归档不改变任何结果的接受状态，不提升旧证明或新稿的审阅保证。

当前入口为[方向重置后的起点](../../STAGE_SUMMARY.md)，不是精确恢复的初始文件。当前研究暂停，等待用户重新指定研究方向。唯一成果标准为降低无条件全局 gap，条件引理不算达标。四轮 gap 粗上界均为 19/28/72/174，累计改善 0；粗上界不是精确 gap。

## 轮次映射

| 轮次 | 原文范围 |
|---|---|
| 第一轮 | [ROUND1_SUMMARY.md](snapshot/ROUND1_SUMMARY.md) 与 research/00–04；04-round-log.md 为累计日志 |
| 第二轮 | [ROUND2_SUMMARY.md](snapshot/ROUND2_SUMMARY.md) 与 research/05–10 |
| 第三轮 | [ROUND3_SUMMARY.md](snapshot/ROUND3_SUMMARY.md) 与 research/11–13 |
| 第四轮 | [原 STAGE_SUMMARY.md](snapshot/STAGE_SUMMARY.md) 与 research/14–16 |

10 个根文件中其余管理文档同样是整理前的原文，内容可能跨轮次累计；本映射不拆分或改写任何原文件。

## 原文、源路径与校验清单

[MANIFEST.json](MANIFEST.json) 是全部 27 份原文的机器可读清单，包含 original_task_relative_path、original_absolute_path、snapshot_relative_path、sha256、bytes。original_task_relative_path 相对于本任务根目录，snapshot_relative_path 相对于本归档目录。以下逐项链接原文；绝对源路径及完整哈希以清单为准。

| 原任务相对路径 | snapshot 原文 | 字节数 | SHA256 |
|---|---|---:|---|
| check.jsonl | [原文](snapshot/check.jsonl) | 485 | fc28671fb19016ce6ff2b2f04447ccd5489f3784a97bc019fbbb785c72f0ec39 |
| design.md | [原文](snapshot/design.md) | 897 | 5a313386883018e08f015ea1d6b6a62327db90acca9f70df50b01e9e3af75e3d |
| implement.jsonl | [原文](snapshot/implement.jsonl) | 501 | 31cee52993928b65bbff96770bb7dc47e1f02869c785edbc64e9fffe51cd8016 |
| implement.md | [原文](snapshot/implement.md) | 3076 | 64907afa62b6275553e4b3b4762a22f64eaec12591d08839c8c018cc635d9e45 |
| prd.md | [原文](snapshot/prd.md) | 2137 | 36adcfcc5af34c4402cb2f588dfe0c1ecf0bb6ec21ca89ef84cb3c60aa930ffa |
| research/00-foundations.md | [原文](snapshot/research/00-foundations.md) | 5165 | 973889d121cdf434cd25fab83329e5dbccf3a46393b211bb9a65e89e64a0d655 |
| research/01-general-lemmas.md | [原文](snapshot/research/01-general-lemmas.md) | 6302 | 5c3b543a645725c5c25042cdbb0436f936ad8dd23ff62a6e09cc9dd5dcbb451e |
| research/02-cross-group-structure.md | [原文](snapshot/research/02-cross-group-structure.md) | 7367 | 2288c23d51a3fb7f6f71b3d5c163210c786aed27d55f299a4d83e44a98eea577 |
| research/03-migration-and-obstacles.md | [原文](snapshot/research/03-migration-and-obstacles.md) | 7741 | 44f435352dfdf51a121be118d61e7ac0020b87e3f0c2565db4c5df4ac8423c1b |
| research/04-round-log.md | [原文](snapshot/research/04-round-log.md) | 5153 | 4c2d567c0c9315e3731e7f79f7e1b44df51125454615e9351387f7b4e8aac73a |
| research/05-core-overlap-and-extreme-structure.md | [原文](snapshot/research/05-core-overlap-and-extreme-structure.md) | 6298 | 02ece624140b8d2dd72eb5a859a0b725b83a4632e11897705b68e95e082db83e |
| research/06-hole-transport-and-sharp-budgets.md | [原文](snapshot/research/06-hole-transport-and-sharp-budgets.md) | 5631 | ce832dc53b2f065ac0955ec8c1437d9b54c65340abfbfffc9b5c7959673d1207 |
| research/07-two-colour-balance-766.md | [原文](snapshot/research/07-two-colour-balance-766.md) | 5922 | 6cad0f4dd6ff94365ecd05ca3a2bb9559e5f910f4e027e639056c8c6f06a625e |
| research/08-interval-descent-and-cover-obstacles.md | [原文](snapshot/research/08-interval-descent-and-cover-obstacles.md) | 6647 | 62be788614ed6d45f71df6af6e324199bdd3ce215a8468e480454be6ee3d1033 |
| research/09-general-capacity-function-and-stability.md | [原文](snapshot/research/09-general-capacity-function-and-stability.md) | 5804 | 0377645325e6d8df66a9e0c75e4d17fd513a12a1f495174b8bfa2e7f5682bc71 |
| research/10-saturated-edge-endpoint-cutoffs.md | [原文](snapshot/research/10-saturated-edge-endpoint-cutoffs.md) | 5020 | 22441981f560517a70469edd2a8fbb478f9d022c961fda81e94e1d3deca937fa |
| research/11-saturated-cross-witnesses.md | [原文](snapshot/research/11-saturated-cross-witnesses.md) | 5644 | 20df4d423fb4f27133e16d58c686b0777f7df200ca65074a21110aab1cc246de |
| research/12-e41-interface-and-remaining-cases.md | [原文](snapshot/research/12-e41-interface-and-remaining-cases.md) | 6803 | 6a7c3d233969f6a4525ae57dba49a7af0f18819a88aa36c435910dc70a9e7ffd |
| research/13-common-tail-capacity-and-deletion.md | [原文](snapshot/research/13-common-tail-capacity-and-deletion.md) | 6972 | 1dd299919e1e04b5aa1bb6083aba0cfeb8a00b4bfbccd1fe06b33b6bca8790fe |
| research/14-second-saturated-family-and-endpoint-branches.md | [原文](snapshot/research/14-second-saturated-family-and-endpoint-branches.md) | 5675 | 693ec8139065bd5d99b69ff80eb09c27f2ac2aaad06db9bfd09b4c5fa5510d09 |
| research/15-blue-tail-support-and-anchor-deficit.md | [原文](snapshot/research/15-blue-tail-support-and-anchor-deficit.md) | 4703 | e95fa491c46502f0e754a61c15d6935b9b63611be5d5a27a65625e57ac6a9a3a |
| research/16-forward-backward-capacity-and-remaining-extremes.md | [原文](snapshot/research/16-forward-backward-capacity-and-remaining-extremes.md) | 9175 | 85552b8bede054443977682d98845844faf934e4a809be2cd7b4751fb64ce9c1 |
| ROUND1_SUMMARY.md | [原文](snapshot/ROUND1_SUMMARY.md) | 5309 | 58e0945df1a0ce94b9fc1c9505d609197c61baa2e04314f2a5fd430372101148 |
| ROUND2_SUMMARY.md | [原文](snapshot/ROUND2_SUMMARY.md) | 8609 | 43cd91eca5b2a3b7ecac2c68d65e598539d1063a2758ec48daab1fa054969823 |
| ROUND3_SUMMARY.md | [原文](snapshot/ROUND3_SUMMARY.md) | 7719 | 2293740648060784f9426dd9948d897f0a2a7bc408568ab3ba1a97a174b861db |
| STAGE_SUMMARY.md | [原文](snapshot/STAGE_SUMMARY.md) | 5966 | 81fcaa0bf3d2d89e3d3a20881dac7d217ba05bc712117d3512f8579036a858c2 |
| task.json | [原文](snapshot/task.json) | 1184 | afe0c40997c586069daba9281f6597f912764fe2fe7af450179fc8d7245cede3 |

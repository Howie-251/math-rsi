# Q7 十六孔闭合归档增量

打开 [START_HERE.html](START_HERE.html) 可离线阅读定理摘要、工作流改进图和证据导航。[MathRSI 工作流改进](guide/Q7_WORKFLOW_CHANGES.md)保留可直接执行的规则。

[E16 研究轨迹](trajectories/SESSION_INDEX_E16.md)补录原 RAR 截止点之后的整层验收、工作流改进及来源定位。[MathRSI 研究 Wiki](research-wiki/README.md)收录可复用的已证工具、方法和证据索引。

[原档结构](guide/ARCHIVE_STRUCTURE.md)连接原 RAR 的全部目录和本地入口。[复现与核验](REPRODUCE.md)给出目录恢复和证据核验命令。

## 归档与组装

本地档案保有原 RAR 的完整目录结构与 E16 增量。冻结证书按原文件名和原字节存放，可直接核验或回放。

汇总 HTML、工作流和本地 E16 材料可离线查阅。既有证据按 SHA-256 绑定在独立保存的原档 `D:\Ruskey–Savage conjecture n=7.rar` 上，按需组装。

从档案根目录运行以下命令。校验使用 Python 3.11 或更新版本，检查本地文件的字节数和 SHA-256。

```powershell
python -B .\archive_inventory\verify_package.py
```

完整组装会在指定空目录保存本地档案和原 RAR 中的 290 项直接导入，并逐件核对 SHA-256。Windows 系统自带的 `tar.exe` 可用于组装。

```powershell
python -B .\archive_inventory\verify_package.py --baseline 'D:\Ruskey–Savage conjecture n=7.rar' --compose 'E:\新问题\q7-e16-assembled'
```

[E16_PACKAGE.json](archive_inventory/E16_PACKAGE.json)列出本地文件、字节数、散列与全部旧件导入。冻结证明中的历史表述和原工作站路径保留原样。查旧路径时先用文件名及正文绑定的 SHA-256 对照归档清单。基线内已有深层历史材料继续使用原 RAR 的 `archive_inventory/dependency_bindings.jsonl`。

## 冻结证书回放

在本档案根目录运行下列命令。DRAT-trim 读取 μ = 0 的冻结 CNF 与 DRUP，验真状态应为 `s VERIFIED`。

```powershell
$e16 = 'research\seven_directions'
$checker = "$e16\mu3_hard_first_2026_11_15\PROOF_TOOLS\drat_trim_official_2e3b2dc\drat-trim.exe"
$stem = "$e16\mu0_global_2026_11_15\certificates\mu0_structured_joint"
& $checker "$stem.cnf" "$stem.drup" -I -U -t 590
```

证书回放检查冻结 CNF 的不可满足性。原输入如何给出 CNF 赋值、五个 μ 整族的穷尽和逐支保原边回代见[完整证明](research/seven_directions/mu0_global_2026_11_15/MU0_FULL_CLOSURE.md)及[独立终审](research/seven_directions/mu0_global_2026_11_15/MU0_FULL_CLOSURE_REVIEW.md)。

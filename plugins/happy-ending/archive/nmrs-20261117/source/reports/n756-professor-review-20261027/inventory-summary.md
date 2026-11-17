# 机械证据清点摘要

本轮只写入本交付目录及新建专用任务 `10-27-n756-professor-review-20261027`。原有 dirty 文件、旧任务、封印运行时、求解进程和大型证明均保持原状。任务创建和进入执行的授权由主代理记录，PRD 已保存。

`raw_inventory.json` / `.csv` 清点选定轻量原文件，逐文件记录相对/绝对路径、字节数、SHA256 和 JSON 状态字段。清点并非仓库全盘完整性审计。大于 8 MiB 的文件不读内容、不哈希；CNF、DRAT/LRAT/GRAT 主体、二进制和图片均排除。最新计数以 `inventory_validation.json` 为准。

正式上界证据主要入口为 `.trellis/tasks/09-03-35-state-cardinality-charging/research/evidence/` 下的 C1/C2 accepted、C3/C4/C5 历史审计批次、C6/C7/C8 accepted 以及 C9/C10 accepted 目录。C3–C5 的完整 final/acceptance 本地副本位于 `tmp/res/state_charging/`。不存在顶层 `res/state_charging/`，此事实不影响收据绑定的 Linux 原路径。

`55-case-register.csv` 和 `.json` 按 `(r,e)` 转录每格原始行证据，保留来源收据及其机械哈希、CNF/proof/checker 的原始路径和哈希。`case-register-validation.json` 检查恰好 55 格且三类哈希无缺项。大型公式与证明没有在本轮重新读取或检查；其原始哈希来自收据。本地可用性单独标记。

下界入口是 P0 历史严格 N25 SAT 的完整 `solver.out`、`sat_audit.json`、`status.json`。新增 `lower_bound_verify.py` 仅在专用 Linux 目录运行，无 SAT/PySAT/求解调用；生成 `color.tsv` 与 `verification.json`。另有完全依赖 TSV 的便携 `verify_color.py` 及 Linux 复核结果 `portable-verification.json`。上传、执行和下载收据均保留，见 E21。Windows 仅执行传输、文档与哈希操作。

Schroeder 文献 selected_sources 中保留论文/Lean 源文件；外部 `restricted_25_points.json` 未取回，本地同名 ZIP 不能作为 ZIP 读取。E33 因此只列为外部文献声明，不用作本报告下界。D7/R11 按主代理要求不纳入本交付主线。

ARIS 两条审阅路由仍禁用。本轮没有调用审稿人，也没有把文档工程核对写成新的独立数学审查。

# Ruskey–Savage Q7 Complete E16 (`≥56` Edges) — Curated Archive

来源为用户归档 `R-S-n=7(2).rar`（2026-11-16 打包；研究运行采用 `MathRSI v3` 本地适配 + E16 难余域优先分类准入规则，方法在 `v6` 吸收），独立存放在本目录，不改动 `v5` 的 `../q7/` 快照。

## 已确立范围与开放边界

- **完整 E16 定理：** `Q₇` 中任意边数 **`|M| ≥ 56`（至多 16 个原孔）** 的短匹配 `M`，均可延拓为保留 `M` 全部规定原边的 128 点全短 Hamilton 圈（由 E14、相邻原孔增广以及独立孔 `μ ∈ {0,1,2,3,4}` 五个整族并合；独立 16 孔奇偶/重量界排除 `μ ≥ 5`）。
- **审计与导入等级：** `PASS · same-family · provisional · sound-modulo-imports`。本目录已把 `E16_PACKAGE.json` 声明的 **全部 290 份基线导入文件（7.98 MB，来自 2026-11-14 `Ruskey–Savage conjecture n=7.rar`）** 一并合入 `source/` 对应路径，消除跨包悬空引用。
- **仍开放范围（OPEN）：** 偶数孔层 18–38（`≤55` 边）、完整 `Q₇`（`R₇`）、自由根路径 `P₇` 及任意维七方向提升（Fink–Hotmar Theorem 5 以 `P₇` 为前提，不能仅凭 `R₇` 或稠密层调用）。

## 随仓可执行检查（Python 标准库）

```sh
python3 -B plugins/hypercube-hamilton/archive/q7-e16/check_e16_bundle.py
```

该脚本无需第三方 Python 包即可逐个校验随仓全部 261 份 E16 原件与全部 290 份已合入基线文件的字节和 SHA-256，复核 `MU0_STRUCTURED_JOINT.pb` 与 189 行（`19 + 98 + 72`）大面独立孔表位串哈希，并在临时副本实际运行 `MU0_A0_BASIS_REVIEW_check.py`、`MU0_A0_PLANS_REVIEW_check.py`、`MU0_A12_BASIS_REVIEW_check.py` 与 `Q6_A8_FULL_REVIEW_check.py` 四套独立几何/计划核验器（若当前环境安装了 `ortools`，还会额外从 `MU0_JOINT_NECESSARY.pb` 重新编译并比对 `MU0_STRUCTURED_JOINT.pb`）。

## 统一省略的 10 份大 `.cnf`/`.drup` 证书与外部复现说明

由于 `even.drup`（201.55 MB）与 `odd.drup`（109.65 MB）超出 GitHub 普通 Git 100 MiB 单文件上限，且部分保留会导致并合定理各分支重放口径不一，本目录统一省略全部 10 份 `.cnf`/`.drup` 文件（共 532.49 MB）及 Windows 可执行文件 `drat-trim.exe`（保留官方源码 `drat-trim.c`、全部 `.pb` 源公式、CNF 编译器与官方验证回执/日志），逐项登记在 [INVENTORY.json](INVENTORY.json)。**哈希清单不能代替 DRUP 轨迹重放；** 完整轨迹重放需从外部研究归档 `R-S-n=7(2).rar` 提取该 10 份文件并用 `drat-trim.c` 编译核验。

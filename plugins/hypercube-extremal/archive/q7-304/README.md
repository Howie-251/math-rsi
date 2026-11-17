# Q7 C4-free Subgraphs (`304`) — Constructions & Source Upper-Bound Report

- **核验结论摘要：** **304 边构造已验证；304 上界按原包报告，本次未复验。**
  (*304-edge construction verified; 304 upper bound as reported in the source package, not re-verified in this pass.*)

## 包含内容与各自支持范围

1. **下界 `ex(Q₇, C₄) ≥ 304`（本轮已独立验证）：**
   `witnesses/A.edges` 与 `witnesses/B.edges`（提取自 `C4-Free进展.zip :: Q8_C4_upper683_20261116/research/ex_qn_c4/proofs/q8_q7_gluing_cycle007/`）给出两份显式 128 点、304 条超立方体边且含零个 `C₄` 的子图。这些构造仅支持下界，不能据此证明上界。
2. **上界 `ex(Q₇, C₄) ≤ 304`（原包报告，本次未复验轨迹）：**
   `source/` 保留 `C4-Free进展.zip :: 成果汇编_20261031/` 中的完整归约正文（`ASTRA_主证明合订.md` 第一部分，将 305 边无 `C₄` 图归约为 21 个 `Q₆` RUP 实例并导出 `20 ≤ 18` 子面矛盾）、两孔轨道独立枚举脚本 `six_profiles_independent_audit.py`、CNF 编码审计脚本 `star_rigidity_encoding_audit.py`、证书清单 `star_rigidity_certificate_manifest.json` 及原 C# history-RUP 检查回执。上游汇编包原本未附带 21 份原始 `.cnf`/`.drup` 文件（原件保存在上游生成项目的 `problem_001_304` 归档中），且原稿标明整证独立终审待补；本仓如实保留原包报告状态，不因大轨迹未随包否定原证明，也不将其写成本轮已独立复验轨迹的精确值。

## 可执行检查命令

```sh
python3 -B plugins/hypercube-extremal/archive/q7-304/check_q7_304.py
```

[SOURCE_FILES.txt](SOURCE_FILES.txt) 列出随仓文件；[INVENTORY.json](INVENTORY.json) 记录上游 `star_rigidity_certificate_manifest.json` 中登记而未随汇编打包的 21 组 `.cnf`/`.drup` 标识。哈希记录不能代替原始轨迹复验。

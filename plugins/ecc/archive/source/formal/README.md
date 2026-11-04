# Lean 复核范围

两个工程均固定 Lean 4.34.1；mathlib 的锁定提交是 `d13f23b723b8a846827a245b89c10fc7d3f11612`。各自 `lake-manifest.json` 固定所有传递依赖。请勿执行 `lake update`，以免改写依赖版本。

在包根目录运行：

```sh
python3 verify.py lean --get-cache --output-dir ../ecc-lean-check
```

脚本把源工程复制到输出目录，从没有本项目 `.olean` 的状态构建 `ECC.Main`、`ECC.Corollaries` 与 `ECC42`，再分别运行 `Audit.lean`、`CorollariesAudit.lean`。新机器需 elan/Lake、Git 和网络下载固定工具链/依赖缓存。已有对应版本 `.lake/packages` 可用 `--dependency-cache /path/to/packages` 代替 `--get-cache`，脚本检查各 Git 提交与已跟踪源码是否干净。

## 导出结果及显式参数

- `ECC.mainClaim_of_external_results`：从 E1、E2、172 个实际母码两两不等价、每个母码的完整配对不兼容性，推出原始 `[43,10,≥17]` 不存在命题。
- `ECC.mainClaim_of_scan_facts`：进一步展开规范化投影、穷尽覆盖和保存配对见证这些计算输入的含义；没有在 Lean 内重跑外部扫描器。
- `ECC.four_table_consequences_of_external_results`：在上述同样输入下，给出前三项最优距离与第四项区间；相关下界矩阵在 Lean 内检查。
- `ECC42.nonexistence_of_proposition2`：以已发表的精确 `[41,14,14]` 不存在性为参数，推出 `[42,16,≥13]` 不存在。

审计打印实际定义、最终类型及传递公理；最终结果通常依赖 `propext`、`Classical.choice`、`Quot.sound`。显式 theorem 参数不会显示在 `#print axioms` 列表中，因此干净的公理列表不等于整个计算证明无外部依赖。172 个矩阵的合法性与参数已内核核验；完整陪集枚举及图规范化仍是外部计算事实。第五项下界由独立 Python 检查。

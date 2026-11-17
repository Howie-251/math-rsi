# 从本文件夹复现

所有命令从本文件夹执行。新结果写到指定的新目录，不能复用已存在的 `--out`。不需要启动模型、重新运行优化器或恢复旧 Goal。

## 文件与原审查绑定

```bash
python3 verify_bundle.py --all --out validation/materials-check.json
```

该命令检查材料的当前完整清单、最终全文审查绑定的 **51** 个文件，以及 **25** 组 Q₆ CNF／DRAT 的原哈希。经过称谓和路径整理的文件通过 `PRESENTATION_EDITS.json` 对照前后散列，并单独计数；不会把整理副本称为与审查原件逐字节一致。它核对文件完整性，数学有效性仍由原证明及核验支撑。

## 最轻量的精确算术检查

```bash
python3 replay.py quick --out validation/quick-new
```

只需 Python 3.10+ 标准库。复制已保存的最终证书与完整枚举输出，用原检查器重新计算矛盾余量。该模式不重新枚举 Q₄。

## 重新编译并完整枚举 Q₄

```bash
python3 replay.py q4 --out validation/q4-new
```

需要 Python 3.10+ 和支持 C++17 的 `g++`，在 Linux／WSL 中运行。程序使用包内源码重新编译，对最终查询执行完整域最大化，然后运行精确算术检查。预期：

- `LEGAL_MARKED_COMPLETIONS 13150453`
- `EXACT_RAW_MAX -37440`
- `STATUS COMPLETE_LEGAL_Q4_MAXIMUM`
- `exact_safe_margin = 782808475930428709/4209067950080000000000`

## 从权重和参数重新构造精确证书

先在自己的 Python 环境中安装 `requirements.txt` 所列 NumPy、SciPy，再执行：

```bash
python3 replay.py reconstruct --out validation/reconstruct-new
```

此模式调用包内原重建程序，从冻结参数及实际分母重新构造系数，并要求两个最终查询文件与已接受版本逐字节一致，再对保存的完整枚举结果检查余量。NumPy／SciPy 是显式第三方运行依赖；没有将作者已安装的二进制环境伪装成跨平台源码。

## 重放 Q₆ 的全部 25 份有限证书

```bash
python3 replay.py q6 --out validation/q6-new
```

需要 Python 标准库、`bash` 和 C++17 编译器。该模式在新工作副本中执行原 `reproduce.sh`，重建输入与覆盖、严格解析 CNF／轨迹、执行 RUP 检查及相关解析核查。预期总数为 **25** 个输入、**4,383,882** 次已验证添加。

Q₆ 脚本的三个输入根路径已整理为 `q6_sources/q8_upper_independent`。包装器在新工作副本中将这些字面路径解析到本包实际位置，记录到 `PATH_ADAPTATIONS.json`。历史审查散列与整理副本的前后散列分别保留；计数、编码、覆盖和检查器算法保持原有内容。

## 结果和范围

每次执行保存 `COMMANDS.json`、stdout、stderr 和 `REPLAY_RESULT.json`。原脚本中 `PENDING_WHOLE_PROOF_ACCEPTANCE` 一类状态描述的是其算术检查职责，不抹去另外保存的后续全文审查；完整定理的接受记录请读 README 指定的 Theorem B 审查入口。

本次整理实际执行了哪些步骤、使用了什么运行环境，见 [交接验证记录](validation/HANDOFF_VALIDATION.md)。同一代理在本文件夹重放，不等同于另一位研究者独立复现，也不会把上界 683 升级为 682。

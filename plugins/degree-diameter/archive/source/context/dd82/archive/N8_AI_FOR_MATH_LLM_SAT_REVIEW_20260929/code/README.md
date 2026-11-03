# 精选源码：理解算法，不要求复现

这里保存原工程关键模块的副本。不要直接运行各个`main()`：它们可能需要原目录结构、CNF、solver、数据与已有队列。本包不包含独立生产环境；用户明确只需专家看懂方法，因此没有再做一套调度或复现平台。

本次只核对了与报告相关的关键函数和调用关系，没有重新执行这些求解器，也没有把源文件存在写成当前已部署或测试通过。

## 三个优先入口

1. **真正改变状态空间：** [n59/branches/c3_cover.py](n59/branches/c3_cover.py)。读`C3CoverEncoder`、`_allocate_primary_variables`、`_encode_permutation_matrices`、`_encode_cover_colors`、`_encode_joint_symmetry_breaking`。它把D表达为六个7阶置换和完美码坐标，而非任意35点图。
2. **理论怎样落到同一张图：** [n59/enc/manual12.py](n59/enc/manual12.py)的`add_m0_transport`，以及[manual12_r2.py](n59/enc/manual12_r2.py)的`zero_matching_row`。前者绑定交集和整数重复量，后者展示全图零根匹配定理的条件编译。
3. **为什么很多局部UNSAT不能关闭父范围：** [n58/c3d/nested_driver.py](n58/c3d/nested_driver.py)、[block_cover.py](n58/c3d/block_cover.py)。每个固定phase有自己的block扩展义务；否定很多phase仍不等于穷尽其parity root。

## 数学—代码对应

| 数学对象/操作 | 入口 | 需要注意的语义 |
|---|---|---|
| 公共邻点AND | `n59/enc/and_gate.py::encode_iff_and/add_iff_and` | 三子句双向等价，含常量简化 |
| 计数与B重数 | `n59/enc/cardinality.py`、`threshold.py` | 阈值位的总和保留整数重数，不是只记支撑 |
| 可变8×50父矩阵 | `n59/enc/variable_parent_matrix.py` | 精确父数与父容量；模块明确没有列/行规范排序 |
| A+B基础输入 | `n59/branches/c1_coarse_v3.py` | `a/d`提供同一个图；`_encode_repeat_entries`、度数和三角形共同绑定 |
| 选极值根 | `n59/enc/extremal_minimum_root.py` | t=m守卫下才比较k；选根资格不是普通根UNSAT |
| Q₂、异常余量 | `n59/enc/root_moment_budget.py`、`exception_sigma_budget.py` | 精确矩量与逐行预算 |
| A1/A2运输 | `n59/enc/manual12.py` | `gated_sum`按整数阈值门控；`equal_sums`保留guard和溢出 |
| H5新条件 | `n59/enc/manual12_r2.py` | `zero_matching_row`的零点guard；范围的H5资格与低Q补集由前沿合同管理 |
| 语义二分与父级闭合 | `n59/jobs/extremal_v5_timeout_splitter.py` | 对同一个literal取正反；`aggregate_split`必须两叶均关闭 |
| 实际最新求解队列 | `n59/jobs/run_structural_v6.py` | 文件名沿用V6，不表示最新只用了V6理论；根/叶新进程不等于内部状态续算 |
| n62七模板A+B | `n62/n62_ab_cnf.py` | 读取模板后编译缺陷与结构，不是只做普通距离覆盖 |
| n62规范补集 | `n62/n62_ab_resume_partition.py` | 最后80任务的覆盖来源，不能当80个任意随机seed |
| n62早期SMS | `n62/n62_sms_solver.py`、`sms_n62_distance_main.cpp` | 延迟距离检查及图对称性，已尝试过但对应批次未闭合 |
| n58 phase参数 | `n58/c3d/phase.py` | 4×12相位数组表示完整左—中关联 |
| n58匿名blocks | `n58/c3d/block_cover.py` | `enumerate_allowed_blocks`、`validate_block_cover`；18个块，24个item各出现3次 |
| n58 B5、预算 | `n58/c1_delta_tools.py` | 上游参考模块；`b5_cnf_clauses`只在选中邻点时禁边，`y_row_budgets`保留固定父集系数 |
| n61 CP02增量 | `n61/cp02_common.py::add_W_le5`、`cp02_compile.py` | 使用CP01已有真实W指示量，只追加数量界，不含全部I12定理 |
| n61并行方式 | `n61/cp02_portfolio55_queue.py` | 同公式多seed，不是互补结构分区 |
| n60行型与guard | `n60/constraints.py`、`encoder.py` | `exact_weights`、`row_profiles`、`add_feedback`将直接R13F后果接入 |

## 用伪代码读懂三个关键动作

### 精确结构谓词

```text
z := (真实边 a AND 真实边 b) 的等价变量
count := sum(z_1, ..., z_m)
q := [count >= k] 的等价变量
若理论前提 H 成立，则要求 C(q,...)
```

单向见证在仅要求存在一条路径时可能用于某些编码，但本项目的精确重数与计数定理需要完整等价绑定；不能把“足以表达至少一次覆盖”的弱变量拿来直接统计全部公共邻点。

### 候选保全的选根

```text
对任意原候选图，证明至少存在一个合法极值根
用该根定义 m、K、异常权与允许Q入口
保留所有可能入口；某入口只是不再作为代表时，不记为新UNSAT
```

### 有覆盖的切分

```text
父输入 F
选择具有精确定义的布尔谓词 p
创建 F AND p 与 F AND NOT p
两者都UNSAT，才能关闭F
若只关闭前者，报告剩余范围 F AND NOT p
```

这段逻辑保证范围正确，并不保证p是好的性能切分点；最新n59的优先级主要是固定语义规则，未做独立lookahead收益测量。

## 副本来源与版本

- `n59/`：来自2026-09-28实际run冻结源码，原位置在`formal_loop/N59_MANUAL12_ACTIVE_CODEX_TO_PRO_r2_20260929/dependencies/run/source/sat59/`。不是凭当前同名文件猜测旧版本。
- `n60/`：来自Round13 r02回收包的`dependencies/run/formulas/code_snapshot/sat60/round13_r02/`。
- `n61/`：来自I12 CP02回收包的`dependencies/implementation/code/`。
- `n62/`与`n58/c3d/`：本次从真实仓库读取的关键实现。报告中的历史计数来自对应运行记录，不声称这些当前副本就是历史运行字节快照。
- `n58/c1_delta_tools.py`：来自专家09-08增量包的参考实现，展示局部编译算法，不冒称其本身是生产队列入口。

各原模块的导入路径保持原样；只复制和安排阅读目录，没有修改算法。`theory/`内有限核对器及Lean草稿同样保持原状态，本次均未执行。

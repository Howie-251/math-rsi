# 完整超图的对抗性反例搜索

2026-10-06。对象是 `FORMAL_SPEC.md` 的 T/E1/E2/F。实现没有导入候选证明、锁定概率、结构分类或其数值上界。

**结果：11 次有预算的目标搜索检查了 124 个候选记录，去除重复后为 120 个不同的有标号 32 边简单五元超图；每个都有保存的合法二染色。生成并核查 2,320 条 COVER 约束。所有目标运行均因时间预算结束，没有反例，也没有得到主问题 UNSAT。该结果不能证明 T，不能把候选证明升级为已验证证明。**

## 编码与不遗漏反例的理由

对固定的 (v)，为全部 (\binom v5) 个五元集设置布尔变量 (z_A)。`Minicard` 使用两条原生基数约束

\[
\sum_A z_A\le32,\qquad \sum_A(1-z_A)\le\binom v5-32,
\]

所以恰好选 32 条不同边。点对覆盖运行还为每个点对加入“至少选择一条包含该点对的边”的子句。这一限制只用于规格 F 的最小反例约化；另有两次 23 点运行移除了点对覆盖，覆盖更大的固定顶点数对象类。没有限制正则性、线性、相交模式或度数序列。

所有运行固定边 ({0,1,2,3,4})。这是可逆的顶点重标号对称性处理：任意 32 边超图都有一条边，可将它的五个顶点映至该集合。它不要求某条特殊结构边存在。顶点编号采用 0 起点。

每个主问题模型给出完整超图 (H)。`Minisat22` 对每条边加入一正一负的两个五文字子句，即 E1，并仅固定顶点 0 为红。固定一个顶点颜色利用全局换色对称性，仍检查全部二染色；**没有要求两色人数相等**。

若该 unrestricted oracle 找到合法染色 (R)，程序直接逐边检查它，并加入

\[
\bigvee_{A\subseteq R\ \mathrm{or}\ A\subseteq V\setminus R}z_A.
\]

这是 E2 的一条必要约束：任何不可二染色超图必须包含一条在这个染色下单色的边；当前 (H) 没有这样的边，所以被排除。因而每条 cut 都排除一个已验证可染候选，同时保留所有真实反例。程序分别通过颜色类内组合枚举和全五元集位掩码扫描生成/核对同一完整文字集合，并检查当前候选确实不满足它。

每个候选还额外提取 15 或 31 个较均衡的合法染色，作为同样有效的必要约束。它们只帮助搜索；只有前面的 unrestricted oracle 有权报告候选不可染色。额外 oracle 的 UNSAT 不会被解释为原超图不可染色。奇数 (v) 时，额外 oracle 使用红点数 (lfloor v/2\rfloor) 且顶点 0 为红，也只是选择一部分有效 cut，不作完备性结论。

初始相位来自五阶仿射平面的 30 条直线：保留 (v) 个点，把短块补足为五元集，去重后补至 32 条。任意保留点对原来所在的直线仍被包含，因此这些初值覆盖点对。后续可用贪心集合覆盖给出满足当前主约束的相位初值；它们均不增加约束，也不把搜索限制在仿射平面或贪心构造类。

每次求解最多 20,000 个冲突、5 秒墙钟时间，并受整次运行的总时间约束。`solve_limited` 返回 `None` 时明确记为 UNKNOWN，保留已学信息后继续，不能当作 UNSAT。主问题若报告 UNSAT，程序仍标为 `MASTER_UNSAT_UNCERTIFIED`，不作无证书的全局证明结论。若 unrestricted oracle 报告不可染色，程序会另用逐个颜色位掩码遍历全部 (2^{v-1}) 个互补代表进行独立核验。目标运行未触发这一分支。

## 实际搜索范围

种子均为 20261006。`greedy` 是最大相位初值尝试次数；0 表示直接 SAT。所有列出的目标运行最终状态均为 `TIME_BUDGET_NO_COUNTEREXAMPLE`。

| 结果目录 | 点对覆盖 | 总预算（秒） | 每候选 cut 数 | greedy | 候选记录 | cut 数 | 主问题 UNKNOWN 次数 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `v19-seed20261006-120s` | 是 | 120 | 16 | 0 | 1 | 16 | 24 |
| `v19-greedy-120s` | 是 | 120 | 16 | 2 | 23 | 368 | 24 |
| `v20-greedy-75s` | 是 | 75 | 16 | 2 | 22 | 352 | 15 |
| `v21-greedy-75s` | 是 | 75 | 16 | 2 | 24 | 384 | 14 |
| `v22-greedy-75s` | 是 | 75 | 16 | 3 | 18 | 288 | 14 |
| `v23-seed20261006-180s` | 是 | 180 | 32 | 0 | 1 | 32 | 36 |
| `v23-paircover-greedy-90s` | 是 | 90 | 16 | 4 | 12 | 192 | 16 |
| `v23-unrestricted-seed20261006-120s` | 否 | 120 | 16 | 0 | 1 | 16 | 24 |
| `v23-unrestricted-greedy-180s` | 否 | 180 | 32 | 1 | 20 | 640 | 35 |
| `v24-greedy-75s` | 是 | 75 | 16 | 4 | 1 | 16 | 14 |
| `v25-greedy-75s` | 是 | 75 | 16 | 4 | 1 | 16 | 13 |

各顶点数的不同有标号超图数为：19 点 23 个、20 点 22 个、21 点 24 个、22 点 18 个、23 点 31 个、24 点 1 个、25 点 1 个。不同种类运行的初始候选可能重复，所以不能把 124 个记录称作 124 个不同超图。

累计运行墙钟预算约 1,185 秒，其中多个运行并行，不是连续 1,185 秒的单次穷尽搜索。实际时间、SAT 冲突/决策/传播次数以及可复现参数均在各 `summary.json`。直接 SAT 通常在加入第一批 cut 后很慢；相位初值使 19–23 点得到更多完整候选。24、25 点只有一个有效候选，搜索深度尤其有限。这里没有统计抽样置信区间，也没有测量总对象空间的覆盖比例。

## 正负对照与保存证据

固定 oracle 对照均同时经过 SAT 与独立的逐颜色位掩码枚举：三角形不可染，删边后可染；Fano 平面不可染，删边后可染；九点完全五元超图不可染，八点完全五元超图可染；17 点 51 边五元构造不可染。最后一个构造取七点循环 Fano 的七条线，各接上五个独立点对之一，再加入五点对中选择一点的所有偶数 (b_i) 奇偶型横截，共 35+16 条边。种子出处为[公开构造说明 §3](https://erdosproblemaday.com/report/901)；本次重新生成全部边，并独立检查了 65,536 个互补颜色代表。

端到端主问题也找到了三角形与 Fano 平面，随后独立穷尽确认不可染色。负对照 `n=3,k=2,m=2` 检查两个满足固定首边的候选、产生两个 cut，最终得到 `MASTER_UNSAT_UNCERTIFIED`；这里只是已知可染小实例上的管线对照。原生基数约束正负文字的符号还用三个变量的全部八个赋值逐一核对。

每次目标运行保存：

- `candidates.jsonl`：全部完整边集、每点度数、最小点对共度、unrestricted oracle 结论和明确的合法红点集。
- `cuts.jsonl`：每条 cut 的红点集、对应候选、单色五元集总数、来自 unrestricted 或额外 oracle 的标记。红点集足以无损重建整条 cut。
- `events.jsonl`：进度、UNKNOWN 次数及时间；`summary.json`：完整命令参数、版本、预算、计数和终态。
- `initial_phase_seed.json`：初始相位候选；它只提供相位偏好。

独立离线重查不调用 SAT：再次核对所有 124 个候选的简单五元/32 边/点对覆盖约束、逐边合法染色、全部 2,320 条 cut 的合法来源，并核对每个后续候选满足此前所有 cut。结果为 [artifact_audit.json](../results/counterexample-search/audit/artifact_audit.json) 的 PASS。该 PASS 只针对已保存的有限证据，不针对 T。

## 复现

实现：[search_counterexample_sat.py](../computations/search_counterexample_sat.py)。环境：项目内 `.venv-counterexample`，Python 3.14.6，`python-sat==1.9.dev15`；依赖文件为 [requirements-counterexample.txt](../computations/requirements-counterexample.txt)。原生基数与中断 API 对照 [PySAT 官方文档](https://pysathq.github.io/docs/html/api/solvers.html)。

优先的 23 点点对覆盖运行：

```bash
.venv-counterexample/bin/python computations/search_counterexample_sat.py \
  --vertices 23 --seconds 90 --batch 16 --greedy-phase-attempts 4 \
  --output results/counterexample-search/reproduce-v23-paircover
```

更大对象类的 23 点运行：

```bash
.venv-counterexample/bin/python computations/search_counterexample_sat.py \
  --vertices 23 --seconds 180 --batch 32 --no-paircover \
  --greedy-phase-attempts 1 \
  --output results/counterexample-search/reproduce-v23-unrestricted
```

其余运行用表中参数替换；全部原始参数亦保存在各 `summary.json.command`。输出目录应使用新名称，以保留现有证据。确定随机种子不保证不同机器或时间片下产生完全相同的候选序列；中断时刻影响增量 SAT 轨迹。

```bash
.venv-counterexample/bin/python computations/search_counterexample_sat.py \
  --controls --output results/counterexample-search/reproduce-controls

.venv-counterexample/bin/python computations/search_counterexample_sat.py \
  --audit-root results/counterexample-search \
  --output results/counterexample-search/audit
```

下一轮若继续搜索，应将资源用于提升当前 COVER 主问题的求解，而不是将这些未命中记录解释为对候选证明的认证。当前有限搜索没有发现候选证明的反例，但也没有排除任何一个目标顶点数的全部超图。

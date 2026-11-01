# A1原35边：一次120秒有界COVER探测

## 实际结果

本轮实际运行了Minicard原H master，而不只是导入依赖。搜索于2026-10-20 03:02:09 UTC开始，03:04:09 UTC按预算结束；测得墙钟120.001625秒（含结束清理），CPU117.667663秒。

**没有构造出第一份满足完整A1角色的H。** 实际40次master求解片段全部返回UNKNOWN；候选数0、COVER cut数0、unrestricted染色oracle调用0、补充染色oracle调用0。没有master UNSAT或不可染候选。不能把这个结果写成“已检查若干A1图均可染”或“A1很可能不存在／目标为真”。本轮只定位到第一份角色可行原H的构造瓶颈，尚未抵达不可染性测试。

完整终态和原命令在[SUMMARY.json](SUMMARY.json)，实际进度在[SEARCH.log](SEARCH.log)、[events.jsonl](events.jsonl)。没有自动续预算或第二轮搜索。

## 1. 原对象及无额外限制的master

[SEARCH.py](SEARCH.py)是本目录独立小程序，不改动或导入旧32边harness，不引用正向概率、signed门、A1残核或候选证明。固定标签如下：x=0、p=1、B={2,3,4,5}、U={6,…,10}、V9={11,…,20}。

对全部 $\binom{21}{5}=20349$ 个五集各设一个0/1边变量。master恰约束：

$$|H|=35,\quad d_0=6,\ d_1=7,\ d_i=8\ (2\le i\le10),\ d_i=9\ (11\le i\le20),$$
$$\lambda(0,b)=2\ (2\le b\le5),\qquad
\lambda(0,v)=1\ (v=1\text{ 或 }6\le v\le20),$$

以及全部210个点对至少被一条边覆盖。35条边来自不同五集变量，因而自动简单、无重复。总度目标为175，中心共度目标总和24，与五元六星相符。

原生exact-cardinality $\sum_{i\in I}z_i=c$ 被写成两份at-most：$\sum z_i\le c$ 和 $\sum(1-z_i)\le|I|-c$。总边数、21个度数、20个中心共度合计84份原生at-most约束，另有210份pointcover子句。

这些是完整原A1角色条件，没有固定首边、仿射限制、平衡颜色限制、中心link分割或指定高交结构。任一实际A1 H可依角色重标记到本域；反之任一master模型就是满足这些条件的完整35边H。程序没有用当前位置顺序删去其他可能角色标签。

[INITIAL_PHASE.json](INITIAL_PHASE.json)给六条符合中心角色的x星边，仅作变量phase偏好；其他变量初始偏好为false。没有将这六条边加入master单元子句。故相位不缩小数学输入域，也不是已有完整可行H。旧M32仿射seed没有被调用。

## 2. 完整候选与COVER验收路径

程序若取得master模型，会立即独立按literal五边重算：35条互异五集、21个原度数、全部210个点对共度和20个中心共度。完整边表和全部这些数据逐份写入[candidates.jsonl](candidates.jsonl)。本次该文件为空，不能虚列边集。

随后unrestricted Minisat22 oracle对每条原五边加正、负两个子句，仅固定x红利用全局换色对称；没有红蓝人数约束。找到proper染色时直接逐边复核，再向master加该染色的全部单色五集变量的析取，即每个非B H必须满足的必要COVER cut。cut文字同时用颜色类内组合枚举和全20349五集位掩码扫描核对。补充oracle同样不限制平衡；它只寻找更多proper染色作cut，不承担不可染结论。

若unrestricted oracle报告UNSAT，则程序会独立遍历全部 $2^{20}=1048576$ 个互补颜色代表，保存显式35边及穷尽结果；只有两者一致不可染才输出反例。该分支本轮没有触发，不能写成已进行全色核。

每次求解受20000冲突、至多3秒片段及共同120秒deadline约束。UNKNOWN保留当前求解器状态后继续，不能解释成UNSAT。master若正常返回UNSAT也只记 `MASTER_UNSAT_UNCERTIFIED`，本程序没有正向穷举证明输出。

## 3. 实际计数和独立离线核查

|项目|实际值|
|---|---:|
|master变量|20349|
|master调用／UNKNOWN片段|40／40|
|master重启|1220|
|master冲突|274502|
|master决策|38829021|
|master传播|134341761|
|完整H候选|0|
|unrestricted／补充染色oracle调用|0／0|
|COVER cuts|0|
|终态|TIME_BUDGET_NO_COUNTEREXAMPLE|

[VERIFY.py](VERIFY.py)为独立标准库保存证据检查器，不导入搜索程序或SAT。它支持原35边的完整角色、逐点对共度、proper原染色、cut全五集字面集合和此前cut满足性的重放；有不可染候选时另做全色核。它本次实际运行，结果[VERIFY.json](VERIFY.json)为PASS、0候选／0cuts。**候选／cut分支为空，因此本次PASS仅表明现存终态和空记录计数自洽，不是原H覆盖或角色可行性证书。**

使用环境为Python3.14.6、python-sat1.9.dev15。这一次native求解确已执行，计数来源为实际 `master.accum_stats()`，没有把先前import检查写成solve通过。

实际唯一搜索命令为：

```sh
.venv-counterexample/bin/python context/propertyb35-paper/round01/counterexample/35_original_search_audit_20261020/a1_probe/SEARCH.py --seconds 120 --batch 16 --seed 20261020
```

命令保存在SUMMARY，日志重定向保存于本目录。该程序输出固定文件名；现有证据应保留，勿无意重运行覆盖它们。只重放当前保存记录可用：

```sh
python3 -B context/propertyb35-paper/round01/counterexample/35_original_search_audit_20261020/a1_probe/VERIFY.py
```

## 4. 结论边界

本次新增的是一份真正运行过的35边A1构造probe及其准确失败边界；没有新增实际A1样本、没有反例、没有证明A1可染或为空。与旧32边120样本保持区分。若以后继续反向路线，首要改善应是构造一份完整A1可行H作phase，或改进原度／星共同表示的可行性求解；仅重复相同120秒设置并不能增加已观察到的颜色oracle覆盖。本轮停止，不运行后续搜索。

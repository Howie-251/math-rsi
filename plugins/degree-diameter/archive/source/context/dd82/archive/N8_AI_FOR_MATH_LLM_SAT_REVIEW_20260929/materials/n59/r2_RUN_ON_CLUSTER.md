# RUN_ON_CLUSTER — N59_MANUAL12_ACTIVE / r2_20260928

03 准备交付；**尚未启动生产计算**。本页供用户在55核实例手动运行。原研究轮次不变，新包修订使用新 run 目录，不 resume r1/P16。

## 1. 计算问题与回收要求

### 数学问题、用途与完整范围

本批用途仅为**决定性搜索**，不附加对照或诊断作业。

在继承的 `LATEST_CONDITIONAL` c1 合同下，余下33个必要代表能否由同一59点、8正则、直径2的真实 A/B 实现？其中新的主要结构问题是：**H5 范围中，所有零三角形顶点均为2211/Q5匹配型，是否仍能实现？**

- m0/3111：Q0–4，5入口；Q4加入N2，保留两种异常图。
- m0/2211：Q0–5，6入口；Q5使用H5代表模式，加入N5/N14/N15。
- m0/21111：Q0–7，8入口；不移植K4结论。
- m0/111111：Q0–6，7入口；保留原K6条件依赖。
- m1/K4/1111：Q1–7，7入口；Q7沿用无R2-P3，保留配对C3。

合计33入口、20个共享基础编码。P16/K3已按N8及继承覆盖**条件性理论关闭**，不生成确认性求解；历史TIMEOUT不改成RAW。

H5模式仅用于2211/Q5入口，并与两个K4分拆的**全部10个Q≤4入口**配套。它不声称任意旧Q5根都满足N15：含低Q出口的图由低Q入口保留；没有低Q出口的图才有H5及N15。单独Q5输入UNSAT不能标记“任意旧Q5根均UNSAT”。全部必要入口及其互补叶闭合才改变对应完整条件性c1范围；不自动解决整个N59或认证历史RAW。

### 最小回收

|实际产物|用于回答什么|
|---|---|
|`campaign.json`、`task_tree.json`、`progress.json`、`run.json`|33代表覆盖、互补叶状态、run标识、实际参数、数学迁移与求解状态分账|
|`inputs/execution_context.json`、`inputs/pro_r2_20260928/`、`source/`|实际使用的数学正文、代码、约束集合、H5覆盖规则和计算问题|
|`templates/*/{case.json,base.map.json,base.stats.json,ready.json,build.log}`及`base.cnf`|具体基础公式、literal映射、构建规模与资源记录|
|`tasks/*/attempt-*.cube.json`、solver日志、task/attempt记录|精确Q选择、互补分支、退出原因、墙钟、采样CPU与RSS|
|若SAT：`attempt-*.verification.json`|完整A、原图核对；原图有效时重算B、t、所有零点的支撑/重数/Q/支撑边、N2交叠及具体冲突|

现有求解器是静默编译版本，TIMEOUT日志可能为空。没有模型时不能提取局部图、失败结构、近似解或未满足核；如实回收“本次没有产生新的数学信息”。

### 结果怎样使用

- SAT：先独立核对完整原图；保留有效原图与继承理论/分支冲突的情况，不因冲突丢弃A。无效模型定位实际失败条件。
- UNSAT：保留 `RAW_UNSAT_NEW` 等原等级，仅关闭本输入。子叶闭合不关闭未齐的父范围。Q5的关闭对象是有覆盖支持的加强代表输入，不是全部旧Q5根。
- 全33入口及其必要互补叶闭合：只能记本合同下c1剩余代表RAW闭合；不是certified，也不是无条件N59定理。
- 超时、取消、内存问题或错误：范围仍开放，分别记录真实状态，不把超时解释为理论无效。
- 本轮没有受控对照，不能由耗时/CNF大小声称编码加速。

### 资源与产物边界

- 最多54个构建/求解子进程；其中构建器≤2，**占用同一54槽**；协调进程另1核，总数≤55。数值库单线程。
- 以下命令总墙钟上限12小时，含构建与15分钟收尾预留；根最多3小时、叶最多4小时，最多一层既有互补切分。理论最大66叶、99树节点，不增加父标签枚举。
- 修正旧队列：深度1也遵守叶时限，不占用全部剩余墙钟；从未尝试的范围优先于已有超时。每叶本session只执行一次，超时不会自动轮回重启。因预算或内存不足仍可能留未运行项，`untried_leaf_ids`明确列出，不承诺必覆盖。
- 名义上3小时根加两批4小时叶约11小时，留出构建空间；这是排队预算说明，**不是求解完成时间预测**。初始仅33个入口，末波可能少于54个，不能靠重复求解来制造满载。
- 本批可以在所有已安排尝试完成后提前以UNRESOLVED结束；12小时是上限，不是必须反复重启凑满的时长。
- 集群具体内存/存储额度未提供，不能写成已批准数字。沿用现有按cgroup可用内存和采样RSS节流；先检查该实例真实额度。上轮约32.3GiB求解器合计采样峰值不是本批保证。
- 20个常驻基础CNF，工作副本只保留运行中的attempt，结束后清理其临时目录；原CNF/map/log保留。每attempt普通日志上限128MiB；默认不生成可能很大的proof日志。
- 采样CPU写为 `cpu_seconds_sampled` / `solver_cpu_hours_sampled`，不把54×墙钟写成实测核时。

## 2. 环境与可复制启动命令

复用共享工程、Python3和已有AE_Kissat，不需要重新安装求解器。请在**计算实例**执行，而不是开发机。

```bash
cd /inspire/hdd/global_user/mahaitong-240108120090/mathagent/degree_diameter_sat

N59_MANUAL_ROUND=/inspire/hdd/global_user/mahaitong-240108120090/mathagent/formal_loop/N59_MANUAL12_ACTIVE_PRO_TO_CODEX_r2_20260928 \
N59_V6_WORKERS=54 \
N59_V6_BUILD_WORKERS=2 \
N59_V6_WALL_TIMEOUT=43200 \
N59_V6_FIRST_TASK_TIMEOUT=10800 \
N59_V6_CHILD_TIMEOUT=14400 \
N59_V6_MAX_SPLIT_DEPTH=1 \
N59_V6_FINAL_RESERVE=900 \
bash run55/start_n59_structural_v6_55cpu.sh
```

命令没有待填参数；仅执行一次。启动输出会给出实际run目录、PID、log、status/stop命令。目录为：

```text
/inspire/hdd/global_user/mahaitong-240108120090/mathagent/formal_loop/
N59_MANUAL12_ACTIVE_PRO_TO_CODEX_r2_20260928/runs/manual12_<hostname>_<UTC>/
```

这是路径的展示换行，**设置变量时必须复制完整单行路径**。启动入口会在同run冻结本次代码、原Pro包、数学正文、运行脚本与约束合同；不会修改r1目录。若误指定旧run，启动器在进入旧冻结代码前拒绝。

当前共享机器已确认Python3和 `solvers/satcomp2025/AE_kissat2025_MAB/kissat` 可用。若新实例未挂载上述共享路径，这条命令在那里不可运行，需要先挂载/同步，不用改成错误的相对 `global_user/...`。

## 3. 查看、停止与结束判定

启动时会打印可直接复制的命令。也可把实际完整路径设为变量：

```bash
campaign_dir='这里替换为启动输出的完整run_dir'
python3 run55/show_n59_structural_v6_progress.py --run-dir "$campaign_dir"
```

上面是查看示例，**占位符未替换前不可执行**。重点看 `closed_representatives/33`、`leaf_states`、`untried_leaf_ids`，不要把完成attempt数当成数学排除数。

正常结束依据：`run.json/sessions[-1].finished_utc`已写入，最终`progress.json`无live进程，并在启动实例确认launcher已退出。快照长时间不更新本身不能说明仍在运行。

停止同一run（只在启动它的机器执行）：

```bash
bash run55/stop_n59_structural_v6_55cpu.sh "$campaign_dir"
```

停止保留结果，不删除任务。中断后先回收状态再决定是否续算；恢复只能用同一r2包/同一run及用户明确剩余预算。Kissat没有内存学习状态checkpoint，恢复是任务级续接，不是从中断指令恢复。本阶段不预先授权额外12小时。

## 4. 下一阶段

用户手动启动后，提供实际 `run_dir`，进入同轮04回收。读取本run的精确输入、约束、范围与产物；无模型就不制造结构规律。原r1结果、原Pro r2包与本阶段开发/Lean记录都保留在共享目录。

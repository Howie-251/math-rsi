# $D=5$ 极小平面阻塞补全、部分折叠改色与专用批次工具

本参考供 [mathrsi-degree-diameter](../skills/mathrsi-degree-diameter/SKILL.md)、[dd-construction](../skills/dd-construction/SKILL.md)、[dd-transfer-diagnosis](../skills/dd-transfer-diagnosis/SKILL.md) 与 [dd-obstruction-certificate](../skills/dd-obstruction-certificate/SKILL.md) 调用。原件与便携复验包位于不可变归档 [dd-latest-two-parameters-20261116](../archive/dd-latest-two-parameters-20261116/README.txt)。

## 1. 保边扩张：极小平面阻塞集 $P$ + 全自由域补全 $T$ 与折叠端口成本

- **Caller 与前提**：当前简单图 $G$ 满足最大度 $\le \Delta$、直径 $\le 5$；自由集 $F=\{v:\deg_G(v)<\Delta\}$ 满足 $\bigcup_{v\in F} B_4^G(v)=V(G)$（否则返回漏点见证退出该源单点保边线）。$V(G)=V_{\text{core}}\sqcup V_{\text{ext}}$，外围 $V_{\text{ext}}$ 含原附点及此前全部新增前缀点。
- **无损分解与真实端口计费**：全奇异平面 $\Pi\cong PG(2,9)$ 的 91 线若被 $P\subseteq F\cap V_{\text{core}}$ 的原像全部命中，极化零点 $\beta(p,x)=0$ 经偶关联路径与 $\sigma,\pi$ 投影即保 $\bigcup_{u\in P} B_4^G(u)\supseteq V_{\text{core}}$。任何具该平面证书的合法邻集 $S$（$|S|\le \Delta$）必含包含极小 91 线命中集 $P$，尾部 $T=S\setminus P$ 从**全部当前 $F\setminus P$**（含同平面其余自由点）共同补齐 $V_{\text{ext}}\setminus B_4^G(P)$，不绑旧 85 模板或固定 `10+2` 配额。
- **折叠成本 $|\pi(B)|$**：度数消耗按折叠后互异 pins 数计费而非 raw 点数 $|B|$。Frobenius 稳定未 split 原像含 $f$ 个固定点与 $p$ 对共轭点时，$|B|=f+2p$ 而端口仅 $f+p$。`(12,5)` 实证中：`42,403` 取 `plane 340` 的 17 raw（5+6 对）耗 11 端口加单守卫 `41421`（`11+1`）；`42,407` 取 **18 raw（2+8 对）反仅耗 10 端口**留 2 守卫槽（`10+2`）；另有 18 raw 耗 12 端口兼覆外围（`12+0`）。每步插入后须在新完整图上重算 $F$ 与外围 provider。
- **全点对覆盖**：源 $G_0$ 的 $D\le 5$ 进口 + $E(G_0)\subseteq E(G_k)$ 保旧旧点对 + 终图全部 $k$ 个新增根完整 BFS（`42,433` 跑 31 根，或用 31 步逐前缀新根 BFS 归纳），配 Moore 界 $M(12,4)=17,569<42,433$ 得 $D=5$。

## 2. 部分折叠改色：单槽反例撤回前部、分量换向与混合点对覆盖

当固定源颜色在全部已知平面均出现空 provider 行（如 `(11,5)` 的 `37,631` 源在 1,120 平面全空，`0.20s` 确诊），对固定 split 纤维集 $S$（`|S|=4,074`，$\pi$ 固定到 `0..37470`）联合求解颜色 $c:S\to\{0,1\}$、平面 91 线端口 $P$ 与度数上限（任意双射 $\sigma_c$ 均保核心四步证书）：
1. **单槽严格反例即停调尾**：按字面关联表、$\tau,\sigma_c,\pi$ 重建核心（边发生增删，旧外围路径不自动保持）并接 `160` 旧外围与 `10`-pin 新点 $z$ 得 $G_0$。剩 1 槽 $z\text{–}a$ 时，$d_{G_0+za}(u,v)=\min(d_0(u,v), d_0(u,z)+1+d_0(a,v), d_0(u,a)+1+d_0(z,v))$。首方向 `37,632` 候选中坏对 `(37546,37618)`（距 6，$d_0(u,z)=4, d_0(v,z)=5$）迫使唯一锚点为已满 11 度的 `37618`，`0.21s` 严格否定该固定前部的一切单边补尾，立即撤回前部而非继续刷坏对分数。
2. **连通分量补色换向**：在 split 相邻图的连通分量上整体取反 $c\mapsto 1-c$，同色/异色关系、全图度数向量及核心 91 线证书完全不变，但反转异色匹配方向。对 `4,060` 点主分量补色将相对 `37,631` 源的改色数从 `3,955` 压至 **`105`**（核心 `-186/+212` 边），一次修好全部 `4` 对旧外围坏对。
3. **精确锚点交集与混合全点对覆盖**：对余下 `3` 对涉 $z$ 坏对在 `2,409` 个合法余度点上求上述不等式的精确共同交集，得 `161` 个解，取 `anchor = 31` 闭合 `37,632`。全图点对分两块严密闭合：(i) `Core × Core`（`0..37470`）由奇关联路径转换（Rajiv Lemma 3.1）及显式特征 3 叉积/`91-star` 源路由桥配合字面 $\sigma,\pi$ 绑定（`203,747` 核心边逐边相等）覆盖；(ii) 其余一切点对由最终图全部 **`161` 个非核心根（`37471..37631`）完整 BFS** 覆盖，配 $M(11,4)=12,222<37,632$ 得 $D=5$。

## 3. 有限批次边界、共享 Lean 缺口与工具调用契约

- **终止语义与认证记账**：`BATCH_LIMIT_REACHED` 仅达本批 `max_new`，非机制耗尽（`(12,5)` 四批 `P_tail_checks: 1 → 1,084 → 10,871 → 88,500` 反映余度耗损，末批在搜 `42,434` 时触 20s 预算停于 `UNKNOWN_WHOLE_CPU_LIMIT_AFTER_ACCEPTED_GRAPH`）；**已完整刷出且过独验的前缀照常验收保留**，未完步记 `UNKNOWN`，半行 JSON 不计候选。`COMPLETE_NO_IN_CURRENT754_SUFFICIENT_PLANE_DOMAIN` 仅关闭当前 754 平面证书域。通用模块（`SingleExtension`、`H9CrossRouting/Geometry/Kernel/Star`）通过内核检查不代表源图 `42342/42402` 或 `Fin 37632` 具体 Lean 已闭；缺失源证明作为**家族单一共享待办项**，禁止对每个 `+1` 重复编译带同一缺口的 wrapper。
- **为什么修正版专用工具放在 `tools/`**：`archive/` 保存不可变历史原件；`plugins/degree-diameter/tools/` 中的修正版脚本修复了相对路径解析与源 `(n,m)`+证据绑定，并通过严格 family 守卫拒绝非匹配任务，可直接消费归档内保留的 `RAW_PLANES_ACTUAL_IDS.txt` 完成真实的家族续接，绝不冒充任意 $D=5$ 通用搜索器：
  1. **便携重建与 161/31 根核验**（不改归档，输出写任务目录）：
     ```bash
     ARCHIVE="/path/to/MathRSI/plugins/degree-diameter/archive/dd-latest-two-parameters-20261116"
     python3 "$ARCHIVE/reproduce.py" --compare --output-dir /task/out/reconstructed
     python3 "$ARCHIVE/verify.py" --output-dir /task/out/verified
     ```
  2. **逐点保边收据消费** [extension_receipts.py](../tools/extension_receipts.py)（配合 [current-context](../../../base/skills/mathrsi-research/references/current-context.md)，限定原逐前缀 checker 格式，核源 `(n,m)`+已接受源证据、保边、当步新根 BFS 与终图 `MATCH`，幂等写回且不抹去同图后续 `UNKNOWN/No` 停止态）：
     ```bash
     python3 /path/to/MathRSI/plugins/degree-diameter/tools/extension_receipts.py \
       --state /task/STATE.json --family 12,5 \
       --author /task/batch/RESULT.json --independent /task/batch/independent/RESULT.json \
       --acceptance-basis "父调度已核前缀独验、保边及终图一致；42402源D5沿用；源Lean仍开"
     ```
  3. **`(12,5)` 绑定域专用续批** [d5_blocking_batch.py](../tools/d5_blocking_batch.py) + [d5_blocking_batch.cpp](../tools/d5_blocking_batch.cpp)（**仅对 `generator_domain == "d12_754_planes_core41356"` 开放**，需 POSIX/`g++`；`--plan-only` 只读检查，实跑要求 `ACTIVE`、无漏收 `terminal_result` 且计划源仍为最新已接受阶数，产出标 `independent_validation: PENDING`）：
     ```bash
     python3 /path/to/MathRSI/plugins/degree-diameter/tools/d5_blocking_batch.py \
       --state /task/STATE.json --planes "$ARCHIVE/originals/ar4math/research/ddp/expert15_20261114/d5_resume_20261115/d12_blocking_family_continuation/RAW_PLANES_ACTUAL_IDS.txt" \
       --output /task/d12_next_batch --max-new 8 --cpu-limit 20 --wall-limit 480 --plan-only
     ```

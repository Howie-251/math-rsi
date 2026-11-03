# Fixed-S cross-port extension — PASS

固定六方向 `S=[inf,0,1,2,3,6]` 现具有完整跨端口 glue。15个 unordered `p<q` 各选确定性字典序首 PGL 补集映射，并使用真逆构成30张新有向 chart；新增750个中央 turn 全满秩。每张新 chart 的源／目标 port 向量运输、双侧真逆、全部9个噪声方向、十条商射线及729点 pencil 覆盖均通过。

旧12张 self-port chart 及300个 turn 直接继承，没有重算。完整参数现含42张实际 chart、1050个有通过回执的 turn，其中750项为本次新检查。未重新生成720个 PGL 元素或重跑252半集分类，只复用其保存的系数与结论。

对实际 dart 的两端局部标签 p、q，异标签按 p<q 选择 canonical 正向、p>q 选择其真逆；相同标签按 u<v 取旧正向、反向取旧真逆。反向 dart 必然切换到实际逆矩阵。因此每顶点可独立按 sorted neighbors 标 ports，无需全局6边着色；没有此处的 target-port 绑定缺口。完整论证见 `PROOF.md`。

一次单worker，PID2273058，exit0，有限检查0.167296002 CPU秒，5CPU硬上限。0 controller／fiber graph／BFS／solver／Lean／hash／install，不计新增图，不声称 C78 或完整54度D3图已存在。该结果仅使用固定 S。

交接：`PARAMETERS.json` 含42张矩阵及直接 source/target lookup，`CHART_CHECKS.json` 含新增750项和30个 pencil 回执，`PROOF.md`、`RESULT.json`、`TERMINAL.json` 给出完整范围与终态。父目录旧证据保持不变。

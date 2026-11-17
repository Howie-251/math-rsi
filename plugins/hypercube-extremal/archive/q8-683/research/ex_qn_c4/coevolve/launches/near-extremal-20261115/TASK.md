# 新的 GPT-6.1 Sol 研究任务：近极值构造与上界协同

**用户最新目标澄清：先读同目录 `PRIMARY_OBJECTIVE.md`。主任务是证明 ex(Q8,C4)≤682；搜索 683 边图只是对抗验证辅助目标，不能代替上界证明的验收。**

用户已明确要求直接启动新任务，并允许读取已有研究结果。他指出 646–648 边的构造对区分 682 与 683 的紧上界帮助有限。当前授权是实际推进新的协同研究，不能停在计划或只解释能力；不需要再询问是否开始。新任务与原线程暂停的旧 Goal 分开，旧状态不阻止这里已明确授权的行动。

工作目录：本文件上两级目录 `coevolve/`。所有改动限于其所在 research 工作区；不要修改相邻 MathRSI 仓库或历史证书。默认模型与实际调用配置为 `gpt-6.1-sol`。该任务继承的宿主 cwd 可能仍是 math-rsi，开始后应显式使用 research/ex_qn_c4/coevolve 作为工作目录。

## 先读取真实结果，避免重跑失败路线

先读 `README.md`、`AGENTS.md`、`implement-stage/BUILD_NOTE.md`、`implement-stage/ASSUMPTIONS.md` 和 `runs/q8_live/REPORT.md`、`runs/q8_live/state.json`。工程试跑完成三轮 Q8、六次模型调用；最好仍是 682，最后四张新图只有 646–648 边。不要将它们写成极值进展。

随后读父目录的 `REPORT_015.md` 与 `RESEARCH_STATE.md` 顶部、`NEXT_ACTIONS.md`，以及 `../research-wiki/index.md`、`query_pack.md`。Wiki 只是导航，以下义务需读取对应完整证明/报告/核验，再决定是否使用：

- `../proofs/q8_universal_small_repair_cycle015/PROOF.md` 及 review：每个 odd682 的两删除障碍、任意 odd 图的四切换障碍。
- `../proofs/even_near_optimal_completion_cycle013/`：odd680 的纯加边路线已排除。
- `../proofs/q8_seed_isometries_cycle011/REPORT.md`：真实种子与已知同构/非同构范围；13 状态及三个方向的旧封闭结果按实际调用范围再读。
- `../proofs/q6_variable_marked130_cycle015/REPORT.md` 与实际边表：单 F 的 129 界已被真实 130 图反驳。
- `../proofs/q7_hole_extension_cycle015/PROOF.md`：1,430 个必要布局不是 Q7 图。
- `../proofs/q7_slack_cycle005/CURRENT_TARGET.md` 及 `../proofs/q7_joint_faces_cycle008/PROOF.md`：J≥73 尚未证；210 个必要配置与四种 Q8 低度分支未闭合，现有路线首先争取排除 687。

按需读相关 wiki 实体全文和失败证据；不要重读全部档案，也不要把旧 Goal active 字样当恢复授权。研究的新实质事实须在核验后增量写回当前任务 wiki，注明新协同任务及准确范围，不重写 Cycle015 冻结证据。

## 已准备好的新起点

`configs/q8_near_extremal.json` 有四张原 682 种子、24 张可复现的派生 680/681 样本，并保留稀疏探索材料。来源与删边清单见本目录 `SEED_INVENTORY.json`，准备脚本为 `prepare_seeds.py`。这些样本只服务局部指标校准，不能宣称是新构造机制。

新增 `quality_band.min_edges=680`：主体亲本和上界发现样本优先工作带；最多留一个带外探索亲本。所有档案图仍核验不等式。novelty/challenge 通道对带外样本先惩罚边数缺口；带内保留有界的新颖性/残差信号；真实适用反例即使稀疏也有价值。程序内部可跨越暂时低边数状态，工作带不是对可行图的排除。

首批重点是**在近极值区域获得新的结构信息**，而非强行每轮提高边数。可利用非奇方形 680–682 图、不同度数/缺陷配置、足够大的混合交换和系统构造；不能只重复已排除的小删除邻域。保留 682 精英，分开报告近极值创新、带外探索和实际反例。680 可根据真实反馈调整，新参数必须解释。

## 现在执行

先检查 `implement-stage/near-extremal-tests.log` 的实际退出情况，再运行首批四轮：

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m cube_coevolve run \
  --config configs/q8_near_extremal.json \
  --output runs/q8_near_extremal_research \
  --rounds 4
```

若输出已存在，先检查 state/错误及是否有活动进程，按真实断点恢复，不覆盖它。不要无信息地扩大 timeout 或挂几十轮同一程序。根据首批实际源码、图簇、不等式和失败反馈修正方法：若生成器只退回原 682 亲本，改进程序与局部目标；若上界只是拟合漂亮曲线，检查其是否能约束 683+，必要时转向明确条件下的 Q6/Q7 局部对象，但要证明回原问题的连接。

候选条件独立于任务条件。`edges>=680` 的条件自动涵盖所有 683+ 候选；`min_degree>=4` 等条件不能凭愿望加上。不等式的样本支持、局部求解成功与 Q8 上界证明分开记录。每个可能的 683+ 图都需独立边表核验；新的全称排除需要真实覆盖与证书或完整结构论证。

首批完成后保存本目录 `PROGRESS.md`：已读原件、实际调用、近极值/探索分布、有效不等式及反例、失败原因、是否改进原目标、具体下一步。依据真实进展继续有界批次或具体证明工作，及时向用户报告，不以运行轮数代替数学价值。旧研究状态与此前验收报告保持历史原样。

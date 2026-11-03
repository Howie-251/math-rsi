# Degree–diameter：构造、覆盖与有范围的排除

本插件研究有限简单无向图的最大度数和直径：在 `Δ(G)≤d`、`diam(G)≤D` 下构造更多顶点，或证明一个明确构造域不能达到目标。它通过现有五个 MathRSI workflow 工作；不启动归档中的旧 Goal，也不把历史结果算成 MathRSI v2 的解题实验。

研究成果、公开比较和构造图解见 [Degree–Diameter 案例（English）](../../case-studies/degree-diameter/README.md)及[中文版](../../case-studies/degree-diameter/README.zh-CN.md)。案例附有离线交互页面和全部 153 张图的紧凑构造程序。

从[领域入口](skills/mathrsi-degree-diameter/SKILL.md)开始。已有明确义务可以直接调用：

- [构造推进](skills/dd-construction/SKILL.md)：当前覆盖增点、冻结完整邻域克隆、仿射共同路线与 GQ 填补。
- [排除与证书](skills/dd-obstruction-certificate/SKILL.md)：必要门、精确有限域、旧路径损伤、共享参数和整数 dual，或固定图原命题核验。
- [迁移诊断](skills/dd-transfer-diagnosis/SKILL.md)：换参数／源图／连接规则后重判可继承证据、失败边界与公开比较。

整理层包含可直接调用的定理条件、证明、实际失败输入、命令及消费者：[阅读与调用地图](references/reading-and-calling.md)、[数学工具](references/construction-mathematics.md)、[排除与证书数学](references/obstructions-and-certificates.md)、[Lean实际接口](references/lean-and-representation.md)、[运行与依赖](references/programs-and-replay.md)、[失败与修法](references/failure-and-transfer.md)。

原研究 wiki、正文、代码、结果、审阅、形式化和构造器完整保留在 [archive/source](archive/source/)。原包本身省略的大图／工具链／部分 JSON 没有因此出现；[归档与来源](archive/README.md)说明原包范围、缺件及阅读账本。归档中的绝对路径、ACTIVE、预算、timer、模型选择和“下一步”均为历史资料。新研究的规格、运行和 wiki 写自己的工作区，插件维护交外层 meta-evolve。

从当前任务工作区调用；先把 `DD_PLUGIN` 设为当前克隆的真实插件绝对路径。下列两个命令只读输入，结果输出到终端：

```sh
DD_PLUGIN="/path/to/MathRSI/plugins/degree-diameter"
python3 -B "$DD_PLUGIN/archive/source/constructors/early_d5/verify_covers.py"
python3 -B "$DD_PLUGIN/tools/replay_mizuno_dual.py"
```

前者检查103步当前图覆盖，继承源图 D5，不是103图全根 BFS；后者只核已保存容量模型的364列 exact dual，不证明几何行必要性，也不排一般14度图。实际本次运行记录见 [evidence/IMPLEMENTATION.md](evidence/IMPLEMENTATION.md)。完整图重建使用原 [rebuild.py](archive/source/constructors/late_graphs/rebuild.py)，写当前任务副本；生成图不等于已验距或新完成 Lean。

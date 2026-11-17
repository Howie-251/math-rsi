# 双端协同研究框架

目标：维护可扩展的精确局部指标；让模型生成构造程序，执行并独立验证输出；从图簇提出、反驳和更新有显式条件的不等式，再把其残差与结构新颖性反馈给下一轮构造与程序选择。支持 Q8 的 683 边目标及条件目标。

输入：任务 JSON、指标定义、真实种子边表、模型配置。输出：逐轮程序、模型原文、图与指标、候选不等式及反例、奖励快照、可恢复状态与报告。样本支持不升级为全称证明。

成功命令：`python3 -m unittest discover -s tests -v`；`python3 -m cube_coevolve run --config configs/smoke.json --output runs/smoke --rounds 2`；实际 Codex 调用的双端闭环另行记录。

Base commit: none (研究工作区不是 Git 仓库；MathRSI 只读)。仅写本目录；不恢复旧数学长程 Goal，不改旧证据。实现借鉴 AlphaEvolve 的程序档案—生成—确定性评估循环，不声称复制其系统或已有数学效果。

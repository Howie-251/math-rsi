# 实际耗时字段与复现

timings_by_experiment.csv从现存JSON递归提取键名含elapsed、duration、wall_time、cpu、seconds、runtime的原字段，逐项保留source、JSON路径与原值。非数值、超时预算、累计值与实际测量混合存在；空值不等于零，不能全表相加为端到端研究耗时。

trajectory_index.csv保存每份结构化研究记录的状态原文、概要、依赖与时间字段。状态可能是历史条件性PASS、FAIL、UNKNOWN或无状态，均不能仅靠名称升级成最终数学结论。

工具真实命令及输出：trajectories/TOOL_EXECUTION.jsonl。搜索、独立检查、模型等待、报告制作的耗时必须分开，机器工具显示的wall_time可能只是一段轮询时间。

本次新执行的验证及时间存verification_runs；历史验算保留其原始范围。复现级别与命令见REPRODUCE.md。没有完整端到端人工/模型等待时间记录的地方不补造。

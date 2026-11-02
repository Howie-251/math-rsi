# 同一非相邻双缺陷机制第2轮：实际完整代码

数学范围和PLAN保持第1轮相同，不增加Wi独立、全局D匹配、h值、交数或对称模板。请完整读取本目录实际四份代码和它们使用的通用定义：

- computations/dd82/n61/nonadjacent_double46_full61_run/encode.py
- computations/dd82/n61/nonadjacent_double46_full61_run/check.py
- computations/dd82/n61/nonadjacent_double46_full61_run/sanity.py
- computations/dd82/n61/nonadjacent_double46_full61_run/runner.py
- 实际导入的 computations/dd82/n61/joint_six_star_h35_run/encode.py 的CNF/neg/truth；不需要复核或运行其旧build/main。
- 实际导入的 computations/dd82/n61/adjacent_double_full61_run/runner.py 的bounded及路径/资源常量；不运行其旧main。
- 本新目录 sanity.json、sanity_process.json、ROOT_REVIEW.md、IMPLEMENTATION.md；若ENCODE_MATH_REVIEW.md已在则读取本地独立结论。

请直接检查：1658原边的全部自由范围、1830对精确共同邻数、共享1..4阈值是否双向等价、相邻c≤1和根c≤2的正确区别、R lex是否仅合法重标且等号保留、SAT解码是否逐条验保存输入以及独立BFS是否真的验完整目标、单次预算和UNKNOWN/RAW等级是否正确。不要仅复述本地PASS；有实际错误给具体路径/修正，无错误则直接SCOPED ACCEPT这份实际实现。

sanity实际exit0，11.926561CPU／11.939842794wall，504158变量1816574子句仅在内存构造。五份真实图赋值的1830对全部与独立整数核对；8正则打样实际直径4，未伪造完整目标正例。尚未prepare或solver。正式计划为一次无proof 90CPU/120wall（软88），单核4GiB、每文件256MiB，无重启。

只读审阅，不启动计算/改文件，不要求安全包装、hash、Lean、参数阶梯或额外不承重审计。若数学与代码均正确，本轮接受后根执行既定唯一有界发现；下一轮只依据真实结果做范围处置。请求与返回模型元数据保持原线程。

# 全局完美匹配生成58点完整图

`generate.py` 读取已保存的 polarity73 `refined/n58/deletion_candidate.json`
中的删除标签，通过原 `screen.py:geometry()` 读取背景数据；不复制几何生成器，
也不固定筛选器选择。58个幸存标签仅提供初始几何偏好。

每个 seed 从空图开始，八轮各加入29条互不重边的完美匹配。每条可用边的
单独新增覆盖收益为精确的 `g`；NetworkX 整数最大权匹配使用
`(30*g + old_flag)*30000 + rng.randrange(1000)`，并要求最大基数。
匹配29边，故旧边数差最多29、随机项总差最多28971：这严格实现
“收益之和、几何旧边数、seed平局扰动”三层字典序。seed只能打破前两层同分。
所有几何旧边均可缺失，没有保护核、匹配删边预算、局部交换或自动重启。

收益之和可能重复计算同一修复；每轮都从合并后的真实图重新计算坏点对，
保存预测收益、实际收益及差值。每轮匹配不含相邻新边，实际新增覆盖是各
单边修复集合之并，所以预测和至少为实际收益。最终必为58点232边八正则
简单图；直径需另验。八匹配可分解性只是初始种子限制，不代表所有目标图。

用法：

```text
python3 generate.py sanity --out-dir OUTPUT
python3 generate.py generate --seed-start 0 --seed-stop 8 --out-dir OUTPUT
```

停止 seed 不含在范围内，合法范围为0至7。每个 seed 的 `rounds.json` 逐轮保存，
`candidate.json` 与 `candidate.edges` 保存完整结果；中断时未完成 seed 不会
冒充完整图。`results.json` 按有标签排序边表直接比较去重，保留每个实际结果
及重复来源；不生成哈希，不声称非同构。重复批次需独立输出目录，不覆盖旧结果。

候选 JSON 包含 `n`、`edges`、`ambient_labels`、完整坏点对、每点三角形数及
几何旧边保留/删除数量，兼容现有独立 `verify_hs_candidate.py`。生成器记录
内部距离二检查，明确独立验证尚未执行；根代理另调独立 checker。

`sanity` 只在五张小图上逐条比较单边收益与独立 BFS，并检查一个预测6、实际4
的共享修复例子及权重优先级界。它不生成58点种子，不运行完整实验。
完整8种子批次及CPU/墙钟上限由根代理的独立 runner 控制。

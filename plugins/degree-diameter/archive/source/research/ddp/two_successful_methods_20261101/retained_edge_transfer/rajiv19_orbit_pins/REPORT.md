# Rajiv19：点轨道与几何线pin规则的实际对照

公开2783点源已按作者PG排序／β约定生成一次，1331点度18、1452线度19；源D3继承公开定理，没有重跑旧全源BFS。

11点transvection orbit确实R2覆盖全部1331点，但只覆盖600条线、缺852。改用一条W-line上的11个点，实际仍覆盖全部点，并完全覆盖其余11线类，只在一个121线类缺106条。这是实质覆盖改善，尚不是新图。

剩余8pins问题可无损化成K上任选9个provider（整11线pencil＋4gadget邻点）覆盖121目标。精确容量给55种未选pencil对中54种最多21/22；唯一(3,9)对再由每pencil最多贡献[1,2,2,3,3,2,3,2,3]、合21严格排除。因此全部Wline11＋8规则已停止，避免base／class／seed续扫；未用solver。

预处理0.183CPU、最终容量门0.00257CPU；新图0。任意19pins和orbit11＋8未被排除。

[完整推导与标签桥](PROOF.md) · [事前预测](PRED.json) · [实际对照](CONTROLLED_COMPARISON.json) · [55对完整整数证据](ALL_BASE_CAPACITY_FINAL.json) · [终态](RESULT.json)。

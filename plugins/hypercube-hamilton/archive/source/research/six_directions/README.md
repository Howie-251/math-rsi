# Six-direction research run

主报告：[PROOF_PACKAGE.md](../../PROOF_PACKAGE.md)。完整六方向猜想 **未证明**。

最新续进：[N10完整图近完美引理](GENERAL_NEAR_PERFECT.md)允许同奇偶长边；[Z6](UNBALANCED_TRANSFER.md)完成一孔/三孔的条件转移；[Z8](DISTANCE_TWO_UNBALANCED.md)对同奇偶孔距离2、根单独在一侧且目标在另一侧的全部Q6四孔匹配成立。[Z7](UNBALANCED_CORE_THEOREM.md)特别关闭孔{0,3,13,49}、根0、目标61的全称族。33条Z7与56条Z8构造由verify_unbalanced_transfer.py独立检查；这是有限回归，证明在上述文稿。审读记录GENERAL_NEAR_PERFECT_REVIEW.md，仍为same-family/provisional。

较早续进：[N6—N8二部近完美引理](BIPARTITE_NEAR_PERFECT.md)与[N9](NEAR_PERFECT_ADJACENT.md)已统一处理二部近完美匹配；[Z5同侧转移](SAME_SIDE_TRANSFER.md)补上另一类切分。旧审读和见证保留。

旧样例经Z5后还剩381例（六孔157、八孔224），其中四孔样例全部有统一条件覆盖，但全体四孔问题仍未完成。[无平衡切分历史义务](UNBALANCED_FOUR_HOLE_CORE.md)中的指定族现已关闭；当前缺口见[NEXT_OBLIGATIONS.md](NEXT_OBLIGATIONS.md)。

最新：[N5/F6自由端点四孔定理](FREE_ENDPOINTS_FOUR_HOLES.md)统一处理全部n≥5四孔短边匹配的异奇偶自由端点，不再限制孔的几何；[审读](FREE_ENDPOINTS_FOUR_HOLES_REVIEW.md)完成28项义务。[Z4/R1/R2人工边归约](AUXILIARY_ENDPOINT_REDUCTION.md)进一步处理部分四孔已覆盖目标和六孔自由目标，适用切分仍是显式前提；对应审读AUXILIARY_ENDPOINT_REDUCTION_REVIEW.md。状态均为same-family/provisional，未认证新颖性。

本轮30条F6及19条R1/R2构造通过独立检查，脚本为verify_free_endpoints.py、verify_auxiliary_reduction.py。原1152例按统一条件还剩398例：30边17例、29边157例、28边224例；不是全空间剩余数。旧阶段数字保留作历史。

2026-11-01续：[双层转移Z1](FOUR_HOLE_SPLIT.md)进入已覆盖终点情形；[距离五四孔Z2](FAR_FOUR_HOLES.md)和[距离3/5矩形四孔Z3](RECTANGULAR_FOUR_HOLES.md)对各自全部30边匹配给出圈延拓，分别给出10和11个已覆盖终点的路径。这不是全部终点结论。对应独立上下文审读见SPLIT_TRANSFER_REVIEW.md、FAR_FOUR_HOLES_REVIEW.md、RECTANGULAR_FOUR_HOLES_REVIEW.md，状态same-family/provisional。

旧1152样例中，无统一引理覆盖的数量经Z1由500降为419，仍非全空间比例。残余样例包含30边27例、29边168例、28边224例；即使完整四孔情形闭合，更多孔的目标仍未解决。新175个构造见证经verify_split_transfer.py独立核验通过，结果见split_transfer_verification.json。

复现新构造：运行split_transfer.py、far_holes_probe.py、rectangular_holes_probe.py，再运行verify_split_transfer.py。完整目标和下一义务见NEXT_OBLIGATIONS.md。

后续四孔工作：[推导F1—F5](FOUR_HOLE_DERIVATION.md)、[独立审读](FOUR_HOLE_REVIEW.md)、[文献核对](FOUR_HOLE_PRIOR_ART.md)。F1允许暂时遗漏一条原匹配边，最终严格恢复；在旧样本中新增关闭4个未覆盖终点实例。40个已覆盖终点实例的1—2切口修补通过独立验证，不能据此宣称一般修补引理成立。

2026-11-01：[近完美补全推导](NEAR_PERFECT_EXTENSION.md) 已关闭全部六维31边实例及其保持指定起点未覆盖的可补全子匹配；[独立审读](NEAR_PERFECT_REVIEW.md) 未发现实质性错误，仍为 same-family/provisional，不声明新颖性。N4给出剩余补全障碍的Hall刻画。原六维样本未被统一引理覆盖的数量由535减为504；这不是全空间证明比例。

第二轮历史结构推导：[CORE_DERIVATION.md](CORE_DERIVATION.md)，包括可补全类和跨层奇偶障碍实例。其旧31边剩余分支已由上述N3闭合。

## 已完成

- 读取用户PDF并核对第2页原文；提取精确有限义务P6。
- 文献查重：PRIOR_ART.md；原作者源码范围审计：SOURCE_AUDIT.md。
- 两种不同搜索模型（C++回溯、SciPy/HiGHS整数规划），独立Python证书检查。
- Q2/Q3共174个避零端点实例完整验证；Q6的36模板×32终点共1152实例验证。
- 36个模板中20个使用全部六方向；按论文机制生成Q7/Q8匹配延拓圈，分别57/117条匹配边。
- 三个终点标准形的剩余覆盖CNF：仅导出，未证明不可满足。

## 复现

当前可用Python为 `D:/anaconda/python.exe`，SciPy版本1.16.3；不依赖OR-Tools。

```powershell
g++ -O3 -std=c++17 E:/新问题/research/six_directions/path_search.cpp -o E:/新问题/research/six_directions/path_search.exe
& D:/anaconda/python.exe E:/新问题/research/six_directions/test_search.py
& D:/anaconda/python.exe E:/新问题/research/six_directions/run_pilot.py
& D:/anaconda/python.exe E:/新问题/research/six_directions/milp_retry.py
& D:/anaconda/python.exe E:/新问题/research/six_directions/verify_witnesses.py E:/新问题/research/six_directions/pilot_results_retry.json
& D:/anaconda/python.exe E:/新问题/research/six_directions/lift_templates.py
& D:/anaconda/python.exe E:/新问题/research/six_directions/verify_cycles.py E:/新问题/research/six_directions/lifted_cycles.json
& D:/anaconda/python.exe E:/新问题/research/six_directions/export_obligations.py
& D:/anaconda/python.exe E:/新问题/research/six_directions/verify_obligations.py
```

搜索预算：每个DFS实例200000节点；MILP仅重试UNKNOWN实例，每实例约5秒软预算。重运行可能因库版本或求解器启发式获得不同路径；结果必须再次检查。`run_pilot.py`只有三个小维数/六维采样范围，绝不代表六维穷尽。

## 下一研究义务

对 `remaining_v1.cnf`、`remaining_v7.cnf`、`remaining_v31.cnf` 做可恢复的“候选匹配—路径见证—覆盖排除”循环；SAT模型只是未被现有路径覆盖的匹配。只有每分支剩余域为空且有可复查穷尽/UNSAT证明，才能关闭P6。若求解器找不到路径而超时，记UNKNOWN；需完整无路径证明才能报反例。

当前认证族已经有严格的高维延拓证明，但不宣称文献新颖性。没有启动无界后台搜索。

## 近完美补全与单跨边核验

```powershell
& D:/anaconda/python.exe E:/新问题/research/six_directions/single_bridge_probe.py
& D:/anaconda/python.exe E:/新问题/research/six_directions/verify_near_perfect.py
& D:/anaconda/python.exe E:/新问题/research/six_directions/construct_near_perfect.py
```

第一项为96个固定种子、27—30边的单跨边实例，全部找到恰好3条跨边的路径；第二项独立检查这些见证，并做小维数刚性引理反例排查和旧样本补全分类；第三项实际执行16个31边实例的“加入长边—中间路径—删除长边—短边拼接”。这些计算均非完整Q6穷尽，N3证明不依赖样本成功。

## 四孔后续复现

```powershell
& D:/anaconda/python.exe E:/新问题/research/six_directions/one_displaced_edge.py
& D:/anaconda/python.exe E:/新问题/research/six_directions/four_hole_surgery.py
& D:/anaconda/python.exe E:/新问题/research/six_directions/verify_four_hole.py
```

固定中间延拓反例尝试脚本fixed_extension_obstruction.py未得到反例；求解器的无解状态不作为独立认证的不可满足证明。不要将该尝试计入已证结论。

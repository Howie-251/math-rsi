# Critical packet 8→70：四全局电压族的完整 NO 与边界

结论：**支持 `COMPLETE_NO_FIXED_BASE_FOUR_GLOBAL_COEFFICIENT_C23_FAMILY`，不排任意 ordinary23-cover。** 本review只读已保存代码/结果/paths/forms；没有新base、路径、参数、field、BFS、cover或solver计算。

## 证据与逻辑绑定

[RESULT](CRITICAL_PACKET_RESULT.json) 给实际pair8→70：长度0..5的NB路径数依次为 `0,0,0,1,10,55`，共66条；[FORMS](CRITICAL_PACKET_FORMS.json) 有26个distinct mod23 four-coefficient forms。两项容量预测均通过，不能再把失败解释为路径条数少于23，或永远同form后仅剩不足23个可能phase。

已读 [唯一脚本](run_critical_packet_once.py)：

- 在已保存240点真实point-arcs上，只以 `next_vertex==previous_vertex` 排除立即反向同edge；没有误删controller reverse但λ不同的路线。
- 到target时保存该prefix，仍继续至长度5，故并非只保第一次到达或某一个长度。
- 每步按0/2正号、1/3负号累计整数 `(1,λ)`，最后才mod23；对应原 ordinary-cover 逆电压，未先mod2。
- 对26个forms的所有first-nonzero-coordinate=1参数，依次枚举 `23³+23²+23+1=12720` 个scalar规范代表。结果和 [SURVIVORS](CRITICAL_PACKET_SURVIVORS.json) 为0幸存，[PHASE_COUNTS](CRITICAL_PACKET_PHASE_COUNTS.tsv) 完整保存每代表的覆盖量，实际最大22/23。

非零共同scalar重标cover的C23坐标，不改变是否全覆盖；zero参数只有phase0，更不可能覆盖23。因此这个**单一base pair**已经给出全部四全局系数的反例：每个参数都缺至少一个lift目标，足以证明该族无D≤5。事前“forms至少23”的预测支持，“存在一组共享电压使此pair满23”的后续预测被反驳。无需再测其它pairs或生成5520图来得到这个负结论。`all_pairs_tested=false` 正确保留，不能改成已经逐对检验。

失败的实质是：26个可区分forms在同一个四维参数上作dot-product，不能同时产生23个phase；共享电压的兼容性失败，而非66条原始路径容量不足。更自由的每edge电压会改变这些forms，所以本结果不排任意ordinary23-cover、其它fold或一般8D5。此前所有base-pair NB容量通过也不保证它们存在。

## 保存路径给出的具体可拆分碰撞

[PATHS](CRITICAL_PACKET_PATHS.json) 的0-based index1与index14分别是：

| index | 实际base vertices | `(port,λ)` 顺序 | 保存的整数form |
|---|---|---|---|
| 1 | `8–104–10–30–173–70` | `(0,0),(1,1),(2,1),(1,0),(1,0)` | `(-2,-1,1,1)` |
| 14 | `8–16–9–29–172–70` | `(1,0),(0,1),(2,1),(1,1),(1,1)` | `(-2,-1,1,1)` |

所以在旧规则下，它们对**每一组** `(cA,dA,cB,dB)` 都有相同电压，重复路径不能提供额外phase。

一个具体、可检验的下一结构问题是：给实际无向point-edge `{8,104}` 一个独立电压perturbation ζ，正向8→104加ζ、反向104→8减ζ，其它edge不改。index1恰正向使用它一次，index14完全不使用，所以二者差从恒0变成ζ。逆电压仍合法，base和fold不变；这说明一个明确的edge-dependent自由度能够打破已保存的全局同form绑定。

这只是指出哪里需要改变共享约束，**不承诺**增加这一个ζ就能使本packet满23，更不保证全部pairs或5520/D5。若root选择追问，最小输入就是这66条保存路径及原forms，按有向edge使用数补一列即可；不用新词、源图/BFS、另一base或field。本review没有补列或枚举新参数，也没有授权这样做。

注意单纯把controller标签的电压常数改成局部常数，未必拆开实际point-edge碰撞：同controller一去一回但λ不同的两条edge可能在该常数上仍抵消。因此上面的明确point-edge扰动不能未经核对偷换成controller-only扰动。

原case实际CPU1.496812969/5、0目标图、0新增参数/Lean保持原记录。review两个标准库只读进程CPU合计0.001737855秒，文档准备可保守计0.10秒，由root决定并入；未修改任何原结果或root/Wiki文件。完成即停。

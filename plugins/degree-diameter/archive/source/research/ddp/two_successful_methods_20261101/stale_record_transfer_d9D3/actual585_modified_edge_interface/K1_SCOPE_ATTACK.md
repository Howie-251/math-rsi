# K1 gate：只读范围与漏域攻击

已读 [OWNER_P0_NEXT_INTERFACE.md](OWNER_P0_NEXT_INTERFACE.md)、[K1_PRED.md](K1_PRED.md) 和实际 [K1_once.py](K1_once.py)。本文件没有执行该脚本、解析source或mask数值文件、枚举packing、构R2、BFS、field、匹配或586图。独立reader保守准备收费总计 **0.30 CPU秒**，已由数值owner计入同case，不另加第二笔。

## 1. 65位与真实label绑定

代码从已绑定的 `PORT16_ELIGIBLE_EDGES.json` 读取p0 actual label/index均0；原64位映射为不含p0的64个actual ports。新映射明确为 `[0]+旧映射`，断言65个互异label。不是把图label直接当port bit。

far旧16位mask左移1，bit0必须为0；owner cut旧mask排除了p0而有15位，因此左移1后补bit0，断言结果16位。此转换保留原最高port位，代码使用Python整数与`(1<<65)-1`，没有截断到64位。owner真实端点从全部2080边绑定读取，要求两个owner恰有一个是p0；总64条owner和1568条far，未借未证明对称只取首owner。

这些是读取实际代码所核对的契约，未在本reader重新计算mask或重新验证旧数据。

## 2. 唯一漏点域没有被MRV强迫覆盖

固定owner mask后余49个端口，要放三条互不交16-mask而留下唯一t。若直接对这49点做普通exact cover，会漏掉“MRV选中的点恰好应为t”的合法选择。

实际代码在每个MRV点枚举全部覆盖它的far边，并在尚未选遗漏点时，额外允许跳过该点一次；没有任何覆盖选项时也保留这一omit分支。若已选三far而此前未omit，自动把最后一个未覆盖位作为t；若已omit，则要求无未覆盖位。因此“漏点早选”与“最后剩点”都覆盖，没有固定t、强迫t来自某个子集或忽略无可覆盖bit。

每条far要求mask完全包含于当前未覆盖域，并检查actual core端点与已用端点互斥；没有把抽象mask存在直接当真实四cut。所有旧sigma far边保持在1568域，未复用只适用于旧k0全四远边的过滤。k1包含owner cut，不能把“三条sigma far＋owner”误当旧全四sigma子域；当前代码没有这种删域。

## 3. a–t及强制匹配没有额外漏解限制

实际packing返回时重新断言四mask互不交、union恰64，补集恰为唯一t。p0在owner mask中，所以t不能是p0。自由owner a也在owner mask中，而三个far cut的owner各在自己的D-mask中，故四mask互斥自动排除了a与其它forced owner的碰撞；t在U外也不可能是这些owner。

代码仍显式检查t≠a及三forced ownerpairs加a–t恰涉及8个不同A label。这个检查不是凭空限制，而是必要mask形状的推论。剩56个A的matching存在性可延拓；当前代码仅保存四个强制pair，没有生成或宣称已经选好了其余28对。

## 4. P2依赖实际core pins，故未使用不安全状态合并

此次读代码前指出过一个实际可能改变结论的问题：端口packing命中但corefail后继续时，若仅以“剩余port mask／层数”缓存失败，不同实际core pin集合可能被合并，漏掉具有不同B2覆盖的完成方案。

实际代码已明确不使用任何failed-state memo。它逐actual owner／far选择保留真实labels；每个packing独立用九个actual pins的支持并做P2，因此没有把某个端口并的core失败挪给另一组实际pins。这里核对的是实现已避免该问题，没有断言不同mask代表一定具有相同core覆盖。

## 5. core条件准确，但仍不是完整586验收

P9是八个cut core端点加p0；全部删除边均在P9内部。任一最短P9到目标的源路线若使用删边，可以从该边后一端重新起步得到更短路，矛盾。因此删除这些边保持的是**到pin集合的最小距离**，并非每个单独pin的距离或R2都不变。实际P2使用九个source闭B2支持的并，符合该引理。

新增A-A matching不能修复新根至core的三步缺口：z先到p0时p0未匹配；先到core pin再经owner和matching，第三步仍落在A。故core支持缺失是真必要反例，不可声称稍后选matching就能补上。代码仅在首packing出现后才允许读取literal一次，直接组合0/1/2旧边生成521个所需pin的core-target支持；这属于已授权的新问题数据，不是源D3或全源BFS复验。本reader没有运行它。

若全部core覆盖，脚本只为585个旧目标保存从新点出发的显式≤3路线，且普通旧腿避开四cut；唯一漏A通过对应core pin–a–t强制matching路线修复。状态明确为 `ALL_NEWROOT_PASS_OLDOLD_UNTESTED`／full graph pending，没有把它升级成全部旧旧D3或完整586图。

## 结论

在所读实际PRED/code中未发现明显的65位截断、固定漏点、错误sigma排重、forced a–t额外删域、core失败状态合并或necessary门冒完整图的问题。这个结论是轻量只读接口检查，不是数值结果、独立packing复算或源图验收。

后续终态仍须分层：端口packing可行、新根到全部旧点可行、完整matching、全部旧旧D3是不同结果。只有完整新根必要域被穷尽且全部失败才可给固定p0/k1原型NO；预算截断必须UNKNOWN。首新根通过也只返回接口给root，不自动继续匹配或制作586图。

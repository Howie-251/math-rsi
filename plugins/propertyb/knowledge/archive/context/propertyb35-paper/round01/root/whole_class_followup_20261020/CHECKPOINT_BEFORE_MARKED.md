# 36纸面研究当前检查点

更新：2026-10-20 13:21 UTC。Goal active，完整 m(5)≥36 未证明；已验收下界34，35完整纸面候选的Lean保持暂停。不运行Lean，不碰v2。

## 当前成果与八类缺口

新规范 `proofs/propertyb35/TWENTYFIVE_FIVE_LOW_EDGE.md` 完整证明：25点／35简单五边／点对覆盖，若有五点全六度的原边，则Property B。解析选边进一步覆盖六度点数 **r≥18**，闭合此前r18–21范围。三低同边的一般充分条件是其余两点D=d(u)+d(v)、α=λuv−1满足D−5α≤12。全部实际H连接、最后Bool染色和局部整数核验已接齐；新范围已获Gemini两轮有效静态审阅，尚未作全36终审。

另 `proofs/propertyb35/TWENTYFIVE_MANY_SIX.md` 完整闭合r=17：有全五低G时接前门；无G时逐低缺陷2迫p8、n2/n3/n4=4/6/19、6全高边，共同高点对低迹互不相交给λ≤13，9名triple型低点中任一W≤24接既有宏星门。root／Sol完整核对，Gemini第三轮有效静态认可这一新范围。故现在r≥17全部有完整纸面证明，无新增局部表。

主要八类仍是：21δ7；22δ6、δ7；23δ6、δ7；24δ6及δ7剩余；25多六度。最后一类已从一般r3…21收紧为 **r3…16，且反例不得有全五低原边**。条件工具增加与整类减少分别报告，不用四个r值折算完成百分比。

## 新共同证明及证据

路径基准B=`context/propertyb35-paper/round01/root/global_reassessment_20261020/three_low_extension/`。

- 共同20点的任意两份五个四块划分，均匀10红10蓝下，两份都同时有全红块和全蓝块的样本数≥400。`B/partition_joint/PROOF.md`包含任意划分→交矩阵→完整19834行排序终态→264行列轨道及精确容斥证明；每个代表/精确计数均保存。
- 第二实现不使用容斥，逐代表直接判定全部184756个红集；独立生成不采用doublelex筛，全部19834终态均规范到同一264代表。`B/partition_joint/independent/REPORT.md`与COMPARISON.json全部PASS。root完整读两份源码并重新编译、完整运行独立实现，`root_replay/ROOT_REPLAY.json`再次逐项一致。
- 实际三低同边补色：三中心各五块冲突16980/N，余19原边按固定u/v分类，减一对交400后总失败≤[160650+2002(D−5α)]/N。全五低G给184674<184756，余82；无冲突时补中心色，G由u/v反色保证。
- r≥20由总低关联与低点对计数选全五低边；r19若无全低边则每个入射边有4低，4n4=114不可能；r18则每低恰一次3低边五次4低边，n3=6而4n4=90不可能。两条整除证明已root与Sol分别核对，不增加枚举。
- `B/ROOT_ACCEPTANCE.md`记录root实际核对与重放。规范证明与条件工具集第六组已同步；本局部完整域不是原超图枚举，未新增Lean。

## 整体效率判断与已停止路线

用户问是否最高效：不能保证，也不能否认此前在局部分支花费偏多。此次具体改为先固定能闭合的实际输入，再证明共同门：r21九种设计参数细分已停止，由上述共同染色论证接管r18–21，再复用旧宏星引理覆盖r17。

`B/TRANSFER_TRIAGE.md`表明不能把20点两划分直接迁到22–24：总缺陷4d−n+1造成重复点/再碰G及中心耦合，24δ7还无六度中心。当前不扩新的19/18/17点矩阵域；只有找到能覆盖实际完整分支的新入口才重试。下一步回到24δ7的critical低边共同修复与25无全五低边的共同结构，不继续证明无明确caller的小门。

以下有用条件结果保留，但不再扩失败域：

- `proofs/propertyb35/TWENTYFIVE_MACRO_STAR_COLORING.md`：W≤25门及Grok新精确费用恒等式；普遍存在合格中心仍未证。`TWENTYFIVE_LINEAR_LOW_EDGES.md`证明低点所在边族F线性且r≥11则可染、含实际30边pair-cover子图且r≥6则可染；F线性不是自动条件。其r18无30子设计反例保存于many_low_design/，不是Property B反例。
- `pairing_nineteen/PROOF.md`：十九命中加实际相容剩余对的门；匹配权≥7不等于命中≥19，旧控制H全部182250个最大权匹配均≤18命中，最大权优先策略已停止。
- `pairing_nineteen/EQUALITY_COMPATIBILITY.md`：16个坏事件划分的Fourier约束、变支持实际局部例及端点翻转预算均已核，但没有完成普遍十九匹配选择/相容保证；不继续造划分例或同类交换。
- 原三划分界、zero-private紧面及其他共用工具见 `research-wiki/PROPERTY_B_CONDITIONAL_TOOLKIT_36.md`。22/23旧moment域和固定cube攻击已停止，旧完整记录在本目录归档检查点，不重复扫描。

## 在途审阅与恢复

1. Grok线程 `f0335392-19cb-4010-bad2-abaca29dd7fc` 的宏星讨论cell1225已完成有效end_turn（4.7-build/xhigh）。其精确费用及条件flat结论已核并保存 `global_reassessment_20261020/GROK_MACRO_RECONCILIATION.md`；不把建议的普遍W选择写成已证。
2. 旧两划分解析讨论cell1251已主动终止，无有效成稿，不再等待。停止原因是完整有限引理及实际H调用已完成，继续追纯解析最优性不再阻塞证明；见B下 `GROK_JOINT_PARTITION_CANCELLED.md`。新Grok完整r≥17连接审阅 **functions cell1261** 在途，fresh、grok-4.7/xhigh、至多8回合；提示／回应为B下 `GROK_R17_PLUS_PROMPT.md`／`GROK_R17_PLUS_RESPONSE.json`。待实际返回对账，不能预记认可。
3. Gemini十九匹配fresh调用cell1245已结束ERROR，无数学意见；原始响应 `pairing_nineteen/GEMINI_SELECTION_RESPONSE.json`，线程33fe9a3f-2c67-4c76-aae7-a6af9b6cc00c。不是认可，不继续等待该cell。
4. 全五低边新Gemini线程 `0a3f3f2a-c0ea-444b-bb32-1e1077bcf205` 的cell1257／1259／1262均有效SUCCESS（CLI gemini-4-argon-high/high）。三份回应依次为B下 `GEMINI_FIVE_LOW_RESPONSE.json`／`GEMINI_R18_R19_RESPONSE.json`／`GEMINI_R17_RESPONSE.json`，处置 `GEMINI_RECONCILIATION.md`。覆盖三低门、五低G、r≥18选边及r17宏星实际连接；没有执行程序，有限算术与旧宏星门按声明进口。不是全25或全36审阅。
5. 当前Sol数学/算术任务已交付；规范wiki实验节点已完成；本次新增r17与原r18节点分开。下一轮按上述明确实际缺口派发，避免空转或重复证明。

旧12:06检查点完整保存在 `global_reassessment_20261020/CHECKPOINT_BEFORE_FIVE_LOW_EDGE.md`。Goal状态不变，不重开旧题或旧Lean。

# 四大正集／三负二门及I1三三迹的独立核查

review_independence: same-family；acceptance_status: provisional。

## 结论

独立逐分支核对root给出的证明，未发现数学缺口；没有集合域或原H搜索。规范全文已写：

* [FOUR_LARGE_POSITIVE_THREE_NEGATIVE_PAIRS_REPAIR.md](../../../../../../proofs/propertyb35/FOUR_LARGE_POSITIVE_THREE_NEGATIVE_PAIRS_REPAIR.md)；
* [TWENTYFOUR_SEVEN_HIGH_ONE_INTERNAL_THREE_TRIPLES.md](../../../../../../proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_ONE_INTERNAL_THREE_TRIPLES.md)。

初次核查的新增整库存范围为I1 \((n_2,n_3,n_4)=(11,3,0)\)。无四迹、\(r=0,1,2\) 已有旧证明，此处提供同一短度数矛盾，不另记新闭合。随后独立核准的 \(r=4\) 升级见末节，不声称 \(r\ge5\)。

## 关键核查

1. “至多四”没有用复制正集实现：正数至多二先禁至多三个负二目标，正四仍非空；三正有交点取安全红对，三正不交64候选的堵界至多34。四正不交的容量按原负二／三／四索引共同收费，堵界至多168。
2. \(q_x\) 始终是原负二索引数，F才是不同邻点集合；重复索引既不去掉发生预算，也不擅自要求三个不同邻点。固定x时的有效堵界是 \((3-q_x)+(5-q_x)\)。
3. \(q_x=2\) 的全堵必须四候选等号，迫F恰两点并包含于U、V，且第三个负二必须活跃并避F。改x蓝、f红时，这唯一剩余负二避f；九候选仅被它和至多四个含f负三堵。旧xf索引虽已安全，仍占用f的一次原负容量。
4. \(q_x=3\) 的候选数至多二时，至少五个F关联迫两个共同F点。换x蓝后所有负二都安全；选择共同f击中U、V，余两三集给九候选，对至多四个含f负三。没有把低候选数解释成自动成功。
5. 实际q-cut中全部单色风险均有完整原边约束：正为q单迹外四集；missed三迹为负二，红二迹为负三，红单迹为负四。唯一内部C已双色，无四迹所以没有负单。每外点signed总次数由其原七度支配。
6. 若某q有 \(h_q+s_q\ge3\)，则正数至多四，负二至多r≤3，新门适用。否则所有C点同时满足 \(h_q+s_q\le2\)，两点D只用非负单迹容量，合得J总度上界 \(26-3r\)，小于真实 \(34-4r\)。\(r=3\) 给17对22，不依赖PL加强或不同q之间拼接。

CHECK.py只枚举q_x、F大小和两组删除关联的小整数，核两个救援尾型的必要大小条件、共同容量标量以及四个r值的源迹恒等式。它不验证或枚举一般signed集合族；一般定理由规范解析证明承担。

复现：

    python3 context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/three_negative_pairs/CHECK.py

实际输出在CHECK.json。没有修改旧规范、导航或wiki，没有Lean、MCP或跨家族审阅声明。Grok等指定审阅由root另行办理。

## 后续短升级：无D的三正四负二门及r4

独立核查root提出的三正门，未发现缺口。准确范围为至多三个正集各至少四元、至多四负二、至多35负三、任意数量更大负集，没有D或底集限制。

正数至多二时直接用交点或16红对，未采用“禁四点而仍假设正四非空”的错误办法。恰三正有交点z时，红对全堵迫第三组恰四元、全部负二恰是不同的四边星；改z蓝后，剩余正大小至少3、3、4，交叠可用两红，不交36三红严格超过35。原三正不交64候选总堵至多51。新规范完整写在 [THREE_LARGE_POSITIVE_FOUR_NEGATIVE_PAIRS_REPAIR.md](../../../../../../proofs/propertyb35/THREE_LARGE_POSITIVE_FOUR_NEGATIVE_PAIRS_REPAIR.md)。

实际r4的q-cut逐索引分类未变，成功门槛分别为h≥3、h2s≥1、h1s≥2和h0s≥4；末者正数至多三、负二四、负三至多五，准确满足新门。否则C频率h≤2且总和至少四，C上的J总度至多 \(15-2H_C+x_2\)，D总度至多 \(4+H_C\)，合计至多 \(19-H_C+x_2\le17\)，矛盾于原J总度18。此处没有使用其他q的门参数或把s上界加在错误的点上。

已把完整r4证明追加到原 THREE_TRIPLES 规范第4节，前三节主证明保留。新增整库存为 \((9,4,0)\)，全稿现统一覆盖r≤4。CHECK_R4.py实际执行PASS：逐一核五点0/1/2频率总和≥4的192个标签标量，最大J度上界17、最小矛盾余量一；结果在CHECK_R4.json。只作小标量检查，不生成任何P源或外点集合域。审阅独立性仍为same-family/provisional，未增加跨家族接受声明。

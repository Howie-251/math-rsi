# ActualConder1250：从旧失败目标冻结三cut＋repair接口

本readgate没有读取source邻接、BFS、solver、候选图或旧验证。实际旧合法源、单细分全NO与5614 two-cut全NO直接继承；本地canonicalConder节点及指定目录未定位真正三disjointcuts＋跨cut原非边repair的既有终态，不声称全历史或文献无人做过。

已将全部5614个FROZEN对象与B_CASES按id绑定。saved first_bad_target有58种；top为1054:583、1178:575、1055:482、1056:444、1179:389、1057:341、1058:303。完整直方图在READ_GATE.json。这是每对象首个未覆盖target的分布，不能当全部坏对或完整缺集。

按root的可解释选择：旧A单细分已知缺1178，因此选secondedge含1178且x-pins恰{0,1178}的lex首对象，而非按totalbadscore选。实际为 **object4536，second_edge_id1515，[869,1178]；x-pins[0,1178]，y-pins[1,869]**。它修好了旧A缺点的直接邻接，但旧B新x仍有saved首缺 **t=1058，R10外、distance下界11**；没有exactB全径或该pair的完整旧最短路数据。

冻结这个J，保x–1178，只允许移p∈{0,1,869}。第三源边g–h避开{0,1,869,1178}，删helper–p和g–h，加helper–g与p–h，后者须原source非边。每helper始终两oldpins＋互边，1252/1878全cubic。此域不是全部三cut族。

缓存旧对象已包含全部1875个源edge元数据；无需sourceparse即定位t的三个incident edge：id1310 [725,1058]、1597 [933,1058]、1709 [1010,1058]。pilot固定g=t、h为这三个邻点，配三可移p，预测9个合法对象。其savedt修复是具体的：移p0给x–t直边；移p1或869给y–t直边、x–y–t两步。旧x–1178保持1，y到1178≤2。它不保证其余新根覆盖，更不保证旧旧D10。

savedB x到t>10还说明这些t邻点不在原四pins中，且与任一可移pin p没有原source边，否则旧J已有≤4步到t，矛盾。这是pilot合法性的纸面依据，数值批仍会按actual source literal确认。

有限域数预测为1865条thirdedges、11178个合法transfer、pilot9：4pins内部仅两旧cut，incident edge共10；每可移p的两余邻点各给2个禁orientation。readgate从缓存edges得到1865，但不把预测替代后续literal核对。新数据缺口是actual modified graph的两helperR10与旧旧点对，不是重复sourceD10。

READ_GATE.json保完整join、三个可选旧base、frozenid/targets与费用。read聚合actual0.029389544＋保守prep0.5＝0.529389544/5CPU。root随后已授权同case20CPU一次pilot＋全frozenfamily批，普通source一次inputparse不做sourceD10验证。

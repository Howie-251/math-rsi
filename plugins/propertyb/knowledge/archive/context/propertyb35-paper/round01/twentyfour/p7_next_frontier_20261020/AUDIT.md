# I1四四迹与新四正门的独立接口核查

review_independence: same-family；acceptance_status: provisional。

## 结论与实际范围

独立阅读 NEXT_MERGE_DIAGNOSIS.md 和 CHECK_NEXT_MERGE.py，逐项重推新修复门、PL容量、四频率型、三顶点J整数尾型与原染色接口，未发现数学缺口。已实际运行原CHECK，输出PASS：14个排序组大小型、最小余量 \(3/2\)、四频率型、三个J型；结果文件实际名是 NEXT_MERGE_SCALARS.json，不是 CHECK_NEXT_MERGE.json。

本次可以新增的完整纸面范围是：24点35边／点对覆盖／P7全八与L17全七／无全七边／恰一内部边／非内部四条四迹、无三迹，即 \(I1,(n_2,n_3,n_4)=(5,0,4)\)。不据此声称其他库存、整个24点或全目标完成。指定跨家族审阅由root另行进行，本文不记其尚未返回的结果。

## 独立核查要点

* 新四正门保留“正二至多三个”，四个全二正集未被误纳入。交叠难型迫出四个不同 \(\{x,u_i,v_j\}\)，耗尽负三；禁x后至多一个正单。无单集调用五小正零T，所得修复缩成至多四点，所以负五及以上不影响；有单集时至少八个四红对至多六个含z负四。两个分支的原索引容量均不返还。
* 四正不交时只计算真正活跃的负三／四，按同一批点容量 \(3u+4v\le6S\) 收费，不把两类预算分别重复使用。独立遍历80个有序大小型，最小余量仍为 \(3/2\)。
* q-cut禁两点后出现四个正二，必迫四条原边都含q,f,g；外七度f的共度盈余只有五，两伙伴却已耗六，严格矛盾。禁点时负约束整份删去，不把负集取差。
* 对D点，外点对覆盖直接给 \(17\le4u+3s+h=32-3h-s\)，而不是假设PL恰覆盖一次；因此 \(s\le\min(8-h,15-3h)\) 为安全必要上界。
* 四条四迹对C的频率和至少八。五点每频率至多二的全部可能排序恰四型，不假设四迹互异。尾型中J的支持只剩三点，两个未覆盖P点对迫a,b≥1；联立五边与两度上界恰得三个整数解。
* 所有纯蓝对参数由同一Q计算。恰八行才用L17的exact8门；其他行用“至多七”35B扩展，没有padding。尾型准确给六正总数、正三2或3、负三零，可用九正门附录B第2节的独立六混合门；该辅助门没有九正或L18前提。
* 唯一内部C、四迹、五条二迹和25条单迹逐类覆盖全部35条原边。所有尚未proper边仅一个符号，故外点D7是真实原度支配；没有零P边未计入，因无全七边已保证P击中每条原边。

没有重新审计原稿所有“此前已闭库存”的底层证明；其54库存差集只被当作整数记账，未用它证明本次新库存。规范正文自身不依赖这份旧闭合列表。

## 产物与复现

新规范：

* [FOUR_MIXED_POSITIVE_FOUR_TRIPLES_REPAIR.md](../../../../../proofs/propertyb35/FOUR_MIXED_POSITIVE_FOUR_TRIPLES_REPAIR.md)完整内联新一般门和q星正二上限。
* [TWENTYFOUR_SEVEN_HIGH_ONE_INTERNAL_FOUR_QUADS.md](../../../../../proofs/propertyb35/TWENTYFOUR_SEVEN_HIGH_ONE_INTERNAL_FOUR_QUADS.md)完整内联实际选择、计数、四型处理和原染色返回。

原CHECK已实际执行；另有独立 AUDIT_CHECK.py，不导入原CHECK或其结果，采用80个有序大小型、独立频率集合／三顶点J集合和完整蓝对参数逐行检查，保存 AUDIT_CHECK.json。二者只算小整数／Fraction，不生成H、自由外点布局或一般P源。

复现命令：

    python3 context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/CHECK_NEXT_MERGE.py
    python3 context/propertyb35-paper/round01/twentyfour/p7_next_frontier_20261020/AUDIT_CHECK.py

没有修改旧规范、导航或wiki，没有Lean或MCP调用。

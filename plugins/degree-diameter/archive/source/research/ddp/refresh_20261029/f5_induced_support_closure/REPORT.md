# 支持层H被反驳：最大proper闭支持19点

固定字面30点controller及已存258个有序distance3唯一词，只处理30个fiber是否非空的布尔支持，不处理各fiber内的具体保留点。目标n≥1921必须支持至少16个fiber，因为每fiber至多125点。

事前预测H“所有proper闭支持至多15点”被反驳。完整NextClosure枚举得到24575个闭支持；最大proper支持恰19点。达到16点以上的proper支持只有6个：3个size16、3个size19，size17/18及20至29均无。

一个19点支持为

    {1,3,5,6,7,11,12,13,15,16,17,20,21,22,23,24,26,27,28}。

全部6个literal支持及补集在`LARGE_PROPER_SUPPORTS.json`，每个均逐条直接核过原258规则。

这仅说明不能凭这258条必要规则无损强制全部30fiber非空；没有得到真正的D3诱导图，也没有证明这些proper支持中任何一个可装入1921个合法保留点。一般partial-fiber问题仍开放。

## 输入、旧范围与实际成本

输入仅`f5_induced_retention_closure/CONTROLLER_UNIQUE_WORDS.json`。每词u-a-b-v给出(u∧v)⇒(a∧b)，原258有序词去掉反向重复后是129条不同双结论Horn规则。定向检查旧同源报告/ledger未见支持层闭集完成枚举；既有300k-variable保留模型、transversal删除和fiber商不是本层问题，均未重跑。

枚举native CPU0.05702秒，含编译/driver1.205346187秒，低于5秒预算；随后仅从已存mask文件提取六个大支持，成本另存结果。source边表读取0、图BFS0、solver0、图生成0。`CLOSED_SUPPORTS.u32le.bin`保存按枚举次序的全部24575个30-bit masks。

## 枚举完备性

闭包cl(S)通过反复加入已被两个端点触发的中间点，直到不再变化。它是扩张、单调、幂等的definite-Horn闭包。

从cl(empty)=empty开始，对当前闭集A，按i=29,…,0尝试尚不在A的i，令

    B_i=cl((A∩{0,…,i−1})∪{i})。

当B_i在i之前的前缀与A完全相同时，取第一个这样的B_i为下个闭集。这是代码中的NextClosure。

完备性可直接证明：设B为lectic序中A的真正后继，i为二者第一个不同位置。则种子A的i前缀加i属于B，故B_i⊆B；它与A有同一低位前缀且包含i，因此可接受，并严格大于A。任何可接受的更大j都会给出介于A与B之间的闭集，违背B的后继性。因此算法所取必为B，不会漏集或重复。到达full30即完整结束。每个输出又经闭包产生，故所有且仅有闭支持被枚举。

所以本次不是raw solver UNSAT结论，而是已完成的有限闭集枚举；最大19的反例本身另有无需枚举完备性的258规则直接检查。

## 可以带回保留模型的内容

若仅使用本Horn系统，n≥1921的支持只能是full30或这6个proper支持之一。可以作精确case split；不能把6个必要支持当成可行图，也不能只因whole-fiber版本失败就删掉所有partial-fiber分支。

whole-fiber版本的严格排除另见`WHOLE_FIBER_PROOF.md`。新external-edge五路共中点闭包另见`MULTIROUTE_LEMMA.md`；本次只纸面核查，没有修改或求解大保留模型。

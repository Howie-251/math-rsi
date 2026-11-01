# 旧T34局部导入：21点有六度以下点即染色；35边原H遂全部edge-critical

## 核查结论

**局部导入成立。** 任21点、至多34条互异五元边的H，若存在点x满足d_H(x)≤6，则H有Property B。这里不以完整T34／≤34全域作为黑箱，也不恢复旧35 Goal。以下只读取了现存源码、裸原题audit和已保存成功日志；本轮没有运行Lean或重新构建。

进一步，任21点35条互异五元边、非B且存在d_H(x)≤6的原H，删去任意原边F后都可染。因此H本身edge-critical，无需改取可能丢失原度谱的极小子族。每原边至少有五个不同的singleton-intersection邻居，故它的非1交图Γ每点度至多29。若另引用新通用minΓ3门，则同一原H满足

    3≤q_Γ(F)≤29  对所有原边F。                      (1)

该结论适用于A2／A3，也不限于它们；不直接给H本身可染。

## 1. 现存裸声明与成功记录

### 1.1 21点度五：没有其余最小度或剩余Goal前提

[TwentyOneFive.lean](../../../../../formal/Aris4Math/ThirtyFour/TwentyOneFive.lean)的实际导出为

    Aris4Math.ThirtyFour.TwentyOneFive.propertyB_of_degree_five
      (H : Simple5Hypergraph (Fin 21))
      (cover : H.PairCovering) (size : H.edges.card=34)
      (x : Fin 21) (dx : H.degree x=5) : PropertyB H。

其开头的`noB`局部变量在最终`omit noB in`处移出定理前提；不是向caller索要非B假设或待证分类。证明内部处理其他≤6点，以及七度点数0／1／2／≥3全部情况。

[FiveAudit.lean](../../../../propertyb34/round01/twentyone-lean/FiveAudit.lean)的`T34TwentyOneFiveAudit.original_branch`从裸Finset五元边集、34边、paircover与所选degree5直接给Bool染色，没有`Assembly.RemainingGoal`前提。该文件另一个名为`conditional_original`的定理有剩余Goal前提，**本导入不使用它**。

已存[five-audit.log](../../../../propertyb34/round01/twentyone-lean/five-audit.log)打印上述裸声明与原题wrapper，二者传递公理仅`propext, Classical.choice, Quot.sound`。[build-five-assembly.log](../../../../propertyb34/round01/twentyone-lean/build-five-assembly.log)明确`Build completed successfully (1068 jobs)`，并显示该定理及Assembly等价定理的标准三公理。

### 1.2 21点度六：确需全局最小度至少六，但可真实补齐

[TwentyOneSix.lean](../../../../../formal/Aris4Math/ThirtyFour/TwentyOneSix.lean)实际导出为

    Aris4Math.ThirtyFour.TwentyOneSix.propertyB_of_degree_six
      (H : Simple5Hypergraph (Fin 21))
      (cover : H.PairCovering) (size : H.edges.card=34)
      (minimum : ∀v,6≤H.degree v)
      (x : Fin 21) (dx : H.degree x=6) : PropertyB H。

该定理不是仅仅“指定点六度”就直接调用；缺的minimum将在第3节以先排任何degree5点补齐。源码内部完整分流二个六度点、唯一六度下七度点数0／1／2／≥3，不含未证局部容量表参数。

[SixAudit.lean](../../../../propertyb34/round01/twentyone-lean/SixAudit.lean)的`T34TwentyOneSixAudit.original_branch`把同样minimum及degree6条件从裸边集接到Bool染色，无剩余Goal。独立[six-audit.log](../../../../propertyb34/round01/twentyone-lean/six-audit.log)打印完整裸声明，两个branch声明的公理仅标准三项。[build-six-assembly.log](../../../../propertyb34/round01/twentyone-lean/build-six-assembly.log)明确`Build completed successfully (1153 jobs)`，含最终TwentyOneSix模块及其公理记录。

当前[Assembly.lean](../../../../../formal/Aris4Math/ThirtyFour/Assembly.lean)亦在实际反向装配中先调用Five，再以无degree5推出minimum6，随后调用Six。其21点剩余只在minimum7下；不能因为Assembly本身是等价式就把全部Target34当已证。

### 1.3 ≤20点局部结论与merge

- [SmallVertices.propertyB_of_vertices_le_eighteen](../../../../../formal/Aris4Math/ThirtyFour/SmallVertices.lean)对任意v≤18和≤34边直接给PropertyB，无cover前提。
- [nineteen_propertyB](../../../../../formal/Aris4Math/ThirtyFour/Nineteen.lean)对19点、cover、≤34边给PropertyB；exact34版本为`nineteen_propertyB_of_eq`。
- [twenty_propertyB](../../../../../formal/Aris4Math/ThirtyFour/Twenty.lean)对20点、cover、exact34边直接给PropertyB，内部全部点度分支已处理，不含剩余Goal。[TwentyAudit.lean](../../../../propertyb34/round01/twenty-lean/TwentyAudit.lean)的`original_coloring`和`original_two_colors`是裸边集wrapper。[twenty-audit.log](../../../../propertyb34/round01/twenty-lean/twenty-audit.log)打印原声明及标准三公理；[build-twenty-complete.log](../../../../propertyb34/round01/twenty-lean/build-twenty-complete.log)明确1045 jobs成功。
- [通用Reduction.lean](../../../../../formal/Aris4Math/Reduction.lean)的`merge`、`merge_edge_count_le`、`propertyB_of_merge`、`smaller_counterexample_of_uncovered_pair`已证明：未共边点对可合并，原每条边上该映射仍单射所以仍五元，去重不增边数，合并后的proper染色可拉回原H。无需保持某个指定点的原度数。
- 已验收[ThirtyThree.Main](../../../../../formal/Aris4Math/ThirtyThree/Main.lean)的`propertyB_of_at_most_thirty_three`只用于边数≤33的已证下界；不混用未完成Target34。

从这些局部定理可独立重组：任≤20点、≤34边都可染。若有反例，在这些点数内取顶点数最少者；未覆盖点对可merge成更小反例，故它cover。≤18由SmallVertices排，19由nineteen排，20且34边由twenty排；若边数≤33先由已验T33排。整个论证不经过未闭21δ7或22…25分支。

## 2. 21点非paircover不能偷偷保留指定点度

若21点H不cover，选一个未共边点对合并，得到≤20点、至多34边简单五元图H'；由上一节局部结论H'可染，再拉回H即可。这个分流只用≤20的完整局部结果，**完全不要求合并保留低点x及其度数**。因此不存在把新合并顶点错误当原六度点的范围偷换。

## 3. 完整局部导入的纸面证明

现设21点、≤34边且有d(x)≤6。若边数≤33，已验T33即染；只需exact34。非cover时用第2节。cover时，每点v与其余20点都共边，故4d(v)≥20，所有点度≥5。

若存在任一degree5点y，直接调用Five（不要求其余点minimum6）。否则所有点度≥6。给定x≤6遂恰degree6，minimum6真实成立，调用Six。这穷尽全部情况，证明所述21点局部定理。

## 4. 35边原对象edge-critical及逐原边singleton下界

设H为21点35边simple5、非B，并有原点x度≤6。对每条原边F，H−F仍是21点34边simple5，且

    d_{H−F}(x)=d_H(x)−1_{x∈F}≤6。

第3节直接给H−F proper，无需H−F保留cover或原度谱。因此原H的**每一条**边删去都proper；没有另选边极小子族。

固定F及proper(H−F)染色。因为原H非B，F必单色。对每个v∈F，单独翻v后原F变proper；若H−F仍全proper，就已染H而矛盾。因此存在f_v∈H−F翻前proper、翻后单色。其变坏必因翻v，所以v∈f_v，且翻前f_v除v外的其余四点均为v的反色。F中其他点与v原来同色，故

    f_v∩F={v}。

不同v的f_v不能是同一条边，因为其与F的精确交集不同。于是F至少五个不同singleton邻居。35条原边的其他34节点中，Γ度q(F)=34−singletondeg(F)≤29。该推理对每个F独立选proper(H−F)即可，不要求不同F共享同一初态。结合新21／22点无条件[Γ最小度三定理](../../../../../proofs/propertyb35/TWENTYONE_TWENTYTWO_MINIMUM_NONUNIT_DEGREE_THREE.md)，即得(1)。

以上仅新增一个从原H到已验旧局部结论的严格导入与必要结构；未运行Lean，未恢复35 Goal，不宣称全T34或当前36完成。

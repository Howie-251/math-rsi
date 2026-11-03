# 15552源／16389目标：成本pilot终态，代表真Walk通过

**本批按原180CPU授权自然停止，无活动进程。** 已完成9个新module，
累计约112.392507115 CPU，含所有已记录准备、三次失败、编译和小表绑定。
完整source-controller0行、全部sourceD4及clone16389原始FinalClaim均未闭，
不加Lean计数。Source15552是公开复现，不作为新图或额外Lean成果。

## 实际已闭合范围

`F3Graph15552Definitions`提供真正Fin15552图及source identitylabel，
实际192×F3^4、960controller entries、五张4×4B／direction／constant，
以及Fin15552⊕Fin837 clone、Fin16389显式label和两原FinalClaim定义。
图只在不同完整global labels间给边，actualholding不能当source edge。
`constant_zero`、controller逆type等有限事实与encode/decode81互逆已kernel通过。
原degree<=15/sourceD4/nonD3和cloneFinalClaim仅typed，未伪称定理。

`F3Graph15552Linear`实际kernel通过一般带offset的affine_coset_solve，以及
本源zero-c operationalroute的线性分解、coset求解和inversebasis求解。
`F3Graph15552Routes`每步明确分成holding equality或真正source edge：
holding对应nil Walk，随后append；因此completedroute的Walk长度不增。
这没有套旧1920/C60无loop forward_adj。有限证明针对实际operationalroute，
不是把外部M/N数字或JSON的PASS当成Lean命题。

无用户证书前提的两个具体定理及独立importAudit实际通过：

* `DegreeDiameter.Portfolio.F3Graph15552.PilotLargestGroup.all_walk_bound`：
  所有x,y:Fin81，源controller0到0，存在真正graph.Walk，length<=4。
  25个contributingword、100个column-vector等式、81个cover-vector等式，
  加actualcontroller endpoints和length界，全部kernel闭合。
* `DegreeDiameter.Portfolio.F3Graph15552.PilotFullrank.all_walk_bound`：
  所有x,y:Fin81，源controller0到33，存在真正Walk，length<=4。
  actualword[0,1,0,1]，四个inverse-noise basis等式和endpoint已kernel闭合。

成功日志`F3Graph15552PilotAudit_attempt001.log`实际打印types/bodies/axioms，
仅propext、Classical.choice、Quot.sound。Prettyprinter省略了可推断的Exists
binder类型，但成功的PilotWalks源码显式写的是`graph.Walk`，不是布尔proxy。
旧及新PASS module均未重编。失败elaboration日志自动出现的sorryAx不属于
任何接受定理；源代码没有sorry/native_decide或新增公理。

## 完整row0尝试与真实停止原因

代表节点完成时累计约73.306CPU。根据当时实际Cert9.435198CPU、import2.244769
及Definitions20.999874CPU的成本模型，完整row0中心预测174.652CPU，故继续原预算。
其新增Row0Data PASS6.996718CPU，Row0FullrankCertificate PASS31.971870CPU。
这已核闭另外172个sharedfullrank word的688个basis-vector等式及172个
source0controller endpoints；连原pilot共173个不同word的逆噪声basis证书。
这些basis事实与sourcecontroller无关，未来可全局复用。

但row0余下18个coset组、完整row0Walk caller和独立Row0Audit没有编译。
新实耗后，剩余8837 vector-route steps、339 controllerlookup和四次import，
沿最乐观旧单位成本累计仍约180.991CPU，
用刚测fullrank单位成本约198.558CPU，
两者还未含1458个choice-group索引检查。均超过180，故未继续launch未PASS
Column/Cover/RowWalk/Audit，也未机械耗尽余额或重置timer。它们的新源码和数据
保留为未编历史，不冒完整row0定理。所有attempt/log/CPU均在FINAL/CHECKPOINT。

三次失败均保留：Definitions函数应用空格语法21.085587CPU；Linear的Vec-SMul
通用simp未匹配5.211375CPU，改pointwise ring；Routes的free-variable Walk.length
不能直接decide2.543071CPU，改显式Nat长度后omega。各修复只作用未PASS新module，
随后通过。最高单module为31.971870CPU，小于60硬限。

## 小表与物理输入绑定

EXTERNAL_BINDING_PREPARATION_RESULT.json实际比较新Definitions中的960controller
entries、80matrix codes、20direction codes、20constant codes与已完成的actual
旧affine recovery表，并逐j核837条独立orderedrole表的center/newlabel公式。
新j=27*i+localindex，oldcenter=81*I[i]+j%3+9*(j//3%3)+27*(j//9%3)，
newlabel=15552+j，W坐标x1=0。每条freshfullN绑定和oldcenter排除收据都存在。
没有重读大graph、重新BFS、旧field/rank或solver。这里只给typedrecipe的外部
small-input桥，不声称Lean解析ASCII边表或kernel枚举了837条原文件邻域。
旧root/frozen/expert/source17文件均未修改，fresh16389验收是独立预算的数学事实。

## 用root新对称性改变下一完整kernel方案

本pilot终态不因新数学而自动续编。Root独立已保存实际port-preserving
controller置换与`SYMMETRY_REDUCED_KERNEL_SCOPE.json`，8个orbits代表
[0,1,2,3,9,10,16,35]，每orbit24层。两generator的全部p通勤可提升为fiber
不变的source automorphism：矩阵只依赖全局typep，bijection保持global equality，
所以sourceholding删除语义也保留。完整代表行对targetpullback后mapWalk即可覆盖
其orbit；不需证明枚举了全部centralizer。本批未重新分析或kernel证明此对称性。

因此新完整工作量应是shared证书和8row，不是重做192row：

* 8×192=1536controllerpairs，其中1384fullrank、152coset。
* 所需distinctfullrank恰173，已经全部PASS；不要重新编译任何basis数据或proof。
  可用一个小sum/option索引池组合pilot word和Row0Fullrank172，纯cases引用已闭证书。
* 新增仅90个coset组：2160 column-vector＋7290 cover-vector等式，共9450；
  group0通过，沿用现有符号coset和holding-Walk桥。建议按4—6组分module并采用
  小型/分块Nat编码lookup，避免一个90×81线性Vec重复reduce；每module仍<=60CPU。
* 1536小controller endpoint/ref/group绑定；2×960 generator通勤、两置换逆表
  和192positive(startrep,groupword)覆盖，wordlength<=5；泛型composition/inverse
  和mapWalk。无需24×960通勤或重新atomicfield/rank。
* Source inverse-type矩阵小身份给degree<=15、root已提供controller0→1的
  length<=3排除给nonD3，另源无isolates。接SourceExact/独立Audit，均须原始
  无用户证书目标和std3。源公开复现不加实例。
* 然后才以31×5目标owner＋五个plane/kernel小左逆身份闭clone load<=1，
  复用FullNeighborhoodClones atD4/非D3retraction和显式Fin16389 label；
  原cloneFinalClaim/实际独立Audit/小表binding齐才可能Lean+1。

据本pilot的真实数值节点，建议**未来完整source+clone累计上限1200CPU，必须
包含本pilot约112.4CPU**；单worker/单module60，所有失败与准备继续同账。
粗略中心总量750—1000CPU，而非实际收据：90组有限证明及数据约400—600，
小controller/symmetry绑定约100—200，degree/lower/aggregation/Audits与cloneowner
约80—150，已有pilot包含在总数。主要不确定性是新group打包和controllerlookup
的真实kernel成本；先做4—6共享组及两generator节点再更新预测。1200是建议，
并非已授权新timer。若root采用另一明确budget，保留所有PASS import并据新实耗
checkpoint。当前不启动任何fullqueue，不再做D3参数/复制倍数研究，也不新增图。

# 24／25点成稿说明（编辑与审计资料，不进入读者正文）

正文：`CHAPTER_24_25.md`。只重组既有候选数学，未启动 Lean、分类搜索、模型调用或原始 Goal。所有小数值摘要为读取已有 JSON 后用 Fraction 聚合，不冒充重新运行原分类或独立概率复算。

## 内容覆盖

24点已展开全部 r=0、1–4、5、6、≥7：原来的 `CANDIDATE_TWENTYFOUR_COMPLETE.md` 只详细覆盖 1–4、其余是链接，本稿将这些依赖展开。包含六低三高共同限制的三个解析矛盾，七低14型及两份剩型混合，五低两种低匹配、单位低/非单位高、最终全单位九锁引理。

25点已展开实际九锁选择、六→七→八→九的块分解完备性、三个带度数域、q8的两个真实第十高点域、q9的六个新度扩张域，以及一般九锁引理的孤点填充和不依赖全局点对覆盖的link配额。明确全部直接及扩张最大界。

正文先用后证的唯一交叉为24点五低末支调用25点章节末的九锁条件引理，已明确指向“下一节”，不存在循环：九锁引理只依赖q5局部表及一般概率式，不依赖24点结果或25点点对覆盖定理。

## 源文与证据范围

完整读取的数学源：

* `context/propertyb34-hour1-20261013/high-math/CANDIDATE_NO_SIX.md`
* 同目录 `CANDIDATE_MANY_LOW.md`
* `context/propertyb34/round01/high-math/CANDIDATE_TWENTYFOUR_COMPLETE.md`
* 同目录 `CANDIDATE_FIVE_LOW_FULL.md`、`CANDIDATE_FIVE_LOW_NONUNIT.md`
* 同目录 `CANDIDATE_SIX_LOW.md`、`CANDIDATE_SEVEN_LOW.md`
* 同目录 `CANDIDATE_EIGHT_SEVEN_MATCHING.md`
* 同目录 `CANDIDATE_TWENTYFIVE.md`、`CANDIDATE_25_MANY_LOW.md`、`NINE_LOCK_UNIVERSAL_LEMMA.md`

读取结果并提取精确最大界的JSON：

* `SEVEN_HOMOGENEOUS_MATCHING_BOUNDS.json`：15619直接严格，最大19447/19448。
* `EIGHTH_LOW_COMPLETE_BOUNDS.json`：220直接严格，最大1285/1287。
* `EIGHTH_MATCHING_Q0.json`：881直接严格，最大1961/2002。
* `SEVEN_MATCHING_QMAX0_JOINT.json`：3严格，最大12148754961/12155000000。
* `SIX_EXTENSION_JOINT.json`：17严格，最大24291226829/24309997569。
* `SIX_LOW_EXTENSION.json`：17有标签直接严格记录，最大12143/12155。
* `SIX_LOW_TWO_HIGH.json`：94直接严格记录，最大11361/11440；未将其12个非严格标签当严格。
* `SIX_LOW_HIGHER_CODEGREE.json`：253直接严格记录，最大1329/1430。
* `FIVE_LOW_NONUNIT_HIGH.json`：371严格，最大24301/24310。
* `FIVE_LOW_NONUNIT_HIGH_JOINT.json`：6严格，最大1805000677/1841667035。
* `MIXED_SIX_JOINT.json`：low5 bad3 37严格最大24279002739/24310000000；bad3_12 37严格最大13444999486/13505554205；badnone 1严格60461689187/60775012155。
* `V25_TENTH_BOUNDS.json`、`V25_Q8_TENTH_BOUNDS.json`：逐个域的标签数、轨道数和全部最大界已入正文表。
* first-hour 的 `MIXED_SIX_v24_low5_badnone.json`、`MIXED_SIX_v24_low5_bad3.json`、`MIXED_SIX_v24_low5_bad3_12.json`、`MIXED_SIX_v24_low6_badnone.json`：读取直接界及五元迹基本型47649/48620。

## 仍需准确呈现的限制

本次没有发现一个足以指出候选论证错误的新数学反例或明确缺口；也没有重新验算数万条全部证书。读者稿保留其真实性质：完整结构与覆盖的自然语言候选，使用明确有限局部分类和保存的精确有理数证书，完整T34 Lean仍未闭合。

大表没有印成数万行。自然语言正文说明了每个分类域的必要条件、生成递归、实际输入归属、拒绝规则、合并依据和严格证书检验规则；原始JSON承担逐输入具体位置/乘子数据。如果主页面要称“单文件含全部可独立核算数据”，必须另外嵌入这些原始表，不能仅因正文已完整叙述就声称含全部逐行证书。建议页面称“完整自然语言候选证明，逐行算术证书另附”。

正文没有保留源文过时的“r≤5仍开放”“25点剩5–8低未处理”等历史句子，也不把这次排版变成新数学验收。

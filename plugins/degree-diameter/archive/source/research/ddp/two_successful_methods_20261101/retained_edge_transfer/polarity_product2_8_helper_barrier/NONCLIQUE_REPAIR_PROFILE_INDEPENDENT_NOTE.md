# 独立攻击结论：固定cap31模型的balanced complete bipartite修补被排除

2026-11-01。**预测在声明范围内成立，未发现漏路线或错误的交集扣重数。** 下面给出纸面依据；唯一tiny scalar实际0.011899883 CPU秒／2，d0..31与t1..31一次完成，最终K(t,t)幸存参数0。此结论不排任意nonclique、unbalanced bipartite或改源/改mandatory边。

## 1. 固定范围与继承事实

只用root指定的literal15点q2 factor A（absolute集合O_A大小5）及给定genuine585点q8 polarity factor B（O_B大小65）。继承已实际32subsets得到的repair profile g(0..5)=(5,4,1,0,0,0)，不重新验证或声称任意15点关系、任意polarity/未运输absolute标记的同构均有此profile。

source为两factor的looped product删selfloops，absolute product有325个based classes。每class保留原26个old nonabsolute neighbors，再加r4个完整原N copies，因此每class共5个free vertices，F大小1625。不同class的mandatory N两两不交，分割全部8450个old nonfree vertices；后者degree已到31，不能接新helper。每个F点mandatory degree26，故只余5个新增degree slots。

新helper h的actual F pin数为p_h，helper内部degree为d_h，p_h+d_h≤31。允许任意F–F peer edges及不均匀、重复based class的actual pins；所有mandatory edges不删。F在mandatory图中独立，helper不能直连饱和old nonfree target。这些是本次路线分类的接口，不读source8775图或旧585数据。

## 2. hard X与g profile给必要式(1)

取X=(A非absolute10点)×O_B，共650个old targets。一个mandatory一步邻居属于唯一based class的2点direct pair，这些pair在每个B-absolute column分割十个A targets。

固定h与B列b，令T_b为h ownpins中该列出现的不同A-absolute rows，t_b=|T_b|。own mandatory旧suffix≤2到X_b的范围只取决于T_b；其他B-absolute列不可能两步进入b，因为不同absolute vertices无edge/common neighbor。重复同class的不同copies不增加这个旧suffix范围。

已继承的g(t_b)恰给至少仍需额外direct class渠道的repair classes数。每个此类至少有一个target仍未覆盖，direct pairs分割X_b，故必须由同based class的own F-peer pin或neighbor-helper pin修复，不能用另一个class替代。

h到old X的≤3路线只有：own Fpin后mandatory≤2；own Fpin后一个F-peer再mandatory一步；neighbor helper后Fpin再mandatory一步。两次free-peer后没有余下一步进old X；第二个内点为helper时，helper不能直接接饱和X。clone–old–otherclone的两步终点是F，不是old X，也不补缺。

每own Fpin已消耗它的1个新增slot，因此最多4个F peers。neighbor helper g最多给p_g个direct based classes。利用g(t)≥5−2t及Σ_b t_b≤p_h，得到

```text
325 − 2p_h ≤ Σ_b g(t_b) ≤ 4p_h + Σ_{g∈N_H(h)} p_g,
325 ≤ 6p_h + Σ_{g∈N_H(h)} p_g.                    (1)
```

取minimum helperdegree为d的顶点。它与其邻居均p≤31−d，故325≤(d+6)(31−d)。一次标量给d∈9..16。**这是minimum degree的范围，不是说每个helper degree都≤16，更不是排除任意nonclique。**

## 3. K(t,t)的F目标界：mixed route没有漏掉

现在仅取helper graph H=K(t,t)，每个helper degree恰t，actual p_h≤p=31−t，不要求相等。以左part的h为根：

- 全部左part pins都可经至多两条helper边到达，贡献≤tp。
- 全部右part pins及它们的F peers贡献≤tp+4tp=5tp。
- own pins的一个peer贡献≤4p；两个peer贡献≤16p，因为中间F点的一条slot已用于回到前pin，余peer slots≤4。
- own pin经过两个mandatory旧边，只能到同based class的其他4个F twins，贡献≤4p；不同class不共享mandatory旧邻点。

还有确实存在的mixed路线 **h–ownFpin–otherhelper–Fpin**。它的终点已经属于某个helper的pin集合，而K(t,t)的全部helper pins都包含在上面left/right两union中，所以不能另加贡献，也没有遗漏。

这些覆盖所有≤3到F的路径类型，故

```text
1625 ≤ (6t+24)(31−t).
```

标量给仅t8..19、p12..23可能。式(1)还可把K(t,t)预筛成t9..16，但以下仍检查完整8..19，便于与root预测对照。

## 4. S_h：heavy row≥8与column≥2是真必要条件

S_h指**未被h ownpins拥有**、但整个26点old mandatory N都由h ownpins的mandatory旧suffix≤2覆盖的based classes。它不要求未被别的helper拥有；此处不能把local unowned偷换为global unowned。

对候选class(a,b)，其26点N包含8个row-a／B-nonabsolute targets、2个A-nonabsolute／column-b targets及16个双nonabsolute targets。

**row-a至少8个distinct pins。** 其他A-absolute row两步到不了a，故8个row-a targets只可能由row-a pins覆盖。由于(a,b)未owned，这些pin的B-absolute列d都不等于b。对任意d≠b，d的mandatory2-support与b的8个nonabsolute邻点恰交1：在原GQ incidence图里，d与line ρ(b)不incident，unique point-to-line projection给唯一三边path d–ρ(z)–v–ρ(b)，对应quotient三步d–z–v–b。不同absolute无edge/common-neighbor使该v不是b，故它确是那8个邻点之一。因此每个pin至多覆盖其中一个，需要至少8个distinct based pins，actual pins更不会少。

这一步**不能仅由row9和absolute无common-neighbor推出**；它实质使用给定genuine GQ的unique projection性质。当前scope有该性质，故不是缺口，也不需要重算585表或Steiner。没有把旧U8≤380／140 targets／18 classes强界或72／9记为本轮新结论。

**column-b至少2个distinct pins。** 要到2个A-nonabsolute／B-absolute targets，ownpin必须在列b。unowned排除row a；固定literal A的其余每个absolute row两步support至多覆盖该pair的一个点，所以至少2个不同rows/classes，actual pins至少2。重复同class copies不加强support。

## 5. 两heavy rows的charge正确，C(p)仅在p≤23使用

把actual ownpin数≥8的A row称heavy。saved class必在heavy row。p≤23确保最多两heavy rows；重复copies可能让某row看起来heavy但并不真的覆盖，忽略这个额外限制只会使上界更宽。

无heavy row时S_h空。若只有一heavy row，至少8个pins在该row；每个unowned saved column都需要两个row外pins，且不同column pins不重用，故|S_h|≤floor((p−8)/2)。

若有两heavy rows，至少16 pins在其中。按每个B column中**有pin的heavy-row classes数**m_b=0/1/2分情况：

- m_b=0：最多两个heavy-row classes可saved；只要saved非空，该列必须有至少2个nonheavy pins，所以saved数≤nonheavy pins数。
- m_b=1：最多一个unowned heavy-row class；要补足它的两种A-support，除已有heavy row外还需一个nonheavy pin。
- m_b=2：两heavy classes都owned，无unowned heavy-row saved class。

这是每column的容量charge，不要求每个saved class物理使用不同pin来覆盖；只需要saved数≤该column可收费nonheavy pins数。column间pins不重叠，因此|S_h|≤总nonheavy pins≤p−16。

所以在本次有效p≤23范围，

```text
|S_h| ≤ C(p)=max(0,floor((p−8)/2),p−16).          (3)
```

实际p_h可以小于p。C在0..23非减，因此用统一cap p上界所有C(p_h)合法。这里不把(3)延到p≥24的三heavy-row情况。

## 6. global union/intersection：每个交集class至少左右各收费一次

令P_h为h ownpins的不同based classes集合，E_h为其own freepeer classes，|P_h|≤p_h、|E_h|≤4p_h。令A=union左P_h、B=union右P_h，a=|A|、b=|B|、i=|A∩B|。

左helper h要覆盖某class的全部26个old targets。右helper pin或own/ownpeer class一旦命中该class就覆盖其整个N；若这些direct class渠道均无该class，则所有targets只能由own mandatory2 suffix覆盖，即该class必须在S_h。因此

```text
325 ≤ b + |P_h| − |P_h∩B| + 4p_h + C(p_h).
```

helper→helper→helper→old target被old非free饱和排除，right-pin peer到old target要4步，均不缺新渠道。可以忽略E_h、S_h的进一步重叠，因为只会高估右侧。

左右两part求和，每个A∩B class在至少一个左helper和至少一个右helper中出现，故两side交集扣项合计≥2i；若有多owner/多pins，扣项只会更大。于是

```text
2t*325 ≤ t(a+b) + 2t(5p+C(p)) − 2i.
```

写Z=a+b≤2tp，i≥max(0,Z−325)。函数tZ−2max(0,Z−325)在t≥2时非减，本次t8..19又有2tp≥325。取Z的最宽上界，化简得

```text
(t−1)*325 ≤ t*((t+3)*p+C(p)).                    (4)
```

这个推导没有把实际pins假定均匀或全class distinct；它只用p_h≤p和按union扣重数。

## 7. 唯一scalar结果与停止范围

一次d0..31／t1..31小整数检查确认：(1)的min degree候选9..16，F-bound候选t8..19，而这12个t全部违反(4)。最接近的是t13、p18、C5：左3900、右3809，仍差91。完整逐t/d行在RESULT.json，未枚任何pinsets或helper graph。

实际0.011899883 CPU秒／2，singleworker，全进程终态。没有读/重算旧585邻域、Steiner、8775 source、field、BFS、solver、Lean、付费审阅，也未重跑32subsets或旧toy。

因此仅关闭当前fixed literal A×genuine B、r4 mandatory copies／cap31的**balanced complete bipartite helper graph K(t,t)**，即使actualpins不均匀、class可多owner且允许任意F-peer edges。任意nonclique、unbalanced bipartite、改源／改mandatory旧边仍开放。本轮到此STOP，不自动扩展或续timer，不修改root状态/Wiki/冻结交付或三／五原目标C审范围，不新增图或kernel计数。

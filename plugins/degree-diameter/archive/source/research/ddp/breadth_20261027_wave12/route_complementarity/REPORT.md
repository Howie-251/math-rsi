# 同一72控制图：从方向障碍到闭路平面的联合覆盖

本轮仍为零新下界，阶段预测验证不等于Goal完成。已实测两个受控图；最新矩阵/方向协调图为1152点、4608边、8正则、D5，普通无序>4坏对12800。它修好指定槽并保住全部468紧路，但比原best12384仍多416个坏对，不能称全局改进。新增的具体反例是同fiber闭路平面的互补性被破坏，下一规则必须同时保护紧路与全部72个同fiber闭路联合覆盖。

| 图 | 本轮是否新生成/全源核验 | 实际D | 普通无序>4坏对 |
|---|---|---:|---:|
| 原cachedbest68 | 只复用既有结果，无旧BFS重跑 | 5 | 12384 |
| 0↔18只改b为3 | 第一个受控图，各一次全1152根BFS | 5 | 13424 |
| 同边协调T′与b′ | 第二个受控图，各一次全1152根BFS | 5 | 12800 |

矩阵图比b-only图少624个坏对，但仍比原图多416。本阶段仅这两个新图、两次独立全源核验；后续归因和预测验证都复用缓存，没有第三个图或重复BFS。

## 未知问题与P1：offset能否补救固定线性部分

本轮最初未知：F2 best68失败是因为offset0使可互补的路线重合，还是方向本身不足？[先冻结P1](PREDICTIONS.md) 后找到base0→10，全部≤4控制walk仅AACA与DCC，像为normal6和normal9的两个rank3超平面。独立平移coset DP及纸面交集计算均给精确union12；任意源fiber值至少漏4。故原best68固定maps/vectors不能仅靠global或edge-local offsets达到D4，不再搜该offset修复。[独立单槽检查](translation_bound_check/ACTUAL_SLOT_CHECK.json) 重新核对了341条控制walk及所有16个源fiber状态，只分析此具体槽，不排其它1023个线性输入。

[同槽F3成功对照](same_slot_success_failure.json) 中，原5832构造的AACA本身满rank4、覆盖81；F2的两条rank3路线仍不互补。另复用原首pencil0→1的四个27点平面、共同core9、联合81证书，见 [成功fixture](ternary_success_fixture.json)。这些是既有成功构造的定向解释，不计新图或新发现。

## 固定T的方向修补：预测命中，但切片不能全局协调

[冻结单边规则](CONTROLLED_PREDICTION.md) 只改0↔18的非零b，其余T、b及offset0不变。15个方向中8个使AACA rank4，却全都损坏原紧路；其余7个在offset0未修目标。按最少损坏、再最小b选择b3，反向b9。预报目标0→10的256个有序fiber对全覆盖（原64缺项消失），同时37↔63两个唯一四路槽rank4→3，各缺128 ordered，对应128 unordered。第一个完整图的 [实际核验](controlled_edge_change/actual_prediction_check.json) 全部匹配；D5/13424并非目标成功。

随后[第二边15值](controlled_edge_change/SECOND_EDGE_REPORT.md)固定first b3，改规定边0↔36：最佳第二b1可恢复37↔63并保目标，却新损2↔36和26↔68两对base fibers；4个有序紧槽各缺128，合计512 ordered/256 unordered。未生成该第二边图。

[联合225值](controlled_edge_change/joint_two_edge_analysis.json)同时取遍这两条边的15×15方向，全部T、offset0与其它142个方向仍固定。120项使AACA rank4，但同时保住全部468紧槽者为0，最低仍损2个有序紧槽。原赋值(1,3)紧槽完整但目标未修，不能误写成225项全部损坏紧槽。最佳(3,3)就是已测单边图，无新图或BFS。该225slice已闭，不排一般edge-local模型。

## 协调T与b：预报保住目标和紧路，实际仍有多路缺口

针对上述缺陷，先冻结一个代数选定候选而非扫描矩阵：同一边0↔18取output shear S，令

    T′=S*T，columns=[2,4,8,3]；b′=3；
    T′⁻¹ columns=[9,1,2,4]；T′⁻¹b′=8。

其它143条边与offset0均保持原best68。与b-only的reverse b9不同，此协同保留原reverse direction8。AACA列成为[10,9,7,1]、rank4，468个唯一四路槽全部仍rank4。[冻结matrix预测](controlled_edge_change/matrix_shear_prediction.json)只检查这一个候选、矩阵grid0。

Root随后生成唯一该matrix图并完成一次独立全1152根BFS：[matrix_prediction_check.json](controlled_edge_change/matrix_prediction_check.json) 确认target0→10 miss0、tight_slot_missing=[]，两个具体预报都命中。然而全图仍D5/12800。这给出下一未知：究竟哪个非tight覆盖被破坏？不能只由总数推测原因。

## 首个off-target反例：rank未变，唯一补点却消失

观察新图后，按字典序定位首个“旧≤4、新>4”点对(0,5)，二者均在fiber0。旧完整route数据给距离4，新缓存给5。[单槽归因](off_target_first_damage/REPORT.md)保留全部33条closed≤4路线（长度0一条、2四条、4二十八条），不是只看最短路。

旧路线中只有0123=ABCD覆盖目标5：

| ABCD | 旧 | 新矩阵图 |
|---|---|---|
| columns | [8,13,13,8] | [8,12,12,8] |
| rank | 2 | 2 |
| image | {0,5,8,13} | {0,4,8,12} |
| word total linear map / 输入0漂移 | I / 0 | I / 0 |

其方向改变，旧唯一补到的5消失，新4和12已被其它路线覆盖；全部路线并由16降为15，只漏5。这不是rank4丢失，也不是漂移改变。另一闭路0213确实rank2→1，但所失1、9仍被其它路线覆盖，不是(0,5)的直接原因。完整33路数据在 [RESULT.json](off_target_first_damage/RESULT.json)。

进一步，33个closed word全都free-reduce为空，逆一致的affine offsets在这些回退路上必相消。因此固定新T/b下，任意输入x的同fiber可达集都是上述union共同平移x，必唯一漏x XOR5；offset也不能救此self方向缺陷。Root事先据此预测，再只读新距离缓存核对全部16个x，[self_plane_prediction_check.json](self_plane_prediction_check.json)逐项EXACT，无新旧BFS。这是8个无序self损失的具体因果例子，不是全部净增416坏对的分解。

## 下一决定与范围

继续同一72控制图的覆盖问题。任何新T/b协调，先同时保护 **468个tight rank4约束** 与 **全部72个同fiber closed-plane union的完整覆盖**，再筛能修其它多路槽的连接。仅保每条rank、reverse-b或tight完整都不足：本例保住这些已检查对象，仍丢失低rank路线的唯一贡献。

暂停已闭固定T单/双边b-only切片及offset修复，不自动加第三b、矩阵grid或独立新模板。本报告没有启动新候选、优化或搜索。所有当前预测/诊断已终态，pending为空；完整D4构造仍未获得，Goal未完成。

[steering前GQ待核稿](../gq80_overlap_bound/REPORT.md)与[compound来源侦察](../compound_route_scout/REPORT.md)仅保留history，不作为本阶段成果。root统一同步Wiki、HTML及恢复入口。


## 最新人工纠偏后的收束状态

用户要求不要深陷每次只减少几百坏点对。当前单/双边及port-preserving局部修补线收束；原拟2520关系筛选实际未启动并已取消，见port_preserving_test/terminal.json，零枚举/候选/图，不是失败或UNKNOWN。上述对照保留为构造理解，不能当成继续局部补洞或最终Goal完成的理由。下一步以整类覆盖保证为选择依据，维持针对性预测，不横向再做模板大筛。

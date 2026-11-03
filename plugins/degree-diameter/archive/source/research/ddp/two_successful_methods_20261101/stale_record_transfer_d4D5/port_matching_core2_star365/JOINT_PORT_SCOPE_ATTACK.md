# 固定首P的joint-port模型：只读反例攻击与Hall终态

仅只读 `joint_fixed_first_P/run_once.py`、RESULT、FOUR_CORE_R4_SUPPORTS及实际名为ALLOWED_MATCHING_MODEL.json的结果；没有读source边表、重算球/距离、运行匹配/solver或候选BFS。未发现exact newroot等价或本次Hall排除的缺口。

## 等价条件的三处关键审查

1. **最多一matching步。** newroot z起的最短路不能再回z。两个连续出现的matching边之间若无oldstep，就是同一匹配边的往返，可消；否则其中段只含old T=G−cuts。若两端是不同原ports，该段长≥5，因为T⊂G且原ports互距5；再加两matching步已超5。这是oldT段的下界，不是假称添加matching后ports仍相距5。
2. **hole前后腿可实际实现。** 所有cut端点都在P，最短source P-to-t路若穿cut，可从该cut下游P点重启并缩短，故dT(P,t)=dG(P,t)。对hole t（dG(P,t)>4），一步star加一步matching后旧腿总长≤3；P全为core使前腿至少1，尾腿至多2，尾port必是唯一R2 owner b。该source≤2尾路若碰P，就有dG(P,t)≤2，矛盾，故自动避cut。于是`dG(P,mate(b))+dG(b,t)<=3`对hole必要且充分。不能把这个P-core契约放松成star接任意port。
3. **无向allowededge须双向成立。** 每个port b的全部hole合并为阈值`3−max beta`；无hole类不限制其mate。{a,b}只在a满足b的阈值、b也满足a的阈值时允许。因每个hole只需一个matching且对应路径不依赖其他matching选择，allowed图的perfectmatching恰等价于newroot覆盖，未漏相互约束；这仍不解决旧旧D5。

## 实际代码/缓存对应

脚本只从四个corepin43,58,151,314各做一次depth4新支持，未重验sourceD5或28ports球。dP用四行非负距离的最小值；无≤4路线记5，足够区分hole及所有1..3阈值。β按R2类内self=0、原source邻接=1、其余=2，使用已继承的完整R2分区。allowed循环实际用了两个互向阈值，并排self；没有把单向proposal误作无向可选边。

原READ阶段没有查β；本次读取root新缓存后，port2的holes为0,91,254,363，β全2；dP(256)=3。因此旧M(2)=256对目标0的条件为3+2>3，和原saved distance6一致。这些是root已存数据的读取，不是本paper重新算距离。

实际RESULT为72holes、24个β2-hard owners；near ports dP≤1仅126，hard owners在actualallowed图的邻集并也仅126。完美匹配会把这24个不同owner注入其不同mate，邻集只有1点，不可能。因此本次`COMPLETE_NO_FIXED_P_ALL_MATCHINGS_BY_HALL`严格关闭固定这两cuts的**全部**28port perfectmatchings。0matching solver、0candidate graph、0oldroot BFS不是缺验：newroot必要门已经完整拒绝。它不是新的365图一般NO，也不是只旧10000样本NO。

## 逐P推广可用于下一必要门，但本paper不执行

对任意两条顶点不交的ORIGINAL core-core边，P都是四core端点，上述全部证明原样适用，未使用首P的特殊labels、source vertex-transitivity或某个旧matching。因而若将来在一个明确完整域中，每P都找到一个Hall不足subset，就可关闭这一整条“两corecuts＋四star＋28portmatching”规则，不需匹配搜索或oldold图检验。反之，Hall未拒绝的P仍是未解决项；一般非二分allowed图中，Hall必要条件通过本身不保证perfectmatching。

还有不需数值的简化：每条corecut的两个端点最多邻接一个不同的绝对port。若有两个不同ports分别相邻这两个端点，其旧距离≤3；同一端点邻两个不同ports则距离≤2，均违原ports距5。所以任意两cuts的near(P)至多2。β2-holeowners的mate必须在near(P)；若hard(P)>near(P)，这个subset就足够拒P。这里只提供后续gate的正确性，未枚任何新cutpair、未声称所有P的hard数已知。

## Conditional fresh草稿不执行

`joint_port_independent_acceptance/verify_candidate.py`在Hall终态到达前已准备，仅AST解析。它本可对真candidate各parse source/candidate一次，核712旧边/两cut/14portmatching/固定star/全4度，并全365候选roots ordinaryBFS；当前没有candidate，故源/候选解析0、BFS0，现标为未用草稿。root实际fixedP NO后，不拿旧失败图或source运行它，也不自动开其它P或solver。

## 同轮全域actual终态：已按代码与回执只读收束

root随后完成 `all_two_corecut_Hall_gate/` 的唯一全域门。本paper只读run_once.py、RESULT、SOURCE_SUPPORT_BINDING与ALL_CUTPAIR_HALL_COUNTS.tsv的表头/首行，未重算任何支持或边对。

- 域来自原source全部630条core-core边，i<j并排除共享端点；expected按core-induced degree的组合数扣除1764个共端点对，实际196371个matching-cut pairs全部完成。没有固定首P、随机抽样或靠source对称少测；630 choose2−1764=196371。
- 4个已存首P depth4支持被转成闭R4位集并复用；其余336core中的332个点仅作新问题所需depth4支持，代码在dist=4停止扩展。未重做旧28port球或source全D5验证。
- 每个port的layer2 mask由其已保存R2类删self与原邻点得到，恰为β2 shell。`shell2 & ~cover`只测试这有限正位集中的遗漏点，不需要把Python无穷补集当额外vertex。四core R4并集为cover；nearbits只并四pin的原port邻接，恰为source dPport≤1。
- hard集合中每port至少有一β2-hole，其mate必须在near(P)。完美匹配对不同hard owners给不同mate，故hard>near就是充分的NO证书；此门没把一般图Hall条件通过当成匹配充分条件。mutual或β0/1其他义务在此只可能进一步收紧，没有必要生成它们。

实际RESULT：196371/196371完成，hard21..27、near0..2，最小hard−near=20，survivors0；native1.211394177 CPU，原case累计3.763081991/20。4旧支持＋332新支持，匹配solver/365graph/oldrootBFS/新sourceD5验证均0。没有发现域、复用索引、β层分类或Hall必要门的实质缺口。

结合前述逐P等价/必要性，可接受严格结论：**固定自然364/714源，任意两条顶点不交原core-core删边、其四端点接同一个新4star、全部28ports作任意perfectmatching且无其它改动，这整个规则不能给D≤5。** 不仅固定首P，不仅旧10000样本；亦不推广到公开364/728源、第三cut、不同star pins、额外repair、多helper或一般365点图。

旧10000样本UNKNOWN是当时样本证据的准确历史，raw结果不改；现在该精确架构由后续完整Hall门关闭。conditional fresh草稿从未读取图或运行，现也无候选可触发。当前全部停止，不自动增加第三cut或打开第二窗口。

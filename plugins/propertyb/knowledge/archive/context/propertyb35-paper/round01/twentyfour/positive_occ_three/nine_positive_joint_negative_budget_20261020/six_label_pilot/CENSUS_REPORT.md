# 六标签域完整诊断与两孤立标签合并

## 完整结果

新[CENSUS.py](CENSUS.py)不在首界失败处停止。10秒profile在1.975 CPU秒内完成整个域

    J为六标签无自环多重图，Δ(J)≤4，7≤E≤12，M3≤13。

结果为417,328个有标签图、981个S6轨道，所有轨道大小之和严格等于417,328。无预算前缀或未处理图。[CENSUS_PROFILE.json](CENSUS_PROFILE.json)保留每代表向量、六个实际四元正集、全部候选数、pair-top前缀、triple扩展、40组最坏b参数和解析标记。旧首停PILOT/PROFILE及[REPORT.md](REPORT.md)保留原范围。

* 原C3/C4联合sum界严格：902轨道，382,963个标签图。
* 原sum界不严格：79轨道，34,365个标签图。
* 至少两个孤立标签：完整域共12轨道，其中原sum界失败两轨道／270个标签图，均由[一般解析稿](TWO_ISOLATED_LABELS.md)修复。
* 所以本轮现有界加两孤立解析后，剩77轨道／34,095个标签图。

这里“剩余”只表示尚未被这些充分判据覆盖，不是能实现的负布局、signed反例或H。原九正族固定x后余族仍有三重点的情形不属于本图域。

## 两孤立标签解析的完整范围

root所给推导已逐项核对并写为[TWO_ISOLATED_LABELS.md](TWO_ISOLATED_LABELS.md)。E≥7排除三孤立；恰两孤立时另外四标签图E只能7或8。E8全四度给K=a²+b²+c²≥6；E7的度型(2,4,4,4)和(3,3,4,4)分别给

    K=2+Σαi²≥4,
    K=a(a+1)+b²+c²≥4。

C4=16K。K≥5时pair扩展≤16、triple扩展≤4，统一堵界≤68<80。K=4仅两种candidate-pair图，均最大度二；u≤2时堵界≤59，u=3时若有重复／非最大pair目标则堵界≤60。余下16候选共享未选pairZ，每个Z点已有至少两次正出现，故活跃不含x负四集最多五个，含x负四至多一个、堵四份，合计9<16。此证明处理完整两孤立类，不依赖本次有限表对该类的通过情况。

## 剩余77轨道的共同范围

[SUMMARIZE.py](SUMMARIZE.py)将每个raw界失败代表的所有合法(u,t,v,b)压成明确b整数区间，保存至[CENSUS_SUMMARY.json](CENSUS_SUMMARY.json)。不是只列最坏b，也没有按不同参数混用C3和C4的严格性。

|性质|剩余轨道数|
|---|---:|
|E=7|64|
|E=8|13|
|M3=0|3|
|M3=1|21|
|M3=2|34|
|M3=3|10|
|M3=4|9|
|无孤立标签|74|
|恰一孤立标签|3|

支撑图分量大小为6的有60轨道，2+4有14轨道，1+5有两轨道，1+2+3有一轨道。按最小出现界失败的t分类，t=1有六轨道、t=2有25轨道、t=3有46轨道。因此现有完整图诊断已把未覆盖集中在E7/8、M3≤4；E≥9或M3≥5在整个已列图域内均被现有sum界覆盖。没有据此将有限计数观察冒充不经证明的一般结构不等式。

最先的三个一孤立代表向量和全部参数已保留；它们不再自动触发单例补新门。本轮没有负布局枚举，也未为77型逐个开展新搜索。

## 全域覆盖与代表运输

第一生成器按标签一次分配全部向后边重数，保持每标签总度≤4与E≤12。未赋值边重数初始为零，所以已完成完美匹配积非负且单调，部分M3>13剪枝安全。剩余总度容量不足以达到E7时才剪枝。任意合法向量唯一确定每个分配分支，故完整递归覆盖该域。

图到六正集的恢复无损：每条实际多重图边给一个同时属于两个标签的点，每标签再补4−d个私有点。余族最大正出现二意味着除此没有其他点型；总并大小为24−E≤17。任意实际点重命名、平行边重命名及六标签S6置换都保持横截数、指定目标扩展分布和统一参数界。

三点横截恰对应三条端点不交图边，所以C3=M3。C4候选逐子集枚举；C3/C4均用64项整数容斥核对。每个代表的完整合法参数满足u≤t≤3、v≤b、u+v≤4、t+b≤20；b单调性使先核40组b=20−t无损。两候选族严格性始终在同一组参数下判定。

## 第二实现与独立计数

[INDEPENDENT_CHECK.py](INDEPENDENT_CHECK.py)另按15个无序标签对逐边分配重数，显式更新两个端点度、E及新完成的完美匹配积。它不使用原生成器的逐标签整行遍历，也不在生成时做S6跳过。它产生417,328个不同目标向量，逐个属于981代表的两两不交S6轨道；数量完全相等，故两个完整域严格相同。

该重放还独立核每代表的全部pair/triple扩展。若指定q个点覆盖标签mask C，仍未命中的标签集合为W，则用条件容斥

    extension = Σ_(S⊆W) (−1)^|S| C(avoid(S)−q,k)，

其中avoid(S)为不遇标签S的实际点数；(q,k)分别取(2,1)、(2,2)、(3,1)。所有指定点都避开S，故统一扣q正好。这个方法不从横截候选列表反向累加Counter，得到与主程序全部pair-top前缀和h3一致。全局C3/C4及全部40参数界也逐行一致。[INDEPENDENT_CHECK.json](INDEPENDENT_CHECK.json)为PASS，CPU约2.76秒。

这是完整域和独立精确计数验证，仍不是跨家族审阅或九正门整体证明。没有读取Gemini推导，没有重复PG扫描，没有改动规范主稿或研究导航。

## 再现

    python3 context/propertyb35-paper/round01/twentyfour/positive_occ_three/nine_positive_joint_negative_budget_20261020/six_label_pilot/CENSUS.py --cpu-limit 10 --prefix CENSUS_PROFILE
    python3 context/propertyb35-paper/round01/twentyfour/positive_occ_three/nine_positive_joint_negative_budget_20261020/six_label_pilot/INDEPENDENT_CHECK.py
    python3 context/propertyb35-paper/round01/twentyfour/positive_occ_three/nine_positive_joint_negative_budget_20261020/six_label_pilot/SUMMARIZE.py

# 单packet逐边解与全pair flow门：只读scope核查

本核查只读`edge_voltage_packet/run_once.py`、其RESULT，以及`allpair_edgeflow_gate/run.cpp`、driver、PRED和RESULT；未读取或重生成二进制cache，未重复路径、消元、BFS、参数或solver。没有发现本次单packet构造及全pair必要门的实质逻辑缺口。旧四全局系数族NO保留，不能把它套到新的960个逐边电压变量上。

## 1. 单packet的显式解确实改变了自由度

每条无向实际point-edge以小label到大label为正，反向电压取负。脚本对原保存的66条路径累加实际edge的整数signed使用数并消去零项，再对相对于第0条路径的差做F23消元；不是把旧`(port,lambda)`四维forms继续当逐边forms。

实际RESULT：66条路径有66个不同signedflows，使用148条边，相对差rank65。取其中22个独立差设成1..22，脚本RREF求一个960维电压解（free列置0），再以原66flows计算全部phases并检查：选中22条相对reference的差恰为1..22，真实phase并满23。reference自身的phase不必为0：整套0..22相对差平移后仍是F23全体。实际解21条边非零，不与选22条独立等式矛盾。

这证明**存在逐边电压覆盖8→70这个packet**，并非只过数量门；不证明其余base pairs或完整5520图D5。原26个globalforms的碰撞来自更强的共享限制，已被这个实际单packet解绕开。

## 2. 全pair代码的对称、NB和canonical语义

engine从全部240个root枚普通point-edge NB walks，长度0..5。`next_vertex!=previous_vertex`只删实际同一simple edge的立即反向；不按controller port删不同point-edge路线。DFS只在记录终点时要求`target>=root`，**中间点不受label大小限制**，所以没有漏掉先走较小label的合法路径。

只存u≤v是完整的：反转u→v路径得到v→u的等长NB路径，signedflow取负；同一反向一致C23电压下，phase集合也取负，覆盖全部23与否相同。含u=v的240个diagonal，没有把它们省略；空walk在depth0、flow0和phase0被保留。28920是包含diagonal的无向packet槽数，不是5520目标图的普通无序坏点对数。

`canonical`按edge绝对ID分组，将正负使用次数相消，把净系数表示为重复的signed `(edgeID+1)`，最后补零到5个int16；零是padding，不是实际edge0。净L1范数不超过原路径长度5，不会溢出这5格。非零ID依绝对值排序，取负仍是同样的canonical顺序，因此diagonal的±membership检查正确。长度≤5两flow每坐标差至多10，mod23相同与整数相同等价，故这个整数flow去重恰处理所有对任意C23电压恒碰撞的路径。

## 3. 实际门通过与稀疏解失败分账

实际28920个packets、保存方向2699760条NB路径与2699760个不同flows，最小66，0packet少于23。每packet去重数≤path数，总数相等说明本次各packet内没有signedflow重复；这只排除了一个可能的容量障碍，**没有证明共享边电压存在**。diagonal不同flows为81..97，每个flowset都含0，0个±缺配；全局path/flow总数也说明没有额外NB零流重复。它支持之前的短闭路零流纸面边界，不是对其它长度的断言。

同批评估原21非零边电压：只有1个packet满23，其余28919个不满；首(0,0)只有9个phase，首漏phase1。由于cache包含全部≤5 NB路径，lift点`(0,0)`到`(0,1)`没有≤5路，已足以否定**这一具体电压解**的D5；没有运行目标图BFS，不能报一个未测的精确距离、ordinary坏对总数或全逐边族NO。

cache按u≤v槽顺序保存`u32 count`及`count×5 int16`，offset表绑定u/v及位置；数据是native写入，后续应依本机已记录的little-endian schema读取，并保留signed/padding语义。后续若在22条方程的解空间做固定有限32参数构造，仍须用同一完整cache查所有packets；全部32失败只能给该有限样本无hit，不能把nullspace整体或任意ordinary/permutation covers判NO。

当前单packet阶段累计1.713051688/10、全pair阶段累计3.535598698/10均继承实际RESULT，不清零。0新目标图/参数/Lean，0额外数值/solver/BFS；不在本次核读时写Wiki，待后续终态统一原位归档。


## 4. 32个conditional全局样本终态（后续只读补充）

只读`conditional_global32/PRED.md`、run_once.py、run.cpp与RESULT，没有读取/重算RREF系数或二进制cache。Python以原22个独立path差构造RREF；C++给全部938个free坐标取F23值，再由RREF还原22个pivot，逐行assert约束。固定一个seed的32例来自这个完整仿射解空间，**不是穷尽该空间**。保留960坐标中的gauge重复不漏合法条件解，也不能把样本数当不同构图数。

每例用同一个完整u≤v flowcache计算全部28920个packet；signedcode取真实边电压，零padding跳过。某packet满23时提前停止其余flows只省无用累加，不漏可能使失败转成功的项；未满的packet全部flow都查。critical packet每例另assert满23。newroot不存在额外对称假设：这里用普通C23全局fibre平移与反向路径，故所有packet满23才等价完整cover D≤5，diagonal不能漏。

实际32例全部保critical满23，其中24例连同首坏diagonal0→0也满，支持这两项有界正预测；仍0 fullD5 hit。按missing-phase义务数择最佳例仅是终态报告，没有据此修改下一例电压，未做hillclimb。最佳0-based sample27：19987/28920 packet满23、diagonal200/240满、最少覆盖18、missing-phase义务10784；这些是base-packet/phase统计，不能改称5520图普通无序坏点对数或精确直径。参数定义合法8regular普通覆盖，不等于D5；没有目标5520 edgefile或accepted图。

RESULT当前samecase5.704705500/20（继承前3.535598698，不清零）。32例失败只给`NO_HIT_32_CONDITIONAL_GLOBAL_VOLTAGES_FAMILY_UNKNOWN_STOP`，不排任意逐边C23或这22约束仿射域；指定22条差的值依次为1..22只是保关键packet的一个充分切片，不是所有成功cover的WLOG。旧四globalcoeff12720严格NO则继续独立成立。没有第33例、第二seed、局部坏对优化或新fold/base授权。本次补充0新消元/参数/paths/BFS/solver/Wiki；等待root实际ROOT/NOTE接受后，才一次原位归档全部累计证据。

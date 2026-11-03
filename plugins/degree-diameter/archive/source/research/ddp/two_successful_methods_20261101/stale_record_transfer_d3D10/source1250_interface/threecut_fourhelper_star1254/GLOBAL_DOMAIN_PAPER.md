# 同源三matching-cut＋K1,3的全域：锚定完整性与exact gates

状态：纸面域与公式确认；没有枚边、DP、BFS、field、Lean或ARIS，没有读取新全域numeric结果。继承actual Conder1250 simple cubic/D10、published edge-transitivity、旧girth16及已修正 `STAR_ROUTE_PAPER.md` 的last-cut证明。sole owner另获同line累计30CPU、包含固定域1.916663729的唯一全域门；本paper不重置成本或启动另一进程。

## 1. 完整操作域与source对称锚定

全域是在固定G中任选三条**两两顶点不交**的旧边F={e0,e1,e2}，每条旧边的两个端点完整接同一个newleaf；另一个centre连接三个leaves，helper拓扑恰K1,3。无oldoldrepair、无撤回端点spoke、无跨cut重新分配pins。最终1254/1881全3regular，是否D≤10待exact门/oldold检查。

给任意这样的三matchingcuts，任选一条e*。source G的edge-transitivity给automorphism α，将无向边e*映到{0,1}。另两条边的像不触0/1且彼此不交。α作用于全部旧点，centre送到centre，三leaf按各自cut的像重新编号，就得到对应anchored候选的图同构。

K1,3允许任意leaf置换，且每条cut只用其无向端点对，因此无需另枚cut→leaf的3!指定或每边orientation。对另外两条边以字面lex顺序e1<e2保一份即可。source automorphism并不要求新candidate vertex-transitive；此证明没有把candidate一个root视作全部root。

因此锚定{0,1}、遍历全部合法无序{e1,e2}完整覆盖source上**所有**该规则的三matching-cut候选，可能含isomorphic重复，但不丢未同构代表。它不覆盖shared-endpoint cuts、其它pairing或P4等helper拓扑。

## 2. 1870 otheredges 与1743779 pair参数的数学计数

将旧顶点0、1移去，原边01计一次，其余分别各2条incident边，共删5条边，因此剩

    |E(G−{0,1})|=1875−5=1870。

girth16排除0/1的共同外邻点；它们的四个其它邻点两两不同，各仅失一边而成为degree2。其余1244点保持degree3（剩余总顶点1248）。

两条不同simple edges最多共享一个端点，所以从所有C(1870,2)无序edgepairs减去逐顶点的incident pairs不会重复扣除。合法disjoint对数恰为

    C(1870,2) − [4·C(2,2)+1244·C(3,2)]
      =1747515−3736
      =1743779。

这是锚定参数数量，不是声称有1743779个两两非同构图；也没有在本paper执行edge enumeration。实际sole owner须绑定完整域计数、结束位置和截断状态，不能用本预期数冒作已完成。

## 3. 用source R7/R8/R9的四root exact门

对每条旧无向边e={u,v}，定义实际source闭球并

    E_e^r = R_r^G(u) ∪ R_r^G(v)。

对三cuts及其leaf，`STAR_ROUTE_PAPER.md`的last-cut引理给真实最终距离：

    centre→t = 2+min_(j=0..2)d_G(Pj,t)；
    leaf i→t = min(1+d_G(Pi,t),
                   3+min_(j≠i)d_G(Pj,t))。

这不是把单个deleted-host球硬换成source球：它依赖三cuts是matching、每cut整对给一leaf、helper拓扑K1,3，且最后cut替换对唯一增权情况有prefix≥1。原weighted-T式与此weighted-G式相等；单独Pi的T/G距离仍未必相同。

于是四newroots完整R10覆盖的充要条件恰为：

    centre：E_e0^8 ∪ E_e1^8 ∪ E_e2^8 = V(G)；
    leaf0：E_e0^9 ∪ E_e1^7 ∪ E_e2^7 = V(G)；
    leaf1：E_e1^9 ∪ E_e0^7 ∪ E_e2^7 = V(G)；
    leaf2：E_e2^9 ∪ E_e0^7 ∪ E_e1^7 = V(G)。

helper pairs自身均≤2。sole owner新计算/读取这些source R7/8/9作为新路线support，不等于又做source D10全有效性验收；不能把DP ordinarywalk计数、距离球和NBword容量混为一类。闭球含root自身，不能改为恰好距离r层。

## 4. 哪些全域结果足以严格停止

若全部1743779参数均被上述至少一个**exact**root gate拒绝，已足以严格排source G上整个三matchingcuts/整pair叶连接/K1,3规则：每个候选都有某newroot无法R10覆盖，不需要再跑oldold、构完整失败图或全rootBFS才能给负结论。已闭固定eF子域可继承其真实反例；无论继承还是在新全域表出现，都不另计方法。

**actual终态后的更强scope校正：** root已实际接受全1743779项全部由centre门失败，而非有些靠leaf门。centre精确距离为 `2+d_G(Pall,t)`，对六端点的任意2+2+2配对都相同；因此同一全域数据实际排除该source上三matchingcuts的全部15种unordered endpoint pairings，不只whole-cut配对。详见 `GLOBAL_CENTRE_PAIRING_SCOPE_ADDENDUM.md`。没有再枚15倍候选；visited仍1743779个cuttriple。本节前述“任一root失败”的一般条件若只靠leaf失败，并不足以作此扩张；扩张使用的是当前更强actual全centreFAIL事实。

若有四root均通过的参数，则只通过新根必要门，不保证旧旧D≤10；原三边已删除，完整oldold验收仍需 `STAR_ROUTE_PAPER.md` 第5节或actualcandidate检查。任意预算截断/未完成参数保持UNKNOWN；不能把expected总数、某一个source root或single-source对称性当完整终态。

第3节whole-cut配对的**正向leaf公式**保持原限定范围，不能用本actual centre-NO反向宣称任意跨配也有相同leaf公式。扩张后的negative仍不排共享端点cuts、P4/其它helper图、更多cuts、oldoldrepair、其它source或一般(3,10)。没有graph/parameter/Lean/record计数变化；完成paper即停止，不开独立模板或补跑新参数。

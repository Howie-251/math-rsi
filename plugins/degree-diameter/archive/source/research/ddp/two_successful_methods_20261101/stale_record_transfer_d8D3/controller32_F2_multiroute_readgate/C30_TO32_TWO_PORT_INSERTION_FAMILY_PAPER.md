# C30→C32：两port插点族的完备域与合法剪枝

本文件仅只读 `conjugate_route_repair/PRED.md/RESULT.json` 与既有实际C30输入，作符号范围/剪枝论证。未生成controller、枚word/参数、算matrix/rank/field、构图、BFS或solver。实际局部反馈必须保留：ARC的0→5仅021，4/8；R修后8/8，邻对0→18仍8；但global goodwords仍24，修021/031/120/130同时损020/030/121/131。R只是本轮第二个有依据对照，不是已证明整体更优。

## 1. 固定两个chart，不能换回其它best/共线输入

数据均来自刚完成的RESULT，matrix格式为三列binary codes：

- ARC：`[[2,1,4],[2,1,4],[1,2,7],[1,2,7]]`；
- R：`[[2,1,4],[2,1,4],[2,1,7],[2,1,7]]`；
- 两者actualforward offsets均`[1,2,4,7]`，bar=[1,0,3,2]。

继承该次actualinverse通过，不重验。一步是`(u,x)->(C[u][p],T_p*x+lambda*v_p)`；若复用F5式directions[bar(p)]，必须按既有说明重索引，不能拿方向[p]或原F5矩阵mod2。旧best28/36与先前共线对照都不属于本次两chart族。

## 2. 插点定义与378450参数的完备性

令原实际C30的a(u)=C[u][0]、b(u)=C[u][2]；port1、3分别为a、b的真实逆排列。原port方向固定，不额外反转A/B、换port颜色或改旧label。

选A的两个不同tail i<j，按旧排列的冻结targets定义

`a'(i)=30, a'(30)=a(i); a'(j)=31, a'(31)=a(j)`，

其余旧tail不变。选B的ordered不同tails(k,l)，定义

`b'(k)=30, b'(30)=b(k); b'(l)=31, b'(31)=b(l)`，

其余不变。再从a'、b'的实际逆排列填port1、3。必须保存旧a(i)/a(j)/b(k)/b(l)再同时改动；所选边相邻时，不能把已经改过的target当旧target。

任一“两个新控制点分别各插一次于两条不同A旧边及两条不同B旧边”的结构，都可交换新标签30/31，使它们在A上的tail满足i<j。这一步只消去new-label交换，旧source不需要transitivity。完成后B的关联已固定，必须保ordered(k,l)；若再强加k<l，就会丢掉交叉关联的一半。

故原始参数数为C(30,2)*30*29=378450。两chart共756900个参数/chart任务，不等于这么多合法或非同构图。每条无向A边有固定正port方向，原simplequartic没有A二周期；枚全部A tails已经覆盖所有A边，不需再加“反向Aedge”参数。B同理。

这是这个插点族的完整表示，不是全部32点quartic控制器，也不是任意两个新点的连接方式。source automorphism可能让不同参数同构，不登记重复为独立成果。

## 3. 先检查真正simple quartic

插入后构造`C'[u]=[a'(u),a'^-1(u),b'(u),b'^-1(u)]`。所有32点均须无loop、四邻点不同；由实际排列填inverse保证typed反向关系。允许A/B所选旧边共享旧端点，或同色两个选边相邻，只要最后通过这一检查；事前把这些情形全删会漏本族。

new30的四邻点是A旧edge两端与B旧edge两端；new31同理。A/B邻域重叠会导致重复邻点，必须拒绝。这里拒绝的是本族“simplequartic controller”要求，不是宣称重复port邻点的所有其它fiber构造都不可能。

若合法，controller有32点64条无向边。两chart的实际inverse/nonzero offsets使每个controllerport给两个不同fiber邻点，四目标controller不同，故条件fiber图256点、degree8、1024边且无loop/重复。原C30/q2仅calibration，不继承其D3，更不继承F4/F5源的整图D3；插点后全部距离义务必须重新由本族路线覆盖。

## 4. 两个共享的安全结构门

**无≤3 controller路线。** 若某orderedcontrollerpair没有长度≤3的walk，其fiber任何路径也不可能≤3，两个chart都可拒。controllerD≤3只是必要条件。

**无三角顶点。** 对先通过simplequartic检查的顶点u，若u不在任何controller三角形上，长度≤3的closedcontrollerwalk只有0步和p,bar(p)两步。两步fiber像为`x+span(v_bar(p))`。V四个非零不同向量的并只有`{x,x+v0,x+v1,x+v2,x+v3}`五点，故同fiber缺三点，两个chart都不可能D3。可先问new30/31，再问全部oldlabels；这只是结构条件，不新枚field。

新点的A两旧端点间原A边已删，B两旧端点间原B边也已删，故其三角只能由A端点与B端点之间仍保留的旧边形成。第二个新点也必须有三角；不能把原C30的三角直接继承给插点后。存在三角仅是必要pass。

## 5. rank证书与actual低秩union不能混

对actualword w，fiber像为`L_w*x+W_w`；3步w=pqr时`L=T_r*T_q*T_p`、`W=span(T_r*T_q*v_p,T_r*v_q,v_r)`。长度0/1/2也必须包含。对每u,v和每个source x∈F2³，所有真实≤3 word的像并必须是八点；这精确等价于256图D≤3。

有一条actual满rank3 word，就对该controllerpair全部x直接足够，可作快速PASS证书；全局24个goodwords数本身不表示它们覆盖哪些pair。若无这种证书，不能按“无single-fullrank”拒绝，也不能用各rank2的容量和或x=0平面并直接升级全x。一般剩余cell仍须全部8个source坐标的真实coset并；任一x/target缺失可早拒该chart/参数，并保其witness，后续未检查的cells不冒已测。

四arc另给adjacentpair的统一纸面证书：若u经port p到v，则p,q,bar(q)都回到v，image为`T_p*x+span(v_p,v_bar(q))`。V是四arc，余三向量模<v_p>占满商空间三个非零方向，三平面并全八点。因此两chart的adjacentfibers都能在3步覆盖，独立于某条single-fullrank word。这可以作为已证明的∀x证书使用，不是把旧0→18数值结果借给所有新点。除这种明确证书外，不能省略全部source x。

controller立即反向可能在fiber里取不同系数而产生新位移；未经证明不能只保36个约化3词。尤其对角、相邻及shorter-route全部义务必须保留。

## 6. 终态与停止口径

ARC/R分别记录：结构非法、共享结构门拒绝、chart-specific首坏pair/x/target、全点routeunion PASS及未访问参数。R局部修好021不能作为丢弃ARC的dominance剪枝；两者goodcount同24也不表示等价。可预存每chart短word的affine image表供同一次窗口复用，但本paper没有生成这些表。

完整routeunion命中才是该固定参数的条件D3构造，随后应保存实际C32、两chart之一的全部参数/完整256边表及绑定，交root接受；不能只报goodword覆盖或某pair成功。若预算在全域走完前停止，余域UNKNOWN；只有完整参数域对两chart全拒才关本插点族。有限全case30CPU含旧read/局部反馈及所有准备，不重置、不加第二窗口、其它chart/source/degree/维数。

本文件0新controller/word/matrix枚举、0图/BFS/field/solver/Lean/ARIS，完成即停。旧max28、当前C30局部packet与此378450域是不同层次证据，均不额外计新纪录或方法。

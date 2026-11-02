# Pin集内部任意重连：exact MILP接口的独立纸面核对

本note只核数学建模，不读/遍历图，不构造候选，不做BFS、2hop复验、solver、编译或查询。源H是本case已实际接受的106点D2图，m582、degree10点T={34,54}、其余degree11；源事实继承已有SOURCE_RESULT。本规则与已严格关闭的minimal4和oneR-anchor规则分开，不重复那些有限范围。

## 精确规则与变量

选S⊆V(H)，10≤|S|≤11，新点z只邻接S。只允许改变H[S]中的旧旧邻接：所有至少一个端点在V\S的边/非边保持原样。对每个旧点v，x_v∈{0,1}表示v∈S；对每个不同旧点的无序对{v,w}，y_vw∈{0,1}表示最终S内部保留/新增该edge，约束

    y_vw≤x_v, y_vw≤x_w.

不要求y≥x_v+x_w−1；否则会错误强迫S成clique。y没有自环、无向共用同一个变量。最终旧图Q的邻接是：两端selected时取y；至少一个端点unselected时取H原邻接。最后加z—S。此定义在所有binary变量下唯一确定一个实际简单无向图，允许删旧边及添旧旧非边，而不是只做原邻域复制。

## 一处必须明确的记号：Dom用闭邻域

与新点z的距离≤2等价于

    x_u + sum_{w∈N_H(u)} x_w ≥ 1                     (Dom)

对每个旧u成立，这里N_H(u)是OPEN源邻域。若原消息NG[u]表示闭邻域，则原写法就是这个条件；root已确认实际代码明确采用上式。

必要性与充分性：u∈S时z-u直接相邻；u∉S时，任何z到u的2步路都是z-w-u，其中w∈S、w-u是保留的cross旧edge，因此恰需N_H(u)∩S非空。内部y不会影响这一项。

不能对所有u额外强制openDom sum_N x≥1：selected u已直接邻接z。对源degree11的selected点，degree upper会自动要求其原S邻居至少一个，否则它保留11条cross边再加z将超度。原degree10的34或54若selected且原S内孤立，则保留10条cross边加z恰11，完全合法；其旧两步路经过的源邻居又全在outside，不因内部重连而删除。本note未搜索这样的完整实际S，只指出exact逻辑不能凭空排掉它。T不需要强制全在S，也不强制S诱导原图无孤点。

## Degree upper确实精确

令d_v=deg_H(v)。若x_v=1，最终度数恰

    deg_G(v)=d_v−sum_{w∈N_H(v)}x_w + sum_w y_vw +1.

删去全部原S内部edge，再按y重建，cross边不动，新点添一条；所以cap11等价于

    sum_w y_vw − sum_{w∈N_H(v)}x_w ≤ (10−d_v)x_v.    (Deg)

对x_v=0，所有incident y为0，左边为非正数、右边0，该约束自动成立；unselected实际degree仍是原d_v≤11。因而这不是放松或过强的bigM。新z的degree恰|S|，由10≤|S|≤11绑定。

若额外使用原edge乘积t_vw=x_v x_w（仅582条原edge），可用

    t_vw≤x_v, t_vw≤x_w, t_vw≥x_v+x_w−1

并直接写每个旧点的真实度数

    D_v = d_v−sum_{w∈N_H(v)}t_vw+sum_w y_vw+x_v.

这样10≤D_v≤11对所有旧点也是exact。下界10合法：107点、max11、D2时，从度d的根至多覆盖1+d+10d=1+11d点，故d≥10。用原(Deg)而另加degree lower时，需要正确处理x_v=0的inactive分支，不能把selected公式未经条件套给unselected点；上面的t表达式可避免这项记号风险。

## 每种旧旧点对恰有什么2步路线

两端outside：其原直接边不变；任何源共同邻点w的两条边都至少一端outside，也都不变，即使w∈S。因此源D2自动继承这一类；不需为它另加修复约束。

两端selected：它们都邻接新z，始终有2步路线u-z-v。原内部edge删与留由y选择，不再要求继承原common neighbor。

仅v selected、u outside：若源v-u直接相邻，它是cross边，保持不变。只有原NONADJACENT对需要新条件。对这些有向旧对(v,u)，全部可能共同邻点分两类：

- w outside：v-w是cross边，u-w在outside，两者保留；恰当且仅当w是原common neighbor且x_w=0。
- w selected：u-w是保留cross边，须w∈N_H(u)；v-w内部边恰由y_vw=1表示。

新z不是v/u的共同邻点，因为u outside不邻接z。因此需要且只需

    (1−x_v)+x_u
      +sum_{w∈N_H(v)∩N_H(u)}(1−x_w)
      +sum_{w∈N_H(u)} y_vw ≥ 1.                    (Cross2)

所有项非负。若v没选或u已选，前两项使约束自动成立；恰在selected/outside时，后两项分别计数上述两类真正存在的共同邻点。重复计数不影响“至少1”的等价性；y强制两个端点selected，故不会把outside y当新edge。v/u原nonadjacent保证v不在N_H(u)，不存在y_vv问题。

对每个无序原nonedge需要包含两个方向，或明确用等价的两个定向约束，不能只按label较小者为selected处理。两条内部新边组成的2步路仅可能连接两端selected，已由z覆盖；没有遗漏mixed-route类别。

## 必要充分定理

假定H是给定D2简单源。上述binary约束、10≤sum x≤11、closed(Dom)、(Deg)及所有原nonedge定向(Cross2)，与以下命题等价：按照本note唯一构造Q与z所得G有107点、maxdegree≤11、D≤2，且只重连S内部，所有cross/outside邻接原样保留。

从合法图到模型：按实际S和内部adj定义x/y；各条degree/route等式直接给必要性。

从模型到合法图：构造简单无向G；(Deg)与|S|给degree界；(Dom)给所有新旧点对；旧旧点对按上面outside/outside、selected/selected、selected/outside及原cross edge分类全部覆盖。107点、max11不可能是完全图，故在这些条件下精确diameter=2。没有依赖“原图修改后D2自动保留”的错误继承，也不需要先枚举S。

## Old-edit objective与边数

对原edge e，t_e−y_e恰指示删除：若不全selected则t=y=0且edge原样保留；若全selected则t1、y决定保留。对原nonedge e，y_e恰指示新增。因此

    edits = sum_{oldedge}t_e − sum_{oldedge}y_e
            +sum_{oldnonedge}y_e

就是实际OLD边编辑数量，不是任意rubric或proxy。新z边数不包含其中，按任务定义正确。最小化该目标可以用于找少量旧改边；求解时必须仍以可行性和actual incumbent为准，不把未达最优当无可行图。

实际最终边数由变量唯一决定：

    m_G = 582 − sum_{oldedge}t_e + sum_{all old pairs}y_e + |S|.

不能把它预写成588；本规则允许多个degree10旧点，目标cap并不强制全图达到最大edge数。若SAT，必须按实际x/y生成完整edge表、逐点degree和全部5671个无序点对(107 choose2)检查，正如root既定验收；本note不提前声称得到候选。若数值INFEAS，只在模型、source数据与closedDom实现正确及实际证据强度内处置，UNKNOWN不把这个内部重连族排除。

## 与旧负结果及本note状态

minimal4与252个oneR-anchor全部失败说明旧新路线的分工可能过窄，不决定此处允许任意S内部重连的模型。这里没有重复它们的搜索或另造手工失败trade。唯一实际记号修正是明确Dom为closed，root在启动前已确认同一精确公式。

本note支持这个规则的必要充分建模，没有发现额外路线或degree漏洞。没有运行solver、candidate、source检查、D4编译或paid review，也没有写root计数或Wiki。数学模型准确与实际可行性是两件事；当前尚无107点新图。

纸面写入进程CPU：0.009441873000000002秒；0数值复算。

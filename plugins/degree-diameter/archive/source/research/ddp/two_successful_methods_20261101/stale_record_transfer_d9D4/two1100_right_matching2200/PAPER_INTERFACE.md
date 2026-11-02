# Loz1100两copy：closed-ball四项式的精确性

纸面检查支持 root 的有限gate接口。只用 READ_GATE 中已绑定的RIGHT-law H1100/S8及继承sourceD4，不运行词、端点、相位卷积、source/candidate BFS、field、solver或图生成。没有新找到的same1100右匹配旧NO；原单拆点与normal275 ordinary5cover结论仍是不同域。

## Closed balls可以把长度和≤3压成四项

令A_p为实际旧source从identity出发恰p步的endpoint集合，A0={e}；B_a=union_(p=0..a)A_p为闭旧球。对固定t∈H，有严格集合等式

`union_(p+q<=3) A_p*t*A_q = union_(a=0..3) B_a*t*B_(3-a)`。

右侧任一项取p≤a、q≤3−a，必有p+q≤3，故包含于左侧。反向给定p+q≤3，取a=p，就有A_p⊆B_p、A_q⊆B_(3−p)，故该项也在右侧。这不是把总长度强制恰为3；closed balls中的短路和0步正是等式成立原因。

因此

`U_t=B0*t*B3 ∪ B1*t*B2 ∪ B2*t*B1 ∪ B3*t*B0`

是完整exact endpoint union。B0必须是{e}，B1含identity，不能误用仅恰a步的集合代替此四项，也不能把集合元素重复的次数当不同target。非交换群中的顺序始终是prefix u、matching t、suffix v，即u*t*v；不能将t换到首尾或用684的不同law/rawlabels。

## 一次cross与全部点对

两份actual1100源保持全部旧边，唯一跨层边是perfect matching `(h,0)--(h*t,1)`。跨层长度≤4的路径只可能有1或3次cross；3cross至多夹1条旧边，必有连续matching往返，可消成一次cross。一次cross的两段oldlegs长度和≤3，故从copy0 identity到copy1的实际R4端点恰为U_t。

共同leftH作用保旧rightedges，也保rightmatching，因为g*(h*t)=(g*h)*t。它把任意copy0 root移到identity，并同时将copy1目标左移；因此U_t=H就覆盖全部cross-copy点对，反向由无向距离包含。这里source确为Cayley1100，而不是只有两个H-orbits的684；不借684的结论或labels。

同copy旧点对无需从B3推D4：sourceD4已由既有正确recipe/历史证据继承，且两份source全部旧边仍在新图中，因此原有≤4路径直接保留。不会因为只计算≤3旧leg球就丢失这些已存在的长度4旧路径。若构造另删旧边，这段继承立即失效，但那不是本批规则。

所以在本固定源/匹配接口下，U_t=H是整张条件图D≤4的充分且必要条件，而非仅某个新点或phase计数门。若U_t不满，则某crosspair≥5；同时先cross一步再沿另一份source≤4步给全图D≤5，所以该参数是D5。若有full-U_t命中，root仍按计划生成实际2200/9900边表及producer/fresh绑定后才作图验收，本paper不提前计图。

## Phase容量只作优先的必要门

phase投影是(j,x)→j∈C20，RIGHT law将phase相加。给定t的phase c，cross将每个prefix相位整体加c；普通oldwalk的phase矩阵/多项式由实际8个generator phase决定。因此若某相对phase的所有≤3oldstep、一个cross位置walk数少于55，则它不可能覆盖该目标phase的55点，严格排整个rightmatching域；这不依赖t的normal坐标。

容量计数若没有这种小于55的槽，只是必要pass，后续仍须真实endpoint U_t；不能用route数≥55代替point-cover。此处不重算任何系数、交球或参数，实际判定仍属root唯一数值窗口。

本文件只完成上述等式与scope论证，不授权额外source验证、第二窗口、其他action/phase/normal或新源；后续按root已定cap10（含read/prep）执行。

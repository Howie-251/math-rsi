# P3：直连旧x缺点会把撤回的0/1变成新缺点

**时序与范围：本推导在未读取任何新三cut数值结果的情况下完成。** 只使用root给出的已知旧source/旧object事实与前文13-route门；0source/矩阵读取、数值、BFS、solver、field或Lean。以下先按明确事实作conditional paper，不能把未另绑定的source性质当成此文件重新验证过。

## 已知旧事实与候选定义

actual旧baseobject4536：源G为simple cubic Conder1250，girth16；两条旧cut为01与qr，其中q=869、r=1178。旧候选J的helpers相邻，x-pins={0,r}、y-pins={1,q}。继承旧距离事实

    d_G(0,r)=d_G(1,r)=10，
    d_G(0,q), d_G(1,q)≥9。

后者也由源边q–r和前者三角不等式推出。保存的新缺点t=1058满足d_J(x,t)≥11。没有借用旧source的bipartite前提。

现取g=t；更一般可取任意旧x闭R10缺集中的g，即d_J(x,g)≥11。第三旧cut为g–h，其端点避原四pins，p–h是源非边；移spoke a–p到a–g，并加repair p–h。p=0时a=x，p=1时a=y。记

    U=G−{01,qr,gh}，
    K=J−{a–p,g–h}，
    H=K+{a–g,p–h}。

g–h不等于旧两cut，所以它确实是J中的旧边；K是J子图。只分析p=0或1，不将p=q=869也宣称排除。

## 1. 无新增边时，x到withdrawn p已经至少11

G的girth16使删除源边01后，0与1之间任何detour长度至少15（若断开则为∞）。K中helpers的互边x–y仍在，所以从x到任何旧target，重复helper/base访问都可在**最后helper**处分解：到x的最短prefix取0步，到y取直接1步，其后只走U。这并未漏掉反复访问helpers的短路。

当p=0，K的x只留pin r，y仍有1,q，因此

    d_K(x,0)=min(1+d_U(r,0), 2+d_U(1,0), 2+d_U(q,0))
             ≥min(11,17,11)=11。

当p=1，K的x仍有0,r，y只留q，因此

    d_K(x,1)=min(1+d_U(0,1), 1+d_U(r,1), 2+d_U(q,1))
             ≥min(16,11,11)=11。

这里所有U旧腿只因额外删边变长，不会比所列源G下界更短。

## 2. 旧x缺集与第三cut给其余下界

令δ=d_K(x,a)，p=0时δ=0，p=1时δ=1。由d_J(x,g)≥11及旧xy边，得d_J(y,g)≥10，且K⊆J给d_K(x,g)≥11。由于gh是J旧边，三角不等式给

    d_K(x,h)≥d_J(x,h)≥10。

旧J中x到0有一条1步路、到1有一条2步路，因此

    d_K(g,p)≥10（p=0），
    d_K(g,p)≥ 9（p=1）。

还需关键下界d_K(g,h)≥9：若有≤8的K路，则从g出发在这么短的路内不能遇到x或y（它们在J中距g已至少11/10，K只删边）。于是整路是G去掉gh后的旧old-only detour，与girth16迫detour≥15矛盾。这个证明不假定K路径完全不准使用helpers，而是由长度下界排除了此处≤8情形。

## 3. 两条新增边的完整路线分类仍不能救withdrawn p

沿用 `THIRDCUT_ROUTE_PAPER.md` 的13-route精确门。等价地，考察一条最短x→p简单路：若用了repair p–h，必须以h→p作为**最后一条边**；否则它已提前到过目标p，删去其后回路会更短。因此涉及repair的其余顺序/orientation不会成为漏掉的最短路。

仅剩下列可能及其下界：

| 新路使用 | 路线长度下界 | p=0 | p=1 |
|---|---|---:|---:|
| 不用新增边 | d_K(x,p) | 11 | 11 |
| 只用a→g | δ+1+d_K(g,p) | 11 | 11 |
| 只用g→a | d_K(x,g)+1+d_K(a,p) | ≥12 | ≥12 |
| 只用repair h→p | d_K(x,h)+1 | 11 | 11 |
| 两条都用，先a→g，再h→p | δ+1+d_K(g,h)+1 | ≥11 | ≥12 |
| 两条都用，先g→a，再h→p | d_K(x,g)+1+d_K(a,h)+1 | ≥13 | ≥13 |

13项中其它repair方向或“repair在前”的拼接，会先到p再离开；其首次到p的prefix也落上述类型且已经≥11，故不能提供长度≤10的反例。没有仅检查一条新增边而遗漏两边协作。

结论为

    p∈{0,1} 且 d_J(x,g)≥11  ⇒  d_H(x,p)≥11。

g=t=1058时，新增a–t确实把保存缺点t变成x的1步邻点（p0）或经y的2步邻点（p1）；但原来1/2步可达的withdrawn p随即成为x的新R10缺点。这个局部tradeoff已严格排对应候选，不需要再检查旧旧点对才能知道不能D10。

## 4. 不能外推的边界

该证明推广到**旧object4536的整个x-R10缺集作为g**，但没有排g不在该缺集的其他transfer，也没有排其他旧J/source或所有三cut规则。shared-endpoint cuts仍在本scope之外。

p=869未被同一论证排除：此时K中x还有0,r，y只留1，来自原cut qr的r→q detour虽长，但经0的宽松界仅给

    d_K(x,q)≥min(1+9,1+15,2+9)=10。

它不能提升为11；没有新增边的10步路线可能仍在。因此不能把p869机械套入p0/1结论。p869后续若被检查，须使用真实候选数据，不以本文宣称失败。

本paper只消费列出的旧事实，标记为before-seeing-new-numeric；不更改新数值owner的参数/结果，不登记一般常识为新独立方法，完成即停。

# 15552源的同步平移核为零，不能缩减K2端口对称

一次精确GF3消元得到 **rank=768、kernel dimension=0**。指定坐标下的全部
fiber-preserving纯平移只有恒等映射；648个实际freeport的轨道全部为singleton。
因此本次不能减少K2首pin选择，**不允许固定A0或固定任意一个freefiber**。
本批按范围停止，不继续一般自同构搜索或旧求解器。

## 与旧范围的区别

只读核对了15552 source-gap账本及
`d15_loop_completed_quotient_probe/affine_relation_recovery`、
`full_free_directions`、`full_inversion_port_cover`、`rank1_reflection_quotient`
等直接相关说明。已存结果包括：全部弧常数c=0给出的取负自同构、取负不变及
affine-line邻域族、二择rank1反射兼容失败。未见当前768未知同步平移核已计算。
旧文“translations are zero”指弧常数c，不是对h核作过判定。

本结果不否定已有取负自同构，也不声称全图自同构群平凡；范围仅为下述纯平移。

## 精确对象与方程

使用已literal绑定全部960弧、77760个arc-input邻集的
`source15552_AFFINE_RELATIONS.json`。原标签为 `81*u+x`，u=0..191；x的四个
低位优先三进制digit给F3^4坐标。完成的弧关系为

```
(u,x) -> (v, B_e x+c_e+t v_e)，t∈F3。
```

仅考虑 `τ_h(u,x)=(u,x+h_u)`，192个h各4坐标，不预先固定任何h_0或fiber。
该映射保留弧e的全部邻集，当且仅当

```
B_e h_u − h_v ∈ span(v_e)。
```

常数c消去；这里不要求B_e可逆。设p为v_e的非零pivot，每个i≠p加入

```
v_p (B_i h_u − h_v,i) − v_i (B_p h_u − h_v,p)=0。
```

三式独立表示模噪声直线的商条件。全960弧共2880行、768未知，自弧中from与to
对应同一变量时按模3累加，未覆盖或丢弃系数。

本次还核实每个controller的5个target bins互异。因此fiber-preserving映射不能
通过在同一个目标bin内交换不同弧而逃过这些条件。已绑定表在degree14顶点上补
虚拟自环才得完成关系；任意原图自同构保持度数，因而保持这类补环集合。反过来，
完成关系的顶点置换保持对角相等条件，删除虚拟自环后仍保原图。
所以该线性系统完整描述**这个固定fiber划分下的纯平移自同构群**，并非仅检验
某些示例平移。未扩展到controller置换或一般线性/仿射映射。

## 消元和实际端口轨道

程序以两个不交bit planes分别记录系数1、2；行乘2交换两planes，逐坐标模3
加法用其真值表实现。对全部768列做GF3 RREF，没有projective规范或人为anchor。
实际每列都有pivot，秩768，全部自由列为空，故核仅含零向量。

- 全192个fiber的核投影秩均为0。
- 最近已核的648个literal freeport分在24个fiber，每fiber27点。
- 这24个freefiber的投影秩同样全0。
- 实际端口轨道：**648个轨道，每个大小1**，并非传递。

一般若存在非平凡投影，点x的轨道会是x加该fiber的完整核投影子空间；不同fiber
的平移仍须来自同一个全局h，不能独立选择。本程序据此算法保存字面轨道，本次
自然退化为648个singleton。

A/B交换后可设A非空，再要求A包含某个轨道代表，是有保全理由的单个anchor OR。
但本次代表集就是全部648个原端口，所以该规则仍为原有非空条件，首pin选择
**648→648，减少0**。没有可用于本次K2模型的新对称约束。

## 文件与实际执行

- `INPUT_AND_EQUATIONS.json`：原relation/端口路径、全部2880行稀疏系数及弧绑定。
- `KERNEL_BASIS.json`：768个pivot、rank768、空自由列与空kernel basis。
- `FIBER_PROJECTIONS.json`：全部192个投影子空间及freefiber对应。
- `FREE_PORT_ORBITS.json`：全部648个端口的字面轨道与代表。
- `run_once.py`、`RESULT.json`、`TERMINAL.json`：完整实现、计时和停止边界。

实际PID **3633556**，exit **0**，单worker **0.671092911 CPU秒**，低于15秒预算。
只读既有relation和已绑定FREE_ORDER，literal源边表读取0、BFS0、图生成0、solver0。
未执行更广Aut筛选、未改变K2公式、未续旧timer，无待办数值步骤。

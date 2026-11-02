# K5普通提升的真实短路线与逐坐标商条件

## Target

固定存储的F3四维chart和K5的两对逆端口，寻找Q16电压普通提升的6480点、最大度12、直径≤4完整图。这里推导不丢弃真实解的商过滤条件；不把完整NB4充分证书当作实际直径必要条件。

## Status

COHERENT AS STATED。root与互补代理已静态核对以下必要性；实际唯一4096投影检验保留30项，其后全部122880个Q16完整赋值已实际检查并失败。必要链及实现又获实际Gemini静态审阅SOUND AS STATED，准确范围见reviews/ddp/k5_q16_actual_route_20261030.DISPOSITION.md。此文件未声称新的普适覆盖定理或Lean结论。

## Invariant Object

固定源(base a, deck identity, field coordinate 0)的真实闭四步可达集。每条长度0至4的原始端口词都参与，不删回退词。目标顶点三部分为(target base, deck group element, field coordinate)。

## Assumptions

K5由两个互补C5给四个端口，inv=(1,0,3,2)。M_p和v_p来自k5_q16_NB4_quotient_gate/BASE_INPUT.json，字面图关系为

    (a,g,x) — (b, g·q_ab, M_p x+t v_p)，t∈F3。

q_ba=q_ab的群逆，field关系的反向端口已用字面矩阵绑定。Q16的表示为r^i s^j，r^8=1，s²=r^4，srs^-1=r^-1；商Q16/<r²>同构V4，每个coset恰4个元素。图原本以这些关系确定，不借用旧6156点满度源的保边余度。

## Notation

端口词w的目标base记b_w，deck电压的signed chord自由词记f_w，零field源的完整终点集合记S_w。一个坐标集合以81位的真实位集表示；这不是产物哈希。相同(b_w,f_w)合并为key j，并令S_j为所有对应S_w的并。

## Derivation Strategy

先证明树规范保全实际图，再对原始field路线求准确像，仅对deck自由词约简，最后用四个deck目标必须被不同key提供的事实作必要过滤。

## Derivation Map

1. tree gauge改变deck标签，不改field或图距离。
2. field像用全部原始词递推，准确含短路与回退。
3. 相同自由词的deck值在任赋值下相同，field像只能求并，不能随deck词消去。
4. 同一V4 coset的每个field坐标需要四个不同deck目标，故至少四个不同key。
5. 遍历全部商赋值，保留者再展开完整群值，并检查全部真实点对。

## Main Derivation

### 树规范是同构重标记

右乘电压约定下，逐base取k_a并将g重标为gk_a。电压变为k_a^-1 q_ab k_b，field不变。取k_0=e、k_i=q_0i^-1，即将四条star树边规范为e。全部其余六条无向chord仍独立取Q16元素，反向取逆，因此16^6覆盖此固定生成规则全部实际同构类，允许重复，不丢真解。

### 341条原始词给真实闭四步像

空词有S_empty={0}。向原始词后附p时，准确递推

    S_(wp) = { M_p y+t v_p : y∈S_w, t∈F3 }。

因此全部1+4+16+64+256=341词之并恰为真实R4。回退可能改变field坐标，所以只在deck电压自由词中消去相邻反字母；field像始终先按原始词计算。即使两个原始词的矩阵乘积不同，零源合并仍可直接取其集合之并；对非零源则需分别加矩阵作用项，不能把本缓存统一平移。

### 逐坐标提供者不等式

给定六个V4 chord值，key j的投影值bar(f_j)已确定。固定target base b、coset c与field坐标x，该coset内有四个不同实际目标(b,g,x)。任意完整Q16赋值下，同一key j只有一个deck值f_j(q)，即使其field像由多条原始路线合并，它至多覆盖上述四点中的一个。因此实际R4覆盖全部图必须满足

    #{ j : b_j=b，bar(f_j)=c，x∈S_j } ≥ 4。

不同自由词可能在Q16中再相等，会使实际覆盖减少，不会使这一必要过滤误排。这不是充分条件，且不同目标不能独立挑选不同电压。

### 商条件与完整图验收分别进行

一项商赋值保留后，每个chord在对应4元coset中选择，得到4^6个完整群赋值。真实零源field像可再准确代入各key的群乘积，检查80个目标控制槽的81位并集。

此后仍须验证其他field源。deck左作用g↦hg是图的显式自同构，且不改base或field，故5×81=405个(base,deck identity,field x)轨道代表的实际depth4 BFS足以证明所有6480点对满足D≤4。只通过零源或五个零field根，不计完整构造。

## Actual Test and Changed Decision

唯一检验完成全部4096个V4赋值及五个零field源；每源341词合并为161个key。4066项由准确的逐坐标提供者不足反例排除，30项保留。全部失败见证记录其原赋值、源base、目标base、coset、field坐标和完整provider key编号，不只汇报总数。

PID4057841，实际0.647435435 CPU秒，单worker。0源边表读取、0BFS、0solver、0控制器或6480图生成。旧NB4证书0/4096结果仍按原范围保留，未覆盖成实际D4族无解。

该门使实际生成域由16^6=16777216缩为30×4^6=122880，而且全程保留实际D4目标的每个可能解。根因此直接检验了全部完整群赋值，不再要求全部控制点对都有NB4；122880项均在首根到自身base层的真实R4失败，见相邻k5_q16_actual_R4/TERMINAL.json及REPORT.md。由商必要条件加完整余域检验，整个固定K5/Q16/chart实际D4规则已排除，不换群、矩阵或基图续试。

## Boundaries and Non Claims

不排一般N(12,4)、其他基图/field chart、非普通提升或非Q16规则。本文通过的30项不是图，也不证明其中有一个可同时实现全部覆盖。若后续预算到界，未完成范围应保留UNKNOWN；不能把仅检查前缀当全部122880。

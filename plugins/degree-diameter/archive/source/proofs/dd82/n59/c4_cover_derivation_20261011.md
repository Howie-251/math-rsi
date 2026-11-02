# Derivation Package

## Target

排除四个具有2211匹配行的零三角形点组成非边重二关系四圈。

## Status

COHERENT AS STATED。完整证明为 `h5_zero_r2_c4_interface_20261011.md`。

## Invariant Object

同一真实图中四个私有点的三角形关联总量 $I_P=\sum_{p\in P}t(p)$。

## Assumptions

59点、最大度至多8、任意不同点有长至多二路径；只对四个指定零点假定2211匹配行。无需全体零点行型、全图 $t\le2$ 或任何 RAW。

## Notation

$X$ 为十二个二邻接点，$P$ 为四个私有点，$W$ 为三十九个不邻四零点的点。$d_X(w)=|N(w)\cap X|$，$h(w)=e(G[N(w)\cap P])$，$T_P$ 为内部私有三角形数。

## Derivation Strategy

先强制真实外部邻域类型，再把两步覆盖不足收费为私有三角形，用同一图的重复预算反证。

## Derivation Map

1. 四点匹配行推出 $X$ 独立、$X$–$P$ 无边、每个 $X$ 有六个 $W$ 邻点。
2. 两步覆盖强制 $G[P]$ 包含四圈，并给 $d_X(w)+h(w)\ge2$。
3. 求和与三角形关联给 $I_P\ge12+3T_P$。
4. 原图预算先给 $T_P=0$，再由私有四圈的对角非边给 $I_P\le8$。

## Main Derivation

Step 1（命题）：完整证明 Steps 1–5 从原图得到所述分解与边禁令，故 $\sum_Wd_X=12\cdot6=72$。

Step 2（命题）：$d_X\ge2$ 时收费成立；$d_X=1$ 时尚未覆盖的两个圈点需要相邻的两个私有点，故 $h\ge1$；$d_X=0$ 时四个私有点都须邻接，故 $h\ge4$。因此 $\sum_Wh\ge2\cdot39-72=6$。

Step 3（精确计数）：含私有边和一个 $W$ 点的三角形各贡献两次私有关联，私有内部三角形各贡献三次，两类不交。所以 $I_P\ge2\sum_Wh+3T_P\ge12+3T_P$。

Step 4（命题）：原图非边重复预算 $6-2t(v)\ge0$ 给 $I_P\le12$，所以 $T_P=0$，私有图只能为四圈。对角非边有至少两个公共邻点，消耗至少一份非边重复，故 $6-2t(p)\ge1$，整数性给 $t(p)\le2$。于是 $I_P\le8<12$，矛盾。

## Remarks and Interpretation

三十九个点的覆盖需求超过七十二条双覆盖外向边所能独立承担的范围；至少六份不足必须通过私有边三角形补偿，但私有点预算不足。

## Boundaries and Non-Claims

只关闭一个完整结构族；H5、n59及其他阶数未关闭。无新 RAW 或 Lean 定理。

## Open Risks

完整纸面证明待独立审阅与形式化；短精确枚举只是局部收费诊断。下一义务是其他重二路径/循环的真实外部共同实现。

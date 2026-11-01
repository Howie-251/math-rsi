# 全局重判案例：21点component DP何时该停

## 卡点与提案

m(5)≥36研究的A1来自21点、35条互异五边、paircover原H。以原边为顶点，Γ连接交集不为1的边。实际incidence矩阵给

    AAᵀ−J=A(I₂₁−J₂₁/25)Aᵀ，PSD，rank≤21。

按Γ分量，大小s的不同等重二进制行块有rank下界ρ(s)=1+ceil(log₂s)，总ρ≤21，孤立≤3。提案把这些rank数据和旧wedge界联合，期待比旧纯边数阈值图界更强。

设n₁为无序单交边对数，e=595−n₁为Γ边数。五组总s时最大跨组对数

    f(s)=[s²−(5−b)a²−b(a+1)²]/2，s=5a+b，
    g(q)=f(34−q)。

对s顶点m边任意simple graph，convex度数目标Σg(q)的最大值由isolated/universal递归

    U(s,m,r)=max(g(r)+U(s−1,m,r),
                 g(s−1+r)+U(s−1,m−s+1,r+1))

计算。新component松弛用各块U加总，并约束Σs=35、Σm=e、Σρ≤21、孤立≤3、非单点m≥s−1。

## 先证新松弛是否真强

对任何合法块集合，取其各自任意graph极值实现后不交并，得35顶点e边graph，所以component值≤U(35,e)。反过来当e≥34，单个名义块(s,m,ρ)=(35,e,7)已经合法，直接给U(35,e)。故整个新majorant对全部e≥34**恒等旧U(35,e)**。

当时25个保存aggregate有49≤e≤198，全部处于无收益范围。这个解析结论使得不必再跑其余24谱、LP乘子或更大component搜索。它没有证明A1可染；它证明这一种放松不能改进当前旧界。

## 可执行复放

原C++为固定pilot，stdout写出PILOT.json；独立Python读它作比较，再从头枚举n≤6全部33,867个simple graphs校验U定义并恢复35点literal极值图。从仓根建立副本：

```sh
PB_ARCHIVE="$PWD/plugins/propertyb/knowledge/archive"
PB_REPLAY=$(mktemp -d "${TMPDIR:-/tmp}/mathrsi-component-XXXXXX")
cp -R "$PB_ARCHIVE/context/propertyb35-paper/round01/middle/a1_rank_component_wedge_budget_20261020" "$PB_REPLAY/component"
clang++ -std=c++17 -O3 "$PB_REPLAY/component/PILOT.cpp" -o "$PB_REPLAY/component/PILOT" > "$PB_REPLAY/component/PILOT.json"
"$PB_REPLAY/component/PILOT" > "$PB_REPLAY/component/PILOT.json"
python3 -B "$PB_REPLAY/component/VERIFY.py"
```

C++仅向stdout输出JSON，上面的重定向把本次pilot写入副本的PILOT.json，随后独核读取它。若只复放Python，可以跳过clang/二进制两行，读取归档复制来的小PILOT.json；此时应说明只验证了已有pilot值。

预期n₁=519/e76，P_component=U(35,76)=13074；旧L2730456仍高于修复阈值2722720。独核保存全部76条边，Γ度34²/11/3⁹/2²³，实际连通无孤立，ρ预算7≤21。因此新增“optimizer connected”不能改变这个见证。

历史C++0.013279CPU秒、Python0.260139秒，总<0.3秒，预算20CPU未耗尽。这里停是数学上无收益，不是算力没用够。脚本输出`VERIFY.json`只认证graph递归与literal，不认证它能是实际H的Γ。

## 后继为何仍不能报整支完成

实际critical singleton core≥34诱导min5排除旧literal；但移五条叶边又得Γ度34/29/16/3⁹/2²³，P13002仍不够。后来真实principal Gram排两份literal：cover{0,1,25}外32个点给4I₃₂，rank>21。它说明保留实际Gram会更强，不代表所有scalar aggregate都已排除。

要重启这条路线，须增加大分量内部真实incidence/weighted Gram/共同附着容量，或者新原染色论证；不能只再跑相同size-only rank DP。来源：[原报告/停止证明](../../../knowledge/archive/context/propertyb35-paper/round01/middle/a1_rank_component_wedge_budget_20261020/REPORT.md)、[critical-core边界](../../../knowledge/archive/context/propertyb35-paper/round01/middle/a1_critical_core_singleton_degree_20261020/REPORT.md)、[真实Gram separator](../../../knowledge/archive/context/propertyb35-paper/round01/middle/a1_principal_rank_separator_20261020/PROOF.md)。

这个例子的交付是一个可复用停止定理与新的信息缺口，原36仍暂停、A1仍开放。局部条件工具有价值；不会将“没有变强”改写成“没有做成任何东西”，也不把局部CPU快速当成全题马上完成。

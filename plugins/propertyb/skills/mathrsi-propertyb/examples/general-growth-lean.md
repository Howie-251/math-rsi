# 一般 k 案例：相同 RS 最大预算接到全部 k≥12 的原染色

## 输入与目标

输入k≥12、任意有限顶点类型V、简单k元边集E。定义d=2^(k−1)，a_k(p)=1−(1−p)^k，J_k(p)=∫₀ᵖ(1−y²)^(k−1)dy，接受正整数M满足存在p∈[0,1]使

    M(M−1)J_k(p)/d² < a_k(p)^(M/d)。

B_RS(k)是**全部正整数**接受预算的最大元，不是有限数值扫描里最大的成功样点，也不是文献原本同名常数。Δ=floor(sqrt(B_RS)/(8(1+log k)))。已完成的主定理返回：边数≤B_RS+Δ时每条原边有true/false两色，Δ≥2，故m(k)≥B_RS+Δ+1。

这里没有把顶点数、paircover、Gram、团数、参数见证当外部前提；它们由证明内部构造。比较D/E是另行纸面结果，不属于本例Lean导出；k12逐项4664也不是本例直接求出的B_RS值。

## 关键公式调用怎样避免“换了问题”

取M₀=2^k、p=1/k：a_k(p)>3/5、J≤1/k，左侧<4/k≤1/3<9/25<a²，给非空接受集合。任意接受M≥2^k的同一见证p满足

    p>1/k²，J≥1/(2k²)，κ=M/d<2k，κ log a>−2log k。

于是全部接受M<k2^k，最大值存在且本身有严格正见证；无须假设接受集合下闭或连续最优值可达。Lean内部`rsBudget`用有限range过滤实现，但`rsBudget_characterization_twelve`证明其覆盖全部正整数的最大性，而不是把range作为额外公理。

对同一接受M，t=sqrt M、s=floor(t/[8(1+log k)])、N=M+s。实际单交图团界给r≤3t，且(2+2log k)s+2<M/r。对数扰动证明

    log[N²(1−1/r)/(M(M−1))] < s log(a)/d。

与同一p的接受不等式相乘得到加强实际判据，再经最小顶点商、真实单交图、真实重染失败空间，返回原E的Bool染色。先前k≥17版用了较强中间界；延到12…16时改用足够的r≤3t及sqrt M≥64，五个种子由精确有理幂核验，其余k复用旧引理。不是逐k搜索超图或对无限参数抽样。

规范推导：[ANALYTIC_EXTENSION](../../../knowledge/archive/context/propertyb-general/bridge-12-16-20261021/ANALYTIC_EXTENSION.md)；入口[Growth/Twelve.lean](../../../knowledge/archive/formal/Aris4Math/General/Growth/Twelve.lean)。

## 已存在的可执行核验

本指南不启动Lean；这是用户授权复现一般结果时的完整命令。归档不含elan/Mathlib缓存，先按固定`lean-toolchain`和`lake-manifest.json`准备Lean4.24.0/固定Mathlib，不能把缺环境说成数学失败。建立独立副本后运行，默认旧Main无效：

```sh
PB_ARCHIVE="$PWD/plugins/propertyb/knowledge/archive"
PB_REPLAY=$(mktemp -d "${TMPDIR:-/tmp}/mathrsi-growth-XXXXXX")
cp -R "$PB_ARCHIVE/formal" "$PB_REPLAY/formal"
cd "$PB_REPLAY/formal"
lake build Aris4Math.General.Growth.Twelve
lake env lean ReviewAuditGeneralGrowth12.lean
```

构建后审计源码[ReviewAuditGeneralGrowth12.lean](../../../knowledge/archive/formal/ReviewAuditGeneralGrowth12.lean)原样复述积分、全部正整数最大性、floor增益和裸Finite/Finset Bool两色，检查核心定义/类型和传递公理。预期核心六导出与两个原题声明仅`propext`、`Classical.choice`、`Quot.sound`，没有sorryAx/新axiom/native_decide。只看编译exit0或标准三公理不足；必须同时确认结论不是`Certificate→PropertyB`或`P→P`。

历史正式构建2576 jobs、15.64秒，依赖大多已有缓存；构建后原题审计7.70秒。它是本机增量构建与独立导入，非从零冷构建/第二台复现，更不能估新的理论形式化时长。[历史核验报告](../../../knowledge/archive/context/propertyb-general/bridge-12-16-20261021/lean/REPORT.md)。

若一般主定理的类型有额外外部证书或缺最大性，暂停成果升级并修相应桥；若只有tactic/API错误，用固定库查实际声明/真实caller，别重写理论。变更严格积分/最大元定义/参数范围才需要重新检查负重数学；只改未展开的注释、排版不需重新审无限域。

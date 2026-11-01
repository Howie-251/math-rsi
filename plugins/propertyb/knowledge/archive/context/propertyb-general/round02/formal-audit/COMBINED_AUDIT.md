# 主定理与有限比较：合并审计范围

**PASS，same-family / provisional。** 该文件合并两份范围明确的数学审计，不改变原 `PROOF_AUDIT.*` 的结论或源范围。

对全部整数 k≥17，原三源证明得到

\[
m(k)\ge B_{\rm RS}(k)+1+
\left\lfloor\frac{\sqrt{B_{\rm RS}(k)}}{8(1+\log k)}\right\rfloor.
\]

对 k≥32，清洁源明确五项参考包络满足 L_ref=B_RS+1，其中 B_lin、B_cont、B_pair 均不超过 B_RS，GR 一般 min–max 式满足 \(L_{\rm GR}(k)\le2^k\le B_{\rm RS}(k)\)。对 k≥256，所定义的零锁必要数据松弛方案不接受任何 M>B_RS；γ=M(M−1) 的 Grill 连续式也不能接受这样的 M。

因此在统一尾范围 **k≥256**，主定理的真实全超图可染预算 B_RS+s（s≥1）严格超过 B_RS、上述 GR 数值所给的预算，以及**这个明确松弛方案**的可接受预算上界。前两者是对明确数学下界的数值比较，第三者是对指定松弛证书方案的限制；不能将第三者改写成针对全部实际 H 或所有 Grill 方法的能力定理。

## 依赖 DAG 及证据

```text
原 CORE / UNIFORM / CLIQUE 三源
  └─ PROOF_AUDIT.json：18单位、78微义务、PASS（same-family/provisional）
       ├─ B_RS存在、严格见证、2^k≤B_RS<k2^k
       └─ 对任意有限简单H的预算B_RS+s染色定理（k≥17）

SOURCES_FINAL §2–3 + Grill源式(3)–(5)
  └─ GR定义、取整、L_GR≤2^k（k≥32）

REPORT §2–5.1 + Grill源式(8)、两条γ公式
  ├─ 所列松弛数据及Λ下界
  ├─ 真正离散式的统一下比较
  ├─ FKG严格间隙 + κ≤3k的位置误差控制
  └─ κ≥3k独立控制
       └─ 每个M>B_RS均不通过指定松弛（k≥256）

Grill连续式(6)/(7) + FKG端项≤线性端项
  └─ γ=M(M−1)连续式接受预算不超过B_RS

以上数学节点
  └─ BASELINE_ADDENDUM.json：研究报告18单位+清洁源10单位、PASS，准确限定范围
       └─ 本合并的k≥256有限比较结论
```

无循环：B_RS 先由旧判据独立定义和证明存在，主定理及比较均引用它；不通过见证没有参与主定理的超图存在性证明。新增松弛比较不要求也未调用实际 H 实现性。

## 未纳入本结论的事项

当前最新文献全包络、历史归属/优先权、书目全面核验、指定跨家族终稿认可、最终 HTML 与 Goal 完成由 root 负责。本合并审计不宣称这些事项已完成。清洁源 `proofs/propertyb-general/BASELINE_COMPARISON.md` 全部349行、10个单位已补验，并纳入本次数学范围；新增明确数据域、行上限、偶性、度<M及五项参考包络均通过定向核查。

本目录原审计文件未修改；本次仅新增 `BASELINE_ADDENDUM.md/json` 与 `COMBINED_AUDIT.md/json`。

父代理随后对 `UNIFORM_INTEGER_GAIN.md` 证明一作一处解释性改写：明确先从被积函数下界得到 J≥1/(2k²)，再代入式(3)推出 a^κ 下界。本 reviewer 已定向读取修改段；公式、范围及证明依赖不变，原审计 UNIFORM-02.05 已明确核销同一推导，所以没有新增数学义务。原审计文件未改。父代理告知的 Grok 成功结果没有被用于本同家族审计的数学判定，也没有扩张其已审范围。

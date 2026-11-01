# Argus 对本项目的适用性

这是一份历史阶段记录，其中的未完成证明状态已被最终交付取代。2026-10-07 的源码深读、实际 checker 测试及技能吸收情况见 [Argus 深读](ARGUS_DEEP_DIVE_20261007.md)和[两项目综合说明](MATH_AGENT_HARNESS_SYNTHESIS.md)。

2026-10-06。核验GitHub main提交 `9cfe9129fd90511c3a1865844ec7dfda1b5d1008`（2026-09-30），读取数学文档、实际Lean检查器、公理审计器和proof ledger assessment源码。未安装或运行Argus；不是性能或完整系统验收。

结论：适合借用证据与义务管理，不能据其工作流文档推断它能解决本题剩余组合引理。我们继续ARIS＋现有Lean工程，暂不迁移调度。

## 直接采用

1. **证明有效性与命题忠实度分开。** 编译通过证明的是实际Lean类型；还需逐项核对FORMAL_SPEC的对象、量词与结论。现已安排Grok只看形式源码盲回译，之后让Gemini对照原规格。每个模块进度保留其输入和仍未消除的前提。[数学工作流 §4.1](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/docs/research-mathematics.md)
2. **完成引理列表不等于完成目标。** 必须有实际形式证明把这些义务连接到原T。当前SmallVertices已证明T↔F，只消除了约化义务；F本身仍待证。[实际route assessment](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/proof_ledger/assessment.py)
3. **证据必须对应实际检查对象。** 已编译并交付的模块冻结，变更后重新检查受影响的命题及依赖；原始审阅意见、失败调用、root纠正分别留存。模型判断不升级为kernel证据。复用现有ARIS记录，不再并行建立第二套状态库。

## 实际能力与边界

`lean_check.py`调用Lean或`lake env lean`，检查缺口、执行环境审计、保存实际返回。它是检查/编排能力；所读代码不提供本题的排列计数、块分类证明或专门的自动定理求证库。[检查器源码](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/tools/lean_check.py)

公理审计源码也已读，但没有在本机执行，不宣称其在本项目Lean4.24环境已通过。当前继续对实际定理执行Lean的`#print axioms`，检查传递依赖；不以文本无sorry替代内核依赖核对。[审计器源码](https://github.com/lbx154/Argus/blob/9cfe9129fd90511c3a1865844ec7dfda1b5d1008/argus/tools/lean_axiom_audit.lean)

Argus文档的独立Reviewer规则本身不证明跨模型家族。我们仍按用户要求使用Grok和Gemini，并逐条核对其意见。其文档对引用证据的描述与当前assessment.py的CONFIRMED分支并非完全一致，因此不将文档当已测试实现契约。

HERO约束继续适用：不为采用框架添加无实际用途的哈希层、重复台账或更多安装。下一项有价值的行动仍是消除Lean中的实际数学前提。

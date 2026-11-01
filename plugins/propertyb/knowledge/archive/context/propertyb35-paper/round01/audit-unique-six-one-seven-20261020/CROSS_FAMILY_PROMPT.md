请对一个新完整数学分支做fresh adversarial proof audit。首轮新会话，无需读任何既有审阅结论，也不要借用其他模型赞同。cwd是 /Users/rfy_naiveai/Desktop/aris4math；只读本项目，不访问aris4math_v2，不运行Lean。

完整输入为 proofs/propertyb35/TWENTYONE_UNIQUE_SIX_ONE_SEVEN.md。请全文读取（约294行），逐节核查，不能只看摘要或最终表。这是21点/35互异五边/点对覆盖/最小度6/唯一六度且恰一七度的完整原超图染色命题，不是全m(5)≥36。主稿§11给数学进口的准确条件和源码入口；按必要范围读取原证明，核每个实际调用条件。无需重跑旧大型证书。你若未执行代码或未完整阅读某进口，应明确记录。

关键攻击点：原假设强迫A1角色是否完整；删星森林给n4≤8且保留barquad秩≤2是否循环；原H单翻/两翻事件的方向因子、共有middle的五容量；threshold凸度最大化的压缩证明；全部21615矩域如何覆盖任意实际H；qΓ≤1直接给原染色且无独立性假设；主子矩阵/原点度删1删2产生全部前缀的取整；固定最大度与独立频率DP真正覆盖放松域；25项恰只剩(n0..n4)=(33,523,0,31,8),tau=1；同H的n4=8→barquad三角形→tau≥3是否成立。DP只作数学界的有限整数递推，不生成超图，也不假定最优序列可实现。

对照最终源 SIMPLE_CHAIN_DP.cpp、SIMPLE_CHAIN_FREQUENCY_VERIFY.cpp、SCALAR_T_ONLY.py 和 SIMPLE_CHAIN_VERIFY.py，位于 context/propertyb35-paper/round01/middle/a1_independent_set_degree_prefix_20261020/。无需重复搜索布局；若只静态阅读请明确。主稿现在删掉旧Schur low19/13、T33/T34 critical-core、N34线性P上界的依赖；不要把未使用旧草案当主链前提。

HERO：只报告真实的数学问题与最小修正，不为了流程增加假想防御。输出：(1)实际完整阅读/部分阅读的文件和章节、是否运行程序；(2)逐MAIN-THEOREM和MAIN-1..11覆盖简表；(3)关键疑点/反例尝试及结论；(4)若存在错误给可核对推导、影响和最小修正；(5)最终判定，准确区分新整支与未证的全36。多模型一致本身不构成证明。

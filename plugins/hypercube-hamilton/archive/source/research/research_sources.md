# ARIS 与 OpenAI 信息论论文核查

核查日期：2026-10-31。此文记录选题依据，不声称完成证明验证。

## 1. ARIS

官方项目为 [Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)，对应 [技术报告 arXiv:2605.03042](https://arxiv.org/abs/2605.03042)。核心是执行者推进研究、独立模型审查，并将论断逐项对应到原始证据。它是研究工作流程，不是保证解决开放问题的数学算法。

## 2. 最直接的可迁移论文：family 119

官方 [目录](https://raw.githubusercontent.com/openai/math/main/CONTENTS.md) 的 119 族包含：

- [Sharp binary-information contraction on the discrete cube](https://github.com/openai/math/blob/main/preprints/Sharp-binary-information-contraction-on-the-discrete-cube-September-24-2026/main.pdf)。目录描述的方法包含局部拼接的三点最优化、两种熵容量、共同输出稀释不等式、维数归纳及噪声半群积分。
- [Hellinger contraction with arbitrary Boolean output bias](https://github.com/openai/math/blob/main/preprints/Hellinger-contraction-with-arbitrary-Boolean-output-bias-September-24-2026/main.pdf)。目录描述非对称维数归纳、噪声半群能量估计及精确算术证书。

已读取官方 [形式化范围说明](https://raw.githubusercontent.com/openai/math/main/lean/docs/119.md)、[目标陈述](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/SoftChannel204.lean) 和 [实现入口](https://raw.githubusercontent.com/openai/math/main/lean/OAI/InformationTheory/SoftChannel/Main.lean)。尚未下载并通读 PDF，也未运行 Lean。

目标陈述给出如下明确接口：设 ψ(r)=((1+r)ln(1+r)+(1-r)ln(1-r))/2，H(r)=ln2−ψ(r)，I(u)=H(Eu)−E H(u)。对均匀离散立方体上的 u∈[-1,1]，其二元随机输出信息收缩目标为

I(Tρu) ≤ ψ(|ρ| ψ⁻¹(I(u)))。

布尔输出的均值 m 进一步给出上界 ψ(|ρ|ψ⁻¹(H(m)))；在 0<|m|<1 且 |ρ|>0 时严格优于无偏坐标基准。

注意：ComparatorChallenges 中的 sorry 是比较器目标占位，不能据此宣称实际证明含缺口。[比较器配置](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/SoftChannel204.json) 指向 OAI.InformationTheory.SoftChannel.Main，许可公理为 propext、Quot.sound、Classical.choice。实际入口使用其他模块的定理完成 fullMain；未编译全部依赖，不能写成“本次已通过机器核验”。

## 3. 可用但尚未解决的多比特目标

[Mahdavifar–Beirami, arXiv:2609.26444v2](https://arxiv.org/abs/2609.26444) 摘要明确提出：对 2≤k≤7，k 比特量化是否总满足 I(Q(X);Y)≤k(1−h₂(p))。作者报告 k≥8 有缩短 Hamming 码反例，2 至 7 比特只获得结构化搜索和 Monte Carlo 支持。

建议先固定 k=2，再限定低维或结构化量化器，寻找完整证书或反例。这里“建议”是选题推断，不是论文原结论。不能把二元信息收缩直接对输出位求和：链式法则需要条件互信息，条件化后的输入通常不再是均匀乘积测度。这是关键证明障碍。

## 4. 可靠性边界

[OpenAI 官方 README](https://github.com/openai/math) 当前列出 721 篇、373 族，并称集合为不同验证阶段的原始研究数据。首发 722 不是当前固定总数。选题应记录依赖版本，逐项复核使用的引理。以上核查只是有针对性的目录和形式化接口阅读，不是完整审阅全部论文。

## 5. 选题的对抗检查

两比特命题必须明确：X 在 {0,1}^n 上均匀，Y 为独立 BSC(p) 噪声后的向量，Q 为至多四标签的确定量化器，目标为 I(Q(X);Y)≤2(1−h₂(p))，0≤p≤1/2。二元定理不自动推出该命题。

不能将等号唯一性设为固定坐标投影。n=3 时 Q=(X₁, X₂ if X₁=0 else X₃) 已是反例：Q 均匀四标签，H(Q)=2；条件链式法则给出 H(Q|Y)=H(X₁|Y)+H(Q₂|X₁,Y)=2h₂(p)，所以它也达到坐标基准。此计算可直接逐步检查，不依赖 OpenAI 的新结果。

主执行者报告 n=3 的 2795 个无标号至多四块划分在 12 个 p 网格上均未发现超出约 5e-16 的违例。划分计数正确：S(8,1)+S(8,2)+S(8,3)+S(8,4)=1+127+966+1701。这里没有重跑实验；有限浮点网格不是全参数证明，约 5e-16 应按舍入误差处理。

建议：原题 C7 可先争取显式构造下界的小幅改善；若强调复用 family 119 的理论工具，可先攻两比特 n=3 的全噪声参数证书，再判断能否推广。两者均属于候选研究任务，尚无新颖性或成功保证。跨模型 Kimi 审查连接失败，不能记作审查通过。

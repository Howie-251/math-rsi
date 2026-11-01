from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
p=ROOT/'proofs/propertyb33/PROOF_PACKAGE_DRAFT.md'
s=p.read_text()
s=s[s.index('## 1.'):]
s='# 至多 33 条五元边均可二染色\n\n**定理：任意有限简单五元超图，只要边数至多 33，就具有 Property B。因此 $m(5)\\ge34$。** 本文给出完整数学推导，配套 Lean 主定理、原题复述审计与精确局部数据。\n\n'+s
s=s.replace('二十三点的完整候选数学分支均已给出。','二十三点的六个数学分支均已闭合。')
s=s.replace('如果第 5–11 节所有数学与数值义务按上述合同核验，七个点数分支与第 2 节归约即推出原始 T33，且不会留下点对覆盖、顶点数、度数、局部表归属、坏槽或概率界作为顶层假设。完成状态仍以稿首和下一节的实际构建范围为准。','第 5–11 节的结构覆盖、实际计数连接和严格有理界分别给出全部七个点数分支。结合第 2 节的无损归约，得到原始 T33：任意有限简单五元超图，只要边数至多三十三，就存在合法二染色。点对覆盖、顶点数、度数、局部表归属、坏槽和概率界均已在证明内部建立。')
s=s.replace('## 13. Lean 对应、复现入口与验收边界','## 13. Lean 形式证明与复现')
s=s.replace('预定最终公开接口位于新的','公开接口位于')
s=s.replace('截至本稿起草，最终源码的存在不等于完成指定构建。尤其不能用默认 `lake build`（默认构建旧 T32）证明新的 T33。','`formal/ReviewAudit33.lean` 另以任意 `[Finite V]` 和裸 `Finset (Finset V)` 复述原题，证明每条边同时含有真、假两色。该文件实际调用上述主定理，不需要任何内部结构或证书前提。')
a=s.index('### 13.3 已核验证据与待完成项');b=s.index('### 13.4 复现命令与数据定位',a)
s=s[:a]+'''### 13.3 原题审计与逻辑基础

完整主定理与独立原题导入已经通过。原对象定义是有限五元子集组成的边集，结论是每边真色点数介于一与四；独立导入同时证明了每边两色均出现的字面表述。点数、度数和分类条件均未进入原主定理的假设。

主定理、原 Bool 染色表述、不可染超图至少三十四边，以及独立原题复述等八项顶层声明的传递公理均只有 `propext`、`Classical.choice`、`Quot.sound`。没有 `sorryAx`、新增未证公理或 `native_decide` 依赖。内核中的有限计算只处理已证明覆盖的局部类型、标签运输和精确有理数公式。

实际命令、退出码、导出类型和公理输出保存在 `context/propertyb33/round02/final-assembly/`。完整核验地图见 `context/propertyb33/FORMAL_VERIFICATION.md`。这是本机的构建与独立导入记录；独立导入是原命题的另一种表达和调用，不是另一个人已经复现，也不是第二份独立数学证明。

'''+s[b:]
s=s.replace('这条命令是**新目标的最终复现入口**，本稿不把待执行的构建写成已成功。各分支可分别显式构建；例如已执行并通过的四低分支为：','默认 `lake build` 仍指向旧 T32，因此这里显式指定新主模块。随后运行原题审计：\n\n```sh\nlake env lean ReviewAudit33.lean\n```\n\n各分支也可单独构建；例如四低分支为：')
a=s.index('## 14. 本稿的验收边界')
s=s[:a]+'''## 14. 方法来源与结论范围

随机排列与贪心染色的路线已有文献基础，参见 András Pluhár, *Greedy Colorings of Uniform Hypergraphs*（2009），以及 Karl Grill、Daniel Linzmayer, *Improved Lower Bounds for Property B*（arXiv:2403.05674v3）。锁定低度点、按精确迹计数和控制临界边对也是已有的方法方向。本文重新证明实际使用的计数与覆盖引理，并将三十三边所需的结构选择、完整局部分类和真实删除连接到同一原命题。

本文结论为 $m(5)\\ge34$，没有证明 $m(5)=34$。形式证明依赖所列 Lean 标准逻辑基础与工具链；模型审阅和候选反例搜索是辅助查错证据。数学证明本身是从任意原始超图到合法染色的全称论证。

- [Grill–Linzmayer 原文](https://arxiv.org/html/2403.05674v3)
- [Pluhár 原文入口](https://doi.org/10.1002/rsa.20267)
'''
(ROOT/'proofs/propertyb33/PROOF_PACKAGE.md').write_text(s)
print(len(s.splitlines()),len(s))

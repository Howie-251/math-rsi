# 六方向匹配延拓：先行研究与新颖性边界

日期：2026-10-31。状态：文献核查与证明义务比较；没有认证其他论文所有证明。目标是删除六方向结果中的额外结构限制，不能把已有受限结果重新命名为新定理。

## 1. 两篇近似标题的论文必须分开

**Wang–Wang 2024**：Shujia Wang, Fan Wang, *A kind of matchings extend to Hamiltonian cycles in hypercubes*, RAIRO Operations Research 58, 5237–5254, DOI 10.1051/ro/2024210。原文摘要及 Theorem 3.2 是 n≥6、至多五方向、|M|<10·2^(n−5) 的圈延拓。不是六方向论文。

来源：[出版社 PDF](https://www.rairo-ro.org/articles/ro/pdf/2024/06/ro230630.pdf)。用户 Fink–Hotmar PDF Theorem 3 引用同一成果，维数写 n≥5；边界差异不影响本轮 d=6 主目标，但引用时以原始定理原文为准。

**Ali 等 2025**：Abid Ali, Weihua Yang, Gohar Ali, Ioan-Lucian Popa, Dilara Akter Mitu, *Kinds of Matchings Extending to Hamiltonian Cycles in Hypercube Networks*, Symmetry 17(7), 995, DOI 10.3390/sym17070995，2025-06-24 发布。

该文 Theorem 12 声称 Q6 的距离3受限匹配可延拓为圈，Theorem 13 声称把同类结论推广到所有 n≥3 的至多六方向匹配。附加条件原句为 “does not cover every two vertices at a distance of 3”。[出版社正文](https://www.mdpi.com/2073-8994/17/7/995)

## 2. 距离3条件存在量词解释风险

不能直接把上述英文改写为“只要匹配不是完美的”或“存在一对距离3点没有同时被覆盖”。正文同时声称此条件推出 |M|<2^(n−2)，并在 Q5 引理中推出某方向至多1条匹配边。这些推断与上述弱存在解释不相容。

直接反查：从 Q6 任一单方向完美匹配删去一条边，得到31边匹配。它不是完美匹配，也有距离3点对未被同时覆盖，但31不小于16。因此，“存在一个未同时覆盖的距离3点对”不能据该文文字作为已审计的定理条件。作者可能意指每一距离3点对都不能同时饱和，即任意已覆盖顶点之间不存在距离3；这比弱存在解释强得多。本次尚未取得无歧义的正式定义来认证该解释。

结论：把此文作为**已有带额外距离3限制的六方向声称**登记，不能据摘要宣称无条件六方向问题已经解决，也不能直接把含糊条件加入自动筛选。原文的量词和中间界需要专项审计。此处指出的是解释与推导义务，并未给出定理反例。

## 3. 本地 Fink–Hotmar 的准确突破义务

本地来源：E:/新问题/2501.19029v1.pdf；提取文本 research/six_directions/paper.txt。

Conjecture 2 的 P_d 命题：任取 Q_d 中匹配 M，任取异奇偶顶点 u,v，若 u 不被 M 覆盖，则存在包含全部 M 的 Hamilton u–v 路径。

Theorem 5：对 n≥d≥2，P_d 蕴含 Q_n 中任何至多 d 方向匹配均能延拓为 Hamilton 圈。正文还用 Observation 14 将 P_d 推到 Q_d 圈版本。

因此当前最干净的新目标是 **P6**，而不只是“Q6 所有匹配有圈”。P6 自动排除了完美匹配，但包含最多31条边的匹配；端点 v 可以被 M 覆盖。以 u=0 固定后，立方体自同构只把 v 的奇数距离分类为1、3、5，不能把这三类混为一种。

P6 的验证完成后还应把 Theorem 5 的拼接构造重新审计，输出严格区分“有限基例已证”与“所有维数推广已证”的证明链。只证明许多实例或全部小匹配都不够。

## 4. 新近文献线索，不能作为未经核验的剪枝规则

发现 *On Extension of Matchings to Hamiltonian Cycles in 6-Cubes*, Abid Ali, Gohar Ali, Weihua Yang, DOI 10.1142/S0219265925500227。期刊目录登记 Journal of Interconnection Networks 26(4), 2550022 (2026)。摘要转录声称 Q6 所有≤20边匹配可延拓为圈。出版社页面本次403，尚未读到出版社全文，因此**20边阈值仅作为待核查文献线索，不计入已验证先行定理**。[出版社 DOI](https://doi.org/10.1142/S0219265925500227)

还发现同作者 *Extending Matchings to Gray Codes in Hypercubes with Prescribed Endpoints*, DOI 10.1142/S0129626426500040，以及 *Extending the Size of Matchings to Hamiltonian Cycles in Hypercubes*, DOI 10.1142/S0219265925500215。仅获取书目/摘要转录，不据此改变 P6 的量词或称已解决。

有可访问原始预印本 *Hamiltonian paths extending a set of matchings in hypercubes*，Ali–Ba–Yang，arXiv:2506.21432，对小规模匹配研究端点路径。摘要的端点障碍措辞须结合全文，不能直接把“任意端点”理解为允许 uv∈M。[原始预印本](https://arxiv.org/abs/2506.21432)

## 5. 本轮计算与声称的执行边界

- 无条件“至多六方向”与距离3受限六方向有明确区分，本轮目标前者。
- 不能用仅有 Hamilton 圈的先行结果替代 P6 端点路径实例。
- 先前推荐中的“六方向是自然下一步”需要补充上述受限先行研究；仍未找到无条件六方向或完整 P6 的可核验已发表证明。
- 若计算声称穷尽，必须记录枚举覆盖范围、对称归约正确性、可独立检查的路径证书和未解决实例；随机正例只提供试探证据。

## 6. 2026-11-01：P6 完成后的准确价值边界

再次核对 Fink–Hotmar 原始 arXiv 页面（https://arxiv.org/abs/2501.19029）、本地全文的 Conjecture 2 / Theorem 5，以及 Symmetry 17(7),995 出版社全文。已经能确认的比较是：前者给出无额外匹配结构限制的至多五方向结果，并提供 P_d 到任意维数至多 d 方向圈延拓的条件推论；后者的六方向结论仍附有距离3条件。

所以，若完整 P6 获得严格证明，则经已经展开的拼接链推出所有 n>=6 的无额外结构限制的六方向圈延拓；同时得到 Q6 中任意自由起点到任意异奇偶终点的匹配延拓。这是两个量词清楚的结果，不能仅说验证一个64顶点实例。它仍不覆盖一般 Q_n 中使用七个或更多方向的匹配，因而不是完整 Ruskey–Savage 猜想的解决。

本轮对两个 World Scientific DOI 再次尝试访问，6-Cubes 页仍403，指定端点页未取到正文；第三方摘要线索继续只作线索，不升级为已核验定理。定向检索没有找到可核验的完整 P6 或无条件六方向证明，但“没有检索到”不等于穷尽查新，不据此保证首创或期刊级别。

当前 P6 未证。完整证明、准确文献比较、独立审查共同决定最终成果价值；已证局部引理和随机证书不能代替这一完成条件。

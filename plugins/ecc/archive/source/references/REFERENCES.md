# 文献输入、定位和使用范围

以下输入均针对二元线性码。`[n,k,d]` 在本包按实际最小距离恰 d 解读；需要 ≥d 时使用已证明的归一化或 Griesmer 论证。

## E1：不存在 `[41,8,18]`

Iliya Bouyukliev, David B. Jaffe, V. Vavrek. **The smallest length of eight-dimensional binary linear codes with prescribed minimum distance.** *IEEE Transactions on Information Theory* 46(4), 1539–1544 (2000). [DOI: 10.1109/18.850690](https://doi.org/10.1109/18.850690)。

原研究实际核读的依据为 Bouyukliev 2008 年博士论文 §6.2.2，Theorem 6.3，印刷页 147 / PDF 第 149 页。这里的定理编号属于博士论文，不是 2000 年期刊原文编号。期刊正文未在本任务取得。主证明利用该结果和 `g₂(8,19)=42` 排除长度 41、维数 8、距离至少 18。

## E2：满支撑 `[40,7,18]` 至多 172 个坐标等价类

Iliya Bouyukliev, David B. Jaffe. **Optimal binary linear codes of dimension at most seven.** *Discrete Mathematics* 226(1–3), 51–70 (2001). [DOI: 10.1016/S0012-365X(00)00125-4](https://doi.org/10.1016/S0012-365X(00)00125-4)。

原研究实际定位：Bouyukliev 2008 年博士论文 Table 6.2，印刷页 158 / PDF 第 160 页。这里使用的是上述满支撑域中的分类上界；本包计算证明 172 个实际对象均合法且两两不等价，结合上界得到穷尽性。单独计算出 172 个对象并不能证明目录穷尽。

可公开访问的交叉来源：Stefka Bouyuklieva, Mariya Dzhumalieva-Stoeva. **Optimal Linear Codes and Their Hulls.** *Mathematics* 13(15), 2491 (2025). [正文与 DOI](https://doi.org/10.3390/math13152491)。§2（PDF 第 2 页）说明满支撑约定；§5（第 8 页）给出 172；Table A5（第 16 页）给出 hull 维数 1、3、5 对应 33、62、77。本包的实际矩阵也重算该分布。

## E3：不存在 `[41,14,14]`

Stefka Bouyuklieva, Iliya Bouyukliev. **Classification of Linear Codes by Extending Their Residuals.** *Mathematical Software—ICMS 2020*, LNCS 12097, 173–180 (2020). [DOI: 10.1007/978-3-030-52200-1_17](https://doi.org/10.1007/978-3-030-52200-1_17)；[公开全文](https://pmc.ncbi.nlm.nih.gov/articles/PMC7340893/)。

精确输入：Proposition 2，印刷页 179 / PDF 第 7 页，排除二元线性 `[41,14,14]`。本包第五项先从假想码构造 `[41,14,≥14]`，再把距离归一到恰 14，以符合输入。没有重新运行作者的分类或复证其全部引用链；按已发表定理整体引用。

## 其他来源与复用

Griesmer (1960) 的界在证明中另有完整推导。已知下界构造的具体生成矩阵、码字枚举程序随包提供，(44,10)、(44,11) 构造来源见 [Grassl 在线码表](https://www.codetables.de/)。联合论文的全部书目信息见 [references.bib](references.bib)。

外部论文 PDF 未在本包重发，避免给未核实的再分发许可作出承诺。上述精确命题、使用条件和来源定位已保留，可离线阅读本包归约；核查来源原文需访问所列文献。作者历史分类不属于本包声称重现的计算。

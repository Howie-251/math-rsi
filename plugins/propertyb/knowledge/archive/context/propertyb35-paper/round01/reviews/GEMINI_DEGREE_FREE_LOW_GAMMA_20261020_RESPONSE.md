### 1. 实际阅读与执行范围

* **执行范围**：本次为独立静态数学与代码审计（**未运行 Python/Lean，未借用任何既有审阅结论，未访问 `aris4math_v2`**）。全量整数算术与组合恒等式均已人工逐项手算核对。
* **完整全文阅读文件**：
  1. [TWENTYONE_TWENTYTWO_LOW_NONUNIT_DEGREE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_TWENTYTWO_LOW_NONUNIT_DEGREE_REPAIR.md)（全文 1–71 行）
  2. [CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/unique_six_two_three_seven_transfer_20261020/CHECK.py)（全文 1–46 行，重点核查第 28–40 行直接染色计数）
  3. [CHECK.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/middle/unique_six_two_three_seven_transfer_20261020/CHECK.json)（全文 1–446 行，重点核查第 416–443 行 `direct_repair` 输出）

---

### 2. 逐项对抗性核查与反例尝试

1. **量词、无隐藏前提与原 $H$ 返回**：
   * **核查**：命题仅要求 $n\in\{21,22\}$、35 条互异五元边、原边非单交图 $\Gamma$ 存在顶点 $F$ 满足 $q_\Gamma(F)\le 1$。全文未使用 $\delta(H)$、$\Delta(H)$、点对覆盖、临界性或特定度谱。
   * 在每一分支（§2、§3 的 $n=21$、§3 的 $n=22$、§4）中，均先根据固定原 $H$ 的结构确定 $F$ 内唯一红点 $v$（余四点蓝，使 $F$ 恒双色），再在固定外部均匀样本空间上对**其余全部 34 条原边**的单色坏事件求上界。坏样本总数严格小于样本空间总数 $D$（或 $D'$），故必存在至少一个样本使原 $H$ 全部 35 条边双色。
2. **$q_\Gamma(F)\le 1$ 的分情形完备性（$q_\Gamma(F)=0$ 与 $q_\Gamma(F)=1, j\in\{0,2,3,4\}$）**：
   * $q_\Gamma(F)=0$：其余 34 条边全与 $F$ 单交；
   * $q_\Gamma(F)=1$：唯一异常邻居 $G$ 与 $F$ 互异（排除 $j=5$）且在 $\Gamma$ 中相邻（排除 $j=1$），故 $j=|F\cap G|\in\{0,2,3,4\}$ 穷尽所有可能。
   * 当 $j\in\{2,3,4\}$ 时，“$\exists v\in F\cap G,\ d_H(v)\le 9$”（§3）与“$\forall u\in F\cap G,\ d_H(u)\ge 10$”（§4）互为逻辑补集，无遗漏。
3. **§1–§2 基础样本、孤立边与 $j=0$ 整数核查**：
   * 外部 $N=n-5$ 点均匀选 10 红：
     * $n=21\ (N=16)$：$D=\binom{16}{10}=8008$，红附着单交边外四点全红 $R=\binom{12}{6}=924$，蓝附着单交边外四点全蓝 $B=\binom{12}{10}=66$；
     * $n=22\ (N=17)$：$D=\binom{17}{10}=19448$，$R=\binom{13}{6}=1716$，$B=\binom{13}{10}=286$。
   * $q_\Gamma(F)=0$（$s=34, c\le\lfloor 34/5\rfloor=6$）：由 $R>B$，坏样本至多 $6R+28B$，分别为 $6(924)+28(66)=7392<8008$ 与 $6(1716)+28(286)=18304<19448$。
   * $q_\Gamma(F)=1, j=0$（$s=33, c\le\lfloor 33/5\rfloor=6$）：$G\subseteq V\setminus F$ 单色样本数为 $\binom{N-5}{5}+\binom{N-5}{10}$，分别为 $\binom{11}{5}+\binom{11}{10}=473$ 与 $\binom{12}{5}+\binom{12}{10}=858$；总坏样本至多 $6R+27B+\text{bad}(G)$，分别为 $5544+1782+473=7799<8008$ 与 $10296+7722+858=18876<19448$。
4. **§3 交核含 $\le 9$ 度点及 $n=22, c=7$ 的同一样本容斥扣除**：
   * 选 $v\in F\cap G$（$d_H(v)\le 9$）为 $F$ 内唯一红点。因 $|F\cap G|=j\ge 2$，$G$ 含红点 $v$ 及至少一个 $F\setminus\{v\}$ 中的蓝点，故 **$G$ 在所有样本下恒双色**。过 $v$ 的原边除 $F,G$ 外全为红附着单交边，故 $c=d_H(v)-2\le 7$。
   * $n=21$：改用外部 16 点选 9 红 7 蓝样本空间 $D'=\binom{16}{9}=11440$，此时 $R'=\binom{12}{5}=792, B'=\binom{12}{9}=220$，最坏 $c=7$ 给 $7(792)+26(220)=11264<11440$。
   * $n=22$：沿用外部 17 点选 10 红 7 蓝样本（$D=19448$）。$c\le 6$ 时 $6(1716)+27(286)=18018<19448$；$c=7$ 时裸 union 为 $7(1716)+26(286)=19448=D$。
   * **反例尝试（测试 $c=7$ 时能否使两红附着边共同坏样本 $<36$）**：任取 7 条红附着单交边中的两条 $E_1,E_2$，其外部四元集 $A_1=E_1\setminus\{v\}, A_2=E_2\setminus\{v\}\subseteq V\setminus F$ 满足 $u:=|A_1\cup A_2|\le 4+4=8$。在同一样本空间上，
     $$\mathbf{1}_{\bigcup_{i=1}^{33} Bad(E_i)} \le \mathbf{1}_{Bad(E_1)} + \mathbf{1}_{Bad(E_2)} - \mathbf{1}_{Bad(E_1)\cap Bad(E_2)} + \sum_{i=3}^{33}\mathbf{1}_{Bad(E_i)}$$
     逐样本成立。$E_1,E_2$ 同时单色当且仅当 $A_1\cup A_2$ 全红，样本数为 $\binom{17-u}{10-u}\ge \binom{17-8}{10-8}=\binom{9}{2}=36$。故总坏样本 $\le 19448-36=19412<19448$，无需 $A_1,A_2$ 不交或树扣除。
5. **§4 交核全 $\ge 10$ 度：仅用 $F$ 为叶的度和恒等式与六个严格界**：
   * **核查是否误用“$G$ 也为叶”**：恒等式
     $$\sum_{u\in F} d_H(u) = \sum_{E\in H}|F\cap E| = |F\cap F| + |F\cap G| + \sum_{E\notin\{F,G\}}|F\cap E| = 5 + j + 33 = 38 + j$$
     **仅使用 $F$ 与其余 33 条原边各交 1 点、与 $G$ 交 $j$ 点**，对 $G$ 与其他原边的交集大小无任何限制。
   * 当 $F\cap G$ 的 $j$ 个点均满足 $d_H(u)\ge 10$ 时，$\sum_{u\in F\setminus G} d_H(u) \le 38+j-10j = 38-9j$。由抽屉原理，$F\setminus G$（大小 $5-j\in\{3,2,1\}$）中必存在点 $v$ 满足：
     * $j=2$：$d_H(v)\le \lfloor 20/3\rfloor = 6$；
     * $j=3$：$d_H(v)\le \lfloor 11/2\rfloor = 5$；
     * $j=4$：$d_H(v)\le 2$。
   * 选 $v\in F\setminus G$ 为 $F$ 内唯一红点。因 $v\notin G$，过 $v$ 的原边除 $F$ 外全为红附着单交边，故 $c=d_H(v)-1$ 分别满足 $c\le 5,4,1$（且 $d_H(v)\ge 1\implies c\ge 0$）。
   * 此时 $G\cap F\subseteq F\setminus\{v\}$ 的 $j\ge 2$ 个点全为蓝，故 $G$ 不可能全红，仅当 $G\setminus F$ 的 $5-j$ 个外部点全蓝时 $G$ 单色。在外部 $N=n-5$ 点选 10 红样本中，10 个红点须避开 $G\setminus F$，坏样本数恰为 $\binom{(n-5)-(5-j)}{10}=\binom{n-10+j}{10}$。
   * 因 $R>B$，取 $c$ 的上界给出安全上界，六项手算复核如下：
     * $n=21, j=2, c\le 5$：$5(924)+28(66)+\binom{13}{10}=4620+1848+286=6754<8008$；
     * $n=21, j=3, c\le 4$：$4(924)+29(66)+\binom{14}{10}=3696+1914+1001=6611<8008$；
     * $n=21, j=4, c\le 1$：$1(924)+32(66)+\binom{15}{10}=924+2112+3003=6039<8008$；
     * $n=22, j=2, c\le 5$：$5(1716)+28(286)+\binom{14}{10}=8580+8008+1001=17589<19448$；
     * $n=22, j=3, c\le 4$：$4(1716)+29(286)+\binom{15}{10}=6864+8294+3003=18161<19448$；
     * $n=22, j=4, c\le 1$：$1(1716)+32(286)+\binom{16}{10}=1716+9152+8008=18876<19448$。

---

### 3. 审阅结论

* **问题报告**：**未发现任何数学错误、隐含假设或边界遗漏**。
* **最终判定**：**PASS**。[TWENTYONE_TWENTYTWO_LOW_NONUNIT_DEGREE_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/TWENTYONE_TWENTYTWO_LOW_NONUNIT_DEGREE_REPAIR.md) 给出了无点度/点对覆盖限制下 21 或 22 点 35 条互异五元边超图中“$\Gamma$ 存在度 $\le 1$ 节点 $\implies$ Property B”的完整严密证明。


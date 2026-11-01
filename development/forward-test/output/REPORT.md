# MathRSI 首版工作流实际试用结果

本次仅完成 INPUTS.md 的 A、B、C，使用小问题快车道。未启动 Goal、搜索、Lean、外部模型或额外研究；未修改技能或原研究项目。

## A：显式二元码构造——完成

**规格。** 构造一个 GF(2) 上长度 3、维数 2、最小距离至少 2 的线性码，并验证实际生成矩阵。

取

\[
G=\begin{pmatrix}1&1&0\\0&1&1\end{pmatrix}.
\]

**证明。** 矩阵为二元 2×3 矩阵。若其两行的线性组合为零，则第一坐标使第一系数为零，第三坐标使第二系数为零，故 GF(2) 行秩为 2。全部消息和码字如下，运算均在 GF(2) 中：

| 消息 u | 码字 uG | 重量 |
|---|---|---:|
| 00 | 000 | 0 |
| 10 | 110 | 2 |
| 01 | 011 | 2 |
| 11 | 101 | 2 |

因此全部三个非零消息的码字重量均为 2；线性码的任意两个不同码字之差为非零码字，所以最小距离恰为 2。这给出了二元 [3,2,2] 码，也满足要求的 [3,2,≥2]。证毕。

真正支撑结果的是上面的满秩证明与完整非零消息核查。日志“search finished，score=2”只描述生成器输出，不能单独替代这些验证。无需证明搜索完备或寻找更大参数。此处已直接穷尽四个消息，无需编程。

## B：全域排除交接判断——完成判断，原不存在性结论未获证明

**规格与已准许进口。** 固定题设母码 K 和共同表示，目标是不存在合格两行扩张。允许直接使用的引理是：每个合格扩张都产生不同的 a,b∈F，且 a+b∈F；本任务不补充任何关于 K 的数据。

按题设提供的日志，现有证据只建立：

\[
L\subseteq F,\qquad
\forall a,b\in L,\ a\ne b\Longrightarrow a+b\notin L.
\]

它排除了三个所需元素 a、b、a+b 全部位于 L 的情形。它**没有排除** a、b 位于 L 而 a+b 位于 F\L 的情形，也没有排除 a 或 b 本身不在 L 的情形。因此，即使保存成员合法、列表内部检查完整且精确，仍不能推出 F 中不存在所需配对，不能交付“K 不存在合格两行扩张”。这里引用的是输入给定的检查结论，本次没有实际列表或母码，未重跑这些检查。

**最值得继续的具体义务：解决合法陪集覆盖。** 在原来的同一共同表示下，证明 F⊆L（与已知 L⊆F 合起来即 F=L）。可先给出每个合法陪集的完整参数表示，证明所有合法陪集均进入该参数域，再完整检查未覆盖参数并核对合法性筛选不会误删。若完整生成发现新元素，则更新集合，并对最终完整 F 检查所有不同元素对的和是否属于 F；不要只重复验证现有 L 成员或再次扫描原 L 的配对。

一旦覆盖成立且完整配对排除成立，假设合格扩张存在，由已准许引理得到不同的 a,b∈F 且 a+b∈F，与配对排除矛盾，才能闭合原目标。覆盖可以由充分的数学论证或完整有限检查解决；不要求继续启发式搜集。若完整 F 出现这样的配对，必要条件仍可行，并不凭这个单向引理就证明实际扩张存在。

交接状态：已知列表内部的精确排除可复用；关键缺口是合法陪集全域覆盖；没有证据表明固定全域已穷尽。恢复应从覆盖义务开始，不为相同列表换种子或重复配对检查。

## C：所有非负整数的偶性——完成

**定理。** 对每个非负整数 n，n(n+1) 为偶数。

**证明。** 若 n=2q，则 n(n+1)=2[q(2q+1)]。若 n=2q+1，则 n(n+1)=2[(2q+1)(q+1)]。整数的两种奇偶情形穷尽所有非负整数，两式括号中均为整数，故结论成立；n=0 亦包含在第一种情形中。证毕。

研究记录处置：路线 B 已由此完整成稿并闭合原目标。路线 A 的无限域连接不再需要，由路线 B 替代，停止编写穷举程序。强化 C 为假：n=1 时 n(n+1)=2，不能被 4 整除；保留这个反例并关闭该强化，不把它当作原目标的剩余义务。无需 Lean、网页或模型审阅。

## 本次实际读取与执行范围

读取的五个文件：

- `base/skills/mathrsi-research/SKILL.md`
- `development/forward-test/INPUTS.md`
- `docs/WORKSPACE.md`
- `plugins/ecc/skills/mathrsi-ecc/SKILL.md`
- `base/skills/mathrsi-research/references/proof-evidence.md`

以上均相对于 `/Users/rfy_naiveai/Desktop/MathRSI/`。没有读取原项目资料、`development/context/`、审阅对话或其它作者笔记；未调用宿主 ARIS 技能，因为这些任务可直接闭环。

实际 shell 命令（均为读取；无计算脚本）：

```text
cat /Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/SKILL.md /Users/rfy_naiveai/Desktop/MathRSI/development/forward-test/INPUTS.md
cat /Users/rfy_naiveai/Desktop/MathRSI/base/docs/WORKSPACE.md
cat /Users/rfy_naiveai/Desktop/MathRSI/plugins/ecc/skills/mathrsi-ecc/SKILL.md /Users/rfy_naiveai/Desktop/MathRSI/base/skills/mathrsi-research/references/proof-evidence.md
cat /Users/rfy_naiveai/Desktop/MathRSI/docs/WORKSPACE.md
git -C /Users/rfy_naiveai/Desktop/MathRSI rev-parse HEAD
wc -l /Users/rfy_naiveai/Desktop/MathRSI/development/forward-test/output/REPORT.md
```

第一次读取 WORKSPACE 时手动解析相对路径错误，命令 exit 1；改读正确的 `docs/WORKSPACE.md` 后 exit 0，其余 cat 均 exit 0。版本查询 exit 128，仓库当时没有可解析的 HEAD，故不填写提交号；实际使用的是上述路径中的本地开发文件和 ECC 插件，没有提交。`wc` 确认报告已写入，exit 0。本报告由 `apply_patch` 写入，是本次唯一写入产物。

**实质阻碍：无。** 小问题快车道允许直接证明与完整小域核查，工作区说明允许单份文档，不需要制造额外状态文件。版本记录要求触发了一次无可解析 HEAD 的查询，但未阻断任何数学任务。B 的缺口来自输入证据不足，而非工作流要求。

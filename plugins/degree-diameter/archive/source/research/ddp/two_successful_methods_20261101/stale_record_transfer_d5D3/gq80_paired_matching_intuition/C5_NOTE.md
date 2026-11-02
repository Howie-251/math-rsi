# 实际 C5 接口成功绑定，但单侧容量障碍被推翻

新 action 成功：固定 seed 的第2个六-transvection product 找到一个实际 order5 symplectic A，核 A^5=I、A≠I、A^T J A=J。它在原有点与线 labels 上都分成8个5cycles，并实际保持缓存160条 incidence。没有重建或重验旧 field/GQ/D4；矩阵、两 permutations、全部 cycles 与字面输入路径在 `C5_ACTION_AND_BINDING.json`。

原1560变量/1080 exact covers 的 C5 压缩也实际完成。每侧16个同一奇数5orbit内的 edge blocks 都使每点度2，故不能作为匹配块；其余每侧140块，共280。每侧8个 orbit degree equations，共16。1080 far pairs 实际形成216个5orbits，每orbit的五个原 cover rows 折成完全相同的 block OR，逐项绑定通过。每侧保留44个 collinear/concurrent blocks，**没有**加 girth5、rectangle 或新的 route cuts。完整模型在 `C5_COMPRESSED_EXACT_MODEL.json`。

两侧分别完整枚举105种8-orbit配对、每配对5^4 shifts，实际各65625项。point matching 对全部216 clauses 的最大 distinct contribution 为114，line matching为113。两者之和为227≥216，所以“内部重复已使总容量不足”的预测被推翻；这不是 C5 可行性证明，更不是无解证明。

保存的两个**首个单侧 argmax**合并只覆盖158个 clauses，重复69个，遗漏58个。它们证明分别最大化两边不能保证路线互补，不能将158冒作全 joint optimum。本批没有遍历65625² joint pairs，也没有运行 solver。完整单侧枚举、coverage histograms、argmax实际matching edges、mask、重复与遗漏 rows 均已保留。

实际数据给出下一兼容性问题的严格必要门：完整命中必须有 point contribution≥103、line contribution≥102，而且两贡献 mask 的 overlap 只能为两覆盖数之和减216，至多11。当前两个 argmax overlap69远超这个上限，但没有排除其他配对；后续若 root 授权，应检验这类联合互补性，不能以减少遗漏数自动续算。本批不启动 joint join、新 solver 或新 action。

没有候选图写出，0 BFS、0 old geometry regeneration、0 solver。新进程0.350192658 CPU秒，新准备计0.25，继承读门1.100792823，累计1.700985481/10。`C5_TERMINAL.json` 是本批实际终态，全部数值已停止；readgate和旧五个UNKNOWN窗口保留历史，不被新容量结果改成NO。

# P7、一／二内部、至少27单迹的完整装配

## 装配命题

设H为24点、35条互异五元边的点对覆盖超图，最小度七，无全七度边，高点集P恰七点，内部边数I∈{1,2}。若n1≥27，则H具有Property B。

本稿完整装配九个整数库存；I2 $(0,2,3)$由补集覆盖与共享实际单迹度的解析证明补齐，不声称原三蓝加权或pair快捷接口全过。主代理已全文核查九种库存的完整覆盖及各准确子定理；新加权四库存和本稿最后解析分支的指定跨家族审阅分别记录。

## 完整整数分流

总度只盈余七，故P七点全八度、L十七点全七度；无全七度边使全部原边遇P。内部／非内部迹预算是

$$n_2+2n_3+3n_4=21-4I,\qquad
n_1=14+3I+n_3+2n_4.$$

令w=n3+2n4。由三／二迹非负消去得

$$n_3=w-2n_4\ge0,\qquad n_2=21-4I-2w+n_4\ge0.$$

所以2w−21+4I≤n4≤⌊w/2⌋，可行时3w≤42−8I。I1给w≤11、n1≤28；I2给w≤8、n1≤28。因此n1>28无整数库存。

`context/propertyb35-paper/round01/twentyfour/p7_one_two_new_gate_transfer_20261020/HIGH_SINGLETON_INVENTORIES.py/json`从n2/n3/n4各自完整有限范围直接三重循环，筛预算相等，独立输出全部54解（I1有33、I2有21），最大n1为28，n1≥27恰九解。没有先凭手列再只检查列中项目。其完整高单迹表及准确调用如下：

|n1|I|库存(n2,n3,n4)|完整实际子定理|
|---:|---:|---|---|
|27|1|(0,4,3)|[唯一内部四三迹规范](TWENTYFOUR_SEVEN_HIGH_ONE_INTERNAL_FOUR_TRIPLES.md)|
|27|1|(1,2,4)|[本目录统一oneJ定理](TWENTYFOUR_SEVEN_HIGH_ONE_PAIR_WEIGHTED.md)|
|27|1|(2,0,5)|[一／二内部蓝对计数规范](TWENTYFOUR_SEVEN_HIGH_ONE_TWO_INTERNAL_TRACE_SELECTION.md)，§2|
|27|2|(0,5,1)|[两内部五三迹规范](TWENTYFOUR_SEVEN_HIGH_TWO_INTERNAL_FIVE_TRIPLES.md)|
|27|2|(1,3,2)|[本目录统一oneJ定理](TWENTYFOUR_SEVEN_HIGH_ONE_PAIR_WEIGHTED.md)|
|27|2|(2,1,3)|[一／二内部蓝对计数规范](TWENTYFOUR_SEVEN_HIGH_ONE_TWO_INTERNAL_TRACE_SELECTION.md)，§2|
|28|1|(0,1,5)|[一／二内部蓝对计数规范](TWENTYFOUR_SEVEN_HIGH_ONE_TWO_INTERNAL_TRACE_SELECTION.md)，§3|
|28|2|(0,2,3)|[补集覆盖与共享单迹度解析修复](TWENTYFOUR_SEVEN_HIGH_TWO_INTERNAL_TWO_TRIPLES_THREE_QUADS.md)|
|28|2|(1,0,4)|[两内部四quad规范](TWENTYFOUR_SEVEN_HIGH_TWO_INTERNAL_PARTIAL.md)，四个四迹部分|

所有子定理共同前提恰是上述实际H前提，再加表中准确内部数和迹库存。它们不是仅有条件signed证书：各自证明实际源覆盖、选蓝、真实外部signed预算、修复门和原35边双色。因此对完整九种情况调用对应子定理便得到原H的Property B；无需在wrapper另建概率对象、复制正集或生成原H。

## 精确结论

对于本命题的P7一／二内部范围，可整体移除全部n1≥27，因而其余库存只须考虑n1≤26。已有纯二迹等独立闭合范围继续保留，不因本表重新打开。此结论不涉及其它P大小、点数或完整全局下界。

I2 $(0,2,3)$不能因手列遗漏被跳过：0+2·2+3·3=13，且20+2+2·3=28。这里先由完整整数程序列出九解，再以其独立解析修复作为真实进口补齐；原快捷选择的失败源仍在独立报告中保留，不改称其全域成功。

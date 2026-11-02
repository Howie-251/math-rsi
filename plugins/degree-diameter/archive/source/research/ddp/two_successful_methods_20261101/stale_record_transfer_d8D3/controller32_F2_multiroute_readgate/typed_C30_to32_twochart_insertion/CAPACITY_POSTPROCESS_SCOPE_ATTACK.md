# 两chart完整结果与下一branch容量门：只读scope检查

仅只读本目录RESULT.json/run.cpp和ALL_INSERTION_RESULTS.tsv表头、最前几行。没有重建controller、枚word或域、计算新DP/field/rank、运行图/BFS/solver。以下把已完成的两chart结论与尚待root执行的更大容量门分开。

## 已完成point程序的域与语义

raw循环A tails i<j，B tails k!=l ordered，合378450；新标签30/31按A关联冻结，B不排序以保关联。两次插入读取不同旧tail的值，随后从实际A/B排列生成逆，最后检查全32点无loop/四邻不同。所选同色边相邻或跨色共享旧端点没有被事前误删；只由最终simple条件拒绝。actual284310simple、94140reject，两个chart各检查全部284310。

packet用64bit打包8个source x、每x对应一个8bit endpoint mask；每步对每实际fiber状态取T_p*y与T_p*y+v_p，确是actualpoint union。zero/one/two步全部保留。三步虽只存36个reduced词，未导致本次NO漏路：被丢词含p,barp相邻controller回退，三步终点必是root邻点；代码对这些邻点先fullmask放行。ARC/R都具有已证明的fourarc packet p,q,barq全八点证书，所以这里既可安全放行，也不会丢非邻/对角坏cell的任何≤3路线。若以后换任意offset/chart，这个邻点放行不能未经证明沿用。

fullrank word packet为FULL可直接放行其实际controller端点；其余packet按controller端点OR后逐8bit source行查缺点。root顺序30,31,0..29；实际两chart所有simple参数均在30失败，31/旧根没有被当作已通过。实际全NO只关ARC/R，不凭R局部修021推其它chart失败或整体更优。ordinary图BFS/256graph0，与exactpoint计算不是同一计数。

## 新容量门必须ordinary walks，不借fourarc证书

固定一个已经保存为simple的C32，root r=30。令W_l(v)为该controller从r到v长度**恰l**的ordinary port-walk数，W_0(r)=1、其它0；递推对四个port邻点累加，不删除controller立即回退。所需上界为

`K(v)=sum_(l=0..3) 2^l * W_l(v)`。

对任一source fiber点x，一个固定长度l的controllerwalk每步至多两个fiber输出，因此最多2^l个实际终点。不同walk/系数可以碰撞，只会减少distinct targets，故真实≤3 reach(v)≤K(v)。若任一v有K(v)<8，该controller对所有遵守“每typed step最多2choices、每fiber8点”的规则都不能D3：包括edge-local、非线性、状态相关的规则；并不需要限定成ARC/R、affine或四global matrices。必要上界甚至放宽了反向/无向一致性，所以也覆盖所有满足这些一致性的子族。

3步controller回退在一般fiber规则里不保证回到同一个fiber点，旧point程序只凭fourarc特殊证书放行邻点；此新门不能据此删词/少计普通walk。必须含0步及所有0..3长度。也不能把K>=8当point coverage；它只是可能含大量碰撞的路线容量。

root给出的首simple tails[0,1,1,0]之30→4只有word03的说明，若按该已给word绑定，容量仅2²=4<8，与chart无关。本paper不另解码该controller或重新核其word集合；全域数字仍由root sole postprocess给实际绑定。

## 完备性与停止口径

下一门只读已存simple-tail行，域仍是同一284310个合法控制器；不重扫被拒的raw、旧pointmodel或chart。每个controller只要root30有一个不足target，就足以拒其全部2choices规则，不需假设controller VT或再查其它roots。

若全部simple参数都出现这种不足，结合既有插点族anchor/label关联的完备表示，可严格关闭**该特定C30→C32插边族上、固定8点fiber、每port最多2choices、只沿controller邻接的所有lift规则**。仍不排其它C32、不同插点/连接、每arc3choices或重新分配degree预算、其他fiber大小/一般256图。

若有capacity survivor，只记这个更大域的必要门PASS/UNKNOWN；既有ARC/R完整NO不改变，但不能把survivor称任意新chart或图可行。预算中断的行必须未测UNKNOWN，不外推全域。root所定新增postprocess cap4、原case cap30及旧费用保留，不重复point模型、不起第二窗口。

本文件只给scope论证；0新DP、controller解码、域枚举、点模型、图/BFS/field/solver/Lean/外审，完成即停。

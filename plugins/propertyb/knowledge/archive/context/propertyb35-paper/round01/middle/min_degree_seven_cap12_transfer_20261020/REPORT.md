# min7低超额cap12与τ容量迁移交付

原99谱中81谱在非B假设下可供给全点对共度至多4。旧cap13 scalar已排其中48谱，本批新增9个完整degree谱（ID13,24,26,28,42,45,48,51,94），合计57谱；仍24谱缺部分cap12 caller。精确数学正文见 [PROOF.md](PROOF.md)。本结论条件于原局部／scalar进口，以及调用者提供的一般 $\delta(\Gamma)\ge4$。18个唯一pair5谱完全未动。

## 完整实际caller

不新增局部门时，81谱仅9谱全部quad门已齐，其中6谱原scalar未过。补唯一小缺口selected $8^4$：10标签／3真D8轨道，原3四锁位置且quota0全部strict，max $25967/36465$；独立inclusive/Möbius生成相同10标签，原35索引63行重放通过。

此后27谱全部quad caller齐全：18旧strict，9谱需新算。$9,10^3$ 只在实际外七度池至少五时调用；$10^4$ 仅在S2（ID94）的九名外七度点、八名外九度点共享列定理下调用。没有把该定理迁到含八度点的新外池。

`PROJECTION.json` 保存81谱完整实际quad及每一门／缺口；`PROJECTION_INITIAL.json` 保存未补 $8^4$ 的范围。当前最终接口为 `TAU_SENSITIVE_READY_SCOPE.json`。

## 九谱完整结果

设 $\tau=\sum_{x<y}\binom{\lambda(x,y)-1}{2}$。非负项逐pair给：$\tau=0$ 时所有共度至多2；$\tau=1,2$ 时所有共度至多3。于是实际三交outer的四个cross pair给 $C_3\le8n_3$（$\tau=0$），实际四交outer的唯一exclusive pair给 $C_4\le2n_4$（$\tau=0$）、$C_4\le3n_4$（$\tau=1,2$）。其余情形使用已经实际证明的cap12和全paircap4。

| ID | 完整键数 | 最大 $2L$ | 小于5445440的余量 |
|---:|---:|---:|---:|
|13|82336|5416992|28448|
|24|82336|5417412|28028|
|26|83176|5424720|20720|
|28|83983|5427156|18284|
|42|82336|5417412|28028|
|45|83176|5424720|20720|
|48|83983|5427156|18284|
|51|84806|5434464|10976|
|94|86399|5444208|1232|

九谱752531键全strict。主算 `TAU_SENSITIVE_RESULT.json` 为1.063546 CPU秒；`TAU_SENSITIVE_VERIFY_RESULT.json` 独立 $n_1$ 参数化、degree关联前缀成本及容量分层式，完整域／最大值／空余键逐项相等，PASS为0.871529 CPU秒。

原固定cap12结果保持于 `RESULT.json`（9谱完整752531键、8谱strict、S2仅一个余键）及 `VERIFY_RESULT.json`。S2旧余键 $n=(27,525,2,36,5),\tau=0$ 的旧上界5448744已被实际τ容量排除。首完整谱profile0.156033、原主算1.073036、原独立核0.917728、新 $8^4$ 门0.009815 CPU秒；两批全部实际CPU小于5秒。

没有引入 $n_4$ 新上界、critical、prefix或新布局。余24谱共38种quad caller缺口均原样保留；含11/12/13点度的quad未扩表；新混合外八度池未算。没有证明全21点或36结论，无Lean／v2。确定性独立复核PASS；模型审阅独立性same-family/provisional，等待parent及指定外部范围验收。

复现命令（项目根）：

```sh
python3 context/propertyb35-paper/round01/middle/min_degree_seven_cap12_transfer_20261020/QUAD8888.py --all
python3 context/propertyb35-paper/round01/middle/min_degree_seven_cap12_transfer_20261020/TRANSFER.py
python3 context/propertyb35-paper/round01/middle/min_degree_seven_cap12_transfer_20261020/VERIFY.py
python3 context/propertyb35-paper/round01/middle/min_degree_seven_cap12_transfer_20261020/TAU_SENSITIVE.py
python3 context/propertyb35-paper/round01/middle/min_degree_seven_cap12_transfer_20261020/TAU_SENSITIVE_VERIFY.py
```

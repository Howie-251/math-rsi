# Baer13新邻域：完整生产42398，交付59例

新邻域类型明确为 **Baer PG2(F3) folded blocking set**：13个rawpoints折叠为11个mandatorypins，再加anchor41666，产生42398点/245889边完整图。不是完整Qline或旧删pin局部修补。source为此前完整生产接受的42397。

完整12邻集：`1928,2576,7337,8710,14217,14622,23929,30347,34888,35165,40153,41666`。11个mandatorypins的实际R4缺项9个，全是extras，core41356点全部覆盖；anchor41666补齐。实际currentdegree及一次selectednative wholeR4接受，所有旧边保留。

root仅从新完整边表独立核验新增root：simple/max12、到全部42398点最远5、0bad，CPU0.2963秒。旧旧距离由retainededges与已接受source归纳继承，未重复旧/allsourceBFS。故Dexact5、N(12,5)≥42398，parent已接受。该新机制只做了这一次必要新根核验。

## 固定410项终态

输入来自364个F3-center平面、各7560 Baer orbit成员的有限degree池；不是所有66430平面。按pins数10/11/12、pinslex、oldindex一遍，410项全访问：

- 初始12个10pin/cap2：首pool31继承root同base完整exactfail/Pcore证据（CPU0.059345另列），其余11个exact≤2失败。
- 105个11pin/cap1：1完整接受、89 exact无单anchor、15个被新degree阻塞。
- 293个12pin/cap0：262个extras未覆盖、31个degree阻塞；无重复selected检查。

总364项实际mandatory检查（含root首校准），全部core缺项0，Pcore得到全部实际检查支持；46degree阻塞项没有强行再算覆盖。0未知、0未试、0core反例。失败只针对各自当时source；较早失败没有在42398自动重试，不作Baer全族排除。

生产CPU16.311927秒，父进程及所有native child均计入；101次prepare、263次verify，其中1次是有anchor正项selectedverify，其余cap0或无anchor检查直接复用，不重复。没有MIP、互审、Lean或全源BFS。

## Literal交付

parent接受后仅append此一步：delivery现59例＝D12的42343..42398共56例＋D11三例。旧58literal逐项保持，lastallsource42377、reviewed38、完整Lean0不变。families.json新step保留13raw原ID/坐标、Baer orbitmask、F3-plane basis、folded11、anchor、actualR4与root新根证据。通用proof以actualR4＋旧边保留为准，旧Qline/subset规则不删。

一次generator edge-set dryrun完全MATCH，0缺/多/重复，未写旧图、未BFS，记录generator_dry_run.json。deliver.py可复现此次schema追加，delivery_update.json保存59例摘要；不写共享Wiki/HTML/root最终证明。P“410中至少1完整图”已命中，Pcore实查无反例。本批结束，不扩中心/样本或重试。

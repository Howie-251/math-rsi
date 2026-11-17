# 实际证据、解析证明与未执行准备的边界

2026-11-05。对应[本轮正文](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-common-private-family-and-cover-obstructions-20261105/PROOF.md>)。所有新解析为same-session、unreviewed/unaccepted，本轮不外审，不改接受范围；当前全模型工作链仍为40/49/75/76。

## 1. 证据分类

| 项目 | 实际状态 | 支持的范围 |
| --- | --- | --- |
| 旧Y25完整position census | Linux确定性核验成功 | 实际$M_R=61>50$反例，全部红五及每个位置已枚举 |
| 冻结$L_5+F(4,4)$校准 | 同一次Linux census核验成功 | 实际$M_R=49=2n-1$；不是前一见证 |
| 固定15点source反例 | Linux确定性核验成功 | 全部32768子集、packet、独立endpoint DP；源集确含红六 |
| 旧14点nested-gate query | 同一次Linux批次成功 | 该一个完整模型的1001组端点无命中，仅此范围 |
| §3.1–3.4一般$q\ge6$ source family | 本轮完整解析逐型证明 | 同会话、未独审；$q=6$另有上述已核实例，最大蓝5，不靠其外推 |
| §3.5增强source family | Root与数学agent完整解析逐型证明 | $q\ge5$、无$B_5$；$q=6$新757十五点表未Linux执行，不是旧十五点输入 |
| §4最新$3q-2$增强greedy family | Root与数学agent解析证明，文档忠实展开 | 无$B_5$；未新Linux执行，无新的16点科学结果 |
| 较早fixed16 kernel及旧24 addon | 准备完成，SSH前提失败，未执行 | 没有科学结果，solver/checker均0；输入不是§4最新表 |
| 随后full-greedy16及冻结附加输入 | 新目录准备完成，另一次preflight失败，未upload | 混合$Y/R$全蓝但$vRR$红的旧表；没有§4增强的$AER/uER$红规则，无科学结果 |
| 附录A三段serial族 | $q\ge6$、$3q-2$点完整解析 | 无$R_{q+1},B_6,\mathrm{weak}(q+1)$；仅反驳serial禁止候选，未执行 |
| 附录B源末同时坏族 | $q\ge6$、$4q-5$点完整解析 | 无$R_{q+1},B_5,\mathrm{weak}(q+1)$，$S/E$均有红$q$但$\tau=1$；未执行 |
| 附录C唯一源内红$q$不hit族 | $q\ge6$、$3q-2$点完整解析 | 源内唯一红$q$与另一红$q$不交，$\tau=2$；未执行 |
| 附录D二十点/三十点红join应用 | 旧产品定理的解析应用 | 757例$\tau_{R_6}=6,\nu=3$；767例$\tau_{R_6}=10,\nu=4$，打包数只限这些实例；未执行 |
| 附录E两张22点position表 | 完整递归颜色与六条路径的解析见证 | 766点态$t\le5,t+e\le7$及反向位置互斥失败；全局position总量仍开放；未执行 |
| 旧D12端点三角形 | 读取旧完整证明及全部红六 | 历史已知反例，不是本轮新构造 |

## 2. 完整position census原件

读取[原VERIFICATION](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_position_cover_census_20261105/VERIFICATION.md>)、[FILE_MANIFEST](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_position_cover_census_20261105/FILE_MANIFEST.json>)。权威科学运行在`/data/ktqiu_hdd/math_agent/tmp/n7_position_cover_census_20261105`，唯一`python3.12 -B census.py`调用exit0、科学stderr空，实际2.4196229041554034秒。没有SAT、随机抽样、重试或外审。

旧Y25完整结果：2300 triples、12650合法packet，全部长度2–6的实际有序子集连续与all-triples判据一致，最大红5/蓝4，同端和8，红五1197条，蓝五0条，位置层$[12,15,17,12,5]$。反例文件包含完整颜色、全部实际路径与逐位置见证，不依赖选定路径样本。校准的红五2506条与位置层$[5,11,11,11,11]$另有独立文件。

| 关键原件 | SHA256 |
| --- | --- |
| census.py | `67be2f348d5fadad0394513db194980ee75add0d71d5924710169a7168b04a29` |
| counterexample.json | `197945da7dc4d4d360e155e72b29c03c5e3e57f15f9af7d97f2ed8f72b043cfb` |
| result.json | `75e9de1cf9b271d0266ae9bb0eab68446a3557ddd231f5fefb92f44eb945995a` |
| census_bundle.tar.gz | `4f01854fca863fba7af595776ce706639be70dc81d0105f3b7a4843ebf2223fa` |

原报告记录16个绑定文件加188667-byte bundle全部与Linux哈希一致。其后计划的24点、旧R24定义、geometry11及through13没有在这次census扩展核验；快照存在不等于获得了它们的新结果。

## 3. 十五点完整source反例与旧14点附加查询

读取[原VERIFICATION](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_red_source_saturation_counter_20261105/VERIFICATION.md>)、[FILE_MANIFEST](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_red_source_saturation_counter_20261105/FILE_MANIFEST.json>)。唯一科学批次在权威Linux目录`/data/ktqiu_hdd/math_agent/tmp/n7_red_source_saturation_counter_20261105`运行`verify.py`，exit0、stderr空，实际0.3831651690416038秒。无SAT求解。

十五点实例检查全部455 triples、1365 packets、32768 subsets。两种单色路径判据逐子集一致，独立固定首点/末对DP与全部路径枚举的端点最大值相同。实际红六7条、蓝六0条，最大蓝5、最大同端和8。源集$S=\{0,1,2,3,4,9\}$，末集$\{9,14\}$，全部红六完整列表及每个source实际见证均保存。

旧14点附加查询重新完整核验全部16384 subsets、364 triples及1001 packets，实际红六14条、蓝四56条、蓝三125条；1001个$a<c<d<b$组无指定nested-gate组合。没有一般全类排除结论。

| 关键原件 | SHA256 |
| --- | --- |
| verify.py | `086faee9e6ccee8eb28d9d6061e129963a8d7b934eab7fc571b600831cc5bcdf` |
| fixture15_validation.json | `8f9cb88ed0e0064c091403769805f4dc86c09695c8738d0cd7c052fb8b8d6893` |
| source_roles.json | `890ff215ce8d67c08399f43eaa0bc76f492938527f68f080f520d5a2d562a006` |
| result.json | `676a1c9714869df874c029dd18b071c0e535b12c3c041bc4889ea0e69d9c4f93` |
| evidence_bundle.tar.gz | `f8e2e11748c848cc308cae225ce9e6ce4c9aab5117a493c9eb93e63c9aa2abba` |

原报告记录11个科学成员及26293-byte bundle全部与Linux哈希一致。一般$q$证明的量词来自正文逐型推导；这份实际运行只核$q=6$的第一family。

## 4. SSH失败与两份未执行16点输入的身份

读取[较早STATUS.md](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_greedy_private_kernel_20261105/STATUS.md>)及[EXPLICIT_INPUTS.md](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_greedy_private_kernel_20261105/EXPLICIT_INPUTS.md>)。这里准备的是**较早另一份16点表**：其$M$分为2点$E$与3点$F$，多项一$R$三元组另有颜色规则；不是正文§4的最新完整greedy family。不得把这份准备脚本称为新family已机核。

[初次preflight receipt](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_greedy_private_kernel_20261105/server_preflight.json>)为exit255、空stdout、remote connection closed，耗时5.1385117秒；[upload receipt](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_greedy_private_kernel_20261105/explicit_upload.json>)同为exit255。Root另外明确授权的一次[transport recovery preflight](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_greedy_private_kernel_20261105/server_preflight_recovery.json>)仍为exit255、connection closed、耗时5.1313693秒，之后没有第二次upload或科学调用。

没有证据证明fresh远程目录已创建。16点显式核验、旧24 addon和准备的kernel solver/main checker均未启动。不存在SAT、UNSAT、timeout或完整反例验证等科学结果，也没有Windows科学fallback。原receipt与输入保持不变；后续外部连通状态改变前不在此文档任务重试。

随后另有独立fresh目录[full-greedy STATUS](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_greedy_counter_20261105/STATUS.md>)与[冻结INPUTS](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_greedy_counter_20261105/INPUTS.md>)。该输入为$A=\{0,1,2,3\},u=4,E=\{5,6,7,8\},z=9,v=10,R=\{11,12,13,14,15\}$的旧full-greedy16：$Y$内部$s/t$表与正文相同，混合$Y/R$三元组全蓝，唯一例外$vRR$红。正文最新增强表另把$AER,uER$改红，**没有冻结进这份脚本，也没有执行**。该目录同时准备旧24点combined-position、旧25点蓝四position和冻结22点fixture查询，均没有结果。

Root另授权的一次新连接[full-greedy preflight receipt](<D:/科研/math agent/erdos-szekeres-sat-main/tmp/n7_full_greedy_counter_20261105/server_preflight.json>)实际exit255、stdout空、connection closed，耗时5.1481502秒；失败后没有upload，科学调用及solver调用均为0。此回执区别于上一目录的两次preflight和一次upload失败，不把它们合并成新科学尝试，更不把冻结旧表视为增强757表的验证。

## 5. 历史及验收边界

旧D12端点三角形引用旧2026-10-27原文与原模型，未重跑。旧报告内当时的容量数字、review可用性及运行状态都是历史，不覆盖当前项目约束或40/49/75/76工作链。

[APPENDIX.md](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-common-private-family-and-cover-obstructions-20261105/APPENDIX.md>)由Root及数学agent冻结推导转写，给出附录A–C完整构造、附录D所需$F(3,4),F(3,5)$因子的递归定义及实际不交路径与横截证明，以及附录E的$F(4,4)$核心、两种端点扩展与六条position见证。附录D调用[旧红join定理§2](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-757-766-structure-20261105/PROOF.md>)，是旧产品定理应用，不是新方法。旧十二点join的运行、坐标或证书不绑定这些新20/30点模型；旧或未执行22点fixture也不充当附录E的科学回执。所有附录新构造均未Linux执行，无新增SAT、checker、独立外审或接受结果。

本轮文档实施仅修改本fresh目录现用报告、附录及本目录文档检查页，不改旧reports、sealed运行或证据、生产编码、acceptance、taskmeta、Goal、git或wiki。Windows只读资料、写报告和核哈希；所有科学计算仍以Linux为目标。新解析证明不因完整有限见证核验而自动接受；本轮没有独立外审。

本轮各数学agent已完成局部任务，无在途数学worker；原目标仍未完成。正文§6及恢复页记录的clique-source饱和匹配排除仍是开放义务，既无证明也无反例；$|S|=15$且源域含红六的条件分支不能扩写为全40点排除，$|S|=16$分支同样没有净收益。40/49/75/76及既有接受范围保持。

此前本目录文档实施在Windows重新计算manifest列出的SHA256及bytes：position目录17项（16文件及bundle）、source目录12项（11成员及bundle）全部PASS，缺失或不匹配为0。随后新增文档的链接、空白及身份检查另见[DOCUMENT_CHECK.md](<D:/科研/math agent/erdos-szekeres-sat-main/reports/n7-common-private-family-and-cover-obstructions-20261105/DOCUMENT_CHECK.md>)；这些只核文件身份及文档链接，不是新科学运行。

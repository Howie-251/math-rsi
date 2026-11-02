# Legacy DDP Wiki回填范围

已只读覆盖任务开始时列出的全部87个非`ddp-wave*`聚合的现有DDP实验节点，生成`legacy_rows.json`。稳定关联键为原Wiki node_id/path，供root复用canonical helper；没有改Wiki、graph或index。6个wave聚合节点明确排除，留给近期回填。某些非聚合的2026-10-27条目可能也在近期材料中，应按既有id/path合并，不能另建节点。

结构化值：73行有明确n，53行有明确actualD，43行有单个明确坏对数，16行带多候选variants。一次有限源metadata补齐读取了53行的JSON字段及报告前60行，补齐47行target；目标某维为空由53行降为6行，剩余6行全部是真多target聚合：

- 六个固定仿射参数比较；
- 124/172两shared-slope底图；
- 930点11/12度容量；
- 多组coset towers及Z98容量证明；
- 五张已知baseline；
- 585复制上界对degree10/11/12。

这些行的target/savedL按variants分别给出，不给整行硬套一个degree。所有其他81行都有明确target；其中5个controller行的target描述控制器必要条件，并另列intended_final_target=(12,3)和保存810门槛，不将控制图的n/actualD冒充最终lift结果。普通单target行共76行可直接关联27格保存baseline。savedL来自现有registry快照并保留日期，不宣称刷新主表。

未从actualD反推target，未从标题数字猜参数。补值逐项保留metadata字段或报告行证据，完整读取摘要在`legacy_metadata_reading.json`。源报告明确AGL8塔为8320点，已补齐n；其生产评分best与仅预检独立验算的图分在variants，避免把预检结果当成最佳候选验收。

所有87行完整保留原Metrics/Reasoning/provenance/duration/idea_id和Wiki路径；distance_text逐字等于原Metrics。原文bad/badpairs未明确方向时，count_type保持未明确；代表根缺失、BB缺口、A³零元、真实坏对和理论下界不互相换算。已验完整图、必要容量排除、有界profile失败、未认证SAT-UNSAT、已知baseline复现分开标记；原始scope文字完整保留。

另有10行附已存在后续Wiki的scope更新链接，包括816整群闭合、930十一度余支、循环F64余支、nonfaithful p17/p29；旧“open/unexecuted”不再是自动重跑许可。没有明确重启条件的行仍留null并保留原Reasoning，未制造新授权。

没有读取暂停dd82条目，没有重跑BFS/搜索，没有读取原始源码去强填数值，没有新建Wiki节点。补齐至此停止，root统一写ledger和canonical experiment helper。

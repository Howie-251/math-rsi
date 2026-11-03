# 完整 joint cover：该实际 C5 子族无解

“两侧采用更互补的匹配可补齐216far-orbits”的正向预测被实际完整检索推翻。原各侧65625个匹配仅从保存 TSV 读取，没有重枚举。根据已完整证明的单侧 maxP=114、maxQ=113，Pcoverage<103 或 Qcoverage<102 不可能形成216的 union，所以分别严格剪掉54856个 P、50427个 Q，保留10769个 P、15198个 Q。

对全部15198个合格 Q，实际建立216个 membership bitsets。对每个合格 P，依次 AND 它所有尚缺 orbit 对应的 Q membership；每一步都精确保留同时覆盖已检查所有缺口的 Q。全部10769个 P 最终 Q 候选集为空，共执行78098次 AND，无未查P。`JOINT_ALL_P_STAGES.tsv` 保存全部65625个 P 的 prune/query 状态与逐步 missingbit/Q survivor counts；`JOINT_Q_MEMBERSHIP.json` 保存实际 Q position→旧matchingindex映射及全部216个 bitsets，可直接从旧 Q TSV 恢复该证据。

完整性来自：任何 full union 的 pair 必先通过两个容量门；其 Q 必属于 P 每个缺口的 membership，因此属于本次求得的交集。交集为空严格排除该 P 的全部 Q，而不是只试一个搭档。故本次隐式完整判定65625²=4306640625个 matching pairs，没有显式4.3b逐对循环、随机抽样或 solver。0命中、0候选图、0 source/candidate BFS。

数学含义与先前容量结果不同：单侧最大贡献114+113=227确实没有耗尽总容量，但实际满足匹配与 C5 结构的覆盖 masks 无法互补成216。它说明这项新对称生成规则的真实联合兼容性失败，不能将原 five UNKNOWN 改写成 unrestricted GQ80 无解。

严格关闭范围是已保存 actual order5 symplectic A 的完整 C5-equivariant point/line paired-matchings 子族，含本次保留的 collinear/concurrent blocks。未据此排任意无对称 paired matchings、其他不等价 action 或一般(5,3)图，不自动换action/timer。后续若要用群论扩张作用的归属范围，应另作纸面论证，不能冒作本次新数值范围。

唯一原 session21056 已actual exit0。新进程1.321034614 CPU秒，新增准备计0.25，继承1.700985481，累计3.272020095/10；`JOINT_TERMINAL.json` 全部终态，数值停止。

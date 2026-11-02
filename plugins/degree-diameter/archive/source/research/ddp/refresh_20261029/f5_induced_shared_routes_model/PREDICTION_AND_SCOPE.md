# 新共享路线保留模型：事前范围

本批引入旧模型未直接编码的 external-edge 五条路共中间点必要条件，
不是恢复旧求解器计时。旧 300221 变量、1170873 子句的 base 只读。
当前只执行一个小型独立支持检查并准备增强 CNF/runner；主模型 solver 不启动。

先用不同于 NextClosure 的算法攻击已保存大 proper 支持的完整性：
30 个支持布尔量满足全部 258 有序词的 endpoint⇒两个 middle Horn 条件，
支持大小至少 16 且不是 full30，再逐一禁止已经枚出的全部 6 个精确支持。
一次 CaDiCaL 调用，整个小检查不超过 3 CPU 秒，无 proof log。
SAT 则立即报告新支持、停止全30非空 cut；raw UNSAT 只作为反例攻击通过，
其本身不冒严格完备性证明。主证据仍是 NextClosure 完备性推导及24575闭集
枚举、三种16支持的投影距离反例，以及三种19支持的匹配密度上界1875。

增强路线范围固定为 60 个有向 external 控制边、每边其它三个端口、每个
源 fiber 的125个 w，共22500组。L为q-source五点线去w，Y=N_p(w)，Z=N_q(w)。
每组加入 `keep(w) OR -OR(L) OR -OR(Y)` 和 `OR(Z) OR -OR(L) OR -OR(Y)`。
恢复旧 OR5/OR25 flag 的原顺序及变量编号，不重建原门；新增 OR4 全部 iff 绑定。
预计新增15000 flags、120000子句。全30支持门确认后另加30条OR125，
预计完整315221变量、1290903子句。

仅读现有邻接缓存，不重读源边表、不做新 BFS/图。主求解仅留待审阅后授权：
一批 solver 累计120 CPU 秒、全部150 CPU 秒、最多4次调用，首窗口60秒；
只有 SAT 真反例才可再调用，first UNKNOWN/raw UNSAT即停。
RLIMIT取窗口+1并预留2秒收尾，观察超时只继续等同PID，不 kill/restart。

# 共享路线增强模型已准备，主求解未启动

实际生成 **315221 变量、1290903 子句**，主 prepare CPU **0.509188752 秒**。
原 `f5_induced_retention_closure/model.cnf` 的 body 只读复制，无原门重建。

| 新增部分 | 变量 | 子句 |
|---|---:|---:|
| 15000 个 OR4 精确 iff 绑定 | 15000 | 75000 |
| 22500 组共享中间点/另一中间点存在条件 | 0 | 45000 |
| 每个控制 fiber 非空 | 0 | 30 |

旧 OR 缓存按原 saved word 顺序、z 升序、先 L 后 P 恢复。闭包前最后变量
296231，恢复后的最后变量300221；3000个OR5、990个OR25全部恢复。
旧字面反例的两 flag **296262、296263** 与旧 MODEL 精确相符。
新增 Y/Z 的所有 OR5 都复用原编号，L 为 source五点线去 w，不错误保留 w。

新增路线仅用于60个无共同控制邻点的有向 external 弧、q≠p：

`keep(w) ∨ ¬O_L ∨ ¬O_Y`，`O_Z ∨ ¬O_L ∨ ¬O_Y`。

`RESTORED_OR_FLAGS.json`、`NEW_OR4_FLAGS.json` 保存精确集合到变量映射；
`SHARED_ROUTE_GROUPS.jsonl` 保存全部22500组及其flag编号，增量CNF为
`shared_routes.added.cnf`。MODEL含指定(0→20,p1,q0,w0)例的完整L/Y/Z和两子句。

## 支持必要条件的独立攻击

小型30支持SAT模型要求原258词的 endpoint⇒两个middle、support≥16、
proper，并禁止已有6个大proper支持的每个完整30位assignment。
唯一调用得到 **RAW_UNSAT**：solver CPU0.01138秒，总0.024678254秒。
该结果只是不同算法未找到漏支持，不是proof log认证的完备性证明。

30个非空fiber hardcuts的主依据是原NextClosure完备性推导与24575个闭支持
完整枚举；仅6个proper支持足够容纳1921点，其中三个16支持被投影距离4
反例排除，三个19支持各有四条不共端点的密度125边，故总点数≤1875。
父代理和degree5代理已纸面确认密度推导。旧PROJECTION_RESULT中的false字段
描述当时仅用投影门的状态，不代表加入后续密度论证后的结论。

## 待审 runner

`run_cegis.py` 复用已核完整候选检查器 `check_induced.cpp`：未编译、未启动。
主批solver累计120 CPU秒，总150 CPU秒（计入本次prepare和小支持攻击），
最多4次调用。首窗口60秒，每次按剩余额度预留2秒；solver RLIMIT为窗口+1。
观察超时仅增加计数并继续等同PID，不能kill/restart，也不丢弃后来实际SAT。
首次UNKNOWN或RAW_UNSAT停止；只有SAT候选的真实缺对才追加精确全二/三步路线cuts。

候选保留至少1921点、实际最大度≤16；若有唯一>1920连通分量，可验其全部根
直接接受。否则原检查边界不变：最多128个字面反例，不把它当全图坏对数。
HIT只导出一张完整诱导图，最终独立验收仍由父代理完成。

本批主solver调用 **0**，新候选/BFS **0**。小支持检查的唯一调用与未来主批
明确分账；既有失败图、旧15秒窗口都没有重跑。

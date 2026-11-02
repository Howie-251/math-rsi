# 确切组合CNF的LRAT认证通过

终态：**LRAT_VERIFIED_UNSAT_EXACT_CNF**。

输入为父目录原样 `model.cnf`：**333551变量、2316695子句**，50142680 bytes。
本批未改变任何CNF literal、模型参数或父目录旧RAW_UNSAT终态。

唯一带证书求解命令：

```text
.tools/lean-4.24.0-linux/bin/cadical -q -t 120 --lrat <exact model.cnf> certificate.lrat
```

CaDiCaL 2.1.2，PID1790221，返回码20，实际 **61.394400 CPU秒**。
12次观察窗口结束后均继续等待同PID，没有终止或重启。
保存的二进制LRAT证书 `certificate.lrat` 为53841287 bytes。

唯一独立检查命令：

```text
.tools/dd82-lrat-check/lrat-trim-rel-0.2.0/lrat-trim <exact model.cnf> certificate.lrat
```

lrat-trim 0.2.0，PID1807056，返回码 **20**，输出 **`s VERIFIED`**，
实际 **0.587518 CPU秒**。显式提供同一CNF，检查器不是只做无CNF的证明修剪；
该返回码和状态表示空子句推导已被接受。

认证子批总 **62.004199912 CPU秒**；加旧批后whole为 **119.899128932秒**，
solver合计 **115.800517秒**，均在授权上限内。没有第二次求解或检查重试。

完整命令、PID、计时、返回码见 `solver.RESULT.json`、`checker.RESULT.json`；
输入记录和预算见 `INPUT_AND_BUDGET.json`，统一终态见 `RESULT.json` / `TERMINAL.json`。
原始输出保存在 `solver.stdout` / `checker.stdout`。

**结论边界：此处独立认证的是这份CNF不可满足。** H65、各路线约束以及
任意目标诱导图到CNF模型的保全性是另一个数学审阅责任，不能由LRAT检查
本身替代。本批没有生成图、执行图BFS或完成新的Lean图论定理。

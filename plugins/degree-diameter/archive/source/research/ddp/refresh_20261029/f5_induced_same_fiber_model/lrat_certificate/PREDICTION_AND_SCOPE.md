# 唯一LRAT认证子批

输入是父目录当前 `model.cnf`，header 为333551变量、2316695子句，
50142680 bytes。只读取这份确切CNF，不修改literal、参数、旧MODEL或旧终态。
旧运行一次54.406117 solver CPU秒返回RAW_UNSAT；旧批whole CPU为57.894923521秒。

本次唯一带证书复现命令为本机CaDiCaL 2.1.2：

`cadical -q -t 120 --lrat ../model.cnf certificate.lrat`

使用其默认二进制LRAT格式；CPU硬上限121秒。仅在实际返回20且证书存在时，
调用本机lrat-trim 0.2.0：

`lrat-trim ../model.cnf certificate.lrat`

已读取本地README与--help：提供CNF会启用证明检查；成功导出空子句时
返回20并输出`s VERIFIED`，返回0而未得空子句不算UNSAT认证。
checker最多90 CPU秒。认证子批总≤220 CPU秒；与旧批相加≤360 whole、
solver合计≤300 CPU秒。所有命令、PID、真实CPU/返回码保留。

预测证书可完成并被独立checker接受；这是待测预测。观察超时仅继续等待
同PID，不kill/restart。任何失败、UNKNOWN、超预算或证书不接受都立即收束，
不第二次重试，数学证据仍只保留原RAW_UNSAT。

成功仅认证这份CNF不可满足。H65、路线编码及从图对象到CNF的数学保全
另行审阅，不借本证书替代它们。零图构造/BFS，不安装、不生成摘要值。

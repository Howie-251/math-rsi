# 唯一F7/C60实例已完整生成

实际图：**20580点、360150边、简单无向35正则，完整路线证书给直径恰3**。

边表为`graph_d35_D3_n20580.edges`；字面参数为PARAMETERS.json；确定性生成器为generate.py；全部3600控制层pair证书及六chart/96turn证书分别为CONTROLLER_ROUTE_CERTIFICATE.json与LOCAL_CHART_CERTIFICATE.json。自含证明在PROOF.md。

此次先验证唯一明确F7局部规则与作者C60，随后生成唯一完整图。没有矩阵/域/controller搜索，没有旧1620或3750复验。局部门0.040972556CPU秒、完整生成0.348461891CPU秒，合0.389434447CPU秒。所有进程已终态。

真正改变是把四port/F5的互补三点推广为五port/F7互补四点；奇数port所需matching符号不能使用单一全局自逆矩阵，实际采用定向T4/T4^-1。C60来自已保存Bhakar作者配方，原F3 chart与旧coplanar方向被新conic方向完全替换。

未执行的C30+matching弱提案没有运行。新图生产检查不是独立验收；独立新图检查由根代理安排。根已读到PolarStar家族在degree35的一个13272点实例，但这不是当前全球最佳上界或完整调查；本报告不称新全球纪录。具体Lean尚未启动。

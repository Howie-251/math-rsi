# 全组完整目标K2执行审阅

Root已读prepare_native.cpp、MODEL_CODE、INPUT、SELECTOR_MAP及恢复后的MODEL。全部3589组按原exact覆盖等价关系保留，每侧≤13仍用forward prefix阈值；3480cap1 mutex、109cap2可共享。每个94186目标的两条覆盖条件都直接表达，只合并234个exact-key重复行。侧0(A:R4,B:R3)、侧1(A:R3,B:R4)与实际写出变量位号一致。原生CNF成功后仅元数据文件重名导致driver失败；已有CNF未重建/修改，一次流式统计恢复的header100492/385396及literal129971928保存。

本次恢复全部合法组并一次给全部目标，是移除旧391 LP支撑限制及稀行限制的对照。不能把上次391 UNKNOWN外推整数全域，不能把本次UNKNOWN视作不可能。

唯一窗口300秒、CPU硬301、max1call；whole charge420。准备初始driver selfCPU缺失，所以预算按完整90CPU准备额度保守预留，并另报可测CPU下界，不伪造精确总数。观察超时只等同PID。SAT须按完整57word支持全验双侧94186目标、cap与pin数，再重建字面A/B供root独立新根验收；solver文本不算新图。

UNKNOWN立即本批停；若rawUNSAT也先按未认证结果记，不自动追加证明工作或把一般14度图排除。旧所有终态和CNF原位保留。

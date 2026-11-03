# 固定 K5/Q16/F3^4 的真实 R4 门

预测：旧 full-NB4 证书失败不自动阻止短路线和回退路线共同覆盖；本次精确检验固定图规则，尚不预测存在完整合格图。

固定 BASE_INPUT 为相邻 k5_q16_NB4_quotient_gate/BASE_INPUT.json，四 chart/噪声向量、真逆端口、两个定向 C5 均继承。Q16 元素 i+8j 表示 r^i s^j；乘积 (i,j)(k,l)=(i+(-1)^j k+4jl mod8,j xor l)。star 四边为 identity，六 chord 按 (12,13,14,23,24,34) 任取16值；完整树规范域 16^6=16777216，不额外商自同构或缩放。

先对源 (base0,deck e,field0) 的全部长度0..4原始端口词（341条）分别计算真实 field 像，之后只约简 deck signed word。相同 (target base, freely reduced chord word) 合并 field 像 OR，不删除回退噪声。

新 actual-provider 必要门：每 V4 投影、每 target base/coset/field x，至少4个不同合并 key 能提供该 x。每 key 在实际 deck 只给一个元素，所以不足4严格阻断该投影的全部4096 lifts。此门不是旧 full-NB4 商门。Root已接管 k5_actual_route_provider_gate 中全部5个零坐标根的4096门；本目录不重复实现或运行该门，只消费其实际 pass/cache。若其0pass，本目录未启动的全搜索立即取消。

真实 root0 R4 通过后构造6480点实际邻接，先检查其他 base 的field0，再检查全部405个 (base,deck e,field x) 根；deck左乘是显式自同构，故这些根覆盖全部6480根。首次完整PASS保存图/80点controller/电压并停。root0通过不称图合法。失败保存实际反例后继续同一完整域；预算到保留精确游标、不重启、不排未检查前缀外。

更新：Root actual-provider门实际30/4096通过（0.647435435CPU），剩余122880电压赋值；预算由180收紧为整体≤90CPU。本轮只prepare并按root新授权做一次首projection/全零lift digits的真实邻接root0校准，未启动范围枚举。以后唯一调用含准备编译、root既有provider费、lift检查及405根验收；留2秒收束。没有solver/随机seed/其他group或controller。旧V4 full-NB4失败不用于删列。

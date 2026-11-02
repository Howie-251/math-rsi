# 自然364源两corecuts＋端口matching＋新星：整个规则NO

## 问题及预测

原10000个随机matching/cut配置全失败，但只是样本UNKNOWN。联合设计固定首P的预测被4个新R4支持反驳：24个β2缺口owner的mate必须来自唯一nearport。由此改变问题为一次完整Hall门，而不是续seed或搜14!配对。新预测所有two-disjointcorecut P都有同类数量障碍，已由完整196371域支持。

## 必要路线与注入条件

G为已绑定自然364/714图，28个3度ports互距5，原R2类分割全部364；其它336点4度。删两条不相交原core边，令四端点集P；加端口perfectmatching M，再加新z邻接P。条件图365点730边、全4度。

原P到t的最短路若穿删边，可从该边下游P端点重启而变短，故source最短P路线不穿cuts。z起最短路不回z；两matching步间若只有旧边，需连两个不同ports、长至少5，故z的≤5路线至多一次M。对source R4(P)外hole t，若其唯一R2 owner b到t的距离β=2，那么1步star+prefix+1步M+2步tail的总长≤5，强迫prefix≤1。因此b必须配给near(P)={a为port且a邻某个P}。β2-tail若穿P就与hole矛盾，必要条件的源距离语义成立；详见JOINT_PORT_SCOPE_ATTACK。

每个hard owner至少有一个这样的hole。M是perfectmatching，owner到mate为一一映射，所以|hard(P)|≤|near(P)|是必要条件。对每条corecut，两个端点最多邻同一个port，否则两个不同ports旧距≤3，违互距5；两cut故near≤2。

## 完整实际域

原G有630条core-core边。全部unordered边对共198135，剔1764共享端点对，余196371全部检验，无随机、同构采样或预算截断。复用固定首P的4个core闭R4，补332个深4支持；hard mask仅问每个已知R2类的β2层是否仍有R4(P)遗漏。没有重源全D5或旧28port球。

完整数据hard为21..27、near为0..2，最小实际hard−near=20，0幸存P。因此每P的所有M均被必要注入条件拒绝，不需要matching求解、完整候选或旧旧BFS。ALL_CUTPAIR_HALL_COUNTS.tsv保每对数据，SOURCE_SUPPORT_BINDING保支持输入，RESULT给分布与最紧例。21的下界来自完整数据，不包装为未证明的普遍几何定理。

## 范围与下一步

只关闭上述fixedsource/two-original-corecuts/portperfectmatching/四端点star且无其它修改的完整机制，不排一般365点或一般(4,5)。旧10000样本UNKNOWN保为历史；新完整域证据现升级架构结论。0新增图/参数/Lean，case最终3.913081991/20CPU（含原样本/读门/准备/fixedP/全域/root整理，不清零）。停止该机制，不自动加第三cut/repair或换源。下一仅B的32控制器/F2多路线只读门，旧严格范围优先继承。

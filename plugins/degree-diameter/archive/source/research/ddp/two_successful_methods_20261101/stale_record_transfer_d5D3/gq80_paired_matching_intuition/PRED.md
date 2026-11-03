# 继承同一 GQ80 机制后的一个局部可推翻预测

修订：root 后续优先提出 common order5/C5-equivariant paired matchings 接口，当前仅核旧 scope 与缓存；该对称 action、压缩模型和求解均尚未构造。本文件下方的 a_0=3 局部正假设保作最初读门记录，未派发、未检验，不与 C5 方向并行启动第二计划。

本文件登记下一算的问题，**本读门没有执行该算**，不是新计划或新增方法。原完整模型与 restricted girth5 模型都仍 UNKNOWN；不续旧 solver timer。

缓存原模型的首个 point-side far row 为 `(x,y)=(0,1)`，坐标分别 `(0,0,0,1)`、`(0,0,1,0)`。以此固定 root/mate 作一项局部路线互补测试：**预测存在 girth5-compatible 的局部 P/Q 选择，满足 P(0)=1、a_0=3，使 own-first 的8个、own-last 的6个和 opposite-relay 的12个 endpoint 恰为26个剩余 far targets 的不交分割。** 这只预言一个局部可实现例子，不预言全80点 D3。

检验对象可完全来自已缓存 incidence、原 matching variable IDs 和 rectangle supports；不需重建 F3/GQ、不需源图 BFS。应同时保存三类 endpoint 实际集合及其交集，避免仅报总遗漏数。找到一项具体 partition 即支持这个局部正假设，并说明 old global solver 的困难至少不只是此单根容量；若完整有限 local domain 无解，才可在其精确假设下将 a_x=3 排除。结合继承 sum a_x=80，若确能对所有对称同类 roots/mates证明 a_x<=2，将迫 a_x=2，但这本身仍不自动给 fullfamily NO。

承继知识而非新发现：a_x<=3、8+(12-2a_x)+12、E_x=6-2a_x+delta_x 和 sum E=80+sum delta 均已在旧 `ANALYSIS_GLOBAL_ROUTE_BUDGET.md` 说明。此前没有 augmented matching pair/失败图可直接“修一下”；下一问题必须检验实际兼容性，不再重复这些计数或增加旧模型的编码窗口。本轮只读 cap5CPU，下一算预算与执行待 root 明确授权。

新接口下一步的实际可推翻预测应在构造授权时先登记：固定一个与缓存 B form 相容、对 P/L 都 free 的 order5 action，是否存在与其 commuting 的两 perfect matchings 共同满足全部旧 exact far-cover rows。旧 five windows 没有该 symmetry 条件；这会改变生成规则，而不是重启原1560变量 timer。当前的8个5-orbits/side、280 blockbinary、16degreeeq、216far-orbit clauses只是 action 成立后的预期维数，不是已生成模型统计。

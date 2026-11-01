# 蓝十二紧面实际核验记录

对象为 [B12_TRANSFER.md](B12_TRANSFER.md)，规范全文为
[TWENTYFIVE_TIGHT_B12_EXCLUSION.md](../../../../../proofs/propertyb35/TWENTYFIVE_TIGHT_B12_EXCLUSION.md)。
准确范围仅为25点35条简单五元边、点对覆盖且含六度点的非B原图中，
按 $\min(b,u,\delta_B),\max|S|$ 选出的唯一低坏边源不能满足
$(b,u,N_2)=(12,0,3)$。

## 同家族独立全文核验

2026-10-20，代理 /root/q4_low_center_gate/twentythree_existing_scope
独立推导了匹配价格加强，随后静态只读全文。其实际反馈为：

> 全文核验PASS，未发现实际source或caller遗漏。高汇点交换式(5)、
> 价格界(9)、E0/E1分流及最终点对覆盖矛盾均成立。

核验特别确认：高汇点交换只比较第二级最小 $u$，无需将其冒充低点；
$q\le1$ 的三低汇点论证没有错误应用于低汇点自身；最终 $z,h_i$
点对按 $G,N_4,N_3,N_2,N_1$ 穷尽，未假定 $z$ 是低点。

唯一MINOR为“每个匹配对端点低”应限于已被低汇点标记的匹配对；
源稿及规范稿均已更正。后文原论证已经只使用该范围。
主代理随后报告已全文读取并认可论证方向。

这是same-family/provisional核验，不是跨家族或正式proof-checker验收。
跨家族审阅由主代理另行负责，本记录不预告其结果。

## 确定性小核

[B12_CHECK.py](B12_CHECK.py)及其实际输出
[B12_RESULT.json](B12_RESULT.json)检查全部11个基础整数角色行、价格筛后
唯一剩余行、91,125个双owner/单owner集合投影及72个可行投影。
它不枚举原超图、不产生布局、不重放概率表；最后点对覆盖矛盾仍由正文
逐颜色型证明。本记录不把这些角色数称为超图分类。

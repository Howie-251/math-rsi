# 放宽到第五商方向：局部修复成立，两控制器仍严格失败

这次允许全部120个商方向置换，解除旧24域把conic方向映回conic方向的限制；实际H_p投影明确区分了第五nucleus方向，没有复用旧固定port置换。

预测得到部分支持：Exoo旧edge0→51从空域变成12种映射。但其他24条边仍有3个incoming方向只能映入2个商方向（已包含joker）；Michel仍有36条边出现同样3→2 Hall冲突。因此两source连任意invertible linear／semilinear portline传送都不能满足唯一三步路线的必要满秩要求。

实际0.099CPU；0源BFS／短词重算、0矩阵域、0SAT、0图。停止在此必要门，不派D0/D2或端口seed搜索；其他控制器仍开放。

[完整证明与范围](PROOF.md) · [事前预测](PRED.json) · [实际商方向绑定](QUOTIENT_BINDING.json) · [所有域计数](RESULT.json) · [Exoo小Hall证](Exoo72/MINIMAL_HALL_CERTIFICATE.json) · [Michel小Hall证](Michel72/MINIMAL_HALL_CERTIFICATE.json)。

# 任意边界matching：新增14580项全失败，完整局部修复域关闭

这次确实放宽了生成规则：允许A-A与B-B边。一个实际例子用51--59--36--18修好了旧唯一跨侧点对51、18，证明旧pure-cross“必须直接匹配”论证不能外推。

但完整28边界点对的准确条件把所有14580个新增assignments全部排除，0survivor。旧4320个pure-cross失败直接继承、没有重跑，合计覆盖180条被删边×105种perfectmatching。partial matching总能补全，所以已关闭这个源删相邻两点、保其余边且max5的全部旧旧edge-repair范围。

单worker15CPU硬guard，实测0.2511CPU；无新控制器全R3、映射模型、SAT、纤维图或Lean。其他删除操作、其他源及一般70点控制器仍开放，不再续本局部surgery。

[完整证明与精确范围](PROOF.md) · [事前预测](PRED.json) · [新批结果](RESULT.json) · [14580个失败证据](BOUNDARY_ATTEMPTS.json) · [旧论证失效的实际正例](OLD_CROSS_ARGUMENT_ESCAPE_EXAMPLE.json)。

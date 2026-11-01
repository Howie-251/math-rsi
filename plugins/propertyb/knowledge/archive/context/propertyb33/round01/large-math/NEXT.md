# Large-math 恢复地图（2026-10-08）

**最新：23、24点均已形成完整候选覆盖。** 正式恢复入口是 `COMPLETE_CANDIDATE_MAP.md`，其中有穷尽分支树、各精确证据及最小Lean接口。下文早先“剩余r=1”的描述保留为研究阶段；它现在已由“有七度bad邻居/全部七度unit”二分闭合。新增23/24还没有Lean或Grok/Gemini最终审阅，不宣称整个T33完成。

## 完成的Lean工作

- `formal/Aris4Math/ThirtyThree/EightClassification.lean`：任意Fin8线性覆盖三元族、至少5条→14型+实际等价；无seed前提。
- `EightTraceClassification.lean`：真实H/S8→完整pairCompletion(rep14)。两模块已build，标准三公理，日志见本目录eight-*。
- 上述已被下游25点完整证明接入；22点也已由其他代理完整Lean闭合。

## 新数学候选（尚未新Lean、尚未跨模型审）

1. `TWENTY_FOUR_AT_LEAST_FIVE_SIXES.md`：24点至少5六度的完整候选。与root `proofs/propertyb33/TWENTY_FOUR_MANY_SEVENS.md` 合成完整24点候选。关键新机制是固定实际bad pair的随机锁序平均，以及真实局部bad类型适配；相应原始数据都在此目录。
2. `TWENTY_THREE_FOUR_SIXES.md`：23点至少4六度完整候选；464有标号局部剖面/50同构型/3176bad输入全严格，131个不同caller独立ABC复算。
3. `TWENTY_THREE_MANY_SEVENS.md`：23点至少19七度完整候选；高共度排除→P3排除→团并→四团/三团选点。实际102个赢家独立复算2346行。三团moment不等式证明能选含大块六锁，正确避开未通过的两个仅三元型。

## 剩余范围与最新推进

23点此前剩余六度数r=1,2,3，七度数19−2r≤t≤18。现在r=3已由 `TWENTY_THREE_THREE_SIXES.md` 完整候选闭合：三低两高五锁844有标号/372代表全严格，最坏43753/43758，全部8556行独立ABC复算。r=2代理也已得到208代表全严格，最后4型用精确dual；完整证据见r123-child/TWO_LOW_THREE_HIGH*.json，代理正在写选点与独立复算。仅r=1仍无完整候选。旧单位共度混合四锁12彩色型不能简单闭合；见MIXED_FOUR_UNIT_V23.json。

最新解析选点已把这三个r统一：任取六度x，有至少t−2≥11个与x共度1的七度点。取其中11个；单位共度图最小度≥4。无C4时二步路径计数给Σ_v C(d(v),2)≤C(11,2)=55，最小度却给≥66，矛盾。因此四七度可选为单位C4；它们之间仅两条对角可能bad。七度pair共度≥4的双锁已单独严格排除，剩下两对角各共度1/2/3。连同x得到唯一待核验的“一个六度中心、四个七度叶子、bad图仅matching”五锁域。子代理正在完整枚举16个大迹的0/1局部输入并核验精确界；选点本身不是该数值域已经通过。

## 在途委派

- /root/t33_large_math/r123_math：独立攻上述r1..3剩余域，只写r123-child独立目录；不改Lean，不调用MCP。
- /root/t33_large_math/candidate_math_audit：只读对抗审查新增24≥5六度与23≥19七度候选，报告candidate-audit/REPORT.md。same-family/provisional；Grok/Gemini仍由root统一组织。

上述审查已完成，未发现实质数学错误；完整局部域和保存代表轨道覆盖、448/119坏槽、43中心dual均独立回放。该代理随后继续研究r=1的C4选点。其新简洁引理：11点单位图δ≥4中，每个指定点均属于C4，否则经过它的二步路径≤10，实际至少4·3=12。故先固定低度实际bad pair，再选其两arm并之外的一个七度点并取经过它的C4，可排除实际badpair的两迹各含两个七度锁的槽。

## 工具与位置

新脚本均在 `computations/propertyb33/round01/`；LP建议器需 `.tools/math-python/bin/python`，原Fraction/独立注入无需该环境。LP返回本身不作证明，使用的是保存的非负有理dual及精确罚项计算。没有读取、修改或干扰aris4math_v2。

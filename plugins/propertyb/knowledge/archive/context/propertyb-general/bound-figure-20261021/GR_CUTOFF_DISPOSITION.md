# 五项参考包络起点17：核查与处置

2026-10-21。范围仅为 `BASELINE_COMPARISON.md` 引理D.2及定理D从k≥32收紧为k≥17；没有重审主定理C或运行Lean。

## 数学结论

全部整数k≥17均有L_GR(k)≤2^k。原D.3已有B_pair≤B_cont≤B_RS以及B_lin≤B_RS，原B.4已有2^k≤B_RS，所以五项明确参考界的最大值L_ref=B_RS+1在全部k≥17成立。主定理C因Δ≥1而严格改进五项中的最大值。不是所有文献方法的无条件最佳纪录声明。

解析加强只需将单调函数2^(x/2)/x的起点改为17，并用131072>73984核对2^(17/2)>16·17。沿原证明获得q>8k、v>4k²。独立Sol报告 `GR_CUTOFF_CHECK.md` 核对取整、同一合法v、逐因子乘积、Bernoulli及全称覆盖，并独立做17…31精确整数辅证；主代理核对解析链及精确算术。有限表不是证明依据。

## 跨家族具体审阅

共同提示保存在 `GR_CUTOFF_REVIEW_PROMPT.txt`，两者均只读数学源及独立核对报告。

|Reviewer|实际返回|完成状态|范围与结论|
|---|---|---|---|
|Grok|grok-4.7-build / xhigh；线程20439f54-1666-479c-a034-08bcc943de5b|end_turn|确认D.2与D均适用全部k≥17；逐项解析核对。原回应 `GR_CUTOFF_GROK.json`。|
|Antigravity/Gemini|CLI选择gemini-4-argon-high / high；线程ad158e17-ea0b-4c81-892a-cc1da2f7491c|SUCCESS|确认同一全称解析证明及D.3衔接，无数学缺口。原回应 `GR_CUTOFF_GEMINI.json`。|

主代理纠正Grok回应的一处书写错误：其“v≥4096≥2k−1”后半不对任意大k成立。正确合法性链是v=(k−1)q≥256(k−1)>2k−1（k≥17）；Sol、Gemini及规范证明均使用这个随k增长的界。原回应保留，不把这句移入证明；不影响后续q>8k、v>4k²链或结论。两模型均未运行Lean，未将模型认可作为形式证明。

## 同步与验证范围

规范D/D.2、文献表、图解、阅读页生成器已同步17；E的256范围不变。图删除32比较门槛，保留32刻度及数值样点。按用户指示横轴加入Property B，右轴明确Δ_cert=g_*≤Δ，所有数值和48个既有证书均未改变。

主定理C既有端到端Lean仍为全部k≥17；本次加强的比较D是纸面推论。独立模型意见为跨家族数学辅助审阅，本轮没有新增Lean核验。旧35/36暂停、v2隔离，无新Goal。

最终展示标题为“Property B m(k)｜差值主图：下界究竟提高了多少”。最新单卷含1005处内嵌公式，桌面与手机离线、公式与源稿顺序、三张内嵌图、链接和页面溢出检查通过；证据 `.aris/traces/render-html/2026-10-21_general-bound-propertyb-title/browser-check.json`。独立限定保真审阅 `CUTOFF17_HTML_REVIEW.md` 无发现（same-family/provisional），只核本次范围/轴标/标题修订，不重审数学。

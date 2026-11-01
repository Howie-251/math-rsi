# 新旧界比较与完整拼接：终审处置

数学规范：`proofs/propertyb-general/BASELINE_COMPARISON.md`，结合另外三份核心源。主代理已核准确L_ref组成、取整、真正离散式的归一化、非全含中心数据、全部M分区及实际范围。正式增量和合并审计为`round02/formal-audit/BASELINE_ADDENDUM.*`与`COMBINED_AUDIT.*`。

## Gemini：有效完成，无修改要求

线程`a112c973-96ea-4124-9af5-c4ae64f5fe4b`沿用Gemini4；返回`status=SUCCESS`，CLI选择`gemini-4-argon-high/high`，effort来源`cli_selected_model_variant`。原始包`GEMINI_BASELINE_RAW.json`，全文`GEMINI_BASELINE_RESPONSE.md`。这是CLI模型回执，不另宣称服务端独立认证。

实际读取比较原稿、SOURCES_FINAL、Grill原始TeX全文以及清洁比较源全文；只读静态审阅，没有运行脚本。四项义务逐项认可，结论为SOUND AND READY FOR ACCEPTANCE：

- 全k≥32的GR包络≤2^k，五项明确定义L_ref=B_RS+1；ceil与外层min量词无问题。
- 全k≥256、每个M>B_RS的指定零锁松弛不通过；实际(B9)的+3位置指标、外部1/v、连续min、FKG差额与κ两区间全部接通。
- 原稿来源范围准确，未将固定k/固定v或未来多锁研究当成已有同域下界。
- 与先前已审三源组合得到全原始超图的新下界，比较范围内严格增益成立。

主代理核对上述实质推导后接受，无需数学修改。回应中的“entire published reference envelope”按正文(B2)明确五项理解，不扩写成所有过去或未来文献的穷尽最优性。松弛见证不被当作实际H。ARIS trace为`009-general-bound-baseline-gemini.*`，位于`.aris/traces/research-review/2026-10-21_run01/`。

## Grok：原生终稿已有效回收，无数学修改要求

同线程`a7072949-9c27-49c9-90ca-ea16d7ece030`的最新baseline turn于04:00:27.970 UTC开始，04:10:37.090 UTC原生`turn_ended outcome=completed`。返回型号`grok-4.7-build`，effort为xhigh，来源为原生最终assistant及summary。暂停/恢复使外层cell1430不可取回，回收的是同一次调用的原生完整终稿，没有新请求、付费重试或终止进程。原MCP envelope及其stopReason未知，保持缺失，不冒填end_turn。

最终正文`GROK_BASELINE_RECOVERED.md`，原生最终消息`GROK_BASELINE_RECOVERED_FINAL.json`；请求准确绑定、实际工具范围与完成证据见`GROK_BASELINE_RECOVERED_METADATA.json`。实际读取清洁比较源、两份原稿全文以及Grill原始公式，并核UNIFORM改写句；没有执行计算。

Grok逐项认可GR比较、指定零锁松弛全部M的比较、准确已发表一般判据包络以及与核心三源的最终拼接。主代理核对后接受，无需数学改动。其对(B14)的解释有一处计数笔误：h=k−1,…,v−k+2共有N+1个位置（j=0,…,N），不是回应所说的N个；正文与两家引用的最终下界均使用正确索引及系数，故不把该笔误写入证明。

ARIS trace为`010-general-bound-baseline-grok-native-recovered.*`，位于`.aris/traces/research-review/2026-10-21_run01/`。该trace的完成判据为明确原生completed事件，原始MCP回包缺失事实保留。

## 最终处置

核心与完整比较均有两家有效审阅，未留下需修复的数学问题。正式数学依据为四份完整源及主代理核查、proof-checker核心/增量/合并审计；模型意见单独记录。完整范围固定为：k≥17无条件新预算，k≥32严格提高(B2)的五项参考包络，k≥256另超过明确定义的零锁必要数据松弛方案。没有将松弛见证升级为真实H或宣称排除全部未来方法。

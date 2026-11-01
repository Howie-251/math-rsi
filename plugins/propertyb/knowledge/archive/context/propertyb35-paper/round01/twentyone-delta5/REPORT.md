# 21点最小度5完整纸面候选与精确证据

2026-10-19。入口`DELTA5_PROOF.md`：对任意点对覆盖的21点35边简单五元超图，只要最小度5，即可二染色。实际选五度中心后，所有邻点单位，五条link构成五个4点块。全分支通过共享同一块划分Π与包含数的局部分类闭合，没有整图枚举。

含另一个五/六度点的完整证明是`LOW_NEIGHBOR_PROOF.md`。其余外点全≥7时，七/八度数量a,b满足2a+b≥10，按a≥5、a=4、3、2、1、0穷尽：

|a|合法实际选点|最终共同域与结论|
|---|---|---|
|≥5|5个7|1型，界2864/3003严格|
|4，b≥2|4个7+1个8|空域|
|3，b≥4|3个7+2个8|28型全严格，最大2137/2145|
|2，b≥6|2个7+3个8|554型553严格；唯一残迫全部八度点落一个4点块，矛盾|
|1，b≥8|1个7+5个8|20份共享I候选均无非负库存，空域|
|0，b≥10|6个8|六份五点残视图无法共享Π/I，空域|

高阶包含数限制始终为：五点≤1、六点=0；中心Π每块≤4、块数≤5。最大只选六个邻点。没有以未获保证的九/十邻点目录替代实际选点预算。

三个最终复算入口不搜索位置，不运行DP、SciPy、MCP或Lean：

```sh
python3 -B context/propertyb35-paper/round01/twentyone-delta5/domain_audit.py
python3 -B context/propertyb35-paper/round01/twentyone-delta5/replay.py
python3 -B context/propertyb35-paper/round01/twentyone-delta5/orbit_audit.py
```

- `DOMAIN_AUDIT.json`：PASS。独立RGS/显式Möbius及前缀扩充，逐项核对所有完整域和空域，约13.28秒。
- `REPLAY.json`：PASS。4879个固定输入，35条stub、1190个有向不同对、102459行独立注入计数；嵌套坏对扣除与两份共享坏对dual均复核，约34.32秒。
- `ORBIT_AUDIT.json`：PASS。15340份原库存逐份核对实际标签/位置映射及源绑定；631个数值轨道代表独立精算，约4.13秒。轨道通过显式置换与整数计数相等验证，保持全部实际输入覆盖。

主要数据与生成器：

- `PILOT.json`：27双锁、110个5–8度两邻点三锁；`pilot.py`。
- `STAR_LOW_DOMAIN.json`、`STAR_LOW_DP.json`、`JOINT_LOW.json`：低邻点117域及4个指定joint残型；`star_low.py`、`joint_low.py`。
- `SIX_SEVEN_FOUR_DP.json`：有6/7邻点的11型完整共同域；`six_seven_four.py`。
- `SIX_EIGHTS_FOUR_DOMAIN/DP.json`、`SIX_EIGHTS_FIVE_DOMAIN/DP.json`：257→17残→166→1残；`six_eights_four.py`、`six_eights_five.py`。
- `STAR_THREE_DOMAIN/DP.json`：一般7/8三邻点316域；`star_three.py`。
- `GENERIC_FOUR_DOMAIN.json`：五种度向量5579完整四邻点域；`generic_four.py`。
- `FOUR_SEVENS_DP.json`、`FOUR_THREE_SEVENS_DP.json`、`GENERIC_7788_DP.json`、`GENERIC_7888_DP.json`、`GENERIC_8888_DP.json`：五种完整四域的固定位置证书。
- `FIVE_SEVENS_DOMAIN/DP.json`、`FIVE_FOUR_SEVENS_DOMAIN/DP.json`、`GENERIC_77788_DOMAIN/DP.json`、`GENERIC_77888_DOMAIN/DP.json`、`GENERIC_78888_DOMAIN/DP.json`、`GENERIC_88888_DOMAIN/DP.json`：六种完整五域。
- `GENERIC_788888_DOMAIN.json`、`GENERIC_888888_DOMAIN.json`：两种空六域；`seven_five_eights.py`、`six_eights.py`。

`GENERIC_FOUR_PILOT.json`仅为初始50样本布局诊断，不承担任何最终全称证据。后续完整域、逐型明确位置及审计覆盖已取代其作用。

状态：完整21点δ5自然语言候选及本机确定性证据已齐。尚未新增跨家族最终审阅或Lean，不将其称为全局m(5)≥36的最终验收；其他点数/度数由主代理继续处理。旧23/24及已有Lean成果未改。

# 20点δ7：r7=3完整、r7=2仅共度二尚开放

2026-10-19。本目录未改已审计δ6或r7≥4的源/证书。仅自然语言证明与精确局部证据，无Lean、MCP或wiki操作。

## 完整纸面候选

- **r7=3全支**：`DELTA7_R3_PROOF.md`。实际全局预算选两名不同八/九度点各低盈余≤3；真实同库存join得2100标签/500轨道。489固定+11联合全部严格，最大4993/5005。`R3_REPLAY.json`独立域/运输/固定/dual PASS，约8.33秒。
- **r7=2、两低共度三全支**：`DELTA7_R2_C3_PROOF.md`。Q≥10、总盈余14，w1已严格排除，故至少三名w0。18共同五锁中14严格、四剩；任意三个w0须恰二paired且九度。四点双计3P=8排≥4，恰三则Q=10而九度点至多一，矛盾。`R2_C3_REPLAY.json`PASS，约4.3秒；14严格最大64208755763/64350000000。
- **r7=2、两低共度一全支**由两份正文覆盖：`DELTA7_R2_C1_MULTIPLE_SMALL_PROOF.md`处理Q中至少两名w≤1；`c1_two_stars/PROOF.md`处理唯一低w的真实刚性谱。
  - 前者346共同五锁中289固定+51联合严格，六剩只允许w类型{0,1,1}（两w1为九度）或{1,1,2}（全九度），经T双计与总度矛盾闭合。`R2_C1_MULTIPLE_SMALL_REPLAY.json`独立域/证书/结构PASS，约13.43秒；340严格最大2573508283/2574000000。
  - 后者实际谱7²8⁹9¹10⁸，八名十度都与两低单位，至少五名unpaired。合法取三名unpaired十度，两份真实star划分共同恢复2533标签/358真S2×S3轨道；**358全部固定严格**，最大43282/45045。`c1_two_stars/REPLAY.json`用不同的全五点inclusive Mobius重建域、全部运输和固定证书PASS，约1.32秒。

以上每份正文都有实际选择、完整参数域、同一H的高阶/槽恢复、证书索引和固定命令。未严格库存只作共同结构必要条件；全局整数矛盾才闭合其所在分支。

## r7=2准确剩余：低共度二

完整现状在`C2_STRUCTURE.md`，原始38余项在`R2_REMAINDERS.json`。已从真实旧容量独立重建2132相关四锁标签、1068共同五锁域：941固定+89联合严格，余38。`R2_C2_REPLAY.json`PASS，约19.88秒，1030严格最大15011/15015。

这38残项已经给出较原表更强的实际归约：

1. Q全部低外共度≤2。共同38三视图加R16/Q≥10/九度预算排除所有w1，因此Q点仅为双unit w0或两低共度(2,2)的w2；所有w2点τ=0。
2. type=(w,degree,τ)只余A=(0,8,0), B=(0,8,1), C=(0,9,0), D=(0,9,1), Z8=(2,8,0), Z9=(2,9,0)。T为w0点集，2≤|T|≤7。
3. A类的双star冲突并集必为匹配，两个中心各只有五条非共边容纳A，故A≤6。
4. 八种全T三元/七种两T+Z型，49个T计数，再加Q/R/度预算，恰83份必要typed-count。`R2_C2_STRUCTURE_REPLAY.json`0.04秒独立核查并保存全部83输入。这是必要类型计数，不是83种实际H或完整概率域。
5. 83份全都保证至少三名外点与两低均单位且unpaired，公式A+C+max(0,q−2|T|−4+B+D)≥3。完整逐型预算保存在`R2_C2_ACTUAL_UNIT_BUDGETS.json`。
6. 83型高点度≤19；高unit十二至十五已有严格三锁，新增十六至十九的八份单位三锁也全部固定严格，最大14023/17017。因此所有双unit外点度在8,9,10,11；实际至少三名unpaired，但不保证其中三人同时高于八度。若高点总w=0，则全为unit，e必须≤高人数；这再排7份type输入，必要外域83→76，逐型记录同预算JSON。

目前**没有**用新的概率表排除这些真实结构。当前必要松弛例见`R2_C2_BUDGET_RELAXATION.json`：Q=六A+四Z8；高点四名十度w0τ1、两名十度w2τ1、一名十度及一名十一度w2τ0，满足总度175、总盈余16、各低盈余8、τ总6及现有所有type约束。它未提供高点间完整共同库存，不是超图或反例。历史“Q十A”松弛已被A≤6排除，单独标为superseded。

## 发现成本与主动回退

一般r2两外点4182标签/2146代表，一次DP/joint后114未严格，约32.91秒。直接第三外点join产生41145标签/16314轨道，1.22秒生成后主动停止，未刷五锁大域。只算三个新真实三视图的205去重输入，81严格，3.97秒降到8133；再以实际Q选点与第三四视图降c2=1068、c3=18，c1至少两低w另降346，才各作一次DP/joint。c2/c3约35.55秒、c1的346约13.28秒。

刚性c1改用三名实际unpaired十度的新双star表示，先10项pilot全部严格，358全域发现加精确注入验证约5.97秒，从而闭合整支。没有反复试原38失败布局，也没有盲加第4/5外点。

`HIGH_OUTSIDE_PILOT.json`12双+156三锁约2.09秒，已独立精确重放；它实际支持十一度刚性谱排除，但(7,7,10)多份输入仍失败，不能给所有高点统一正w下界。新增八份高unit16–19约0.10秒；`replay_high_outside.py`现也重放这些固定证书。

## 固定无搜索复现

```sh
python3 -B context/propertyb35-paper/round01/middle/20-new-high/low_seven_r23/replay_r3.py
python3 -B context/propertyb35-paper/round01/middle/20-new-high/low_seven_r23/replay_r2_c3.py
python3 -B context/propertyb35-paper/round01/middle/20-new-high/low_seven_r23/replay_r2_c1_multi.py
python3 -B context/propertyb35-paper/round01/middle/20-new-high/low_seven_r23/c1_two_stars/replay.py
python3 -B context/propertyb35-paper/round01/middle/20-new-high/low_seven_r23/replay_r2_c2.py
python3 -B context/propertyb35-paper/round01/middle/20-new-high/low_seven_r23/replay_c2_structure.py
python3 -B context/propertyb35-paper/round01/middle/20-new-high/low_seven_r23/replay_high_outside.py
```

这些重放不运行DP、SciPy或LP；固定A/B/C与坏对扣除使用35个stub、1190有向不同stub对的独立下降阶乘注入计数，全部精确Fraction。发现脚本如需重跑使用`.tools/math-python/bin/python -B`。`R3_ONE_*`早期292轨道较强单点预算不能代替最终两点证明所用`R3_WEAK_ONE_*`的344轨道统一预算。

本目录只推进20点δ7的所列范围；r7=1、δ8和其他点数状态由主代理总地图另列，不宣称20点或全题完成。

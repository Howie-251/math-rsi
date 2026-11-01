# 新修复门对P7一／二内部的转移

## 两项完整新结构范围

1. **两内部、纯二迹整支可解析补齐。** [TWO_INTERNAL_PURE_PAIR_PROOF.md](TWO_INTERNAL_PURE_PAIR_PROOF.md)保留旧共同点s>0分流，新增C全s0：missing相邻时D三点总J度容量22<26矛盾；missing不交时D四点、总J度26、每点≤7，迫一外高点s=7且private0。与共同q双蓝得到精确6P4/6T14B，现成六正6T门修复。没有任何新局部表，主代理已核实际caller并纳入P7两内部规范部分定理。
2. **两内部、(n2,n3,n4)=(1,0,4)整支有限候选。** [FOUR_QUAD_PROOF.md](FOUR_QUAD_PROOF.md)完整证明actual H→两missing标准形→全部四P4多重集和唯一P2→必要域→own bluepair→原染色。1.12 CPU秒完整生成相邻missing26189与不交51651，共77840必要P源，零残。全部保存自己的blue和所用门；逐35迹重放2724400条源索引PASS，约2.01 CPU秒。门分布为旧七19244、旧L17八38860、新九19736。25的J-first第二独立生成已重建完整键集并逐35迹重放；主代理已本机运行CHECK核验通过，证据在 `independent_four_quad_domain/`。

这些是精确结构分支，不是整个P7一／二内部的完成声明。

## 新八门的严格适用边界

P7耗尽总度盈余七，所以外部L恰17点，且全七度。因此新的L18、8P4/1T20B门在这些P7分支中不新增条数覆盖：旧 `EIGHT_POSITIVE_FOUR_SET_REPAIR.md` 的L17、8P4/3T20B扩展已经包含它。这个判断不适用于P6的L18，不能把两种地面混淆。

## 九门选择的真实不变量

记内部边数I为1或2，非内部三／四迹数为n3,n4。总度给

$$n_2+2n_3+3n_4=21-4I,\qquad n_1=14+3I+n_3+2n_4.$$

固定两个蓝高点Q，要求它们命中所有内部与高迹，并在二迹多图J中独立。令c_Q为蓝点内部出现总数、h_Q为蓝点高迹出现总数、s_Q为二迹度数和。此时没有负二／一或正三风险，实际

$$m=16-c_Q-h_Q-s_Q,\quad T=n_2-s_Q,\quad B=n_1-m,$$

所以

$$m-T=4I-5-c_Q-h_Q+2n_3+3n_4.$$

单个共同q蓝给正四数至多7（I1）或6（I2），不能直接生成恰九正；九门需要多蓝选择。纯二迹时，蓝pair给m−T=−1−c_Q或3−c_Q，因此m8/9必伴过多负三，不能调用新八／九门。纯二迹新增完整证明因此使用别的真实强度：s=7把双蓝正数压到六，并直接接六正6T门。

一般高迹中，h_Q≥n3+n4。若双蓝想满足九门m=9,T≤3，则必要有

$$n_3+2n_4\ge11-4I+c_Q.$$

即I1至少7+c_Q，I2至少3+c_Q。这说明新九门在I1的一般低高迹库存中不会自动奏效；它最直接的收益是四迹较多的分支。此次只展开最明确I2四四迹库存，未扩I2全部库存或I1全部P迹域。

## 源码、数据和交接

* `FOUR_QUAD_PROFILE.py/json`：完整必要P域及接受统计，无外部布局。
* `FOUR_QUAD_WITNESSES.jsonl`：每源自己的四迹多重集、二迹、private、blue、gate和(m,T,B)；schema在JSON。
* `REPLAY_FOUR_QUADS.py/json`：从每份保存源展开35条原索引，重新分类全部signed约束及门假设；不是第二域生成。
* [FOUR_QUAD_PROOF.md](FOUR_QUAD_PROOF.md)给所有筛选必要性、完整循环、两missing标准化与实际染色运输。

没有名为 `TWENTYFOUR_SEVEN_HIGH_TWO_INTERNAL*` 的现存规范文件；本次读取的是当前BRANCH_COVERAGE、root合并稿与上述旧共同点条件caller，未编造不存在文件的内容。旧范围不被历史报告覆盖。源码CPU合计不足五秒，未复制旧P6域，也未进行原H枚举。canonical与导航均未改。

新增无表统一入口见 [GENERAL_SINGLE_BLUE_PURE_PAIR.md](GENERAL_SINGLE_BLUE_PURE_PAIR.md)：一般单蓝共同点m=d(q)−I−s、总负M−d(q)，以及P7 I1/I2/I3纯二迹的完整scope；I2/I3引用已验旧源，I1总J度数选点新补齐。

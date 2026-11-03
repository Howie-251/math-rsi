# Actual94186的相邻K2互助：路线门通过，模型仅准备

固定14度、D5、94186点/657452边源，新增相邻两点，分别接旧集合A/B、各至多13个pin。当前3685个free旧点中3670点仅1个slot，15点2个slot。不能混成88452旧core，亦不恢复旧单helper MIP。

## 仅一次新R3计算

按旧`BALLS_META.json`的同一free顺序，一次C++读取literal94186源，核对全部free标签与12/13/14度直方图。只生成3685个闭R3球，每行1472个小端uint64；旧R4直接读取、不重算。

全部94186目标的R3 provider数在25至119之间，T0为空。因而本门没有目标必须靠两侧各自R4独立覆盖，未产生容量<2证据或两cap1端口强迫相异边；相异图为空。这个必要门不排K2，也不提供可行解。

R3本身CPU0.088秒，native0.335022秒，含编译/driver总1.994530046秒，单worker，低于10CPU。保存`allfree_R3.u64le.bin`、`R3_META.json`、`FREE_ORDER.txt`、`FREE_SPARES.txt`及target provider计数，供后续准确复用。旧R4未重复计算，source D5未复验。

## 唯一确定性greedy对照

按授权每步选择合法side/port，最大化own R4新覆盖加opposite R3新覆盖；平局先A、再小label。最终两侧各13点，最多26步，没有seed、重启或swap。

完整94186mask核对给出：A/B新根各遗漏3881/3559个旧目标；其中legacy9754类各445/323。单侧自己的R4分别遗漏5157/4654，因此也没有顺带得到单helper94187候选。这些是新增root的未覆旧目标数，不是生成图的无序坏对统计；没有导出图。

## 已准备的精确选择编码

`K2_model/`含7370个selector。A/B各自at-most13；3670个cap1端口用¬A_j∨¬B_j，15个cap2端口可共享。完整条件是R4(A)∪R3(B)=V和R4(B)∪R3(A)=V。

初始只取256个最稀combined-support目标，加legacy9754中128个最稀目标与最小标签，去重后338目标、两侧676条原始精确row。103180变量、203308子句。所有feasible K2仍被保留；这不是完整94186×2行系统，SAT命中必须再查全mask。

准备CPU5.820313181秒，连同route gate共7.814843227秒。`run_reviewed_once.py --solve`已保存供root审核，但本轮未调用。它只允许一个批次，最多6轮、每轮至多15秒、共享solver CPU60秒及含准备90CPU；UNKNOWN立即停止，不重复同模型。每个SAT候选核全部旧目标，最多每侧256个真实违反row加入下一轮，并分别检查单侧R4是否已完整覆盖。任何hit立即保存参数交root独立验收。

当前status为`K2_CNF_PREPARED_NOT_SOLVED`，没有solver HANDLE、solver调用或新图。是否启动唯一求解批由root在审阅后决定；不自动调用、加时或更换source/pins规则。

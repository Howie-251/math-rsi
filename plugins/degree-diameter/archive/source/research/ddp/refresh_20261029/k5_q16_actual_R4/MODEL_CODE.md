# 固定实际 R4 算法与准备状态

## Target / Status

COHERENT AS STATED。目标是固定 K5 端口、Q16 普通电压与保存 F3^4 chart 的真实 D≤4 图，不再要求每个 controller pair 都有 NB4 词。代码仅完成 prepare 和明确授权的一次首赋值校准；尚未枚举电压。

## Invariant object / assumptions

每个原始长度≤4端口词 w 从源 field0 出发的精确可达集合为 S_w⊆F3^4，逐步关系是 x→T_p x+tℓ_p，t∈F3。BASE_INPUT 提供四个 T/ℓ、inverse ports=[1,0,3,2] 与两个定向 C5 的 K5 邻居表。小域字段标签 x=x0+3x1+9x2+27x3，完整图标签 81(16*base+deck)+x。

## Exact derivation map

1. 每条原始词的 field 像必须先保留；deck 树边为单位，signed chord 仅作自由约简。这种约简不消除原始回退噪声。
2. 相同 key=(targetbase,reduced deck word) 在任何 Q16 赋值下落在同一 deck，因此取 S_key=OR S_w 是精确合并。Root 已保存341原词、161 keys/根的缓存；本目录只转换 roots[0]，没有重算 provider。
3. 对赋值 q，把每个 S_key OR 到 (targetbase,word(q)) 的81位槽。全部80槽满等价于首根 (0,e,0) 的真实闭 R4 全覆。这一步包括空词、短词和回退词。
4. Root 的新 provider 门针对每个 (base,coset,x) 数不同 key≥4，只是实际 R4 必要门。它完整保留30个 V4 赋值，分别有4^6个Q16 lifts，总122880。本代码不读取旧 full-NB4 PASS 文件。
5. 首根通过后按字面群公式及 field 邻居表生成6480点实际邻接。先验其他4个base/field0，再验源root0与所有其他field值，共405个不同代表根。每个根逐层 BFS 到4，没有用零源合并像推断非零源。
6. 对任意 h∈Q16，(u,g,x)→(u,hg,x) 与所有右电压边和chart关系交换。因此405代表根完整覆盖所有6480根。每个候选首个失败根留下实际缺点；预算内继续下一赋值。只有405根全通过才输出图。

## Gauge and group formula

Q16 元素编码 i+8j，乘法 (i,j)(k,l)=(i+(-1)^j k+4jl mod8,j xor l)。偶层逆 (-i,0)，奇层逆 (i+4,1)。旧点(u,g)换标到(u,g h_u)，新电压是 h_u^-1 q_uv h_v。取 h0=e、hi=q_0i^-1 把四条star边置e；field不变，也保留源(0,e,0)。这是任意普通Q16电压赋值到当前树规范域的同构，不是额外限制。

## Implementation and scope

- `prepare.py --prepare-only` 只将 root 的真实缓存/30pass转换为 `search_input.txt`，构造固定972个field transition，编译 `search.cpp`，运行一次获准校准。
- 输入 prefix trie 对 signed chord 的实际有序乘积缓存；没有把非阿贝尔词按变量计数代替。所有六电压的四个lift完整枚举，第一chord是最高base4位。
- `run_once.py --run` 才会调用唯一枚举进程；prepare不调用它。全批预算90CPU，计入1.405047250准备CPU及root既有0.647435435providerCPU，保留2秒收束。原180预算已废止。
- 观察等待超时仅继续同PID；实际budget由native CPU检查与RLIMIT界定，不重启。预算终态保存phase/lift/候选根游标，不能把前缀当完整排除。
- 搜索独立于旧V4 full-NB4门。完成失败时结合root actual-provider必要门才排固定K5/Q16/这些chart的实际D4域；不排其它chart/基图/群。

## Calibration / limits

唯一确定性校准取首保留projection与六个lift digits=0，即电压[9,8,1,8,0,8]。实际6480邻接为简单12正则，逐边真逆端口匹配。字面root0 BFS与缓存代入的6480个布尔值全部一致，两者R4大小4563，首缺点162。它是校准失败图，不是新合法图；未验405根、未枚举电压范围。两完整位集保存为 CALIBRATION.*.u8.bin。

若最终有图，`hit.edges`含6480/38880，`hit.controller.edges`含80/160，HIT保存六电压与405根通过事实；root另外做独立验收。当前没有hit边表、没有搜索终态。

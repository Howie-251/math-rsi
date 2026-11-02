# 15552源的K2路线门：T0为空，无此类直接阻断

一次完整处理得 **T0=∅**：全部15552个旧目标均有 **3..18** 个closedR2 provider。
因此本门没有R3零支持、singleton容量冲突或二支持opposition条件，**不排除K2，
也不证明14-pin双侧整数覆盖存在**。没有启动求解器或生成新图。

## 精确操作与覆盖条件

固定旧源为15552点、116316边的已绑定D4图，648个可用旧点均为度14、spare1。
保留旧边，新增相邻helper y,z，分别连接不同端口集合 A、B，满足
`|A|,|B|≤14`、`A∩B=∅`。则最大度至多15，候选阶数15554。

对任意旧点t，最短新根距离精确为

```
d(y,t)=min(1+d_G(A,t), 2+d_G(B,t))，
d(z,t)=min(1+d_G(B,t), 2+d_G(A,t))。
```

若路径经过另一helper，其到该helper的前缀可被两helper的直边代替；剩余部分
在旧图，因此没有遗漏利用新边的更短路线。旧旧距离不会增加，两helper直接相邻，
所以全图D≤4恰需全部旧目标满足

```
R3(A) ∪ R2(B)=V，R3(B) ∪ R2(A)=V。
```

在全端口R2都不覆盖的T0上，两侧各须独立R3覆盖。T0中R3-support0立即不可能；
support1迫同一spare1端口同时供两侧，亦不可能；support2只给两端口须分居两侧
的必要条件。本次实际T0为空，这些条件没有实例。

## 全部实际计数与输入绑定

仅读literal源一次，核header `(15552,116316)`、度数与全部free标签。648个旧缓存
标签互异，其集合恰等于源的全部度14顶点。顺序严格沿旧 `R3_MASKS.bin`：12byte
uint32 header `(648,15552,243)`，每行一个uint32旧标签及243个uint64 closedR3。
没有重算R3或源D4。

对这648个端口直接枚举0、1、2步终点，得到完整closedR2。每个R2大小均为 **191**，
且逐位包含于对应继承R3；旧R3大小均为 **2310**，全目标R3支持数 **67..185**。

| R2 provider数 | 目标数 |
|---:|---:|
| 3 | 5184 |
| 6 | 1296 |
| 9 | 5832 |
| 11 | 648 |
| 12 | 648 |
| 15 | 648 |
| 18 | 1296 |

最小支持3仍可能在未来共同整数条件中形成限制，但本批不进行进一步选择或求解。

## 保存接口与执行记录

- `R2_MASKS.bin`：与旧R3完全相同的header/label/row格式，保持原648端口顺序。
- `FREE_ORDER.txt` / `FREE_ORDER.u32le.bin`：该字面顺序。
- `target_R2_support.u64le.bin` / `target_R3_support.u64le.bin`：各15552行，每行11个
  little-endian uint64；bit j对应FREE_ORDER第j个端口。完整保留648列，padding为0。
- `target_R2_provider_counts.u16le.bin` / `target_R3_provider_counts.u16le.bin`：全部目标支持数。
- `T0_TARGETS.u32le.bin` 为空；`T0_SUPPORTS.json` 的targets为空，二支持TSV只有表头。
- `RESULT.json` / `TERMINAL.json`、源码与进程日志保存全部实际终态。

driver PID **2952784**，唯一native PID **2952790**，exit **0**。编译1.081328CPU秒，
native子进程0.026539CPU秒，累计 **1.111414086 CPU秒**，低于10秒预算。
literal源读取1次，计算648个R2，R3重算0、源D4 BFS0、solver0、新图0。
本批结束，不自动进入完整整数模型，也不重启旧single-helper任务。

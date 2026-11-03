# 同fiber完整路线必要模型：准备完成，未求解

实际完整检查了 **232500** 个同fiber不同无序端点对。全部计数与事前预测一致：

| 类别 | 点对数 | 每对两步路 | 每对三步路 | 新clauses |
|---|---:|---:|---:|---:|
| 差值不在四方向线并集 | 202500 | 0 | 2 | 810000 |
| 差值在一条非零方向线上 | 30000 | 5 | 2 | 120000 |

每个fiber的7750对全部核查，分别为6750/1000对。每对两条三步路的四个
中间点均实际互异。共枚举150000条两步路、465000条三步路；所有3000个
既有OR5 flag均被复用，没有新建辅助变量。

对端点x,y与三步中间点(a,b)、(c,d)，若存在两步路，其共同邻居的保留OR
由原flag z表示。精确条件为

`keep(x)&keep(y) => z OR (keep(a)&keep(b)) OR (keep(c)&keep(d))`。

无两步路时删去z。其分配展开的四条clauses分别取中间点cross组合
(a,c)、(a,d)、(b,c)、(b,d)，各加两个端点负literal及可选z。

父315221变量/1290903子句的body只读复制，实际新增 **930000子句、零变量**，
完整模型为 **315221变量、2220903子句**。它精确处理全部同fiber端点的
距离≤3要求，仍不是所有源点对的完整D3模型，不将必要松弛当实际图。

完整输出：

- `model.cnf`：父模型加本次全部clauses。
- `same_fiber.added.cnf`：本次930000条增量clauses。
- `ROUTES.u32le.bin`：每对7个little-endian uint32，依次为旧标签
  x,y,a,b,c,d及OR5 flag；末项0表示无两步路。按fiber、x、y升序排列。
- `FIBER_CALIBRATION.json`：30个fiber的完整计数与各自一个online/offline字面例。
- `OR5_FLAGS.tsv`：实际使用的3000个原OR5映射。
- `MODEL.json`、`NATIVE_RESULT.json`、`TERMINAL.json`：准确范围和计时。
- `prepare_once.py`、`prepare_native.cpp`：单次生成代码。

总compile/native/driver **1.385191193 CPU秒**；native **0.337919秒**。
源邻接缓存读取一次，原边表读取0、BFS0、solver0、实际候选图0。
没有编写runner；后续是否执行及预算由父代理依据数学scope另行决定。

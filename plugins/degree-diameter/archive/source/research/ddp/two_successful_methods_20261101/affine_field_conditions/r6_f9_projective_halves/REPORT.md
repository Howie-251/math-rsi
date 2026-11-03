# r6/F9 projective-half gate — PASS

完成唯一新局部门：PG¹(F9) 上720个纯 PGL₂ 置换对全部252个五点半集的完整分类。恰两轨道，大小180与72，稳定子阶4与10；两轨道各自对补集不变。因此每个五半集都能用纯射影线性变换映到补集。未加入 Frobenius。

固定 `S=[∞,0,1,2,w,−w]` 的六个 `B_p=S\{p}` 全通过。为每个 port 取确定性字典序首补集映射，得到六张正向矩阵及六张真逆反向矩阵。实际300个中央 turn 行列式全非零；每张 chart 的十个商射线恰为全 PG¹(F9)，十平面并集恰729点；真逆、源/反向 port 向量及噪声方向兼容均通过。所有六张正向矩阵的平方都不等于 I，反向必须用保存的实际逆矩阵。

一次单worker运行，PID2008827，exit0，测得有限检查0.655405084 CPU秒，20CPU硬上限。未生成 controller 或 fiber graph，0 BFS／solver／Lean，未换 S／域／seed，未安装或生成哈希。没有完整54度D3图或公开纪录结论；没有选择目标 N。旧 C120 trianglefree STOP 保持。

本次继承而非新增：`../general_ports/DERIVATION_PACKAGE.md` 全文，包括全rank与纯回退pencil共同迫 `q=2r−3`；当前新结果是先前明确未检的 r6/q9 有限半集分类和字面 chart 绑定。

可复用产物：

- `PROOF.md`：完整范围、分类覆盖证明和真逆 chart 接口。
- `ORBIT_WITNESSES.json`：720标准化PGL系数、两轨道、全部252半集及其显式线性见证。
- `PARAMETERS.json`：F9字面表、固定六方向、f/Q/H、全部12实际矩阵。
- `CHART_CHECKS.json`：20 conic三元组、300turn、每chart十射线／平面／729覆盖回执。
- `check_once.py`、`PREDICTION.md`、`RESULT.json`、`TERMINAL.json`：事前预测、唯一运行与终态。

剩余实质义务在控制器侧：需一个具有合法六port绑定及所有同层／非邻层所需NB3路线的真实控制器，再结合其完整控制层路线与最新公开54度比较判断是否应生成完整提升图。这些工作不在本目录运行。

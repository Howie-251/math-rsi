# P_center：唯一 flat-plane 中心成立，anchor 归属预测被反驳

固定已有的 675 条 ambient Q(6,9) singular projective-line 见证，全部求得唯一 flat-plane 中心：675/675 的七变量 GF9 核维数均为 1，归一化中心均在 quadric 上且不在线上。但 **657 个 folded-image10 实例的额外 core anchors 属于中心 φ-fiber** 这一预测被反驳：25 个空 anchor 集通过，632 个非空 anchor 集全部不满足包含关系。本轮没有换 selected line、修改 pin 或拟合替代 anchor 规则；新图和新下界均为 0。

## 事前冻结与精确计算

[事前预测](PREDICTION.json) 固定上轮已经选定的 675 条线，不因结果改用其他可能的线见证。对其中 657 条 image10 线预测所有额外 anchors 均在 {π(y),π(φy)}；允许 anchors 为空。18 条 image7 线只作描述统计，没有施加这一预测。

采用作者 GF9=F3[t]/(t²+1)，元素 a+bt 编码为 a+3b。quadric 方程为

\[
Q(X)=X_0X_4+X_1X_5+X_2X_6-X_3^2=0.
\]

对所选线的固定基 x,z，令 y 为七个未知坐标。作者六个 Plücker 等式的索引是

\[
(12,34),\ (54,32),\ (20,35),\ (65,30),\ (01,36),\ (46,31).
\]

每一项 (ab,cd) 表示 x_a y_b−x_b y_a=x_c y_d−x_d y_c。另加 polar 方程

\[
B(x,y)=x_4y_0+x_5y_1+x_6y_2+x_3y_3+x_0y_4+x_1y_5+x_2y_6=0;
\]

中间系数为 −2x₃=x₃，因为特征是3。对 z 再取相同七行，共 14×7 方程，直接 GF9 行消元求核。只用六个 Plücker 式不足以定义这里的 flat-plane，polar 行不能省略。

复用上轮已经保存的 66430 个 point 坐标和 point→core fold cache；φ 取坐标 Frobenius x↦x³，和 τ² 的对应沿用已保存的全点校准。没有重建 H9 incidence lines 或邻接。两个小校准为：H9 line span(e₀,e₅) 的核维数2；非 H9 singular line span(e₅,e₆) 的核维数1，中心 e₀。实际 675 条线均为已识别的非 H9 线。

## 全范围结果

| 项目 | 结果 |
|---|---:|
| 固定 selected lines | 675，全部处理 |
| 核维数1 / singular center | 675 / 675 |
| 中心在线上 | 0 |
| image10 的空 anchors | 25，全部通过预测 |
| image10 的非空 anchors | 632，全部反驳包含预测 |
| image10 anchor 个数 | 0:25，1:228，2:404 |
| image10 中心 fold φ-fiber 大小 | 1:313，2:344 |
| image7 描述统计 | 18；anchor 个数1:2、2:8、3:7、4:1 |

18 个 image7 实例的中心 fold φ-fiber 大小均为1，且其 anchors 均不包含于该集合；因为事前没有对此组作包含预测，这只是描述结果，不计作该预测的额外失败。

单次进程 CPU **0.082783284 秒**，一个 worker。输入675条全处理，`pending=[]`。完整核基、中心坐标、原 point 编号、φ-center、fold φ-fiber 与反例 anchors 均在 [RESULT.json](RESULT.json) 的675条 records 中；[check.py](check.py) 可重现同一固定范围。

## 首个反例：core anchor12 不是中心像518

最先失败的附加点是 **41505**，所选 image10 线的基为

\[
x=(1,0,0,2,1,8,1),\qquad z=(1,1,2,5,6,5,8).
\]

归一化唯一中心为

\[
y=(1,0,1,1,2,5,2),\qquad
\phi y=(1,0,1,1,2,8,2).
\]

它们在原 H9 point 编号中为 833、836，fold 后都对应 **core vertex518**。该 selected line 以外的额外 core anchor 是 **12**，所以 {12}⊄{518}。此处 12、518 是 core 顶点编号，833、836 是原 point 编号，不能混用。

## 对后续生成规则的影响

坐标结果支持“选 ambient non-H9 singular line，可恢复唯一 flat-plane 中心”的参数化；它与同轮几何中心论证一致，不是一个新下界。另一方面，不能再把额外 anchors 限定在中心 φ-fiber 来重建这 675 个附件。完整 singular-line fold 像仍是已经恢复的附件主体，额外 anchors、度预算和所有新类之间的≤5路由仍须另有规则。

反驳严格限于本次固定 selected witnesses；上轮没有证明每个附加点的 qualifying line 唯一，因此本实验不声称排除了所有可能替代 line 的同类 anchor 解释，也不会据此自动换 witness 续试。它更不推出删去 anchors 后原图仍保径。此次只交付实际中心和反例，未做 old–new/new–new BFS、距离优化或新的图生成。

## 证据

- [冻结预测](PREDICTION.json)、[完整结果](RESULT.json)、[固定范围计算程序](check.py)。
- [675条原始线见证](../h9_quadric_line_signature/RESULT.json)、[坐标/附件 API](../h9_quadric_line_signature/geometry.py)，及该目录两个二进制坐标/fold cache。
- 六式与 quadric 坐标取自[作者生成器](../../breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/verify_witness.py) 的关联线判定；polar 行与线性化方向由同轮几何推导代理确认。本项没有执行原作者 incidence 生成或 verifier。

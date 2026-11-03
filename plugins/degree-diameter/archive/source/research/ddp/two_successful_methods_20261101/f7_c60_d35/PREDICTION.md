# 唯一F7/C60五port构造预测

冻结于新数值前。替代未执行的C30+matching较弱提议；不运行或回退该提议。

## 来源与规则

只继承 `research/ddp/more_graphs_20261027/d15_D3_current1620_source/construction.author.json` 的实际60点controller及其(a,a^-1,b,b^-1,s)端口，原F3图/旧chart不重跑。来源为Bhakar作者仓库f4t4nt/degree-diameter-graphs；一般route-chart背景及已有F5借鉴分别保留原归属。

新fiber为F7³，port方向依次为conic参数[∞,0,1,2,3]。前三张有向商映射固定为

`f01=3z/(z+3)`，`f23=(2z+4)/(z+1)`，`f44=(3z+3)/(z+4)`。

3×3提升严格按general_ports/DERIVATION_PACKAGE.md的H_target^-1 diag(1,Q_f) H_source；反向为真实矩阵逆。s匹配用低controller标签方向的T4+，反向T4−，不误用全局自逆矩阵。

## 可反驳预测及唯一小门

- 六chart均逆/方向相容，每chart16个中央turn全rank3，共96项；每chart的两组四射影点恰为PG(1,7)八点。
- 作者literal controller简单5正则、反向port绑定；全部3600控制ordered pairs中，每个非邻/同层pair有NB3，邻层使用pencil。
- 小门仅这一F7/chart/controller，单worker≤5CPU秒；失败保存字面反例并停，不改矩阵、域或controller。

## 通过后的已授权实际构造

门通过即额外≤20CPU秒完整生成唯一20580点图，标签`343*c+x0+7*x1+49*x2`；每port7邻点，预期35正则/360150边。检查所有实际邻点互异、无自环、反向边一致，并保存完整边表及参数。D≤3由全部控制路线和96局部rank/完整八平面统一推导，D≥3由Moore(35,2)=1226<20580。

不在本worker重跑原1620或3750图BFS；新完整图独验由根代理安排。新35D3公开比较只已知根代理读到的PolarStar特定参数族13272，最新全球最好仍未核，不称全球纪录。该候选不是域/控制器/矩阵扫描。

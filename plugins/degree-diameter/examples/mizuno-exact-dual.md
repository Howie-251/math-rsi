# 完整小证书案例：从局部27块到共享controller上界

## 原问题与局部修法

公开13正则、88452点、D5源为364×F3^5。希望在cap14下用完整邻域克隆严格超过94186，至少需5735个clones，即213个满27块。四条ordinary输入方向是W=span(e0,e1)的全部射影线，同fiber兼容中心最多27，原81点超平面提案失败。

27点横截块的ordinary pins可分离，但M匹配造成重叠。不变泛函给出局部351个不同邻点的见证，仍不是213块共同构造。过零块同时占目标零点；统一H被法向交叠挡住。放宽为依source选择的729种斜率后，g≤3猜想又被真实g4反例推翻。自环例外也要处理，不能把315个常规source的界外推全部364个。

后继证明处理所有364个source：不同目标法向产生27点交，而删除自环至多去掉9点，不能消除冲突。匹配容量与bad-output独占给每个target的选择量≤3，以及203项成本5、161项成本6、总成本≤1092。这些是原几何证明的进口，薄脚本不重新证明。

选择域明确限制**每个被选原fiber一个完整27点的affine W横截块**，允许各自选择斜率与phase。binary上界不是从同一fiber任意多块自动得到的。

## 精确有限对象

[MODEL](../archive/source/research/ddp/two_successful_methods_20261101/mizuno13_clone_interface/source_dependent_geometry/controller213_capacity_gate/MODEL.json)保存364个binary选择变量。每个target计四个ordinary incoming来源与M mate；M mate本身也是ordinary provider，所以非零行系数为2,1,1,1，行和与列和均5。加cost行共365行，x≤1也有dual乘子。

原MIP的数值infeasible不自动构成独立严格证明。后继exact dual的Y,Z≥0使每列组合≥10001，分母Q=10000，右端2061908。因此10000T≤2061908<2070000，整数T≤206，clones≤5562，终图阶≤94014。

## 在当前任务工作区执行

将 `DD_PLUGIN` 替换为当前MathRSI克隆的真实插件绝对路径；脚本从自身位置找归档，结果输出终端，无需切换目录：

```sh
DD_PLUGIN="/path/to/MathRSI/plugins/degree-diameter"
python3 -B "$DD_PLUGIN/tools/replay_mizuno_dual.py"
```

读取随仓MODEL与SIMPLIFIED_DUAL_CERTIFICATE，从现存数据重建原包缺失LP_INPUT中的相同365行；核行列pattern、cost、所有乘子符号、全部364列、RHS和保存的准确上界。[实际结果](../evidence/MIZUNO_DUAL_REPLAY.json)为PASS、min10001、Q10000、bound515477/2500、T≤206。无solver、图生成、Lean或源写入。

运行支持整数线性组合，不独自证明模型行的几何必要性、所有归约完备或一般N(14,5)上界。消费者仍须把有限结论代入已读原证明。非线性横截、partial／mixed blocks及不同邻域规则仍在外；改变条件就要重推模型，不能继续直接套该dual。

## 失败和恢复

字段或系数不同导致assert失败时，返回实际差异，不补造PASS。求解新model需要当前任务的新数学输入和预算，不能因已有replay入口恢复旧MIP。原verifier依赖缺失LP_INPUT且会写EXACT_CHECK；本适配透明重建输入，不在归档中填入伪称原件的新文件。

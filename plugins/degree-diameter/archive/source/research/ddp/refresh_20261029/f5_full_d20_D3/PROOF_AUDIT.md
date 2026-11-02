# 具体F5图的最终证明核对

结论：**PASS，具体公式图的3750点、最大度≤20、直径恰3的Lean见证已完成。** 公开最新纪录仍未确认；磁盘边表文本本身的解析等同性未在Lean中证明。

## 实际声明

命名空间DegreeDiameter.Portfolio.F5Graph3750中的两个无参数、无额外假设定理：

```text
concrete_order_degree_and_D3 :
  card(Fin3750)=3750 ∧ (∀u, graph.degree u≤20) ∧ DiameterAtMost graph3

diameter_exact_three_in_project_definition :
  DiameterAtMost graph3 ∧ ¬DiameterAtMost graph2
```

实际DiameterAtMost定义为∀u v, ∃p:G.Walk u v, p.length≤D。它控制每个顶点对的真实图上walk，不是抽样、单根覆盖或假设存在路由。graph是固定字面controller和F5运算定义的SimpleGraph(Fin3750)。

## 输入、编译与公理

根代理与fresh审阅者分别直接比较controller、matrix、direction、inversePort四组字面数组，均与PARAMETERS.json一致。坐标编码、噪声方向及forward公式与标准库生成器一致。已保存的FORMAL_FINAL_SOURCES十个源文件与对应当前源直接逐字节相同。

FINAL_COMPILE_RESULT.json及逐模块日志覆盖最终成功链：900个控制器单元、4500 NB decoder、500 adjacent decoder均已过kernel检查，随后全对Walk定理及exact3定理均exit0。早期CPU限结束不是成功；后续改变了Array表示和证明项归约方式，最终成功回执单列保存。核验没有重复编译或运行BFS。

两个最终声明的实际#print axioms只有propext、Classical.choice、Quot.sound。没有sorryAx、新增未证公理或native_decide；decide +kernel使用kernel归约。输入绑定和编译输出见FORMAL_INPUT_BINDING_CHECK.json、FINAL_COMPILE_RESULT.json及对应日志。

## 独立语义核对

fresh只读审阅者/root/f5_final_statement_audit（gpt-6-astra，ultra）未看本audit，实际读取最终定义、依赖源、参数、编译日志与独立图验证，结论PASS。审阅者没有执行编译、BFS、生成器或solver。

其关键核对是：所有相邻/不相邻controller分支的前提都由已核证书当场提供；任意源坐标由仿射lemma推广；0→6否证通过Adj↔生成边涵盖全部短walk。没有把旧源D3、引用论文、模型同意或Python输出当作Lean假设。

该语义审阅本身标记same-family/provisional；最终定理的确定性证据是已完成的Lean kernel编译及标准公理输出。之前Gemini的数学对象审阅仍是原范围的外部静态意见，不冒充对新增Lean代码的又一次跨模型检查。

## 验收边界

- 已证明固定参数公式图的完整order/degree-bound/真实Walk直径见证，可记1个已完成的具体公式图Lean实例。旧103图仍未因此形式化。
- Goal明确允许“无向边表或确定性生成器及参数”；当前公式图数据与生成器已对齐，不额外要求Lean内实现文本parser才承认这个图的形式化见证。
- 未声称Lean已解析并验证ASCII边表、所有度数恰等20或mathlib字面ediam等式。这些均不作为本次最大度≤20、直径3见证的隐藏结论。
- 数学实例合法104/4参数、原confirmed主表改善103/3、20D3最新global novelty pending1分别保留。该审计不证明全球纪录或最优性，也不标整个Goal完成。

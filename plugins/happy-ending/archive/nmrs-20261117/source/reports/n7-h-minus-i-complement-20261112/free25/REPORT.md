# 自由25点：h−i=11的完整SAT见证

实际25点染色满足全部767条件，精确 \(h=12,i=1\)。它反驳无条件互补式 \(h-i\le10\)，不反驳75点附加条件版本。[主报告](../REPORT.md)列出全部四角色和H点逐点双蓝五锚。

- [完整颜色](colors.tsv)：2300行，SHA256 `be4ed4f5e23e67825ce902f71998e107ee39f52582920ae4f07a30334c46aa9d`。
- [物理见证](physical-witness.json)：H/I、四角色、12点双锚、全部300端对的每种精确长度和实际路径。
- [独立物理核验](independent-verification.json)：逐CNF子句、packet、R7/B6、全部弱七、精确角色与h−i均通过。
- [公式](formula.cnf)：32891变量、1237062子句，SHA256 `07380efe23389e361fd351f4a06de81769cd5550d6e759875c3732e323c78223`。
- [完整SAT输出](solve.stdout)、[运行记录](result.json)、[精确规格](spec.json)、[源码](probe.py)、[物理核验器](verify.py)。

唯一外部Kissat调用 `--no-binary --time=60 formula.cnf proof.drat` 在24.28秒返回SAT，exit10；墙钟75秒、独立进程组可回收。Linux权威目录为 `/data/ktqiu_hdd/math_agent/reports/n7-h-minus-i-complement-20261112/free25`。Python为 `/opt/anaconda3/envs/forktqiu3/bin/python3.12`；二进制路径及SHA见runtime.json。

schema-audit只是DIMACS结构检查，未独立重建整个公式。SAT核验只从完整颜色重新计算全部实际路径性质，并核验全部赋值子句，因此本例不借助UNSAT解释。运行器继承的状态标签 `VERIFIED_SAT_NECESSARY_SUBDOMAIN` 为历史命名；这里输出本身已是完整自由25点767染色，并非缺少约束的必要核。

复现应复制本目录源码至新的Linux目录运行probe.py（原目录create-only），或者在保留公式与solve.stdout的副本运行 `python3.12 -B verify.py --sat`。后者重新写核验收据。原SAT过程产生的proof.drat保存在权威Linux，不作为任何证明前提；本地不必下载。final-bindings.json列明其原始哈希。result.json中run.stdout的早期空文件绑定发生于最后状态打印之前，最终manifest绑定其最终内容。

发现此例后停止所有新增实验。无外部审查。

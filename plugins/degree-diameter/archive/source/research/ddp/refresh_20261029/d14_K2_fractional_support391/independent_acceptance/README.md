# 独立候选验收源码：尚未编译或执行

check_candidate.cpp只读两个字面边文件，不使用R3/R4缓存、selector、生产侧覆盖结果或哈希。参数顺序为已验94186点/657452边source、94188点candidate。允许无header的u v行，或首个数字行n m；允许#注释。标号固定为0..94185及0..94187。

仅在真实SAT并导出候选后，由root决定编译和执行，例如：

```bash
g++ -O2 -std=c++17 check_candidate.cpp -o check_candidate
./check_candidate SOURCE94186.edges CANDIDATE94188.edges > independent_result.json
```

源码将无向边规范成排序的unsigned vertex pairs。要求source边数恰657452、simple且maxdegree≤14；candidate simple、maxdegree≤14；candidate全部旧旧边与source逐边完全相同；两个新增点94186/94187相邻。结构失败时拒绝并跳过BFS。

结构通过后恰做两个新增根BFS：第一遍同时检查全图连通，两遍均要求全部目标距离≤5。全部旧旧距离≤5明确继承预先验收的source，不重复任何旧根BFS。JSON包含度数直方图、helper度数、两个新根的距离直方图、旧目标/全目标超过5或不可达数、旧边保全和最终接收状态。exit0表示接受，exit1表示候选拒绝，exit2表示输入错误。

本次交付只有源码与此说明：0图读取、0编译、0执行、0BFS。若当前batch UNKNOWN，则不进行候选验证。

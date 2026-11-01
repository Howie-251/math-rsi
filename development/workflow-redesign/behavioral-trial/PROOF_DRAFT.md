# 双配额容量修复：定理与实际调用

## Claim / Status

原命题见[INPUT.md](INPUT.md)。状态：`PROVABLE AS STATED`。这是明确有限实数不等式与一个实例的复用；不建立任何新Property B下界。

来源为本仓 `plugins/propertyb/skills/mathrsi-propertyb/references/mathematics/03-permutations-bad-pairs-and-duality.md` 的“L7．配额可相加，但重叠必须由容量修复”（定理与完整纸面证明）。该引理的源记号 $q_q$在本题映为$b_q$；有限集合、容量、非负数量、配额及非负乘子全部是本题已有假设。$a,w,b$不要求非负。$c_s\ge0$由$0\le z_s\le c_s$自动推出，不添额外条件。

## 一般修复定理

**定理。** 对INPUT中任意满足假设的有限数据，所述weighted-cost bound成立。

**证明。** 定义 $t_s=\sum_{q\in Q}\delta_qa_{qs}$。由每个配额与$\delta_q\ge0$，有限求和交换给
$$\sum_q\delta_qb_q\le\sum_q\delta_q\sum_sa_{qs}z_s=\sum_st_sz_s.$$
对每个槽$s$，若$t_s-w_s<0$，则由$z_s\ge0$得$(t_s-w_s)z_s\le0=c_s\max(0,t_s-w_s)$；若$t_s-w_s\ge0$，由$z_s\le c_s$得同一不等式。因此
$$\sum_q\delta_qb_q\le\sum_sw_sz_s+\sum_s(t_s-w_s)z_s
\le\sum_sw_sz_s+\sum_sc_s\max(0,t_s-w_s).$$
移项得原目标。空索引集合也由空和及相同逐项证明覆盖。这里没有近似、强对偶或最优性假设。$\square$

## 双配额实际caller

令$S=\{s\}$、$Q=\{1,2\}$且所有指定数据为1。每条配额都是$z_s\ge1$，与$0\le z_s\le1$合起来强制$z_s=1$。原题显式选择$z_s=1$确实可行，故检查的不是一个虚拟不可实现配额表。

每个单配额分别应用L7并令其乘子1，得到$w_sz_s\ge1$。两个推论的**左边是同一个成本**，相加只能得到$2w_sz_s\ge2$，不能得到$w_sz_s\ge2$。将共享对象各花费一次正是错误所在；实际可行输入成本为1，直接否定错误加强。

共同应用L7，$t_s=1+1=2$，容量罚项$c_s\max(0,t_s-w_s)=1$，所以修复下界$2-1=1$。

## 消费局部验证并结束原调用

局部verify返回[VERIFICATION.md](VERIFICATION.md)，其中的精确执行与[fresh局部意见](local-review/REVIEW.md)确认上述caller的假设、共享对象及计算，没有需要修复的局部问题。原prove调用读取该回执后继续：把共同修复引理应用到本实例，得到$1=w_sz_s\ge1$；结合本实例可行性，修复界在原输入上有效且取等。两个独立下界各为1只能合成同一成本至少$\max(1,1)=1$，或等价地先得到$2w_sz_s\ge2$再除以2；不能得到同一成本至少2。

因此原任务的一般实数weighted-cost bound及其双配额实际调用均已给出完整论证；错误直接叠加被满足全部前提的原输入严格反驳。该结论不依赖探针样本覆盖全实数，也不宣称运行过正式proof-checker或Lean。$\square$

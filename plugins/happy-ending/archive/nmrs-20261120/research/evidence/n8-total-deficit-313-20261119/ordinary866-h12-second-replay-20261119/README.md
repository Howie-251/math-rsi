<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# H12独立完整重建与第二次实际DRAT

独立完整重建及第二实际DRAT均已PASS；第一实际DRAT也已PASS。
[第二最终回执](../../../../SOURCE_MAP.md#excluded-sources)和
[第二原日志](../../../../SOURCE_MAP.md#excluded-sources)已本地实取回：checker退出0，
恰一个`s VERIFIED`，核验2074.270秒。原普通866≤57现已兑现。
没有调用外部评审，不作sharp性主张。

[原输入桥与信用边界](SEMANTIC_BRIDGE.md)独立列明真实P、来源秩、最初六点
及进口核的范围；本次完整重建没有把新公式的语义必要性藏在hash相等之后。

## 原件与独立性

原query为任意完整有序rank-3普通866输入的全70态真实incoming-P图，预算
H≤12。原公式、proof及第一checker均不改动。第二次运行使用自己新建的
`reconstructed/formula.cnf`和原proof只读路径：

```
<private-artifact-root>
```

两项固定SHA256为：

* 完整CNF：`5d51a77cceb8296381c1ab8cd61c5b52460c5e64a80537d316b067b7803e561d`。
* 原proof：`fabcd1750c8c093ca8c5d84d4caa0d890536ab7d6901aae590a4fdff0654acee`，1160694777字节。

`rebuild.py`是另写的标准库完整编译器，**没有把原body复制为重建结果，
没有使用原作者audit输出作证**。它独立生成70个理想、所有可比pair/triple/
quad及变量编号；验证63个循环的3528组三元六时间序，重建30个共享pivot
支撑；重建全部2165442条base子句；从明确四矩形重建2876个Hall子句；
从2^20色表重新筛选908份合法packet及906份rank有界真实最初六点模板，
并重算全部41958尾部。旧641纯局部核继续作为有冻结hash的数学进口，不
伪称本次又重放了其所有历史局核proof。

实际完整重建结果：
`PASS_INDEPENDENT_COMPLETE_SEMANTIC_RECONSTRUCTION_H12`，70172变量、
2207400子句，与原CNF逐字节hash相同。原body只在生成后用于hash对照。
新编译器源码SHA256为
`cbba54272b11ab7208c3d9f319b2755d05c94c7e14029123334131183a7adb85`。

## 第二次检查与恢复

[Process-control details omitted; historical mathematical status and receipts retain their separate scope.]
为`2f01df83916c158d7da43deefde1ea3ea60b19f5d636ae03f31042e88ef179e9`，
即服务器原权威drat-trim。它与第一checker是不同进程、同一实现；并非
另一实现或外部审稿。启动前已独立重算原proof和重建CNF的两个SHA256。
结束后再次重算两hash，checker实际退出0且恰一个`s VERIFIED`，两hash未变，
最终状态为`PASS_SECOND_FULL_DRAT_WITH_INDEPENDENT_RECONSTRUCTION`。
第一检查的[实际结果](../../../../SOURCE_MAP.md#excluded-sources)和
[原日志](../../../../SOURCE_MAP.md#excluded-sources)另已实取回，核验2034.175秒。

服务端实际`-h`及对应源码显示其`-t0`不会禁用timeout，而是很快TIMEOUT；
本地另一个版本的说明不能覆盖它。因此第二次显式使用`-t2147483647`，
无外部deadline；如实保留内部最大32位秒值，不称二进制真正无限时。
没有改变第一checker的参数或任何原产物。

Linux独占工作根为

```
<private-artifact-root>
```

只读恢复：

```bash
<private-python-runtime> -B status_second.py
```

不要重发`launch_second.py`。主H12与本次第二检查均已自然成功终结，
未改其完整CNF/proof。互补corner/low-rank分支仍保留自己的阶段和原件；
其后续结果不是这次普通57装配的额外前提。

对现有原件的单次手动回放命令（仅供复现，不要与现有进程重复启动）：

```bash
<private-artifact-root> \
  <private-artifact-root> \
  <private-artifact-root> \
  -t 2147483647
```

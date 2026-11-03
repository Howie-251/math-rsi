# 同一 Bhakar104 cohort 的 unlettered(a) / b：实际输入就绪，two-cut scope 未定位旧关闭

状态：**仅 primary/read/input binding 完成，候选枚举未授权或启动。** 本门严格只取同批另外两张104图；旧104c的20904个 two-cut-star NO 仍关闭，不重跑。

## 官方链接的实际情况

当前 [官方 D4 `#44`](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g4.html#44) 仍声明 Nishant Bhakar 于2026-08-27给出三张非同构104点/208边图。描述为13点基 multigraph 的Z8 lift加symmetry-breaking repair，不能用未修补lift替代 literal。

本次 fresh HTML HTTP200，并保存为 `official_desc_g4.html`。其三个链接的**显示文本**为104c、104b、104_unlettered，但第三个实际href仍误指104b；所以绝没有将该href下载两次并重命名成a。

显示名对应的另一个真实官方文件地址也实际HTTP200。为了避免伪造官方命名，本门称它 **a_unlettered**；“a”仅是本轮对照alias，官方文件名不是104a。

| 本轮 alias | 准确官方 raw URL | 实际保存文件 |
|---|---|---|
| a_unlettered | [104_d4D4.txt](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD4/104_d4D4.txt) | `source104_unlettered.author.txt`，1432B |
| b | [104b_d4D4.txt](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD4/104b_d4D4.txt) | `source104b.author.txt`，1224B |

同时保存的 [官方 Sage 原文](https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD4/104_d4D4_SageMath.txt) `official104_SageMath.txt`（HTTP200/10960B）分别列出 `bakhar104`、`bakhar104b`、`bakhar104c`，支持 unlettered 与 b/c 的 cohort 身份。原文给出三者104/208、4正则、D4；本次没有执行 Sage 或自行验证直径/非同构。

所有HTTP状态和URL见 `PRIMARY_DOWNLOAD_RESULT.json`。最初 web-open timeout，随后一次标准库下载流程成功取得上述4个必要primary文件；不关闭TLS校验、不安装库、没有联系作者。

## 唯一一次实际 input binding

两份raw都是**无header、每行两个整数、每条无向边只列一次**的edge list；原labels都是0..103，无需重标。各自仅parse1次完成允许的简单label/edge/degree绑定：104个labels、208条互异非loop边、所有点degree4。

规范化可直接交 root 的文件：

- `source104a.header.edges`：对应 a_unlettered，不是官方额外命名；
- `source104b.header.edges`：对应 b。

两者均保原labels，首行 `104 208`，随后lex排序的 `u<v` 边。绑定结果保存在 `INPUT_BINDING_RESULT.json`。D4和同批非同构是primary继承，未作新BFS、R3、source diameter或isomorphism计算。

## 旧 scope 检索与下一决策边界

有限本地检索覆盖source文件名、canonical experiment条目及原始md/INPUT/PRED/SCOPE/RESULT/py中的a/b/unlettered标识，未定位这两张literal上的完整 two-cut4star NO或已执行UNKNOWN。实际找到的旧完整 two-cut case是 `breadth_20261027_wave2/extension105_d4`，其 `inputs.json` 明确固定104c；相邻split及split/absorb旧case同样明确104c，不能外推本a/b。

“本次未定位”不是无人尝试或全球优先性的证明，也不是一般105图可行性结论。当前两份实际输入可在 root **另定一次有限联合预算**后比较；本门不自行启动。

对任一这两份4正则104源，删除两条不交原边、添新点连四端点，度账为105/210全4正则。四端点P包含全部被删边两端，故删除不改变 `d(P,t)`；新根R4当且仅当源closedR3(P)覆盖104。旧旧D4仍须后续完整候选检查。该数学条件未在本门计算任何一例。

本门不改选第三种source、不重新计算104c，不展开其它机制。新增source-reproduction仅作输入，不计新图/参数/Lean；候选/距离球/BFS/solver均0。

native下载进程CPU0.044095855秒，唯一input-binding进程0.001059767秒，合0.045155622秒；检索/文档准备保守charge0.25，total0.295155622/1.5秒。完成只读准备后停止。

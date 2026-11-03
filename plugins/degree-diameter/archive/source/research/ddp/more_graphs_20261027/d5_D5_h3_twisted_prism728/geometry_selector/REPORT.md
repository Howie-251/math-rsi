# H3 twisted-prism 的真实坐标与唯一反射 selector

本文件只记录 source/坐标绑定和几何 selector，没有另建图或 BFS。唯一实际 728 图由 source_scout 生产；其首根 R5 失败、结合通用 upper6 得精确 D6，因此本次候选没有超过 (5,5)=650。

## 真实 source 与坐标

沿用自然 H3 极性图 [364/714 literal](../../d4_D5_polarity_extensions/source_and_single/source364.edges)，不是另一个 364/728 全 4 正则公开图。实际自然源有 28 个 degree3 absolute ports、336 个 degree4 点；旧 D5 直接继承已保存的 polarity 几何证明，不重验。

Q_data 的 H3_point_representatives 按当前 364 label 顺序选择 h9 point_coords.u8.bin 的 7-byte tuples。选中坐标全部在 F3 中，364 个互异、规范化的坐标恰为

~~~text
Q(6,3): x0*x4+x1*x5+x2*x6-x3²=0
~~~

的全部 projective points。不是从 364=28*13 猜模型。对应 label 坐标小缓存为 [POINT_COORDS_BY_VERTEX.u8.bin](POINT_COORDS_BY_VERTEX.u8.bin)。

源 28 个 cached B2 classes 各 13 点；实际逐类 rank=3，且恰等于其三维向量空间的全部 13 个 projective points、全部 singular。[B2_PLANES](B2_PLANES.json) 保存实际成员及 basis。没有为此重做球或 BFS。

## 事前修订 selector 与实际计数

最初只偏好 pi(F)∩F 为空的反射，尚未运行、尚未有图时，父代理加入了更强必要 route 筛：若反射逐点固定两个 port 的 B2 球，其 twisted prism 必 D6，故先排该类。旧未执行预测保在 UNEXECUTED_PRIOR_PREDICTION.json，新 [PREDICTION](PREDICTION.json) 在唯一计数前冻结。

对 729 个 normalized anisotropic projective normals v，反射为

~~~text
R_v(x)=x-B(x,v)/Q(v)*v, then projectively normalize.
B(x,v)=x0v4+x4v0+x1v5+x5v1+x2v6+x6v2+x3v3.
~~~

实际结果：

- 378 个 Q(v)=2 normals，每个恰点态固定两个 B2 球，按必要 route 障碍排除。
- 351 个 Q(v)=1 normals，每个没有固定完整 B2 球，保留作为 selector 范围。
- ports overlap 分布为 12:378、7:288、28:63；空 overlap 为 0，原偏好在此反射族中无法实现。

按新规则“先 fixedballs<2，再最小 port overlap，再 tuple lex”，唯一 normal 为 (0,0,1,0,0,0,1)，Q=1。其反射可简单写成 x2→−x6、x6→−x2，其它坐标不变。真实 pi364 是 involution、保持全部 Q 点，固定 ports 为 24,116,230,249,267,298,320；恰 7 个 port 留在 port 类，其余 21 个 port 映到 degree4 点。因此它不可能是源图 Auto（Auto 必保度），不是 arbitrary label shuffle。

完整 [REFLECTION](REFLECTION.json) 已在任何图生成前给唯一 producer。selector CPU 0.117300399 秒，硬 RLIMIT_CPU 1 秒；0图/源BFS。没有再按图的坏对挑反射或改 selector。

## 生产结果的范围

source_scout 只对上述一个 pi 生成 two-copy source 加 matching 的 728 点、1792 边、maxdegree5 图。首根 0 的 R5 缺 78 个 cross targets，首个为 (layer1,old84)。任何这种 two-copy source matching 图都有 diameter≤6，而此缺项给 diameter≥6，故该唯一候选精确 D6；本 selector 没有重复验图。结果只否定这个 canonical pi，不排全部 351 个剩余反射或其它跨层匹配。378 个 fixed-two-B2 类由独立条件 theorem 关闭，不能把这个数量与实际构图次数混为一谈。

全部几何计数与生产证据应合并同一 twisted-prism raw 记录，不另算一种独立方法。下一步若无明确新授权，不换反射、不追坏点、不追加图。

证据：[完整 selector 结果](RESULT.json)、[729 条记录](SELECTOR_RECORDS.json)、[复现入口](select.py)。生产报告/独立 route proof 由同目录上级的 owner 管理。

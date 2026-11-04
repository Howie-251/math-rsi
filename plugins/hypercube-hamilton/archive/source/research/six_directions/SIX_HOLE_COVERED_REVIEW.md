# 六孔已覆盖目标条件归约：独立审计

**结论：PASS，same-family / provisional。** 用户指定 GPT-6.1-sol、high，覆盖 proof-checker 默认配置。S9 四子情形及 C6-covered 的全称拼接逻辑均可闭合，未发现本地 FATAL、CRITICAL 或其他实质问题。**该结论仍以未证 A4 为条件，完整 P6 未证明。**

完整审读 SIX_HOLE_COVERED_REDUCTION.md；复用刚独立审读的 K4、S7、N10、S4、Z18 及相关依赖，另读 TWO_ODD_HOLES_TRANSFER.md 中 N14 的精确陈述和证明。这里只检查既有输入在本次应用处的假设，不递归重新认证全部外部文献。未重新运行几何枚举。旧几何审计及主证明、台账、census 均保持不变。

## 关键结论

- D 可能接触跨端口 v，原文已正确处理：删 D 仅可能孤立 v，立即接回真实 vh；因此 T_v 可以只有一条边。其他内部顶点不可能因删除匹配而孤立。
- 根 u 在 A 时，D 非空且属于原 Hamilton u-v 路径；删除后 u、v 必在不同分量。接入互异的新 B 端点不会把旧分量连在一起或产生圈，故确有不同的两条终端路径。
- 唯一重合点 y 的修复删除 yk、yd 并添加 kd。加辅助 ur 或 r-s-prime 后，N14 的两个孔始终是同偶 q、y；没有偷偷限制 r 或 s-prime 的奇偶。删辅助边得到指定的 B-y 路径，再展开 kd 恢复 y 一次。
- K4 处四孔确实平衡；其允许 D 任意完整图边，涵盖 D 覆盖目标 v 的情况。N10 各次调用都以偶 y 为与另一孔 q 同奇偶的目标。
- 任取分开 z、q 的坐标，目标侧一偶孔对应奇孔数 1/2/3/4，分别由 S7/S4/S4/S9 处理。不存在漏类或循环依赖。

## 微义务

- **C6-01**：Normalize root parity by cube translation acting on all data. Since M is short its six holes split three even/three odd; covered target is a distinct odd vertex.
- **C6-02**：An adjacent pair among non-root holes can be added as a short matching edge, keeping u free and v covered; Z18 supplies the requested path for this four-hole supermatching.
- **S9-01**：The S9 cut has z in A and q in B while the three odd holes and v are all in A. Candidate y=w xor e_i is even and cannot equal q by preprocessing.
- **S9-02**：If u is in B, at most one of the three distinct candidates equals u; otherwise none are holes. A nonhole candidate is internally M_B-covered since its unique crossing neighbor is an original odd hole. Choose such a y, outside X_B and different from all original holes.
- **S9-03**：For u in B, A holes have even-minus-odd count -2. Equal internal parity coverage forces |X_A even|-|X_A odd|=2, so c is even >=2 and an even port a exists.
- **S9-04**：Y=(X_A minus a) plus w has even size c; D is a legal matching on uncovered vertices of M_A. Its union with M_A has exactly balanced four holes a,z,s,t.
- **S9-05**：K4 applies in dimension five with free even root a and odd target v. If v crosses, v belongs to Y since a is even, and D covers v. If v is internal, M_A covers v. No shortness/bipartiteness of D is assumed.
- **S9-06**：Removing matching D from an a-v Hamilton path cannot isolate any internal vertex; the only possibly isolated vertex is v when v belongs to X_A. Each deleted-D incidence supplies an exposed endpoint. Every port receives its distinct real crossing edge, including vh at isolated v, and w receives wy.
- **S9-07**：Appending fresh, pairwise distinct B endpoints to a path forest cannot create a cycle or connect distinct A components. Degrees leave v and X_B plus y as endpoints. Hence there is exactly one v-terminal path T_v and the other components compress to R on (X_B plus y) minus r.
- **S9-08**：3a r=y: R covers all X_B, disjoint from M_B. L_B has precisely two even holes u,q. N10 root u and covered target y satisfy y distinct from u and parity(y)=parity(q).
- **S9-09**：3a: expand R and append T_v at y. T_v interior lies in A, its only B vertex is y, so the result spans all vertices once and retains all original matching edges.
- **S9-10**：3b r in X_B: y is the sole overlap of M_B and R. k=M_B(y) is internally covered, while d=R(y) belongs to X_B minus r. Therefore k,d,y,u,q,r are distinct where required; kd is a legal replacement.
- **S9-11**：3b: removing yk and yd then adding kd leaves precisely holes u,q,r,y. The auxiliary ur joins two holes, leaving only same-even holes q,y.
- **S9-12**：3b: N14 with designated omitted hole y gives a 31-vertex B-y cycle containing ur and kd; ur and kd have disjoint endpoint sets. Deleting ur yields a u-r path retaining kd, regardless of parity(r).
- **S9-13**：3b: expand kd to k-y followed by the y-d transfer segment, restoring y once and its original edge ky. Expand other R edges, then append T_v at r; no artificial long edge remains.
- **S9-14**：For u in A, A has five original holes and B has only q, hence c is odd and >=1. D on X_A plus w has size (c+1)/2>=1, disjoint from u. M_A+D has exactly balanced holes u,z,s,t.
- **S9-15**：K4 applies with free even u and odd covered v, including when D covers v. Nonempty D belongs to the Hamilton u-v path, so deleting it separates u and v; only v can become isolated and real vh immediately attaches it to B.
- **S9-16**：After adding true crossing edges and wy, all B endpoints are distinct and fresh. The components remain a forest: one u-terminal component ending at r, one v-terminal component ending at s-prime, and compressed R on remaining endpoints. In particular r is distinct from s-prime.
- **S9-17**：4a y is one terminal B endpoint, other endpoint b belongs to X_B. R covers X_B minus b and is disjoint from M_B; L_B has exactly holes q,b.
- **S9-18**：4a: N10 with free root b, other hole q and target y applies since y is even like q and y differs from b. No assumption on parity(b) is needed. Orient its Hamilton b-y path to connect T_u and T_v, expanding R.
- **S9-19**：4b: y is covered by R, with d in X_B minus r,s-prime. Sole-overlap repair gives precisely holes q,y,r,s-prime; internal partner k is outside ports and all these holes.
- **S9-20**：4b: adding auxiliary r-s-prime leaves same-even holes q,y. N14 omitting y produces a cycle containing both auxiliary r-s-prime and replacement kd; deleting the former produces a spanning B-y r-s-prime path.
- **S9-21**：4b: expand kd and all remaining R edges, recovering y once. Attach the two terminal components at r,s-prime. Their interiors are disjoint and cover all A vertices together with R expansions, so the final result is a single Hamilton u-v path containing M.
- **C6-03**：For any coordinate separating distinct even holes z,q, the target half of M*=M-vh+hu has exactly one even hole and 1,2,3,or 4 odd holes. Values 1,2/3,4 invoke respectively S7,S4,S9. This does not require a further coordinate or geometric census.
- **C6-04**：A4 -> K4 -> S9 uses N10 and N14, while A4 -> S4,S7 are prior inputs. C6 combines these and Z18. Neither K4 nor N14 nor S9 uses C6, and G6 is unnecessary: no dependency cycle.
- **C6-05**：Only covered odd targets were used; the theorem remains conditional on A4 and named imported theorems. Six-hole free targets and larger hole counts are not consequences. The earlier twelve representatives remain the accurate exceptions to S4/S7 alone.

## 依赖、反例检查及未关闭范围

- External FM2/FM8 -> N10,N14
- A4+N10 -> K4
- A4 -> S4,S7 via previously checked inputs
- K4+N10+N14 -> S9
- Z18+S4+S7+S9 -> C6-covered

对抗性检查包括 v 跨边、D 末边删去后的孤立 v、最小跨边数、任意长辅助边、终端端点任意奇偶、桥端 y 在终端路径或 R 中、候选等于根等边界。未发现反例；此判断依据明确的森林、孔集和展开论证，不依据未穷尽的路径计算。

本次共有 26 项微义务。K4、S9、S4、S7、C6-covered 均保留 A4 条件；A4、消辅助边 E3、六孔自由目标及完整 P6 保持 open。

旧 G6 的十二几何代表仍准确描述 S4/S7 单独的例外；新 S9 在 A4 下继续覆盖它们，因此它们已不再是六孔已覆盖目标条件性归约的残余。此范围更新不需要改写旧审计所审文件版本。

## 实际输入 SHA256

- `SIX_HOLE_COVERED_REDUCTION.md`: `sha256:c80fb9e0cdad9c146fe5bac594b321b41fe5f0646dae9b98e3d64e6463be9837`
- `SIX_HOLE_MIXED_AND_GEOMETRY.md`: `sha256:9c4450060f472b54397a337c9d2128a26d31077b677c35b0a0669fb1d3022e68`
- `GENERAL_NEAR_PERFECT.md`: `sha256:bafaea9040f4a677687aa21abee661bb9fa44db9d9ce33879e288a6a9d90ea55`
- `TWO_ODD_HOLES_TRANSFER.md`: `sha256:d88d6f27357e776d8d9b4638812dd091f636d643cc9f4f42c98442348f0a577c`
- `FOUR_HOLE_FULL.md`: `sha256:a3c7dbe56246d1853ddc601ac7c5f5d07d0bf2dcf12cf9e47553397a5d0b73da`
- `SIX_HOLE_FOUR_AUX_REDUCTION.md`: `sha256:3b9e7f667c7661358f6668b2e0ae5c60e59fc156944e80dd0d53fe74c3672d49`
- `AVOIDED_VERTEX_TRANSFER.md`: `sha256:f44623960b51f85549ea15b6b7c8262222c097f56c37ae10c05b77b6dd8776a7`
- `DISTANCE_TWO_ALL_TARGETS.md`: `sha256:41b5514d63a43bd0e1e1fd47453532f8264dccf23f454b56623c74a82e5654a6`
- `paper.txt`: `sha256:e7036badbca184e006a075e569772520aadfb6514f1a42b68840838eba8f887f`
- `F:\c4free-hypercube-main\ARIS\skills\skills-codex\proof-checker\SKILL.md`: `sha256:b234e51e41c8d92b1ff79a0a11750bbcc34a01ebc123eaf2439715b1ac22915a`

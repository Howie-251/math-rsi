# 六孔自由端点条件归约：独立审计

**结论：PASS，same-family / provisional。** 依用户指定采用 GPT-6.1-sol、high，覆盖技能默认模型/推理配置。全文逐项审读后，C6-free 六类及全部桥端子情形未发现本地数学缺口。结合已审 C6-covered，得到 **A4 ⇒ 完整六孔端点结论**。A4 本身及完整 P6 均仍未证明。

仅写本次 SIX_HOLE_FREE_REVIEW.md/.json，先前几何和 covered 审计保持不变。复用已独立审读的 K4、N10、N14、Z18、A4 及五方向输入，逐次重新核对应用假设；没有重新进行几何或匹配枚举，也未递归重证全部文献链。

## 核心核查

- 第3a节 y 为终端时，另一终端 b 奇偶任意。L_B−yk+kb 确将孔 b 换为奇孔 y，故 A4 的孔恰为 q 偶及 w、t、y 奇。删 kb 接 ky 给出全 B 的 b-y 路径；这里没有误用平衡四孔 K4。
- 每个 D 都避开路径端点。根在 A 时 D 非空，删 D 必将 u、v 分开；接入互异 B 端点保持森林结构，因此终端段不会误合并。自由 v 不属于端口或 D，不出现孤立 v。
- 两种桥均有内部覆盖点 y：z 的镜像奇 y 与 w、t 的相邻关系由预处理排除；w/t 的镜像偶 y 至多一个等于根 u，可以改选另一个。
- 冲突只发生在 y，修复后逐支孔集正确。临时加 rs 或 ur 的端点都是自由点，且不接触 kd；删辅助边后 kd 仍保留供展开，y 只恢复一次。
- N10 仅要求目标 y 与另一个孔 q 同奇偶，不要求自由根 b 的奇偶固定。NC 则只用在 q、t 异奇偶双孔上。
- 选任一坐标分开 z、q 后，目标面奇孔数只能为1、2、3；与根两侧相交恰六类，且所有 y 在终端/R 中的子情形齐全。

## 微义务

- **F01**：Short M with six holes has three even and three odd holes. Translation can normalize u even, and the other free opposite-parity endpoint v is one of the three odd holes.
- **F02**：Adding a short edge between non-root holes keeps u free, yields a four-hole supermatching for Z18, and may cover v legally because Z18 allows either free or covered targets.
- **F03**：Distinct even holes z,q have a differing coordinate. After relabeling there is exactly one non-root even hole z in A and q in B; A contains one, two, or three original odd holes including v.
- **F04**：If c=0, all M edges avoid coordinate i. The five-direction theorem applies to Q6 with free u and opposite-parity v; all C1-C3 obstacles require u covered and hence fail.
- **F05**：NC applies only to a complete-graph matching with two opposite-parity holes. A short-neighbor target of one hole has parity of the other; N10 gives a full 32-vertex path and the short endpoint edge closes it without duplicating a path edge.
- **F06**：Every D is supported on currently M_A-free ports and optional original hole z or w. It avoids chosen path endpoints u,v or a,v. Matching deletion cannot isolate an internal path vertex, so all resulting segments are nontrivial.
- **F07**：When u lies in A, each indicated D is nonempty and included in P_A. Deleting it separates u and v. Appending mutually different fresh B endpoints by real cross-edges and the chosen bridge neither joins old A components nor creates a cycle.
- **F08**：The resulting terminal components and R-partition cover A vertices exactly once. Distinct terminal B endpoints are omitted from R; all other ports and the bridge endpoint are in R. This proves connectivity after the local B path is attached, beyond mere degree counts.
- **F09**：If y is internally covered in B and also covered by R, it is the sole overlap. k=M_B(y) is outside ports, holes and terminal endpoints; d=R(y) is a nonterminal cross-port. Replacing yk,yd by kd gives a legal complete-graph matching.
- **F10**：The replacement kd is always distinct from and endpoint-disjoint from the temporary terminal-joining auxiliary edge. It survives deletion of that edge and expands to ky followed by the y-d transfer segment, restoring y once and all original matching edges.
- **F2a-1**：A holes u,z even and v,w odd give even c. Removing the c=0 case yields c>=2. D pairs X_A, hence is nonempty and disjoint from u,v. M_A+D has balanced four holes for K4 u-v.
- **F2a-2**：R covers X_B minus distinct r,s. M_B+R has holes q,t,r,s. Add rs, leaving exactly opposite-parity holes q,t, apply NC, delete rs, expand R and attach terminal paths. No parity assumption on r,s is used.
- **F2b-1**：A holes z even and v,w odd force excess one even port, hence odd c>=1 and an even a. D pairs X_A minus a and may be empty; four holes z,a,v,w are balanced for K4 a-v.
- **F2b-2**：With one terminal r-v, R covers X_B minus r. B matching M_B+R has holes u,q,t,r. Add ur, apply NC to remaining q,t, delete ur and attach terminal path at r.
- **F3-1**：For y=z xor e_i, y is odd and differs from w,t by nonadjacency preprocessing and from u,q by parity. Its unique crossing neighbor z is free, so y is internally M_B-covered and is not a port.
- **F3a-1**：A holes u,z even and v odd force odd c>=1. D pairs X_A plus z, is nonempty and avoids u,v. M_A+D has precisely holes u,v, and N10 root u, target v applies.
- **F3a-2**：If y is terminal and other terminal b is a port, R covers X_B minus b and M_B+R has holes q,w,t,b. k=L_B(y)=M_B(y), since R omits y. b differs from k,y,q,w,t because b is a cross-port.
- **F3a-3**：Replace yk by kb: the free hole b is filled and y is freed, irrespective of parity(b). The four holes become exactly even q and odd w,t,y. A4 omitting y gives a 31-cycle containing kb.
- **F3a-4**：Delete kb and append original edge ky at k, obtaining a full B b-y Hamilton path containing every L_B edge. No K4 is invoked in this possibly unbalanced four-hole case. Expansion and orientation attach the two terminal paths.
- **F3a-5**：If y is in R, unique-overlap repair has exactly six holes q,w,t,r,s,y. Add rs, leaving q even and w,t,y odd; A4 omits y. Delete rs, expand kd to restore y, then expand all other R and attach terminals.
- **F3b-1**：A holes z even,v odd force equal port parity counts. After c=0 is excluded, c>=2 and an even a exists. D pairs (X_A minus a) plus z and avoids a,v. Its union with M_A has holes a,v; N10 yields a-v.
- **F3b-2**：If r=y, R covers all X_B and M_B+R has balanced four holes u,q,w,t. K4 applies from free even u to internally covered odd y; expand and append terminal y-v.
- **F3b-3**：If r is a port, unique-overlap repair has six holes u,q,w,t,r,y. Add ur to leave q even and w,t,y odd. A4 omits y; delete ur, expand kd restoring y, and append terminal path at r.
- **F4-1**：Choose among mirrors of w,t an internally M_B-covered even y. Neither equals q by preprocessing; at most one can equal root u if u is in B. The selected nonhole candidate has a free cross-neighbor, hence cannot be a port.
- **F4B-1**：With u in B, A holes z even and v,w,t odd force excess two even ports, hence c even>=2 and even a. D pairs (X_A minus a) plus w, yielding balanced holes a,z,v,t; K4 a-v applies and D avoids endpoints.
- **F4B-2**：If r=y, M_B+R holes are same-even u,q. N10 root u to even covered y is valid because parity(y)=parity(q). No false opposite-parity-root requirement is imposed on N10.
- **F4B-3**：If r is a port, repair holes are u,q,r,y. Add ur to leave same-even q,y. N14 omits y; delete ur and expand kd to restore y. Parity(r) need not be fixed.
- **F4A-1**：With u in A, A holes u,z even and v,w,t odd force odd c>=1. D on X_A plus w is nonempty and avoids u,v, giving balanced holes u,z,v,t for K4 u-v and distinct terminal endpoints r,s.
- **F4A-2**：If y is terminal, other terminal b is a port. M_B+R holes are q,b; N10 root b and target even y requires only parity(y)=parity(q), not any parity restriction on b. Expand R and attach terminals.
- **F4A-3**：If y is in R, repair holes are q,y,r,s. Add rs to leave same-even q,y; N14 omits y. Delete rs, expand kd restoring y, and attach terminal paths. All auxiliary edges are deleted or expanded.
- **F30**：All three possible counts of A odd holes and both possible root sides are covered, with every bridge endpoint either terminal or in R. D never contains free v, so the covered-target isolated-v boundary does not occur.
- **F31**：Free proof uses A4->K4, N10, N14, NC, Z18 and five-direction theorem, not C6-covered. Only after proving C6-free is it combined with previously checked C6-covered to obtain A4=>all six-hole endpoints; no circular use of this conclusion occurs.

## 依赖与未关闭义务

- N10 -> NC
- A4+N10 -> K4
- A4+K4+N10+N14+NC+Z18+five-direction theorem -> C6-free
- C6-free+C6-covered -> A4-conditional complete six-hole endpoint conclusion

本次 32 项微义务闭合。未发现循环：C6-free 不以 C6-covered 为输入，二者只在最后合并。未使用枚举证明任何路径存在性。

A4、消辅助边 E3 及完整 P6 保持 open。此前 covered 审计记录的“六孔自由目标尚未归约”现在由本次新的条件性定理推进；先前报告不作回溯修改。一般八孔及更多孔仍在本归约范围之外。

## 实际输入 SHA256

- `SIX_HOLE_FREE_REDUCTION.md`: `sha256:c04a1f090b51f19ea68db7f7a90d7ab1c7c9ed79feb1549898c4a3b4be88b8e4`
- `SIX_HOLE_COVERED_REDUCTION.md`: `sha256:c80fb9e0cdad9c146fe5bac594b321b41fe5f0646dae9b98e3d64e6463be9837`
- `SIX_HOLE_MIXED_AND_GEOMETRY.md`: `sha256:9c4450060f472b54397a337c9d2128a26d31077b677c35b0a0669fb1d3022e68`
- `GENERAL_NEAR_PERFECT.md`: `sha256:bafaea9040f4a677687aa21abee661bb9fa44db9d9ce33879e288a6a9d90ea55`
- `TWO_ODD_HOLES_TRANSFER.md`: `sha256:d88d6f27357e776d8d9b4638812dd091f636d643cc9f4f42c98442348f0a577c`
- `FOUR_HOLE_FULL.md`: `sha256:a3c7dbe56246d1853ddc601ac7c5f5d07d0bf2dcf12cf9e47553397a5d0b73da`
- `SIX_HOLE_FOUR_AUX_REDUCTION.md`: `sha256:3b9e7f667c7661358f6668b2e0ae5c60e59fc156944e80dd0d53fe74c3672d49`
- `paper.txt`: `sha256:e7036badbca184e006a075e569772520aadfb6514f1a42b68840838eba8f887f`
- `F:\c4free-hypercube-main\ARIS\skills\skills-codex\proof-checker\SKILL.md`: `sha256:b234e51e41c8d92b1ff79a0a11750bbcc34a01ebc123eaf2439715b1ac22915a`

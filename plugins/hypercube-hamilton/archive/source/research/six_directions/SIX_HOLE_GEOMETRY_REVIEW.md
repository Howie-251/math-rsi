# SIX_HOLE_MIXED_AND_GEOMETRY 独立审计

结论：**PASS（仅对明确的条件性陈述；same-family / provisional）**。用户指定 GPT-6.1-sol、high，覆盖 proof-checker 的默认 Astra/ultra。独立审读全文，未发现需要修改主证明的数学错误。K4、S8、S7 依赖未证 A4；G6 的几何分类不依赖 A4。A4、消辅助边 E3、完整 P6 均未关闭。

审计范围：对列出的依赖检查本次应用的假设，不递归重证所有既有文献输入；paper.txt 实际审读 Theorem 8 与 C1–C3。仅写本审计 MD/JSON，未修改主证明、台账、census 脚本或数据。

## 微义务与核验

- **K4-1**：F arbitrary complete-graph matching; a even by parity-changing translation; no bipartiteness assumption is used.
- **K4-2**：Free y: adding ay leaves an opposite-parity two-hole matching; N10 root at one remaining hole and short-neighbor target has parity of the other. Closing and deleting ay preserves all F.
- **K4-3**：Covered y: replace yk by ka. Hole set replaces a by y independently of parity(k), hence one even and three odd holes. A4 can omit y.
- **K4-4**：Opening ka and restoring ky recovers all original long edges; choosing a short-neighbor y closes a 32-vertex path to a cycle without duplicating its endpoint edge.
- **PRE-1**：An adjacent non-root hole pair can be joined while keeping u free; Z18 applies to the resulting short four-hole matching for the same opposite-parity target.
- **PRE-2**：For each candidate mirror of a B odd hole, the original cross-neighbor is free; absent original hole adjacency it is internally covered unless it is u. After replacement only at most one of three candidates can be a cross-port; at least two are internal.
- **S8-1**：A has one hole v, so c is odd. F=M_A*-bk has no half-layer and within A minus v,b has Y=X_A plus k, with even size c+1>=4.
- **S8-2**：N12 supplies W; k pairs with a in X_A. D=W-ak avoids a,b and N11 compression is precisely F+W, with v odd and b even.
- **S8-3**：Removing matching D from a-b path yields nontrivial vertex-disjoint segments. Real cross-edges and bw yield R on X_B plus w, disjoint from M_B*. The remaining holes are z,q,s,t, balanced for K4.
- **S7-1**：For c>=2, F has Y=X_A plus z,k of even size >=4. W(k) lies in X_A or is z. N11 applies also when a=z; endpoint set after deleting D is X_A plus z,b.
- **S7-2**：y=z xor e_i is odd, is not a B original hole or u,h, and is internally covered; hence R and M_B* overlap exactly at y.
- **S7-3**：r=M_B*(y) is outside R endpoints, d=R(y) is outside M_B* endpoints other than y; replacing yr,yd by rd is legal. Exactly q,s,t,y become holes, of type one even/three odd.
- **S7-4**：A4 omits y; rd expands as ry followed by y-d transfer segment. Every A-v vertex and B vertex is recovered once, including any real long cross-edge hu.
- **S7-5**：For c=0, a=z and D empty. Tb free of half-layers is exactly the N11 condition; no use of N12 with two free points is made.
- **S7-6**：At most one half-layer is possible in M_A*: a half-layer forces all short edges into its direction and both half-layers of that direction would cover free v.
- **S7-7**：For c>=2, no half-layer or a half-layer touching an internally covered candidate yields the first-stage deletion. A noninternal candidate cannot touch a matching half-layer, so the residual real half-layer avoids all three candidates.
- **S7-8**：For c=0 and hu in A, v,h,u all lie in A: otherwise original vh is a remaining true cross-edge. All original M edges avoid cut i. paper.txt Theorem 8 applies with n=6, at most five directions; C1-C3 all require u covered and thus fail.
- **S7-9**：For c=0 and hu in B, M_A*=M_A is short, with holes v,z; the three even candidates have distinct short matching edges and odd partners.
- **S7-10**：If each Tb has a half-layer, each contributes >=7 old short edges; Te retains >=6 of them. All its short edges must follow its half-layer direction, forcing common direction. Omission of v forces the same half-layer H.
- **S7-11**：The common H avoids every candidate b. In Te for e!=b, bk_b is retained, so k_b cannot be in H. Thus zk_b cannot be in H, which proves H is contained in original M_A and avoids z as well as v.
- **S7-12**：The complement of H gives equal j-bits for z and all candidates, opposite the j-bit of v. Since j!=i, these are exactly the j-bits of w,s,t.
- **S7-13**：E2 applies to the same complete-graph matching M* omitting v, n=6>=4. Recut target side A_j has no half-layer and at least eight real cross-edges; z,w,s,t are on its opposite side.
- **S7-14**：Only q may join v after recut. If q does, invoke already-proved first-stage c>=2 case; otherwise one-hole side has odd c>=9 and invokes already-proved S8. No recursive appeal to S7.
- **G6-1**：For any differing coordinate of z,q, nonconstant W gives one/two W points on each target side, hence S4. Thus W is constant on every coordinate in D. Three distinct same-parity points require >=3 remaining coordinates; positive even |D| is therefore two.
- **G6-2**：Translation by even z preserves parity and adjacency, permutation sends q to 3; low-bit r=3 is reduced by xor3 exchanging even holes, and r=2 by swapping low coordinates. All reductions act on v and u too.
- **G6-3**：r=0 forces all high words to weight three. r=1 permits only weights two/four. Three edges on four vertices have precisely triangle, star, path types; with the weight-four word the remaining two edges are adjacent or disjoint. Six rows exhaust W.
- **G6-4**：High columns give S4 iff v_j=1 and c_j=2; low columns add S7 exactly when v_i differs from r_i. Include v odd and outside W. Table yields 1+1+5+2+2+1=12 pairs, without claiming minimal target/root orbits.
- **G6-5**：The chosen root is any even point outside the two non-root even holes, at most 30; it is not enumerated. No matching feasibility assertion or path-existence conclusion follows from the geometry enumeration.

## 依赖与作用域

- A4+N10 -> K4
- K4+N11+N12 -> S8
- A4+N11+N12+E2+five-direction theorem+S8 -> S7
- bit counts+four-vertex graph classification -> G6
- Z18+S4+S7+G6 -> conditional residual geometry

上述 DAG 无环。重切后的分支调用已先行证明的 S7 第一阶段或 S8，未将完整 S7 当输入。A4 全程以完整图四孔命题使用，没有暗中要求原匹配二部。Z18 仅用于添加非根孔间短边后的四孔实例。五方向分支中原根 u 仍自由，因此 paper.txt 的三个 C 障碍均不存在。

## 独立计算复核

另写内存 Python，直接按每坐标、每侧构造孔数与目标掩码；没有运行会写入 census JSON 的原脚本。复得全部 1,198,860 个几何输入，其中 S4 覆盖 1,188,480，S4 外 10,380，S7 新覆盖 8,010，最终 2,370。独立枚举四点图三边得到三个类型，并逐行复核无 S4 目标数 4,4,29,8,8,2，以及余下目标 [4]、[1]、[1,25,41,49,61]、[1,37]、[1,37]、[1]。

这是 z=0 后非根孔—目标几何域的穷尽；不是匹配穷尽，也不验证任何未证路径义务。十二代表并非匹配数或最小同构类数。任意合法偶根及任意原短匹配仍需处理。

## 对抗性核查与未关闭义务

检查了 K4 长边与伙伴任意奇偶、自由/覆盖目标、S7 a=z、D 空、hu 真跨边、候选等于根/变端口、零跨边 hu 在 A/B、三个 Tb 同时有半层、重切后 q 两侧及 G6 极端重量模式。未发现反例；未把无反例等同于证明。没有开放的本地 FATAL/CRITICAL 缺口；A4 是显式假设，不是已证结论。

A4、消辅助边 E3、残余十二几何的全称匹配结论、六孔自由目标及更多孔均保持 open，完整 P6 未证明。

## 实际输入 SHA256

- `SIX_HOLE_MIXED_AND_GEOMETRY.md`: `sha256:9c4450060f472b54397a337c9d2128a26d31077b677c35b0a0669fb1d3022e68`
- `GENERAL_NEAR_PERFECT.md`: `sha256:bafaea9040f4a677687aa21abee661bb9fa44db9d9ce33879e288a6a9d90ea55`
- `AVOIDED_VERTEX_TRANSFER.md`: `sha256:f44623960b51f85549ea15b6b7c8262222c097f56c37ae10c05b77b6dd8776a7`
- `DISTANCE_TWO_ALL_TARGETS.md`: `sha256:41b5514d63a43bd0e1e1fd47453532f8264dccf23f454b56623c74a82e5654a6`
- `FOUR_HOLE_FULL.md`: `sha256:a3c7dbe56246d1853ddc601ac7c5f5d07d0bf2dcf12cf9e47553397a5d0b73da`
- `SIX_HOLE_FOUR_AUX_REDUCTION.md`: `sha256:3b9e7f667c7661358f6668b2e0ae5c60e59fc156944e80dd0d53fe74c3672d49`
- `paper.txt`: `sha256:e7036badbca184e006a075e569772520aadfb6514f1a42b68840838eba8f887f`
- `six_hole_geometry_census.py`: `sha256:72f925af18b8c519187e99ee80ffda9e54f333b51d07644387541e354c44a7ec`
- `six_hole_geometry_census.json`: `sha256:c24b32046c0be1b35bf768e832455ea7e12837e75d80b61156a11e47b68d4786`
- `F:\c4free-hypercube-main\ARIS\skills\skills-codex\proof-checker\SKILL.md`: `sha256:b234e51e41c8d92b1ff79a0a11750bbcc34a01ebc123eaf2439715b1ac22915a`

# R7 四块平衡及保两桥补全：独立审计

2026-11-05。直接 caller `/root`；独立审计代理 `/root/r7_blocks_independent_audit`。
按工作区指定 GPT-6.1-sol/high 执行 ARIS proof-checker **本地适配**；实际后端身份未另行认证。
**PASS，相对于下列明确进口；same-family/provisional，sound-modulo-imports。**
作者与本审计上下文分离。未执行上游 LaTeX/PDF 流程或再开嵌套终审。

## 固定提交与进口

完整读取两份作者稿并逐分支核验。本次审计固定为：

| 稿件 | SHA256 |
|---|---|
| `R7_BALANCED_Q5_BLOCKS.md` | `857531f04a85c80f8582eb2249b41b3c2f6622a92b01cc9c1a1b464fd5834d55` |
| `R7_TWO_BRIDGE_MAXIMAL_REDUCTION.md` | `9a13a22b914d5c6d2956a870cccbe23af5e26b4d53b2a28ebfd5d85e5908c827` |
| `R7_BALANCED_Q5_BLOCKS_INPUTS.json` | `291c310217670ed649cea2e38b2a6fd1f66e902989248140aea10c56a5cc0110` |

数学进口：冻结 Q5_A10_FULL_CLOSURE.md 的全孔 consequences 及最终 Q5_A10_FULL_REVIEW.md/.json；其接受范围为任意 K(Q5) 匹配的所有平衡孔圈及正孔自由根任意异色目标路（目标可覆盖），新增边短。历史草稿措辞不缩小最终审计范围。
冻结 P6_FULL_CLOSURE.md/P6_FULL_REVIEW.json 的短匹配全端点定理；Fink C0 的任意完全图完美匹配延拓（这里只用维数6、7）；R7_THREE_FREE_PAIRINGS.md/REVIEW.json 的已审 F7；R7_ODD_BRIDGE_MARGIN_REVIEW.json 对同一个旧56边见证的列明规则外结论。
HK82 作为外部定理进口：Havel–Křivánek, *On maximal matchings in Q6 and a conjecture of R. Forcade*, CMUC 23(1),123–136 (1982)。本次直接打开[原始论文](https://dml.cz/bitstream/handle/10338.dmlcz/106137/CommentatMathUnivCarol_023-1982-1_10.pdf)，核其第125页 Theorem 2 以及第124页 maximal 定义，确为任意包含意义极大 Q6 匹配至少24边；不重证其分类论证。
作者清单24项散列逐项相符，直接已接受报告对 Q5/P6/F7 主稿和旧56边数据的四项绑定逐项相符；详见JSON。传递大证书与全部祖先报告未重放或逐一重核，本审计不提高其认证等级。

## 逐项义务

| ID | 对象 | 核验与回代 | 结论 |
|---|---|---|---|
| C01 | C6 domain | F is an arbitrary K(Q6) matching; cross-edge endpoint map phi is a genuine bijection, without a mirror or color assumption. | PASS |
| C02 | C6 even crossing count | 32=2m_U+q+h_U and balanced holes imply q even, including long or same-color prescribed edges. | PASS |
| C03 | C6 first local input | D pairs all and only X_U; F_U union D is a matching with exactly the original holes in U. Q5 all-hole cycle applies. | PASS |
| C04 | C6 actual paths | Deleting the nonempty disjoint marked D edges from a single cycle yields q/2 vertex-disjoint spanning paths with precisely X_U as endpoints and no cycle component. | PASS |
| C05 | C6 cross transport | Attach the unique original cross edge at every endpoint using phi. Interiors are in U and endpoints in X_V; all are pairwise disjoint. | PASS |
| C06 | C6 second local input | The actual endpoint pairing R is a matching on X_V, disjoint from F_V; F_V union R has exactly original holes in V. Q5 cycle applies again. | PASS |
| C07 | C6 expansion | Replacing marked R edges by disjoint actual paths preserves one cycle and inserts every U vertex exactly once. F_U,F_V and all original cross edges survive; only F edges may be long. | PASS |
| C08 | C6 zero-cross with holes | Rename a face with holes U. An incident non-F_V edge at x* exists since F_V is a matching; it is short. Mirror target y* is opposite to free x; Q5 path allows covered targets. | PASS |
| C09 | C6 zero-cross gluing and perfect case | Two disjoint spanning paths plus the two distinct mirror bridges form one spanning cycle. With no holes and q=0, F is perfect and C0 applies. Cases exhaust all q. | PASS |
| Q01 | R6 import discharge | For a short matching with a free root, P6 applies to a short neighbor target. The endpoint edge cannot lie in a 64-vertex simple path; adding it closes one cycle. Perfect input uses C0. | PASS |
| Q02 | Q outer parity | Four balanced Q5 hole blocks imply each Q6 face has balanced original holes. Internal short matching covers colors equally, so the outer ports have equal color counts and c is even. | PASS |
| Q03 | Q first C6 input | M_A union D has exactly H intersect A, because ports are covered by D and were not original holes. Its chosen two Q5 hole sets remain unchanged. | PASS |
| Q04 | Q actual outer pairing | After removing D every retained A edge is short; attaching original short cross edges creates disjoint actual short paths with distinct B endpoints. | PASS |
| Q05 | Q second C6 input | M_B union R has exactly H intersect B; its two Q5 hole sets remain balanced even if R is long or crosses the internal cut. C6 explicitly permits such R. | PASS |
| Q06 | Q final cycle and bridge count | Expansion produces a single 128-vertex short cycle containing all M. Only original C crosses the outer coordinate, hence exactly c outer bridges for c>0. | PASS |
| Q07 | Q zero-cross branches | With holes choose the face containing a free root, use R6 on the other face and P6 on the chosen face with a possibly covered opposite target; two bridges close. Without holes use d=7 C0. | PASS |
| T01 | T all-input implication | Odd weight 1,3,5 leaves at least two fixed coordinates; translation by t fixes all four blocks and flips color. It pairs their holes bijectively, independently of matching symmetry. | PASS |
| W01 | Single fixed input arithmetic | Independently reconstructed the 56 short disjoint edges, their 16 holes, direction counts, xor67 invariance, and fixed split (i,k)=(5,2). Four color counts are 2:2,2:2,1:1,3:3; c=20. | PASS |
| W02 | Strict new coverage scope | The directly bound prior N audit explicitly certifies this witness is outside its listed rules including M and N. This imported exclusion plus Q/T witnesses strict new coverage relative to those rules only. | PASS |
| R01 | Bridge-preserving completion | Greedy extension in each Q6 minus its two original bridge endpoints is finite, preserves M, keeps both endpoints free internally and produces an independent remaining hole set in that face. | PASS |
| R02 | At most two further edges | When extending L_S in full Q6, every newly added edge touches the two retained endpoints because H_S was independent. Free sets only shrink, and disjoint new edges use at most two endpoints. | PASS |
| R03 | HK82 input and bound | HK82 Theorem 2 states every inclusion-maximal Q6 matching has at least24 edges. Thus |L_S|>=24-2=22. Temporary endpoint-occupying edges are not put into L. | PASS |
| R04 | Dense and opposite-color branches | Opposite-color ports allow P6 in each face with two free opposite endpoints. Same-color ports and any face internal size>=28 meet exactly imported F7, without a density condition on the other face. | PASS |
| R05 | Residual counts | With both internal sizes22..27, |L|=|L_A|+|L_B|+2 is46..56, global holes16..36 and each face global holes62-2|L_S| is8..18. These are L holes, not numerical restrictions on the original M. | PASS |
| R06 | Rich direction and independent scope | At least44 internal edges across six directions imply some direction has at least8 in total. Only facewise hole independence follows; neither global maximality nor a stitching condition follows. | PASS |
| R07 | Back substitution and m2 | Any cycle containing L contains M. Original bridge count remains exactly2 and all other direction counts do not decrease. Under the stated all-seven-directions-at-least2 hypothesis m stays2. Residual universal extension remains unproved. | PASS |
| G01 | Dependencies and quantifiers | Q5+C0=>C6; P6+C0=>R6; C6+P6+R6+C0=>Q=>T. HK82=>completion bound; F7/P6=>closed branches. No R7/P7 reverse use; each choice is sequential after actual paths exist. | PASS |
| G02 | Bindings and assurance | All24 author-manifest bindings pass; four direct accepted source bindings pass. Full R7/P7, full m2, seven-direction lifting and historical4228 remain open; no solver, family enumeration or large-certificate replay occurred. | PASS |

## 独立固定算术与反例检查

独立内联 Python 从旧数据的 edges 重建，不执行作者生产脚本。56边覆盖112个不同顶点，均为短边；方向数(4,4,6,10,10,20,2)。四块孔分别为 {10,17,73,82}、{6,28,69,95}、{56,123}、{44,52,62,111,119,125}，全局色数为2:2、2:2、1:1、3:3。孔集在 xor67 下不变，固定外切向5恰20条原桥。只核一个已有输入，不搜索新输入。
反例尝试覆盖：C6长且不保色跨边（用真实phi运输，未用镜像）；q=2/q=32与零孔块（删非空匹配边仍为实际路径）；q=0仅一面有孔（可交换有孔面）；被覆盖目标（Q5/P6明确允许）；辅助边恰为几何短边（按标签删/展开）；内部切向不同及R跨内部切分（孔集不变、C6任意K匹配）；补全占用原桥端点（只使用L，T不保留）；跨面孔相邻（仅主张面内独立）；丰富方向集中在一面（只主张合计8边）。均未构成反例，不以未找到反例充当证明。
无渐近、概率模式或分析交换命题；定义和常数均在固定维数、同一原输入内使用。

## 已证及仍开

提交范围内28项义务均通过，无未决 FATAL/CRITICAL/MAJOR/MINOR 问题，作者无需修订。C6、Q、T 给出明确的全称充分子族，覆盖所有满足孔平移条件的短匹配；固定旧孔集的全部短匹配实现也包含在内。旧56边输入只证明相对列明旧规则有严格新增，不给出新增域的基数。
两桥补全稿证明保端点覆盖归约、22边下界和数值/方向约束；没有证明归约后的剩余类均可延拓。不是原M的大小限制，不能用该归约宣称完整两跨边或m2闭合。
完整两跨边、m2、R7、P7、七方向提升及历史4228均仍开。未改作者稿、冻结区、账本或RUN_STATE。主代理负责最终证明回代与研究决策。

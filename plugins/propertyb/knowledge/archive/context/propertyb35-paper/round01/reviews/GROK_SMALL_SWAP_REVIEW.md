# Grok：小点数交换定理的静态数学审阅

请求模型grok-4.7/xhigh；实际返回grok-4.7-build/xhigh，stopReason=end_turn。线程e15e0bbb-2d5c-4968-888a-0cece44788af。实际范围为SMALL_VERTEX_SWAP.md及必要的本轮局部计数材料；没有执行复算、Lean或其他模型审阅。结论限≤18点≤36边定理，不覆盖全局m(5)≥36。

+The theorem is correct. Every finite simple 5-uniform hypergraph on at most 18 vertices with at most 36 edges has Property B. On 18 vertices the same argument gives a coloring with both classes of size 9.

The check covers the repair lemma, the ordered-pair table, the complement factor, the source-g restriction, the strict gap, and the isolated-vertex pullback in `proofs/propertyb35/SMALL_VERTEX_SWAP.md`.

The repair count holds. If every state has at least one event and U states have exactly one, then \(S\ge U+2(N-U)\), so \(U\ge 2N-S\). Each of the \(d\) labeled repairs from such a state destroys its unique event \(e\), and the image still has an event \(g\). That \(g\) is a different edge and was bichromatic in the source. Distinct sources or labels stay distinct, so \(dU\le\sum_{e\neq g}K(e,g)\). Thus \(d(2N-S)>\sum K\) cannot occur, and some state has no event.

Here \(N=\binom{18}{9}=48620\) and \(d=45\). Each edge is monochromatic in \(2\binom{13}{4}=1430\) balanced colorings, so \(S=1430m\). All 9 opposite vertices lie outside a monochromatic 5-edge, so all 45 swaps exist and leave that edge with colors 4+1.

The table is exact. For a red \(e\) whose image makes \(g\) red, \(x\in e\setminus g\) and \(y\) is the unique blue vertex of \(g\), hence \(y\in g\setminus e\). The source copy of \(g\) is therefore bichromatic. The red set can be completed in \(\binom{8+t}{t}\) ways. The color-swap bijection doubles this to \(2(5-t)^2\binom{8+t}{t}\): 50, 288, 810, 1320, 990 for \(t=0,1,2,3,4\). For a blue image of \(g\), \(y\notin g\) and \(x\) is the unique red vertex of \(g\), so \(t=1\) and \(x=e\cap g\). The red-\(e\) count is \(5\binom{9}{4}=630\), and both colors give 1260. The two image colors are disjoint, so \(K_1=1548\) and \(K_t=(50,1548,810,1320,990)\). One swap recolors one vertex in each direction, so every repair that makes \(g\) monochromatic is in exactly one of these cases.

The factor 2 is \(R\mapsto V\setminus R\). It matches red-\(e\) states with blue-\(e\) states, preserves monochromaticity, and sends each legal labeled swap to a legal swap. No 9-subset equals its complement.

At \(m\le 36\) both sides are extreme at \(m=36\): \(45(97240-1430\cdot 36)=45\cdot 45760=2059200\) and \(1548\cdot 36\cdot 35=1950480\). The gap is 108720, so the lemma applies. At \(m=35\) the gap is \(2123550-1842120=281430\). For every smaller \(m\) the left side is larger and \(m(m-1)\) is smaller.

If \(n<18\), add isolated vertices until there are 18. The edge set is unchanged, so the 18-vertex coloring exists. Restricting it leaves both colors on every original edge.

The sum is over ordered pairs \(e\neq g\), so the multiplier is \(m(m-1)\). No intersection in \(\{0,1,2,3,4\}\) has coefficient above 1548.

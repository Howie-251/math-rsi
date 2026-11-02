# Independent paper attack: absolute radius-two overlap

**Inheritance correction, 2026-11-01:** the actual585-source support72, pair-intersection9, and stronger Steiner3-(65,9,1) certificate were already checked on2026-10-27. They are inherited results, not discoveries of this paper review. See the existing Wiki nodes `ddp-polarity585-port-steiner-local-premises-20261027` and `ddp-polarity585-all-preserved-edge-extensions-theorem-20261027`, with original `research/ddp/more_graphs_20261027/d9_D3_polarity_cover_prediction/{SOURCE.json,BLOCKS.json,PORT_R2.json,THEOREM.md}` and `research/ddp/polarity585_replication/source585.implicit_adj.txt`.

For the product whose B factor is this saved actual585 source, inherit the old third-order Bonferroni bound `U(a)=72a-9*binom(a,2)+binom(a,3)`. It gives `U(8)=380`, hence at least140 of520 nonabsolute targets missed and at least18 unowned based classes requiring external access, because each class owns8 such targets. This is an upper bound on the union, not a claim that every eight-subset attains380. It supersedes the weaker513 bound **for this actual certified source**. No old factor, block, pair, triple, or BFS computation was rerun.

The new use is the old585 evidence's application to product-cap31 row-routing obligations, together with the separately executed literalq2 support calibration. The general matrix derivation below remains a valid independent explanation and a fallback without the stronger source-specific triple certificate; it is not a first discovery of72/9 or a new graph/theorem count.

2026-11-01. **SUPPORTED under the genuine GQ/polarity interface. No gap found.** The matrix identity, exact support sizes, exact pair intersections, and stated union upper bound all hold. This review uses paper reasoning and local source-file I/O only. No factor, source graph, scalar enumeration, BFS, field, solver, Lean or paid-review computation was run. In particular it does not duplicate the root's separate literal15-factor experiment or the earlier230 calibration.

The hypotheses are an actual finite GQ(q,q), its actual involutory point-line polarity rho, and its symmetric 0/1 relation matrix

`M[x,y]=1 iff point x is incident with line rho(y)`.

An absolute point contributes one diagonal entry to M. Matrix row size is q+1, with a loop counted **once** as a relation entry. No claim of a polarity at arbitrary q is made. The conclusions apply to the genuine q2/q8 factors used in the prediction.

## 1. Exact incidence-walk/quotient-walk bijection

A matrix-counted three-walk `x-u-v-y` corresponds to the incidence walk

`point x - line rho(u) - point v - line rho(y)`.

The middle step is valid because `u in rho(v)` is equivalent, by polarity reciprocity, to `v in rho(u)`. Conversely an incidence walk `x-L-v-rho(y)` gives the unique `u=rho(L)` and recovers the quotient walk. This is a bijection, not a many-to-one projection. Consecutive equal quotient vertices are allowed: their quotient loop represents a genuine incidence edge between different point/line types. Loops and backtracking are retained throughout the matrix count.

For point x and incident line L, every three-step incidence walk `x-L'-v-L` has `L'=L` or `v=x`. Otherwise two distinct points x,v lie on two distinct lines L,L', an incidence4-cycle. There are q+1 choices in each of these two cases and exactly one common walk, `x-L-x-L`. The total is therefore `2(q+1)-1=2q+1`.

For x nonincident with L, the GQ point-to-line projection axiom gives exactly one such three-step walk. Its connecting point and line are uniquely determined. Backtracking or loop padding cannot create extra incidence walks in this nonincident case. Hence, entry by entry,

`M^3 = 2q M + J`.

Multiplication by M, using every row size q+1, yields

`M^4 = 2q M^2 + (q+1)J`.

The identity is for the looped relation. Removing loops before this count would invalidate the uniform row and padding arguments; no such removal is made here.

## 2. Two-step entries and the absolute support

For x distinct from y, `M^2[x,y]` counts common incident lines of the two points, via the same polarity bijection. Two points have at most one common line, since otherwise there is an incidence4-cycle. Therefore every off-diagonal entry of M^2 is 0 or1. Symmetry and the 0/1 row give `M^2[x,x]=q+1`.

Distinct absolutes b,c are not adjacent: adjacency would put both points on both distinct lines rho(b),rho(c), creating a4-cycle. They cannot have a common quotient neighbor u either. If u is one of b,c, this already requires the forbidden edge; otherwise the three distinct points and polar lines give the incidence6-cycle

`b-rho(u)-c-rho(c)-u-rho(b)-b`.

Thus `M[b,c]=M^2[b,c]=0` for different absolutes, including with loops retained.

For an absolute b, every immediate nonabsolute neighbor is also reached in exactly two relation steps by padding with b's loop. Thus the set T_b of nonabsolute targets reachable in at most two steps is exactly the nonabsolute support of the b row of M^2. Each supported entry is1, since it is off diagonal. The only absolute contribution in that row is its own diagonal q+1. The row sum of M^2 is `(q+1)^2`, giving

`|T_b| = (q+1)^2-(q+1) = q(q+1)`.

For different absolutes b,c, the matrix identity gives `M^4[b,c]=q+1`. On the other hand,

`M^4[b,c] = sum_x M^2[b,x] M^2[x,c]`.

All absolute x terms vanish: the two absolute rows have disjoint diagonal positions and zero off-diagonal absolute entries. The nonabsolute terms are precisely the 0/1 indicators of membership in both T_b and T_c. Consequently

`|T_b intersect T_c| = q+1`.

There is no hidden multiplicity from the diagonal entries q+1 in this intersection calculation.

The supplied absolute count q^2+1 is consistent with this same genuine interface. For completeness, the quotient has no triangle on three distinct vertices, since it would lift to an incidence6-cycle. At a nonabsolute x, the diagonal identity `M^3[x,x]=1` therefore counts exactly its absolute neighbors (the only remaining closed three-walk is `x-b-b-x`). Every nonabsolute has one absolute neighbor. Each absolute has q nonabsolute neighbors and its own loop, so `|V|=(q+1)|O|`, giving `|O|=q^2+1`. Equivalently their q+1-entry neighborhoods partition the factor. The number of nonabsolute targets is `q(q^2+1)`.

## 3. The union inequality has the correct direction

Take t distinct absolutes and let m_x be the number of their supports containing a nonabsolute x. On the union, `1<=m_x<=t`, and

`binom(m_x,2) <= t(m_x-1)/2`.

Sum this inequality over the union. If N is its cardinality, the first and second incidence counts are

`sum m_x = t q(q+1)`,

`sum binom(m_x,2) = binom(t,2)(q+1)`.

Thus

`binom(t,2)(q+1) <= t/2 * (t q(q+1)-N)`.

Since t>0, rearranging gives the claimed **upper** bound

`N <= (q+1)((q-1)t+1)`.

The proof does not reverse a Cauchy/second-moment lower bound. This particular inequality is valid for any positive t; the restriction t<=q ensures that it forces a missed target. At t=q the complement has size at least q-1. It is not asserted that the upper bound is attained for q8.

For q8,t8, each support has72 elements, pair intersections have9, and the union has at most513 of520 nonabsolute targets. At least7 targets are missed. For q2,t2 the exact two-set union is `6+6-3=9` of10, so exactly one is missed. These are symbolic substitutions, not executed scalar tests.

For the saved actual585 factor, the inherited Steiner certificate is stronger: each point lies in72 blocks, each pair in9, each triple in1. Applying the already saved odd Bonferroni truncation to eight own classes gives `8*72-28*9+56=380`. Thus the actual-source application must use missed>=140 and external classes>=18, rather than stop at the general pair-only missed>=7 result. This does not claim the Steiner premise for every hypothetical GQ8 polarity quotient.

## 4. What the missed targets require in the fixed helper model

Every nonabsolute B target x has a unique absolute neighbor b, as established above. If x is missed by a selected union, b cannot be one of its selected absolutes: x would already be an immediate member of T_b. Thus the missed targets include at least one target belonging to an **unowned** based class.

For a helper owning exactly eight distinct based classes in a fixed absolute-A row a, its own pins in that row have mandatory suffix coverage contained in these eight B supports. Pins in a different absolute-A row cannot supply a mandatory suffix of length at most2 to `(a,x)`, because distinct A absolutes have no one- or two-step walk. Repeated copies of an owned based class do not enlarge its mandatory support.

In the previously stated mandatory-edge-preserving saturated product family, the uncovered target must therefore use an external route: a helper-neighbor's pin of its unique based class, or an F-peer of one of the helper's pins. These are exactly the already classified `h-g-f-x` and `h-f-f'-x` routes. The matrix support statement alone is not a theorem about arbitrary rewired source graphs.

Seven missed **vertices** need not mean seven missed **classes**; one class can own multiple such targets. The conclusion is at least one required external unowned based class for that eight-class row. It does not say that every helper has such a row, that every helper needs nine owned pins, that nine own classes suffice, or that cap31 is impossible. It also does not show that the required external routes can be implemented simultaneously.

The source-specific inherited improvement counts classes more sharply:140 missed vertices, at most8 per unique absolute owner class, require at least18 distinct unowned classes in the accessible external-class set for such a row. This remains a conditional route obligation, not a cap31 exclusion, not a claim that every helper has an eight-class row, and not a simultaneous construction of those external routes.

## Disposition

The prediction is supported. A future concrete cap31 generator must account for support overlap and explicit residual classes as well as the earlier necessary heavy-row condition. Reaching eight owned classes does not finish a row; an external helper/F-peer route is still necessary there. No controller, subset search or source generation is authorized or started by this paper check.

The current three-graph final C did not certify this new overlap analysis. No Wiki, root-state, frozen package, portfolio count or Lean count was changed by the review.

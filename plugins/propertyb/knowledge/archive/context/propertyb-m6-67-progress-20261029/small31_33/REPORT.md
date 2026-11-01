# M66: complete 31/32/33-point branches

The original target remains all finite simple six-uniform hypergraphs with at most 66 edges. The imported minimal-counterexample reduction gives pair-cover, exactly 66 edges, total degree 396 and minimum degree at least ceil((v−1)/5). This report establishes the complete v31, v32 and v33 branches. It does not claim the global target.

The probability engine is imported from `propertyB_small_k/propertyB_m6_certificate.py`, with its module constant explicitly reset to M=66. This is exact local finite verification, not an independent probability implementation. `certificate.py` generates every actual local type used below, together with its successful layout and exact upper bound. `CERTIFICATE.json` records the result. Root must independently verify this candidate and integrate it with the complete object domain.

## Lemma 1: a stronger link bad-pair quota

Let F be a family of f distinct five-element sets on at most N points. Let G have these sets as vertices, adjacency meaning nonempty intersection, and q edges. Different connected components of G have disjoint supports.

For one component with t vertices and e edges, where t−1≤e≤C(t,2), define

$$a(t,e)=\max\left(\left\lceil\frac{t^2}{t+2e}\right\rceil,\left\lceil\frac{2t-e-1}{2}\right\rceil\right).$$

Its independence number is at least a(t,e). The first term follows from the random-order independent-set expectation and Cauchy–Schwarz. For the second, fix a spanning tree. There are r=e−t+1 edges outside it. Delete at most one endpoint for each such edge, a total of at most r vertices. The remaining induced graph is a forest on at least t−r vertices, whose larger bipartition class is an independent set of size at least ceil((t−r)/2)=ceil((2t−e−1)/2). If this expression is nonpositive it is harmless.

Disjoint five-sets from an independent set imply component support at least 5a(t,e). A component with t≥2 also has support at least six, because its five-sets are distinct. A further valid strengthening is support at least eleven if

$$e<\binom t2-\left\lfloor\frac t2\right\rfloor.$$

Indeed, if the component support had at most ten points, any five-set would have at most one distinct disjoint partner: on fewer than ten points there is none, and on exactly ten points the only possible partner is its complement. Thus the nonedge graph would have maximum degree at most one and at most floor(t/2) edges, contradicting the displayed condition.

Write u(1,0)=5. For t≥2 let u(t,e) be the maximum of 6, 5a(t,e), and eleven when the last condition holds. Define recursively

$$S(0,q)=0,\qquad S(f,q)=\min_{\substack{1\le t\le f\\t-1\le e\le\min\{q,\binom t2\}}}\{u(t,e)+S(f-t,q-e)\}.$$

Then the union of F has at least S(f,q) points. To prove this, select an actual component (t,e), apply its valid support bound, and apply induction to the remaining actual components, whose supports are disjoint. The recurrence permits component parameters without a realizing graph; this only lowers S, hence preserves its necessary-bound direction. It also permits unused budget q, as needed for an at-most-q assertion.

Consequently define

$$q_*(f,N)=\min\{q\ge0:S(f,q)\le N\}.$$

Then F has at least q_*(f,N) intersecting pairs. The implementation starts from the older valid ceiling bound ceil((5f−N)/4), truncated at zero; since that lower bound is valid, this does not skip a possible actual q. Its finite search terminates whenever a family F exists, and all parameter inputs used here admit an accepted relaxed component partition.

Applied to the actual link at a lock vertex, F consists of the original edges containing that vertex with the vertex removed. These five-sets are distinct because the original hypergraph is simple. Their support is at most v−1. Therefore q_*(d,v−1) can replace the old quota in the existing nonnegative capacity/weight deletion argument. For an avoided-lock subfamily the same conclusion uses f equal to its actual number of edges and N=v−1−|R|. The script `diagnose.py` exports `support_min(f,q)` and `quota(N+1,f)` for this purpose.

All three strengthening components above are used by the current candidate. In particular, the final two-point delta11 cases use the feedback-vertex bound and the unique-complement bound. The full table for f=0,…,24 and support N=28,…,32 is in `CERTIFICATE.json`. No claim of novelty is made for these elementary graph bounds.

## Lemma 2: complete v31 selection

The minimum degree d lies in 6,…,12. For d≤11 choose a vertex of degree d and one lock; the six exact bounds are strict.

If d=12, at least seven vertices have degree exactly twelve: otherwise at least 25 vertices would have degree at least thirteen, forcing total degree at least 31·12+25=397>396. Fix a twelve-degree vertex x among them. Pair-cover gives

$$\sum_{y\ne x}(\lambda_{xy}-1)=5\cdot12-30=30.$$

If its six other twelve-degree partners all had codegree at least seven, the sum would be at least 36. Thus some second twelve-degree vertex y has 1≤λxy≤6. The complete trace multiplicities are

$$\ell_{xy}=\lambda,\quad\ell_x=\ell_y=12-\lambda,\quad\ell_0=42+\lambda.$$

All six actual types have strict recorded bounds. Wider layouts are essential for λ=3 and λ=4; checking only central adjacent locks had missed these cases. This closes all v31 inputs.

## Lemma 3: complete v32, minimum degree at most eleven

For a minimum-degree vertex x of degree d, there are at least

$$n=2(v-1)-5d$$

unit-codegree neighbors. This follows because the sum of λxy−1 is 5d−(v−1), and each nonunit neighbor contributes at least one. Here n>0 for d=7,…,11. If all unit neighbors had degree greater than

$$t=d+\left\lfloor\frac{396-vd}{n}\right\rfloor,$$

the total degree would exceed vd+n(t+1−d)>396. Choose a unit neighbor y with degree e in d,…,t. `certificate.py` enumerates this entire necessary interval separately for each d, uses the unique two-lock trace, and obtains strict bounds for every such type. This closes v32,d≤11.

## Lemma 4: complete v32, minimum degree twelve

Let R be the twelve-degree vertices. The total excess above twelve is twelve, so |R|≥20. All vertices outside R have degree at most 24. Each r∈R has at least two unit neighbors because its pair-excess is 29 among 31 partners.

If there is a unit pair inside R, its two-lock type (12,12,1) is strict. If there is a unit pair from R to a vertex of degree e∈{14,…,24}, the complete eleven-type two-lock certificate is strict. Hence assume every unit neighbor of every r∈R has degree thirteen. Let B be the set of these neighbors. Since each costs at least one of the twelve excess units, |B|≤12. The unit pairs between R and B form a bipartite graph with every r nonisolated.

Write u_r for r's degree in this bipartite graph and t_b for b's degree. Suppose there is no b-centered wedge r–b–r′ whose endpoint codegree is at most two. Then every such r′ has λrr′≥3. For every edge rb, all t_b−1 other R-neighbors of b are among these partners. Relative to baseline codegree two on all 31 partners of r, exactly u_r unit partners decrease its row sum by one each; the t_b−1 identified partners increase it by at least one each. Thus

$$60=\sum_{z\ne r}\lambda_{rz}\ge62-u_r+t_b-1,$$

so t_b≤u_r−1 and therefore 1/t_b>1/u_r. Summing over all bipartite edges gives

$$|B|=\sum_{rb}\frac1{t_b}>\sum_{rb}\frac1{u_r}=|R|,$$

contradicting |B|≤12<20≤|R|. Hence there is an actual wedge with center degree13, endpoints degree12, both center–endpoint codegrees one and endpoint codegree l∈{1,2}.

The triple intersection τ is zero or one. These four complete actual trace types are

$$\ell_{123}=\tau,\quad\ell_{12}=\ell_{13}=1-\tau,\quad\ell_{23}=l-\tau,$$

$$\ell_1=11+\tau,\quad\ell_2=\ell_3=11-l+\tau,\quad\ell_0=66-\sum_{T\ne\varnothing}\ell_T,$$

where vertex1 is the degree13 center. All four certificate bounds are strict. This closes v32,d12.

## Lemma 5: complete v33 selection

The same actual minimum/unit-partner selection covers d=7,…,12. With the stronger link quota every two-lock type is strict except e14 at d9,d10,d11. In particular d12 is handled directly, and the earlier max-unit-degree wedge idea is unnecessary.

Here take y to be a minimum-degree unit neighbor of the minimum-degree x. If e=d(y)≠14, the corresponding passing type applies. In the exceptional three cases e=14, all unit neighbors of x have degree at least fourteen.

If d=9, x has at least 19 unit neighbors. The total excess above nine is 99. Nineteen vertices of degree at least fourteen cost at least 95 of those excess units; twenty would cost 100, so x has exactly nineteen unit neighbors. Its other thirteen partners are nonunit. Since

$$\sum_{z\ne x}(\lambda_{xz}-1)=45-32=13,$$

every one of those thirteen partners has codegree exactly two with x. The nineteen unit neighbors leave only four excess degree units among the other fourteen vertices (including x), so at least ten vertices have degree nine. Thus another degree9 vertex y exists, is a nonunit partner, and has λxy=2. Its two-lock type has exact upper bound

$$101147/103385<1$$

at positions (16,18). This closes d9 entirely, including the previous failed three-lock λ=3 profiles.

If d=10 or d=11, let n=64−5d, respectively 14 or 9. The total excess above d is 396−33d, and n unit neighbors cost at least n(14−d). The respective remaining slacks are ten or six. Among at least n unit neighbors, therefore at least n−slack have degree exactly fourteen: respectively four or three. This count is still valid if there are more than n unit neighbors: each additional one costs at least 14−d≥3 extra units and cannot reduce the lower bound. More directly, if u≥n actual unit neighbors and h of them have degree above fourteen, then

$$u(14-d)+h\le396-33d,$$

so the number u−h of degree14 unit neighbors is at least (15−d)u−(396−33d)≥(15−d)n−(396−33d)=n−slack.

Choose two degree14 unit neighbors. Their mutual codegree l ranges from one to fourteen. Their triple intersection τ with x is zero or one; nonnegative single traces require 13−l+τ≥0. The actual trace multiplicities are

$$\ell_{123}=\tau,\quad\ell_{12}=\ell_{13}=1-\tau,\quad\ell_{23}=l-\tau,$$

$$\ell_1=d-2+\tau,\quad\ell_2=\ell_3=13-l+\tau,\quad\ell_0=66-\sum_{T\ne\varnothing}\ell_T.$$

For each d=10,11 the complete 27 actual (l,τ) types have strict bounds in the certificate. This closes v33.

## Exact verification and status

`certificate.py` enumerates every necessary type in these selection branches, without enumeration of original hypergraphs. It records all multiplicities, positions and exact rational upper bounds in `CERTIFICATE.json`. Every final certificate row is strict. `DIAGNOSTIC.json`, `FOUR.json` and the exploratory files preserve failed older menus; those failed menus are not assumptions or components of the final proof.

The arithmetic imports the existing conditional random-greedy probability formulas and replaces only the justified link quota. It is not an independent reimplementation. No Lean, external model review or global m(6)≥67 conclusion is claimed by this local delivery.

# Twenty-one vertices with at least three degree-seven points

2026-10-13. Complete paper candidate, not yet Lean. H is simple, pair-covering and five-uniform, has 21 vertices and 34 edges, and has minimum degree seven. Write r for the number of seven-degree points. This note proves the branch r≥3 using actual selections and finite local trace classifications. Cases r=1,2 and minimum degree eight remain open in this note.

Every degree-seven point has codegree excess eight, since $4\cdot7-(21-1)=8$. If L is the degree-eight set, the total degree 170 gives

$$|L|\geq19-2r,$$

because the baseline with r sevens and the other 21−r vertices at least eight is 168−r; at most r+2 of those other vertices can have degree at least nine.

## 1. Initial low-degree codegrees

A pair with a degree-seven endpoint and codegree at least five has a strict double witness. For three seven-degree points the remaining complete (7,7,7) triple domain has 154 profiles. Its 137 strict cases exclude every pair codegree three or four; the seventeen residues have all pair codegrees one or two. Thus when r≥3 every pair of sevens has codegree in {1,2}.

Similarly, the (7,7,8) domain has 157 profiles with 140 strict; its seventeen residues again have only pair codegrees one or two. Whenever at least two sevens and a degree-eight point are available, each seven-to-eight codegree may be assumed in {1,2}.

A separate eleven-profile (7,8,8) table shows that two eight-degree points unit to the same seven-degree point have codegree at most two unless a strict witness already supplies a coloring. These facts are used below before any extra structural assumption is made.

## 2. Four seven-degree points

The complete four-lock domain with all six pair codegrees in {1,2} contains 674 profiles. Of these, 567 have strict single-layout witnesses, another 71 have strict shared-bad-vector mixed-layout certificates, and 36 labelled residues remain, in nine permutation orbits.

For the unit-codegree graph on these four points, every residue has one of four induced graphs:

$$K_4,\quad K_{1,3},\quad C_4,\quad\overline{K_4}.$$

The saved residues retain exact triple and quadruple counts as well as their graph. Graph shape alone is not substituted for these trace conditions.

### r≥5

Apply the four-point conclusion to every four-element set of sevens. A graph all of whose induced four-vertex graphs belong to the displayed list is either complete or complete bipartite, allowing one empty bipartition class.

To prove this, if the graph contains a triangle, any fourth vertex must complete a K4. Every other vertex is adjacent to the triangle; then the same condition on two triangle vertices and any two outside vertices forces the outside pair adjacent. The graph is complete. If it is triangle-free and has an edge a-b, every other point is adjacent to exactly one of a,b: two adjacencies form a triangle; zero adjacencies is incompatible with either a claw or a C4 on a,b,this point and a fourth point. This partitions the graph into two classes. Inside-class edges would form triangles. A missing cross edge would create a forbidden induced path on four vertices, so every cross edge is present. The edge-free case is the bipartite graph with an empty class.

Select any five sevens. Their unit graph is therefore K5 or one of $K_{0,5},K_{1,4},K_{2,3}$. The exact five-lock domain for these four graph families contains 1,143 raw profiles. Requiring all five four-point projections to be among the 36 retained residues leaves 55 profiles. All 55 have strict single-layout witnesses; the largest bound is $2143/2145<1$. This proves r≥5.

### r=4

There are at least eleven eight-degree points. Choose any such point w. Its four codegrees to the sevens are one or two by Section 1. Normalize the four-seven profile to one of the nine residual representatives, then add w.

For each existing exact trace t, split its multiplicity n_t into traces t and t∪{w}. The split counts are nonnegative, at most n_t, sum to d(w)=8, and induce each specified seven-to-w codegree in {1,2}. This enumerates every actual extension once in that chosen labelling; it does not assume extra incidence restrictions. The nine representative domains have 315,134,32,339,332,206,89,209,344 extensions respectively, totaling 2,000. There are 1,993 strict single-layout witnesses and seven strict mixed-layout certificates. Hence r=4 is proved.

## 3. Exactly three seven-degree points

Let the sevens be x,y,z. Then |L|≥13. Section 1 gives all codegrees among the sevens and between a seven and a point of L in {1,2}. For u∈L, record its pattern

$$b(u)=(\lambda(x,u),\lambda(y,u),\lambda(z,u))\in\{1,2\}^3.$$

Let p(u) be the number of entries equal to two. The sum of p(u) over L is at most the three sevens' total codegree excess, hence at most 24. Therefore

$$\sum_{u\in L}(3-p(u))\geq3|L|-24\geq15.$$

If none of the seven patterns other than (2,2,2) occurred twice, that sum would be at most $3+3\cdot2+3\cdot1=12$. Thus distinct u,v∈L share a pattern other than (2,2,2). At least one of x,y,z is a common unit neighbor of u,v, so λ(u,v) is one or two by Section 1.

Use locks (x,y,z,u,v), with degrees (7,7,7,8,8). The three seven-pair codegrees are arbitrary in {1,2}; u,v share one of the seven non-(2,2,2) patterns; and λ(u,v)∈{1,2}. There are 13,944 labelled local profiles, or 1,722 representatives under permutations of the three equal-degree seven locks and the two equal-degree eight locks. Of these representatives, 1,707 are strict single-layout cases and twelve more have strict mixed-layout certificates. Only three residual representatives remain.

Every residual forces all three seven-pair codegrees to be two and the shared pattern b(u)=b(v)=(1,1,1). It also forces λ(u,v)=2. The exact higher traces are retained in the three residual representatives, not discarded.

If another non-(2,2,2), non-(1,1,1) pattern occurred twice, the same five-lock argument would be strict. Thus each of those six other patterns occurs at most once. Meanwhile the three internal double codegrees consume six of the sevens' total excess, so now $\sum_{u\in L}p(u)\leq18$. Consequently

$$\sum_{u\in L}(3-p(u))\geq3\cdot13-18=21.$$

The six nonconstant patterns contribute at most nine, the (2,2,2) pattern contributes zero, and each (1,1,1) point contributes three. Therefore at least four points of L have pattern (1,1,1). Call this set S. Every pair of S, together with x,y,z, must be one of the three retained five-lock residues; in particular all S-pair codegrees are two.

Select any three points u,v,w∈S. Begin with the residual profile on x,y,z,u,v and add w by the exact trace-splitting procedure, now requiring its codegrees to x,y,z to be one and to u,v to be two. Require each of the three five-point projections using a pair of u,v,w to lie among the retained residuals. Exactly 67 labelled extensions survive. Sixty-six have strict single-layout witnesses and one has a strict mixed-layout certificate,

$$5550369862/5561110555<1.$$

This supplies a coloring and proves r=3.

## 4. Verification and remaining interfaces

The actual-input selections above are mathematical arguments. The local generators enumerate nonnegative higher trace multiplicities within fixed pair capacities, derive exact pairs/singletons/empty trace, and retain projection constraints. They do not enumerate complete hypergraphs. Equal-degree permutations preserve the existence of a strict layout, so canonical representatives can be used after transporting their lock labels.

For r≥5, `MANY_SEVENS_WITNESSES_VERIFIED.json` records 762 independently replayed single-layout witnesses, while `MANY_SEVENS_JOINT_VERIFIED.json` records 71 exact mixed-layout checks. These include the earlier triple and double inputs. The four-point residue list is `FOUR_SEVENS_RESIDUES.json`; the five-point classification and witnesses are `FIVE_SEVENS.json`.

For r=4 and r=3, `THREE_FOUR_SEVENS_WITNESSES.json` gathers the strict single-layout data; independent checks use `verify_exact.py`. Mixed-layout checks use `verify_joint.py` on `FOUR_SEVEN_EXTEND_JOINT.json`, `THREE_SEVEN_TWO_EIGHT_STRICT_JOINT.json` and `THREE_SEVEN_THREE_EIGHT_JOINT.json`. Their saved `_VERIFIED.json` files are the completion evidence, rather than the LP solver's success status. All exact probabilities are recomputed using independent labelled injections; all quotas, weights, layout masses and capacity repairs are checked rationally.

As elsewhere, fixed H has one common actual bad-count vector across layouts. A weighted average of layout-specific upper bounds below one implies that at least one layout has its own failure probability below one. It does not assert that different conditional layouts have the same failure probability.

The finite-table completeness/actual-profile connection and the probability/quota interfaces remain to be formalized in Lean. The two genuinely remaining minimum-degree-seven branches are r=1 and r=2.

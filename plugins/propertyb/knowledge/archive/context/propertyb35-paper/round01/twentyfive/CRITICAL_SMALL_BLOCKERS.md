# Critical low-edge repair: exact singleton/pair obstructions

The new structural results are an exact description of failure with one or two positive four-sets, and a genuine repair lemma when there is only one initially red exterior point on24 vertices. It preserves the association between the center, blue vertices and original negative edges. A bounded count diagnostic confirms that aggregate color-type moments alone still do not close the branch. The 23/24-point minimum-degree-seven branches remain open.

## 1. Actual input and scope

Use the critical normalization and actual edge selection proved in `LOW_EDGE_REPAIR_INTERFACE.md`: first choose an original counterexample with minimum vertex number and then minimum edge number, without padding it. It is pair-covering and edge-critical, with M=34 or35. In the four branches below, choose the actual edge G after normalization:

| n | M | d(G) upper bound | Guaranteed seven-degree points k in G |
|---:|---:|---:|---:|
|24|34|35|5|
|24|35|36|4|
|23|34|37|3|
|23|35|38|2|

Color H−G properly; noncolorability makes G all red after complementing colors. G is the only monochromatic edge. Let L be the blue exterior, with b points, and let a=n−5−b count red exterior points. A zero-G proper edge exists because d(G)≤M+3, so a,b≥1.

For a seven-degree g∈G, flip g blue. The positive family consists of the four-sets A=e−{g} where e∩G={g} and A⊆L. There are m_g≤5. Negative sets are B_f=f∩L for **every** edge f avoiding g, including zero-G edges. They are nonempty and have sizes1,…,4. Indices of original edges are retained. A set R⊆L repairs H if and only if it hits all positive sets and contains no negative set. The previous interface proves this equivalence; it is not an independent random coloring assumption.

Define the forbidden-point set

F_g={x∈L: some edge f avoiding g has B_f={x}},

and the graph Q_g on L−F_g whose edges are the distinct pairs B_f of size2 for edges f avoiding g. Any feasible repair avoids F_g. Larger negative sets cannot obstruct a repair with at most two vertices.

## 2. Exact small-blocker lemma

**One positive set.** If m_g=1 with positive four-set A, repair fails exactly when A⊆F_g.

Indeed, any x∈A−F_g is a valid one-point repair: it hits A and contains no nonempty negative set except possibly a singleton, which the definition of F_g excludes. Conversely every repair must hit A, so A⊆F_g prevents it. In particular, failure requires four different singleton-negative blue vertices and at least four different original singleton-negative edges avoiding g.

**Two positive sets.** Suppose m_g=2, with A_1,A_2, and put U=A_1−F_g, V=A_2−F_g. There are exactly three possibilities.

1. If U or V is empty, singleton constraints alone block every repair.
2. If U∩V is nonempty, any point of this intersection is a valid repair.
3. If U,V are nonempty and disjoint, repair fails **if and only if** every pair {x,y}, x∈U,y∈V, is an edge of Q_g.

For the third case, a missing pair is itself a valid repair. Conversely every repair contains some x∈U and y∈V; if every such pair is a negative set, no repair is possible. Equivalently, every feasible repair contains an inclusion-minimal hitting subset of size at most2, and the preceding list exhausts those subsets.

Consequently, in the third case there are at least |U||V| different original negative-pair edges avoiding g. When |F_g|≤3 this is at least (4−|F_g|)^2. The emptiness case in item1 must be checked first; the crosspair conclusion does not apply to it.

This is an actual incidence requirement. One chosen original edge for each required pair {x,y} has blue part exactly {x,y}, has three initially red points, and avoids g. Different pairs require different original edges. For each x∈U, at least |V| of these original edges pass through x; similarly for y∈V. If a second center is considered, its negative family must be obtained from these same original edges rather than assigning an independent pair graph.

`CRITICAL_SMALL_BLOCKERS_INTEGER_REPLAY.py` directly enumerates all496 canonical two-four-set/singleton-deletion patterns. It computes the inclusion-minimal free transversals of size at most2 and checks the description above, without importing the construction or optimization code. The mathematical proof is the preceding paragraph.

## 3. A consequence shared by the five centers

Let c count the original nongroup edges with G-trace a singleton and four blue exterior points, and let N_1 count all original edges whose blue part has size1. The five positive families partition these c edges by their unique G vertex.

In a non-B initial state every G vertex has at least one positive edge: otherwise flipping that vertex alone colors H. Suppose k of the G vertices have degree7. If every such vertex has at least two positive edges, then

c≥2k+(5−k)=k+5.

Otherwise one seven-degree vertex has exactly one positive set; the preceding lemma gives N_1≥4. Thus the following necessary disjunction is proved:

**c≥k+5, or N_1≥4.**

More precisely, if ℓ seven-degree centers have exactly one positive edge, their four required forbidden incidences give

Σ_(f:|f∩L|=1) (5−|f∩G|) ≥4ℓ,

because a singleton-negative edge f can supply at most one forbidden vertex for each center outside f, and supplies none for a center inside f. Also ℓ≥max(0,k+5−c). This inequality retains a center-counting consequence, but the exact lemma retains more information through F_g and Q_g.

The remaining difficulty is not the proof of this disjunction. Neither the low G degree sum nor pair coverage has yet been shown to force a center with m_g≤2 and small F_g, or to make its required complete bipartite negative-pair graph impossible. A complete bipartite graph here represents actual original edges with three red vertices each; its compatibility across centers and with a chosen extremal initial coloring is still missing.

## 3a. A true repair lemma for one red exterior point on24 vertices

Assume n=24, δ≥7, d(G)≤36 and a=1. Write r_0 for the unique initially red exterior point. For **any** center g∈G, with d(g)≥7 supplied by the minimum-degree hypothesis, if m_g≤2 then a one-direction repair exists. The conclusion does not require this center to have degree7; that degree restriction is only needed for the earlier bound m_g≤5.

The underlying row-budget statement has a useful parameterized form. Let H be a finite k-uniform pair-covering hypergraph on n points, k≥2, with an edge G and a coloring whose unique bad edge is red G and whose unique red point outside G is r_0. Fix any g∈G, of any degree, and set B_f=f∩L for every edge f avoiding g. Properness of H−G gives1≤|B_f|≤k−1. Then

**Σ_(f:g∉f) (k−|B_f|−1)² ≤ (k−1)(d(G)−d(g)−n+2).**

Indeed put S=G−{g}. The total repeated-pair row budget of S is

R=Σ_(h∈S)Σ_(v≠h)(λ(h,v)−1)
=(k−1)(d(G)−d(g)−(n−1)).

For an edge f avoiding g let t=|B_f|, ε=1_(r_0∈f), and h=|f∩S|=k−t−ε. Such an edge contributes h(h−1) to ordered pairs inside S and hε to pairs between S and r_0. G itself already supplies one occurrence of every internal S pair. The total of these contributions over edges avoiding g is therefore at most R+(k−1): internal pairs use only their surplus over G, while the S-to-r_0 pairs additionally use their k−1 baseline occurrences. For ε=1 the individual contribution is(k−t−1)²; for ε=0 it is(k−t)(k−t−1), at least that square. Summing proves the displayed inequality. All pair-surplus terms discarded in this argument are nonnegative by pair coverage.

For k=5,n=24,d(G)≤36,d(g)≥7, its right-hand side is at most

4(d(G)−d(g)−24+2)≤4d(G)−116≤28.

Thus the squared costs of negative singleton, pair and triple edges are9,4,1. Writing n_t(g) for their indexed counts gives the actual common-star inequality

**9 n_1(g)+4 n_2(g)+n_3(g)≤28.**

Discarding the n_3 term recovers9n_1+4n_2≤28.

If d(G)=35 the stronger upper bound is24. In particular n_1(g)≤3. The integer q below is the **indexed edge count** n_1(g), not the distinct forbidden-point count: |F_g|≤q, which is sufficient for |A_i−F_g|≥4−q. With one positive set, singleton blocking would require n_1(g)≥4, impossible. With two positive sets neither remaining set can be empty. If they intersect, there is a one-point repair. Otherwise, failure requires at least(4−n_1(g))² distinct pair-negative edges. For q=n_1(g)=0,1,2,3, this would force

9q+4 n_2(g)≥9q+4(4−q)²=64,45,34,31,

respectively. Each exceeds28. This proves the repair lemma. The case m_g=0 is immediate. More generally, in the five-uniform one-red-exterior interface a row-budget upper bound at most30 already implies repair for m_g≤2: q≥4 costs at least36, while q=0,…,3 costs at least31. The degree-bound formula supplies the appropriate actual upper bound.

Thus in a putative non-B24-point branch with a=1 and d(G)≤36, **every one of the five centers must have at least three positive edges**, so c≥15. This is a necessary condition, not a contradiction: no argument here forces a center with m_g≤2. The key gain is the simultaneous singleton/pair bound using the original G-trace and the same repeated-pair rows. Separate unconstrained negative graphs would miss it.

There is also a small extension for m_g=3. At a seven-degree center, the case n_1(g)=3 is repairable. The common-row bound gives n_2(g)=0 and n_3(g)≤1. Delete F_g; all three remaining positive sets are nonempty. If any two intersect, a point in their intersection together with a point in the third set is a repair of size at most2. Otherwise the three sets are pairwise disjoint. Their one-point-per-set triples are different candidate repairs; at most one can equal the sole possible negative triple. Failure would therefore require each remaining set to have size1. Since each original positive set has size4 and |F_g|≤3, all three original sets would contain the same three forbidden points. Their positive repeated-incidence surplus would then be at least3·(3−1)=6, contradicting the seven-degree center budget5 on24 vertices.

For n_1(g)=q≤2 and three positive sets, the same argument gives a precise sufficient pair-repair test. After singleton deletion, suppose two sets have intersection X and the third is W. A nonempty common intersection gives a one-point repair. Otherwise X and W are disjoint and all |X||W| pairs are two-point transversals. If

|X||W| > floor((28−9q)/4),

one of these pairs is not negative and repairs H. This does not settle the smaller-intersection or pairwise-disjoint cases. In particular it does not prove the existence of a center with at most two positive sets.

The independent replay also checks the three local red-part coefficient minima and the four integer q inequalities. These are small arithmetic checks of the displayed direct proof, without a solver or an expanded lock inventory.

## 4. Independent verification of the proposed all-j action count

Classify each original edge other than G by (r,s,t), counting G points, red exterior points and blue exterior points. Then r+s+t=5, 1≤t≤4 and 1≤r+s≤4. Let N_rst denote the number of such edges; c=N_104.

Choose any g∈G and any j-element subset J⊆L. Flip g blue and all points of J red. There are5 binom(b,j) actions.

A newly blue bad edge must be a type(1,0,4) edge whose singleton G vertex is the chosen g, and all its four blue vertices must avoid J. Its total action incidence is binom(b−4,j). A newly red bad edge of type(r,s,t) requires the chosen g to avoid that edge and all its t blue vertices to lie in J. Its incidence is (5−r)binom(b−t,j−t). All other edges remain proper or are included in these cases; G itself becomes proper. Therefore if every action fails, the union bound gives, for every j=0,…,b,

c binom(b−4,j)+Σ_(r,s,t) (5−r)binom(b−t,j−t)N_rst ≥5 binom(b,j).

Binomial coefficients outside their natural range are zero. In particular j=0 gives c≥5. Independent Bernoulli selection gives the corresponding necessary polynomial inequality for every p∈[0,1]:

c(1−p)^4+Σ_(r,s,t)(5−r)N_rst p^t ≥5.

These counts use all five choices of g, irrespective of their degrees; the seven-degree restriction enters the small positive-family lemma, not this action count.

## 5. Bounded aggregate diagnostic and its exact limitation

The diagnostic used only14 possible (r,s,t) types, not a hypergraph enumeration or a free-lock inventory. For each actual parameter range in §1 and every a=1,…,n−6, it imposed:

- ΣN=M−1 and ΣrN=d(G)−5;
- ΣsN≥7a and ΣtN≥7b;
- all five pair-cover moments: ΣrsN≥5a, ΣrtN≥5b, Σbinom(s,2)N≥binom(a,2), ΣstN≥ab, Σbinom(t,2)N≥binom(b,2);
- every integer-j action inequality from §4;
- even-cut lower bounds Σu(5−u)N≥2ceil(k(n−k)/2), for (u,k)=(r,5),(s,a),(t,b).

The even-cut strengthening is valid because each five-edge contributes an even cut size u(5−u), while pair coverage requires at least k(n−k) crossing incidences.

Choose the initial proper coloring of H−G with G red to minimize |5+a−b|. If b−(5+a)≥2, every blue exterior vertex must have a red-creating singleton blocker, giving Σ_(t=1)N≥b. If (5+a)−b≥2, every red exterior vertex must have a blue-creating zero-G edge with one red exterior point, giving N_014≥a. For n=23 a gap of1 only reverses the majority under a flip and does not improve this potential, so no corresponding unsupported constraint was imposed. For even n=24 every strict gap is at least2.

The full173 small real LPs, including parity cuts, ran in0.073 seconds. They returned38 feasible models:2/18 for(n,M)=(24,34),6/36 for(24,35),12/51 for(23,34),18/68 for(23,35). Solver-reported infeasibility has **not** been converted to exact dual certificates and is not used to exclude any branch. One feasible rational vertex was recovered by exact Gaussian elimination and all its inequalities were replayed with rational arithmetic.

There is also a short integer count witness at n=24,M=34,d(G)=35,a=7,b=12:

| (r,s,t) | N |
|---|---:|
|(0,2,3)|5|
|(0,4,1)|1|
|(1,0,4)|7|
|(1,1,3)|2|
|(1,2,2)|17|
|(4,0,1)|1|

All omitted counts are zero. It satisfies every aggregate constraint listed above and every j=0,…,12 action inequality; j=2 is equality. Its Bernoulli polynomial equals

7−22p+110p²+5p³+35p⁴
=59/10+110(p−1/10)²+5p³+35p⁴ >5.

This is only a count witness. The new actual-center lemma rules it out: all five G vertices have degree7, c=7<10, but N_1=2<4. Thus the aggregate model had omitted a genuine obstruction association.

To check whether this single addition closes the moment domain, only four further tiny integer models were tested: a=7 or8, and the two branches c≥10 or(c≤9,N_1≥4), for n=24,M=34,d(G)=35. They took0.016 seconds. Three returned integer witnesses, all checked exactly. For example the c≥10 branch at a=7 has

N_032=3, N_104=10, N_113=6, N_122=6, N_131=8.

It satisfies all the same aggregate and parity constraints, every integer-j action inequality, and the new disjunction. This does not assert an actual incidence realization or actual failure for all centers. The one solver-reported infeasible branch is not used as a theorem. No further aggregate LP cuts were pursued.

The independent standard-library replay checks five stored rational/integer witnesses and all496 small-set patterns in0.0053 seconds. It imports neither SciPy nor the LP/construction sources. Exact feasible witnesses suffice to establish the stated limitations; floating infeasibility is not needed.

## 6. A realized singleton obstruction from an actual colorable H

A single center can genuinely be blocked even with pair coverage, δ7 and a real all-seven G. `CRITICAL_SMALL_BLOCKERS_PILOT.json` contains all35 distinct five-edges on vertices0,…,23. The deterministic construction is24 affine lines not passing through point24 of AG(2,5), six completed four-point punctured lines, and five further five-edges. Direct replay checks simplicity, all pair coverage and degree sequence7^17 8^7.

Take

G={6,8,15,19,21},

and initially red points

{2,6,7,8,9,10,11,13,15,16,17,19,20,21,22}.

All five G degrees are7 and G is the only bad edge. At g=6 the sole positive set is A={0,1,12,18}. The following actual edges avoid6 and forbid its four individual points:

| Blue part | Actual edge |
|---|---|
|{0}|{0,8,11,19,22}|
|{1}|{1,2,8,10,17}|
|{12}|{2,7,12,17,22}|
|{18}|{2,9,11,18,20}|

Their remaining four points are initially red. Consequently no one-direction repair at center6 exists, regardless of the probability distribution used to hit A. The exact signed-transversal search confirms this.

This H is colorable: at each of the other four G centers there are no positive edges, and flipping that center alone suffices. In particular remove8 from the displayed red set for an explicit proper coloring. No criticality or non-B claim is made for this H. Its initial coloring is also not asserted to minimize the balance potential. The example rejects an arbitrary-center repair theorem under the local degree/pair-cover hypotheses; it does not reject an existential good-center theorem or the stronger critical/extremal-coloring hypotheses.

## 7. Reproduction and remaining obligation

The direct deterministic replays are:

```sh
python3 context/propertyb35-paper/round01/twentyfive/CRITICAL_SMALL_BLOCKERS_REPLAY.py
python3 context/propertyb35-paper/round01/twentyfive/CRITICAL_SMALL_BLOCKERS_INTEGER_REPLAY.py
```

The original bounded diagnostics use `.tools/math-python/bin/python` for SciPy. `ACTION_LP.py/json`, `ACTION_PARITY_LP.py/json`, and `CENTER_BRANCH.py/json` record the scopes, models, measured costs and exact feasible supports. `PILOT.py/json` records the actual construction and initial-state search. The independent replay reads its saved actual edges, not its construction code.

The proved advances are the small-blocker lemma in §2, its actual-center consequence in §3, and the one-red-exterior repair lemma in §3a. The decisive unresolved task is to exploit the same original singleton/pair edges across multiple centers, or an extremal proper coloring of H−G, to rule out all their exact obstruction graphs. The currently available total-degree and pair-cover moments do not prove that. No complete23/24 branch or new global lower bound is claimed here.

# Local check of the successful Gemini response

2026-10-15. Read only GEMINI_RESPONSE.md as the mathematical input. This is a same-family local check of a cross-family response, not a full theorem/Lean audit or a proof of the new Property B bound. No MCP call or build was performed.

## Verdict and actual scope

The response gives a valid proof of the following selection lemma: every pair-covering simple five-uniform hypergraph with 25 vertices and 35 edges contains nine vertices of degrees six or seven such that all pair codegrees are one except for a matching of pairs with codegree two. The accompanying affine-plane construction validly disproves the stronger demand for nine vertices with every pair codegree one. Neither conclusion by itself proves two-colourability.

## Detailed mathematical check

Write r=n_6, t=n_7, and w(x,y)=lambda(x,y)-1. Pair coverage gives w>=0 and 4d(x)>=24, hence minimum degree six. The identity sum_y w(x,y)=4(d(x)-6) holds because every incident five-edge contributes four partners. A degree-six vertex therefore has w=0 to every other vertex. Total degree 175 gives n_{>=8}<=r, and therefore t>=25-2r. All these statements use actual incidences, not an assumed degree profile.

The graph G on the degree-seven vertices has positive w as adjacency, with weighted degree at most four inside G. Choose a **maximum** independent set I, of size a; mere maximality would not suffice for the class-clique argument. Maximality implies every exterior vertex meets I. Since the total weight leaving I is at most 4a, splitting exterior vertices by weight one versus at least two gives |R_1|>=2t-6a. The response's inequality direction is correct: weights to vertices outside the degree-seven set can only reduce the available 4a budget.

Each x in R_1 has a unique I-neighbour u, and w(x,u)=1. Thus R_1 partitions into the classes C_u. If two vertices of C_u were nonadjacent, replacing u by those two vertices would enlarge I; no other I-adjacencies occur. Consequently C_u is a clique.

For x in C_u, its full weighted-degree budget four pays at least one unit for u, |C_u|-1 for its classmates, and one unit for every neighbour outside C_u in R_1. These are disjoint vertex sets, so

\[
|C_u|+|N_G(x)\cap(R_1\setminus C_u)|\le4.
\]

The greedy step chooses x, deletes its entire class and its external R_1-neighbours, and hence removes at most four **currently available** vertices. Previously removed vertices do not increase that number. Exhaustion yields a set B of size at least ceil(|R_1|/4), independent in G, with at most one selected vertex per class. This last condition ensures that the positive-weight pairs between I and B form a matching; their weights are exactly one. No positive-weight pair occurs inside I or B. The degree-six set adds no positive-weight pairs. Taking a nine-element subset preserves the matching property.

The ceiling manipulations in the response are correct. In its residual case, r+a<=8 implies a<=8, and

\[
|U|\ge r+a+\left\lceil\frac{50-4r-6a}{4}\right\rceil
=\left\lceil\frac{25-a}{2}\right\rceil\ge9.
\]

The early cases r>=9 and r+a>=9 are also legitimate: they provide enough vertices with all codegrees one. They do not require the residual argument.

## Sharper size statement

The R_1/class/greedy construction is valid for **every** maximum independent set I, without the residual assumption r+a<=8. Even when 2t-6a is nonpositive, the resulting lower bound remains valid (it may simply be weak). Therefore the same construction gives

\[
|U|\ge r+a+\left\lceil\frac{2t-6a}{4}\right\rceil
=r+\left\lceil\frac{t-a}{2}\right\rceil
\ge\left\lceil\frac{25-a}{2}\right\rceil.
\]

In addition |U|>=r+a always, since it contains V_6 and I. Thus the stronger combined bound is the maximum of these two lower bounds. The identity moving a inside the ceiling uses that a is an integer. The last inequality uses t>=25-2r and that r is an integer.

In particular, if a<=6 then |U|>=10, even if the response would have stopped in its early r+a>=9 branch: one can continue the construction instead. If r=0 and a=5 or 6, this supplies ten **degree-seven** vertices with excess-codegree support a matching. This does not establish a universal ten-vertex assertion: for instance the present argument only guarantees nine when r=0,a=7 or 8. No claim of impossibility in those cases is made.

## Affine-plane counterexample

AG(2,5) has 25 points and 30 distinct five-point affine lines (six directions, five parallel lines per direction), and every pair of distinct points lies on exactly one line. The five sets f_i={(x,x^2+i):x in F_5} are disjoint, each has five points, and together partition the plane. A vertical line meets f_i once; a nonvertical line meets it at the roots of a degree-two polynomial and hence at most twice. Thus no f_i is a line, and adding them gives exactly 35 distinct five-edges.

Every point lies on six lines and one f_i, so all degrees are seven. Two distinct points acquire exactly one extra common edge precisely when they lie in the same f_i. The support graph is therefore five disjoint copies of K_5, each with edge weight one. A set with all codegrees one takes at most one point from each part, so has size at most five. This proves the response's claimed counterexample to the stronger all-unit assertion. It also illustrates the sharper construction: selecting two points from each f_i gives ten vertices whose excess support is a matching.

No missing mathematical assumption or invalid counting step was found in the response's stated local conclusions. Its title “original proposition” must be read as the nine-lock selection lemma under discussion, not as the complete Property B conjecture or any completed Lean result.

## Addendum: all-degree-seven branch and equality rigidity

Suppose r=0. Since t>=25-2r and there are exactly 25 vertices, every vertex has degree seven. The support graph G has maximum degree at most four, so greedy independent-set selection gives a=alpha(G)>=ceil(25/5)=5. Applying the established construction and, when necessary, taking a smaller B gives these exact available lock patterns:

| Maximum independent-set size a | Selected locks | Positive-weight pairs |
|---:|---:|---:|
| a>=9 | 9 from I | 0 |
| 8 | 8 from I, 1 from B | exactly 1 matching pair |
| 7 | 7 from I, 2 from B | exactly 2 matching pairs |
| 6 | 6 from I, 4 from B | exactly 4 matching pairs |
| 5 | 5 from I, 5 from B | exactly 5 matching pairs |

The B-size guarantees follow from |R_1|>=50-6a: these lower bounds are respectively 2,8,14,20 for a=8,7,6,5, and their ceilings after division by four are 1,2,4,5. “Exactly” is justified because each selected B vertex has one distinct owner in I and cross weight exactly one; there are no other positive-weight pairs among the selected vertices. Thus the positive-codegree pairs all have lambda=2, and all other pairs have lambda=1.

For a=5 one gets actual rigidity of the entire weighted support graph. There are 20 vertices outside I, each contributes at least one to w(x,I), while the total cross weight is at most 4a=20. Equality forces all 20 exterior vertices into R_1 and gives each of them exactly one unit-weight edge to I. Every owner has weighted degree four, so its class C_u has at most four vertices. The five classes partition 20 vertices; hence each has exactly four. The maximum-independent-set exchange argument makes C_u a clique. For x in C_u, the edge to its owner and its three classmates already consume the full weighted-degree budget four. Every one of those four weights is therefore one, and x has no other support neighbour. The owner also exhausts its budget on its four class vertices. Consequently G is exactly a disjoint union of five K_5 components, with every support weight one.

This identifies the **codegree-excess graph**, not the complete hypergraph H. It does not assert that H must be the affine-line-plus-parabola construction. That construction is one realization of the same weighted-support pattern.

# Property B: an exact-arithmetic proof certificate for m(7) >= 130

## Theorem

Every finite simple 7-uniform hypergraph with at most 129 edges admits a two-coloring with no monochromatic edge. Consequently **m(7) >= 130**.

This is a **computer-assisted, rational-arithmetic** proof: the structural lemmas below are mathematical, and the accompanying standalone Python file `propertyB_m7_certificate.py` checks all 115 required exact rational inequalities. The bounds and proofs have not been independently Lean-verified.

## 1. Reduction

Suppose a counterexample with at most 129 edges exists. Choose one on the smallest possible number of vertices, v. Any two distinct vertices must lie in a common edge: otherwise identifying them preserves 7-uniformity and non-2-colorability, contradicting minimality. Write `d(x)` for vertex degree and `lambda_xy` for codegree. Thus

\[
\lambda_{xy}\ge1,\quad 6d(x)=\sum_{y\ne x}\lambda_{xy}\ge v-1,\quad\sum_xd(x)=7m\le903.
\]

In particular \(v\lceil(v-1)/6\rceil\le903\), excluding \(v\ge74\). For \(v\le12\) choose two color classes of size at most 6. For \(13\le v\le36\), a uniformly selected balanced red class makes a given 7-edge monochromatic with probability

\[
p_v={\binom{\lfloor v/2\rfloor}7+\binom{\lceil v/2\rceil}7\over\binom v7}.
\]

An exact finite check gives \(129p_v<1\) throughout this range (its maximal value is \(1677/1705\), attained at \(v=35,36\)). Thus \(37\le v\le73\). Add distinct edges on the same vertex set to obtain exactly 129 edges while preserving non-colorability and pair coverage, which is possible since \(\binom v7\ge129\). Henceforth \(m=129\), \(\sum_xd(x)=903\).

## 2. Random greedy coloring and its failure witnesses

Take a permutation of the vertices. Initially color all vertices red. Upon processing vertex `x`, recolor it blue if there is a currently all-red edge whose last (in permutation order) vertex is `x`; otherwise leave it red. The final coloring has no all-red edge. If there is an all-blue edge `B`, take its earliest vertex `x`. Its recoloring has an all-red witness `A` with

\[
 A\cap B=\{x\},\qquad\max_\sigma A=x=\min_\sigma B.
\]

Such a **critical ordered pair** is a necessary condition for failure.

Fix distinct locked vertices \(s_1,\ldots,s_t\) and distinct prescribed permutation positions \(p_1,\ldots,p_t\). Uniformly permute the other \(N=v-t\) vertices. Let \(\ell_T\) be the number of edges whose intersection with the locked set is **exactly** the index set \(T\subseteq[t]\), and set \(r_T=7-|T|\). For a position \(h\), let \(a_h,b_h\) be the number of unlocked positions before and after \(h\). Let \(I_h^-\) and \(I_h^+\) be the locked indices occurring before and after \(h\).

For a free position `h`, a fixed edge of type `T` ends there with probability

\[
 E_h^-(T)={r_T\over N}{\binom{a_h}{r_T-1}\over\binom{N-1}{r_T-1}},\qquad T\subseteq I_h^-,\ r_T\ge1,
\]

and begins there with \(E_h^+(T)=(r_T/N)\binom{b_h}{r_T-1}/\binom{N-1}{r_T-1}\) if \(T\subseteq I_h^+\), otherwise zero. For a locked position \(h=p_j\), the ending probability is

\[
 E_h^-(T)={\binom{a_h}{r_T}\over\binom N{r_T}}
\]

provided \(j\in T\) and \(T\setminus\{j\}\subseteq I_h^-\); beginnings are symmetric with \(b_h,I_h^+\). Define

\[
A_h=\sum_T\ell_T E_h^-(T),\qquad B_h=\sum_T\ell_T E_h^+(T).
\]

For a **fixed distinct ordered pair of 7-edges that intersect exactly in their common critical vertex**, the exact probability to form a critical pair at free position \(h\) is

\[
w_h(T,U)={\binom{a_h}{r_T-1}\binom{b_h}{r_U-1}\over N\binom{N-1}{r_T-1}\binom{N-r_T}{r_U-1}},
\]

provided \(T\subseteq I_h^-\), \(U\subseteq I_h^+\), \(r_T,r_U\ge1\), and \(r_T+r_U-1\le N\). For a locked critical position \(h=p_j\), it is

\[
w_h(T,U)={\binom{a_h}{r_T}\binom{b_h}{r_U}\over\binom N{r_T}\binom{N-r_T}{r_U}},
\]

provided \(T\cap U=\{j\}\), \(T\setminus\{j\}\subseteq I_h^-\), \(U\setminus\{j\}\subseteq I_h^+\), and \(r_T+r_U\le N\). Other cases have weight zero. Empty/infeasible binomial terms likewise give zero; denominators are evaluated only in feasible cases.

The total number of **distinct ordered edge pairs of types (T,U)** is \(\ell_T(\ell_U-\mathbf1_{T=U})\). Even though most pairs need not be single-intersection pairs, a valid coarse bound is

\[
C_h=\sum_{T,U}\ell_T(\ell_U-\mathbf1_{T=U})w_h(T,U).
\]

Thus \(\Pr(Q_h)\le\min\{A_h,B_h,C_h\}\), where \(Q_h\) is the existence of a critical pair at position \(h\).

### Link-pair deletion

Every locked center \(u\) of degree \(d(u)\) has at least

\[
q_u=\left\lceil{6d(u)-(v-1)\over5}\right\rceil
\]

**distinct unordered pairs** of incident edges having an additional common vertex. Indeed,

\[
\sum_{w\ne u}\binom{\lambda_{uw}}2\ge\sum_{w\ne u}(\lambda_{uw}-1)=6d(u)-(v-1),
\]

and two distinct incident 7-edges have at most 5 other common vertices. None of these unordered pairs can be a critical pair in either direction.

For each unordered type pair \(\{T,U\}\) where both contain the center's locked index, the number of unordered edge pairs in that cell is \(\binom{\ell_T}{2}\) if \(T=U\) and \(\ell_T\ell_U\) otherwise. Each carries the *coarse accounting* weight \(w_h(T,U)+w_h(U,T)\ge0\). Fill the type cells from smallest weight upward until \(q_u\) distinct unordered pairs have been counted; call the resulting weight \(D_h\). Every actual set of \(q_u\) bad incident edge pairs has combined weight at least \(D_h\), so subtracting \(D_h\) is valid even when some cells have zero weight. We set \(D_h=0\) at free positions.

Therefore the rigorous failure upper bound is

\[
\boxed{\Pr(\mathrm{Fail})\le U(v,p,\ell):=\sum_{h=1}^v\min\{A_h,B_h,C_h-D_h\}.}
\tag{1}
\]

All entries are exact rational values. When no vertices are locked, one can instead bound the total number of critical ordered pairs using the global overlap lemma: there are at least

\[
Q_v=\left\lceil\frac{129\binom72-\binom v2}{\binom62}\right\rceil
\]

unordered edge pairs with intersection size at least 2. Consequently the number of admissible ordered pairs is at most \(129\cdot128-2Q_v\). The no-lock positionwise bound uses

\[
A_h={903\over v}{\binom{h-1}6\over\binom{v-1}6},\quad
B_h={903\over v}{\binom{v-h}6\over\binom{v-1}6},\quad
C_h=(129\cdot128-2Q_v){\binom{h-1}6\binom{v-h}6\over v\binom{v-1}6\binom{v-7}6}.
\tag{2}
\]

## 3. Choice of locks for the 37 remaining vertex counts

### Case I: 37 <= v <= 56

Use no locks and evaluate (2). All twenty values of (1) are strictly below 1. The largest is

\[
U(56)=\frac{174761}{175175}<1.
\]

### Case II: 57 <= v <= 61

Choose a minimum-degree vertex `x` and lock it at \(\lfloor v/2\rfloor\). Its degree lies in

\[
\left\lceil{v-1\over6}\right\rceil\le d(x)\le\left\lfloor{903\over v}\right\rfloor.
\]

The only types are \(\ell_\varnothing=129-d(x)\), \(\ell_x=d(x)\). Exactly 29 degree profiles arise across these five values of \(v\); after link deletion each gives (1) strictly below 1. The largest is

\[
U(61,d=14)=\frac{500653147237}{501489685620}<1.
\]

### Case III: 62 <= v <= 70

Choose a minimum-degree vertex `x`, of degree `d`. Its codegree surplus is

\[
e=6d-(v-1)\ge0.
\]

At most `e` other vertices have codegree at least 2 with `x`; hence at least

\[
s=v-1-e=2(v-1)-6d
\]

vertices satisfy \(\lambda_{xy}=1\). Let `B` be the smallest integer \(B\ge d\) satisfying

\[
vd+s(B+1-d)>903.\tag{3}
\]

If every codegree-one neighbor `y` had degree at least `B+1`, then the total degree sum would be at least the left-hand side in (3), contradicting its value 903. Thus a codegree-one neighbor `y` exists with

\[
d\le d(y)\le B.
\]

There are no hidden assumptions about regularity. For each \(v,d\), the exact permissible degree range of `y` is calculated by (3). The following table gives all `d -> B` possibilities:

| v | d -> B |
|---:|---|
|62|11→14, 12→15, 13→15, 14→14|
|63|11→14, 12→14, 13→14, 14→14|
|64|11→14, 12→14, 13→14, 14→14|
|65|11→14, 12→14, 13→14|
|66|11→13, 12→13, 13→13|
|67|11→13, 12→13, 13→13|
|68|12→13, 13→13|
|69|12→13, 13→13|
|70|12→12|

Lock `x,y` at \((\lfloor v/2\rfloor,\lfloor v/2\rfloor+1)\). Since \(\lambda_{xy}=1\), the exact types are

\[
\ell_{xy}=1,\quad\ell_x=d-1,\quad\ell_y=d(y)-1,\quad\ell_\varnothing=130-d-d(y).
\]

The table produces **60** rational profiles. Every one gives \(U<1\). The largest is

\[
U(70,12,12)=\frac{96528412797259}{96675167749160}<1.
\]

### Case IV: 71 <= v <= 73

Each vertex has degree at least 12. Let \(r\) be the number of 12-degree vertices. Since any other vertex has degree at least 13,

\[
903\ge12r+13(v-r)=13v-r
\quad\Longrightarrow\quad r\ge13v-903.
\]

For \(v=71,72,73\), respectively, this gives \(r\ge20,33,46\). A 12-degree vertex `x` satisfies

\[
\sum_{y\ne x}(\lambda_{xy}-1)=72-(v-1)=73-v\in\{2,1,0\}.
\]

Construct an auxiliary graph on these `r` degree-12 vertices, joining pairs of codegree >= 2. Its maximum degree is at most \(73-v\), hence its independence number is at least \(\lceil r/(74-v)\rceil\), which is **at least 3** in all three cases. Thus there exist three degree-12 vertices \(x,y,z\) with all pairwise codegrees 1.

The edges meeting these three locked vertices in at least two vertices are either (a) precisely one `xyz` edge; or (b) three distinct `xy`, `xz`, `yz` edges. In case (a),

\[
\ell_{xyz}=1,\quad\ell_x=\ell_y=\ell_z=11,\quad\ell_\varnothing=95.
\]

In case (b),

\[
\ell_{xy}=\ell_{xz}=\ell_{yz}=1,\quad\ell_x=\ell_y=\ell_z=10,\quad\ell_\varnothing=96.
\]

Lock them at \((\lfloor v/2\rfloor-1,\lfloor v/2\rfloor,\lfloor v/2\rfloor+1)\). All six profiles give \(U<1\), the largest being

\[
U(73,12,12,12,\text{three pair edges})
=\frac{464713722173}{471886430015}<1.
\]

## 4. Rational certificate and conclusion

The standalone attached script checks all profile groups with standard-library `fractions.Fraction`:

| Case | v range | Number of profiles | Maximum U |
|---|---|---:|---|
| No locks | 37–56 | 20 | 174761/175175 |
| One lock | 57–61 | 29 | 500653147237/501489685620 |
| Two locks | 62–70 | 60 | 96528412797259/96675167749160 |
| Three locks | 71–73 | 6 | 464713722173/471886430015 |
| **Total** | **37–73** | **115** | **each < 1** |

Run:

```bash
python3 propertyB_m7_certificate.py
```

This performs exact arithmetic and asserts all 115 bounds strictly below 1; it also checks the balanced-coloring and structural parameter ranges.

For every putative counterexample, one of the four cases gives a locked uniform-permutation distribution with \(\Pr(\mathrm{Fail})<1\). Thus some permutation makes the greedy coloring successful, giving a proper two-coloring. This contradicts the definition of counterexample. Consequently

\[
\boxed{m(7)\ge130.}\qquad\square
\]

### Scope and limitations

* The probability count and exact-arithmetic inequalities have been checked using the included program. The accompanying human proof establishes the reduction and the selection of lockable vertices; the program does not enumerate hypergraphs, and its finite inequality checks are complete only because the selection lemmas cover all possibilities.
* This is a **computer-assisted proof candidate**, not yet an independent formal kernel check or peer-reviewed result. It should be independently audited before submission or publicly claiming a verified record.
* Trying the same 0/1/2/3-lock scheme for 130 edges fails for the 66-vertex degree profiles `(12,14)` and `(13,14)` by narrow margins (approximately `1.0000263` and `1.0000485`); this does not imply that `m(7)>=131` is false, only that the current certificates do not establish it.

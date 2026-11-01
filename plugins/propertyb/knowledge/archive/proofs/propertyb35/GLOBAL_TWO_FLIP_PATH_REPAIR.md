# Global two-flip path repair

**Status: PROVABLE AS STATED.** This is a sufficient criterion for Property B, with necessary moment inequalities for a counterexample. The moment inequalities alone do not close all 21–25-point inputs.

## 1. Counts on the original hypergraph

Let \(H\) be a finite simple \(k\)-uniform hypergraph on \(n\) vertices, where \(k\ge2\), \(n\ge k\), and \(M=|H|\). Choose a red \(a\)-subset uniformly, for a fixed \(0\le a\le n\). All probabilities below concern this initial coloring; the repaired coloring need not have \(a\) red vertices.

Let \(X\) count monochromatic edges. Let \(S\) count the ordered pairs \((G,F)\) for which \(G\cap F=\{g\}\), \(G\) is monochromatic of color \(c\), and \(F\setminus\{g\}\) has color opposite to \(c\). These definitions agree with `GLOBAL_PRIVATE_PAIR_REPAIR.md`.

Define \(Z\) as the number of ordered triples \((G,F,J)\) of distinct original edges satisfying

\[
 G\cap F=\{g\},\quad F\cap J=\{h\},\quad g\ne h,\quad g\notin J,
\]

and having the following initial colors:

\[
 G\text{ is all color }c,\qquad
 F\setminus\{g\}\text{ is all opposite to }c,\qquad
 J\setminus\{h\}\text{ is all color }c.
\]

Both choices of \(c\) are included. No uniqueness condition on the private edge \(F\) is imposed in \(Z\); this intentional enlargement makes its expectation easy to bound.

## 2. The repair algorithm and its pointwise certificate

On an initial coloring, do the following.

If \(X=0\), keep it. If \(X\ge2\), declare failure. Suppose \(X=1\), and let \(G\) be the unique monochromatic edge, of color \(c\). For \(g\in G\), let \(m_g\) be the number of private edges \(F\) appearing with \(G\) in \(S\).

If some \(m_g=0\), flip \(g\), which repairs the input by the single-flip argument. Otherwise, for every \(g\) with \(m_g=1\), let \(F_g\) be its unique private edge and try every simultaneous flip of \(g\) and \(h\in F_g\setminus\{g\}\). Keep any proper resulting coloring. Declare failure if all such trials fail.

Here is a complete classification of the possible newly monochromatic edges in such a trial. Initially \(g\) has color \(c\), while \(h\) has the opposite color. An edge containing both remains bichromatic after the two flips. An edge containing neither is unchanged. A newly monochromatic edge of color opposite to \(c\) must contain \(g\), avoid \(h\), and initially be private at \(g\). But the unique such private edge is \(F_g\), which contains \(h\), so this case is impossible. Thus every new bad edge is of color \(c\), contains \(h\), avoids \(g\), and initially has \(h\) as its unique vertex of the opposite color.

The original bad edge \(G\) becomes proper, since \(h\notin G\) and \(k\ge2\). The edge \(F_g\) also becomes proper: its flipped vertices \(g,h\) have opposite colors after the trial. Hence, if a trial fails, there is an original edge \(J\) as in the last case. All of \(F_g\setminus\{g,h\}\) have the initial color of \(h\), whereas all of \(J\setminus\{h\}\) have the other color. Together with \(g\notin J\), this proves \(F_g\cap J=\{h\}\). The failure therefore supplies a triple counted by \(Z\).

On a failed coloring with \(X=1\), all \(m_g\ge1\) and

\[
 S=\sum_{g\in G}m_g.
\]

If \(u\) of these \(k\) multiplicities equal one, then \(S\ge u+2(k-u)\), so \(u\ge(2k-S)_+\). Each of the \(k-1\) choices of \(h\) at each such \(g\) supplies a distinct triple. Different \(g\) have different private edges, because those edges meet \(G\) at different singletons. For fixed \(g\), different \(h\) cannot give the same triple, since \(F_g\cap J=\{h\}\). Consequently

\[
 Z\ge(k-1)(2k-S)_+.
\]

Writing \(I_2\) for the indicator that this algorithm fails, we obtain the pointwise bound

\[
 \boxed{\quad I_2\le\frac X2+
 \frac{S+Z/(k-1)}{4k}.\quad}
\]

Indeed, a failure with \(X=1\) has \(S+Z/(k-1)\ge2k\); a failure with \(X\ge2\) is already paid for by \(X/2\). All terms are nonnegative on successful inputs.

**Expectation criterion.** It follows that

\[
 \boxed{\quad
 \mathbb EX+\frac{\mathbb ES+\mathbb EZ/(k-1)}{2k}<2
 \quad\Longrightarrow\quad H\text{ has Property B}.
 \quad}
\]

This is an algorithm on colorings of the original \(H\). It assumes no criticality or prescribed deleted-hypergraph coloring.

## 3. Exact path expectation and degree upper bounds

For distinct outer edges \(G,J\), let \(c(G,J)\) count the original middle edges \(F\) such that \(F\cap G=\{g\}\), \(F\cap J=\{h\}\), with \(g\ne h\). In particular, \(g\in G\setminus J\), \(h\in J\setminus G\). This middle-edge count is symmetric in its two outer edges.

For \(0\le j\le k-1\), let \(n_j\) count unordered distinct outer edge pairs with intersection size \(j\), and put

\[
 C_j=\sum_{\substack{\{G,J\}\subset H\\|G\cap J|=j}}c(G,J).
\]

Use the convention that invalid binomial coefficients vanish, and define

\[
 p=\frac{\binom{n-k}{a-k}+\binom{n-k}{a}}{\binom na},\quad
 q=\frac{\binom{n-2k+1}{a-k}+\binom{n-2k+1}{a-k+1}}{\binom na},
\]

\[
 r_j=\frac{
 \binom{n-3k+2+j}{a-2k+1+j}+
 \binom{n-3k+2+j}{a-k+1}}
 {\binom na}.
\]

For a fixed ordered triple with outer intersection size \(j\), the prescribed color-\(c\) set is \(G\cup(J\setminus\{h\})\), of size \(2k-1-j\). The opposite-color set is \(F\setminus\{g\}\), of size \(k-1\). They are disjoint. Their union has size \(3k-2-j\). Counting both choices of \(c\) gives exactly \(r_j\). Since each unordered outer pair has two orientations,

\[
 \mathbb EX=Mp,\qquad \mathbb ES=2n_1q,\qquad
 \boxed{\quad\mathbb EZ=2\sum_{j=0}^{k-1}C_jr_j.\quad}
\]

Suppose \(M\ge2\) and the maximum original vertex degree is \(\Delta\). Every candidate middle edge is distinct from both outer edges. It meets \(G\setminus J\) in exactly one vertex, so it is counted exactly once in the relevant sum of degrees after excluding \(G\). The symmetric statement holds on \(J\setminus G\). Hence

\[
 c(G,J)\le\min\left\{
 M-2,\ \sum_{v\in G\setminus J}(d_v-1),\
 \sum_{v\in J\setminus G}(d_v-1)\right\}
 \le c_j:=\min\{M-2,(k-j)(\Delta-1)\}.
\]

Thus \(C_j\le n_jc_j\). A readily computable sufficient criterion is

\[
 \boxed{\quad
 Mp+\frac{n_1q}{k}
 +\frac{\sum_{j=0}^{k-1}n_jc_jr_j}{k(k-1)}<2.
 \quad}
\]

The exact \(C_j\), or the pointwise degree-sum bounds, may replace the coarser \(n_jc_j\). The cases \(M=0,1\) are trivially colorable for \(k\ge2\).

## 4. Five-uniform specialization at 21 and 22 points

Set \(k=5,M=35,a=\lfloor n/2\rfloor\), and assume \(n=21\) or \(22\), with \(\Delta\le9\). With \(D=352716\), both point counts have

\[
 p=2/57,\quad q=1716/D,\quad
 (r_0,r_1,r_2,r_3,r_4)=(36,120,330,792,1716)/D,
\]

\[
 (c_0,c_1,c_2,c_3,c_4)=(33,32,24,16,8).
\]

At 22 points the ordinary balanced-color denominator is \(705432=2D\), with each displayed numerator doubled; the probabilities are unchanged. The sufficient criterion becomes

\[
 \boxed{\quad
 L:=594n_0+5352n_1+3960n_2+6336n_3+6864n_4
 <2722720.
 \quad}
\]

Therefore a non-B input in this range necessarily has \(L\ge2722720\).

For the 21-point A1 spectrum \(6,7,8^9,9^{10}\), point-pair coverage gives

\[
 \sum_jn_j=595,\quad W=648,\quad T=140+\tau,
 \qquad \tau=\sum_{v<w}\binom{\lambda_{vw}-1}{2}\ge0.
\]

The exact substitutions are

\[
 n_1=368-2\tau+3n_3+8n_4,\quad
 n_2=140+\tau-3n_3-6n_4,\quad
 n_0=87+\tau-n_3-3n_4.
\]

Consequently

\[
 L=2575614+9918n_3+24138n_4-6150\tau.
\]

Every A1 non-B input must therefore satisfy

\[
 \boxed{\quad9918n_3+24138n_4-6150\tau\ge147106.\quad}
\]

Since the left side is a multiple of six, its equivalent integer lower bound is \(147108\). This is a weighted mixed-intersection condition; no separate disjunction on \(n_3\) and \(n_4\) is asserted.

The abstract integer PSD distribution \((78,397,110,9,1)\) that survived the one-flip moment relaxation has \(L=2670564<2722720\). It is therefore excluded by this two-flip necessary condition. This statement concerns an abstract distribution, not a previously constructed hypergraph.

## 5. Finite evidence and remaining scope

The exact check and diagnostic are in

`context/propertyb35-paper/round01/middle/global_private_pair_moments_20261020/two_flip_path_20261020/`.

`CHECK.py` checks all local proper-edge color types for \(k=2,\ldots,6\), bounded private-multiplicity vectors, the exact 21/22/23 arithmetic, and explicit feasible moment/PSD distributions. The proof in §§1–3 is general and does not rely on the bounded color-type check.

The strengthened moment relaxation remains feasible for A1 and for the diagnostic parameters \(n=23,\Delta\le8,W=581,T\ge97\). Thus these criteria provide actual sufficient coloring conditions and stronger necessary counterexample structure; they do not yet prove either full original branch.

## 6. Shared middle-edge capacity for the reduced A1 role

The following refinement uses actual shared incidences rather than independently assigning the largest middle-edge capacity to every outer pair.

### 6.1 Singleton outer intersections

For a vertex \(w\), let \(t_w\) be the number of unordered edge pairs whose intersection is exactly \(\{w\}\). Then \(\sum_wt_w=n_1\) and \(t_w\le\binom{d_w}2\). Any valid middle edge for such an outer pair must avoid \(w\): otherwise both singleton intersections with the outer edges would be \(w\), contrary to the distinct attachment vertices in the path definition. There are only \(M-d_w\) original edges avoiding \(w\). Therefore

\[
 C_1\le\sum_w(M-d_w)t_w=Mn_1-\sum_wd_wt_w.
\]

Let \(W=\sum_w\binom{d_w}2\), \(D_* =\sum_wd_w\binom{d_w}2\), and \(\Delta\) be the maximum degree. Since each \(\binom{d_w}2-t_w\ge0\),

\[
 \sum_wd_wt_w
 =D_*-\sum_wd_w\left(\binom{d_w}2-t_w\right)
 \ge D_*-\Delta(W-n_1).
\]

Thus, generally,

\[
 \boxed{\quad C_1\le(M-\Delta)n_1+\Delta W-D_*.\quad}
\]

For the A1 degree spectrum \(6,7,8^9,9^{10}\),

\[
 W=648,\qquad D_*=6\cdot15+7\cdot21+9\cdot8\cdot28+10\cdot9\cdot36=5493,
\]

so

\[
 \boxed{\quad C_1\le26n_1+339.\quad}
\]

The original bound \(C_1\le32n_1\) remains available as well; one may use the minimum of the two. In particular, the shared bound is stronger throughout the non-B range \(n_1\ge397\).

### 6.2 Four-point outer intersections and the exact strong-pair import

If outer edges meet in four points, write their singleton differences as \(\{u\}\) and \(\{v\}\). Every valid middle edge must contain both \(u,v\), and hence

\[
 c(G,J)\le\lambda_{uv}.
\]

Consequently, under the explicit additional assumption \(\max_{u\ne v}\lambda_{uv}\le4\),

\[
 \boxed{\quad C_4\le4n_4.\quad}
\]

The following is the precise actual-input bridge for the reduced A1 role. Besides its degree spectrum and point-pair coverage, this role has a unique six-degree point \(x\), a unique seven-degree point \(p\), four eight-degree points \(B\) with \(\lambda(x,b)=2\), and unit codegree from \(x\) to every other point. The remaining points have degrees eight or nine.

Section 2 of `context/propertyb35-paper/round01/middle/high_edge_intersection_repair_20261020/REPORT.md` proves the following actual strong-pair coloring cases using the original-hypergraph permutation criterion and fixed local certificates:

| Degree pair | Every listed codegree gives Property B |
|---|---:|
| \(7,8\) | \(4,5,6,7\) |
| \(7,9\) | \(5,6,7\) |
| \(8,8\) | \(5,6,7,8\) |
| \(8,9\) | \(5,6,7,8\) |
| \(9,9\) | \(5,6,7,8,9\) |

These ranges include all possible codegrees above their respective thresholds, since codegree is at most the smaller degree. The fifteen older fixed imports and five \(9,9\) imports have saved independent original-index replay, recorded in that directory's `VERIFY.json` and `RESULT.json`. This is the specific imported local-certificate ingredient; its newer cross-family review is separate.

If an actual reduced-A1 input were non-B, all these coloring cases would be absent. Pairs involving \(x\) already have codegree one or two by its actual role. There is no pair of distinct seven-degree points because \(p\) is unique. Every other degree pair is in the table. Hence every point pair has codegree at most four (and every \(7,8\) pair at most three). This conclusion applies globally, not only to a subsequently selected four-point intersection kernel.

No inference here claims that the A1 degree sequence alone implies the stated \(x\)-role. Without importing that actual role and its strong-pair reductions, the capacity calculation remains valid with \(\max\lambda\le4\) as an explicit hypothesis.

### 6.3 The resulting sufficient criterion and necessary structure

Keep \(C_0\le33n_0\), \(C_2\le24n_2\), \(C_3\le16n_3\), and use the shared \(C_1\) and codegree \(C_4\) bounds. For a 21-point, 35-edge, pair-covering input of the A1 degree spectrum, with \(\max\lambda\le4\), the two-flip criterion proves Property B whenever

\[
 \boxed{\quad
 L'=594n_0+4992n_1+3960n_2+6336n_3+3432n_4+20340
 <2722720.
 \quad}
\]

The constant \(20340=(339\cdot120)/2\) is the contribution of the shared-capacity remainder, so it must not be dropped. Substitution of the same A1 moment identities as in §4 gives

\[
 L'=2463474+8838n_3+17826n_4-5430\tau.
\]

Thus every non-B input in the reduced A1 role necessarily satisfies the stronger mixed condition

\[
 \boxed{\quad8838n_3+17826n_4-5430\tau\ge259246,
 \quad}
\]

or equivalently \(\ge259248\), since the left side is a multiple of six. In particular, it requires at least fifteen edge pairs intersecting in at least three points; if \(n_4=0\), then \(n_3\ge30\), and if \(n_3=0\), then \(n_4\ge15\). These individual statements retain all mixed cases through the boxed inequality.

The same imported high-intersection report additionally proves that, in a remaining non-B reduced-A1 input, the intersection kernel of every four-intersection edge pair avoids both \(x\) and \(p\). This is a separate complete actual repair subcase; the capacity calculation itself does not need it. No analogous exclusion of general three-intersection kernels is asserted.

The exact shared-capacity check is in the earlier evidence directory's `shared_capacity_20261020/CHECK.py`. It verifies the degree moments, all coefficients, the twenty saved strong-pair import ranges and bounds, and the old rational maximum-\(n_1\) PSD witness. That abstract witness, \((17,1664/3,0,0,70/3)\), still has \(L'=2879414\ge2722720\); this strengthening therefore does not by itself contradict the complete edge-intersection moment/PSD relaxation. No new hypergraph or intersection-distribution search was performed for this refinement.
